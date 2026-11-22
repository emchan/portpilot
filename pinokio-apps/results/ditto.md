# ditto — portability analysis

- **Package name:** ditto (`ditto`)
- **Description:** the simplest self-building coding agent https://github.com/yoheinakajima/ditto
- **Original git URL:** https://github.com/pinokiofactory/ditto
- **Analyzed commit:** `aa45279201a7ddaead5ac33d56feba35417319c5`
- **Platforms supported:** Cross-platform
- **Porting difficulty:** Low
- **CUDA-only packages:** —

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

flask, litellm

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 204
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- `torch.js` routes present: none.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Difficulty score: 0.0 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-20)

- Downloaded upstream `yoheinakajima/ditto`; installed dependencies on CPU.
- Pinned `litellm` could not be satisfied on Python 3.14, so installed the current `litellm` release plus `flask`.
- Flask app started successfully on `http://127.0.0.1:8080`.
- Result: **CPU port works with dependency updates.**

## CPU port attempt

- **Attempt order:** #5 of 101 (by porting effort, easiest first).
- **Status:** CPU-ready (no changes).
- **Changes applied / required:** no change required (no local GEMM workload); add a CPU wheel branch / remove GPU-only wheel pins.
- **Smoke check:** n/a (no Python source in snapshot).
- **Blockers:** none identified.
- **Scope note:** static portability review of the Pinokio wrapper; no install or model download was executed.
<!-- cross-analysis:start -->
## Cross-analysis details

- **CPU category (cpu.md):** CPU-native / no local GEMM
- **TPU suitability:** Irrelevant - no local GEMM workload
- **TPU work needed:** No local GEMM/model workload; TPU gives no acceleration benefit
- **Effort ranking (effort.md):** #5 — Low
- **Effort blockers:** none — no local GEMM workload
- **Precisions noted:** unspecified
- **Models/flows noted:** —
- **Flow graph:** [flows/ditto.md](../flows/ditto.md)

### Snapshot verification (cloned analyzed commit)

- **Snapshot source:** `https://codeload.github.com/pinokiofactory/ditto/tar.gz/<analyzed commit>` extracted to `/tmp/opencode/pinokio-snapshots/ditto`
- **Files scanned:** 11 total (0 .py, 6 .js, 5 other)
- **Key files present:** pinokio.js, install.js, start.js
- **TPU/CUDA-relevant signals:** none detected by text scan (still inspect runtime behavior before porting)

### Evidence from analysis files

| Source | Evidence |
|---|---|
| [kernels.md](../analysis/kernels.md) | No per-repo kernel table row matched; see kernels.md for global signals. |
| [quantization.md](../analysis/quantization.md) | No per-repo quantization table row matched; see quantization.md. |
| [fusion.md](../analysis/fusion.md) | No direct fusion table row matched; see fusion.md for global context. |
| [models.md](../analysis/models.md) | No model pull/shape row matched in models.md. |
| [cpu.md](../analysis/cpu.md) | CPU category: **CPU-native / no local GEMM** |
| [tpu.md](../analysis/tpu.md) | TPU suitability: **Irrelevant - no local GEMM workload** — No local GEMM/model workload; TPU gives no acceleration benefit |

### Related analysis

- [CPU analysis](../analysis/cpu.md)
- [TPU analysis](../analysis/tpu.md)
- [Effort ranking](../analysis/effort.md)
- [Kernel evidence](../analysis/kernels.md)
- [Quantization evidence](../analysis/quantization.md)
- [Fusion evidence](../analysis/fusion.md)
- [Model pulls/shapes](../analysis/models.md)
- [Flow graphs](../analysis/flows.md)
- [App flow graph](../flows/ditto.md)
<!-- cross-analysis:end -->

## Snapdragon evaluation (deep clone)
- **Clone/scan status:** cloned and scanned
- **Files scanned:** 11 total (0 .py, 6 .js/.ts, 5 other)
 - **Snapdragon-relevant signals:** none detected by text scan
- **Snapdragon verdict:** No Python GEMM in wrapper; Snapdragon CPU-ready as launcher/wrapper (no model port).
