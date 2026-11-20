# flashdiffusion — portability analysis

- **Package name:** flashdiffusion (`flashdiffusion`)
- **Description:** Accelerating any conditional diffusion model for few steps image generation https://gojasper.github.io/flash-diffusion-project/
- **Original git URL:** https://github.com/pinokiofactory/flashdiffusion
- **Analyzed commit:** `c61d18626e05f89335aca054a34cbbd6703d5b6b`
- **Platforms supported:** NVIDIA / AMD / Mac
- **Porting difficulty:** Low
- **CUDA-only packages:** xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

devicetorch, gradio, torch, torch-directml, torchaudio, torchvision, xformers

Wheel indexes referenced: cpu, cu121, nightly, rocm5.7.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 277
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- `torch.js` routes present: nvidia, amd, mac, cpu.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): xformers
- Difficulty score: 0.5 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).
