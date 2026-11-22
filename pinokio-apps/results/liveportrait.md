# liveportrait — portability analysis

- **Package name:** LivePortrait (`liveportrait`)
- **Description:** Bring portraits to life! https://github.com/KwaiVGI/LivePortrait
- **Original git URL:** https://github.com/pinokiofactory/liveportrait
- **Analyzed commit:** `b5fb16ce6df50e79d11d7c1a2d7b39faa720411e`
- **Platforms supported:** NVIDIA / AMD / Mac
- **Porting difficulty:** Low–medium
- **CUDA-only packages:** onnxruntime-gpu, xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

install, onnxruntime-gpu, torch, torch-directml, torchaudio, torchvision, xformers

Wheel indexes referenced: cpu, cu128, rocm6.0.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 388
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- `torch.js` routes present: nvidia, amd, mac, cpu.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): xformers
- Difficulty score: 2.5 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- import failed due to CUDA-only code path (torch.cuda) on CPU.
- Result: **not runnable in this container.**

## CPU port attempt

- **Attempt order:** #49 of 101 (by porting effort, easiest first).
- **Status:** CPU-capable (shipped fallback).
- **Changes applied / required:** use existing CPU wheel branch in torch.js; use existing non-NVIDIA/non-AMD branch in torch.js; use existing non-GPU launcher route; rely on devicetorch (already present); substitute GPU-only attention libs with SDPA math backend; remove GPU runtimes (onnxruntime-gpu/deepspeed/cudnn/tensorrt).
- **Smoke check:** n/a (no Python source in snapshot).
- **Blockers:** GPU-only attention: xformers; GPU runtime: onnxruntime-gpu.
- **Scope note:** static portability review of the Pinokio wrapper; no install or model download was executed.
<!-- cross-analysis:start -->
## Cross-analysis details

- **CPU category (cpu.md):** CPU-capable with shipped fallback
- **TPU suitability:** Difficult - significant port
- **TPU work needed:** replace CUDA attention kernels with TPU-compatible attention/SDPA/XLA; replace onnxruntime-gpu with TPU-compatible runtime; multiple CUDA-specific dependencies or large model/dtype constraints
- **Effort ranking (effort.md):** #49 — Medium
- **Effort blockers:** GPU-only attention: xformers; GPU runtime: onnxruntime-gpu
- **Precisions noted:** unspecified
- **Models/flows noted:** [KwaiVGI/LivePortrait](https://huggingface.co/KwaiVGI/LivePortrait), [cleardusk/LivePortrait-Windows](https://huggingface.co/cleardusk/LivePortrait-Windows)
- **Flow graph:** [flows/liveportrait.md](../flows/liveportrait.md)

### Snapshot verification (cloned analyzed commit)

- **Snapshot source:** `https://codeload.github.com/pinokiofactory/liveportrait/tar.gz/<analyzed commit>` extracted to `/tmp/opencode/pinokio-snapshots/liveportrait`
- **Files scanned:** 13 total (0 .py, 8 .js, 5 other)
- **Key files present:** pinokio.js, install.js, torch.js, start.js
- **TPU/CUDA-relevant signals:**
  - `xformers`: 5 match(es) (e.g. torch.js:10, torch.js:10)
  - `onnxruntime_gpu`: 1 match(es) (e.g. install.js:26)
  - `directml`: 1 match(es) (e.g. torch.js:21)

### Evidence from analysis files

| Source | Evidence |
|---|---|
| [kernels.md](../analysis/kernels.md) | No per-repo kernel table row matched; see kernels.md for global signals. |
| [quantization.md](../analysis/quantization.md) | No per-repo quantization table row matched; see quantization.md. |
| [fusion.md](../analysis/fusion.md) | No direct fusion table row matched; see fusion.md for global context. |
| [models.md](../analysis/models.md) | No model pull/shape row matched in models.md. |
| [cpu.md](../analysis/cpu.md) | CPU category: **CPU-capable with shipped fallback** |
| [tpu.md](../analysis/tpu.md) | TPU suitability: **Difficult - significant port** — replace CUDA attention kernels with TPU-compatible attention/SDPA/XLA; replace onnxruntime-gpu with TPU-compatible runtime; multiple CUDA-specific dependencies or large model/dtype constraints |

### Related analysis

- [CPU analysis](../analysis/cpu.md)
- [TPU analysis](../analysis/tpu.md)
- [Effort ranking](../analysis/effort.md)
- [Kernel evidence](../analysis/kernels.md)
- [Quantization evidence](../analysis/quantization.md)
- [Fusion evidence](../analysis/fusion.md)
- [Model pulls/shapes](../analysis/models.md)
- [Flow graphs](../analysis/flows.md)
- [App flow graph](../flows/liveportrait.md)
<!-- cross-analysis:end -->

## Snapdragon evaluation (deep clone)
- **Clone/scan status:** cloned and scanned
- **Files scanned:** 13 total (0 .py, 8 .js/.ts, 5 other)
- **Snapdragon-relevant signals:** torch=11, xformers=3, mps=1, directml=1, onnxruntime-gpu=1
- **Example evidence:**
  - torch: `common.js:14`
  - xformers: `common.js:18`
  - mps: `start.js:12`
  - directml: `torch.js:21`
  - onnxruntime-gpu: `install.js:26`
- **Snapdragon verdict:** Unsuitable (MLX/Apple-only runtime) for Snapdragon unless ported to CPU/ONNX.
