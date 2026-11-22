# dough — portability analysis

- **Package name:** Dough (`dough`)
- **Description:** Dough is a open source tool for steering AI animations with precision
- **Original git URL:** https://github.com/pinokiofactory/dough
- **Analyzed commit:** `3e8a58b5da380ec15cd5743ffc57d220a64fdae1`
- **Platforms supported:** NVIDIA only
- **Porting difficulty:** Medium
- **CUDA-only packages:** torch (CUDA wheel)

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

torch, torchaudio, torchvision

Wheel indexes referenced: cu118.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 240
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- `torch.js` routes present: none.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Difficulty score: 4.0 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- retested on Python 3.10; import app.py failed with botocore NoCredentialsError (AWS credentials missing).
- Result: **not runnable in this container.**
<!-- cross-analysis:start -->
## Cross-analysis details

- **CPU category (cpu.md):** CPU possible, but launcher must change
- **TPU suitability:** Difficult - significant port
- **TPU work needed:** replace CUDA torch wheel with TPU-supported runtime; add TPU launcher/runtime branch; multiple CUDA-specific dependencies or large model/dtype constraints
- **Effort ranking (effort.md):** #69 — Medium–high
- **Effort blockers:** no CPU/AMD launcher branch; CUDA-only torch wheel
- **Precisions noted:** unspecified
- **Models/flows noted:** —
- **Flow graph:** [flows/dough.md](../flows/dough.md)

### Snapshot verification (cloned analyzed commit)

- **Snapshot source:** `https://codeload.github.com/pinokiofactory/dough/tar.gz/<analyzed commit>` extracted to `/tmp/opencode/pinokio-snapshots/dough`
- **Files scanned:** 11 total (1 .py, 8 .js, 2 other)
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
- [App flow graph](../flows/dough.md)
<!-- cross-analysis:end -->

## Snapdragon evaluation (deep clone)
- **Clone/scan status:** cloned and scanned
- **Files scanned:** 11 total (1 .py, 8 .js/.ts, 2 other)
- **Snapdragon-relevant signals:** torch=1
- **Example evidence:**
  - torch: `install.js:29`
- **Snapdragon verdict:** No CUDA signals; feasible on Snapdragon CPU via ARM64 wheels; GPU/NPU only via ONNX conversion.
