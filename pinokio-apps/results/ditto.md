# ditto — portability analysis

- **Package name:** ditto (`ditto`)
- **Description:** the simplest self-building coding agent https://github.com/yoheinakajima/ditto
- **Original git URL:** https://github.com/pinokiofactory/ditto
- **Analyzed commit:** `aa45279201a7ddaead5ac33d56feba35417319c5`
- **Platforms supported:** Cross-platform
- **Porting difficulty:** Low
- **CUDA-only packages:** —

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

flask, litellm

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 204
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- `torch.js` routes present: none.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Difficulty score: 0.0 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-20)

- Downloaded upstream `yoheinakajima/ditto`; installed dependencies on CPU.
- Pinned `litellm` could not be satisfied on Python 3.14, so installed the current `litellm` release plus `flask`.
- Flask app started successfully on `http://127.0.0.1:8080`.
- Result: **CPU port works with dependency updates.**

## CPU port attempt

- **Attempt order:** #5 of 101 (by porting effort, easiest first).
- **Status:** CPU-ready (no changes).
- **Changes applied / required:** no change required (no local GEMM workload); add a CPU wheel branch / remove GPU-only wheel pins.
- **Smoke check:** n/a (no Python source in snapshot).
- **Blockers:** none identified.
- **Scope note:** static portability review of the Pinokio wrapper; no install or model download was executed.
