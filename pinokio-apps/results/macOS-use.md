# macOS-use — portability analysis

- **Package name:** macOS-use (`macOS-use`)
- **Description:** [Mac Only] We make AI agents that control Mac apps: https://github.com/browser-use/macOS-use
- **Original git URL:** https://github.com/pinokiofactory/macOS-use
- **Analyzed commit:** `7417e3a1c1c5f38ec665d4c8ceb31857d8939bc4`
- **Platforms supported:** Mac (Apple Silicon) only
- **Porting difficulty:** Low
- **CUDA-only packages:** —

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

gradio

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 225
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- Explicit platform tag found: Mac (Apple Silicon) only.
- `torch.js` routes present: none.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Difficulty score: 1.0 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).
