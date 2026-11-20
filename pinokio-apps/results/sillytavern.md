# sillytavern — portability analysis

- **Package name:** SillyTavern (`sillytavern`)
- **Description:** a local-install interface that allows you to interact with text generation AIs (LLMs) to chat and roleplay with custom characters. https://docs.sillytavern.app/
- **Original git URL:** https://github.com/pinokiofactory/sillytavern
- **Analyzed commit:** `f75be07a853a78f0a9369d2faeec4518c553241a`
- **Platforms supported:** Cross-platform
- **Porting difficulty:** Low
- **CUDA-only packages:** —

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

No package dependencies were declared in the repository. Installers that only run `npm install` or clone another app do not name packages here.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 184
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- `torch.js` routes present: none.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Difficulty score: 0.0 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).
