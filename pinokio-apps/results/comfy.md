# comfy — portability analysis

- **Package name:** Comfyui (`comfy`)
- **Description:** The most powerful and modular diffusion model GUI, api and backend with a graph/nodes interface. https://github.com/comfyanonymous/ComfyUI
- **Original git URL:** https://github.com/pinokiofactory/comfy
- **Analyzed commit:** `ba110479f88835d64c603044c2fe69102833fa55`
- **Platforms supported:** NVIDIA / AMD / Mac
- **Porting difficulty:** Very high
- **CUDA-only packages:** bitsandbytes, flash-attn, sageattention, triton, triton-windows, xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

bitsandbytes, flash-attn, numpy, sageattention, torch, torch-directml, torchaudio, torchvision, triton, triton-windows, xformers

Wheel indexes referenced: cpu, cu128, rocm6.3.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 1262
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- `torch.js` routes present: nvidia, amd, mac, cpu.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): xformers
- Difficulty score: 12.5 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- dependencies installed; server started on CPU with --cpu flag.
- Result: **CPU port works with --cpu.**

## CPU port attempt

- **Attempt order:** #96 of 101 (by porting effort, easiest first).
- **Status:** CPU-capable (shipped fallback).
- **Changes applied / required:** use existing CPU wheel branch in torch.js; use existing non-NVIDIA/non-AMD branch in torch.js; use existing non-GPU launcher route; disable fused GPU kernels (xformers/flash/sage) in config; substitute GPU-only attention libs with SDPA math backend; remove bitsandbytes/torchao GPU quantisers or switch to GGUF; +3.
- **Smoke check:** n/a (no Python source in snapshot).
- **Blockers:** GPU-only attention: flash-attn/sageattention/triton/triton-windows/xformers; GPU quantisers: bitsandbytes; CUDA-only fused kernels; 2916 FP8 GEMMs; +1.
- **Scope note:** static portability review of the Pinokio wrapper; no install or model download was executed.
