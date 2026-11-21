# LTX-Desktop-WanGP — portability analysis

- **Package name:** LTX-Desktop-WanGP (`LTX-Desktop-WanGP`)
- **Description:** [NVIDIA only] [Currently Windows only] LTX-Desktop powered By WanGP itself powered among other things by LTX-2 Engine
- **Original git URL:** https://github.com/pinokiofactory/LTX-Desktop-WanGP
- **Analyzed commit:** `2a3fedd030e9c7c12f9f67a14466007319ecc3d5`
- **Platforms supported:** NVIDIA only
- **Porting difficulty:** Medium
- **CUDA-only packages:** —

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

No package dependencies were declared in the repository. Installers that only run `npm install` or clone another app do not name packages here.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 182
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- Explicit platform tag found: NVIDIA only.
- `torch.js` routes present: none.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Difficulty score: 3.0 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- setup:dev:linux hung/timed out in this container.
- Result: **not runnable in this container.**

## CPU port attempt

- **Attempt order:** #58 of 101 (by porting effort, easiest first).
- **Status:** Needs launcher change.
- **Changes applied / required:** add a CPU wheel branch / remove GPU-only wheel pins.
- **Smoke check:** n/a (no Python source in snapshot).
- **Blockers:** no CPU/AMD launcher branch.
- **Scope note:** static portability review of the Pinokio wrapper; no install or model download was executed.
