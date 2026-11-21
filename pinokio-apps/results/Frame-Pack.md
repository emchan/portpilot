# Frame-Pack — portability analysis

- **Package name:** FramePack (`Frame-Pack`)
- **Description:** [NVIDIA ONLY] Generate Video Progressively. FramePack is a next-frame (next-frame-section) prediction neural network structure that generates videos progressively. https://github.com/lllyasviel/FramePack
- **Original git URL:** https://github.com/pinokiofactory/Frame-Pack
- **Analyzed commit:** `f0d7d1eba4155f5985a465d0476a9f926d0c6179`
- **Platforms supported:** NVIDIA only
- **Porting difficulty:** Very high
- **CUDA-only packages:** sageattention, triton, triton-windows, xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

devicetorch, diffusers, diffusers-helper, einops, gradio, hf-xet, numpy, pil, safetensors, sageattention, torch, torch-directml, torchaudio, torchvision, transformers, triton, triton-windows, xformers

Third-party Python imports detected in local source: diffusers, diffusers-helper, einops, gradio, numpy, pil, safetensors, torch, transformers.

Wheel indexes referenced: cpu, cu128, rocm6.3.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 1231
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- Explicit platform tag found: NVIDIA only.
- `torch.js` routes present: nvidia, amd, mac, cpu.
- No requirements file; third-party Python imports used as a fallback signal.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): xformers
- Difficulty score: 10.0 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- retested on Python 3.10; import failed on CUDA-only module-level code (torch.cuda.current_device()).
- Result: **not runnable in this container.**
