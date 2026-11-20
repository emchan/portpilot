# Allegro-txt2vid — portability analysis

- **Package name:** Allegro-txt2vid (`Allegro-txt2vid`)
- **Description:** Allegro is a powerful text-to-video model that generates high-quality videos up to 6 seconds at 15 FPS and 720p resolution from simple text input.
- **Original git URL:** https://github.com/pinokiofactory/Allegro-txt2vid
- **Analyzed commit:** `f8327e3172834ee8d932d7284641a5e9a0065cbc`
- **Platforms supported:** NVIDIA only
- **Porting difficulty:** Medium
- **CUDA-only packages:** xformers

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

accelerate, bs4, decord, einops, ftfy, imageio, imageio-ffmpeg, numpy, psutil, pytorch-msssim, sentencepiece, tqdm, transformers

Requirements files: `requirements.txt`.

Third-party Python imports detected in local source: allegro, bs4, decord, devicetorch, diffusers, einops, ftfy, gradio, huggingface-hub, imageio, numpy, psutil, rife, torch, torchvision, tqdm, transformers, xformers.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 6266
- **CUDA-related functions used:** `torch.cuda.get_device_name`, `torch.cuda.is_available`

## Evidence and notes

- `torch.js` routes present: none.
- Requirements from: requirements.txt
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Difficulty score: 4.0 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).
