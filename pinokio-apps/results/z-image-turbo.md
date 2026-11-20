# z-image-turbo — portability analysis

- **Package name:** Z-Image-Turbo (`z-image-turbo`)
- **Description:** Simple Gradio app for generating images with Tongyi-MAI/Z-Image-Turbo.
- **Original git URL:** https://github.com/pinokiofactory/z-image-turbo
- **Analyzed commit:** `54899fdb5c023072de43c8b91ad2b0f0bee5b5c4`
- **Platforms supported:** NVIDIA / AMD / Mac
- **Porting difficulty:** High
- **CUDA-only packages:** flash-attn, sageattention *(optional)*, triton *(optional)*, triton-windows, xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

accelerate, diffusers, fastapi, flash-attn, gradio, huggingface-hub, numpy, pillow, pydantic, safetensors, sageattention, torch, torch-directml, torchaudio, torchvision, transformers, triton, triton-windows, xformers

Requirements files: `app/requirements.txt`.

Third-party Python imports detected in local source: diffusers, gradio, torch.

Wheel indexes referenced: cpu, cu128, rocm6.3.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 361
- **CUDA-related functions used:** `torch.cuda.is_available`

## Evidence and notes

- `torch.js` routes present: nvidia, amd, mac, cpu.
- Requirements from: app/requirements.txt
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): sageattention, triton, xformers
- Difficulty score: 7.8 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).
