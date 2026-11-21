# RuinedFooocus — portability analysis

- **Package name:** RuinedFooocus (`RuinedFooocus`)
- **Description:** Forget everything you thought you knew about AI art generation - RuinedFooocus is here to completely reinvent the game!
- **Original git URL:** https://github.com/pinokiofactory/RuinedFooocus
- **Analyzed commit:** `cd741937b44a7f1625acf35250ebf1bc6521dbb2`
- **Platforms supported:** NVIDIA only
- **Porting difficulty:** High
- **CUDA-only packages:** sageattention *(optional)*, triton-windows, xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

sageattention, torch, torchaudio, torchcodec, torchvision, triton-windows, xformers

Wheel indexes referenced: cu128.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 273
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- Explicit platform tag found: NVIDIA only.
- `torch.js` routes present: nvidia.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): sageattention, triton, xformers
- Difficulty score: 9.0 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- Installed dependencies and cloned ComfyUI, but runtime failed on missing molbal_comfyui_gguf module.
- Result: **not runnable in this container.**

## CPU port attempt

- **Attempt order:** #90 of 101 (by porting effort, easiest first).
- **Status:** Needs launcher change.
- **Changes applied / required:** add a CPU wheel branch / remove GPU-only wheel pins; disable fused GPU kernels (xformers/flash/sage) in config; substitute GPU-only attention libs with SDPA math backend.
- **Smoke check:** n/a (no Python source in snapshot).
- **Blockers:** no CPU/AMD launcher branch; GPU-only attention: sageattention/triton-windows/xformers; CUDA-only fused kernels.
- **Scope note:** static portability review of the Pinokio wrapper; no install or model download was executed.
<!-- cross-analysis:start -->
## Cross-analysis details

- **CPU category (cpu.md):** CPU possible, but launcher must change
- **TPU suitability:** Difficult - significant port
- **TPU work needed:** replace CUDA attention kernels with TPU-compatible attention/SDPA/XLA; add TPU launcher/runtime branch; multiple CUDA-specific dependencies or large model/dtype constraints
- **Effort ranking (effort.md):** #90 — Very high
- **Effort blockers:** no CPU/AMD launcher branch; GPU-only attention: sageattention/triton-windows/xformers; CUDA-only fused kernels need config change
- **Precisions noted:** unspecified
- **Models/flows noted:** —
- **Flow graph:** [flows/RuinedFooocus.md](../flows/RuinedFooocus.md)

### Snapshot verification (cloned analyzed commit)

- **Snapshot source:** `https://codeload.github.com/pinokiofactory/RuinedFooocus/tar.gz/<analyzed commit>` extracted to `/tmp/opencode/pinokio-snapshots/RuinedFooocus`
- **Files scanned:** 10 total (0 .py, 7 .js, 3 other)
- **Key files present:** pinokio.js, install.js, torch.js, start.js
- **TPU/CUDA-relevant signals:**
  - `xformers`: 3 match(es) (e.g. torch.js:27, torch.js:27)
  - `sageattention`: 6 match(es) (e.g. torch.js:14, torch.js:14)
  - `triton`: 3 match(es) (e.g. torch.js:13, torch.js:13)

### Evidence from analysis files

| Source | Evidence |
|---|---|
| [kernels.md](../analysis/kernels.md) | `\| [RuinedFooocus](https://github.com/pinokiofactory/RuinedFooocus) \| [cd74193](https://github.com/pinokiofactory/RuinedFooocus/commit/cd741937b44a7f1625acf35250ebf1bc6521dbb2) \| optional flag + launcher install \| install.js, torch.js \| [torch.js:13](https://github.com/pinokiofactory/RuinedFooocus/blob/cd741937b44a7f1625acf35250ebf1bc6521dbb2/torch.js#L13) — "{{args && args.triton ? 'uv pip install -U --pre triton-windows' : ''}}", \|` |
| [kernels.md](../analysis/kernels.md) | `\| [RuinedFooocus](https://github.com/pinokiofactory/RuinedFooocus) \| [cd74193](https://github.com/pinokiofactory/RuinedFooocus/commit/cd741937b44a7f1625acf35250ebf1bc6521dbb2) \| optional flag + launcher install \| [torch.js:14](https://github.com/pinokiofactory/RuinedFooocus/blob/cd741937b44a7f1625acf35250ebf1bc6521dbb2/torch.js#L14) — "{{args && args.sageattention ? 'uv pip install https://github.com/woct0rdho/SageAttention/releases/download/v2.1.1-windows/sageattention-2.1.1+cu128torch2.7.0-cp...<br>[torch.js:29](https://github.com/pinokiofactory/RuinedFooocus/blob/cd741937b44a7f1625acf35250ebf1bc6521dbb2/torch.js#L29) — "{{args && args.sageattention ? 'uv pip install git+https://github.com/thu-ml/SageAttention.git' : ''}}", \|` |
| [quantization.md](../analysis/quantization.md) | No per-repo quantization table row matched; see quantization.md. |
| [fusion.md](../analysis/fusion.md) | `\| [RuinedFooocus](https://github.com/pinokiofactory/RuinedFooocus) \| [cd74193](https://github.com/pinokiofactory/RuinedFooocus/commit/cd741937b44a7f1625acf35250ebf1bc6521dbb2) \| optional launcher flag \| [torch.js:14](https://github.com/pinokiofactory/RuinedFooocus/blob/cd741937b44a7f1625acf35250ebf1bc6521dbb2/torch.js#L14) — `"{{args && args.sageattention ? 'uv pip install https://github.com/woct0rdho/SageAttention/releases/download/v2.1.1-windows/sageattention-2.1.1+cu128t` \|` |
| [models.md](../analysis/models.md) | No model pull/shape row matched in models.md. |
| [cpu.md](../analysis/cpu.md) | CPU category: **CPU possible, but launcher must change** |
| [tpu.md](../analysis/tpu.md) | TPU suitability: **Difficult - significant port** — replace CUDA attention kernels with TPU-compatible attention/SDPA/XLA; add TPU launcher/runtime branch; multiple CUDA-specific dependencies or large model/dtype constraints |

### Related analysis

- [CPU analysis](../analysis/cpu.md)
- [TPU analysis](../analysis/tpu.md)
- [Effort ranking](../analysis/effort.md)
- [Kernel evidence](../analysis/kernels.md)
- [Quantization evidence](../analysis/quantization.md)
- [Fusion evidence](../analysis/fusion.md)
- [Model pulls/shapes](../analysis/models.md)
- [Flow graphs](../analysis/flows.md)
- [App flow graph](../flows/RuinedFooocus.md)
<!-- cross-analysis:end -->
