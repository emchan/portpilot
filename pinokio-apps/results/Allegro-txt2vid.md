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

## CPU test run (2026-11-21)

- blocked by torchvision operator mismatch.
- Result: **not runnable in this container.**

## CPU port attempt

- **Attempt order:** #89 of 101 (by porting effort, easiest first).
- **Status:** Blocked.
- **Changes applied / required:** rely on devicetorch (already present); replace direct torch.cuda calls with devicetorch or cpu fallback; disable fused GPU kernels (xformers/flash/sage) in config; substitute GPU-only attention libs with SDPA math backend.
- **Smoke check:** pass (15/15 files).
- **Blockers:** hard CUDA/TensorRT blocker; GPU-only attention: xformers; direct torch.cuda calls; CUDA-only fused kernels.
- **Scope note:** static portability review of the Pinokio wrapper; no install or model download was executed.
