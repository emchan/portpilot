# RMBG-2-Studio — portability analysis

- **Package name:** RMBG-2-Studio (`RMBG-2-Studio`)
- **Description:** Enhanced background remove and replace app built around BRIA-RMBG-2.0 https://huggingface.co/briaai/RMBG-2.0
- **Original git URL:** https://github.com/pinokiofactory/RMBG-2-Studio
- **Analyzed commit:** `a2c3a0d0f1618c74c115d3221eb665bab5e8df10`
- **Platforms supported:** NVIDIA / AMD / Mac
- **Porting difficulty:** Low
- **CUDA-only packages:** xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

devicetorch, gradio, gradio-imageslider, kornia, loadimg, numpy, opencv-python, pillow, prettytable, pydantic, scikit-image, starlette, timm, torch, torch-directml, torchaudio, torchvision, transformers, typing, xformers

Requirements files: `app/requirements.txt`.

Third-party Python imports detected in local source: cv2, devicetorch, gradio, gradio-imageslider, loadimg, numpy, pil, requests, torch, torchvision, tqdm, transformers.

Wheel indexes referenced: cpu, cu124, cu128, rocm6.2.4.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 1084
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- `torch.js` routes present: nvidia, amd, mac, cpu.
- Requirements from: app/requirements.txt
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): xformers
- Difficulty score: 0.5 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- retested on Python 3.12; dependencies installed and app imported successfully on CPU.
- Result: **CPU port imports successfully.**
<!-- cross-analysis:start -->
## Cross-analysis details

- **CPU category (cpu.md):** CPU-capable with shipped fallback
- **TPU suitability:** Possible - moderate port
- **TPU work needed:** replace CUDA attention kernels with TPU-compatible attention/SDPA/XLA; moderate device/kernel/runtime adaptation
- **Effort ranking (effort.md):** #17 — Low
- **Effort blockers:** GPU-only attention: xformers
- **Precisions noted:** UINT8
- **Models/flows noted:** [briaai/RMBG-2.0](https://huggingface.co/briaai/RMBG-2.0)
- **Flow graph:** [flows/RMBG-2-Studio.md](../flows/RMBG-2-Studio.md)

### Snapshot verification (cloned analyzed commit)

- **Snapshot source:** `https://codeload.github.com/pinokiofactory/RMBG-2-Studio/tar.gz/<analyzed commit>` extracted to `/tmp/opencode/pinokio-snapshots/RMBG-2-Studio`
- **Files scanned:** 16 total (1 .py, 8 .js, 7 other)
- **Key files present:** pinokio.js, install.js, torch.js, start.js
- **TPU/CUDA-relevant signals:**
  - `xformers`: 4 match(es) (e.g. torch.js:23, torch.js:23)
  - `directml`: 1 match(es) (e.g. torch.js:33)

### Evidence from analysis files

| Source | Evidence |
|---|---|
| [kernels.md](../analysis/kernels.md) | No per-repo kernel table row matched; see kernels.md for global signals. |
| [quantization.md](../analysis/quantization.md) | `\| [RMBG-2-Studio](https://github.com/pinokiofactory/RMBG-2-Studio) \| [a2c3a0d](https://github.com/pinokiofactory/RMBG-2-Studio/commit/a2c3a0d0f1618c74c115d3221eb665bab5e8df10) \| [364](https://github.com/pinokiofactory/RMBG-2-Studio/blob/a2c3a0d0f1618c74c115d3221eb665bab5e8df10/app/app.py#L364) \| uint8 \| explicit cast \| return Image.fromarray(img_array.astype('uint8')) \|` |
| [fusion.md](../analysis/fusion.md) | No direct fusion table row matched; see fusion.md for global context. |
| [models.md](../analysis/models.md) | No model pull/shape row matched in models.md. |
| [cpu.md](../analysis/cpu.md) | CPU category: **CPU-capable with shipped fallback** |
| [tpu.md](../analysis/tpu.md) | TPU suitability: **Possible - moderate port** — replace CUDA attention kernels with TPU-compatible attention/SDPA/XLA; moderate device/kernel/runtime adaptation |

### Related analysis

- [CPU analysis](../analysis/cpu.md)
- [TPU analysis](../analysis/tpu.md)
- [Effort ranking](../analysis/effort.md)
- [Kernel evidence](../analysis/kernels.md)
- [Quantization evidence](../analysis/quantization.md)
- [Fusion evidence](../analysis/fusion.md)
- [Model pulls/shapes](../analysis/models.md)
- [Flow graphs](../analysis/flows.md)
- [App flow graph](../flows/RMBG-2-Studio.md)
<!-- cross-analysis:end -->
