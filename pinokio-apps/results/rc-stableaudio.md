# rc-stableaudio — portability analysis

- **Package name:** RC Stable Audio Tools (`rc-stableaudio`)
- **Description:** Advanced Gradio UI for Stable Audio https://github.com/RoyalCities/RC-stable-audio-tools
- **Original git URL:** https://github.com/pinokiofactory/rc-stableaudio
- **Analyzed commit:** `b3a7d5abecbee8fed08717405830126911825e81`
- **Platforms supported:** NVIDIA / AMD / Mac
- **Porting difficulty:** High
- **CUDA-only packages:** flash-attn, sageattention *(optional)*, triton *(optional)*, triton-windows, xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

flash-attn, gradio, libsndfile, numpy, sageattention, torch, torch-directml, torchaudio, torchvision, triton, triton-windows, xformers

Wheel indexes referenced: cpu, cu128, rocm6.3.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 349
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- `torch.js` routes present: nvidia, amd, mac, cpu.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): sageattention, triton, xformers
- Difficulty score: 7.8 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).
