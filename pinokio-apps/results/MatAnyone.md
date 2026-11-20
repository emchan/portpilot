# MatAnyone — portability analysis

- **Package name:** MatAnyone (`MatAnyone`)
- **Description:** MatAnyone AI is a tool for editing videos by separating objects from their backgrounds. It is an AI to remove the background from videos effectively. Stable Video Matting with Consistent Memory Propagation: https://github.com/pq-yang/MatAnyone.git
- **Original git URL:** https://github.com/pinokiofactory/MatAnyone
- **Analyzed commit:** `84831993029bc83f5942f0401bc8a32dd315b217`
- **Platforms supported:** NVIDIA only
- **Porting difficulty:** Medium
- **CUDA-only packages:** xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

av, cchardet, charset-normalizer, cython, easydict, einops, fastapi, ffmpeg-python, gdown, gitpython, gradio, hickle, hydra-core, imageio, matplotlib, netifaces, numpy, opencv-python, openmim, pillow, progressbar2, psutil, pycocotools, pyqtdarktheme, pyside6, pyyaml, requests, scipy, tensorboard, torch, torch-directml, torchaudio, torchvision, tqdm, xformers

Requirements files: `requirements.txt`.

Third-party Python imports detected in local source: cv2, ffmpeg, gradio, imageio, matanyone, matanyone-wrapper, numpy, pil, psutil, tools, torch.

Wheel indexes referenced: cpu, cu124, cu128, rocm6.2.4.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 1528
- **CUDA-related functions used:** `torch.cuda.is_available`

## Evidence and notes

- Explicit platform tag found: NVIDIA only.
- `torch.js` routes present: nvidia, amd, mac, cpu.
- Requirements from: requirements.txt
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): xformers
- Difficulty score: 3.5 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).
