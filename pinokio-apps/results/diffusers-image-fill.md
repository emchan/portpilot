# diffusers-image-fill — portability analysis

- **Package name:** diffusers-image-fill (`diffusers-image-fill`)
- **Description:** Remove objects from an image https://huggingface.co/spaces/OzzyGT/diffusers-image-fill
- **Original git URL:** https://github.com/pinokiofactory/diffusers-image-fill
- **Analyzed commit:** `a8b6497483d956df7ca1ffc882bf29af03476a26`
- **Platforms supported:** NVIDIA / AMD / Mac
- **Porting difficulty:** Low
- **CUDA-only packages:** xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

accelerate, devicetorch, diffusers, fastapi, gradio, gradio-imageslider, huggingface-hub, numpy, opencv-python, pillow, pydantic, spaces, torch, torch-directml, torchaudio, torchvision, transformers, xformers

Requirements files: `requirements.txt`.

Third-party Python imports detected in local source: cv2, devicetorch, diffusers, gradio, gradio-imageslider, huggingface-hub, pil, torch, transformers.

Wheel indexes referenced: cpu, cu128, rocm6.3.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 2073
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- `torch.js` routes present: nvidia, amd, mac, cpu.
- Requirements from: requirements.txt
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): xformers
- Difficulty score: 0.5 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- Retested on Python 3.12 with corrected dependencies; importing app.py still hung in this container.
- Result: **not runnable in this container.**
