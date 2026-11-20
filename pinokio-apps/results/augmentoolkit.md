# augmentoolkit — portability analysis

- **Package name:** augmentoolkit (`augmentoolkit`)
- **Description:** Turn any raw text into a high-quality dataset for AI finetuning https://github.com/e-p-armstrong/augmentoolkit
- **Original git URL:** https://github.com/pinokiofactory/augmentoolkit
- **Analyzed commit:** `24f80371c8ae61a91295b71f773e41a2616437e6`
- **Platforms supported:** NVIDIA / AMD / Mac
- **Porting difficulty:** Low
- **CUDA-only packages:** xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

torch, torch-directml, torchaudio, torchvision, xformers

Wheel indexes referenced: cpu, cu121, rocm5.7.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 293
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- `torch.js` routes present: nvidia, amd, mac, cpu.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): xformers
- Difficulty score: 0.5 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).
