# augmentoolkit — portability analysis

- **Package name:** augmentoolkit (`augmentoolkit`)
- **Description:** Turn any raw text into a high-quality dataset for AI finetuning https://github.com/e-p-armstrong/augmentoolkit
- **Original git URL:** https://github.com/pinokiofactory/augmentoolkit
- **Analyzed commit:** `24f80371c8ae61a91295b71f773e41a2616437e6`
- **Platforms supported:** NVIDIA / AMD / Mac
- **Porting difficulty:** Low
- **CUDA-only packages:** xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

torch, torch-directml, torchaudio, torchvision, xformers

Wheel indexes referenced: cpu, cu121, rocm5.7.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 293
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- `torch.js` routes present: nvidia, amd, mac, cpu.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): xformers
- Difficulty score: 0.5 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- Dependency installation hung/timed out in this container.
- Result: **not runnable in this container.**

## CPU port attempt

- **Attempt order:** #22 of 101 (by porting effort, easiest first).
- **Status:** CPU-capable (shipped fallback).
- **Changes applied / required:** use existing CPU wheel branch in torch.js; use existing non-NVIDIA/non-AMD branch in torch.js; use existing non-GPU launcher route; substitute GPU-only attention libs with SDPA math backend.
- **Smoke check:** n/a (no Python source in snapshot).
- **Blockers:** GPU-only attention: xformers.
- **Scope note:** static portability review of the Pinokio wrapper; no install or model download was executed.
<!-- cross-analysis:start -->
## Cross-analysis details

- **CPU category (cpu.md):** CPU-capable with shipped fallback
- **TPU suitability:** Possible - moderate port
- **TPU work needed:** replace CUDA attention kernels with TPU-compatible attention/SDPA/XLA; moderate device/kernel/runtime adaptation
- **Effort ranking (effort.md):** #22 — Low
- **Effort blockers:** GPU-only attention: xformers
- **Precisions noted:** unspecified
- **Models/flows noted:** —
- **Flow graph:** [flows/augmentoolkit.md](../flows/augmentoolkit.md)

### Snapshot verification (cloned analyzed commit)

- **Snapshot source:** `https://codeload.github.com/pinokiofactory/augmentoolkit/tar.gz/<analyzed commit>` extracted to `/tmp/opencode/pinokio-snapshots/augmentoolkit`
- **Files scanned:** 13 total (0 .py, 7 .js, 6 other)
- **Key files present:** pinokio.js, install.js, torch.js, start.js, package.json
- **TPU/CUDA-relevant signals:**
  - `xformers`: 4 match(es) (e.g. torch.js:9, torch.js:9)
  - `directml`: 1 match(es) (e.g. torch.js:19)

### Evidence from analysis files

| Source | Evidence |
|---|---|
| [kernels.md](../analysis/kernels.md) | No per-repo kernel table row matched; see kernels.md for global signals. |
| [quantization.md](../analysis/quantization.md) | No per-repo quantization table row matched; see quantization.md. |
| [fusion.md](../analysis/fusion.md) | No direct fusion table row matched; see fusion.md for global context. |
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
- [App flow graph](../flows/augmentoolkit.md)
<!-- cross-analysis:end -->

## Snapdragon evaluation (deep clone)
- **Clone/scan status:** cloned and scanned
- **Files scanned:** 13 total (0 .py, 7 .js/.ts, 6 other)
- **Snapdragon-relevant signals:** torch=7, xformers=2, directml=1
- **Example evidence:**
  - torch: `torch.js:9`
  - xformers: `torch.js:9`
  - directml: `torch.js:19`
- **Snapdragon verdict:** No Python GEMM in wrapper; Snapdragon CPU-ready as launcher/wrapper (no model port).
