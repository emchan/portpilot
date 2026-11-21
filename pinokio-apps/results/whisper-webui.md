# whisper-webui — portability analysis

- **Package name:** Whisper-WebUI (`whisper-webui`)
- **Description:** A Web UI for easy subtitle using whisper model.
- **Original git URL:** https://github.com/pinokiofactory/whisper-webui
- **Analyzed commit:** `5b6ebed2652d7adb7608ebe5c82ed01619e10daf`
- **Platforms supported:** NVIDIA / AMD / Mac
- **Porting difficulty:** Low
- **CUDA-only packages:** xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

faster-whisper, gradio, gradio-i18n, hf-xet, matplotlib, numpy, pyannote.audio, pytubefix, ruamel.yaml, torch, torch-directml, torchaudio, torchvision, transformers, xformers

Requirements files: `requirements.txt`.

Wheel indexes referenced: cpu, cu128, rocm6.3.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 315
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- `torch.js` routes present: nvidia, amd, mac, cpu.
- Requirements from: requirements.txt
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): xformers
- Difficulty score: 0.5 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- blocked by jhj0517-whisper build failure (pkg_resources/__version__) on Python 3.14.
- Result: **not runnable in this container.**

## CPU port attempt

- **Attempt order:** #39 of 101 (by porting effort, easiest first).
- **Status:** CPU-capable (shipped fallback).
- **Changes applied / required:** use existing CPU wheel branch in torch.js; use existing non-NVIDIA/non-AMD branch in torch.js; use existing non-GPU launcher route; substitute GPU-only attention libs with SDPA math backend.
- **Smoke check:** n/a (no Python source in snapshot).
- **Blockers:** GPU-only attention: xformers.
- **Scope note:** static portability review of the Pinokio wrapper; no install or model download was executed.
