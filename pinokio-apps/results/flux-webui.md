# flux-webui — portability analysis

- **Package name:** flux-webui (`flux-webui`)
- **Description:** Minimal Flux Web UI powered by Gradio & Diffusers (Flux Schnell + Flux Merged)
- **Original git URL:** https://github.com/pinokiofactory/flux-webui
- **Analyzed commit:** `62d2f5692da1e0aaf776c3dceef0a720a6a24bb6`
- **Platforms supported:** NVIDIA / AMD / Mac
- **Porting difficulty:** High
- **CUDA-only packages:** flash-attn, sageattention *(optional)*, triton *(optional)*, triton-windows, xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

devicetorch, flash-attn, gradio, hf-xet, numpy, protobuf, sageattention, sentencepiece, torch, torch-directml, torchaudio, torchvision, transformers, triton, triton-windows, xformers

Requirements files: `requirements.txt`.

Third-party Python imports detected in local source: devicetorch, diffusers, gradio, numpy, optimum, pil, torch, transformers.

Wheel indexes referenced: cpu, cu128, rocm6.3.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 487
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- `torch.js` routes present: nvidia, amd, mac, cpu.
- Requirements from: requirements.txt
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): sageattention, triton, xformers
- Difficulty score: 7.8 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).
