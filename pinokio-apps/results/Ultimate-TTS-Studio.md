# Ultimate-TTS-Studio — portability analysis

- **Package name:** Ultimate-TTS-Studio (`Ultimate-TTS-Studio`)
- **Description:** Kokoro, KittenTTS, Higgs audio, Chatterbox/Multi, Fish-Speech, F5 & index-tts & indextts2, VoxCPM and VibeVoice in one app
- **Original git URL:** https://github.com/pinokiofactory/Ultimate-TTS-Studio
- **Analyzed commit:** `b8c15efaead5a5e8744783fd443466333d2b1805`
- **Platforms supported:** NVIDIA only
- **Porting difficulty:** Very high
- **CUDA-only packages:** flash-attn, onnxruntime-gpu, sageattention *(optional)*, triton *(optional)*, triton-windows, xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

devicetorch, espeak-ng, flash-attn, gradio, libaio-dev, libsox-fmt-all, numpy, onnxruntime-gpu, openai-whisper, phonemizer-fork, portaudio, pynini, sageattention, setuptools, sox, torch, torch-directml, torchaudio, torchvision, triton, triton-windows, voxcpm, wetextprocessing, xformers

Wheel indexes referenced: cpu, cu128, rocm6.3.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 374
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- Explicit platform tag found: NVIDIA only.
- `torch.js` routes present: nvidia, amd, mac, cpu.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): sageattention, triton, xformers
- Difficulty score: 12.8 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- blocked by numpy==1.26.0 requirement on Python 3.14.
- Result: **not runnable in this container.**

## CPU port attempt

- **Attempt order:** #94 of 101 (by porting effort, easiest first).
- **Status:** CPU-capable (shipped fallback).
- **Changes applied / required:** use existing CPU wheel branch in torch.js; use existing non-NVIDIA/non-AMD branch in torch.js; use existing non-GPU launcher route; rely on devicetorch (already present); disable fused GPU kernels (xformers/flash/sage) in config; substitute GPU-only attention libs with SDPA math backend; +1.
- **Smoke check:** n/a (no Python source in snapshot).
- **Blockers:** GPU-only attention: flash-attn/sageattention/triton/triton-windows/xformers; GPU runtime: onnxruntime-gpu; CUDA-only fused kernels.
- **Scope note:** static portability review of the Pinokio wrapper; no install or model download was executed.
