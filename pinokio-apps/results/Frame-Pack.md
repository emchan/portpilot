# Frame-Pack — portability analysis

- **Package name:** FramePack (`Frame-Pack`)
- **Description:** [NVIDIA ONLY] Generate Video Progressively. FramePack is a next-frame (next-frame-section) prediction neural network structure that generates videos progressively. https://github.com/lllyasviel/FramePack
- **Original git URL:** https://github.com/pinokiofactory/Frame-Pack
- **Analyzed commit:** `f0d7d1eba4155f5985a465d0476a9f926d0c6179`
- **Platforms supported:** NVIDIA only
- **Porting difficulty:** Very high
- **CUDA-only packages:** sageattention, triton, triton-windows, xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

devicetorch, diffusers, diffusers-helper, einops, gradio, hf-xet, numpy, pil, safetensors, sageattention, torch, torch-directml, torchaudio, torchvision, transformers, triton, triton-windows, xformers

Third-party Python imports detected in local source: diffusers, diffusers-helper, einops, gradio, numpy, pil, safetensors, torch, transformers.

Wheel indexes referenced: cpu, cu128, rocm6.3.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 1231
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- Explicit platform tag found: NVIDIA only.
- `torch.js` routes present: nvidia, amd, mac, cpu.
- No requirements file; third-party Python imports used as a fallback signal.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): xformers
- Difficulty score: 10.0 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- blocked by av build failure (pkg-config) on Python 3.14.
- Result: **not runnable in this container.**

## CPU port attempt

- **Attempt order:** #85 of 101 (by porting effort, easiest first).
- **Status:** CPU-capable (shipped fallback).
- **Changes applied / required:** use existing CPU wheel branch in torch.js; use existing non-NVIDIA/non-AMD branch in torch.js; use existing non-GPU launcher route; rely on devicetorch (already present); disable fused GPU kernels (xformers/flash/sage) in config; substitute GPU-only attention libs with SDPA math backend; +1.
- **Smoke check:** pass (2/2 files).
- **Blockers:** GPU-only attention: sageattention/triton/triton-windows/xformers; CUDA-only fused kernels.
- **Scope note:** static portability review of the Pinokio wrapper; no install or model download was executed.
