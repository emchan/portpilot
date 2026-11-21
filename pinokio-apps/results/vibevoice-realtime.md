# vibevoice-realtime — portability analysis

- **Package name:** VibeVoice Realtime (`vibevoice-realtime`)
- **Description:** Realtime streaming TTS demo using microsoft/VibeVoice-Realtime-0.5B
- **Original git URL:** https://github.com/pinokiofactory/vibevoice-realtime
- **Analyzed commit:** `e8f4b7bd22f65e45b19cd4e67cd0c1a982109102`
- **Platforms supported:** NVIDIA / AMD / Mac
- **Porting difficulty:** Low
- **CUDA-only packages:** —

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

numpy, torch, torch-directml, torchaudio, torchvision

Wheel indexes referenced: cpu, cu128, rocm6.3.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 320
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- `torch.js` routes present: nvidia, amd, mac, cpu.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Difficulty score: 0.0 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-20)

- Downloaded upstream `microsoft/VibeVoice`; installed CPU torch and package.
- First run failed on `torch.load(..., weights_only=True)` for cached voice presets.
- Patched `demo/web/app.py` to `weights_only=False`; demo then started on `http://0.0.0.0:3000`.
- Result: **CPU port works with a source patch.**

## CPU port attempt

- **Attempt order:** #12 of 101 (by porting effort, easiest first).
- **Status:** CPU-capable (shipped fallback).
- **Changes applied / required:** use existing CPU wheel branch in torch.js; use existing non-GPU launcher route; keep explicit device='cpu' branch; tune oneDNN/MKL threads for FP16/BF16 GEMMs.
- **Smoke check:** n/a (no Python source in snapshot).
- **Blockers:** none identified.
- **Scope note:** static portability review of the Pinokio wrapper; no install or model download was executed.
