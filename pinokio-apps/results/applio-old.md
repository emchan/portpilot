# applio-old — portability analysis

- **Package name:** Applio (`applio-old`)
- **Description:** VITS-based Voice Conversion focused on simplicity, quality and performance
- **Original git URL:** https://github.com/pinokiofactory/applio-old
- **Analyzed commit:** `a8d276c8f426304428755974392b5e42d4ef29a5`
- **Platforms supported:** NVIDIA only
- **Porting difficulty:** Medium
- **CUDA-only packages:** torch (CUDA wheel)

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

setuptools, torch, torchaudio, torchvision

Wheel indexes referenced: cu121.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 193
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- `torch.js` routes present: none.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Difficulty score: 4.0 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).
