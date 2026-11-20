# llamafactory — portability analysis

- **Package name:** LlamaFactory (`llamafactory`)
- **Description:** Unify Efficient Fine-Tuning of 100+ LLMs https://github.com/hiyouga/LLaMA-Factory
- **Original git URL:** https://github.com/pinokiofactory/llamafactory
- **Analyzed commit:** `e299b25b26f48bb6ef96a670c2da402f0e328441`
- **Platforms supported:** NVIDIA / AMD / Mac
- **Porting difficulty:** Medium–high
- **CUDA-only packages:** bitsandbytes, flash-attn, xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

bitsandbytes, flash-attn, numpy, torch, torch-directml, torchaudio, torchvision, xformers

Wheel indexes referenced: cpu, cu128, rocm6.3.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 315
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- `torch.js` routes present: nvidia, amd, mac, cpu.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): xformers
- Difficulty score: 6.0 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).
