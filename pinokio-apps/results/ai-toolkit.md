# ai-toolkit — portability analysis

- **Package name:** ai-toolkit (`ai-toolkit`)
- **Description:** AI Toolkit by Ostris
- **Original git URL:** https://github.com/pinokiofactory/ai-toolkit
- **Analyzed commit:** `ddfefd70eb6f9d0b97c95e30b5c72aaac8660b0e`
- **Platforms supported:** NVIDIA only
- **Porting difficulty:** High
- **CUDA-only packages:** triton, triton-windows

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

numpy, torch, torchaudio, torchvision, triton, triton-windows

Wheel indexes referenced: cpu, cu128.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 307
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- Explicit platform tag found: NVIDIA only.
- `torch.js` routes present: nvidia, mac, cpu.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Difficulty score: 7.5 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- all JS files pass node --check; explicit NVIDIA-only guard prevents CPU install.
- Result: **not runnable in this container.**

## CPU port attempt

- **Attempt order:** #95 of 101 (by porting effort, easiest first).
- **Status:** Blocked.
- **Changes applied / required:** use existing CPU wheel branch in torch.js; use existing non-GPU launcher route; substitute GPU-only attention libs with SDPA math backend.
- **Smoke check:** n/a (no Python source in snapshot).
- **Blockers:** hard CUDA/TensorRT blocker; GPU-only attention: triton/triton-windows.
- **Scope note:** static portability review of the Pinokio wrapper; no install or model download was executed.
<!-- cross-analysis:start -->
## Cross-analysis details

- **CPU category (cpu.md):** Hard-blocked on CUDA
- **TPU suitability:** Hard - major rewrite/replacement required
- **TPU work needed:** CUDA/TensorRT/compiled CUDA extension dependency
- **Effort ranking (effort.md):** #95 — Very high
- **Effort blockers:** hard CUDA/TensorRT blocker in code; GPU-only attention: triton/triton-windows
- **Precisions noted:** unspecified
- **Models/flows noted:** —
- **Flow graph:** [flows/ai-toolkit.md](../flows/ai-toolkit.md)

### Snapshot verification (cloned analyzed commit)

- **Snapshot source:** `https://codeload.github.com/pinokiofactory/ai-toolkit/tar.gz/<analyzed commit>` extracted to `/tmp/opencode/pinokio-snapshots/ai-toolkit`
- **Files scanned:** 11 total (0 .py, 7 .js, 4 other)
- **Key files present:** pinokio.js, install.js, torch.js, start.js
- **TPU/CUDA-relevant signals:**
  - `triton`: 2 match(es) (e.g. torch.js:12, torch.js:39)

### Evidence from analysis files

| Source | Evidence |
|---|---|
| [kernels.md](../analysis/kernels.md) | `\| [ai-toolkit](https://github.com/pinokiofactory/ai-toolkit) \| [ddfefd7](https://github.com/pinokiofactory/ai-toolkit/commit/ddfefd70eb6f9d0b97c95e30b5c72aaac8660b0e) \| launcher install \| torch.js \| [torch.js:12](https://github.com/pinokiofactory/ai-toolkit/blob/ddfefd70eb6f9d0b97c95e30b5c72aaac8660b0e/torch.js#L12) — "uv pip install triton-windows==3.5.1.post22 --reinstall --no-deps" \|` |
| [quantization.md](../analysis/quantization.md) | No per-repo quantization table row matched; see quantization.md. |
| [fusion.md](../analysis/fusion.md) | No direct fusion table row matched; see fusion.md for global context. |
| [models.md](../analysis/models.md) | No model pull/shape row matched in models.md. |
| [cpu.md](../analysis/cpu.md) | CPU category: **Hard-blocked on CUDA** |
| [tpu.md](../analysis/tpu.md) | TPU suitability: **Hard - major rewrite/replacement required** — CUDA/TensorRT/compiled CUDA extension dependency |

### Related analysis

- [CPU analysis](../analysis/cpu.md)
- [TPU analysis](../analysis/tpu.md)
- [Effort ranking](../analysis/effort.md)
- [Kernel evidence](../analysis/kernels.md)
- [Quantization evidence](../analysis/quantization.md)
- [Fusion evidence](../analysis/fusion.md)
- [Model pulls/shapes](../analysis/models.md)
- [Flow graphs](../analysis/flows.md)
- [App flow graph](../flows/ai-toolkit.md)
<!-- cross-analysis:end -->
