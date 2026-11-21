# MFLUX-WEBUI — portability analysis

- **Package name:** MFLUX-WEBUI (`MFLUX-WEBUI`)
- **Description:** [MAC ONLY] A powerful and user-friendly web interface for FLUX, powered by MLX and Gradio via MFLUX
- **Original git URL:** https://github.com/pinokiofactory/MFLUX-WEBUI
- **Analyzed commit:** `62b3f9364abf53951cfdfb3c2e872d470d5baa4a`
- **Platforms supported:** Mac (Apple Silicon) only
- **Porting difficulty:** Low
- **CUDA-only packages:** —

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

No package dependencies were declared in the repository. Installers that only run `npm install` or clone another app do not name packages here.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 254
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- Explicit platform tag found: Mac (Apple Silicon) only.
- `torch.js` routes present: none.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Difficulty score: 1.0 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- requires MLX/Apple Silicon and Python 3.12; cannot run on this Linux CPU container.
- Result: **not runnable in this container.**

## CPU port attempt

- **Attempt order:** #61 of 101 (by porting effort, easiest first).
- **Status:** Blocked (Apple-only).
- **Changes applied / required:** no change identified.
- **Smoke check:** n/a (no Python source in snapshot).
- **Blockers:** Apple-silicon-only MLX runtime.
- **Scope note:** static portability review of the Pinokio wrapper; no install or model download was executed.
