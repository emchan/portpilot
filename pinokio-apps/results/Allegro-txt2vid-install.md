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

- blocked by numpy build failure on Python 3.14.
- Result: **not runnable in this container.**

## CPU port attempt

- **Attempt order:** #82 of 101 (by porting effort, easiest first).
- **Status:** Needs launcher change.
- **Changes applied / required:** add a CPU wheel branch / remove GPU-only wheel pins; rely on devicetorch (already present); substitute GPU-only attention libs with SDPA math backend.
- **Smoke check:** n/a (no Python source in snapshot).
- **Blockers:** no CPU/AMD launcher branch; GPU-only attention: triton-windows/xformers.
- **Scope note:** static portability review of the Pinokio wrapper; no install or model download was executed.
