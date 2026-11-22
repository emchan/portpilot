# AudioX — portability analysis

- **Package name:** AudioX (`AudioX`)
- **Description:** AudioX Diffusion Transformer for Anything-to-Audio Generation
- **Original git URL:** https://github.com/pinokiofactory/AudioX
- **Analyzed commit:** `7a0ff7b5ca8d5eeb6054edf84196a23389545d1d`
- **Platforms supported:** NVIDIA / AMD / Mac
- **Porting difficulty:** High
- **CUDA-only packages:** flash-attn, sageattention *(optional)*, triton-windows, xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

flash-attn, hf-xet, numpy, pydantic, sageattention, torch, torch-directml, torchaudio, torchvision, triton-windows, xformers

Wheel indexes referenced: cpu, cu128, rocm6.1.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 344
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- `torch.js` routes present: nvidia, amd, mac, cpu.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): sageattention, triton, xformers
- Difficulty score: 7.0 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- retested on Python 3.10; blocked by torchvision operator mismatch (torchvision::nms).
- Result: **not runnable in this container.**
<!-- cross-analysis:start -->
## Cross-analysis details

- **CPU category (cpu.md):** CPU-capable with shipped fallback
- **TPU suitability:** Possible - moderate port
- **TPU work needed:** replace CUDA attention kernels with TPU-compatible attention/SDPA/XLA; moderate device/kernel/runtime adaptation
- **Effort ranking (effort.md):** #76 — High
- **Effort blockers:** GPU-only attention: flash-attn/sageattention/triton-windows/xformers; CUDA-only fused kernels need config change
- **Precisions noted:** unspecified
- **Models/flows noted:** [HKUSTAudio/AudioX](https://huggingface.co/HKUSTAudio/AudioX)
- **Flow graph:** [flows/AudioX.md](../flows/AudioX.md)

### Snapshot verification (cloned analyzed commit)

- **Snapshot source:** `https://codeload.github.com/pinokiofactory/AudioX/tar.gz/<analyzed commit>` extracted to `/tmp/opencode/pinokio-snapshots/AudioX`
- **Files scanned:** 10 total (0 .py, 7 .js, 3 other)
- **Key files present:** pinokio.js, install.js, torch.js, start.js
- **TPU/CUDA-relevant signals:**
  - `xformers`: 6 match(es) (e.g. torch.js:27, torch.js:27)
  - `flash_attn`: 6 match(es) (e.g. torch.js:14, torch.js:14)
  - `sageattention`: 12 match(es) (e.g. torch.js:13, torch.js:13)
  - `triton`: 5 match(es) (e.g. torch.js:12, torch.js:12)
  - `directml`: 1 match(es) (e.g. torch.js:42)

### Evidence from analysis files

| Source | Evidence |
|---|---|
| [kernels.md](../analysis/kernels.md) | `\| [AudioX](https://github.com/pinokiofactory/AudioX) \| [7a0ff7b](https://github.com/pinokiofactory/AudioX/commit/7a0ff7b5ca8d5eeb6054edf84196a23389545d1d) \| optional flag + launcher install \| install.js, torch.js \| [torch.js:12](https://github.com/pinokiofactory/AudioX/blob/7a0ff7b5ca8d5eeb6054edf84196a23389545d1d/torch.js#L12) — "{{args && args.triton ? 'uv pip install -U --pre triton-windows' : ''}}", \|` |
| [kernels.md](../analysis/kernels.md) | `\| [AudioX](https://github.com/pinokiofactory/AudioX) \| [7a0ff7b](https://github.com/pinokiofactory/AudioX/commit/7a0ff7b5ca8d5eeb6054edf84196a23389545d1d) \| optional flag + launcher install \| [torch.js:14](https://github.com/pinokiofactory/AudioX/blob/7a0ff7b5ca8d5eeb6054edf84196a23389545d1d/torch.js#L14) — "{{args && args.flashattention ? 'uv pip install https://huggingface.co/lldacing/flash-attention-windows-wheel/resolve/main/flash_attn-2.7.4.post1%2Bcu128torch2.8...<br>[torch.js:30](https://github.com/pinokiofactory/AudioX/blob/7a0ff7b5ca8d5eeb6054edf84196a23389545d1d/torch.js#L30) — "{{args && args.flashattention ? 'uv pip install https://huggingface.co/lldacing/flash-attention-windows-wheel/resolve/main/flash_attn-2.7.4.post1%2Bcu128torch2.7... \|` |
| [kernels.md](../analysis/kernels.md) | `\| [AudioX](https://github.com/pinokiofactory/AudioX) \| [7a0ff7b](https://github.com/pinokiofactory/AudioX/commit/7a0ff7b5ca8d5eeb6054edf84196a23389545d1d) \| optional flag + launcher install \| [torch.js:13](https://github.com/pinokiofactory/AudioX/blob/7a0ff7b5ca8d5eeb6054edf84196a23389545d1d/torch.js#L13) — "{{args && args.sageattention ? 'uv pip install https://github.com/woct0rdho/SageAttention/releases/download/v2.1.1-windows/sageattention-2.1.1+cu128torch2.7.0-cp...<br>[torch.js:29](https://github.com/pinokiofactory/AudioX/blob/7a0ff7b5ca8d5eeb6054edf84196a23389545d1d/torch.js#L29) — "{{args && args.sageattention ? 'uv pip install https://github.com/deepbeepmeep/SageAttention/raw/refs/heads/main/releases/sageattention-2.1.0-cp310-cp310-win_amd... \|` |
| [quantization.md](../analysis/quantization.md) | No per-repo quantization table row matched; see quantization.md. |
| [fusion.md](../analysis/fusion.md) | `\| [AudioX](https://github.com/pinokiofactory/AudioX) \| [7a0ff7b](https://github.com/pinokiofactory/AudioX/commit/7a0ff7b5ca8d5eeb6054edf84196a23389545d1d) \| optional launcher flag \| [torch.js:13](https://github.com/pinokiofactory/AudioX/blob/7a0ff7b5ca8d5eeb6054edf84196a23389545d1d/torch.js#L13) — `"{{args && args.sageattention ? 'uv pip install https://github.com/woct0rdho/SageAttention/releases/download/v2.1.1-windows/sageattention-2.1.1+cu128t` \|` |
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
- [App flow graph](../flows/AudioX.md)
<!-- cross-analysis:end -->

## Snapdragon evaluation (deep clone)
- **Clone/scan status:** cloned and scanned
- **Files scanned:** 10 total (0 .py, 7 .js/.ts, 3 other)
- **Snapdragon-relevant signals:** torch=15, triton=3, xformers=3, flashattention=4, sageattention=5, directml=1
- **Example evidence:**
  - torch: `install.js:12`
  - triton: `install.js:21`
  - xformers: `install.js:20`
  - flashattention: `install.js:23`
  - sageattention: `install.js:22`
  - directml: `torch.js:42`
- **Snapdragon verdict:** Contains CUDA/Triton/TensorRT signals; Snapdragon path requires replacement or ONNX conversion.
