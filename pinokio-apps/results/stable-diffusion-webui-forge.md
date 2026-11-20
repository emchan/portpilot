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
