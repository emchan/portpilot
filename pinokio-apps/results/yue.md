# yue — portability analysis

- **Package name:** YuE (`yue`)
- **Description:** [NVIDIA ONLY] YuEGP--A Web UI for YuE, an Open Full-song Generation Foundation Model (10G VRAM required), via https://github.com/deepbeepmeep/YuEGP
- **Original git URL:** https://github.com/pinokiofactory/yue
- **Analyzed commit:** `3261118f111c8d2bb098b82b2870458dfbc486c7`
- **Platforms supported:** NVIDIA only
- **Porting difficulty:** Very high
- **CUDA-only packages:** flash-attn, triton *(optional)*, triton-windows, xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

flash-attn, hf-xet, torch, torchaudio, torchvision, transformers, triton, triton-windows, xformers

Wheel indexes referenced: cu121, cu124, cu128, rocm6.3.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 385
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- Explicit platform tag found: NVIDIA only.
- `torch.js` routes present: nvidia, amd.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): triton, xformers
- Difficulty score: 10.2 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- retested on Python 3.10; dependencies installed and inference module imported successfully on CPU.
- Result: **CPU port imports successfully.**
<!-- cross-analysis:start -->
## Cross-analysis details

- **CPU category (cpu.md):** CPU possible, but launcher must change
- **TPU suitability:** Difficult - significant port
- **TPU work needed:** replace CUDA attention kernels with TPU-compatible attention/SDPA/XLA; add TPU launcher/runtime branch; multiple CUDA-specific dependencies or large model/dtype constraints
- **Effort ranking (effort.md):** #92 — Very high
- **Effort blockers:** no CPU/AMD launcher branch; GPU-only attention: flash-attn/triton/triton-windows/xformers; CUDA-only fused kernels need config change
- **Precisions noted:** unspecified
- **Models/flows noted:** [m-a-p/xcodec_mini_infer](https://huggingface.co/m-a-p/xcodec_mini_infer)
- **Flow graph:** [flows/yue.md](../flows/yue.md)

### Snapshot verification (cloned analyzed commit)

- **Snapshot source:** `https://codeload.github.com/pinokiofactory/yue/tar.gz/<analyzed commit>` extracted to `/tmp/opencode/pinokio-snapshots/yue`
- **Files scanned:** 11 total (0 .py, 7 .js, 4 other)
- **Key files present:** pinokio.js, install.js, torch.js, start.js
- **TPU/CUDA-relevant signals:**
  - `xformers`: 9 match(es) (e.g. torch.js:12, torch.js:12)
  - `flash_attn`: 8 match(es) (e.g. torch.js:14, torch.js:14)
  - `triton`: 9 match(es) (e.g. torch.js:13, torch.js:13)

### Evidence from analysis files

| Source | Evidence |
|---|---|
| [kernels.md](../analysis/kernels.md) | `\| [yue](https://github.com/pinokiofactory/yue) \| [3261118](https://github.com/pinokiofactory/yue/commit/3261118f111c8d2bb098b82b2870458dfbc486c7) \| optional flag + launcher install \| install.js, torch.js \| [torch.js:13](https://github.com/pinokiofactory/yue/blob/3261118f111c8d2bb098b82b2870458dfbc486c7/torch.js#L13) — "{{args && args.triton ? 'uv pip install triton-windows==3.3.1.post19' : ''}}", \|` |
| [kernels.md](../analysis/kernels.md) | `\| [yue](https://github.com/pinokiofactory/yue) \| [3261118](https://github.com/pinokiofactory/yue/commit/3261118f111c8d2bb098b82b2870458dfbc486c7) \| launcher install \| [torch.js:14](https://github.com/pinokiofactory/yue/blob/3261118f111c8d2bb098b82b2870458dfbc486c7/torch.js#L14) — "uv pip install https://huggingface.co/lldacing/flash-attention-windows-wheel/resolve/main/flash_attn-2.7.4.post1%2Bcu128torch2.7.0cxx11abiFALSE-cp311-cp311-win_a...<br>[torch.js:30](https://github.com/pinokiofactory/yue/blob/3261118f111c8d2bb098b82b2870458dfbc486c7/torch.js#L30) — "uv pip install https://huggingface.co/lldacing/flash-attention-windows-wheel/resolve/main/flash_attn-2.7.0.post2%2Bcu124torch2.5.1cxx11abiFALSE-cp311-cp311-win_a... \|` |
| [quantization.md](../analysis/quantization.md) | `\| [yue](https://github.com/pinokiofactory/yue) \| reference \| `pinokio.js:77` — text: "12g vram (quantized)",<br>`pinokio.js:84` — text: "10g vram (quantized)", \|` |
| [fusion.md](../analysis/fusion.md) | `\| [yue](https://github.com/pinokiofactory/yue) \| [3261118](https://github.com/pinokiofactory/yue/commit/3261118f111c8d2bb098b82b2870458dfbc486c7) \| [start.js:18](https://github.com/pinokiofactory/yue/blob/3261118f111c8d2bb098b82b2870458dfbc486c7/start.js#L18) \| Launcher forwards `--compile` to the upstream Gradio server \|` |
| [fusion.md](../analysis/fusion.md) | `\| [yue](https://github.com/pinokiofactory/yue) \| [3261118](https://github.com/pinokiofactory/yue/commit/3261118f111c8d2bb098b82b2870458dfbc486c7) \| installed by launcher \| [torch.js:14](https://github.com/pinokiofactory/yue/blob/3261118f111c8d2bb098b82b2870458dfbc486c7/torch.js#L14) — `"uv pip install https://huggingface.co/lldacing/flash-attention-windows-wheel/resolve/main/flash_attn-2.7.4.post1%2Bcu128torch2.7.0cxx11abiFALSE-cp311` \|` |
| [models.md](../analysis/models.md) | No model pull/shape row matched in models.md. |
| [cpu.md](../analysis/cpu.md) | CPU category: **CPU possible, but launcher must change** |
| [tpu.md](../analysis/tpu.md) | TPU suitability: **Difficult - significant port** — replace CUDA attention kernels with TPU-compatible attention/SDPA/XLA; add TPU launcher/runtime branch; multiple CUDA-specific dependencies or large model/dtype constraints |

### Related analysis

- [CPU analysis](../analysis/cpu.md)
- [TPU analysis](../analysis/tpu.md)
- [Effort ranking](../analysis/effort.md)
- [Kernel evidence](../analysis/kernels.md)
- [Quantization evidence](../analysis/quantization.md)
- [Fusion evidence](../analysis/fusion.md)
- [Model pulls/shapes](../analysis/models.md)
- [Flow graphs](../analysis/flows.md)
- [App flow graph](../flows/yue.md)
<!-- cross-analysis:end -->
