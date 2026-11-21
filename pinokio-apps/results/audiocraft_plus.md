# audiocraft_plus — portability analysis

- **Package name:** audiocraft_plus (`audiocraft_plus`)
- **Description:** AudioCraft Plus is an all-in-one WebUI for the original AudioCraft, adding many quality features on top https://github.com/GrandaddyShmax/audiocraft_plus
- **Original git URL:** https://github.com/pinokiofactory/audiocraft_plus
- **Analyzed commit:** `a8e0d2731e8dbb7185a4a0ffd53b495d003586ab`
- **Platforms supported:** NVIDIA / AMD / Mac
- **Porting difficulty:** Low–medium
- **CUDA-only packages:** triton-windows, xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

av, demucs, einops, encodec, fastapi, flashy, gradio, gradio-client, huggingface-hub, hydra-colorlog, hydra-core, julius, librosa, num2words, numpy, pytaglib, sentencepiece, spacy, torch, torch-directml, torchaudio, torchmetrics, torchvision, tqdm, transformers, triton-windows, wheel, xformers

Requirements files: `requirements.txt`.

Wheel indexes referenced: cpu, cu128, rocm6.3.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 297
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- `torch.js` routes present: nvidia, amd, mac, cpu.
- Requirements from: requirements.txt
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): xformers
- Difficulty score: 2.5 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- blocked by spacy build failure on Python 3.14.
- Result: **not runnable in this container.**

## CPU port attempt

- **Attempt order:** #47 of 101 (by porting effort, easiest first).
- **Status:** CPU-capable (shipped fallback).
- **Changes applied / required:** use existing CPU wheel branch in torch.js; use existing non-NVIDIA/non-AMD branch in torch.js; use existing non-GPU launcher route; substitute GPU-only attention libs with SDPA math backend.
- **Smoke check:** n/a (no Python source in snapshot).
- **Blockers:** GPU-only attention: triton-windows/xformers.
- **Scope note:** static portability review of the Pinokio wrapper; no install or model download was executed.
