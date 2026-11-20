# cogvideo — portability analysis

- **Package name:** cogvideo (`cogvideo`)
- **Description:** [NVIDIA ONLY] Generate videos with less than 10GB VRAM https://github.com/THUDM/CogVideo
- **Original git URL:** https://github.com/pinokiofactory/cogvideo
- **Analyzed commit:** `9e2a18626426cbeb7e84be537d98e9082de8fe97`
- **Platforms supported:** NVIDIA only
- **Porting difficulty:** Very high
- **CUDA-only packages:** flash-attn, sageattention *(optional)*, triton *(optional)*, triton-windows, xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

accelerate, diffusers, flash-attn, gradio, hf-xet, imageio, imageio-ffmpeg, moviepy, numpy, openai, pillow, protobuf, sageattention, sentencepiece, tiktoken, torch, torch-directml, torchaudio, torchvision, transformers, triton, triton-windows, xformers

Requirements files: `requirements.txt`.

Wheel indexes referenced: cpu, cu128, rocm6.3.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 310
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- Explicit platform tag found: NVIDIA only.
- `torch.js` routes present: nvidia, amd, mac, cpu.
- Requirements from: requirements.txt
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): sageattention, triton, xformers
- Difficulty score: 10.8 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).
