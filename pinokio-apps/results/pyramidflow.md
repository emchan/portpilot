# pyramidflow — portability analysis

- **Package name:** pyramidflow (`pyramidflow`)
- **Description:** Pyramd Flow Video Generation AI (text-to-video & image-to-video) https://github.com/jy0205/Pyramid-Flow
- **Original git URL:** https://github.com/pinokiofactory/pyramidflow
- **Analyzed commit:** `6ae7e61806478b430473c2a6ce9866525e3cd1a2`
- **Platforms supported:** NVIDIA / AMD / Mac
- **Porting difficulty:** Medium
- **CUDA-only packages:** triton *(optional)*, triton-windows, xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

gradio, numpy, torch, torch-directml, torchaudio, torchvision, triton, triton-windows, xformers

Wheel indexes referenced: cpu, cu128, rocm6.3.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 309
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- `torch.js` routes present: nvidia, amd, mac, cpu.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): triton, xformers
- Difficulty score: 3.2 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- blocked by torchvision operator mismatch.
- Result: **not runnable in this container.**

## CPU port attempt

- **Attempt order:** #50 of 101 (by porting effort, easiest first).
- **Status:** CPU-capable (shipped fallback).
- **Changes applied / required:** use existing CPU wheel branch in torch.js; use existing non-NVIDIA/non-AMD branch in torch.js; use existing non-GPU launcher route; substitute GPU-only attention libs with SDPA math backend.
- **Smoke check:** n/a (no Python source in snapshot).
- **Blockers:** GPU-only attention: triton/triton-windows/xformers.
- **Scope note:** static portability review of the Pinokio wrapper; no install or model download was executed.
