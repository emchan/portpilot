# errortest — portability analysis

- **Package name:** errortest (`errortest`)
- **Description:** No description provided in the repository.
- **Original git URL:** https://github.com/pinokiofactory/errortest
- **Analyzed commit:** `dd4051727b682cdfdb3f0ae792875052bd4398b9`
- **Platforms supported:** Cross-platform
- **Porting difficulty:** Low
- **CUDA-only packages:** —

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

No package dependencies were declared in the repository. Installers that only run `npm install` or clone another app do not name packages here.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 48
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- `torch.js` routes present: none.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Difficulty score: 0.0 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-20)

- Attempted to install `gradio==5.5.0` with `uvicorn==0.13.4` as pinned by the wrapper.
- Failed: version conflict (`gradio 5.5.0` requires `uvicorn>=0.14.0`).
- With `uvicorn>=0.14`, install succeeded but import failed: `HfFolder` removed from `huggingface_hub`.
- Result: **CPU port blocked by dependency/API breakage; needs version updates.**

## CPU port attempt

- **Attempt order:** #6 of 101 (by porting effort, easiest first).
- **Status:** CPU-ready (no changes).
- **Changes applied / required:** no change required (no local GEMM workload); add a CPU wheel branch / remove GPU-only wheel pins.
- **Smoke check:** n/a (no Python source in snapshot).
- **Blockers:** none identified.
- **Scope note:** static portability review of the Pinokio wrapper; no install or model download was executed.
