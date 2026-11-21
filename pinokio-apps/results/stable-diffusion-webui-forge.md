# stable-diffusion-webui-forge — portability analysis

- **Package name:** Forge (`stable-diffusion-webui-forge`)
- **Description:** [NVIDIA ONLY] The most efficient way to run FLUX (Optimized to run even on low memory machines, as low as 3GB VRAM with 512x512 resolution) https://github.com/lllyasviel/stable-diffusion-webui-forge
- **Original git URL:** https://github.com/pinokiofactory/stable-diffusion-webui-forge
- **Analyzed commit:** `e44fda22458c495919a1c90ed9e7d5c63c37adfb`
- **Platforms supported:** NVIDIA only
- **Porting difficulty:** Medium
- **CUDA-only packages:** torch (CUDA wheel)

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

numpy, torch, torchaudio, torchvision, wheel

Wheel indexes referenced: cu128.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 374
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- Explicit platform tag found: NVIDIA only.
- `torch.js` routes present: none.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Difficulty score: 4.0 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- blocked by numpy build failure on Python 3.14.
- Result: **not runnable in this container.**

## CPU port attempt

- **Attempt order:** #73 of 101 (by porting effort, easiest first).
- **Status:** CPU-capable (shipped fallback).
- **Changes applied / required:** use existing non-GPU launcher route; replace CUDA-only torch wheel with CPU wheel; upcast 817 FP8 GEMMs to BF16/FP32; dequantize 626 packed 4-bit weights; tune oneDNN/MKL threads for FP16/BF16 GEMMs.
- **Smoke check:** n/a (no Python source in snapshot).
- **Blockers:** CUDA-only torch wheel; 817 FP8 GEMMs; 626 packed 4-bit weights.
- **Scope note:** static portability review of the Pinokio wrapper; no install or model download was executed.
