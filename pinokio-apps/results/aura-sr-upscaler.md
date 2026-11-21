# aura-sr-upscaler — portability analysis

- **Package name:** aura-sr-upscaler (`aura-sr-upscaler`)
- **Description:** AuraSR-v2 - An open reproduction of the GigaGAN Upscaler from fal.ai https://huggingface.co/spaces/gokaygokay/AuraSR-v2
- **Original git URL:** https://github.com/pinokiofactory/aura-sr-upscaler
- **Analyzed commit:** `9357cf93dac1f28179bb5d32c98b1c5c75a61ece`
- **Platforms supported:** NVIDIA / AMD / Mac
- **Porting difficulty:** High
- **CUDA-only packages:** flash-attn, sageattention *(optional)*, triton *(optional)*, triton-windows, xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

devicetorch, flash-attn, gradio, hf-xet, numpy, sageattention, torch, torch-directml, torchaudio, torchvision, triton, triton-windows, xformers

Wheel indexes referenced: cpu, cu128, rocm6.3.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 289
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- `torch.js` routes present: nvidia, amd, mac, cpu.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): sageattention, triton, xformers
- Difficulty score: 7.8 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- retested on Python 3.12; blocked by torchvision operator mismatch (torchvision::nms).
- Result: **not runnable in this container.**
<!-- cross-analysis:start -->
## Cross-analysis details

- **CPU category (cpu.md):** CPU-capable with shipped fallback
- **TPU suitability:** Possible - moderate port
- **TPU work needed:** replace CUDA attention kernels with TPU-compatible attention/SDPA/XLA; moderate device/kernel/runtime adaptation
- **Effort ranking (effort.md):** #78 — High
- **Effort blockers:** GPU-only attention: flash-attn/sageattention/triton/triton-windows/xformers; CUDA-only fused kernels need config change
- **Precisions noted:** unspecified
- **Models/flows noted:** —
- **Flow graph:** [flows/aura-sr-upscaler.md](../flows/aura-sr-upscaler.md)

### Snapshot verification (cloned analyzed commit)

- **Snapshot source:** `https://codeload.github.com/pinokiofactory/aura-sr-upscaler/tar.gz/<analyzed commit>` extracted to `/tmp/opencode/pinokio-snapshots/aura-sr-upscaler`
- **Files scanned:** 11 total (0 .py, 7 .js, 4 other)
- **Key files present:** pinokio.js, install.js, torch.js, start.js
- **TPU/CUDA-relevant signals:**
  - `xformers`: 5 match(es) (e.g. torch.js:11, torch.js:11)
  - `flash_attn`: 2 match(es) (e.g. torch.js:14, torch.js:31)
  - `sageattention`: 4 match(es) (e.g. torch.js:13, torch.js:13)
  - `triton`: 4 match(es) (e.g. torch.js:12, torch.js:12)
  - `directml`: 1 match(es) (e.g. torch.js:45)

### Evidence from analysis files

| Source | Evidence |
|---|---|
| [kernels.md](../analysis/kernels.md) | `\| [aura-sr-upscaler](https://github.com/pinokiofactory/aura-sr-upscaler) \| [9357cf9](https://github.com/pinokiofactory/aura-sr-upscaler/commit/9357cf93dac1f28179bb5d32c98b1c5c75a61ece) \| optional flag + launcher install \| torch.js \| [torch.js:12](https://github.com/pinokiofactory/aura-sr-upscaler/blob/9357cf93dac1f28179bb5d32c98b1c5c75a61ece/torch.js#L12) — "{{args && args.triton ? 'uv pip install triton-windows==3.3.1.post19' : ''}}", \|` |
| [kernels.md](../analysis/kernels.md) | `\| [aura-sr-upscaler](https://github.com/pinokiofactory/aura-sr-upscaler) \| [9357cf9](https://github.com/pinokiofactory/aura-sr-upscaler/commit/9357cf93dac1f28179bb5d32c98b1c5c75a61ece) \| optional flag + launcher install \| [torch.js:14](https://github.com/pinokiofactory/aura-sr-upscaler/blob/9357cf93dac1f28179bb5d32c98b1c5c75a61ece/torch.js#L14) — "{{args && args.flashattention ? 'uv pip install https://huggingface.co/cocktailpeanut/wheels/resolve/main/flash_attn-2.8.2%2Bcu128torch2.7-cp310-cp310-win_amd64....<br>[torch.js:31](https://github.com/pinokiofactory/aura-sr-upscaler/blob/9357cf93dac1f28179bb5d32c98b1c5c75a61ece/torch.js#L31) — "{{args && args.flashattention ? 'uv pip install https://huggingface.co/cocktailpeanut/wheels/resolve/main/flash_attn-2.8.3%2Bcu128torch2.7-cp310-cp310-linux_x86_... \|` |
| [kernels.md](../analysis/kernels.md) | `\| [aura-sr-upscaler](https://github.com/pinokiofactory/aura-sr-upscaler) \| [9357cf9](https://github.com/pinokiofactory/aura-sr-upscaler/commit/9357cf93dac1f28179bb5d32c98b1c5c75a61ece) \| optional flag + launcher install \| [torch.js:13](https://github.com/pinokiofactory/aura-sr-upscaler/blob/9357cf93dac1f28179bb5d32c98b1c5c75a61ece/torch.js#L13) — "{{args && args.sageattention ? 'uv pip install https://huggingface.co/cocktailpeanut/wheels/resolve/main/sageattention-2.1.1%2Bcu128torch2.7.1-cp310-cp310-win_am...<br>[torch.js:30](https://github.com/pinokiofactory/aura-sr-upscaler/blob/9357cf93dac1f28179bb5d32c98b1c5c75a61ece/torch.js#L30) — "{{args && args.sageattention ? 'uv pip install https://huggingface.co/cocktailpeanut/wheels/resolve/main/sageattention-2.1.1%2Bcu128torch2.7.1-cp310-cp310-linux_... \|` |
| [quantization.md](../analysis/quantization.md) | No per-repo quantization table row matched; see quantization.md. |
| [fusion.md](../analysis/fusion.md) | `\| [aura-sr-upscaler](https://github.com/pinokiofactory/aura-sr-upscaler) \| [9357cf9](https://github.com/pinokiofactory/aura-sr-upscaler/commit/9357cf93dac1f28179bb5d32c98b1c5c75a61ece) \| optional launcher flag \| [torch.js:13](https://github.com/pinokiofactory/aura-sr-upscaler/blob/9357cf93dac1f28179bb5d32c98b1c5c75a61ece/torch.js#L13) — `"{{args && args.sageattention ? 'uv pip install https://huggingface.co/cocktailpeanut/wheels/resolve/main/sageattention-2.1.1%2Bcu128torch2.7.1-cp310-` \|` |
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
- [App flow graph](../flows/aura-sr-upscaler.md)
<!-- cross-analysis:end -->
