# MagicQuill — portability analysis

- **Package name:** MagicQuill (`MagicQuill`)
- **Description:** An intelligent, interactive Image Editing System. Easily erase and add objects on a user-friendly interface.
- **Original git URL:** https://github.com/pinokiofactory/MagicQuill
- **Analyzed commit:** `bfdae2847a85d7b00761b4e93fbcb91be5e6d494`
- **Platforms supported:** NVIDIA / AMD / Mac
- **Porting difficulty:** Medium
- **CUDA-only packages:** bitsandbytes, xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

bitsandbytes, huggingface-hub, numpy, torch, torch-directml, torchaudio, torchvision, xformers

Wheel indexes referenced: cpu, cu128, rocm6.3.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 357
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- `torch.js` routes present: nvidia, amd, mac, cpu.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): xformers
- Difficulty score: 3.0 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- Install completed but runtime blocked by gradio/huggingface_hub HfFolder incompatibility.
- Result: **not runnable in this container.**

## CPU port attempt

- **Attempt order:** #53 of 101 (by porting effort, easiest first).
- **Status:** CPU-capable (shipped fallback).
- **Changes applied / required:** use existing CPU wheel branch in torch.js; use existing non-NVIDIA/non-AMD branch in torch.js; use existing non-GPU launcher route; substitute GPU-only attention libs with SDPA math backend; remove bitsandbytes/torchao GPU quantisers or switch to GGUF; tune oneDNN/MKL threads for FP16/BF16 GEMMs.
- **Smoke check:** n/a (no Python source in snapshot).
- **Blockers:** GPU-only attention: xformers; GPU quantisers: bitsandbytes.
- **Scope note:** static portability review of the Pinokio wrapper; no install or model download was executed.
