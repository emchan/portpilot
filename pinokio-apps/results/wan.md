# wan — portability analysis

- **Package name:** Wan2GP (`wan`)
- **Description:** 1-click WanGP Launcher. Super Optimized Gradio UI for AI video creation for GPU poor machines (6GB+ VRAM). Supports Wan 2.1/2.2, Qwen, Hunyuan Video, LTX Video and Flux. https://github.com/deepbeepmeep/Wan2GP
- **Original git URL:** https://github.com/pinokiofactory/wan
- **Analyzed commit:** `8ed14108ca7148a612c5eb9528b00ceac99810ff`
- **Platforms supported:** NVIDIA / AMD / Mac
- **Porting difficulty:** Very high
- **CUDA-only packages:** bitsandbytes, flash-attn, sageattention, triton-windows, xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

bitsandbytes, comtypes, flash-attn, hf-xet, lightx2v-kernel, llamacpp-gguf-cuda, numpy, nunchaku, sageattention, spas-sage-attn, torch, torchaudio, torchvision, triton-windows, unsafe-best-match, wgpkernels, xformers

Wheel indexes referenced: cpu, cu128, cu130, rocm7.1.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 650
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- `torch.js` routes present: nvidia, amd, mac, cpu.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): xformers
- Difficulty score: 11.0 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).
