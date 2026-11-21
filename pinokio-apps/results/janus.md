# janus — portability analysis

- **Package name:** Janus Pro (`janus`)
- **Description:** Unified Image Understanding and Image Generation with Data and Model Scaling https://github.com/peanutcocktail/Janus
- **Original git URL:** https://github.com/pinokiofactory/janus
- **Analyzed commit:** `6332de02fce4540acfea094435af331903120c69`
- **Platforms supported:** NVIDIA / AMD / Mac
- **Porting difficulty:** Low
- **CUDA-only packages:** xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

numpy, pkg-config, sentencepiece, torch, torch-directml, xformers

Wheel indexes referenced: cpu, cu118, rocm6.0.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 271
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- `torch.js` routes present: nvidia, amd, mac, cpu.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): xformers
- Difficulty score: 0.5 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- retested on Python 3.12; runtime still calls .cuda() and is not CPU-compatible.
- Result: **not runnable in this container.**
