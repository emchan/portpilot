# mlx-video-transcription — portability analysis

- **Package name:** MLX-Video-Transcription (`mlx-video-transcription`)
- **Description:** [Mac Only] Super Fast MLX Powered Video Transcription https://github.com/RayFernando1337/MLX-Auto-Subtitled-Video-Generator/ by https://x.com/RayFernando1337
- **Original git URL:** https://github.com/pinokiofactory/mlx-video-transcription
- **Analyzed commit:** `331245a916c9eb1602637a5cedebf83eb2322ee5`
- **Platforms supported:** Mac (Apple Silicon) only
- **Porting difficulty:** Low
- **CUDA-only packages:** —

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

No package dependencies were declared in the repository. Installers that only run `npm install` or clone another app do not name packages here.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 174
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- Explicit platform tag found: Mac (Apple Silicon) only.
- `torch.js` routes present: none.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Difficulty score: 1.0 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- MLX installed but libmlx.so missing at runtime on this Linux container.
- Result: **not runnable in this container.**

## CPU port attempt

- **Attempt order:** #64 of 101 (by porting effort, easiest first).
- **Status:** Blocked (Apple-only).
- **Changes applied / required:** no change identified.
- **Smoke check:** n/a (no Python source in snapshot).
- **Blockers:** Apple-silicon-only MLX runtime.
- **Scope note:** static portability review of the Pinokio wrapper; no install or model download was executed.
<!-- cross-analysis:start -->
## Cross-analysis details

- **CPU category (cpu.md):** Apple-silicon-only runtime
- **TPU suitability:** Unsuitable - Apple MLX-only runtime
- **TPU work needed:** MLX/Apple-silicon runtime; not a PyTorch/XLA TPU target
- **Effort ranking (effort.md):** #64 — Medium–high
- **Effort blockers:** Apple-silicon-only MLX runtime
- **Precisions noted:** unspecified
- **Models/flows noted:** —
- **Flow graph:** [flows/mlx-video-transcription.md](../flows/mlx-video-transcription.md)

### Snapshot verification (cloned analyzed commit)

- **Snapshot source:** `https://codeload.github.com/pinokiofactory/mlx-video-transcription/tar.gz/<analyzed commit>` extracted to `/tmp/opencode/pinokio-snapshots/mlx-video-transcription`
- **Files scanned:** 9 total (0 .py, 5 .js, 4 other)
- **Key files present:** pinokio.js, install.js, start.js
- **TPU/CUDA-relevant signals:**
  - `mlx`: 6 match(es) (e.g. README.md:1, README.md:3)

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
- [App flow graph](../flows/mlx-video-transcription.md)
<!-- cross-analysis:end -->
