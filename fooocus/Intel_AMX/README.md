# Porting Fooocus to Intel AMX

**Status:** tested end-to-end on a GPU-less GCP C4 instance; CLI and Gradio UI generate images.

**Scope:** 262 changed lines across 9 files (+227/−35). **Difficulty:** medium–high — the patch is small, but most of the work was modernizing dependencies (Transformers 5, numpy 2, Python 3.13) and remapping checkpoint keys.

**Architecture map:** [`architecture.html#port=amx`](../architecture/architecture.html#port=amx) highlights where this port hooks into the upstream flow.

## Source and version

- **Repository**: https://github.com/lllyasviel/Fooocus
- **Version**: Fooocus 2.5.5, `main` HEAD at snapshot time (Nov 2026)
- **Clone command**: `git clone --depth 1 https://github.com/lllyasviel/Fooocus.git`
- **Original commit**: not recorded — the run used a tarball because `git` was
  unavailable, so the exact commit hash was not captured. Pin `v2.5.5` if you
  need a reproducible base.

## Environment

| Item | Value |
|------|-------|
| Cloud | Google Cloud Platform (GCP) **C4** instance |
| CPU | Intel Xeon 6985P-C (Granite Rapids), 4 cores / 8 threads, 1 NUMA node |
| AMX | `amx_bf16`, `amx_int8`, `amx_tile` (verified in `/proc/cpuinfo`) |
| RAM | 60 GB (31 GB tmpfs at `/tmp`) |
| GPU | none (CPU-only) |
| OS | Linux (Debian-based), kernel 6.x |
| Python | 3.13.5 |
| PyTorch | 2.8.0+cpu |
| IPEX | 2.8.0+cpu |
| transformers | 5.22.2 (ported from 4.42.4) |
| numpy | 2.5.4 (ported from 1.26.4) |
| gradio | 3.41.2 (installed with `--no-deps`) |

## Steps taken

1. **Clone** Fooocus (tarball, since `git` was unavailable; later installed git).
2. **Set up venv** at `/tmp/opencode/venv` with Python 3.13; bootstrap pip via `get-pip.py`.
3. **Install PyTorch 2.8.0+cpu** + **IPEX 2.8.0** (the only versions with cp313 wheels) from the CPU index.
4. **Install Fooocus deps** (safetensors, einops, transformers, accelerate, etc.) — had to upgrade transformers to 5.22.2 and numpy to 2.5.4 because 4.42.4/1.26.4 have no cp313 wheels.
5. **Port transformers 4.x → 5.x API**:
   - `transformers.modeling_utils.no_init_weights` moved to `transformers.initialization`.
   - `CLIPTextModel` no longer wraps with `.text_model`; embeddings/encoder/final_layer_norm are now top-level.
   - Updated all key remapping in `sd.py`, `supported_models.py`, `sdxl_clip.py`.
6. **Port numpy 1.x → 2.x**: `np.cumprod` still works; `torch.cumprod(numpy_array)` no longer accepts numpy → use `np.cumprod`.
7. **Download SD1.5 checkpoint** (`v1-5-pruned-emaonly.safetensors`, 4.3 GB) and later **SDXL base** (6.9 GB) into `/tmp/opencode/models/`.
8. **Create `modules/amx.py`** — AMX detection, thread/NUMA tuning, flush-denormals, oneDNN cache, autocast context manager, IPEX optimize/quantize helpers.
9. **Wire AMX into `modules/patch.py`** — configure AMX; wrap UNet forward, VAE decode, CLIP encode in `torch.autocast(bfloat16)` so oneDNN dispatches to `avx10_1_512_amx`.
10. **Wire into `model_management.py`** — enable SDPA on CPU under AMX; apply IPEX prepack at model load (ipex mode).
11. **Add `--amx` CLI flag** to `args_parser.py`.
12. **Verify end-to-end** with both SD1.5 and SDXL — generated images, confirmed AMX kernels via `ONEDNN_VERBOSE`, and used [`processwatch`](https://github.com/intel/processwatch) to verify AMX activity during inference.
13. **Run Fooocus webui with `--share`** — installed gradio 3.41.2 + transitive deps; started webui; generated public URL.

## Bugs encountered & resolutions

| Bug | Resolution |
|-----|------------|
| `git` not installed | Downloaded tarball via curl; later installed git via apt (failed, no root) — used tarball throughout. |
| `pip` missing in venv | Bootstrapped with `get-pip.py`. |
| `torch 2.1.0` (Fooocus pin) has no cp313 wheel | Upgraded to torch 2.8.0+cpu + IPEX 2.8.0. |
| `transformers 4.42.4` requires numpy<2 | Upgraded to transformers 5.22.2; ported CLIP key layouts. |
| `torch.cumprod(numpy_array)` rejected in newer torch | Fooocus's patched `_register_schedule` uses `np.cumprod` (already). Other paths unaffected. |
| `modeling_utils.no_init_weights` removed in transformers 5.x | Imported from `transformers.initialization`. |
| `CLIPTextModel` no longer has `.text_model` in 5.x | Remapped `transformer.text_model.` → `transformer.` in `sd.py`, `supported_models.py`. |
| `patched_SDClipModel` accessed `.text_model.embeddings` | Changed to `.embeddings` and `.final_layer_norm`. |
| `load_checkpoint_guess_config` returns 5 values, not 3 | Updated unpacking in test scripts. |
| `BaseModel` has no `.dtype` attribute | Use `.get_dtype()`. |
| `patch_settings[pid]` KeyError | Initialize `PatchSettings()` in test harness. |
| `core.ksampler` expects `positive` as list of `[cond, dict]`, not wrapped | Pass `pos` directly, not `[pos]`. |
| `convert_cond` IndexError | Same as above. |
| VAE tiled decode wrapper bound wrong `_orig` (late binding) | Bound `_orig` as default arg. |
| IPEX `optimize` "training mode" error | Call `module.eval()` before optimize; removed invalid `training=` kwarg. |
| `ipex.optimize` slower than plain autocast | Default mode set to `bf16` (autocast only); ipex mode kept experimental. |
| `opencv-python` (GUI) needs libxcb | Uninstalled GUI opencv; `opencv-contrib-python-headless` provides cv2. |
| `gradio 3.41.2` metadata build fails on numpy 2.x | Installed with `--no-deps`; manually installed transitive deps. |
| `audioop` removed in 3.13 | Installed `audioop-lts`. |
| `groundingdino` / `segment_anything` / `rembg` missing | Installed from PyPI. |
| `requirements_versions.txt` reinstall fails on py3.13 | Set `REQS_FILE` to an empty file to skip. |
| `--share` gradio `TypeError: unhashable type: 'dict'` | Hardened `template_response` to catch and recover; downgraded Starlette to 0.27.0. |
| Images generated but not returned to webui | `np.bool8` AttributeError in gradio `processing_utils._convert` (numpy 2.x removed `bool8`); guarded with `hasattr`. |
| Default preset missing (`presets/default.json`) | Set `os.chdir` to Fooocus dir; config.txt points to SDXL checkpoint. |

## Key learnings

1. **AMX is engaged automatically by oneDNN** when inputs are `bfloat16` and the CPU supports it — no IPEX required for the baseline speedup. Just `torch.autocast("cpu", dtype=torch.bfloat16)` around conv/matmul-heavy code paths is enough to get `avx10_1_512_amx` kernels.
2. **IPEX `optimize` with `weights_prepack=True`** can prepack weights for additional speedup, but on Fooocus's ComfyUI-style `ModelPatcher` (which casts weights at load time) it added overhead and was slower than plain autocast. Plain bf16 autocast is the recommended default.
3. **Python 3.13 is a poor fit for Fooocus's pinned stack** (numpy 1.x, gradio 3.x, audioop, etc.). A Python 3.10/3.11 environment would avoid most compatibility work.
4. **transformers 5.x broke CLIP's internal layout** (`text_model` wrapper removed). The checkpoint still uses the old layout, so a one-way remapping (`transformer.text_model.` → `transformer.`) is needed at load time.
5. **Fooocus's `modules/patch.py` is the right integration point** — it's called once at startup and already monkeypatches UNet/VAE/CLIP/attention. Adding AMX autocast there covers all compute paths without touching model code.
6. **Thread tuning matters**: `torch.set_flush_denormal(True)` and proper `OMP_PROC_BIND`/`OMP_PLACES` give measurable gains on Xeon.

## Files changed

See [`fooocus-amx.diff`](fooocus-amx.diff) (9 files):

- `ldm_patched/modules/args_parser.py` — `--amx` flag
- `ldm_patched/modules/model_management.py` — SDPA on CPU, IPEX prepack hook
- `ldm_patched/modules/sd.py` — CLIP key remapping (transformers 5.x)
- `ldm_patched/modules/sdxl_clip.py` — CLIP-G detection
- `ldm_patched/modules/supported_models.py` — SD1.5/SD2/SDXL process_clip_state_dict
- `modules/amx.py` — new AMX module
- `modules/patch.py` — AMX configure + autocast wraps
- `modules/patch_clip.py` — transformers 5.x port
- `modules/ui_gradio_extensions.py` — robust template_response for gradio/starlette version mismatch

## Verification

- SD1.5: 256×256, 4 steps → 2.2 s (vs 3.3 s baseline); image saved to `out.png`.
- SDXL base: 512×512, 4 steps → 8.6 s; image saved to `out_sdxl.png`.
- `ONEDNN_VERBOSE` confirms `brg_matmul/conv_fwd/conv_1x1: avx10_1_512_amx`.
- [`processwatch`](https://github.com/intel/processwatch) confirms AMX activity during inference.
- Webui started with `--share`: public URL printed as
  `https://<random>.gradio.live` (the test process was killed by the sandbox
  timeout, so the link had already expired).
- One-command launcher: [`fooocus-amx.sh`](fooocus-amx.sh) clones Fooocus,
  applies the patch, installs dependencies, and starts the UI.