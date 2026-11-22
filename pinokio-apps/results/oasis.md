# oasis — portability analysis

- **Package name:** oasis (`oasis`)
- **Description:** # oasis
- **Original git URL:** https://github.com/pinokiofactory/oasis
- **Analyzed commit:** `a84069d12ae3165aa0c8c955f9a93314ecf3d3d8`
- **Platforms supported:** NVIDIA / AMD / Mac
- **Porting difficulty:** Low
- **CUDA-only packages:** xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

devicetorch, gradio, huggingface-hub, numpy, torch, torch-directml, torchaudio, torchvision, xformers

Wheel indexes referenced: cpu, cu121, rocm6.0.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 276
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- `torch.js` routes present: nvidia, amd, mac, cpu.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): xformers
- Difficulty score: 0.5 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- retested on Python 3.12; dependency installation hung/timed out in this container.
- Result: **not runnable in this container.**
<!-- cross-analysis:start -->
## Cross-analysis details

- **CPU category (cpu.md):** CPU-capable with shipped fallback
- **TPU suitability:** Possible - moderate port
- **TPU work needed:** replace CUDA attention kernels with TPU-compatible attention/SDPA/XLA; moderate device/kernel/runtime adaptation
- **Effort ranking (effort.md):** #33 — Low
- **Effort blockers:** GPU-only attention: xformers
- **Precisions noted:** FP32
- **Models/flows noted:** [cocktailpeanut/sisao](https://huggingface.co/cocktailpeanut/sisao)
- **Flow graph:** [flows/oasis.md](../flows/oasis.md)

### Snapshot verification (cloned analyzed commit)

- **Snapshot source:** `https://codeload.github.com/pinokiofactory/oasis/tar.gz/<analyzed commit>` extracted to `/tmp/opencode/pinokio-snapshots/oasis`
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
| [fusion.md](../analysis/fusion.md) | `\| [oasis](https://github.com/pinokiofactory/oasis) \| [a84069d](https://github.com/pinokiofactory/oasis/commit/a84069d12ae3165aa0c8c955f9a93314ecf3d3d8) \| 100 \| [`oasis.md`](../flows/oasis.md) \|` |
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
- [App flow graph](../flows/oasis.md)
<!-- cross-analysis:end -->

## Snapdragon evaluation (deep clone)
- **Clone/scan status:** cloned and scanned
- **Files scanned:** 9 total (0 .py, 6 .js/.ts, 3 other)
- **Snapdragon-relevant signals:** torch=10, xformers=3, directml=1
- **Example evidence:**
  - torch: `install.js:12`
  - xformers: `install.js:20`
  - directml: `torch.js:20`
- **Snapdragon verdict:** No Python GEMM in wrapper; Snapdragon CPU-ready as launcher/wrapper (no model port).
