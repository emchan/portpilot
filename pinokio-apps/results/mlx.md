# mlx — portability analysis

- **Package name:** chat-with-mlx (`mlx`)
- **Description:** [Mac Onlyl] An all-in-one LLMs Chat UI for Apple Silicon Mac using MLX Framework. https://github.com/qnguyen3/chat-with-mlx
- **Original git URL:** https://github.com/pinokiofactory/mlx
- **Analyzed commit:** `eedc5a1a3f57fbd7d78ad36d3f934b20372fac4c`
- **Platforms supported:** Mac (Apple Silicon) only
- **Porting difficulty:** Low–medium
- **CUDA-only packages:** xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

huggingface-hub, torch, torch-directml, torchaudio, torchvision, xformers

Wheel indexes referenced: cpu, cu121, nightly, rocm5.7.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 250
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- Explicit platform tag found: Mac (Apple Silicon) only.
- `torch.js` routes present: nvidia, amd, mac, cpu.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): xformers
- Difficulty score: 1.5 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- retested on Python 3.12; mlx package installed but libmlx.so missing at runtime on Linux.
- Result: **not runnable in this container.**
<!-- cross-analysis:start -->
## Cross-analysis details

- **CPU category (cpu.md):** Apple-silicon-only runtime
- **TPU suitability:** Unsuitable - Apple MLX-only runtime
- **TPU work needed:** MLX/Apple-silicon runtime; not a PyTorch/XLA TPU target
- **Effort ranking (effort.md):** #71 — Medium–high
- **Effort blockers:** Apple-silicon-only MLX runtime; GPU-only attention: xformers
- **Precisions noted:** unspecified
- **Models/flows noted:** —
- **Flow graph:** [flows/mlx.md](../flows/mlx.md)

### Snapshot verification (cloned analyzed commit)

- **Snapshot source:** `https://codeload.github.com/pinokiofactory/mlx/tar.gz/<analyzed commit>` extracted to `/tmp/opencode/pinokio-snapshots/mlx`
- **Files scanned:** 9 total (0 .py, 6 .js, 3 other)
- **Key files present:** pinokio.js, install.js, torch.js, start.js
- **TPU/CUDA-relevant signals:**
  - `xformers`: 4 match(es) (e.g. torch.js:9, torch.js:9)
  - `directml`: 1 match(es) (e.g. torch.js:19)
  - `mlx`: 5 match(es) (e.g. pinokio.js:4, pinokio.js:5)

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
- [App flow graph](../flows/mlx.md)
<!-- cross-analysis:end -->
