# Allegro-txt2vid — portability analysis

- **Package name:** Allegro-txt2vid (`Allegro-txt2vid`)
- **Description:** Allegro is a powerful text-to-video model that generates high-quality videos up to 6 seconds at 15 FPS and 720p resolution from simple text input.
- **Original git URL:** https://github.com/pinokiofactory/Allegro-txt2vid
- **Analyzed commit:** `f8327e3172834ee8d932d7284641a5e9a0065cbc`
- **Platforms supported:** NVIDIA only
- **Porting difficulty:** Medium
- **CUDA-only packages:** xformers

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

accelerate, bs4, decord, einops, ftfy, imageio, imageio-ffmpeg, numpy, psutil, pytorch-msssim, sentencepiece, tqdm, transformers

Requirements files: `requirements.txt`.

Third-party Python imports detected in local source: allegro, bs4, decord, devicetorch, diffusers, einops, ftfy, gradio, huggingface-hub, imageio, numpy, psutil, rife, torch, torchvision, tqdm, transformers, xformers.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 6266
- **CUDA-related functions used:** `torch.cuda.get_device_name`, `torch.cuda.is_available`

## Evidence and notes

- `torch.js` routes present: none.
- Requirements from: requirements.txt
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Difficulty score: 4.0 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- retested on Python 3.10; blocked by gradio/transformers version mismatch (FLAX_WEIGHTS_NAME).
- Result: **not runnable in this container.**
<!-- cross-analysis:start -->
## Cross-analysis details

- **CPU category (cpu.md):** Hard-blocked on CUDA
- **TPU suitability:** Hard - major rewrite/replacement required
- **TPU work needed:** CUDA/TensorRT/compiled CUDA extension dependency
- **Effort ranking (effort.md):** #89 — Very high
- **Effort blockers:** hard CUDA/TensorRT blocker in code; GPU-only attention: xformers; direct `torch.cuda` calls; CUDA-only fused kernels need config change
- **Precisions noted:** FP32, FP16, BF16, UINT8, INT32, INT64, FP64
- **Models/flows noted:** [AlexWortega/RIFE](https://huggingface.co/AlexWortega/RIFE), [PixArt-alpha/PixArt-alpha](https://huggingface.co/PixArt-alpha/PixArt-alpha), [rhymes-ai/Allegro](https://huggingface.co/rhymes-ai/Allegro), [stabilityai/sd-vae-ft-mse-original](https://huggingface.co/stabilityai/sd-vae-ft-mse-original)
- **Flow graph:** [flows/Allegro-txt2vid.md](../flows/Allegro-txt2vid.md)

### Snapshot verification (cloned analyzed commit)

- **Snapshot source:** `https://codeload.github.com/pinokiofactory/Allegro-txt2vid/tar.gz/<analyzed commit>` extracted to `/tmp/opencode/pinokio-snapshots/Allegro-txt2vid`
- **Files scanned:** 23 total (15 .py, 0 .js, 8 other)
- **Key files present:** requirements.txt
- **TPU/CUDA-relevant signals:**
  - `torch_cuda`: 13 match(es) (e.g. gradio_app.py:567, single_inference.py:16)
  - `xformers`: 23 match(es) (e.g. requirements.txt:7, allegro/models/transformers/block.py:47)
  - `flash_attn`: 1 match(es) (e.g. allegro/models/transformers/block.py:822)
  - `mps`: 5 match(es) (e.g. allegro/pipelines/pipeline_allegro.py:257, allegro/pipelines/pipeline_allegro.py:287)

### Evidence from analysis files

| Source | Evidence |
|---|---|
| [kernels.md](../analysis/kernels.md) | `\| [Allegro-txt2vid](https://github.com/pinokiofactory/Allegro-txt2vid) \| [f8327e3](https://github.com/pinokiofactory/Allegro-txt2vid/commit/f8327e3172834ee8d932d7284641a5e9a0065cbc) \| direct code \| [allegro/pipelines/pipeline_allegro.py:257](https://github.com/pinokiofactory/Allegro-txt2vid/blob/f8327e3172834ee8d932d7284641a5e9a0065cbc/allegro/pipelines/pipeline_allegro.py#L257) — # duplicate text embeddings and attention mask for each generation per prompt, using mps friendly method<br>[allegro/pipelines/pipeline_allegro.py:287](https://github.com/pinokiofactory/Allegro-txt2vid/blob/f8327e3172834ee8d932d7284641a5e9a0065cbc/allegro/pipelines/pipeline_allegro.py#L287) — # duplicate unconditional embeddings for each generation per prompt, using mps friendly method \|` |
| [quantization.md](../analysis/quantization.md) | `\| [Allegro-txt2vid](https://github.com/pinokiofactory/Allegro-txt2vid) \| [f8327e3](https://github.com/pinokiofactory/Allegro-txt2vid/commit/f8327e3172834ee8d932d7284641a5e9a0065cbc) \| [172](https://github.com/pinokiofactory/Allegro-txt2vid/blob/f8327e3172834ee8d932d7284641a5e9a0065cbc/gradio_app.py#L172) \| float16 / FP16 \| dtype declaration \| dtype = torch.float16 \|` |
| [quantization.md](../analysis/quantization.md) | `\| [Allegro-txt2vid](https://github.com/pinokiofactory/Allegro-txt2vid) \| [f8327e3](https://github.com/pinokiofactory/Allegro-txt2vid/commit/f8327e3172834ee8d932d7284641a5e9a0065cbc) \| [203](https://github.com/pinokiofactory/Allegro-txt2vid/blob/f8327e3172834ee8d932d7284641a5e9a0065cbc/gradio_app.py#L203) \| float / FP32 \| dtype declaration \| torch_dtype=torch.float32 \|` |
| [quantization.md](../analysis/quantization.md) | `\| [Allegro-txt2vid](https://github.com/pinokiofactory/Allegro-txt2vid) \| [f8327e3](https://github.com/pinokiofactory/Allegro-txt2vid/commit/f8327e3172834ee8d932d7284641a5e9a0065cbc) \| [15](https://github.com/pinokiofactory/Allegro-txt2vid/blob/f8327e3172834ee8d932d7284641a5e9a0065cbc/vae_inference.py#L15) \| float / FP32 \| dtype declaration \| # vae have better performance in float32 \|` |
| [quantization.md](../analysis/quantization.md) | `\| [Allegro-txt2vid](https://github.com/pinokiofactory/Allegro-txt2vid) \| [f8327e3](https://github.com/pinokiofactory/Allegro-txt2vid/commit/f8327e3172834ee8d932d7284641a5e9a0065cbc) \| [16](https://github.com/pinokiofactory/Allegro-txt2vid/blob/f8327e3172834ee8d932d7284641a5e9a0065cbc/vae_inference.py#L16) \| float / FP32 \| dtype declaration \| vae = AllegroAutoencoderKL3D.from_pretrained(args.vae, torch_dtype=torch.float32).cuda() \|` |
| [quantization.md](../analysis/quantization.md) | `\| [Allegro-txt2vid](https://github.com/pinokiofactory/Allegro-txt2vid) \| [f8327e3](https://github.com/pinokiofactory/Allegro-txt2vid/commit/f8327e3172834ee8d932d7284641a5e9a0065cbc) \| [23](https://github.com/pinokiofactory/Allegro-txt2vid/blob/f8327e3172834ee8d932d7284641a5e9a0065cbc/vae_inference.py#L23) \| — \| explicit cast \| frames = torch.from_numpy(frames).float() / 255.0 \|` |
| [quantization.md](../analysis/quantization.md) | `\| [Allegro-txt2vid](https://github.com/pinokiofactory/Allegro-txt2vid) \| [f8327e3](https://github.com/pinokiofactory/Allegro-txt2vid/commit/f8327e3172834ee8d932d7284641a5e9a0065cbc) \| [28](https://github.com/pinokiofactory/Allegro-txt2vid/blob/f8327e3172834ee8d932d7284641a5e9a0065cbc/vae_inference.py#L28) \| float / FP32 \| explicit cast \| frames = frames.cuda().to(torch.float32) \|` |
| [quantization.md](../analysis/quantization.md) | `\| [Allegro-txt2vid](https://github.com/pinokiofactory/Allegro-txt2vid) \| [f8327e3](https://github.com/pinokiofactory/Allegro-txt2vid/commit/f8327e3172834ee8d932d7284641a5e9a0065cbc) \| [31](https://github.com/pinokiofactory/Allegro-txt2vid/blob/f8327e3172834ee8d932d7284641a5e9a0065cbc/vae_inference.py#L31) \| uint8 \| explicit cast \| out_video = ((out_video / 2.0 + 0.5).clamp(0, 1) * 255).to(dtype=torch.uint8).cpu().permute(0, 1, 3, 4, 2).contiguous() \|` |
| [quantization.md](../analysis/quantization.md) | `\| [Allegro-txt2vid](https://github.com/pinokiofactory/Allegro-txt2vid) \| [f8327e3](https://github.com/pinokiofactory/Allegro-txt2vid/commit/f8327e3172834ee8d932d7284641a5e9a0065cbc) \| [13](https://github.com/pinokiofactory/Allegro-txt2vid/blob/f8327e3172834ee8d932d7284641a5e9a0065cbc/single_inference.py#L13) \| bfloat16 / BF16 \| dtype declaration \| dtype=torch.bfloat16 \|` |
| [quantization.md](../analysis/quantization.md) | *15 more rows omitted* |
| [fusion.md](../analysis/fusion.md) | `\| Fused GEMM epilogue (`baddbmm`) \| 1 \| Allegro-txt2vid only \|` |
| [fusion.md](../analysis/fusion.md) | `\| Fused activation (`GELU(approximate='tanh')`, SiLU) \| 3 \| Allegro-txt2vid, Nari-Dia-TTS, diffusers-image-fill \|` |
| [fusion.md](../analysis/fusion.md) | `\| [Allegro-txt2vid](https://github.com/pinokiofactory/Allegro-txt2vid) \| [f8327e3](https://github.com/pinokiofactory/Allegro-txt2vid/commit/f8327e3172834ee8d932d7284641a5e9a0065cbc) \| direct code \| [allegro/models/transformers/block.py:238](https://github.com/pinokiofactory/Allegro-txt2vid/blob/f8327e3172834ee8d932d7284641a5e9a0065cbc/allegro/models/transformers/block.py#L238) — `if hasattr(F, "scaled_dot_product_attention") and self.scale_qk` \|` |
| [models.md](../analysis/models.md) | No model pull/shape row matched in models.md. |
| [cpu.md](../analysis/cpu.md) | CPU category: **Hard-blocked on CUDA** |
| [tpu.md](../analysis/tpu.md) | TPU suitability: **Hard - major rewrite/replacement required** — CUDA/TensorRT/compiled CUDA extension dependency |

### Related analysis

- [CPU analysis](../analysis/cpu.md)
- [TPU analysis](../analysis/tpu.md)
- [Effort ranking](../analysis/effort.md)
- [Kernel evidence](../analysis/kernels.md)
- [Quantization evidence](../analysis/quantization.md)
- [Fusion evidence](../analysis/fusion.md)
- [Model pulls/shapes](../analysis/models.md)
- [Flow graphs](../analysis/flows.md)
- [App flow graph](../flows/Allegro-txt2vid.md)
<!-- cross-analysis:end -->
