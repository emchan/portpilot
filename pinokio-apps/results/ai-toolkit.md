# ai-toolkit — portability analysis

- **Package name:** ai-toolkit (`ai-toolkit`)
- **Description:** AI Toolkit by Ostris
- **Original git URL:** https://github.com/pinokiofactory/ai-toolkit
- **Analyzed commit:** `ddfefd70eb6f9d0b97c95e30b5c72aaac8660b0e`
- **Platforms supported:** NVIDIA only
- **Porting difficulty:** High
- **CUDA-only packages:** triton, triton-windows

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

numpy, torch, torchaudio, torchvision, triton, triton-windows

Wheel indexes referenced: cpu, cu128.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 307
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- Explicit platform tag found: NVIDIA only.
- `torch.js` routes present: nvidia, mac, cpu.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Difficulty score: 7.5 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- all JS files pass node --check; explicit NVIDIA-only guard prevents CPU install.
- Result: **not runnable in this container.**

## CPU port attempt

- **Attempt order:** #95 of 101 (by porting effort, easiest first).
- **Status:** Blocked.
- **Changes applied / required:** use existing CPU wheel branch in torch.js; use existing non-GPU launcher route; substitute GPU-only attention libs with SDPA math backend.
- **Smoke check:** n/a (no Python source in snapshot).
- **Blockers:** hard CUDA/TensorRT blocker; GPU-only attention: triton/triton-windows.
- **Scope note:** static portability review of the Pinokio wrapper; no install or model download was executed.
