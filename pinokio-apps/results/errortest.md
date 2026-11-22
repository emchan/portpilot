# errortest — portability analysis

- **Package name:** errortest (`errortest`)
- **Description:** No description provided in the repository.
- **Original git URL:** https://github.com/pinokiofactory/errortest
- **Analyzed commit:** `dd4051727b682cdfdb3f0ae792875052bd4398b9`
- **Platforms supported:** Cross-platform
- **Porting difficulty:** Low
- **CUDA-only packages:** —

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

No package dependencies were declared in the repository. Installers that only run `npm install` or clone another app do not name packages here.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 48
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- `torch.js` routes present: none.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Difficulty score: 0.0 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- Installed on Python 3.12 with huggingface_hub==0.25.2; gradio and uvicorn import successfully.
- Result: **CPU port works with dependency/version fixes.**
<!-- cross-analysis:start -->
## Cross-analysis details

- **CPU category (cpu.md):** CPU-native / no local GEMM
- **TPU suitability:** Irrelevant - no local GEMM workload
- **TPU work needed:** No local GEMM/model workload; TPU gives no acceleration benefit
- **Effort ranking (effort.md):** #6 — Low
- **Effort blockers:** none — no local GEMM workload
- **Precisions noted:** unspecified
- **Models/flows noted:** —
- **Flow graph:** [flows/errortest.md](../flows/errortest.md)

### Snapshot verification (cloned analyzed commit)

- **Snapshot source:** `https://codeload.github.com/pinokiofactory/errortest/tar.gz/<analyzed commit>` extracted to `/tmp/opencode/pinokio-snapshots/errortest`
- **Files scanned:** 4 total (0 .py, 3 .js, 1 other)
- **Key files present:** pinokio.js
- **TPU/CUDA-relevant signals:**
  - `triton`: 1 match(es) (e.g. test.js:15)

### Evidence from analysis files

| Source | Evidence |
|---|---|
| [kernels.md](../analysis/kernels.md) | `\| [errortest](https://github.com/pinokiofactory/errortest) \| [dd40517](https://github.com/pinokiofactory/errortest/commit/dd4051727b682cdfdb3f0ae792875052bd4398b9) \| mention/hint \| test.js \| [test.js:15](https://github.com/pinokiofactory/errortest/blob/dd4051727b682cdfdb3f0ae792875052bd4398b9/test.js#L15) — //          "event": "/error:.*triton/i", \|` |
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
- [App flow graph](../flows/errortest.md)
<!-- cross-analysis:end -->

## Snapdragon evaluation (deep clone)
- **Clone/scan status:** cloned and scanned
- **Files scanned:** 4 total (0 .py, 3 .js/.ts, 1 other)
- **Snapdragon-relevant signals:** triton=1
- **Example evidence:**
  - triton: `test.js:15`
- **Snapdragon verdict:** Contains CUDA/Triton/TensorRT signals; Snapdragon path requires replacement or ONNX conversion.
