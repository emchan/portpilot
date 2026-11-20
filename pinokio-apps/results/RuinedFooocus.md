# RuinedFooocus — portability analysis

- **Package name:** RuinedFooocus (`RuinedFooocus`)
- **Description:** Forget everything you thought you knew about AI art generation - RuinedFooocus is here to completely reinvent the game!
- **Original git URL:** https://github.com/pinokiofactory/RuinedFooocus
- **Analyzed commit:** `cd741937b44a7f1625acf35250ebf1bc6521dbb2`
- **Platforms supported:** NVIDIA only
- **Porting difficulty:** High
- **CUDA-only packages:** sageattention *(optional)*, triton-windows, xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

sageattention, torch, torchaudio, torchcodec, torchvision, triton-windows, xformers

Wheel indexes referenced: cu128.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 273
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- Explicit platform tag found: NVIDIA only.
- `torch.js` routes present: nvidia.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): sageattention, triton, xformers
- Difficulty score: 9.0 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).
