# liveportrait — portability analysis

- **Package name:** LivePortrait (`liveportrait`)
- **Description:** Bring portraits to life! https://github.com/KwaiVGI/LivePortrait
- **Original git URL:** https://github.com/pinokiofactory/liveportrait
- **Analyzed commit:** `b5fb16ce6df50e79d11d7c1a2d7b39faa720411e`
- **Platforms supported:** NVIDIA / AMD / Mac
- **Porting difficulty:** Low–medium
- **CUDA-only packages:** onnxruntime-gpu, xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

install, onnxruntime-gpu, torch, torch-directml, torchaudio, torchvision, xformers

Wheel indexes referenced: cpu, cu128, rocm6.0.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 388
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- `torch.js` routes present: nvidia, amd, mac, cpu.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): xformers
- Difficulty score: 2.5 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).
