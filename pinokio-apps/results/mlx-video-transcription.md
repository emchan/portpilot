# mlx-video-transcription — portability analysis

- **Package name:** MLX-Video-Transcription (`mlx-video-transcription`)
- **Description:** [Mac Only] Super Fast MLX Powered Video Transcription https://github.com/RayFernando1337/MLX-Auto-Subtitled-Video-Generator/ by https://x.com/RayFernando1337
- **Original git URL:** https://github.com/pinokiofactory/mlx-video-transcription
- **Analyzed commit:** `331245a916c9eb1602637a5cedebf83eb2322ee5`
- **Platforms supported:** Mac (Apple Silicon) only
- **Porting difficulty:** Low
- **CUDA-only packages:** —

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

No package dependencies were declared in the repository. Installers that only run `npm install` or clone another app do not name packages here.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 174
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- Explicit platform tag found: Mac (Apple Silicon) only.
- `torch.js` routes present: none.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Difficulty score: 1.0 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).
