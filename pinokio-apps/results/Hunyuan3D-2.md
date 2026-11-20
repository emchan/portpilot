# Hunyuan3D-2 — portability analysis

- **Package name:** Hunyuan3D-2 (`Hunyuan3D-2`)
- **Description:** [NVIDIA ONLY] Requires 24GB VRAM (Use the lowvram option, it has the same quality). High-Resolution 3D Assets Generation with Large Scale Hunyuan3D Diffusion Models. https://github.com/Tencent/Hunyuan3D-2
- **Original git URL:** https://github.com/pinokiofactory/Hunyuan3D-2
- **Analyzed commit:** `c0aa654a27ccda410b1d0914b61adbd52731c3c7`
- **Platforms supported:** NVIDIA only
- **Porting difficulty:** Medium
- **CUDA-only packages:** xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

gxx, numpy, torch, torch-directml, torchaudio, torchvision, xformers

Wheel indexes referenced: cpu, cu121, nightly, rocm6.0.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 360
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- Explicit platform tag found: NVIDIA only.
- `torch.js` routes present: nvidia, amd, mac, cpu.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): xformers
- Difficulty score: 3.5 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).
