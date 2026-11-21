# Hunyuan3d-2-lowvram — portability analysis

- **Package name:** Hunyuan3D-2-LowVRAM (`Hunyuan3d-2-lowvram`)
- **Description:** Text/Image to 3D (Cross Platform: Mac + Windows + Linux): High-Resolution 3D Assets Generation with Large Scale Hunyuan3D Diffusion Models. https://github.com/deepbeepmeep/Hunyuan3D-2GP
- **Original git URL:** https://github.com/pinokiofactory/Hunyuan3d-2-lowvram
- **Analyzed commit:** `9c415021473ec16b64b85bda5d3d50295c478e5b`
- **Platforms supported:** Cross-platform
- **Porting difficulty:** Low
- **CUDA-only packages:** xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

diffusers, diso, gradio, gxx, huggingface-hub, numba, numpy, sentencepiece, setuptools, torch, torch-directml, torchaudio, torchvision, wheel, xformers

Wheel indexes referenced: cpu, cu128, rocm6.3.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 633
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- Explicit platform tag found: Cross-platform.
- `torch.js` routes present: nvidia, amd, mac, cpu.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): xformers
- Difficulty score: 0.5 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- Upstream install blocked by compiled extension/build failures (diso, xatlas, pillow/pydantic) in this environment.
- Result: **not runnable in this container.**

## CPU port attempt

- **Attempt order:** #13 of 101 (by porting effort, easiest first).
- **Status:** CPU-capable (shipped fallback).
- **Changes applied / required:** use existing CPU wheel branch in torch.js; use existing non-NVIDIA/non-AMD branch in torch.js; use existing non-GPU launcher route; substitute GPU-only attention libs with SDPA math backend.
- **Smoke check:** n/a (no Python source in snapshot).
- **Blockers:** GPU-only attention: xformers.
- **Scope note:** static portability review of the Pinokio wrapper; no install or model download was executed.
