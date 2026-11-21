# yue — portability analysis

- **Package name:** YuE (`yue`)
- **Description:** [NVIDIA ONLY] YuEGP--A Web UI for YuE, an Open Full-song Generation Foundation Model (10G VRAM required), via https://github.com/deepbeepmeep/YuEGP
- **Original git URL:** https://github.com/pinokiofactory/yue
- **Analyzed commit:** `3261118f111c8d2bb098b82b2870458dfbc486c7`
- **Platforms supported:** NVIDIA only
- **Porting difficulty:** Very high
- **CUDA-only packages:** flash-attn, triton *(optional)*, triton-windows, xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

flash-attn, hf-xet, torch, torchaudio, torchvision, transformers, triton, triton-windows, xformers

Wheel indexes referenced: cu121, cu124, cu128, rocm6.3.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 385
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- Explicit platform tag found: NVIDIA only.
- `torch.js` routes present: nvidia, amd.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): triton, xformers
- Difficulty score: 10.2 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- blocked by scipy version requirement (scipy==1.10.1) on Python 3.14.
- Result: **not runnable in this container.**

## CPU port attempt

- **Attempt order:** #92 of 101 (by porting effort, easiest first).
- **Status:** Needs launcher change.
- **Changes applied / required:** add a CPU wheel branch / remove GPU-only wheel pins; disable fused GPU kernels (xformers/flash/sage) in config; substitute GPU-only attention libs with SDPA math backend.
- **Smoke check:** n/a (no Python source in snapshot).
- **Blockers:** no CPU/AMD launcher branch; GPU-only attention: flash-attn/triton/triton-windows/xformers; CUDA-only fused kernels.
- **Scope note:** static portability review of the Pinokio wrapper; no install or model download was executed.
