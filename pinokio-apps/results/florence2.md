# florence2 — portability analysis

- **Package name:** Florence2 (`florence2`)
- **Description:** An advanced vision foundation model from MicroSoft https://huggingface.co/spaces/gokaygokay/Florence-2
- **Original git URL:** https://github.com/pinokiofactory/florence2
- **Analyzed commit:** `5b517ac86c59d3b8a28a5d75c3aba34e2aa2e3b6`
- **Platforms supported:** NVIDIA / AMD / Mac
- **Porting difficulty:** Low
- **CUDA-only packages:** xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

devicetorch, gradio, pydantic, torch, torch-directml, torchaudio, torchvision, transformers, xformers

Wheel indexes referenced: cpu, cu128, rocm6.3.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 303
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- `torch.js` routes present: nvidia, amd, mac, cpu.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): xformers
- Difficulty score: 0.5 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- Retested on Python 3.12; dependencies installed, but full model loading not attempted due to multi-GB downloads.
- Result: **not runnable in this container.**
<!-- cross-analysis:start -->
## Cross-analysis details

- **CPU category (cpu.md):** CPU-capable with shipped fallback
- **TPU suitability:** Possible - moderate port
- **TPU work needed:** replace CUDA attention kernels with TPU-compatible attention/SDPA/XLA; moderate device/kernel/runtime adaptation
- **Effort ranking (effort.md):** #29 — Low
- **Effort blockers:** GPU-only attention: xformers
- **Precisions noted:** unspecified
- **Models/flows noted:** —
- **Flow graph:** [flows/florence2.md](../flows/florence2.md)

### Snapshot verification (cloned analyzed commit)

- **Snapshot source:** `https://codeload.github.com/pinokiofactory/florence2/tar.gz/<analyzed commit>` extracted to `/tmp/opencode/pinokio-snapshots/florence2`
- **Files scanned:** 10 total (0 .py, 7 .js, 3 other)
- **Key files present:** pinokio.js, install.js, torch.js, start.js
- **TPU/CUDA-relevant signals:**
  - `xformers`: 5 match(es) (e.g. torch.js:11, torch.js:11)
  - `directml`: 1 match(es) (e.g. torch.js:23)

### Evidence from analysis files

| Source | Evidence |
|---|---|
| [kernels.md](../analysis/kernels.md) | `\| [florence2](https://github.com/pinokiofactory/florence2) \| [5b517ac](https://github.com/pinokiofactory/florence2/commit/5b517ac86c59d3b8a28a5d75c3aba34e2aa2e3b6) \| env/config flag \| [install.js:28](https://github.com/pinokiofactory/florence2/blob/5b517ac86c59d3b8a28a5d75c3aba34e2aa2e3b6/install.js#L28) — "FLASH_ATTENTION_SKIP_CUDA_BUILD": "TRUE" \|` |
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
- [App flow graph](../flows/florence2.md)
<!-- cross-analysis:end -->

## Snapdragon evaluation (deep clone)
- **Clone/scan status:** cloned and scanned
- **Files scanned:** 10 total (0 .py, 7 .js/.ts, 3 other)
- **Snapdragon-relevant signals:** cuda=1, torch=10, xformers=3, directml=1
- **Example evidence:**
  - cuda: `install.js:28`
  - torch: `install.js:14`
  - xformers: `install.js:18`
  - directml: `torch.js:23`
- **Snapdragon verdict:** Contains CUDA/Triton/TensorRT signals; Snapdragon path requires replacement or ONNX conversion.
