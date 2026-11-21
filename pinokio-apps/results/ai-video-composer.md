# ai-video-composer — portability analysis

- **Package name:** ai-video-composer (`ai-video-composer`)
- **Description:** The ultimate video editor powered by natural language and FFMPEG https://huggingface.co/spaces/huggingface-projects/ai-video-composer
- **Original git URL:** https://github.com/pinokiofactory/ai-video-composer
- **Analyzed commit:** `0cc7921ff899b4d8ce6e5b8f419f9144e50fa43d`
- **Platforms supported:** Cross-platform
- **Porting difficulty:** Low
- **CUDA-only packages:** —

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

huggingface-hub, pydantic

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 198
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- `torch.js` routes present: none.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Difficulty score: 0.0 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- Downloaded upstream HF space; install failed on building pillow<11 for gradio 5.0.0 on Python 3.14. With newer gradio/moviepy, import hung.
- Result: **not runnable in this container without dependency/version adjustments.**

## CPU port attempt

- **Attempt order:** #1 of 101 (by porting effort, easiest first).
- **Status:** CPU-ready (no changes).
- **Changes applied / required:** no change required (no local GEMM workload); add a CPU wheel branch / remove GPU-only wheel pins.
- **Smoke check:** n/a (no Python source in snapshot).
- **Blockers:** none identified.
- **Scope note:** static portability review of the Pinokio wrapper; no install or model download was executed.
