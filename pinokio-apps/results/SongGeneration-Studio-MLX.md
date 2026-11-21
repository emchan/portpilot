# SongGeneration-Studio-MLX — portability analysis

- **Package name:** SongGeneration Studio MLX (`SongGeneration-Studio-MLX`)
- **Description:** MLX-only song generation studio with lyrics+style AI and auto model downloads.
- **Original git URL:** https://github.com/pinokiofactory/SongGeneration-Studio-MLX
- **Analyzed commit:** `49e365c88512ffd1a4bf17d800c5508e7d5781da`
- **Platforms supported:** Mac (Apple Silicon) only
- **Porting difficulty:** Low
- **CUDA-only packages:** —

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

No package dependencies were declared in the repository. Installers that only run `npm install` or clone another app do not name packages here.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 195
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- Explicit platform tag found: Mac (Apple Silicon) only.
- `torch.js` routes present: none.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Difficulty score: 1.0 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- requires MLX/Apple Silicon; cannot run on Linux CPU.
- Result: **not runnable in this container.**

## CPU port attempt

- **Attempt order:** #62 of 101 (by porting effort, easiest first).
- **Status:** Blocked (Apple-only).
- **Changes applied / required:** no change identified.
- **Smoke check:** n/a (no Python source in snapshot).
- **Blockers:** Apple-silicon-only MLX runtime.
- **Scope note:** static portability review of the Pinokio wrapper; no install or model download was executed.
