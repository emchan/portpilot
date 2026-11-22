# LTX-Desktop-WanGP — portability analysis

- **Package name:** LTX-Desktop-WanGP (`LTX-Desktop-WanGP`)
- **Description:** [NVIDIA only] [Currently Windows only] LTX-Desktop powered By WanGP itself powered among other things by LTX-2 Engine
- **Original git URL:** https://github.com/pinokiofactory/LTX-Desktop-WanGP
- **Analyzed commit:** `2a3fedd030e9c7c12f9f67a14466007319ecc3d5`
- **Platforms supported:** NVIDIA only
- **Porting difficulty:** Medium
- **CUDA-only packages:** —

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

No package dependencies were declared in the repository. Installers that only run `npm install` or clone another app do not name packages here.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 182
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- Explicit platform tag found: NVIDIA only.
- `torch.js` routes present: none.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Difficulty score: 3.0 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- setup:dev:linux hung/timed out in this container.
- Result: **not runnable in this container.**

## CPU port attempt

- **Attempt order:** #58 of 101 (by porting effort, easiest first).
- **Status:** Needs launcher change.
- **Changes applied / required:** add a CPU wheel branch / remove GPU-only wheel pins.
- **Smoke check:** n/a (no Python source in snapshot).
- **Blockers:** no CPU/AMD launcher branch.
- **Scope note:** static portability review of the Pinokio wrapper; no install or model download was executed.
<!-- cross-analysis:start -->
## Cross-analysis details

- **CPU category (cpu.md):** CPU possible, but launcher must change
- **TPU suitability:** Possible - moderate port
- **TPU work needed:** add TPU launcher/runtime branch; moderate device/kernel/runtime adaptation
- **Effort ranking (effort.md):** #58 — Medium–high
- **Effort blockers:** no CPU/AMD launcher branch
- **Precisions noted:** unspecified
- **Models/flows noted:** —
- **Flow graph:** [flows/LTX-Desktop-WanGP.md](../flows/LTX-Desktop-WanGP.md)

### Snapshot verification (cloned analyzed commit)

- **Snapshot source:** `https://codeload.github.com/pinokiofactory/LTX-Desktop-WanGP/tar.gz/<analyzed commit>` extracted to `/tmp/opencode/pinokio-snapshots/LTX-Desktop-WanGP`
- **Files scanned:** 9 total (0 .py, 6 .js, 3 other)
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
| [tpu.md](../analysis/tpu.md) | TPU suitability: **Possible - moderate port** — add TPU launcher/runtime branch; moderate device/kernel/runtime adaptation |

### Related analysis

- [CPU analysis](../analysis/cpu.md)
- [TPU analysis](../analysis/tpu.md)
- [Effort ranking](../analysis/effort.md)
- [Kernel evidence](../analysis/kernels.md)
- [Quantization evidence](../analysis/quantization.md)
- [Fusion evidence](../analysis/fusion.md)
- [Model pulls/shapes](../analysis/models.md)
- [Flow graphs](../analysis/flows.md)
- [App flow graph](../flows/LTX-Desktop-WanGP.md)
<!-- cross-analysis:end -->

## Snapdragon evaluation (deep clone)
- **Clone/scan status:** cloned and scanned
- **Files scanned:** 9 total (0 .py, 6 .js/.ts, 3 other)
 - **Snapdragon-relevant signals:** none detected by text scan
- **Snapdragon verdict:** No Python GEMM in wrapper; Snapdragon CPU-ready as launcher/wrapper (no model port).
