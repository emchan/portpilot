# wan — portability analysis

- **Package name:** Wan2GP (`wan`)
- **Description:** 1-click WanGP Launcher. Super Optimized Gradio UI for AI video creation for GPU poor machines (6GB+ VRAM). Supports Wan 2.1/2.2, Qwen, Hunyuan Video, LTX Video and Flux. https://github.com/deepbeepmeep/Wan2GP
- **Original git URL:** https://github.com/pinokiofactory/wan
- **Analyzed commit:** `8ed14108ca7148a612c5eb9528b00ceac99810ff`
- **Platforms supported:** NVIDIA / AMD / Mac
- **Porting difficulty:** Very high
- **CUDA-only packages:** bitsandbytes, flash-attn, sageattention, triton-windows, xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

bitsandbytes, comtypes, flash-attn, hf-xet, lightx2v-kernel, llamacpp-gguf-cuda, numpy, nunchaku, sageattention, spas-sage-attn, torch, torchaudio, torchvision, triton-windows, unsafe-best-match, wgpkernels, xformers

Wheel indexes referenced: cpu, cu128, cu130, rocm7.1.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 650
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- `torch.js` routes present: nvidia, amd, mac, cpu.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): xformers
- Difficulty score: 11.0 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- retested on Python 3.12; dependencies installed but import failed due optimum/quanto/transformers API mismatch (PreTrainedModel).
- Result: **not runnable in this container.**
<!-- cross-analysis:start -->
## Cross-analysis details

- **CPU category (cpu.md):** CPU-capable with shipped fallback
- **TPU suitability:** Difficult - significant port
- **TPU work needed:** replace CUDA attention kernels with TPU-compatible attention/SDPA/XLA; NF4/bitsandbytes quantization needs dequant/upcast or TPU-supported path; multiple CUDA-specific dependencies or large model/dtype constraints
- **Effort ranking (effort.md):** #91 — Very high
- **Effort blockers:** GPU-only attention: flash-attn/sageattention/triton-windows/xformers; GPU quantisers: bitsandbytes; CUDA-only fused kernels need config change
- **Precisions noted:** unspecified
- **Models/flows noted:** —
- **Flow graph:** [flows/wan.md](../flows/wan.md)

### Snapshot verification (cloned analyzed commit)

- **Snapshot source:** `https://codeload.github.com/pinokiofactory/wan/tar.gz/<analyzed commit>` extracted to `/tmp/opencode/pinokio-snapshots/wan`
- **Files scanned:** 12 total (0 .py, 6 .js, 6 other)
- **Key files present:** pinokio.js, install.js, torch.js, start.js
- **TPU/CUDA-relevant signals:**
  - `xformers`: 18 match(es) (e.g. torch.js:12, torch.js:12)
  - `flash_attn`: 8 match(es) (e.g. torch.js:49, torch.js:49)
  - `sageattention`: 14 match(es) (e.g. torch.js:28, torch.js:30)
  - `triton`: 3 match(es) (e.g. torch.js:27, torch.js:47)
  - `bitsandbytes`: 7 match(es) (e.g. torch.js:32, torch.js:55)
  - `gguf`: 6 match(es) (e.g. torch.js:29, torch.js:52)

### Evidence from analysis files

| Source | Evidence |
|---|---|
| [kernels.md](../analysis/kernels.md) | `\| [wan](https://github.com/pinokiofactory/wan) \| [8ed1410](https://github.com/pinokiofactory/wan/commit/8ed14108ca7148a612c5eb9528b00ceac99810ff) \| launcher install \| torch.js \| [torch.js:27](https://github.com/pinokiofactory/wan/blob/8ed14108ca7148a612c5eb9528b00ceac99810ff/torch.js#L27) — 'uv pip install "triton-windows>=3.2,<3.3"', \|` |
| [kernels.md](../analysis/kernels.md) | `\| [wan](https://github.com/pinokiofactory/wan) \| [8ed1410](https://github.com/pinokiofactory/wan/commit/8ed14108ca7148a612c5eb9528b00ceac99810ff) \| launcher install \| [torch.js:49](https://github.com/pinokiofactory/wan/blob/8ed14108ca7148a612c5eb9528b00ceac99810ff/torch.js#L49) — "uv pip install https://github.com/mjun0812/flash-attention-prebuild-wheels/releases/download/v0.7.13/flash_attn-2.8.3+cu130torch2.10-cp311-cp311-win_amd64.whl",<br>[torch.js:72](https://github.com/pinokiofactory/wan/blob/8ed14108ca7148a612c5eb9528b00ceac99810ff/torch.js#L72) — "uv pip install https://github.com/mjun0812/flash-attention-prebuild-wheels/releases/download/v0.7.13/flash_attn-2.8.3+cu130torch2.10-cp311-cp311-win_amd64.whl", \|` |
| [kernels.md](../analysis/kernels.md) | `\| [wan](https://github.com/pinokiofactory/wan) \| [8ed1410](https://github.com/pinokiofactory/wan/commit/8ed14108ca7148a612c5eb9528b00ceac99810ff) \| launcher install \| [torch.js:28](https://github.com/pinokiofactory/wan/blob/8ed14108ca7148a612c5eb9528b00ceac99810ff/torch.js#L28) — "uv pip install sageattention==1.0.6",<br>[torch.js:48](https://github.com/pinokiofactory/wan/blob/8ed14108ca7148a612c5eb9528b00ceac99810ff/torch.js#L48) — "uv pip install https://github.com/woct0rdho/SageAttention/releases/download/v2.2.0-windows.post4/sageattention-2.2.0+cu130torch2.9.0andhigher.post4-cp39-abi3-win... \|` |
| [quantization.md](../analysis/quantization.md) | `\| [wan](https://github.com/pinokiofactory/wan) \| launcher install \| `torch.js:29` — "uv pip install https://github.com/deepbeepmeep/kernels/releases/download/gguf-v1.0.29/llamacpp_gguf_cuda-1.0.29%2Btorch210cu130py311-cp311-cp311-win_amd64.whl --...<br>`torch.js:52` — "uv pip install https://github.com/deepbeepmeep/kernels/releases/download/gguf-v1.0.29/llamacpp_gguf_cuda-1.0.29%2Btorch210cu130py311-cp311-cp311-win_amd64.whl --... \|` |
| [quantization.md](../analysis/quantization.md) | `\| [wan](https://github.com/pinokiofactory/wan) \| launcher install \| `torch.js:32` — "uv pip install bitsandbytes==0.49.2 --no-deps"<br>`torch.js:55` — "uv pip install bitsandbytes==0.49.2 --no-deps" \|` |
| [fusion.md](../analysis/fusion.md) | `\| [wan](https://github.com/pinokiofactory/wan) \| [8ed1410](https://github.com/pinokiofactory/wan/commit/8ed14108ca7148a612c5eb9528b00ceac99810ff) \| [start.js:19](https://github.com/pinokiofactory/wan/blob/8ed14108ca7148a612c5eb9528b00ceac99810ff/start.js#L19) \| Launcher forwards `--compile` to `wgp.py` \|` |
| [fusion.md](../analysis/fusion.md) | `\| [wan](https://github.com/pinokiofactory/wan) \| [8ed1410](https://github.com/pinokiofactory/wan/commit/8ed14108ca7148a612c5eb9528b00ceac99810ff) \| installed by launcher \| [torch.js:28](https://github.com/pinokiofactory/wan/blob/8ed14108ca7148a612c5eb9528b00ceac99810ff/torch.js#L28) — `"uv pip install sageattention==1.0.6",` \|` |
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
- [App flow graph](../flows/wan.md)
<!-- cross-analysis:end -->
