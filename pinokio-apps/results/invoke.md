# invoke — portability analysis

- **Package name:** Invoke (`invoke`)
- **Description:** The Gen AI Platform for Pro Studios https://github.com/invoke-ai/InvokeAI
- **Original git URL:** https://github.com/pinokiofactory/invoke
- **Analyzed commit:** `67ac5a161a265badb1ff73d46c41f762c16bff35`
- **Platforms supported:** NVIDIA / AMD / Mac
- **Porting difficulty:** Low
- **CUDA-only packages:** —

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

invokeai

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 275
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- `torch.js` routes present: nvidia, amd, mac.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Difficulty score: 0.0 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- All JS files pass node --check. Upstream InvokeAI download is very large; not downloaded/tested in this container.
- Result: **static verification only.**

## CPU port attempt

- **Attempt order:** #7 of 101 (by porting effort, easiest first).
- **Status:** CPU-capable (shipped fallback).
- **Changes applied / required:** use existing non-NVIDIA/non-AMD branch in torch.js; use existing non-GPU launcher route.
- **Smoke check:** n/a (no Python source in snapshot).
- **Blockers:** none identified.
- **Scope note:** static portability review of the Pinokio wrapper; no install or model download was executed.
