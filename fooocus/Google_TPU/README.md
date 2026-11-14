# Porting Fooocus (SDXL) to PyTorch's native TPU backend

**Result:** Fooocus 2.5.5 runs its real SDXL pipeline on TPU — Gradio UI, text
encoding, LoRA loading, 30-step sampling with CFG/ADM guidance, previews, VAE
decode and PNG/metadata output — using `torch.device("tpu")` from the native
`torch_tpu` PrivateUse1 backend. No `torch_xla`, no model surgery, no
replacement sampling code.

- Code patch: [`fooocus_tpu_patch.diff`](./fooocus_tpu_patch.diff) — 13 files, +789/−36
- One-command launcher: [`fooocus-tpu.sh`](./fooocus-tpu.sh) — clones `v2.5.5`,
  applies the patch, installs dependencies, and starts the UI
- **Scope:** 825 changed lines. **Difficulty:** high — a new backend path with
  attention, precision, and compilation issues to resolve.
- Tested on: Google Colab Pro, `torch 2.14.1+cpu` + `torch_tpu 0.2.0`,
  `transformers 5.22.1`, Python 3.13.18, one TPU device (16,126 MiB visible
  HBM), 48 GB host RAM, SDXL `juggernautXL_v8Rundiffusion.safetensors` at
  1024×1024 and 1152×896.
- **Architecture map:** [`architecture.html#port=tpu`](../architecture/architecture.html#port=tpu) highlights where this port hooks into the upstream flow.

TPU support is conditional: it is only selected when the running PyTorch build
reports an available `tpu` accelerator. CUDA, MPS, XPU and CPU paths are
unchanged, and classic `torch_xla` is not used.

---

## 0. Step-by-step setup and run (fresh TPU VM)

### 0.1 Prerequisites
1. A Google Colab Pro TPU VM with PyTorch's native backend pre-installed:
   `torch 2.14.1+cpu`, `torch_tpu 0.2.0`, Python 3.13.x.
2. Confirm the backend is visible:
   ```bash
   python -c "import torch; print(torch.accelerator.is_available(), torch.accelerator.current_accelerator())"
   # expect: True tpu
   ```
3. Only one process may own the TPU. Stop any other TPU job first.

### 0.2 Clone Fooocus at the tested tag
```bash
git clone --branch v2.5.5 https://github.com/lllyasviel/Fooocus.git
cd Fooocus
```

### 0.3 Apply the TPU port patch
```bash
git apply --check /path/to/fooocus_tpu_patch.diff   # should print nothing
git apply      /path/to/fooocus_tpu_patch.diff
```
The patch adds 13 files (10 modified + `tpu_debug_nan.py`,
`tpu_full_generate.py`, `tpu_ui_driver.py`) and changes 789 additions and 36
deletions.

### 0.4 Install the TPU-safe dependency set (do NOT run requirements_versions.txt)
```bash
# runtime extras used by sampling / preprocessors
pip install torchsde==0.2.6 trampoline
pip install --no-deps opencv-python-headless

# UI / preprocessor extras imported by webui + async_worker
pip install supervision timm pycocotools addict segment-anything groundingdino-py
pip install onnxruntime rembg

# Gradio 3.41.2 + the FastAPI/Pydantic/websockets versions it expects
pip install --no-deps gradio==3.41.2 gradio-client==0.5.0
pip install fastapi==0.104.1 starlette==0.27.0 pydantic==2.9.2 websockets==11.0.3
pip install ffmpy pydub semantic-version orjson importlib-resources
```
`launch.py` detects TPU and skips `requirements_versions.txt` automatically, so
even if you forget, the CUDA-era pins will not be installed.

Symptoms of a mismatched Gradio web stack:

| Error | Cause |
| --- | --- |
| `TypeError: unhashable type: 'dict'` in `jinja2` | Starlette too new for Gradio 3.41 (`TemplateResponse` argument order changed) |
| `AttributeError: 'FieldInfo' object has no attribute 'in_'` | Pydantic too new for the pinned FastAPI |
| `TypeError: ... create_connection() got an unexpected keyword argument 'extra_headers'` | `websockets` too new for `gradio-client 0.5.0` |
| `ValueError: When localhost is not accessible ...` | Usually a follow-up to one of the above; the health check gets a 500 |

### 0.5 Model assets

The defaults from `presets/default.json` are expected in the usual places:

```
models/checkpoints/juggernautXL_v8Rundiffusion.safetensors
models/loras/sd_xl_offset_example-lora_1.0.safetensors
models/vae_approx/xlvaeapp.pth
models/prompt_expansion/fooocus_expansion/pytorch_model.bin
```

`launch.py` downloads them if they are missing.

### 0.6 Verify the headless pipeline (before touching the UI)
```bash
STEPS=2  python tpu_debug_nan.py       # must print "conditioning finite: True"
STEPS=30 python tpu_full_generate.py   # writes /content/fooocus_tpu_output.png
```
The first command audits every conditioning tensor and the sampled latent for
NaN/Inf; the second runs the real `default_pipeline` path and saves a PNG.

### 0.7 Start the Gradio UI
```bash
python launch.py --disable-analytics --disable-in-browser --port 7860 --share
```
Wait for `Running on public URL: https://...gradio.live` (and
`App started successful.`). Models load in the background; the first request
will also trigger PJRT compilation (~90 s for a new shape).

Useful flags:

- `--attention-pytorch` — explicit SDPA selection (already the TPU default).
- `--always-normal-vram` — keep Fooocus from choosing low-VRAM mode.
- `--disable-xformers` — harmless on TPU (xformers is already disabled).

Do not use `--always-cpu` unless you really want the CPU backend.

### 0.8 (Optional) Drive the UI end to end from the shell
```bash
python tpu_ui_driver.py --steps 8 --image-number 1 --outdir outputs/ui_driver
```
This speaks the websocket queue protocol exactly like a browser and fails if the
Generate chain does not return `process_completed success=True`.

### 0.9 Stop the server
```bash
kill $(cat /tmp/fooocus_ui.pid)   # if launched in the background
```
Avoid `pkill -f launch.py` — it matches the shell that launched it.

---

## 1. Constraints that shaped the port

| Constraint | Consequence |
| --- | --- |
| Backend is **native `torch_tpu`**, not `torch_xla` | Everything uses `torch.device("tpu")`, `torch.accelerator.*`; nothing imports `torch_xla` |
| No CUDA at all | Every `torch.backends.cuda.*`, `torch.cuda.OutOfMemoryError`, `device_type='cuda'` and xformers assumption must be made conditional |
| ~15.7 GiB HBM | SDXL base UNet + text encoders + VAE must run in bf16; the default preset (1152×896) peaks at ~15.0 GiB |
| Python 3.13 / CUDA-era pinned requirements | The repo's `requirements_versions.txt` (numpy 1.x, torch 2.1, gradio 3.41.2) cannot be installed over the TPU stack |
| `transformers 5.x` while Fooocus was written for 4.x | CLIP text/vision construction APIs changed |
| Only one process can own the TPU | All validation is serialized; the UI and test scripts cannot overlap |
| Static-shape compilation | First forward pass per shape pays PJRT compilation; the container has the tier-3 compile cache disabled |

The port therefore follows one rule: **TPU is a conditional backend**. Every
change is inert unless `torch_tpu` reports a `tpu` accelerator, so CUDA / MPS /
XPU / CPU keep their original code paths.

---

## 2. Porting strategy

1. **Detect, don't fork.** A single conservative probe (`_detect_tpu()` in
   `ldm_patched/modules/model_management.py`, mirrored in `launch.py`) drives
   every branch: device, dtype, attention backend, memory accounting, OOM type.
2. **Reuse the existing compute path.** Fooocus's sampler, UNet and VAE are
   untouched. Only the *policy* (device/dtype/attention) and a handful of
   numeric/API incompatibilities changed.
3. **Prefer backend-native kernels.** bf16 everywhere + `F.scaled_dot_product_attention`
   instead of xformers/split/sub-quadratic CUDA kernels.
4. **Fix from the top of the stack down.** Get imports working, then model
   loading, then conditioning, then sampling, then UI plumbing — with a headless
   reproducer at each layer.

---

## 3. Change inventory

### 3.1 Backend detection and memory accounting
`ldm_patched/modules/model_management.py`

- `_detect_tpu()` uses `torch.accelerator.is_available()` +
  `current_accelerator().type == "tpu"`; exposed as `tpu_available` / `is_tpu()`.
- `get_torch_device()` returns `torch.device("tpu")`; `get_torch_device_name()`
  reports it.
- `get_total_memory()` and `get_free_memory()` use
  `torch.accelerator.memory.get_memory_info / memory_allocated / memory_reserved`
  instead of `torch.cuda.mem_get_info`.
- `soft_empty_cache()` calls `torch.accelerator.memory.empty_cache()`.
- `OOM_EXCEPTION` falls back to `torch.OutOfMemoryError` (no `torch.cuda` class).
- `device_supports_non_blocking()` returns `False` on TPU (no async copy
  guarantee), and `cast_to_device()` treats TPU like CUDA for bf16.

### 3.2 Dtype policy
`model_management.py`

- `unet_dtype()` → **bf16**; `text_encoder_dtype()` → **bf16**; `VAE_DTYPE` → **bf16**.
- `unet_manual_cast()` returns `None`: weights already live in the inference
  dtype, so per-op weight casting would only add copies and break the fused bf16
  fast path.
- `should_use_fp16()` returns `False` so no FP16 path is selected.
- The CLIP text **embeddings stay float32** (upstream Fooocus behaviour). With
  `manual_cast` on the text encoder this effectively runs the CLIP text stack in
  fp32, which is small and precision-sensitive; the UNet/VAE stay bf16.

### 3.3 Attention
`ldm_patched/ldm/modules/attention.py`, `sub_quadratic_attention.py`

- TPU forces `optimized_attention = attention_pytorch` (PyTorch SDPA) regardless
  of xformers flags.
- All hard-coded `torch.autocast(device_type='cuda')` calls now use
  `q.device.type` / `query.device.type`.
- `torch.backends.cuda.enable_*_sdp(...)` toggles are skipped on TPU (they only
  affect the CUDA dispatcher).

### 3.4 Numerical / API incompatibilities
| File | Fix |
| --- | --- |
| `ldm_patched/k_diffusion/utils.py` | `tf32_mode()` guards `torch.backends.cuda` / `cudnn` access behind `torch.cuda.is_available()` |
| `ldm_patched/modules/model_sampling.py` | `make_beta_schedule()` returns a NumPy array; wrap with `torch.as_tensor(..., float64)` before `torch.cumprod` |
| `modules/anisotropic.py` | `torch.std_mean(..., correction=1)` hits unimplemented `aten::std_mean.correction`; replaced with mean/variance ops (population std; relative error ~1e-6 at these sizes) |
| `modules/core.py` | bf16 previews and `pytorch_to_numpy()` cast to `.float()` before `.cpu().numpy()` (NumPy has no bf16) |
| `modules/patch.py` | progress/eps bookkeeping casts to float before NumPy; NaN/Inf diagnostics on model output and sampler result |

### 3.5 CLIP under Transformers 5 — the real blocker
`modules/patch_clip.py`

Two independent Transformers 5 issues:

1. `modeling_utils.no_init_weights` moved to `transformers.initialization`;
   imported with a 4.x fallback.
2. **`CLIPTextModel` no longer has a `text_model` submodule.** All SDXL
   checkpoints and Fooocus's converters use keys like
   `cond_stage_model.clip_l.transformer.text_model.encoder.layers.0...`.
   Because the module is created inside `no_init_weights()`,
   `load_state_dict(..., strict=False)` silently loaded *nothing* and every
   parameter kept **uninitialised memory**. On TPU that memory is NaN, so
   `c_crossattn` and `pooled_output` were entirely NaN and every image was black.

   Fix: `_LegacyCLIPTextModelLayout` wraps the Transformers 5 model so the
   encoder is re-exposed as `transformer.text_model`, restoring the exact
   checkpoint parameter names (and LoRA/`state_dict` key maps) without touching
   the loader.

CLIP vision also gets an explicit bf16 dtype on TPU.

#### Why this was porting-induced, not pre-existing

Fooocus 2.5.5 pins `transformers 4.42.4`, where `CLIPTextModel` exposes the
`text_model` submodule and the checkpoint keys match. The TPU image requires
`transformers 5.22.1`, which flattened that layout. On the original stack this
bug does not occur; it was introduced by the dependency upgrade needed for the
port.

The failure was silent for three compounding reasons:

1. The model is constructed inside `no_init_weights()`, so every parameter
   starts as uninitialised memory instead of being randomly initialised.
2. `load_state_dict(..., strict=False)` reports no error when **zero** keys
   match; it simply leaves the parameters untouched.
3. Fooocus does not assert that any keys were loaded, so the model looked
   healthy enough to run.

The result depends on the backend: on TPU the uninitialised memory is NaN,
which propagated through `c_crossattn` and `pooled_output` and produced
all-black images. On CPU or CUDA the same silent mismatch could produce
garbage output or appear to work, which makes this class of bug easy to miss.

This is the general risk when porting versions of dependent libraries: a
version bump can change parameter names or loading semantics without changing
the API surface the application calls. The same Transformers 5 layout change
also hit the Intel AMX port, where it was fixed with checkpoint key remapping.

How it was isolated: disabling `patch_all()` made the custom CLIP path finite,
while the patched Transformers path was all NaN. Random-weight instances of the
same Transformers model were finite, proving the compute path was fine and
pointing at weight loading; `no_init_weights()` plus flattened keys explained
the rest. `tpu_debug_nan.py` now checks the loaded conditioning tensors directly
so this failure cannot pass silently again.

### 3.6 Launcher
`launch.py`

`prepare_environment()` skips `pip install -r requirements_versions.txt` when
the running torch reports TPU. Installing those CUDA-era pins (numpy 1.x,
torch 2.1-era transitive deps) can replace or break the pre-installed TPU
stack. Everything else (model/preset download, arg parsing, `from webui import *`)
is unchanged.

On TPU the launcher also applies two compatibility shims needed to finish the
Gradio UI port on the TPU image (numpy 2.x + Gradio 3.41.2):

- **NumPy 1.x aliases.** The TPU image ships NumPy 2.4.6 (the pinned
  `numpy==1.26.4` is intentionally skipped), but Gradio 3.41's image encoder
  references `np.bool8`, `np.float_` and `np.obj2sctype`, which were removed
  in NumPy 2.0. The launcher restores them (`np.bool_`, `np.float64`,
  `np.dtype(obj).type`) before `webui` is imported, so preview/progress images
  encode instead of raising `AttributeError`.
- **Gradio queue HTTP timeout.** Gradio 3.41's queue worker calls its own
  `/api/predict` endpoint through an internal `httpx.AsyncClient` created in
  `Queue.start()` with httpx's default 5 s read timeout. A generator endpoint
  (Fooocus' Generate chain) only answers once the next yield is ready; on TPU
  the first diffusion step triggers lazy kernel compilation and can take tens
  of seconds, so the worker timed out and closed the browser websocket
  mid-generation. `Queue.start` is wrapped to set
  `queue_client.timeout = httpx.Timeout(None)` after the client is created.

---

## 4. Debug log (symptom → cause → fix)

| # | Symptom | Root cause | Fix |
| --- | --- | --- | --- |
| 1 | Import-time crash enumerating CUDA devices | `torch.cuda.current_device()` on a CUDA-less build | TPU check before CUDA device branch |
| 2 | `AttributeError` in TF32 context manager | `torch.backends.cuda.matmul` unavailable | `torch.cuda.is_available()` guard |
| 3 | `RuntimeError` in attention | `torch.autocast(device_type='cuda')` on TPU | use tensor's device type |
| 4 | `TypeError: cumprod(): argument 'input' must be Tensor` | numpy beta schedule | `torch.as_tensor` |
| 5 | `aten::std_mean.correction` not implemented | anisotropic sharpening filter | manual mean/variance |
| 6 | `TypeError` converting preview/output to NumPy | bf16 has no NumPy dtype | `.float()` before `.cpu().numpy()` |
| 7 | `torch.cuda.OutOfMemoryError` missing | CUDA-only exception type | `getattr(torch, "OutOfMemoryError", Exception)` |
| 8 | Slow/basic attention | xformers unavailable, `attention_basic` selected | force `attention_pytorch` (SDPA) |
| 9 | `pip` downgrades numpy, breaks `torch_tpu` | pinned CUDA-era requirements | skip requirements install on TPU |
| 10 | `ImportError: no_init_weights` | Transformers 5 moved the helper | import from `transformers.initialization` |
| 11 | **Black images / all-NaN conditioning** | Transformers 5 flattened `CLIPTextModel`, `strict=False` loaded zero weights, uninitialised params are NaN | restore `text_model` nesting (`_LegacyCLIPTextModelLayout`) |
| 12 | Gradio server exits before serving | modern FastAPI/Starlette/Pydantic/websockets vs Gradio 3.41.2 | pin `fastapi 0.104.1`, `starlette 0.27.0`, `pydantic 2.9.2`, `websockets 11.0.3` |
| 13 | Browser websocket closes mid-generation (no final image) | Gradio 3.41 queue client uses httpx's default 5 s read timeout; TPU first step takes tens of seconds | wrap `Queue.start` to set `queue_client.timeout = httpx.Timeout(None)` |
| 14 | `AttributeError: np.bool8/np.float_/np.obj2sctype` while encoding preview images | NumPy 2.x removed aliases that Gradio 3.41's `processing_utils._convert` indexes | restore the three aliases in `launch.py` before `webui` import |

Bug 11 is the one that mattered for correctness. It was localized by a
headless reproducer that printed conditioning tensors: with `patch_all()`
disabled the custom CLIP implementation was finite; with the patched
Transformers path it was all NaN. Random-weight instances of the same
Transformers model were *finite*, which proved the compute path was fine and
pointed at weight loading — and `no_init_weights()` + flattened keys explained
the rest.

---

## 5. Validation

### 5.1 Headless conditioning/sampling audit
```bash
STEPS=2 python tpu_debug_nan.py
```
Checks every `c_crossattn` / `pooled_output`, the patched ADM embedding and the
sampled latent with `torch.isfinite`.

Result with the real checkpoint and the default offset LoRA:

```
is_tpu: True device: tpu
final_unet dtype: torch.bfloat16
attention: <function attention_pytorch ...>
positive.c_crossattn: (1, 231, 2048) float32 finite=True
positive.pooled_output: (1, 1280) float32 finite=True
negative.c_crossattn: (1, 385, 2048) float32 finite=True
negative.pooled_output: (1, 1280) float32 finite=True
positive.adm_y: (1, 5632) finite=True        # Fooocus SDXL ADM layout
negative.adm_y: (1, 5632) finite=True
sampled_latent: (1, 4, 112, 144) finite=True
RESULT: sampled latent finite = True | conditioning finite = True
```

### 5.2 Full pipeline generation
```bash
STEPS=30 python tpu_full_generate.py
```

- 1024×1024, 30 steps: PNG with real structure (mean 110, std 58.5).
- 1152×896, 8 steps (cold process, includes compilation): text encoding 4.9 s,
  `process_diffusion` 89.9 s, **peak HBM 15,058 MiB of 16,126 MiB**.
- 1152×896, 30 steps: `dpmpp_2m_sde_gpu`/`karras` at ~2.4 it/s once compiled.

### 5.3 Real UI generate path
The UI's own worker (`modules/async_worker.AsyncTask` → `worker()` thread, the
code behind the Generate button) was driven with the **live `/config` defaults**
(the shipped preset): 1152×896, 30 steps, cfg 4.0, Fooocus V2/Enhance/Sharp,
offset LoRA 0.1, seed 12345.

```
task: Performance.SPEED 30 steps | 1152×896 | ['Fooocus V2', 'Fooocus Enhance', 'Fooocus Sharp']
preview 100%: Saving image 1/1 to system ...
Image generated with private log at: outputs/2026-11-12/log.html
Generating and saving time: 117.02 seconds
finish: 1 image(s)   -> outputs/2026-11-12/2026-11-12_19-59-07_7825.png
```

The saved image has a bright sky band and darker terrain (mean 84.8, std 54.6),
i.e. a real generation, not a flat/black decode.

### 5.4 Gradio (end to end)
`python launch.py --disable-analytics --disable-in-browser --port 7860` serves
`HTTP 200` on `127.0.0.1:7860` with the full block tree (all 152 generate
inputs resolved from `/config`).

The complete Generate chain (fn_index 67 `get_task` → fn_index 68
`generate_clicked`) was driven through the websocket queue protocol exactly as a
browser does (`POST /queue/join` + streamed `/queue/data` messages), using the
live `/config` defaults: 1152×896, 30 steps, cfg 4.0, Fooocus V2/Enhance/Sharp,
offset LoRA 0.1, seed 12345. The chain now completes with
`process_completed success=True` and delivers a gallery image
(`outputs/ui_driver/2026-11-12_20-51-37_1166.png`, 1152×896, mean 63.0,
std 47.7 — non-flat), with previews streaming through the websocket. The UI
worker path is therefore fully functional, not just page-serving.

---

## 6. Performance notes

- **Compilation dominates cold starts.** Each new static shape triggers PJRT
  compilation; the first 8-step 1152×896 request took ~90 s end-to-end. Steady
  state is ~1.3–2.6 it/s for SDXL bf16, so 30 steps cost ~23–36 s depending on
  resolution.
- **Keep shapes stable.** Changing resolution, batch size or tiled-decode
  settings recompiles. Seed changes do not.
- **HBM is tight.** ~15.0 GiB peak at 1152×896 leaves <1 GiB headroom. 1024×1024
  is safer; base+refiner simultaneously is not recommended on this device.
- Attention is SDPA on every call (cross-attn and self-attn), which is the only
  fused attention path available on this backend.
- **Use bf16, not fp16.** FP16 does not use the TPU SDPA fast path; bf16 is the
  intended dtype.
- FP8 options are CUDA-only and are not used here.
- Tiled VAE decode is available if a full-resolution decode runs out of HBM.

---

## 7. Known limitations / follow-ups

- **Inpaint/upscale/enhance/face/ControlNet paths are not exercised.** They are
  CPU/ONNX or CUDA-oriented preprocessors; imports work, TPU execution is
  untested.
- **No quality parity study** against CUDA FP16. Same weights, same prompt, same
  seed produce plausible images, but no FID/CLIP comparison was done.
- **Refiner at high resolution is untested** — likely to OOM at 1152×896 with
  both UNets resident.
- **No `torch.compile`/`torch.export` integration.** We rely on PJRT's automatic
  compilation of eager graphs.
- **Compile cache is disabled in this container**, so every process restart pays
  compilation again. Enabling the PJRT/tier-3 cache would cut cold-start time.
- **Gradio 3.41.2 stack is brittle** on Python 3.13; it is pinned in section 0.4
  because newer FastAPI/Pydantic/websockets break the old server code. The port
  adds two runtime shims (NumPy 1.x aliases and the queue HTTP timeout) so the
  UI now runs end to end on the TPU image.
- **Population-vs-sample std** in `adaptive_anisotropic_filter` is a deliberate
  numerical deviation (negligible at SDXL tensor sizes).
- **Single device only.** No SPMD/multi-TPU or `torch.distributed` work was done.
- **Other unimplemented ATen ops** may appear in less common paths (the
  `std_mean` hit suggests auditing `torch.*` reductions if new samplers fail).

---

## 8. Reproducing

```bash
# environment (see section 0.4 for the full list)
pip install torchsde==0.2.6 trampoline
pip install --no-deps opencv-python-headless gradio==3.41.2 gradio-client==0.5.0
pip install fastapi==0.104.1 starlette==0.27.0 pydantic==2.9.2 websockets==11.0.3
pip install ffmpy pydub semantic-version orjson importlib-resources
pip install supervision timm pycocotools addict segment-anything groundingdino-py onnxruntime rembg

cd Fooocus
STEPS=2  python tpu_debug_nan.py        # conditioning must be finite
STEPS=30 python tpu_full_generate.py    # writes /content/fooocus_tpu_output.png
python launch.py --disable-analytics --disable-in-browser --port 7860
# drive the live UI end to end (websocket queue protocol):
python tpu_ui_driver.py --steps 8 --image-number 1 --outdir outputs/ui_driver
```

Apply / revert the port:

```bash
git apply --check /content/fooocus_tpu_patch.diff   # verified against v2.5.5
git apply         /content/fooocus_tpu_patch.diff
git apply -R      /content/fooocus_tpu_patch.diff   # revert
```

---

## 9. Porting checklist for other diffusion apps

If you port a similar CUDA-era SD app to this backend, the same order works:

1. Make device selection explicit and conservative (`torch.accelerator` probe);
   never touch `torch.cuda.*` unless `torch.cuda.is_available()`.
2. Replace hard-coded `device_type='cuda'` autocast calls with the tensor's
   device type.
3. Pick bf16 and disable manual/weight casting when storage and compute dtype
   match.
4. Force PyTorch SDPA; disable xformers/split/sub-quadratic kernels.
5. Convert NumPy↔tensor boundaries (beta schedules) and bf16→fp32 before
   `.numpy()`.
6. Audit numerics that hit unimplemented ATen ops (start with reductions like
   `std_mean`, `var_mean`, `correction=`).
7. **Verify weight loading**, not just that the model runs: compare
   `state_dict` key counts and load reports. `no_init_weights()` + a silent
   `strict=False` mismatch is invisible until you get NaN/black output.
8. Validate in layers: finite conditioning → finite one-step sample → full
   generation → UI path, with a headless reproducer per layer.
