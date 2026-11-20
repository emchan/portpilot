# MagicQuill — portability analysis

- **Package name:** MagicQuill (`MagicQuill`)
- **Description:** An intelligent, interactive Image Editing System. Easily erase and add objects on a user-friendly interface.
- **Original git URL:** https://github.com/pinokiofactory/MagicQuill
- **Analyzed commit:** `bfdae2847a85d7b00761b4e93fbcb91be5e6d494`
- **Platforms supported:** NVIDIA / AMD / Mac
- **Porting difficulty:** Medium
- **CUDA-only packages:** bitsandbytes, xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

bitsandbytes, huggingface-hub, numpy, torch, torch-directml, torchaudio, torchvision, xformers

Wheel indexes referenced: cpu, cu128, rocm6.3.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 357
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- `torch.js` routes present: nvidia, amd, mac, cpu.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): xformers
- Difficulty score: 3.0 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).
