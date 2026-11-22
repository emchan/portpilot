# MagicQuill — portability analysis

- **Package name:** MagicQuill (`MagicQuill`)
- **Description:** An intelligent, interactive Image Editing System. Easily erase and add objects on a user-friendly interface.
- **Original git URL:** https://github.com/pinokiofactory/MagicQuill
- **Analyzed commit:** `bfdae2847a85d7b00761b4e93fbcb91be5e6d494`
- **Platforms supported:** NVIDIA / AMD / Mac
- **Porting difficulty:** Medium
- **CUDA-only packages:** bitsandbytes, xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

bitsandbytes, huggingface-hub, numpy, torch, torch-directml, torchaudio, torchvision, xformers

Wheel indexes referenced: cpu, cu128, rocm6.3.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 357
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- `torch.js` routes present: nvidia, amd, mac, cpu.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): xformers
- Difficulty score: 3.0 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- retested on Python 3.12; blocked by gradio/huggingface_hub HfFolder incompatibility.
- Result: **not runnable in this container.**
<!-- cross-analysis:start -->
## Cross-analysis details

- **CPU category (cpu.md):** CPU-capable with shipped fallback
- **TPU suitability:** Difficult - significant port
- **TPU work needed:** replace CUDA attention kernels with TPU-compatible attention/SDPA/XLA; NF4/bitsandbytes quantization needs dequant/upcast or TPU-supported path; large BF16/FP16 GEMM workload; expect XLA compile/memory tuning; multiple CUDA-specific dependencies or large model/dtype constraints
- **Effort ranking (effort.md):** #53 — Medium
- **Effort blockers:** GPU-only attention: xformers; GPU quantisers: bitsandbytes; large FP16/BF16 GEMM load
- **Precisions noted:** FP16
- **Models/flows noted:** [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models)
- **Flow graph:** [flows/MagicQuill.md](../flows/MagicQuill.md)

### Snapshot verification (cloned analyzed commit)

- **Snapshot source:** `https://codeload.github.com/pinokiofactory/MagicQuill/tar.gz/<analyzed commit>` extracted to `/tmp/opencode/pinokio-snapshots/MagicQuill`
- **Files scanned:** 11 total (0 .py, 7 .js, 4 other)
- **Key files present:** pinokio.js, install.js, torch.js, start.js
- **TPU/CUDA-relevant signals:**
  - `xformers`: 5 match(es) (e.g. torch.js:10, torch.js:10)
  - `bitsandbytes`: 3 match(es) (e.g. torch.js:75, torch.js:75)
  - `directml`: 1 match(es) (e.g. torch.js:20)

### Evidence from analysis files

| Source | Evidence |
|---|---|
| [kernels.md](../analysis/kernels.md) | No per-repo kernel table row matched; see kernels.md for global signals. |
| [quantization.md](../analysis/quantization.md) | `\| [MagicQuill](https://github.com/pinokiofactory/MagicQuill) \| launcher install \| `torch.js:75` — "uv pip install https://github.com/bitsandbytes-foundation/bitsandbytes/releases/download/continuous-release_multi-backend-refactor/bitsandbytes-0.44.1.dev0-py3-n... \|` |
| [fusion.md](../analysis/fusion.md) | `\| [MagicQuill](https://github.com/pinokiofactory/MagicQuill) \| [bfdae28](https://github.com/pinokiofactory/MagicQuill/commit/bfdae2847a85d7b00761b4e93fbcb91be5e6d494) \| 40 \| `q_proj.weight` / `k_proj.weight` / `v_proj.weight` in `cond_stage_model.transformer.text_model.encoder.layers.0.self_attn` (LiuZichen/MagicQuill-models, B=`[768, 768]`) \| [`MagicQuill.md`](../flows/MagicQuill.md) \|` |
| [fusion.md](../analysis/fusion.md) | `\| [MagicQuill](https://github.com/pinokiofactory/MagicQuill) \| [bfdae28](https://github.com/pinokiofactory/MagicQuill/commit/bfdae2847a85d7b00761b4e93fbcb91be5e6d494) \| 552 \| [`MagicQuill.md`](../flows/MagicQuill.md) \|` |
| [fusion.md](../analysis/fusion.md) | `\| [MagicQuill](https://github.com/pinokiofactory/MagicQuill) \| [bfdae28](https://github.com/pinokiofactory/MagicQuill/commit/bfdae2847a85d7b00761b4e93fbcb91be5e6d494) \| 144 \| [`MagicQuill.md`](../flows/MagicQuill.md) \|` |
| [models.md](../analysis/models.md) | No model pull/shape row matched in models.md. |
| [cpu.md](../analysis/cpu.md) | CPU category: **CPU-capable with shipped fallback** |
| [tpu.md](../analysis/tpu.md) | TPU suitability: **Difficult - significant port** — replace CUDA attention kernels with TPU-compatible attention/SDPA/XLA; NF4/bitsandbytes quantization needs dequant/upcast or TPU-supported path; large BF16/FP16 GEMM workload; expect XLA compile/memory tuning; multiple CUDA-specific dependencies or large model/dtype constraints |

### Related analysis

- [CPU analysis](../analysis/cpu.md)
- [TPU analysis](../analysis/tpu.md)
- [Effort ranking](../analysis/effort.md)
- [Kernel evidence](../analysis/kernels.md)
- [Quantization evidence](../analysis/quantization.md)
- [Fusion evidence](../analysis/fusion.md)
- [Model pulls/shapes](../analysis/models.md)
- [Flow graphs](../analysis/flows.md)
- [App flow graph](../flows/MagicQuill.md)
<!-- cross-analysis:end -->

## Snapdragon evaluation (deep clone)
- **Clone/scan status:** cloned and scanned
- **Files scanned:** 11 total (0 .py, 7 .js/.ts, 4 other)
- **Snapdragon-relevant signals:** torch=13, xformers=3, bitsandbytes=1, directml=1, safetensors=5
- **Example evidence:**
  - torch: `install.js:46`
  - xformers: `install.js:73`
  - bitsandbytes: `torch.js:75`
  - directml: `torch.js:20`
  - safetensors: `models.yaml:2`
- **Snapdragon verdict:** No Python GEMM in wrapper; Snapdragon CPU-ready as launcher/wrapper (no model port).
