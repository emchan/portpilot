# ovis — portability analysis

- **Package name:** Ovis-Image 7B (`ovis`)
- **Description:** Generate text-accurate images with the official Ovis-Image-7B diffusers pipeline.
- **Original git URL:** https://github.com/pinokiofactory/ovis
- **Analyzed commit:** `00a570258ba7370090037bb14bcfa67e1e81194e`
- **Platforms supported:** NVIDIA only
- **Porting difficulty:** Medium
- **CUDA-only packages:** torch (CUDA wheel)

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

accelerate, gradio, huggingface-hub, numpy, pillow, safetensors, sentencepiece, torch, torchaudio, torchvision, transformers

Requirements files: `app/requirements.txt`.

Third-party Python imports detected in local source: diffusers, gradio, torch.

Wheel indexes referenced: cpu, cu121, cu124, rocm6.0.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 383
- **CUDA-related functions used:** `torch.cuda.is_available`

## Evidence and notes

- `torch.js` routes present: none.
- Requirements from: app/requirements.txt
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Difficulty score: 4.0 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- dependencies installed and app.py imported successfully on CPU.
- Result: **CPU port imports successfully.**

## CPU port attempt

- **Attempt order:** #60 of 101 (by porting effort, easiest first).
- **Status:** CPU-capable (shipped fallback).
- **Changes applied / required:** use existing CPU wheel branch in torch.js; use existing non-NVIDIA/non-AMD branch in torch.js; use existing non-GPU launcher route; keep explicit device='cpu' branch; replace direct torch.cuda calls with devicetorch or cpu fallback; replace CUDA-only torch wheel with CPU wheel; +1.
- **Smoke check:** pass (1/1 files).
- **Blockers:** CUDA-only torch wheel; direct torch.cuda calls; MPS branch Apple-only.
- **Scope note:** static portability review of the Pinokio wrapper; no install or model download was executed.
