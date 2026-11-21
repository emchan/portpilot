# llamafactory — portability analysis

- **Package name:** LlamaFactory (`llamafactory`)
- **Description:** Unify Efficient Fine-Tuning of 100+ LLMs https://github.com/hiyouga/LLaMA-Factory
- **Original git URL:** https://github.com/pinokiofactory/llamafactory
- **Analyzed commit:** `e299b25b26f48bb6ef96a670c2da402f0e328441`
- **Platforms supported:** NVIDIA / AMD / Mac
- **Porting difficulty:** Medium–high
- **CUDA-only packages:** bitsandbytes, flash-attn, xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

bitsandbytes, flash-attn, numpy, torch, torch-directml, torchaudio, torchvision, xformers

Wheel indexes referenced: cpu, cu128, rocm6.3.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 315
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- `torch.js` routes present: nvidia, amd, mac, cpu.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): xformers
- Difficulty score: 6.0 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- dependencies installed and package imported successfully on CPU.
- Result: **CPU port imports successfully.**

## CPU port attempt

- **Attempt order:** #75 of 101 (by porting effort, easiest first).
- **Status:** CPU-capable (shipped fallback).
- **Changes applied / required:** use existing CPU wheel branch in torch.js; use existing non-NVIDIA/non-AMD branch in torch.js; use existing non-GPU launcher route; disable fused GPU kernels (xformers/flash/sage) in config; substitute GPU-only attention libs with SDPA math backend; remove bitsandbytes/torchao GPU quantisers or switch to GGUF.
- **Smoke check:** n/a (no Python source in snapshot).
- **Blockers:** GPU-only attention: flash-attn/xformers; GPU quantisers: bitsandbytes; CUDA-only fused kernels.
- **Scope note:** static portability review of the Pinokio wrapper; no install or model download was executed.
<!-- cross-analysis:start -->
## Cross-analysis details

- **CPU category (cpu.md):** CPU-capable with shipped fallback
- **TPU suitability:** Difficult - significant port
- **TPU work needed:** replace CUDA attention kernels with TPU-compatible attention/SDPA/XLA; NF4/bitsandbytes quantization needs dequant/upcast or TPU-supported path; multiple CUDA-specific dependencies or large model/dtype constraints
- **Effort ranking (effort.md):** #75 — Medium–high
- **Effort blockers:** GPU-only attention: flash-attn/xformers; GPU quantisers: bitsandbytes; CUDA-only fused kernels need config change
- **Precisions noted:** unspecified
- **Models/flows noted:** —
- **Flow graph:** [flows/llamafactory.md](../flows/llamafactory.md)

### Snapshot verification (cloned analyzed commit)

- **Snapshot source:** `https://codeload.github.com/pinokiofactory/llamafactory/tar.gz/<analyzed commit>` extracted to `/tmp/opencode/pinokio-snapshots/llamafactory`
- **Files scanned:** 10 total (0 .py, 7 .js, 3 other)
- **Key files present:** pinokio.js, install.js, torch.js, start.js
- **TPU/CUDA-relevant signals:**
  - `xformers`: 5 match(es) (e.g. torch.js:12, torch.js:12)
  - `flash_attn`: 4 match(es) (e.g. torch.js:13, torch.js:13)
  - `bitsandbytes`: 1 match(es) (e.g. install.js:32)
  - `directml`: 1 match(es) (e.g. torch.js:26)

### Evidence from analysis files

| Source | Evidence |
|---|---|
| [kernels.md](../analysis/kernels.md) | `\| [llamafactory](https://github.com/pinokiofactory/llamafactory) \| [e299b25](https://github.com/pinokiofactory/llamafactory/commit/e299b25b26f48bb6ef96a670c2da402f0e328441) \| launcher install \| [torch.js:13](https://github.com/pinokiofactory/llamafactory/blob/e299b25b26f48bb6ef96a670c2da402f0e328441/torch.js#L13) — "uv pip install https://github.com/mjun0812/flash-attention-prebuild-wheels/releases/download/v0.4.10/flash_attn-2.7.4+cu128torch2.7-cp311-cp311-win_amd64.whl"<br>[torch.js:73](https://github.com/pinokiofactory/llamafactory/blob/e299b25b26f48bb6ef96a670c2da402f0e328441/torch.js#L73) — "uv pip install https://github.com/mjun0812/flash-attention-prebuild-wheels/releases/download/v0.7.2/flash_attn-2.7.4+cu128torch2.7-cp311-cp311-linux_x86_64.whl" \|` |
| [quantization.md](../analysis/quantization.md) | `\| [llamafactory](https://github.com/pinokiofactory/llamafactory) \| launcher install \| `install.js:32` — "uv pip install bitsandbytes --no-deps", \|` |
| [fusion.md](../analysis/fusion.md) | `\| [llamafactory](https://github.com/pinokiofactory/llamafactory) \| [e299b25](https://github.com/pinokiofactory/llamafactory/commit/e299b25b26f48bb6ef96a670c2da402f0e328441) \| installed by launcher \| [torch.js:13](https://github.com/pinokiofactory/llamafactory/blob/e299b25b26f48bb6ef96a670c2da402f0e328441/torch.js#L13) — `"uv pip install https://github.com/mjun0812/flash-attention-prebuild-wheels/releases/download/v0.4.10/flash_attn-2.7.4+cu128torch2.7-cp311-cp311-win_a` \|` |
| [models.md](../analysis/models.md) | No model pull/shape row matched in models.md. |
| [cpu.md](../analysis/cpu.md) | CPU category: **CPU-capable with shipped fallback** |
| [tpu.md](../analysis/tpu.md) | TPU suitability: **Difficult - significant port** — replace CUDA attention kernels with TPU-compatible attention/SDPA/XLA; NF4/bitsandbytes quantization needs dequant/upcast or TPU-supported path; multiple CUDA-specific dependencies or large model/dtype constraints |

### Related analysis

- [CPU analysis](../analysis/cpu.md)
- [TPU analysis](../analysis/tpu.md)
- [Effort ranking](../analysis/effort.md)
- [Kernel evidence](../analysis/kernels.md)
- [Quantization evidence](../analysis/quantization.md)
- [Fusion evidence](../analysis/fusion.md)
- [Model pulls/shapes](../analysis/models.md)
- [Flow graphs](../analysis/flows.md)
- [App flow graph](../flows/llamafactory.md)
<!-- cross-analysis:end -->
