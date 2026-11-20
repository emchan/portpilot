# omnigen — portability analysis

- **Package name:** omnigen (`omnigen`)
- **Description:** A unified image generation model that you can use to perform various tasks, including but not limited to text-to-image generation, subject-driven generation, Identity-Preserving Generation, and image-conditioned generation. https://huggingface.co/spaces/Shitao/OmniGen
- **Original git URL:** https://github.com/pinokiofactory/omnigen
- **Analyzed commit:** `07de8c2c3944d3852bcab55d2f2c4d74bd245532`
- **Platforms supported:** NVIDIA / AMD / Mac
- **Porting difficulty:** Low–medium
- **CUDA-only packages:** triton-windows, xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

gradio, numpy, spaces, torch, torch-directml, torchaudio, torchvision, triton-windows, xformers

Wheel indexes referenced: cpu, cu128, rocm6.3.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 291
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- `torch.js` routes present: nvidia, amd, mac, cpu.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): triton, xformers
- Difficulty score: 2.5 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).
