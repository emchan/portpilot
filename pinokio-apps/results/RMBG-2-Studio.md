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

- Install blocked by gradio 4.44 requiring HfFolder from huggingface_hub.
- Result: **not runnable in this container.**

## CPU port attempt

- **Attempt order:** #17 of 101 (by porting effort, easiest first).
- **Status:** CPU-capable (shipped fallback).
- **Changes applied / required:** use existing CPU wheel branch in torch.js; use existing non-NVIDIA/non-AMD branch in torch.js; use existing non-GPU launcher route; rely on devicetorch (already present); substitute GPU-only attention libs with SDPA math backend.
- **Smoke check:** pass (1/1 files).
- **Blockers:** GPU-only attention: xformers.
- **Scope note:** static portability review of the Pinokio wrapper; no install or model download was executed.
