# Hunyuan3d-2-lowvram — portability analysis

- **Package name:** Hunyuan3D-2-LowVRAM (`Hunyuan3d-2-lowvram`)
- **Description:** Text/Image to 3D (Cross Platform: Mac + Windows + Linux): High-Resolution 3D Assets Generation with Large Scale Hunyuan3D Diffusion Models. https://github.com/deepbeepmeep/Hunyuan3D-2GP
- **Original git URL:** https://github.com/pinokiofactory/Hunyuan3d-2-lowvram
- **Analyzed commit:** `9c415021473ec16b64b85bda5d3d50295c478e5b`
- **Platforms supported:** Cross-platform
- **Porting difficulty:** Low
- **CUDA-only packages:** xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

diffusers, diso, gradio, gxx, huggingface-hub, numba, numpy, sentencepiece, setuptools, torch, torch-directml, torchaudio, torchvision, wheel, xformers

Wheel indexes referenced: cpu, cu128, rocm6.3.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 633
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- Explicit platform tag found: Cross-platform.
- `torch.js` routes present: nvidia, amd, mac, cpu.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): xformers
- Difficulty score: 0.5 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- Upstream install blocked by compiled extension/build failures (diso, xatlas, pillow/pydantic) in this environment.
- Result: **not runnable in this container.**

## CPU port attempt

- **Attempt order:** #13 of 101 (by porting effort, easiest first).
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
- **Effort ranking (effort.md):** #13 — Low
- **Effort blockers:** GPU-only attention: xformers
- **Precisions noted:** unspecified
- **Models/flows noted:** —
- **Flow graph:** [flows/Hunyuan3d-2-lowvram.md](../flows/Hunyuan3d-2-lowvram.md)

### Snapshot verification (cloned analyzed commit)

- **Snapshot source:** `https://codeload.github.com/pinokiofactory/Hunyuan3d-2-lowvram/tar.gz/<analyzed commit>` extracted to `/tmp/opencode/pinokio-snapshots/Hunyuan3d-2-lowvram`
- **Files scanned:** 13 total (0 .py, 6 .js, 7 other)
- **Key files present:** pinokio.js, install.js, torch.js, start.js
- **TPU/CUDA-relevant signals:**
  - `xformers`: 5 match(es) (e.g. torch.js:10, torch.js:10)
  - `directml`: 1 match(es) (e.g. torch.js:21)
  - `mps`: 1 match(es) (e.g. start.js:5)

### Evidence from analysis files

| Source | Evidence |
|---|---|
| [kernels.md](../analysis/kernels.md) | `\| [Hunyuan3d-2-lowvram](https://github.com/pinokiofactory/Hunyuan3d-2-lowvram) \| [9c41502](https://github.com/pinokiofactory/Hunyuan3d-2-lowvram/commit/9c415021473ec16b64b85bda5d3d50295c478e5b) \| direct code + optional flag \| [start.js:5](https://github.com/pinokiofactory/Hunyuan3d-2-lowvram/blob/9c415021473ec16b64b85bda5d3d50295c478e5b/start.js#L5) — cmd = `python gradio_app.py {{args.model_path ? '--model_path ' + args.model_path : ''}} {{ args.subfolder ? '--subfolder ' + args.subfolder : ''}} --enable_t23d ... \|` |
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
- [App flow graph](../flows/Hunyuan3d-2-lowvram.md)
<!-- cross-analysis:end -->

## Snapdragon evaluation (deep clone)
- **Clone/scan status:** cloned and scanned
- **Files scanned:** 13 total (0 .py, 6 .js/.ts, 7 other)
- **Snapdragon-relevant signals:** cuda=3, torch=11, xformers=3, mps=1, directml=1
- **Example evidence:**
  - cuda: `install.js:49`
  - torch: `install.js:17`
  - xformers: `install.js:21`
  - mps: `start.js:5`
  - directml: `torch.js:21`
- **Snapdragon verdict:** Contains CUDA/Triton/TensorRT signals; Snapdragon path requires replacement or ONNX conversion.
