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

- retested on Python 3.10; import app.py failed with botocore NoCredentialsError (AWS credentials missing).
- Result: **not runnable in this container.**
