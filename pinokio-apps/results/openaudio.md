# openaudio — portability analysis

- **Package name:** OpenAudio (`openaudio`)
- **Description:** Multilingual Text-to-Speech with Voice Cloning (Supports: English, Japanese, Korean, Chinese, French, German, Arabic, and Spanish) https://github.com/fishaudio/fish-speech
- **Original git URL:** https://github.com/pinokiofactory/openaudio
- **Analyzed commit:** `6a69e7903d7430cc3d08dae6673caf85b9032fcf`
- **Platforms supported:** NVIDIA / AMD / Mac
- **Porting difficulty:** High
- **CUDA-only packages:** flash-attn, sageattention *(optional)*, triton *(optional)*, triton-windows, xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

cachetools, flash-attn, gradio, livekit, livekit-agents, numpy, portaudio, sageattention, torch, torch-directml, torchaudio, torchvision, triton, triton-windows, xformers

Wheel indexes referenced: cpu, cu128, rocm6.3.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 313
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- `torch.js` routes present: nvidia, amd, mac, cpu.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): sageattention, triton, xformers
- Difficulty score: 7.8 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).
