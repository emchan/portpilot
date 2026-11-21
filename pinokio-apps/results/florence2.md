# florence2 — portability analysis

- **Package name:** Florence2 (`florence2`)
- **Description:** An advanced vision foundation model from MicroSoft https://huggingface.co/spaces/gokaygokay/Florence-2
- **Original git URL:** https://github.com/pinokiofactory/florence2
- **Analyzed commit:** `5b517ac86c59d3b8a28a5d75c3aba34e2aa2e3b6`
- **Platforms supported:** NVIDIA / AMD / Mac
- **Porting difficulty:** Low
- **CUDA-only packages:** xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

devicetorch, gradio, pydantic, torch, torch-directml, torchaudio, torchvision, transformers, xformers

Wheel indexes referenced: cpu, cu128, rocm6.3.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 303
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- `torch.js` routes present: nvidia, amd, mac, cpu.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): xformers
- Difficulty score: 0.5 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- Retested on Python 3.12; dependencies installed, but full model loading not attempted due to multi-GB downloads.
- Result: **not runnable in this container.**
