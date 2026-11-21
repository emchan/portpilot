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

## CPU test run (2026-11-21)

- Installed on Python 3.12 with huggingface_hub==0.25.2; gradio and uvicorn import successfully.
- Result: **CPU port works with dependency/version fixes.**
