# clarity-refiners-ui — portability analysis

- **Package name:** Clarity Refiners UI (`clarity-refiners-ui`)
- **Description:** An enhanced local port of finegrain-image-enhancer powered by Refiners (https://huggingface.co/spaces/finegrain/finegrain-image-enhancer), which was adapted from philz1337x's Clarity Upscaler (https://github.com/philz1337x/clarity-upscaler)
- **Original git URL:** https://github.com/pinokiofactory/clarity-refiners-ui
- **Analyzed commit:** `a632fb6b948fa6b1a55d816982655d6dc8ed995e`
- **Platforms supported:** NVIDIA / AMD / Mac
- **Porting difficulty:** Low
- **CUDA-only packages:** xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

accelerate, devicetorch, einops, ftfy, gradio, gradio-imageslider, numpy, pillow, pillow-heif, pydantic, regex, timm, torch, torch-directml, torchaudio, torchvision, tqdm, transformers, xformers

Requirements files: `app/requirements.txt`.

Third-party Python imports detected in local source: devicetorch, gradio, gradio-imageslider, huggingface-hub, numpy, pil, pillow-heif, psutil, refiners, torch, transformers.

Wheel indexes referenced: cpu, cu128, rocm6.3.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 1871
- **CUDA-related functions used:** `torch.cuda.get_device_name`, `torch.cuda.get_device_properties`, `torch.cuda.is_available`, `torch.cuda.memory_allocated`

## Evidence and notes

- `torch.js` routes present: nvidia, amd, mac, cpu.
- Requirements from: app/requirements.txt
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): xformers
- Difficulty score: 0.5 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- retested on Python 3.12; blocked by torchvision operator mismatch.
- Result: **not runnable in this container.**
<!-- cross-analysis:start -->
## Cross-analysis details

- **CPU category (cpu.md):** CPU-capable with shipped fallback
- **TPU suitability:** Difficult - significant port
- **TPU work needed:** replace CUDA attention kernels with TPU-compatible attention/SDPA/XLA; remove direct torch.cuda device assumptions; large BF16/FP16 GEMM workload; expect XLA compile/memory tuning; multiple CUDA-specific dependencies or large model/dtype constraints
- **Effort ranking (effort.md):** #44 — Low–medium
- **Effort blockers:** GPU-only attention: xformers; direct `torch.cuda` calls; CUDA-only fused kernels need config change; large FP16/BF16 GEMM load
- **Precisions noted:** FP32, FP16, BF16, UINT8
- **Models/flows noted:** [multimodalart/Florence-2-large-no-flash-attn](https://huggingface.co/multimodalart/Florence-2-large-no-flash-attn), [philz1337x/embeddings](https://huggingface.co/philz1337x/embeddings), [philz1337x/loras](https://huggingface.co/philz1337x/loras), [philz1337x/upscaler](https://huggingface.co/philz1337x/upscaler), [refiners/controlnet.sd1_5.tile](https://huggingface.co/refiners/controlnet.sd1_5.tile), [refiners/juggernaut.reborn.sd1_5.autoencoder](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.autoencoder), [refiners/juggernaut.reborn.sd1_5.text_encoder](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.text_encoder), [refiners/juggernaut.reborn.sd1_5.unet](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.unet)
- **Flow graph:** [flows/clarity-refiners-ui.md](../flows/clarity-refiners-ui.md)

### Snapshot verification (cloned analyzed commit)

- **Snapshot source:** `https://codeload.github.com/pinokiofactory/clarity-refiners-ui/tar.gz/<analyzed commit>` extracted to `/tmp/opencode/pinokio-snapshots/clarity-refiners-ui`
- **Files scanned:** 20 total (5 .py, 8 .js, 7 other)
- **Key files present:** pinokio.js, install.js, torch.js, start.js
- **TPU/CUDA-relevant signals:**
  - `torch_cuda`: 4 match(es) (e.g. app/system_monitor.py:16, app/system_monitor.py:36)
  - `xformers`: 4 match(es) (e.g. torch.js:10, torch.js:10)
  - `flash_attn`: 3 match(es) (e.g. README.md:42, app/app.py:134)
  - `directml`: 1 match(es) (e.g. torch.js:34)

### Evidence from analysis files

| Source | Evidence |
|---|---|
| [kernels.md](../analysis/kernels.md) | `\| [clarity-refiners-ui](https://github.com/pinokiofactory/clarity-refiners-ui) \| [a632fb6](https://github.com/pinokiofactory/clarity-refiners-ui/commit/a632fb6b948fa6b1a55d816982655d6dc8ed995e) \| reference \| [README.md:42](https://github.com/pinokiofactory/clarity-refiners-ui/blob/a632fb6b948fa6b1a55d816982655d6dc8ed995e/README.md#L42) — - https://huggingface.co/multimodalart/Florence-2-large-no-flash-attn<br>[app/app.py:134](https://github.com/pinokiofactory/clarity-refiners-ui/blob/a632fb6b948fa6b1a55d816982655d6dc8ed995e/app/app.py#L134) — "multimodalart/Florence-2-large-no-flash-attn", \|` |
| [quantization.md](../analysis/quantization.md) | `\| [clarity-refiners-ui](https://github.com/pinokiofactory/clarity-refiners-ui) \| [a632fb6](https://github.com/pinokiofactory/clarity-refiners-ui/commit/a632fb6b948fa6b1a55d816982655d6dc8ed995e) \| [82](https://github.com/pinokiofactory/clarity-refiners-ui/blob/a632fb6b948fa6b1a55d816982655d6dc8ed995e/app/system_monitor.py#L82) \| float / FP32 \| dtype declaration \| metrics['memory_used'] = float(parts[used_idx]) / 1024 \|` |
| [quantization.md](../analysis/quantization.md) | `\| [clarity-refiners-ui](https://github.com/pinokiofactory/clarity-refiners-ui) \| [a632fb6](https://github.com/pinokiofactory/clarity-refiners-ui/commit/a632fb6b948fa6b1a55d816982655d6dc8ed995e) \| [83](https://github.com/pinokiofactory/clarity-refiners-ui/blob/a632fb6b948fa6b1a55d816982655d6dc8ed995e/app/system_monitor.py#L83) \| float / FP32 \| dtype declaration \| metrics['memory_total'] = float(parts[total_idx]) / 1024 \|` |
| [quantization.md](../analysis/quantization.md) | `\| [clarity-refiners-ui](https://github.com/pinokiofactory/clarity-refiners-ui) \| [a632fb6](https://github.com/pinokiofactory/clarity-refiners-ui/commit/a632fb6b948fa6b1a55d816982655d6dc8ed995e) \| [85](https://github.com/pinokiofactory/clarity-refiners-ui/blob/a632fb6b948fa6b1a55d816982655d6dc8ed995e/app/system_monitor.py#L85) \| float / FP32 \| dtype declaration \| temp = float(line.split(':')[1].strip().replace('c', '')) \|` |
| [quantization.md](../analysis/quantization.md) | `\| [clarity-refiners-ui](https://github.com/pinokiofactory/clarity-refiners-ui) \| [a632fb6](https://github.com/pinokiofactory/clarity-refiners-ui/commit/a632fb6b948fa6b1a55d816982655d6dc8ed995e) \| [88](https://github.com/pinokiofactory/clarity-refiners-ui/blob/a632fb6b948fa6b1a55d816982655d6dc8ed995e/app/system_monitor.py#L88) \| float / FP32 \| dtype declaration \| util = float(line.split(':')[1].strip().replace('%', '')) \|` |
| [quantization.md](../analysis/quantization.md) | `\| [clarity-refiners-ui](https://github.com/pinokiofactory/clarity-refiners-ui) \| [a632fb6](https://github.com/pinokiofactory/clarity-refiners-ui/commit/a632fb6b948fa6b1a55d816982655d6dc8ed995e) \| [97](https://github.com/pinokiofactory/clarity-refiners-ui/blob/a632fb6b948fa6b1a55d816982655d6dc8ed995e/app/system_monitor.py#L97) \| float / FP32 \| dtype declaration \| metrics['temperature'] = float(f.read().strip()) / 1000 \|` |
| [quantization.md](../analysis/quantization.md) | `\| [clarity-refiners-ui](https://github.com/pinokiofactory/clarity-refiners-ui) \| [a632fb6](https://github.com/pinokiofactory/clarity-refiners-ui/commit/a632fb6b948fa6b1a55d816982655d6dc8ed995e) \| [100](https://github.com/pinokiofactory/clarity-refiners-ui/blob/a632fb6b948fa6b1a55d816982655d6dc8ed995e/app/system_monitor.py#L100) \| float / FP32 \| dtype declaration \| metrics['memory_total'] = float(f.read().strip()) / 1024**3 \|` |
| [quantization.md](../analysis/quantization.md) | `\| [clarity-refiners-ui](https://github.com/pinokiofactory/clarity-refiners-ui) \| [a632fb6](https://github.com/pinokiofactory/clarity-refiners-ui/commit/a632fb6b948fa6b1a55d816982655d6dc8ed995e) \| [102](https://github.com/pinokiofactory/clarity-refiners-ui/blob/a632fb6b948fa6b1a55d816982655d6dc8ed995e/app/system_monitor.py#L102) \| float / FP32 \| dtype declaration \| metrics['memory_used'] = float(f.read().strip()) / 1024**3 \|` |
| [quantization.md](../analysis/quantization.md) | `\| [clarity-refiners-ui](https://github.com/pinokiofactory/clarity-refiners-ui) \| [a632fb6](https://github.com/pinokiofactory/clarity-refiners-ui/commit/a632fb6b948fa6b1a55d816982655d6dc8ed995e) \| [105](https://github.com/pinokiofactory/clarity-refiners-ui/blob/a632fb6b948fa6b1a55d816982655d6dc8ed995e/app/system_monitor.py#L105) \| float / FP32 \| dtype declaration \| metrics['utilization'] = float(f.read().strip()) \|` |
| [quantization.md](../analysis/quantization.md) | *10 more rows omitted* |
| [fusion.md](../analysis/fusion.md) | `\| [clarity-refiners-ui](https://github.com/pinokiofactory/clarity-refiners-ui) \| [a632fb6](https://github.com/pinokiofactory/clarity-refiners-ui/commit/a632fb6b948fa6b1a55d816982655d6dc8ed995e) \| documentation \| [README.md:42](https://github.com/pinokiofactory/clarity-refiners-ui/blob/a632fb6b948fa6b1a55d816982655d6dc8ed995e/README.md#L42) — `- https://huggingface.co/multimodalart/Florence-2-large-no-flash-attn` \|` |
| [fusion.md](../analysis/fusion.md) | `\| [clarity-refiners-ui](https://github.com/pinokiofactory/clarity-refiners-ui) \| [a632fb6](https://github.com/pinokiofactory/clarity-refiners-ui/commit/a632fb6b948fa6b1a55d816982655d6dc8ed995e) \| 1,440 \| [`clarity-refiners-ui.md`](../flows/clarity-refiners-ui.md) \|` |
| [fusion.md](../analysis/fusion.md) | `\| [clarity-refiners-ui](https://github.com/pinokiofactory/clarity-refiners-ui) \| [a632fb6](https://github.com/pinokiofactory/clarity-refiners-ui/commit/a632fb6b948fa6b1a55d816982655d6dc8ed995e) \| 223 \| 0 \|` |
| [models.md](../analysis/models.md) | No model pull/shape row matched in models.md. |
| [cpu.md](../analysis/cpu.md) | CPU category: **CPU-capable with shipped fallback** |
| [tpu.md](../analysis/tpu.md) | TPU suitability: **Difficult - significant port** — replace CUDA attention kernels with TPU-compatible attention/SDPA/XLA; remove direct torch.cuda device assumptions; large BF16/FP16 GEMM workload; expect XLA compile/memory tuning; multiple CUDA-specific dependencies or large model/dtype constraints |

### Related analysis

- [CPU analysis](../analysis/cpu.md)
- [TPU analysis](../analysis/tpu.md)
- [Effort ranking](../analysis/effort.md)
- [Kernel evidence](../analysis/kernels.md)
- [Quantization evidence](../analysis/quantization.md)
- [Fusion evidence](../analysis/fusion.md)
- [Model pulls/shapes](../analysis/models.md)
- [Flow graphs](../analysis/flows.md)
- [App flow graph](../flows/clarity-refiners-ui.md)
<!-- cross-analysis:end -->
