# facepoke — portability analysis

- **Package name:** facepoke (`facepoke`)
- **Description:** [NVIDIA Only] Select a portrait, click to move the head around https://github.com/jbilcke-hf/FacePoke
- **Original git URL:** https://github.com/pinokiofactory/facepoke
- **Analyzed commit:** `f3a8c9610834b51b64069f3bce9b1da3a321e620`
- **Platforms supported:** NVIDIA only
- **Porting difficulty:** Medium–high
- **CUDA-only packages:** onnxruntime-gpu, xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

numpy, onnxruntime, onnxruntime-directml, onnxruntime-gpu, onnxruntime-rocm, torch, torch-directml, torchaudio, torchvision, wheel, xformers

Wheel indexes referenced: cpu, cu128, rocm6.3.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 312
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- Explicit platform tag found: NVIDIA only.
- `torch.js` routes present: nvidia, amd, mac, cpu.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): xformers
- Difficulty score: 5.5 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).
