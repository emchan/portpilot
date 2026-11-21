# photomaker2 — portability analysis

- **Package name:** PhotoMaker2 (`photomaker2`)
- **Description:** Customizing Realistic Human Photos via Stacked ID Embedding https://huggingface.co/spaces/TencentARC/PhotoMaker-V2
- **Original git URL:** https://github.com/pinokiofactory/photomaker2
- **Analyzed commit:** `2c48cd3f30a305069aad6de30bfe4c3f0fe900f7`
- **Platforms supported:** NVIDIA / AMD / Mac
- **Porting difficulty:** Medium–high
- **CUDA-only packages:** cudnn, onnxruntime-gpu, xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

cudnn, devicetorch, gradio, huggingface-hub, numpy, onnxruntime, onnxruntime-directml, onnxruntime-gpu, onnxruntime-rocm, peft, torch, torch-directml, torchaudio, torchvision, transformers, xformers

Wheel indexes referenced: cpu, cu128, rocm6.3.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 316
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- `torch.js` routes present: nvidia, amd, mac, cpu.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): xformers
- Difficulty score: 5.0 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- retested on Python 3.10; blocked by torchvision 0.19.1 installation hang.
- Result: **not runnable in this container.**
