# mlx-video-ui — portability analysis

- **Package name:** MLX Video UI (`mlx-video-ui`)
- **Description:** Local UI for MLX Video (Next.js frontend + FastAPI backend).
- **Original git URL:** https://github.com/pinokiofactory/mlx-video-ui
- **Analyzed commit:** `2f91ff7c3749a11dfcb3ed3e555a375cb5400421`
- **Platforms supported:** Mac (Apple Silicon) only
- **Porting difficulty:** Low
- **CUDA-only packages:** —

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

mlx-video, ok, printmlx-video

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 652
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- `torch.js` routes present: none.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Difficulty score: 1.0 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).
