# stable-fast-3d — portability analysis

- **Package name:** stable-fast-3d (`stable-fast-3d`)
- **Description:** [NVIDIA ONLY] a state-of-the-art open-source model for fast feedforward 3D mesh reconstruction from a single image, from Stability AI. https://huggingface.co/spaces/stabilityai/stable-fast-3d
- **Original git URL:** https://github.com/pinokiofactory/stable-fast-3d
- **Analyzed commit:** `00fdb293b784f223c100971f37a23f2e8a801654`
- **Platforms supported:** NVIDIA only
- **Porting difficulty:** Medium
- **CUDA-only packages:** xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

devicetorch, gradio, nvidia, rembg, torch, torch-directml, torchaudio, torchvision, xformers

Wheel indexes referenced: cpu, cu121, rocm6.0.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 262
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- Explicit platform tag found: NVIDIA only.
- `torch.js` routes present: nvidia, amd, mac, cpu.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): xformers
- Difficulty score: 3.5 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- retested on Python 3.12; blocked by scipy 1.18/numpy 1.26.4 mismatch (np.long removed).
- Result: **not runnable in this container.**
