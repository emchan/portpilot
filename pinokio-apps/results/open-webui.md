# open-webui — portability analysis

- **Package name:** Open WebUI (`open-webui`)
- **Description:** User-friendly WebUI for LLMs, supported LLM runners include Ollama and OpenAI-compatible APIs https://github.com/open-webui/open-webui
- **Original git URL:** https://github.com/pinokiofactory/open-webui
- **Analyzed commit:** `d7c59329e3758cac350a1b5f1b834038727bec6c`
- **Platforms supported:** Cross-platform
- **Porting difficulty:** Low
- **CUDA-only packages:** —

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

itsdangerous, onnxruntime, open-webui

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 269
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- `torch.js` routes present: none.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Difficulty score: 0.0 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).
