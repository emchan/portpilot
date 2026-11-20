# cogstudio — portability analysis

- **Package name:** CogStudio (`cogstudio`)
- **Description:** [NVIDIA ONLY] Advanced Web UI for CogVideo (text to video, image to video, video to video, extend video, etc) -- Generate videos with less than 10GB VRAM
- **Original git URL:** https://github.com/pinokiofactory/cogstudio
- **Analyzed commit:** `7dfb014a636513c5b42de070c43e285c9bf7cce7`
- **Platforms supported:** NVIDIA only
- **Porting difficulty:** Medium
- **CUDA-only packages:** xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

diffusers, gradio, hf-xet, moviepy, numpy, protobuf, tiktoken, torch, torchaudio, torchvision, tqdm, transformers, xformers

Requirements files: `requirements.txt`.

Third-party Python imports detected in local source: cv2, diffusers, gradio, huggingface-hub, imageio-ffmpeg, moviepy, openai, pil, rife-model, torch, utils.

Wheel indexes referenced: cu128, rocm6.3.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 1147
- **CUDA-related functions used:** `torch.cuda.empty_cache`, `torch.cuda.is_available`

## Evidence and notes

- Explicit platform tag found: NVIDIA only.
- `torch.js` routes present: nvidia, amd.
- Requirements from: requirements.txt
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): xformers
- Difficulty score: 4.5 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).
