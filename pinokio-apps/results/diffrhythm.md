# diffrhythm — portability analysis

- **Package name:** DiffRhythm (`diffrhythm`)
- **Description:** Generate songs with AI (up to 4 min 45 sec). Both with lyrics or instrumental https://github.com/ASLP-lab/DiffRhythm
- **Original git URL:** https://github.com/pinokiofactory/diffrhythm
- **Analyzed commit:** `15166cfd3b677d7fd6294b4d9fb88e7f4845d3ee`
- **Platforms supported:** NVIDIA / AMD / Mac
- **Porting difficulty:** High
- **CUDA-only packages:** bitsandbytes, onnxruntime-gpu, triton *(optional)*, triton-windows, xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

accelerate, bitsandbytes, cn2an, ema-pytorch, espeak-ng, jieba, langsegment, libaio-dev, librosa, muq, mutagen, numpy, onnxruntime, onnxruntime-gpu, openai, pandas, phonemizer, prefigure, pyarrow, pykakasi, pylance, pyopenjtalk, pypinyin, spaces, torch, torch-directml, torchaudio, torchdiffeq, torchvision, transformers, triton, triton-windows, unidecode, x-transformers, xformers

Requirements files: `requirements.txt`.

Wheel indexes referenced: cpu, cu128, rocm6.3.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 409
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- `torch.js` routes present: nvidia, amd, mac, cpu.
- Requirements from: requirements.txt
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): triton, xformers
- Difficulty score: 7.8 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).
