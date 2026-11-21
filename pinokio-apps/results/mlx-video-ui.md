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

## CPU test run (2026-11-21)

- requires MLX/Apple Silicon and Python 3.11; not runnable on this Linux CPU container.
- Result: **not runnable in this container.**

## CPU port attempt

- **Attempt order:** #65 of 101 (by porting effort, easiest first).
- **Status:** Blocked (Apple-only).
- **Changes applied / required:** no change identified.
- **Smoke check:** n/a (no Python source in snapshot).
- **Blockers:** Apple-silicon-only MLX runtime.
- **Scope note:** static portability review of the Pinokio wrapper; no install or model download was executed.
