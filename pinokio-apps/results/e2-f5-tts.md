# e2-f5-tts — portability analysis

- **Package name:** e2-f5-tts (`e2-f5-tts`)
- **Description:** F5-TTS: A Fairytaler that Fakes Fluent and Faithful Speech with Flow Matching https://huggingface.co/spaces/mrfakename/E2-F5-TTS
- **Original git URL:** https://github.com/pinokiofactory/e2-f5-tts
- **Analyzed commit:** `f871e54167835552efa88b366388b299f50c36af`
- **Platforms supported:** NVIDIA / AMD / Mac
- **Porting difficulty:** Low
- **CUDA-only packages:** xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

hf-xet, numpy, torch, torchaudio, torchvision, xformers

Wheel indexes referenced: cpu, cu128, rocm6.3.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 462
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- `torch.js` routes present: nvidia, amd, mac, cpu.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): xformers
- Difficulty score: 0.5 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).
