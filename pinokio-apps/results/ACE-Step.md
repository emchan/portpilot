# ACE-Step — portability analysis

- **Package name:** ACE-Step (`ACE-Step`)
- **Description:** A Step Towards Music Generation Foundation Model
- **Original git URL:** https://github.com/pinokiofactory/ACE-Step
- **Analyzed commit:** `8cf2fac2765b1383e6d078b399acc3e38374949e`
- **Platforms supported:** NVIDIA only
- **Porting difficulty:** High
- **CUDA-only packages:** triton, triton-windows, xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

gradio, peft, torch, torchaudio, torchcodec, torchvision, triton, triton-windows, xformers

Wheel indexes referenced: cu128.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 245
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- `torch.js` routes present: nvidia.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): xformers
- Difficulty score: 9.0 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).
