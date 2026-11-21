# moshi — portability analysis

- **Package name:** moshi (`moshi`)
- **Description:** [Mac only] a speech-text foundation model for real time dialogue https://github.com/kyutai-labs/moshi
- **Original git URL:** https://github.com/pinokiofactory/moshi
- **Analyzed commit:** `485d527a4d8a57e99e58b4735b61b5fb300d2aa3`
- **Platforms supported:** Mac (Apple Silicon) only
- **Porting difficulty:** Low–medium
- **CUDA-only packages:** xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

install, moshi, moshi-mlx, numpy, rust, torch, torch-directml, torchaudio, torchvision, xformers

Wheel indexes referenced: cpu, cu121, nightly, rocm6.0.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 289
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- Explicit platform tag found: Mac (Apple Silicon) only.
- `torch.js` routes present: nvidia, amd, mac, cpu.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): xformers
- Difficulty score: 1.5 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- retested on Python 3.12; moshi package blocked by numpy build failure.
- Result: **not runnable in this container.**
<!-- cross-analysis:start -->
## Cross-analysis details

- **CPU category (cpu.md):** Apple-silicon-only runtime
- **TPU suitability:** Unsuitable - Apple MLX-only runtime
- **TPU work needed:** MLX/Apple-silicon runtime; not a PyTorch/XLA TPU target
- **Effort ranking (effort.md):** #72 — Medium–high
- **Effort blockers:** Apple-silicon-only MLX runtime; GPU-only attention: xformers
- **Precisions noted:** unspecified
- **Models/flows noted:** —
- **Flow graph:** [flows/moshi.md](../flows/moshi.md)

### Snapshot verification (cloned analyzed commit)

- **Snapshot source:** `https://codeload.github.com/pinokiofactory/moshi/tar.gz/<analyzed commit>` extracted to `/tmp/opencode/pinokio-snapshots/moshi`
- **Files scanned:** 8 total (0 .py, 6 .js, 2 other)
- **Key files present:** pinokio.js, install.js, torch.js, start.js
- **TPU/CUDA-relevant signals:**
  - `xformers`: 6 match(es) (e.g. torch.js:24, torch.js:24)
  - `directml`: 1 match(es) (e.g. torch.js:35)

### Evidence from analysis files

| Source | Evidence |
|---|---|
| [kernels.md](../analysis/kernels.md) | No per-repo kernel table row matched; see kernels.md for global signals. |
| [quantization.md](../analysis/quantization.md) | No per-repo quantization table row matched; see quantization.md. |
| [fusion.md](../analysis/fusion.md) | No direct fusion table row matched; see fusion.md for global context. |
| [models.md](../analysis/models.md) | No model pull/shape row matched in models.md. |
| [cpu.md](../analysis/cpu.md) | CPU category: **Apple-silicon-only runtime** |
| [tpu.md](../analysis/tpu.md) | TPU suitability: **Unsuitable - Apple MLX-only runtime** — MLX/Apple-silicon runtime; not a PyTorch/XLA TPU target |

### Related analysis

- [CPU analysis](../analysis/cpu.md)
- [TPU analysis](../analysis/tpu.md)
- [Effort ranking](../analysis/effort.md)
- [Kernel evidence](../analysis/kernels.md)
- [Quantization evidence](../analysis/quantization.md)
- [Fusion evidence](../analysis/fusion.md)
- [Model pulls/shapes](../analysis/models.md)
- [Flow graphs](../analysis/flows.md)
- [App flow graph](../flows/moshi.md)
<!-- cross-analysis:end -->
