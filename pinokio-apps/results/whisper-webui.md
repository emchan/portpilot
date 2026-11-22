# whisper-webui — portability analysis

- **Package name:** Whisper-WebUI (`whisper-webui`)
- **Description:** A Web UI for easy subtitle using whisper model.
- **Original git URL:** https://github.com/pinokiofactory/whisper-webui
- **Analyzed commit:** `5b6ebed2652d7adb7608ebe5c82ed01619e10daf`
- **Platforms supported:** NVIDIA / AMD / Mac
- **Porting difficulty:** Low
- **CUDA-only packages:** xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

faster-whisper, gradio, gradio-i18n, hf-xet, matplotlib, numpy, pyannote.audio, pytubefix, ruamel.yaml, torch, torch-directml, torchaudio, torchvision, transformers, xformers

Requirements files: `requirements.txt`.

Wheel indexes referenced: cpu, cu128, rocm6.3.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 315
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- `torch.js` routes present: nvidia, amd, mac, cpu.
- Requirements from: requirements.txt
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): xformers
- Difficulty score: 0.5 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- retested on Python 3.12; jhj0517-whisper build still fails due setuptools/pkg_resources.
- Result: **not runnable in this container.**
<!-- cross-analysis:start -->
## Cross-analysis details

- **CPU category (cpu.md):** CPU-capable with shipped fallback
- **TPU suitability:** Possible - moderate port
- **TPU work needed:** replace CUDA attention kernels with TPU-compatible attention/SDPA/XLA; moderate device/kernel/runtime adaptation
- **Effort ranking (effort.md):** #39 — Low
- **Effort blockers:** GPU-only attention: xformers
- **Precisions noted:** unspecified
- **Models/flows noted:** —
- **Flow graph:** [flows/whisper-webui.md](../flows/whisper-webui.md)

### Snapshot verification (cloned analyzed commit)

- **Snapshot source:** `https://codeload.github.com/pinokiofactory/whisper-webui/tar.gz/<analyzed commit>` extracted to `/tmp/opencode/pinokio-snapshots/whisper-webui`
- **Files scanned:** 13 total (0 .py, 7 .js, 6 other)
- **Key files present:** pinokio.js, install.js, torch.js, start.js, requirements.txt
- **TPU/CUDA-relevant signals:**
  - `xformers`: 4 match(es) (e.g. torch.js:10, torch.js:10)
  - `directml`: 1 match(es) (e.g. torch.js:22)

### Evidence from analysis files

| Source | Evidence |
|---|---|
| [kernels.md](../analysis/kernels.md) | No per-repo kernel table row matched; see kernels.md for global signals. |
| [quantization.md](../analysis/quantization.md) | No per-repo quantization table row matched; see quantization.md. |
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
- [App flow graph](../flows/whisper-webui.md)
<!-- cross-analysis:end -->

## Snapdragon evaluation (deep clone)
- **Clone/scan status:** cloned and scanned
- **Files scanned:** 13 total (0 .py, 7 .js/.ts, 6 other)
- **Snapdragon-relevant signals:** torch=9, xformers=2, directml=1
- **Example evidence:**
  - torch: `install.js:36`
  - xformers: `torch.js:10`
  - directml: `torch.js:22`
- **Snapdragon verdict:** No Python GEMM in wrapper; Snapdragon CPU-ready as launcher/wrapper (no model port).
