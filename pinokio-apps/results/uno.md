# uno — portability analysis

- **Package name:** uno (`uno`)
- **Description:** [NVIDIA ONLY] Generate an image from multiple images https://github.com/bytedance/UNO
- **Original git URL:** https://github.com/pinokiofactory/uno
- **Analyzed commit:** `6f190672a75ccadd481a5cd69db95ed392ede8c0`
- **Platforms supported:** NVIDIA only
- **Porting difficulty:** High
- **CUDA-only packages:** deepspeed, sageattention *(optional)*, triton *(optional)*, triton-windows, xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

deepspeed, numpy, sageattention, torch, torch-directml, torchaudio, torchvision, triton, triton-windows, xformers

Wheel indexes referenced: cpu, cu121, cu128, rocm6.2.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 354
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- Explicit platform tag found: NVIDIA only.
- `torch.js` routes present: nvidia, amd, mac, cpu.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): sageattention, triton, xformers
- Difficulty score: 9.8 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- retested on Python 3.10; dependencies installed and app.py imported successfully on CPU.
- Result: **CPU port imports successfully.**
<!-- cross-analysis:start -->
## Cross-analysis details

- **CPU category (cpu.md):** CPU-capable with shipped fallback
- **TPU suitability:** Difficult - high-effort port
- **TPU work needed:** replace CUDA attention kernels with TPU-compatible attention/SDPA/XLA; FP8 GEMMs need upcast or TPU FP8 kernel support/validation; DeepSpeed training/runtime path is CUDA-oriented; many CUDA-specific dependencies/quantization/runtime constraints
- **Effort ranking (effort.md):** #87 — Very high
- **Effort blockers:** GPU-only attention: sageattention/triton/triton-windows/xformers; GPU runtime: deepspeed; CUDA-only fused kernels need config change
- **Precisions noted:** FP8
- **Models/flows noted:** —
- **Flow graph:** [flows/uno.md](../flows/uno.md)

### Snapshot verification (cloned analyzed commit)

- **Snapshot source:** `https://codeload.github.com/pinokiofactory/uno/tar.gz/<analyzed commit>` extracted to `/tmp/opencode/pinokio-snapshots/uno`
- **Files scanned:** 11 total (0 .py, 7 .js, 4 other)
- **Key files present:** pinokio.js, install.js, torch.js, start.js
- **TPU/CUDA-relevant signals:**
  - `xformers`: 5 match(es) (e.g. torch.js:26, torch.js:26)
  - `sageattention`: 11 match(es) (e.g. torch.js:13, torch.js:13)
  - `triton`: 6 match(es) (e.g. torch.js:12, torch.js:12)
  - `deepspeed`: 2 match(es) (e.g. install.js:34, install.js:45)
  - `fp8`: 2 match(es) (e.g. pinokio.js:69, pinokio.js:72)
  - `directml`: 1 match(es) (e.g. torch.js:40)

### Evidence from analysis files

| Source | Evidence |
|---|---|
| [kernels.md](../analysis/kernels.md) | `\| [uno](https://github.com/pinokiofactory/uno) \| [6f19067](https://github.com/pinokiofactory/uno/commit/6f190672a75ccadd481a5cd69db95ed392ede8c0) \| optional flag + launcher install \| install.js, torch.js \| [torch.js:12](https://github.com/pinokiofactory/uno/blob/6f190672a75ccadd481a5cd69db95ed392ede8c0/torch.js#L12) — "{{args && args.triton ? 'uv pip install -U --pre triton-windows' : ''}}", \|` |
| [kernels.md](../analysis/kernels.md) | `\| [uno](https://github.com/pinokiofactory/uno) \| [6f19067](https://github.com/pinokiofactory/uno/commit/6f190672a75ccadd481a5cd69db95ed392ede8c0) \| optional flag + launcher install \| [torch.js:13](https://github.com/pinokiofactory/uno/blob/6f190672a75ccadd481a5cd69db95ed392ede8c0/torch.js#L13) — "{{args && args.sageattention ? 'uv pip install https://github.com/woct0rdho/SageAttention/releases/download/v2.1.1-windows/sageattention-2.1.1+cu128torch2.7.0-cp...<br>[torch.js:28](https://github.com/pinokiofactory/uno/blob/6f190672a75ccadd481a5cd69db95ed392ede8c0/torch.js#L28) — "{{args && args.sageattention ? 'uv pip install https://github.com/deepbeepmeep/SageAttention/raw/refs/heads/main/releases/sageattention-2.1.0-cp310-cp310-win_amd... \|` |
| [quantization.md](../analysis/quantization.md) | `\| [uno](https://github.com/pinokiofactory/uno) \| reference \| `pinokio.js:69` — text: "Start FP8 Model (Low VRAM)",<br>`pinokio.js:72` — name: "flux-dev-fp8" \|` |
| [quantization.md](../analysis/quantization.md) | `\| [uno](https://github.com/pinokiofactory/uno) \| [6f19067](https://github.com/pinokiofactory/uno/commit/6f190672a75ccadd481a5cd69db95ed392ede8c0) \| [69](https://github.com/pinokiofactory/uno/blob/6f190672a75ccadd481a5cd69db95ed392ede8c0/pinokio.js#L69) \| float8 / FP8 \| checkpoint / config \| text: "Start FP8 Model (Low VRAM)", \|` |
| [quantization.md](../analysis/quantization.md) | `\| [uno](https://github.com/pinokiofactory/uno) \| [6f19067](https://github.com/pinokiofactory/uno/commit/6f190672a75ccadd481a5cd69db95ed392ede8c0) \| [72](https://github.com/pinokiofactory/uno/blob/6f190672a75ccadd481a5cd69db95ed392ede8c0/pinokio.js#L72) \| float8 / FP8 \| checkpoint / config \| name: "flux-dev-fp8" \|` |
| [fusion.md](../analysis/fusion.md) | `\| [uno](https://github.com/pinokiofactory/uno) \| [6f19067](https://github.com/pinokiofactory/uno/commit/6f190672a75ccadd481a5cd69db95ed392ede8c0) \| optional launcher flag \| [torch.js:13](https://github.com/pinokiofactory/uno/blob/6f190672a75ccadd481a5cd69db95ed392ede8c0/torch.js#L13) — `"{{args && args.sageattention ? 'uv pip install https://github.com/woct0rdho/SageAttention/releases/download/v2.1.1-windows/sageattention-2.1.1+cu128t` \|` |
| [models.md](../analysis/models.md) | No model pull/shape row matched in models.md. |
| [cpu.md](../analysis/cpu.md) | CPU category: **CPU-capable with shipped fallback** |
| [tpu.md](../analysis/tpu.md) | TPU suitability: **Difficult - high-effort port** — replace CUDA attention kernels with TPU-compatible attention/SDPA/XLA; FP8 GEMMs need upcast or TPU FP8 kernel support/validation; DeepSpeed training/runtime path is CUDA-oriented; many CUDA-specific dependencies/quantization/runtime constraints |

### Related analysis

- [CPU analysis](../analysis/cpu.md)
- [TPU analysis](../analysis/tpu.md)
- [Effort ranking](../analysis/effort.md)
- [Kernel evidence](../analysis/kernels.md)
- [Quantization evidence](../analysis/quantization.md)
- [Fusion evidence](../analysis/fusion.md)
- [Model pulls/shapes](../analysis/models.md)
- [Flow graphs](../analysis/flows.md)
- [App flow graph](../flows/uno.md)
<!-- cross-analysis:end -->
