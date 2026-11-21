# Ilaria-RVC — portability analysis

- **Package name:** Ilaria-RVC (`Ilaria-RVC`)
- **Description:** Easily convert audio in Speech to Speech with built-in Text to Speech with RVC.
- **Original git URL:** https://github.com/pinokiofactory/Ilaria-RVC
- **Analyzed commit:** `2dd918e4d99c051cbc3a4201484cb91990cfa118`
- **Platforms supported:** NVIDIA / AMD / Mac
- **Porting difficulty:** Low
- **CUDA-only packages:** xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

devicetorch, gradio, numpy, torch, torch-directml, torchaudio, torchvision, xformers

Wheel indexes referenced: cpu, cu121, rocm6.0.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 261
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- `torch.js` routes present: nvidia, amd, mac, cpu.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): xformers
- Difficulty score: 0.5 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- retested on Python 3.10; blocked by fairseq/omegaconf dependency conflict (fairseq requires omegaconf<2.1).
- Result: **not runnable in this container.**
