# facepoke — portability analysis

- **Package name:** facepoke (`facepoke`)
- **Description:** [NVIDIA Only] Select a portrait, click to move the head around https://github.com/jbilcke-hf/FacePoke
- **Original git URL:** https://github.com/pinokiofactory/facepoke
- **Analyzed commit:** `f3a8c9610834b51b64069f3bce9b1da3a321e620`
- **Platforms supported:** NVIDIA only
- **Porting difficulty:** Medium–high
- **CUDA-only packages:** onnxruntime-gpu, xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

numpy, onnxruntime, onnxruntime-directml, onnxruntime-gpu, onnxruntime-rocm, torch, torch-directml, torchaudio, torchvision, wheel, xformers

Wheel indexes referenced: cpu, cu128, rocm6.3.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 312
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- Explicit platform tag found: NVIDIA only.
- `torch.js` routes present: nvidia, amd, mac, cpu.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): xformers
- Difficulty score: 5.5 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- retested on Python 3.10; blocked by chumpy build failure (no pip in build env).
- Result: **not runnable in this container.**
<!-- cross-analysis:start -->
## Cross-analysis details

- **CPU category (cpu.md):** CPU-capable with shipped fallback
- **TPU suitability:** Difficult - significant port
- **TPU work needed:** replace CUDA attention kernels with TPU-compatible attention/SDPA/XLA; replace onnxruntime-gpu with TPU-compatible runtime; multiple CUDA-specific dependencies or large model/dtype constraints
- **Effort ranking (effort.md):** #70 — Medium–high
- **Effort blockers:** GPU-only attention: xformers; GPU runtime: onnxruntime-gpu
- **Precisions noted:** unspecified
- **Models/flows noted:** —
- **Flow graph:** [flows/facepoke.md](../flows/facepoke.md)

### Snapshot verification (cloned analyzed commit)

- **Snapshot source:** `https://codeload.github.com/pinokiofactory/facepoke/tar.gz/<analyzed commit>` extracted to `/tmp/opencode/pinokio-snapshots/facepoke`
- **Files scanned:** 8 total (0 .py, 7 .js, 1 other)
- **Key files present:** pinokio.js, install.js, torch.js, start.js
- **TPU/CUDA-relevant signals:**
  - `xformers`: 5 match(es) (e.g. torch.js:11, torch.js:11)
  - `onnxruntime_gpu`: 2 match(es) (e.g. torch.js:12, torch.js:79)
  - `directml`: 2 match(es) (e.g. torch.js:25, torch.js:26)

### Evidence from analysis files

| Source | Evidence |
|---|---|
| [kernels.md](../analysis/kernels.md) | No per-repo kernel table row matched; see kernels.md for global signals. |
| [quantization.md](../analysis/quantization.md) | No per-repo quantization table row matched; see quantization.md. |
| [fusion.md](../analysis/fusion.md) | No direct fusion table row matched; see fusion.md for global context. |
| [models.md](../analysis/models.md) | No model pull/shape row matched in models.md. |
| [cpu.md](../analysis/cpu.md) | CPU category: **CPU-capable with shipped fallback** |
| [tpu.md](../analysis/tpu.md) | TPU suitability: **Difficult - significant port** — replace CUDA attention kernels with TPU-compatible attention/SDPA/XLA; replace onnxruntime-gpu with TPU-compatible runtime; multiple CUDA-specific dependencies or large model/dtype constraints |

### Related analysis

- [CPU analysis](../analysis/cpu.md)
- [TPU analysis](../analysis/tpu.md)
- [Effort ranking](../analysis/effort.md)
- [Kernel evidence](../analysis/kernels.md)
- [Quantization evidence](../analysis/quantization.md)
- [Fusion evidence](../analysis/fusion.md)
- [Model pulls/shapes](../analysis/models.md)
- [Flow graphs](../analysis/flows.md)
- [App flow graph](../flows/facepoke.md)
<!-- cross-analysis:end -->
