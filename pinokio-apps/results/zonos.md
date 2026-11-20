# zonos — portability analysis

- **Package name:** zonos (`zonos`)
- **Description:** Zonos-v0.1 is a leading open-weight text-to-speech model trained on more than 200k hours of varied multilingual speech, delivering expressiveness and quality on par with—or even surpassing—top TTS providers. https://github.com/Zyphra/Zonos
- **Original git URL:** https://github.com/pinokiofactory/zonos
- **Analyzed commit:** `0be13e4e803fe0834bae8326240633ac8e53bffc`
- **Platforms supported:** NVIDIA / AMD / Mac
- **Porting difficulty:** High
- **CUDA-only packages:** flash-attn, triton, triton-windows, xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

espeak-ng, flash-attn, gradio, hf-xet, libaio-dev, numpy, sympy, torch, torch-directml, torchaudio, torchvision, triton, triton-windows, wheel, xformers

Third-party Python imports detected in local source: sympy, torch, triton.

Wheel indexes referenced: cpu, cu128, rocm6.3.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 7276
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- `torch.js` routes present: nvidia, amd, mac, cpu.
- No requirements file; third-party Python imports used as a fallback signal.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): xformers
- Difficulty score: 7.0 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).
