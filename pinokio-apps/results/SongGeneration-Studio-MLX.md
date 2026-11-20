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
