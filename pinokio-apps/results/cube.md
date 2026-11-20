# cube — portability analysis

- **Package name:** cube (`cube`)
- **Description:** Roblox Foundation Model for 3D Intelligence --- Cross Platform (Mac, Windows, Linux): Requires 16GB+ VRAM PC or 18GB+ Memory Macs https://github.com/Roblox/cube
- **Original git URL:** https://github.com/pinokiofactory/cube
- **Analyzed commit:** `58844658cfc9eab4f8e956bab4883fa8d867cf44`
- **Platforms supported:** Cross-platform
- **Porting difficulty:** Low
- **CUDA-only packages:** xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

gradio, huggingface-hub, numpy, torch, torch-directml, torchaudio, torchvision, xformers

Wheel indexes referenced: cpu, cu128, rocm6.3.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 292
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- Explicit platform tag found: Cross-platform.
- `torch.js` routes present: nvidia, amd, mac, cpu.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): xformers
- Difficulty score: 0.5 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).
