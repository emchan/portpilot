# Allegro-txt2vid-install — portability analysis

- **Package name:** Allegro-txt2vid (`Allegro-txt2vid-install`)
- **Description:** [NVIDIA ONLY] Generate videos with Allegro txt2vid model https://github.com/rhymes-ai/Allegro
- **Original git URL:** https://github.com/pinokiofactory/Allegro-txt2vid-install
- **Analyzed commit:** `6000ff1e395f6238eaa89e68b45a571e84d324e1`
- **Platforms supported:** NVIDIA only
- **Porting difficulty:** Medium–high
- **CUDA-only packages:** triton-windows, xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

devicetorch, gradio, numpy, torch, torchaudio, torchvision, triton-windows, xformers

Wheel indexes referenced: cu128, rocm6.3.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 262
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- Explicit platform tag found: NVIDIA only.
- `torch.js` routes present: nvidia, amd.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): xformers
- Difficulty score: 6.5 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).
