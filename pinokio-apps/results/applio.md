# applio — portability analysis

- **Package name:** Applio (`applio`)
- **Description:** A simple, high-quality voice conversion tool focused on ease of use and performance.
- **Original git URL:** https://github.com/pinokiofactory/applio
- **Analyzed commit:** `41a9ccd75fbb39d84059447a8717581640c11143`
- **Platforms supported:** NVIDIA / AMD / Mac
- **Porting difficulty:** Low
- **CUDA-only packages:** xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

antlr4-python3-runtime, beautifulsoup4, certifi, edge-tts, einops, faiss-cpu, ffmpeg-python, gradio, librosa, matplotlib, noisereduce, numba, numpy, omegaconf, pedalboard, pip, psutil, pypresence, pyyaml, requests, scipy, setuptools, sounddevice, soundfile, soxr, stftpitchshift, swift-f0, tensorboard, tensorboardx, torch, torch-directml, torchaudio, torchcrepe, torchfcpe, torchvision, tqdm, transformers, webrtcvad-wheels, wget, wheel, xformers

Requirements files: `requirements.txt`.

Wheel indexes referenced: cpu, cu128, rocm6.3.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 475
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- `torch.js` routes present: nvidia, amd, mac, cpu.
- Requirements from: requirements.txt
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): xformers
- Difficulty score: 0.5 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- Dependency installation hung/timed out in this container.
- Result: **not runnable in this container.**

## CPU port attempt

- **Attempt order:** #20 of 101 (by porting effort, easiest first).
- **Status:** CPU-capable (shipped fallback).
- **Changes applied / required:** use existing CPU wheel branch in torch.js; use existing non-NVIDIA/non-AMD branch in torch.js; use existing non-GPU launcher route; substitute GPU-only attention libs with SDPA math backend.
- **Smoke check:** n/a (no Python source in snapshot).
- **Blockers:** GPU-only attention: xformers.
- **Scope note:** static portability review of the Pinokio wrapper; no install or model download was executed.
