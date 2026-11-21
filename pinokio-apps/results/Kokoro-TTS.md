# Kokoro-TTS — portability analysis

- **Package name:** Kokoro-TTS (`Kokoro-TTS`)
- **Description:** Welcome to Kokoro, a high-quality text-to-speech synthesis program powered by deep learning. This tool converts any text into high-fidelity speech in just a few seconds. Simply input text, select a voice, adjust the speed, and enjoy the generated audio.
- **Original git URL:** https://github.com/pinokiofactory/Kokoro-TTS
- **Analyzed commit:** `491a369bdca03b320586bd230f1c819562c03558`
- **Platforms supported:** NVIDIA / AMD / Mac
- **Porting difficulty:** Low
- **CUDA-only packages:** xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

accelerate, diffusers, espeak-ng, espeakng-loader, ffmpeg, gradio, hf-xet, huggingface-hub, imageio-ffmpeg, kokoro, libaio-dev, misaki, numpy, phonemizer-fork, pydub, scipy, setuptools, soundfile, torch, torch-directml, torchaudio, torchvision, transformers, wheel, xformers

Requirements files: `requirements.txt`.

Third-party Python imports detected in local source: gradio, imageio-ffmpeg, kokoro, scipy, torch, tqdm.

Wheel indexes referenced: cpu, cu128, rocm6.3.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 3518
- **CUDA-related functions used:** `torch.cuda.is_available`

## Evidence and notes

- `torch.js` routes present: nvidia, amd, mac, cpu.
- Requirements from: requirements.txt
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): xformers
- Difficulty score: 0.5 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- blocked by gradio/gradio_client version mismatch.
- Result: **not runnable in this container.**

## CPU port attempt

- **Attempt order:** #43 of 101 (by porting effort, easiest first).
- **Status:** CPU-capable (shipped fallback).
- **Changes applied / required:** use existing CPU wheel branch in torch.js; use existing non-GPU launcher route; replace direct torch.cuda calls with devicetorch or cpu fallback; substitute GPU-only attention libs with SDPA math backend.
- **Smoke check:** pass (1/1 files).
- **Blockers:** GPU-only attention: xformers; direct torch.cuda calls.
- **Scope note:** static portability review of the Pinokio wrapper; no install or model download was executed.
