# hunyuanvideo — portability analysis

- **Package name:** HunyuanVideo (`hunyuanvideo`)
- **Description:** [NVIDIA ONLY] Super Optimized Gradio UI for Hunyuan Video Generator that works on GPU poor machines. Generate up to 10~14 sec videos https://github.com/deepbeepmeep/HunyuanVideoGP
- **Original git URL:** https://github.com/pinokiofactory/hunyuanvideo
- **Analyzed commit:** `c65cb772466eea61e0a330f52ed7764a9d4e821d`
- **Platforms supported:** NVIDIA only
- **Porting difficulty:** Very high
- **CUDA-only packages:** flash-attn, sageattention *(optional)*, triton *(optional)*, triton-windows, xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

accelerate, av, diffusers, einops, fire, flash-attn, gradio, hf-xet, imageio, imageio-ffmpeg, lightning, loguru, mmgp, moviepy, numpy, omegaconf, opencv-python, pandas, peft, pydantic, safetensors, sageattention, tokenizers, torch, torchaudio, torchvision, tqdm, transformers, triton, triton-windows, xformers

Requirements files: `requirements.txt`.

Wheel indexes referenced: cu128.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 462
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- Explicit platform tag found: NVIDIA only.
- `torch.js` routes present: nvidia.
- Requirements from: requirements.txt
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): sageattention, triton, xformers
- Difficulty score: 12.8 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- retested packaging path; still blocked by explicit NVIDIA-only guard and pandas build failure.
- Result: **not runnable in this container.**
