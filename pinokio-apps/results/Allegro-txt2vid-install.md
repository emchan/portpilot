# Allegro-txt2vid-install — portability analysis

- **Package name:** Allegro-txt2vid (`Allegro-txt2vid-install`)
- **Description:** [NVIDIA ONLY] Generate videos with Allegro txt2vid model https://github.com/rhymes-ai/Allegro
- **Original git URL:** https://github.com/pinokiofactory/Allegro-txt2vid-install
- **Analyzed commit:** `6000ff1e395f6238eaa89e68b45a571e84d324e1`
- **Platforms supported:** NVIDIA only
- **Porting difficulty:** Medium–high
- **CUDA-only packages:** triton-windows, xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

devicetorch, gradio, numpy, torch, torchaudio, torchvision, triton-windows, xformers

Wheel indexes referenced: cu128, rocm6.3.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 262
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- Explicit platform tag found: NVIDIA only.
- `torch.js` routes present: nvidia, amd.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): xformers
- Difficulty score: 6.5 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- retested on Python 3.10; blocked by torchvision operator mismatch (torchvision::nms).
- Result: **not runnable in this container.**
<!-- cross-analysis:start -->
## Cross-analysis details

- **CPU category (cpu.md):** CPU possible, but launcher must change
- **TPU suitability:** Difficult - significant port
- **TPU work needed:** replace CUDA attention kernels with TPU-compatible attention/SDPA/XLA; add TPU launcher/runtime branch; multiple CUDA-specific dependencies or large model/dtype constraints
- **Effort ranking (effort.md):** #82 — High
- **Effort blockers:** no CPU/AMD launcher branch; GPU-only attention: triton-windows/xformers
- **Precisions noted:** unspecified
- **Models/flows noted:** [AlexWortega/RIFE](https://huggingface.co/AlexWortega/RIFE)
- **Flow graph:** [flows/Allegro-txt2vid-install.md](../flows/Allegro-txt2vid-install.md)

### Snapshot verification (cloned analyzed commit)

- **Snapshot source:** `https://codeload.github.com/pinokiofactory/Allegro-txt2vid-install/tar.gz/<analyzed commit>` extracted to `/tmp/opencode/pinokio-snapshots/Allegro-txt2vid-install`
- **Files scanned:** 12 total (0 .py, 8 .js, 4 other)
- **Key files present:** pinokio.js, install.js, torch.js, start.js
- **TPU/CUDA-relevant signals:**
  - `xformers`: 5 match(es) (e.g. torch.js:11, torch.js:11)
  - `triton`: 1 match(es) (e.g. torch.js:12)

### Evidence from analysis files

| Source | Evidence |
|---|---|
| [kernels.md](../analysis/kernels.md) | `\| [Allegro-txt2vid-install](https://github.com/pinokiofactory/Allegro-txt2vid-install) \| [6000ff1](https://github.com/pinokiofactory/Allegro-txt2vid-install/commit/6000ff1e395f6238eaa89e68b45a571e84d324e1) \| launcher install \| torch.js \| [torch.js:12](https://github.com/pinokiofactory/Allegro-txt2vid-install/blob/6000ff1e395f6238eaa89e68b45a571e84d324e1/torch.js#L12) — "uv pip install triton-windows==3.3.1.post19" \|` |
| [quantization.md](../analysis/quantization.md) | No per-repo quantization table row matched; see quantization.md. |
| [fusion.md](../analysis/fusion.md) | No direct fusion table row matched; see fusion.md for global context. |
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
- [App flow graph](../flows/Allegro-txt2vid-install.md)
<!-- cross-analysis:end -->
