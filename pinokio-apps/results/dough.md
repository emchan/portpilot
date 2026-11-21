# dough — portability analysis

- **Package name:** Dough (`dough`)
- **Description:** Dough is a open source tool for steering AI animations with precision
- **Original git URL:** https://github.com/pinokiofactory/dough
- **Analyzed commit:** `3e8a58b5da380ec15cd5743ffc57d220a64fdae1`
- **Platforms supported:** NVIDIA only
- **Porting difficulty:** Medium
- **CUDA-only packages:** torch (CUDA wheel)

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

torch, torchaudio, torchvision

Wheel indexes referenced: cu118.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 240
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- `torch.js` routes present: none.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Difficulty score: 4.0 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- blocked by Python 3.14-incompatible pinned requirements (numpy 1.24.4, Pillow 9.4.0, streamlit 1.27.0).
- Result: **not runnable in this container.**

## CPU port attempt

- **Attempt order:** #69 of 101 (by porting effort, easiest first).
- **Status:** Needs launcher change.
- **Changes applied / required:** add a CPU wheel branch / remove GPU-only wheel pins; replace CUDA-only torch wheel with CPU wheel.
- **Smoke check:** pass (1/1 files).
- **Blockers:** no CPU/AMD launcher branch; CUDA-only torch wheel.
- **Scope note:** static portability review of the Pinokio wrapper; no install or model download was executed.
