# bolt — portability analysis

- **Package name:** bolt.diy (`bolt`)
- **Description:** Prompt, run, edit, and deploy full-stack web apps. https://github.com/stackblitz-labs/bolt.diy
- **Original git URL:** https://github.com/pinokiofactory/bolt
- **Analyzed commit:** `e78682b26d423a3e26fe8c120521eddb6411d78b`
- **Platforms supported:** Cross-platform
- **Porting difficulty:** Low
- **CUDA-only packages:** —

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

litellm, wrangler

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 446
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- `torch.js` routes present: none.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Difficulty score: 0.0 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).
