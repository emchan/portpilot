# stable-fast-3d — portability analysis

- **Package name:** stable-fast-3d (`stable-fast-3d`)
- **Description:** [NVIDIA ONLY] a state-of-the-art open-source model for fast feedforward 3D mesh reconstruction from a single image, from Stability AI. https://huggingface.co/spaces/stabilityai/stable-fast-3d
- **Original git URL:** https://github.com/pinokiofactory/stable-fast-3d
- **Analyzed commit:** `00fdb293b784f223c100971f37a23f2e8a801654`
- **Platforms supported:** NVIDIA only
- **Porting difficulty:** Medium
- **CUDA-only packages:** xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

devicetorch, gradio, nvidia, rembg, torch, torch-directml, torchaudio, torchvision, xformers

Wheel indexes referenced: cpu, cu121, rocm6.0.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 262
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- Explicit platform tag found: NVIDIA only.
- `torch.js` routes present: nvidia, amd, mac, cpu.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): xformers
- Difficulty score: 3.5 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- retested on Python 3.12; blocked by scipy 1.18/numpy 1.26.4 mismatch (np.long removed).
- Result: **not runnable in this container.**
<!-- cross-analysis:start -->
## Cross-analysis details

- **CPU category (cpu.md):** CPU-capable with shipped fallback
- **TPU suitability:** Possible - moderate port
- **TPU work needed:** replace CUDA attention kernels with TPU-compatible attention/SDPA/XLA; moderate device/kernel/runtime adaptation
- **Effort ranking (effort.md):** #55 — Medium
- **Effort blockers:** GPU-only attention: xformers; CUDA-only fused kernels need config change
- **Precisions noted:** FP32
- **Models/flows noted:** [cocktailpeanut/sf3d](https://huggingface.co/cocktailpeanut/sf3d)
- **Flow graph:** [flows/stable-fast-3d.md](../flows/stable-fast-3d.md)

### Snapshot verification (cloned analyzed commit)

- **Snapshot source:** `https://codeload.github.com/pinokiofactory/stable-fast-3d/tar.gz/<analyzed commit>` extracted to `/tmp/opencode/pinokio-snapshots/stable-fast-3d`
- **Files scanned:** 9 total (0 .py, 6 .js, 3 other)
- **Key files present:** pinokio.js, install.js, torch.js, start.js
- **TPU/CUDA-relevant signals:**
  - `xformers`: 6 match(es) (e.g. torch.js:10, torch.js:10)
  - `directml`: 1 match(es) (e.g. torch.js:20)

### Evidence from analysis files

| Source | Evidence |
|---|---|
| [kernels.md](../analysis/kernels.md) | No per-repo kernel table row matched; see kernels.md for global signals. |
| [quantization.md](../analysis/quantization.md) | No per-repo quantization table row matched; see quantization.md. |
| [fusion.md](../analysis/fusion.md) | `\| [stable-fast-3d](https://github.com/pinokiofactory/stable-fast-3d) \| [00fdb29](https://github.com/pinokiofactory/stable-fast-3d/commit/00fdb293b784f223c100971f37a23f2e8a801654) \| 24 \| `query.weight` / `key.weight` / `value.weight` in `image_tokenizer.model.encoder.layer.0.attention.attention` (cocktailpeanut/sf3d, B=`[1024, 1024]`) \| [`stable-fast-3d.md`](../flows/stable-fast-3d.md) \|` |
| [fusion.md](../analysis/fusion.md) | `\| [stable-fast-3d](https://github.com/pinokiofactory/stable-fast-3d) \| [00fdb29](https://github.com/pinokiofactory/stable-fast-3d/commit/00fdb293b784f223c100971f37a23f2e8a801654) \| 24 \| 1 \| 48 \| 0 \| 373 \| 7 \| 453 \|` |
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
- [App flow graph](../flows/stable-fast-3d.md)
<!-- cross-analysis:end -->
