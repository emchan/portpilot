# hallo — portability analysis

- **Package name:** hallo (`hallo`)
- **Description:** [NVIDIA Only] Hierarchical Audio-Driven Visual Synthesis for Portrait Image Animation https://github.com/fudan-generative-vision/hallo
- **Original git URL:** https://github.com/pinokiofactory/hallo
- **Analyzed commit:** `c72097c6c23be58e7435bc48fbe9d0be5d0da1e5`
- **Platforms supported:** NVIDIA only
- **Porting difficulty:** Medium–high
- **CUDA-only packages:** bitsandbytes, xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

accelerate, audio-separator, av, bitsandbytes, decord, devicetorch, diffusers, einops, eva-decord, gradio, hf-xet, huggingface-hub, insightface, install, isort, librosa, mediapipe, mlflow, moviepy, numpy, omegaconf, onnx, onnx2torch, onnxruntime, opencv-contrib-python, opencv-python, opencv-python-headless, pillow, pre-commit, pylint, setuptools, torch, torch-directml, torchaudio, torchvision, tqdm, transformers, xformers

Requirements files: `requirements.txt`.

Wheel indexes referenced: cpu, cu128, rocm6.3.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 296
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- Explicit platform tag found: NVIDIA only.
- `torch.js` routes present: nvidia, amd, mac, cpu.
- Requirements from: requirements.txt
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): xformers
- Difficulty score: 6.0 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).
