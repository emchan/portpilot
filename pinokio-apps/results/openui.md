# openui — portability analysis

- **Package name:** openui (`openui`)
- **Description:** Describe UI and see it rendered live. Ask for changes and convert HTML to React, Svelte, Web Components, etc. Like vercel v0, but open source https://github.com/wandb/openui
- **Original git URL:** https://github.com/pinokiofactory/openui
- **Analyzed commit:** `83ab6b5534ee0500674a6e2872e235092310cd9d`
- **Platforms supported:** Cross-platform
- **Porting difficulty:** Low
- **CUDA-only packages:** —

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

tiktoken

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 295
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- `torch.js` routes present: none.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Difficulty score: 0.0 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).
