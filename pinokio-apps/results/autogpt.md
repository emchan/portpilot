# autogpt — portability analysis

- **Package name:** autogpt (`autogpt`)
- **Description:** AutoGPT is a powerful tool that lets you create and run intelligent agents https://github.com/Significant-Gravitas/AutoGPT
- **Original git URL:** https://github.com/pinokiofactory/autogpt
- **Analyzed commit:** `53e7c0e1e22b3b9162d7d0669f9bac3491cf5d51`
- **Platforms supported:** NVIDIA / AMD / Mac
- **Porting difficulty:** Low
- **CUDA-only packages:** xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

poetry, torch, torch-directml, torchaudio, torchvision, xformers

Wheel indexes referenced: cpu, cu121, rocm6.0.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 280
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- `torch.js` routes present: nvidia, amd, mac, cpu.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): xformers
- Difficulty score: 0.5 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).
