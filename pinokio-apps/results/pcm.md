# pcm — portability analysis

- **Package name:** PCM (`pcm`)
- **Description:** Phased Consistency Model - generate high quality images with 2 steps https://huggingface.co/spaces/radames/Phased-Consistency-Model-PCM
- **Original git URL:** https://github.com/pinokiofactory/pcm
- **Analyzed commit:** `1902e63160c5626aa0b14f0a1279f8c59a6239c1`
- **Platforms supported:** NVIDIA / AMD / Mac
- **Porting difficulty:** Low
- **CUDA-only packages:** xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

numpy, torch, torch-directml, torchaudio, torchvision, xformers

Wheel indexes referenced: cpu, cu124, nightly, rocm6.2.

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
