# echomimic2 — portability analysis

- **Package name:** echomimic2 (`echomimic2`)
- **Description:** [NVIDIA ONLY] Make virtual avatars talk whatever you want with an image and an audio clip https://github.com/antgroup/echomimic_v2
- **Original git URL:** https://github.com/pinokiofactory/echomimic2
- **Analyzed commit:** `eb7915a14420505c7c8b929a2dbba570f1639831`
- **Platforms supported:** NVIDIA only
- **Porting difficulty:** High
- **CUDA-only packages:** onnxruntime-gpu, triton-windows, xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

accelerate, av, clip, controlnet-aux, decord, diffusers, einops, facenet-pytorch, ffmpeg-python, gradio, gradio-client, hf-xet, huggingface-hub, imageio, imageio-ffmpeg, ipython, mediapipe, mlflow, moviepy, numpy, omegaconf, onnxruntime-gpu, open-clip-torch, opencv-contrib-python, opencv-python, pillow, pydantic, scenedetect, scikit-image, scikit-learn, scipy, soundfile, torch, torchao, torchaudio, torchdiffeq, torchmetrics, torchsde, torchtyping, torchvision, tqdm, transformers, triton-windows, wheel, xformers

Requirements files: `requirements.txt`.

Wheel indexes referenced: cu128.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 275
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- Explicit platform tag found: NVIDIA only.
- `torch.js` routes present: nvidia.
- Requirements from: requirements.txt
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): triton, xformers
- Difficulty score: 9.5 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).
