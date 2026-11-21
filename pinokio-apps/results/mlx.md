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
