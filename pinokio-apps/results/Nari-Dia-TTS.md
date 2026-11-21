# Nari-Dia-TTS — portability analysis

- **Package name:** Nari-Dia-TTS (`Nari-Dia-TTS`)
- **Description:** Nari Dia is a powerful text-to-speech (TTS) application based on the Dia-1.6B model from Nari Labs. This application allows you to convert text into natural-sounding speech with various customization options.
- **Original git URL:** https://github.com/pinokiofactory/Nari-Dia-TTS
- **Analyzed commit:** `e5b630df297c7f47f6c518a00d6c3f44be4e25b5`
- **Platforms supported:** NVIDIA / AMD / Mac
- **Porting difficulty:** Medium
- **CUDA-only packages:** sageattention *(optional)*, triton-windows, xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

descript-audio-codec, gradio, huggingface-hub, numpy, pydantic, sageattention, soundfile, torch, torch-directml, torchaudio, torchvision, triton-windows, xformers

Requirements files: `requirements.txt`.

Third-party Python imports detected in local source: dac, dia, gradio, huggingface-hub, numpy, pydantic, soundfile, the, torch, torchaudio.

Wheel indexes referenced: cpu, cu124, nightly, rocm6.2.4.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 2634
- **CUDA-related functions used:** `torch.cuda.is_available`

## Evidence and notes

- `torch.js` routes present: nvidia, amd, mac, cpu.
- Requirements from: requirements.txt
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): sageattention, triton, xformers
- Difficulty score: 4.0 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- blocked by torchaudio extension incompatibility on Python 3.14.
- Result: **not runnable in this container.**

## CPU port attempt

- **Attempt order:** #59 of 101 (by porting effort, easiest first).
- **Status:** CPU-capable (shipped fallback).
- **Changes applied / required:** use existing CPU wheel branch in torch.js; use existing non-NVIDIA/non-AMD branch in torch.js; use existing non-GPU launcher route; keep explicit device='cpu' branch; replace direct torch.cuda calls with devicetorch or cpu fallback; disable fused GPU kernels (xformers/flash/sage) in config; +2.
- **Smoke check:** pass (6/6 files).
- **Blockers:** GPU-only attention: sageattention/triton-windows/xformers; direct torch.cuda calls; CUDA-only fused kernels; MPS branch Apple-only.
- **Scope note:** static portability review of the Pinokio wrapper; no install or model download was executed.
