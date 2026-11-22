# invoke — portability analysis

- **Package name:** Invoke (`invoke`)
- **Description:** The Gen AI Platform for Pro Studios https://github.com/invoke-ai/InvokeAI
- **Original git URL:** https://github.com/pinokiofactory/invoke
- **Analyzed commit:** `67ac5a161a265badb1ff73d46c41f762c16bff35`
- **Platforms supported:** NVIDIA / AMD / Mac
- **Porting difficulty:** Low
- **CUDA-only packages:** —

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

invokeai

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 275
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- `torch.js` routes present: nvidia, amd, mac.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Difficulty score: 0.0 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- All JS files pass node --check. Upstream InvokeAI download is very large; not downloaded/tested in this container.
- Result: **static verification only.**

## CPU port attempt

- **Attempt order:** #7 of 101 (by porting effort, easiest first).
- **Status:** CPU-capable (shipped fallback).
- **Changes applied / required:** use existing non-NVIDIA/non-AMD branch in torch.js; use existing non-GPU launcher route.
- **Smoke check:** n/a (no Python source in snapshot).
- **Blockers:** none identified.
- **Scope note:** static portability review of the Pinokio wrapper; no install or model download was executed.
<!-- cross-analysis:start -->
## Cross-analysis details

- **CPU category (cpu.md):** CPU-capable with shipped fallback
- **TPU suitability:** Possible - straightforward PyTorch/XLA pilot
- **TPU work needed:** no hard CUDA source blocker identified; standard PyTorch/XLA bring-up expected
- **Effort ranking (effort.md):** #7 — Low
- **Effort blockers:** no source-level blocker found
- **Precisions noted:** unspecified
- **Models/flows noted:** —
- **Flow graph:** [flows/invoke.md](../flows/invoke.md)

### Snapshot verification (cloned analyzed commit)

- **Snapshot source:** `https://codeload.github.com/pinokiofactory/invoke/tar.gz/<analyzed commit>` extracted to `/tmp/opencode/pinokio-snapshots/invoke`
- **Files scanned:** 9 total (0 .py, 6 .js, 3 other)
- **Key files present:** pinokio.js, install.js, torch.js, start.js
- **TPU/CUDA-relevant signals:** none detected by text scan (still inspect runtime behavior before porting)

### Evidence from analysis files

| Source | Evidence |
|---|---|
| [kernels.md](../analysis/kernels.md) | No per-repo kernel table row matched; see kernels.md for global signals. |
| [quantization.md](../analysis/quantization.md) | No per-repo quantization table row matched; see quantization.md. |
| [fusion.md](../analysis/fusion.md) | No direct fusion table row matched; see fusion.md for global context. |
| [models.md](../analysis/models.md) | No model pull/shape row matched in models.md. |
| [cpu.md](../analysis/cpu.md) | CPU category: **CPU-capable with shipped fallback** |
| [tpu.md](../analysis/tpu.md) | TPU suitability: **Possible - straightforward PyTorch/XLA pilot** — no hard CUDA source blocker identified; standard PyTorch/XLA bring-up expected |

### Related analysis

- [CPU analysis](../analysis/cpu.md)
- [TPU analysis](../analysis/tpu.md)
- [Effort ranking](../analysis/effort.md)
- [Kernel evidence](../analysis/kernels.md)
- [Quantization evidence](../analysis/quantization.md)
- [Fusion evidence](../analysis/fusion.md)
- [Model pulls/shapes](../analysis/models.md)
- [Flow graphs](../analysis/flows.md)
- [App flow graph](../flows/invoke.md)
<!-- cross-analysis:end -->

## Snapdragon evaluation (deep clone)
- **Clone/scan status:** cloned and scanned
- **Files scanned:** 9 total (0 .py, 6 .js/.ts, 3 other)
- **Snapdragon-relevant signals:** torch=5
- **Example evidence:**
  - torch: `install.js:29`
- **Snapdragon verdict:** No Python GEMM in wrapper; Snapdragon CPU-ready as launcher/wrapper (no model port).
