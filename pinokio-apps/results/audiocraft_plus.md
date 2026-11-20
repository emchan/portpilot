# audiocraft_plus — portability analysis

- **Package name:** audiocraft_plus (`audiocraft_plus`)
- **Description:** AudioCraft Plus is an all-in-one WebUI for the original AudioCraft, adding many quality features on top https://github.com/GrandaddyShmax/audiocraft_plus
- **Original git URL:** https://github.com/pinokiofactory/audiocraft_plus
- **Analyzed commit:** `a8e0d2731e8dbb7185a4a0ffd53b495d003586ab`
- **Platforms supported:** NVIDIA / AMD / Mac
- **Porting difficulty:** Low–medium
- **CUDA-only packages:** triton-windows, xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

av, demucs, einops, encodec, fastapi, flashy, gradio, gradio-client, huggingface-hub, hydra-colorlog, hydra-core, julius, librosa, num2words, numpy, pytaglib, sentencepiece, spacy, torch, torch-directml, torchaudio, torchmetrics, torchvision, tqdm, transformers, triton-windows, wheel, xformers

Requirements files: `requirements.txt`.

Wheel indexes referenced: cpu, cu128, rocm6.3.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 297
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- `torch.js` routes present: nvidia, amd, mac, cpu.
- Requirements from: requirements.txt
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): xformers
- Difficulty score: 2.5 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).
