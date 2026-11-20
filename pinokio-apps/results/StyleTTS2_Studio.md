# StyleTTS2_Studio — portability analysis

- **Package name:** StyleTTS2 Studio (`StyleTTS2_Studio`)
- **Description:** Build your own voice for StyleTTS2
- **Original git URL:** https://github.com/pinokiofactory/StyleTTS2_Studio
- **Analyzed commit:** `cb09179fa56bf5d34c86dffc9b5424c5331005a7`
- **Platforms supported:** NVIDIA / AMD / Mac
- **Porting difficulty:** Low
- **CUDA-only packages:** xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

audiofile, cached-path, einops, einops-exts, gradio, hf-xet, huggingface-hub, librosa, markdown, matplotlib, munch, nltk, numpy, openphonemizer, phonemizer, pydantic, scikit-learn, soundfile, torch, torch-directml, torchaudio, torchvision, tqdm, transformers, txtsplit, xformers

Requirements files: `requirements.txt`.

Wheel indexes referenced: cpu, cu128, rocm6.3.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 293
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- `torch.js` routes present: nvidia, amd, mac, cpu.
- Requirements from: requirements.txt
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): xformers
- Difficulty score: 0.5 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).
