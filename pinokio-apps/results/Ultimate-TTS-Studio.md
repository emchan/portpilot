# Ultimate-TTS-Studio — portability analysis

- **Package name:** Ultimate-TTS-Studio (`Ultimate-TTS-Studio`)
- **Description:** Kokoro, KittenTTS, Higgs audio, Chatterbox/Multi, Fish-Speech, F5 & index-tts & indextts2, VoxCPM and VibeVoice in one app
- **Original git URL:** https://github.com/pinokiofactory/Ultimate-TTS-Studio
- **Analyzed commit:** `b8c15efaead5a5e8744783fd443466333d2b1805`
- **Platforms supported:** NVIDIA only
- **Porting difficulty:** Very high
- **CUDA-only packages:** flash-attn, onnxruntime-gpu, sageattention *(optional)*, triton *(optional)*, triton-windows, xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

devicetorch, espeak-ng, flash-attn, gradio, libaio-dev, libsox-fmt-all, numpy, onnxruntime-gpu, openai-whisper, phonemizer-fork, portaudio, pynini, sageattention, setuptools, sox, torch, torch-directml, torchaudio, torchvision, triton, triton-windows, voxcpm, wetextprocessing, xformers

Wheel indexes referenced: cpu, cu128, rocm6.3.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 374
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- Explicit platform tag found: NVIDIA only.
- `torch.js` routes present: nvidia, amd, mac, cpu.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): sageattention, triton, xformers
- Difficulty score: 12.8 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).
