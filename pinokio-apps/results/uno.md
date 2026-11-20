# uno — portability analysis

- **Package name:** uno (`uno`)
- **Description:** [NVIDIA ONLY] Generate an image from multiple images https://github.com/bytedance/UNO
- **Original git URL:** https://github.com/pinokiofactory/uno
- **Analyzed commit:** `6f190672a75ccadd481a5cd69db95ed392ede8c0`
- **Platforms supported:** NVIDIA only
- **Porting difficulty:** High
- **CUDA-only packages:** deepspeed, sageattention *(optional)*, triton *(optional)*, triton-windows, xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

deepspeed, numpy, sageattention, torch, torch-directml, torchaudio, torchvision, triton, triton-windows, xformers

Wheel indexes referenced: cpu, cu121, cu128, rocm6.2.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 354
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- Explicit platform tag found: NVIDIA only.
- `torch.js` routes present: nvidia, amd, mac, cpu.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): sageattention, triton, xformers
- Difficulty score: 9.8 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).
