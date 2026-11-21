# diffusers-image-fill — portability analysis

- **Package name:** diffusers-image-fill (`diffusers-image-fill`)
- **Description:** Remove objects from an image https://huggingface.co/spaces/OzzyGT/diffusers-image-fill
- **Original git URL:** https://github.com/pinokiofactory/diffusers-image-fill
- **Analyzed commit:** `a8b6497483d956df7ca1ffc882bf29af03476a26`
- **Platforms supported:** NVIDIA / AMD / Mac
- **Porting difficulty:** Low
- **CUDA-only packages:** xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

accelerate, devicetorch, diffusers, fastapi, gradio, gradio-imageslider, huggingface-hub, numpy, opencv-python, pillow, pydantic, spaces, torch, torch-directml, torchaudio, torchvision, transformers, xformers

Requirements files: `requirements.txt`.

Third-party Python imports detected in local source: cv2, devicetorch, diffusers, gradio, gradio-imageslider, huggingface-hub, pil, torch, transformers.

Wheel indexes referenced: cpu, cu128, rocm6.3.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 2073
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- `torch.js` routes present: nvidia, amd, mac, cpu.
- Requirements from: requirements.txt
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): xformers
- Difficulty score: 0.5 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- Retested on Python 3.12 with corrected dependencies; importing app.py still hung in this container.
- Result: **not runnable in this container.**
<!-- cross-analysis:start -->
## Cross-analysis details

- **CPU category (cpu.md):** CPU-capable with shipped fallback
- **TPU suitability:** Possible - moderate port
- **TPU work needed:** replace CUDA attention kernels with TPU-compatible attention/SDPA/XLA; moderate device/kernel/runtime adaptation
- **Effort ranking (effort.md):** #26 — Low
- **Effort blockers:** GPU-only attention: xformers
- **Precisions noted:** FP32, FP16, INT32, INT64, FP64
- **Models/flows noted:** —
- **Flow graph:** [flows/diffusers-image-fill.md](../flows/diffusers-image-fill.md)

### Snapshot verification (cloned analyzed commit)

- **Snapshot source:** `https://codeload.github.com/pinokiofactory/diffusers-image-fill/tar.gz/<analyzed commit>` extracted to `/tmp/opencode/pinokio-snapshots/diffusers-image-fill`
- **Files scanned:** 14 total (3 .py, 7 .js, 4 other)
- **Key files present:** pinokio.js, install.js, torch.js, start.js, requirements.txt
- **TPU/CUDA-relevant signals:**
  - `xformers`: 5 match(es) (e.g. torch.js:10, torch.js:10)
  - `directml`: 1 match(es) (e.g. torch.js:22)
  - `mps`: 3 match(es) (e.g. pipeline_fill_sd_xl.py:236, pipeline_fill_sd_xl.py:241)

### Evidence from analysis files

| Source | Evidence |
|---|---|
| [kernels.md](../analysis/kernels.md) | `\| [diffusers-image-fill](https://github.com/pinokiofactory/diffusers-image-fill) \| [a8b6497](https://github.com/pinokiofactory/diffusers-image-fill/commit/a8b6497483d956df7ca1ffc882bf29af03476a26) \| direct code \| [controlnet_union.py:899](https://github.com/pinokiofactory/diffusers-image-fill/blob/a8b6497483d956df7ca1ffc882bf29af03476a26/controlnet_union.py#L899) — is_mps = sample.device.type == "mps"<br>[pipeline_fill_sd_xl.py:236](https://github.com/pinokiofactory/diffusers-image-fill/blob/a8b6497483d956df7ca1ffc882bf29af03476a26/pipeline_fill_sd_xl.py#L236) — # duplicate text embeddings for each generation per prompt, using mps friendly method \|` |
| [quantization.md](../analysis/quantization.md) | `\| [diffusers-image-fill](https://github.com/pinokiofactory/diffusers-image-fill) \| [a8b6497](https://github.com/pinokiofactory/diffusers-image-fill/commit/a8b6497483d956df7ca1ffc882bf29af03476a26) \| [40](https://github.com/pinokiofactory/diffusers-image-fill/blob/a8b6497483d956df7ca1ffc882bf29af03476a26/app.py#L40) \| float16 / FP16 \| dtype declaration \| model.to(device=DEVICE, dtype=torch.float16) \|` |
| [quantization.md](../analysis/quantization.md) | `\| [diffusers-image-fill](https://github.com/pinokiofactory/diffusers-image-fill) \| [a8b6497](https://github.com/pinokiofactory/diffusers-image-fill/commit/a8b6497483d956df7ca1ffc882bf29af03476a26) \| [43](https://github.com/pinokiofactory/diffusers-image-fill/blob/a8b6497483d956df7ca1ffc882bf29af03476a26/app.py#L43) \| float16 / FP16 \| dtype declaration \| "madebyollin/sdxl-vae-fp16-fix", torch_dtype=torch.float16 \|` |
| [quantization.md](../analysis/quantization.md) | `\| [diffusers-image-fill](https://github.com/pinokiofactory/diffusers-image-fill) \| [a8b6497](https://github.com/pinokiofactory/diffusers-image-fill/commit/a8b6497483d956df7ca1ffc882bf29af03476a26) \| [48](https://github.com/pinokiofactory/diffusers-image-fill/blob/a8b6497483d956df7ca1ffc882bf29af03476a26/app.py#L48) \| float16 / FP16 \| dtype declaration \| torch_dtype=torch.float16, \|` |
| [quantization.md](../analysis/quantization.md) | `\| [diffusers-image-fill](https://github.com/pinokiofactory/diffusers-image-fill) \| [a8b6497](https://github.com/pinokiofactory/diffusers-image-fill/commit/a8b6497483d956df7ca1ffc882bf29af03476a26) \| [51](https://github.com/pinokiofactory/diffusers-image-fill/blob/a8b6497483d956df7ca1ffc882bf29af03476a26/app.py#L51) \| float16 / FP16 \| dtype declaration \| variant="fp16", \|` |
| [quantization.md](../analysis/quantization.md) | `\| [diffusers-image-fill](https://github.com/pinokiofactory/diffusers-image-fill) \| [a8b6497](https://github.com/pinokiofactory/diffusers-image-fill/commit/a8b6497483d956df7ca1ffc882bf29af03476a26) \| [59](https://github.com/pinokiofactory/diffusers-image-fill/blob/a8b6497483d956df7ca1ffc882bf29af03476a26/controlnet_union.py#L59) \| float16 / FP16 \| dtype declaration \| """Subclass torch's LayerNorm to handle fp16.""" \|` |
| [quantization.md](../analysis/quantization.md) | `\| [diffusers-image-fill](https://github.com/pinokiofactory/diffusers-image-fill) \| [a8b6497](https://github.com/pinokiofactory/diffusers-image-fill/commit/a8b6497483d956df7ca1ffc882bf29af03476a26) \| [901](https://github.com/pinokiofactory/diffusers-image-fill/blob/a8b6497483d956df7ca1ffc882bf29af03476a26/controlnet_union.py#L901) \| float / FP32, float64 \| dtype declaration \| dtype = torch.float32 if is_mps else torch.float64 \|` |
| [quantization.md](../analysis/quantization.md) | `\| [diffusers-image-fill](https://github.com/pinokiofactory/diffusers-image-fill) \| [a8b6497](https://github.com/pinokiofactory/diffusers-image-fill/commit/a8b6497483d956df7ca1ffc882bf29af03476a26) \| [903](https://github.com/pinokiofactory/diffusers-image-fill/blob/a8b6497483d956df7ca1ffc882bf29af03476a26/controlnet_union.py#L903) \| int32, int64 \| dtype declaration \| dtype = torch.int32 if is_mps else torch.int64 \|` |
| [quantization.md](../analysis/quantization.md) | `\| [diffusers-image-fill](https://github.com/pinokiofactory/diffusers-image-fill) \| [a8b6497](https://github.com/pinokiofactory/diffusers-image-fill/commit/a8b6497483d956df7ca1ffc882bf29af03476a26) \| [914](https://github.com/pinokiofactory/diffusers-image-fill/blob/a8b6497483d956df7ca1ffc882bf29af03476a26/controlnet_union.py#L914) \| float16 / FP16 \| dtype declaration \| # but time_embedding might actually be running in fp16. so we need to cast here. \|` |
| [quantization.md](../analysis/quantization.md) | *1 more rows omitted* |
| [fusion.md](../analysis/fusion.md) | `\| Fused activation (`GELU(approximate='tanh')`, SiLU) \| 3 \| Allegro-txt2vid, Nari-Dia-TTS, diffusers-image-fill \|` |
| [fusion.md](../analysis/fusion.md) | `\| [diffusers-image-fill](https://github.com/pinokiofactory/diffusers-image-fill) \| [a8b6497](https://github.com/pinokiofactory/diffusers-image-fill/commit/a8b6497483d956df7ca1ffc882bf29af03476a26) \| [pipeline_fill_sd_xl.py:308](https://github.com/pinokiofactory/diffusers-image-fill/blob/a8b6497483d956df7ca1ffc882bf29af03476a26/pipeline_fill_sd_xl.py#L308) \| `hasattr(F, 'scaled_dot_product_attention')` compiled-module check (line 309 references `OptimizedModule`) \|` |
| [fusion.md](../analysis/fusion.md) | `\| [diffusers-image-fill](https://github.com/pinokiofactory/diffusers-image-fill) \| [a8b6497](https://github.com/pinokiofactory/diffusers-image-fill/commit/a8b6497483d956df7ca1ffc882bf29af03476a26) \| direct code \| [pipeline_fill_sd_xl.py:308](https://github.com/pinokiofactory/diffusers-image-fill/blob/a8b6497483d956df7ca1ffc882bf29af03476a26/pipeline_fill_sd_xl.py#L308) — `is_compiled = hasattr(F, "scaled_dot_product_attention") and isinstance(` \|` |
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
- [App flow graph](../flows/diffusers-image-fill.md)
<!-- cross-analysis:end -->
