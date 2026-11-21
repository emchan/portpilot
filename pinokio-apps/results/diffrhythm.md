# diffrhythm — portability analysis

- **Package name:** DiffRhythm (`diffrhythm`)
- **Description:** Generate songs with AI (up to 4 min 45 sec). Both with lyrics or instrumental https://github.com/ASLP-lab/DiffRhythm
- **Original git URL:** https://github.com/pinokiofactory/diffrhythm
- **Analyzed commit:** `15166cfd3b677d7fd6294b4d9fb88e7f4845d3ee`
- **Platforms supported:** NVIDIA / AMD / Mac
- **Porting difficulty:** High
- **CUDA-only packages:** bitsandbytes, onnxruntime-gpu, triton *(optional)*, triton-windows, xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

accelerate, bitsandbytes, cn2an, ema-pytorch, espeak-ng, jieba, langsegment, libaio-dev, librosa, muq, mutagen, numpy, onnxruntime, onnxruntime-gpu, openai, pandas, phonemizer, prefigure, pyarrow, pykakasi, pylance, pyopenjtalk, pypinyin, spaces, torch, torch-directml, torchaudio, torchdiffeq, torchvision, transformers, triton, triton-windows, unidecode, x-transformers, xformers

Requirements files: `requirements.txt`.

Wheel indexes referenced: cpu, cu128, rocm6.3.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 409
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- `torch.js` routes present: nvidia, amd, mac, cpu.
- Requirements from: requirements.txt
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): triton, xformers
- Difficulty score: 7.8 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- blocked by pandas build failure on Python 3.14.
- Result: **not runnable in this container.**

## CPU port attempt

- **Attempt order:** #83 of 101 (by porting effort, easiest first).
- **Status:** CPU-capable (shipped fallback).
- **Changes applied / required:** use existing CPU wheel branch in torch.js; use existing non-NVIDIA/non-AMD branch in torch.js; use existing non-GPU launcher route; substitute GPU-only attention libs with SDPA math backend; remove bitsandbytes/torchao GPU quantisers or switch to GGUF; remove GPU runtimes (onnxruntime-gpu/deepspeed/cudnn/tensorrt).
- **Smoke check:** n/a (no Python source in snapshot).
- **Blockers:** GPU-only attention: triton/triton-windows/xformers; GPU quantisers: bitsandbytes; GPU runtime: onnxruntime-gpu.
- **Scope note:** static portability review of the Pinokio wrapper; no install or model download was executed.
