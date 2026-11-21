# florence-sam — portability analysis

- **Package name:** florence-sam (`florence-sam`)
- **Description:** Integrates Florence2 and SAM2 models for detailed image captioning and object detection. Florence2 generates detailed captions that are then used to perform phrase grounding. The Segment Anything Model 2 (SAM2) converts these phrase-grounded boxes into masks. https://huggingface.co/spaces/SkalskiP/f
- **Original git URL:** https://github.com/pinokiofactory/florence-sam
- **Analyzed commit:** `3cca86f7edf8e94daae4339727f202895306c021`
- **Platforms supported:** NVIDIA / AMD / Mac
- **Porting difficulty:** Medium
- **CUDA-only packages:** cudnn, xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

cudnn, devicetorch, gradio, torch, torch-directml, torchaudio, torchvision, transformers, xformers

Wheel indexes referenced: cpu, cu121, rocm6.0.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 271
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- `torch.js` routes present: nvidia, amd, mac, cpu.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): xformers
- Difficulty score: 3.0 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- blocked by transformers API mismatch (AutoProcessor).
- Result: **not runnable in this container.**

## CPU port attempt

- **Attempt order:** #54 of 101 (by porting effort, easiest first).
- **Status:** CPU-capable (shipped fallback).
- **Changes applied / required:** use existing CPU wheel branch in torch.js; use existing non-NVIDIA/non-AMD branch in torch.js; use existing non-GPU launcher route; rely on devicetorch (already present); substitute GPU-only attention libs with SDPA math backend; remove GPU runtimes (onnxruntime-gpu/deepspeed/cudnn/tensorrt).
- **Smoke check:** n/a (no Python source in snapshot).
- **Blockers:** GPU-only attention: xformers; GPU runtime: cudnn.
- **Scope note:** static portability review of the Pinokio wrapper; no install or model download was executed.
