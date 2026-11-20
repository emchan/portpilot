# AudioX — portability analysis

- **Package name:** AudioX (`AudioX`)
- **Description:** AudioX Diffusion Transformer for Anything-to-Audio Generation
- **Original git URL:** https://github.com/pinokiofactory/AudioX
- **Analyzed commit:** `7a0ff7b5ca8d5eeb6054edf84196a23389545d1d`
- **Platforms supported:** NVIDIA / AMD / Mac
- **Porting difficulty:** High
- **CUDA-only packages:** flash-attn, sageattention *(optional)*, triton-windows, xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

flash-attn, hf-xet, numpy, pydantic, sageattention, torch, torch-directml, torchaudio, torchvision, triton-windows, xformers

Wheel indexes referenced: cpu, cu128, rocm6.1.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 344
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- `torch.js` routes present: nvidia, amd, mac, cpu.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): sageattention, triton, xformers
- Difficulty score: 7.0 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).
