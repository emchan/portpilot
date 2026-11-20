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
