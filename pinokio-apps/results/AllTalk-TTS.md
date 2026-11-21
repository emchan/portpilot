# AllTalk-TTS — portability analysis

- **Package name:** AllTalk-TTS v2 (`AllTalk-TTS`)
- **Description:** [NVIDIA ONLY] AllTalk-TTS is a unified UI for E5-TTS, XTTS, Vite TTS, Piper TTS, Parler TTS and RVC, based on CoquiTTS, including a finetune mode.
- **Original git URL:** https://github.com/pinokiofactory/AllTalk-TTS
- **Analyzed commit:** `7b6ed78e5a661eeafccdf446f0772be475390a5c`
- **Platforms supported:** NVIDIA only
- **Porting difficulty:** Medium–high
- **CUDA-only packages:** deepspeed, xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

cxx-compiler, deepspeed, espeak-ng, faiss-cpu, fastapi, ffmpeg, gcc, gfortran-osx-arm64, git-lfs, gradio, libaio-dev, numpy, pydantic, torch, torch-directml, torchaudio, torchvision, xformers

Wheel indexes referenced: cpu, cu121, rocm6.0.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 429
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- Explicit platform tag found: NVIDIA only.
- `torch.js` routes present: nvidia, amd, mac, cpu.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): xformers
- Difficulty score: 5.5 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- blocked by coqui-tts Python version requirement (>=3.9,<3.13).
- Result: **not runnable in this container.**

## CPU port attempt

- **Attempt order:** #67 of 101 (by porting effort, easiest first).
- **Status:** CPU-capable (shipped fallback).
- **Changes applied / required:** use existing CPU wheel branch in torch.js; use existing non-NVIDIA/non-AMD branch in torch.js; use existing non-GPU launcher route; substitute GPU-only attention libs with SDPA math backend; remove GPU runtimes (onnxruntime-gpu/deepspeed/cudnn/tensorrt).
- **Smoke check:** n/a (no Python source in snapshot).
- **Blockers:** GPU-only attention: xformers; GPU runtime: deepspeed.
- **Scope note:** static portability review of the Pinokio wrapper; no install or model download was executed.
