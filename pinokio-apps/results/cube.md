# cube — portability analysis

- **Package name:** cube (`cube`)
- **Description:** Roblox Foundation Model for 3D Intelligence --- Cross Platform (Mac, Windows, Linux): Requires 16GB+ VRAM PC or 18GB+ Memory Macs https://github.com/Roblox/cube
- **Original git URL:** https://github.com/pinokiofactory/cube
- **Analyzed commit:** `58844658cfc9eab4f8e956bab4883fa8d867cf44`
- **Platforms supported:** Cross-platform
- **Porting difficulty:** Low
- **CUDA-only packages:** xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

gradio, huggingface-hub, numpy, torch, torch-directml, torchaudio, torchvision, xformers

Wheel indexes referenced: cpu, cu128, rocm6.3.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 292
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- Explicit platform tag found: Cross-platform.
- `torch.js` routes present: nvidia, amd, mac, cpu.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): xformers
- Difficulty score: 0.5 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- Dependencies installed and app.py imported successfully on CPU (pymeshlab OpenGL warnings only).
- Result: **CPU port imports successfully.**

## CPU port attempt

- **Attempt order:** #24 of 101 (by porting effort, easiest first).
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
- **Effort ranking (effort.md):** #24 — Low
- **Effort blockers:** GPU-only attention: xformers
- **Precisions noted:** FP32
- **Models/flows noted:** [Roblox/cube3d-v0.1](https://huggingface.co/Roblox/cube3d-v0.1)
- **Flow graph:** [flows/cube.md](../flows/cube.md)

### Snapshot verification (cloned analyzed commit)

- **Snapshot source:** `https://codeload.github.com/pinokiofactory/cube/tar.gz/<analyzed commit>` extracted to `/tmp/opencode/pinokio-snapshots/cube`
- **Files scanned:** 11 total (0 .py, 7 .js, 4 other)
- **Key files present:** pinokio.js, install.js, torch.js, start.js
- **TPU/CUDA-relevant signals:**
  - `xformers`: 5 match(es) (e.g. torch.js:11, torch.js:11)
  - `directml`: 1 match(es) (e.g. torch.js:22)

### Evidence from analysis files

| Source | Evidence |
|---|---|
| [kernels.md](../analysis/kernels.md) | No per-repo kernel table row matched; see kernels.md for global signals. |
| [quantization.md](../analysis/quantization.md) | No per-repo quantization table row matched; see quantization.md. |
| [fusion.md](../analysis/fusion.md) | `\| [cube](https://github.com/pinokiofactory/cube) \| [5884465](https://github.com/pinokiofactory/cube/commit/58844658cfc9eab4f8e956bab4883fa8d867cf44) \| 437 \| [`cube.md`](../flows/cube.md) \|` |
| [fusion.md](../analysis/fusion.md) | `\| [cube](https://github.com/pinokiofactory/cube) \| [5884465](https://github.com/pinokiofactory/cube/commit/58844658cfc9eab4f8e956bab4883fa8d867cf44) \| 212 \| [`cube.md`](../flows/cube.md) \|` |
| [fusion.md](../analysis/fusion.md) | `\| [cube](https://github.com/pinokiofactory/cube) \| [5884465](https://github.com/pinokiofactory/cube/commit/58844658cfc9eab4f8e956bab4883fa8d867cf44) \| 0 \| 1 \| 212 \| 0 \| 437 \| 0 \| 650 \|` |
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
- [App flow graph](../flows/cube.md)
<!-- cross-analysis:end -->

## Snapdragon evaluation (deep clone)
- **Clone/scan status:** cloned and scanned
- **Files scanned:** 11 total (0 .py, 7 .js/.ts, 4 other)
- **Snapdragon-relevant signals:** torch=9, xformers=3, directml=1
- **Example evidence:**
  - torch: `install.js:29`
  - xformers: `install.js:33`
  - directml: `torch.js:22`
- **Snapdragon verdict:** No Python GEMM in wrapper; Snapdragon CPU-ready as launcher/wrapper (no model port).
