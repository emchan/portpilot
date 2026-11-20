# stableaudio — portability analysis

- **Package name:** StableAudio (`stableaudio`)
- **Description:** An Open Source Model for Audio Samples and Sound Design https://github.com/Stability-AI/stable-audio-tools
- **Original git URL:** https://github.com/pinokiofactory/stableaudio
- **Analyzed commit:** `14c9fbb56ef0054d8fae55bcee825216d30be047`
- **Platforms supported:** NVIDIA / AMD / Mac
- **Porting difficulty:** Low
- **CUDA-only packages:** xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

devicetorch, gradio, hf-xet, libsndfile, numpy, soxr, torch, torch-directml, torchaudio, torchvision, xformers

Wheel indexes referenced: cpu, cu128, rocm6.3.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 324
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- `torch.js` routes present: nvidia, amd, mac, cpu.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): xformers
- Difficulty score: 0.5 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).
