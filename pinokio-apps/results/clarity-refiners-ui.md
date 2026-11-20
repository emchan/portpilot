# clarity-refiners-ui — portability analysis

- **Package name:** Clarity Refiners UI (`clarity-refiners-ui`)
- **Description:** An enhanced local port of finegrain-image-enhancer powered by Refiners (https://huggingface.co/spaces/finegrain/finegrain-image-enhancer), which was adapted from philz1337x's Clarity Upscaler (https://github.com/philz1337x/clarity-upscaler)
- **Original git URL:** https://github.com/pinokiofactory/clarity-refiners-ui
- **Analyzed commit:** `a632fb6b948fa6b1a55d816982655d6dc8ed995e`
- **Platforms supported:** NVIDIA / AMD / Mac
- **Porting difficulty:** Low
- **CUDA-only packages:** xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

accelerate, devicetorch, einops, ftfy, gradio, gradio-imageslider, numpy, pillow, pillow-heif, pydantic, regex, timm, torch, torch-directml, torchaudio, torchvision, tqdm, transformers, xformers

Requirements files: `app/requirements.txt`.

Third-party Python imports detected in local source: devicetorch, gradio, gradio-imageslider, huggingface-hub, numpy, pil, pillow-heif, psutil, refiners, torch, transformers.

Wheel indexes referenced: cpu, cu128, rocm6.3.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 1871
- **CUDA-related functions used:** `torch.cuda.get_device_name`, `torch.cuda.get_device_properties`, `torch.cuda.is_available`, `torch.cuda.memory_allocated`

## Evidence and notes

- `torch.js` routes present: nvidia, amd, mac, cpu.
- Requirements from: app/requirements.txt
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): xformers
- Difficulty score: 0.5 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).
