# vibevoice-realtime — portability analysis

- **Package name:** VibeVoice Realtime (`vibevoice-realtime`)
- **Description:** Realtime streaming TTS demo using microsoft/VibeVoice-Realtime-0.5B
- **Original git URL:** https://github.com/pinokiofactory/vibevoice-realtime
- **Analyzed commit:** `e8f4b7bd22f65e45b19cd4e67cd0c1a982109102`
- **Platforms supported:** NVIDIA / AMD / Mac
- **Porting difficulty:** Low
- **CUDA-only packages:** —

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

numpy, torch, torch-directml, torchaudio, torchvision

Wheel indexes referenced: cpu, cu128, rocm6.3.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 320
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- `torch.js` routes present: nvidia, amd, mac, cpu.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Difficulty score: 0.0 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).
