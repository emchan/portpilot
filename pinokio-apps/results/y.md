# y — portability analysis

- **Package name:** y (`y`)
- **Description:** No description provided in the repository.
- **Original git URL:** https://github.com/pinokiofactory/y
- **Analyzed commit:** N/A (empty repository)
- **Platforms supported:** N/A (empty repository)
- **Porting difficulty:** N/A (empty repository)
- **CUDA-only packages:** —

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

No package dependencies were declared in the repository. Installers that only run `npm install` or clone another app do not name packages here.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 0
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- Difficulty score: 0 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- Empty repository; no install, dependency, or runtime test possible.
- Result: **N/A (empty repository).**

## CPU port attempt

- **Attempt order:** #101 of 101 (by porting effort, easiest first).
- **Status:** N/A (empty).
- **Changes applied / required:** none — empty repository.
- **Smoke check:** n/a (no Python source in snapshot).
- **Blockers:** empty repository.
- **Scope note:** static portability review of the Pinokio wrapper; no install or model download was executed.
<!-- cross-analysis:start -->
## Cross-analysis details

- **CPU category (cpu.md):** Unclassified in cpu.md
- **TPU suitability:** N/A - empty repository
- **TPU work needed:** Empty repository; no runtime to port
- **Effort ranking (effort.md):** #101 — N/A
- **Effort blockers:** Empty repository
- **Precisions noted:** unspecified
- **Models/flows noted:** —
- **Flow graph:** [flows/y.md](../flows/y.md)

### Snapshot verification (cloned analyzed commit)

- **Snapshot source:** `https://codeload.github.com/pinokiofactory/y/tar.gz/<analyzed commit>` extracted to `/tmp/opencode/pinokio-snapshots/y`
- **Files scanned:** 0 total (0 .py, 0 .js, 0 other)
- **Key files present:** none of the common launcher files found
- **TPU/CUDA-relevant signals:** none detected by text scan (still inspect runtime behavior before porting)

### Evidence from analysis files

| Source | Evidence |
|---|---|
| [kernels.md](../analysis/kernels.md) | No per-repo kernel table row matched; see kernels.md for global signals. |
| [quantization.md](../analysis/quantization.md) | No per-repo quantization table row matched; see quantization.md. |
| [fusion.md](../analysis/fusion.md) | No direct fusion table row matched; see fusion.md for global context. |
| [models.md](../analysis/models.md) | No model pull/shape row matched in models.md. |
| [cpu.md](../analysis/cpu.md) | CPU category: **Unclassified in cpu.md** |
| [tpu.md](../analysis/tpu.md) | TPU suitability: **N/A - empty repository** — Empty repository; no runtime to port |

### Related analysis

- [CPU analysis](../analysis/cpu.md)
- [TPU analysis](../analysis/tpu.md)
- [Effort ranking](../analysis/effort.md)
- [Kernel evidence](../analysis/kernels.md)
- [Quantization evidence](../analysis/quantization.md)
- [Fusion evidence](../analysis/fusion.md)
- [Model pulls/shapes](../analysis/models.md)
- [Flow graphs](../analysis/flows.md)
- [App flow graph](../flows/y.md)
<!-- cross-analysis:end -->
