# omniparser — portability analysis

- **Package name:** omniparser (`omniparser`)
- **Description:** # omniparser
- **Original git URL:** https://github.com/pinokiofactory/omniparser
- **Analyzed commit:** `b2f7de9607dcc3087229feaee36c6c2f0345fc80`
- **Platforms supported:** NVIDIA / AMD / Mac
- **Porting difficulty:** Low
- **CUDA-only packages:** xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

devicetorch, einops, gradio, huggingface-hub, numpy, torch, torch-directml, torchaudio, torchvision, xformers

Wheel indexes referenced: cpu, cu121, rocm6.0.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 274
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- `torch.js` routes present: nvidia, amd, mac, cpu.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): xformers
- Difficulty score: 0.5 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- retested on Python 3.12; dependency installation completed but gradio_demo failed on paddleocr use_gpu argument.
- Result: **not runnable in this container.**
<!-- cross-analysis:start -->
## Cross-analysis details

- **CPU category (cpu.md):** CPU-capable with shipped fallback
- **TPU suitability:** Possible - moderate port
- **TPU work needed:** replace CUDA attention kernels with TPU-compatible attention/SDPA/XLA; large BF16/FP16 GEMM workload; expect XLA compile/memory tuning; moderate device/kernel/runtime adaptation
- **Effort ranking (effort.md):** #34 — Low
- **Effort blockers:** GPU-only attention: xformers; large FP16/BF16 GEMM load
- **Precisions noted:** FP32, FP16
- **Models/flows noted:** [microsoft/OmniParser](https://huggingface.co/microsoft/OmniParser)
- **Flow graph:** [flows/omniparser.md](../flows/omniparser.md)

### Snapshot verification (cloned analyzed commit)

- **Snapshot source:** `https://codeload.github.com/pinokiofactory/omniparser/tar.gz/<analyzed commit>` extracted to `/tmp/opencode/pinokio-snapshots/omniparser`
- **Files scanned:** 9 total (0 .py, 6 .js, 3 other)
- **Key files present:** pinokio.js, install.js, torch.js, start.js
- **TPU/CUDA-relevant signals:**
  - `xformers`: 6 match(es) (e.g. torch.js:10, torch.js:10)
  - `directml`: 1 match(es) (e.g. torch.js:20)

### Evidence from analysis files

| Source | Evidence |
|---|---|
| [kernels.md](../analysis/kernels.md) | No per-repo kernel table row matched; see kernels.md for global signals. |
| [quantization.md](../analysis/quantization.md) | No per-repo quantization table row matched; see quantization.md. |
| [fusion.md](../analysis/fusion.md) | `\| [omniparser](https://github.com/pinokiofactory/omniparser) \| [b2f7de9](https://github.com/pinokiofactory/omniparser/commit/b2f7de9607dcc3087229feaee36c6c2f0345fc80) \| 58 \| 228 \|` |
| [fusion.md](../analysis/fusion.md) | `\| [omniparser](https://github.com/pinokiofactory/omniparser) \| [b2f7de9](https://github.com/pinokiofactory/omniparser/commit/b2f7de9607dcc3087229feaee36c6c2f0345fc80) \| 18 \| 1 \| 0 \| 0 \| 192 \| 58 \| 497 \|` |
| [models.md](../analysis/models.md) | No model pull/shape row matched in models.md. |
| [cpu.md](../analysis/cpu.md) | CPU category: **CPU-capable with shipped fallback** |
| [tpu.md](../analysis/tpu.md) | TPU suitability: **Possible - moderate port** — replace CUDA attention kernels with TPU-compatible attention/SDPA/XLA; large BF16/FP16 GEMM workload; expect XLA compile/memory tuning; moderate device/kernel/runtime adaptation |

### Related analysis

- [CPU analysis](../analysis/cpu.md)
- [TPU analysis](../analysis/tpu.md)
- [Effort ranking](../analysis/effort.md)
- [Kernel evidence](../analysis/kernels.md)
- [Quantization evidence](../analysis/quantization.md)
- [Fusion evidence](../analysis/fusion.md)
- [Model pulls/shapes](../analysis/models.md)
- [Flow graphs](../analysis/flows.md)
- [App flow graph](../flows/omniparser.md)
<!-- cross-analysis:end -->
