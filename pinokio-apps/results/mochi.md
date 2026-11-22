# mochi — portability analysis

- **Package name:** mochi (`mochi`)
- **Description:** # mochi
- **Original git URL:** https://github.com/pinokiofactory/mochi
- **Analyzed commit:** `93d4b2bddb16f3ce883f47336f1de7c126955d6e`
- **Platforms supported:** NVIDIA / AMD / Mac
- **Porting difficulty:** Low
- **CUDA-only packages:** xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

numpy, torch, torch-directml, torchaudio, torchvision, wheel, xformers

Wheel indexes referenced: cpu, cu121, rocm6.0.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 303
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- `torch.js` routes present: nvidia, amd, mac, cpu.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): xformers
- Difficulty score: 0.5 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- package imported successfully on CPU (moviepy/pillow dependency conflict not resolved).
- Result: **CPU port imports successfully.**

## CPU port attempt

- **Attempt order:** #32 of 101 (by porting effort, easiest first).
- **Status:** CPU-capable (shipped fallback).
- **Changes applied / required:** use existing CPU wheel branch in torch.js; use existing non-NVIDIA/non-AMD branch in torch.js; use existing non-GPU launcher route; rely on devicetorch (already present); disable fused GPU kernels (xformers/flash/sage) in config; substitute GPU-only attention libs with SDPA math backend.
- **Smoke check:** n/a (no Python source in snapshot).
- **Blockers:** GPU-only attention: xformers; CUDA-only fused kernels.
- **Scope note:** static portability review of the Pinokio wrapper; no install or model download was executed.
<!-- cross-analysis:start -->
## Cross-analysis details

- **CPU category (cpu.md):** CPU-capable with shipped fallback
- **TPU suitability:** Possible - moderate port
- **TPU work needed:** replace CUDA attention kernels with TPU-compatible attention/SDPA/XLA; moderate device/kernel/runtime adaptation
- **Effort ranking (effort.md):** #32 — Low
- **Effort blockers:** GPU-only attention: xformers; CUDA-only fused kernels need config change
- **Precisions noted:** FP32
- **Models/flows noted:** [genmo/mochi-1-preview](https://huggingface.co/genmo/mochi-1-preview)
- **Flow graph:** [flows/mochi.md](../flows/mochi.md)

### Snapshot verification (cloned analyzed commit)

- **Snapshot source:** `https://codeload.github.com/pinokiofactory/mochi/tar.gz/<analyzed commit>` extracted to `/tmp/opencode/pinokio-snapshots/mochi`
- **Files scanned:** 9 total (0 .py, 6 .js, 3 other)
- **Key files present:** pinokio.js, install.js, torch.js, start.js
- **TPU/CUDA-relevant signals:**
  - `xformers`: 6 match(es) (e.g. torch.js:10, torch.js:10)
  - `flash_attn`: 5 match(es) (e.g. install.js:19, install.js:19)
  - `directml`: 1 match(es) (e.g. torch.js:20)

### Evidence from analysis files

| Source | Evidence |
|---|---|
| [kernels.md](../analysis/kernels.md) | `\| [mochi](https://github.com/pinokiofactory/mochi) \| [93d4b2b](https://github.com/pinokiofactory/mochi/commit/93d4b2bddb16f3ce883f47336f1de7c126955d6e) \| mention/hint \| [install.js:19](https://github.com/pinokiofactory/mochi/blob/93d4b2bddb16f3ce883f47336f1de7c126955d6e/install.js#L19) — //        message: "pip install https://github.com/oobabooga/flash-attention/releases/download/v2.6.3/flash_attn-2.6.3+cu122torch2.4.1cxx11abiFALSE-cp310-cp310-wi...<br>[install.js:28](https://github.com/pinokiofactory/mochi/blob/93d4b2bddb16f3ce883f47336f1de7c126955d6e/install.js#L28) — //        message: "pip install https://github.com/Dao-AILab/flash-attention/releases/download/v2.6.3/flash_attn-2.6.3+cu123torch2.4cxx11abiFALSE-cp310-cp310-linu... \|` |
| [quantization.md](../analysis/quantization.md) | No per-repo quantization table row matched; see quantization.md. |
| [fusion.md](../analysis/fusion.md) | `\| [mochi](https://github.com/pinokiofactory/mochi) \| [93d4b2b](https://github.com/pinokiofactory/mochi/commit/93d4b2bddb16f3ce883f47336f1de7c126955d6e) \| commented-out flag \| [install.js:19](https://github.com/pinokiofactory/mochi/blob/93d4b2bddb16f3ce883f47336f1de7c126955d6e/install.js#L19) — `// message: "pip install https://github.com/oobabooga/flash-attention/releases/download/v2.6.3/flash_attn-2.6.3+cu122torch2.4.1cxx11abiFALSE-cp310-cp3` \|` |
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
- [App flow graph](../flows/mochi.md)
<!-- cross-analysis:end -->

## Snapdragon evaluation (deep clone)
- **Clone/scan status:** cloned and scanned
- **Files scanned:** 9 total (0 .py, 6 .js/.ts, 3 other)
- **Snapdragon-relevant signals:** cuda=1, torch=12, xformers=3, directml=1
- **Example evidence:**
  - cuda: `start.js:11`
  - torch: `install.js:19`
  - xformers: `install.js:53`
  - directml: `torch.js:20`
- **Snapdragon verdict:** Contains CUDA/Triton/TensorRT signals; Snapdragon path requires replacement or ONNX conversion.
