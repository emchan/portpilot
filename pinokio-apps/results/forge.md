# forge — portability analysis

- **Package name:** Stable Diffusion Forge (`forge`)
- **Description:** Stable Diffusion WebUI Forge is a platform on top of Stable Diffusion WebUI (based on Gradio) to make development easier, optimize resource management, and speed up inference. https://github.com/lllyasviel/stable-diffusion-webui-forge?tab=readme-ov-file
- **Original git URL:** https://github.com/pinokiofactory/forge
- **Analyzed commit:** `e3378c35f7f1c4fec2f600c33b9d17ab6d330b4c`
- **Platforms supported:** Cross-platform
- **Porting difficulty:** Low
- **CUDA-only packages:** —

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

No package dependencies were declared in the repository. Installers that only run `npm install` or clone another app do not name packages here.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 323
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- `torch.js` routes present: none.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Difficulty score: 0.0 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- blocked by numpy build failure on Python 3.14.
- Result: **not runnable in this container.**

## CPU port attempt

- **Attempt order:** #46 of 101 (by porting effort, easiest first).
- **Status:** Needs launcher change.
- **Changes applied / required:** add a CPU wheel branch / remove GPU-only wheel pins; tune oneDNN/MKL threads for FP16/BF16 GEMMs.
- **Smoke check:** n/a (no Python source in snapshot).
- **Blockers:** no CPU/AMD launcher branch.
- **Scope note:** static portability review of the Pinokio wrapper; no install or model download was executed.
