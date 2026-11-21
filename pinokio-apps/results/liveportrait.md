# liveportrait — portability analysis

- **Package name:** LivePortrait (`liveportrait`)
- **Description:** Bring portraits to life! https://github.com/KwaiVGI/LivePortrait
- **Original git URL:** https://github.com/pinokiofactory/liveportrait
- **Analyzed commit:** `b5fb16ce6df50e79d11d7c1a2d7b39faa720411e`
- **Platforms supported:** NVIDIA / AMD / Mac
- **Porting difficulty:** Low–medium
- **CUDA-only packages:** onnxruntime-gpu, xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

install, onnxruntime-gpu, torch, torch-directml, torchaudio, torchvision, xformers

Wheel indexes referenced: cpu, cu128, rocm6.0.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 388
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- `torch.js` routes present: nvidia, amd, mac, cpu.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): xformers
- Difficulty score: 2.5 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- import failed due to CUDA-only code path (torch.cuda) on CPU.
- Result: **not runnable in this container.**

## CPU port attempt

- **Attempt order:** #49 of 101 (by porting effort, easiest first).
- **Status:** CPU-capable (shipped fallback).
- **Changes applied / required:** use existing CPU wheel branch in torch.js; use existing non-NVIDIA/non-AMD branch in torch.js; use existing non-GPU launcher route; rely on devicetorch (already present); substitute GPU-only attention libs with SDPA math backend; remove GPU runtimes (onnxruntime-gpu/deepspeed/cudnn/tensorrt).
- **Smoke check:** n/a (no Python source in snapshot).
- **Blockers:** GPU-only attention: xformers; GPU runtime: onnxruntime-gpu.
- **Scope note:** static portability review of the Pinokio wrapper; no install or model download was executed.
