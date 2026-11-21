# ominicontrol — portability analysis

- **Package name:** OminiControl (`ominicontrol`)
- **Description:** A minimal and universal controller for FLUX.1 https://github.com/Yuanshi9815/OminiControl
- **Original git URL:** https://github.com/pinokiofactory/ominicontrol
- **Analyzed commit:** `2c9e78d353de3a48ea5adb83c618081bb2be71db`
- **Platforms supported:** NVIDIA / AMD / Mac
- **Porting difficulty:** Low
- **CUDA-only packages:** xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

numpy, torch, torch-directml, torchao, torchaudio, torchvision, xformers

Wheel indexes referenced: cpu, cu121, nightly, rocm6.0.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 278
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- `torch.js` routes present: nvidia, amd, mac, cpu.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): xformers
- Difficulty score: 0.5 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- retested on Python 3.12; still blocked by diffusers API mismatch (USE_PEFT_BACKEND).
- Result: **not runnable in this container.**
