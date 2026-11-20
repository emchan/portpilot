# aura-sr-upscaler — portability analysis

- **Package name:** aura-sr-upscaler (`aura-sr-upscaler`)
- **Description:** AuraSR-v2 - An open reproduction of the GigaGAN Upscaler from fal.ai https://huggingface.co/spaces/gokaygokay/AuraSR-v2
- **Original git URL:** https://github.com/pinokiofactory/aura-sr-upscaler
- **Analyzed commit:** `9357cf93dac1f28179bb5d32c98b1c5c75a61ece`
- **Platforms supported:** NVIDIA / AMD / Mac
- **Porting difficulty:** High
- **CUDA-only packages:** flash-attn, sageattention *(optional)*, triton *(optional)*, triton-windows, xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

devicetorch, flash-attn, gradio, hf-xet, numpy, sageattention, torch, torch-directml, torchaudio, torchvision, triton, triton-windows, xformers

Wheel indexes referenced: cpu, cu128, rocm6.3.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 289
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- `torch.js` routes present: nvidia, amd, mac, cpu.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): sageattention, triton, xformers
- Difficulty score: 7.8 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).
