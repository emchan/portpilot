# moshi — portability analysis

- **Package name:** moshi (`moshi`)
- **Description:** [Mac only] a speech-text foundation model for real time dialogue https://github.com/kyutai-labs/moshi
- **Original git URL:** https://github.com/pinokiofactory/moshi
- **Analyzed commit:** `485d527a4d8a57e99e58b4735b61b5fb300d2aa3`
- **Platforms supported:** Mac (Apple Silicon) only
- **Porting difficulty:** Low–medium
- **CUDA-only packages:** xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

install, moshi, moshi-mlx, numpy, rust, torch, torch-directml, torchaudio, torchvision, xformers

Wheel indexes referenced: cpu, cu121, nightly, rocm6.0.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 289
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- Explicit platform tag found: Mac (Apple Silicon) only.
- `torch.js` routes present: nvidia, amd, mac, cpu.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): xformers
- Difficulty score: 1.5 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- retested on Python 3.12; moshi package blocked by numpy build failure.
- Result: **not runnable in this container.**
