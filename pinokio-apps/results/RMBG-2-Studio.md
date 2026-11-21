# RMBG-2-Studio — portability analysis

- **Package name:** RMBG-2-Studio (`RMBG-2-Studio`)
- **Description:** Enhanced background remove and replace app built around BRIA-RMBG-2.0 https://huggingface.co/briaai/RMBG-2.0
- **Original git URL:** https://github.com/pinokiofactory/RMBG-2-Studio
- **Analyzed commit:** `a2c3a0d0f1618c74c115d3221eb665bab5e8df10`
- **Platforms supported:** NVIDIA / AMD / Mac
- **Porting difficulty:** Low
- **CUDA-only packages:** xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

devicetorch, gradio, gradio-imageslider, kornia, loadimg, numpy, opencv-python, pillow, prettytable, pydantic, scikit-image, starlette, timm, torch, torch-directml, torchaudio, torchvision, transformers, typing, xformers

Requirements files: `app/requirements.txt`.

Third-party Python imports detected in local source: cv2, devicetorch, gradio, gradio-imageslider, loadimg, numpy, pil, requests, torch, torchvision, tqdm, transformers.

Wheel indexes referenced: cpu, cu124, cu128, rocm6.2.4.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 1084
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- `torch.js` routes present: nvidia, amd, mac, cpu.
- Requirements from: app/requirements.txt
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): xformers
- Difficulty score: 0.5 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- retested on Python 3.12; dependencies installed and app imported successfully on CPU.
- Result: **CPU port imports successfully.**
