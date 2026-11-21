# hertz — portability analysis

- **Package name:** hertz (`hertz`)
- **Description:** # hertz
- **Original git URL:** https://github.com/pinokiofactory/hertz
- **Analyzed commit:** `306ecc634eea5a51a3d20729d44cc94f5650d45d`
- **Platforms supported:** NVIDIA / AMD / Mac
- **Porting difficulty:** Low
- **CUDA-only packages:** —

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

ipython, matplotlib, model, numpy, tokenizer, torch, torch-directml, torchaudio, torchvision, utils

Third-party Python imports detected in local source: ipython, matplotlib, model, tokenizer, torch, torchaudio, utils.

Wheel indexes referenced: cu121, nightly.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 476
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- `torch.js` routes present: nvidia, amd, mac.
- No requirements file; third-party Python imports used as a fallback signal.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Difficulty score: 0.0 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-20)

- Downloaded upstream `peanutcocktail/hertz-dev`; installed CPU torch plus `requirements.txt`.
- Patched `app.py`: `device='cpu'`, removed `T.cuda.set_device(0)`, `autocast(device_type='cpu')`, dropped the BF16 `.to()` cast.
- Run completed and downloaded `inference_apatosaurus_95000.pt`; no runtime error after the patches.
- Result: **CPU port works with source patches.**

## CPU port attempt

- **Attempt order:** #40 of 101 (by porting effort, easiest first).
- **Status:** CPU-capable (shipped fallback).
- **Changes applied / required:** use existing non-NVIDIA/non-AMD branch in torch.js; use existing non-GPU launcher route; keep explicit device='cpu' branch; replace direct torch.cuda calls with devicetorch or cpu fallback.
- **Smoke check:** pass (1/1 files).
- **Blockers:** direct torch.cuda calls.
- **Scope note:** static portability review of the Pinokio wrapper; no install or model download was executed.
