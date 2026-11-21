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

- blocked by numpy build failure and missing MLX runtime on Linux.
- Result: **not runnable in this container.**

## CPU port attempt

- **Attempt order:** #71 of 101 (by porting effort, easiest first).
- **Status:** Blocked (Apple-only).
- **Changes applied / required:** use existing CPU wheel branch in torch.js; use existing non-NVIDIA/non-AMD branch in torch.js; use existing non-GPU launcher route; substitute GPU-only attention libs with SDPA math backend.
- **Smoke check:** n/a (no Python source in snapshot).
- **Blockers:** Apple-silicon-only MLX runtime; GPU-only attention: xformers.
- **Scope note:** static portability review of the Pinokio wrapper; no install or model download was executed.
