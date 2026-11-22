# applio-old — portability analysis

- **Package name:** Applio (`applio-old`)
- **Description:** VITS-based Voice Conversion focused on simplicity, quality and performance
- **Original git URL:** https://github.com/pinokiofactory/applio-old
- **Analyzed commit:** `a8d276c8f426304428755974392b5e42d4ef29a5`
- **Platforms supported:** NVIDIA only
- **Porting difficulty:** Medium
- **CUDA-only packages:** torch (CUDA wheel)

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

setuptools, torch, torchaudio, torchvision

Wheel indexes referenced: cu121.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 193
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- `torch.js` routes present: none.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Difficulty score: 4.0 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- requires Python 3.9 and CUDA 12.1 wheels; not runnable on this Python 3.14 CPU container.
- Result: **not runnable in this container.**

## CPU port attempt

- **Attempt order:** #68 of 101 (by porting effort, easiest first).
- **Status:** Needs launcher change.
- **Changes applied / required:** add a CPU wheel branch / remove GPU-only wheel pins; replace CUDA-only torch wheel with CPU wheel.
- **Smoke check:** n/a (no Python source in snapshot).
- **Blockers:** no CPU/AMD launcher branch; CUDA-only torch wheel.
- **Scope note:** static portability review of the Pinokio wrapper; no install or model download was executed.
<!-- cross-analysis:start -->
## Cross-analysis details

- **CPU category (cpu.md):** CPU possible, but launcher must change
- **TPU suitability:** Difficult - significant port
- **TPU work needed:** replace CUDA torch wheel with TPU-supported runtime; add TPU launcher/runtime branch; multiple CUDA-specific dependencies or large model/dtype constraints
- **Effort ranking (effort.md):** #68 — Medium–high
- **Effort blockers:** no CPU/AMD launcher branch; CUDA-only torch wheel
- **Precisions noted:** unspecified
- **Models/flows noted:** [IAHispano/Applio](https://huggingface.co/IAHispano/Applio)
- **Flow graph:** [flows/applio-old.md](../flows/applio-old.md)

### Snapshot verification (cloned analyzed commit)

- **Snapshot source:** `https://codeload.github.com/pinokiofactory/applio-old/tar.gz/<analyzed commit>` extracted to `/tmp/opencode/pinokio-snapshots/applio-old`
- **Files scanned:** 6 total (0 .py, 5 .js, 1 other)
- **Key files present:** pinokio.js, install.js, start.js
- **TPU/CUDA-relevant signals:** none detected by text scan (still inspect runtime behavior before porting)

### Evidence from analysis files

| Source | Evidence |
|---|---|
| [kernels.md](../analysis/kernels.md) | No per-repo kernel table row matched; see kernels.md for global signals. |
| [quantization.md](../analysis/quantization.md) | No per-repo quantization table row matched; see quantization.md. |
| [fusion.md](../analysis/fusion.md) | No direct fusion table row matched; see fusion.md for global context. |
| [models.md](../analysis/models.md) | No model pull/shape row matched in models.md. |
| [cpu.md](../analysis/cpu.md) | CPU category: **CPU possible, but launcher must change** |
| [tpu.md](../analysis/tpu.md) | TPU suitability: **Difficult - significant port** — replace CUDA torch wheel with TPU-supported runtime; add TPU launcher/runtime branch; multiple CUDA-specific dependencies or large model/dtype constraints |

### Related analysis

- [CPU analysis](../analysis/cpu.md)
- [TPU analysis](../analysis/tpu.md)
- [Effort ranking](../analysis/effort.md)
- [Kernel evidence](../analysis/kernels.md)
- [Quantization evidence](../analysis/quantization.md)
- [Fusion evidence](../analysis/fusion.md)
- [Model pulls/shapes](../analysis/models.md)
- [Flow graphs](../analysis/flows.md)
- [App flow graph](../flows/applio-old.md)
<!-- cross-analysis:end -->

## Snapdragon evaluation (deep clone)
- **Clone/scan status:** cloned and scanned
- **Files scanned:** 6 total (0 .py, 5 .js/.ts, 1 other)
- **Snapdragon-relevant signals:** torch=2
- **Example evidence:**
  - torch: `install.js:48`
- **Snapdragon verdict:** No Python GEMM in wrapper; Snapdragon CPU-ready as launcher/wrapper (no model port).
