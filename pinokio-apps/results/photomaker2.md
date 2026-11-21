# photomaker2 — portability analysis

- **Package name:** PhotoMaker2 (`photomaker2`)
- **Description:** Customizing Realistic Human Photos via Stacked ID Embedding https://huggingface.co/spaces/TencentARC/PhotoMaker-V2
- **Original git URL:** https://github.com/pinokiofactory/photomaker2
- **Analyzed commit:** `2c48cd3f30a305069aad6de30bfe4c3f0fe900f7`
- **Platforms supported:** NVIDIA / AMD / Mac
- **Porting difficulty:** Medium–high
- **CUDA-only packages:** cudnn, onnxruntime-gpu, xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

cudnn, devicetorch, gradio, huggingface-hub, numpy, onnxruntime, onnxruntime-directml, onnxruntime-gpu, onnxruntime-rocm, peft, torch, torch-directml, torchaudio, torchvision, transformers, xformers

Wheel indexes referenced: cpu, cu128, rocm6.3.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 316
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- `torch.js` routes present: nvidia, amd, mac, cpu.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): xformers
- Difficulty score: 5.0 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- blocked by numpy build failure on Python 3.14.
- Result: **not runnable in this container.**

## CPU port attempt

- **Attempt order:** #66 of 101 (by porting effort, easiest first).
- **Status:** CPU-capable (shipped fallback).
- **Changes applied / required:** use existing CPU wheel branch in torch.js; use existing non-NVIDIA/non-AMD branch in torch.js; use existing non-GPU launcher route; rely on devicetorch (already present); substitute GPU-only attention libs with SDPA math backend; remove GPU runtimes (onnxruntime-gpu/deepspeed/cudnn/tensorrt).
- **Smoke check:** n/a (no Python source in snapshot).
- **Blockers:** GPU-only attention: xformers; GPU runtime: cudnn/onnxruntime-gpu.
- **Scope note:** static portability review of the Pinokio wrapper; no install or model download was executed.
