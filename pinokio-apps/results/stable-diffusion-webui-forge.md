# stable-diffusion-webui-forge — portability analysis

- **Package name:** Forge (`stable-diffusion-webui-forge`)
- **Description:** [NVIDIA ONLY] The most efficient way to run FLUX (Optimized to run even on low memory machines, as low as 3GB VRAM with 512x512 resolution) https://github.com/lllyasviel/stable-diffusion-webui-forge
- **Original git URL:** https://github.com/pinokiofactory/stable-diffusion-webui-forge
- **Analyzed commit:** `e44fda22458c495919a1c90ed9e7d5c63c37adfb`
- **Platforms supported:** NVIDIA only
- **Porting difficulty:** Medium
- **CUDA-only packages:** torch (CUDA wheel)

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

numpy, torch, torchaudio, torchvision, wheel

Wheel indexes referenced: cu128.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 374
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- Explicit platform tag found: NVIDIA only.
- `torch.js` routes present: none.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Difficulty score: 4.0 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- retested on Python 3.10; runtime still calls torch.cuda.current_device() and is not CPU-compatible.
- Result: **not runnable in this container.**
<!-- cross-analysis:start -->
## Cross-analysis details

- **CPU category (cpu.md):** CPU-capable with shipped fallback
- **TPU suitability:** Difficult - high-effort port
- **TPU work needed:** replace CUDA torch wheel with TPU-supported runtime; NF4/bitsandbytes quantization needs dequant/upcast or TPU-supported path; FP8 GEMMs need upcast or TPU FP8 kernel support/validation; large BF16/FP16 GEMM workload; expect XLA compile/memory tuning; many CUDA-specific dependencies/quantization/runtime constraints
- **Effort ranking (effort.md):** #73 — Medium–high
- **Effort blockers:** CUDA-only torch wheel; 817 FP8 GEMMs need upcast; 626 packed 4-bit weights need dequantisation; large FP16/BF16 GEMM load
- **Precisions noted:** FP32, FP16, BF16, FP8, NF4, UINT8
- **Models/flows noted:** [XLabs-AI/flux-lora-collection](https://huggingface.co/XLabs-AI/flux-lora-collection), [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv), [latent-consistency/lcm-lora-sdxl](https://huggingface.co/latent-consistency/lcm-lora-sdxl), [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4), [lllyasviel/flux1_dev](https://huggingface.co/lllyasviel/flux1_dev), [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5), [silveroxides/flux1-nf4-weights](https://huggingface.co/silveroxides/flux1-nf4-weights), [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo), [stabilityai/stable-diffusion-2-1](https://huggingface.co/stabilityai/stable-diffusion-2-1), [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0), [stabilityai/stable-diffusion-xl-refiner-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0), [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt), [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid)
- **Flow graph:** [flows/stable-diffusion-webui-forge.md](../flows/stable-diffusion-webui-forge.md)

### Snapshot verification (cloned analyzed commit)

- **Snapshot source:** `https://codeload.github.com/pinokiofactory/stable-diffusion-webui-forge/tar.gz/<analyzed commit>` extracted to `/tmp/opencode/pinokio-snapshots/stable-diffusion-webui-forge`
- **Files scanned:** 23 total (0 .py, 5 .js, 18 other)
- **Key files present:** pinokio.js, install.js, start.js
- **TPU/CUDA-relevant signals:**
  - `bitsandbytes`: 5 match(es) (e.g. download-flux1-schnell-nf4.json:5, install.js:99)
  - `fp8`: 5 match(es) (e.g. pinokio.js:14, pinokio.js:100)
  - `nf4`: 12 match(es) (e.g. pinokio.js:12, pinokio.js:13)

### Evidence from analysis files

| Source | Evidence |
|---|---|
| [kernels.md](../analysis/kernels.md) | No per-repo kernel table row matched; see kernels.md for global signals. |
| [quantization.md](../analysis/quantization.md) | `\| [stable-diffusion-webui-forge](https://github.com/pinokiofactory/stable-diffusion-webui-forge) \| reference \| `install.js:99` — "hf download lllyasviel/flux1-dev-bnb-nf4 flux1-dev-bnb-nf4-v2.safetensors --local-dir app/models/Stable-diffusion"<br>`install.js:108` — "hf download lllyasviel/flux1_dev flux1-dev-fp8.safetensors --local-dir app/models/Stable-diffusion" \|` |
| [quantization.md](../analysis/quantization.md) | `\| [stable-diffusion-webui-forge](https://github.com/pinokiofactory/stable-diffusion-webui-forge) \| reference \| `install.js:99` — "hf download lllyasviel/flux1-dev-bnb-nf4 flux1-dev-bnb-nf4-v2.safetensors --local-dir app/models/Stable-diffusion"<br>`download-flux1-schnell-nf4.json:5` — "uri": "https://huggingface.co/silveroxides/flux1-nf4-weights/resolve/main/flux1-schnell-bnb-nf4.safetensors?download=true", \|` |
| [quantization.md](../analysis/quantization.md) | `\| [stable-diffusion-webui-forge](https://github.com/pinokiofactory/stable-diffusion-webui-forge) \| [e44fda2](https://github.com/pinokiofactory/stable-diffusion-webui-forge/commit/e44fda22458c495919a1c90ed9e7d5c63c37adfb) \| [99](https://github.com/pinokiofactory/stable-diffusion-webui-forge/blob/e44fda22458c495919a1c90ed9e7d5c63c37adfb/install.js#L99) \| NF4 / bnb 4-bit \| dtype declaration \| "hf download lllyasviel/flux1-dev-bnb-nf4 flux1-dev-bnb-nf4-v2.safetensors --local-dir app/models/Stable-diffusion" \|` |
| [quantization.md](../analysis/quantization.md) | `\| [stable-diffusion-webui-forge](https://github.com/pinokiofactory/stable-diffusion-webui-forge) \| [e44fda2](https://github.com/pinokiofactory/stable-diffusion-webui-forge/commit/e44fda22458c495919a1c90ed9e7d5c63c37adfb) \| [108](https://github.com/pinokiofactory/stable-diffusion-webui-forge/blob/e44fda22458c495919a1c90ed9e7d5c63c37adfb/install.js#L108) \| float8 / FP8 \| dtype declaration \| "hf download lllyasviel/flux1_dev flux1-dev-fp8.safetensors --local-dir app/models/Stable-diffusion" \|` |
| [quantization.md](../analysis/quantization.md) | `\| [stable-diffusion-webui-forge](https://github.com/pinokiofactory/stable-diffusion-webui-forge) \| [e44fda2](https://github.com/pinokiofactory/stable-diffusion-webui-forge/commit/e44fda22458c495919a1c90ed9e7d5c63c37adfb) \| [5](https://github.com/pinokiofactory/stable-diffusion-webui-forge/blob/e44fda22458c495919a1c90ed9e7d5c63c37adfb/download-flux1-dev-fp8.json#L5) \| float8 / FP8 \| checkpoint / config \| "uri": "https://huggingface.co/lllyasviel/flux1_dev/resolve/main/flux1-dev-fp8.safetensors?download=true", \|` |
| [quantization.md](../analysis/quantization.md) | `\| [stable-diffusion-webui-forge](https://github.com/pinokiofactory/stable-diffusion-webui-forge) \| [e44fda2](https://github.com/pinokiofactory/stable-diffusion-webui-forge/commit/e44fda22458c495919a1c90ed9e7d5c63c37adfb) \| [12](https://github.com/pinokiofactory/stable-diffusion-webui-forge/blob/e44fda22458c495919a1c90ed9e7d5c63c37adfb/pinokio.js#L12) \| NF4 / bnb 4-bit \| checkpoint / config \| "download-flux1-dev-nf4-v2.json", \|` |
| [quantization.md](../analysis/quantization.md) | `\| [stable-diffusion-webui-forge](https://github.com/pinokiofactory/stable-diffusion-webui-forge) \| [e44fda2](https://github.com/pinokiofactory/stable-diffusion-webui-forge/commit/e44fda22458c495919a1c90ed9e7d5c63c37adfb) \| [13](https://github.com/pinokiofactory/stable-diffusion-webui-forge/blob/e44fda22458c495919a1c90ed9e7d5c63c37adfb/pinokio.js#L13) \| NF4 / bnb 4-bit \| checkpoint / config \| "download-flux1-schnell-nf4.json", \|` |
| [quantization.md](../analysis/quantization.md) | `\| [stable-diffusion-webui-forge](https://github.com/pinokiofactory/stable-diffusion-webui-forge) \| [e44fda2](https://github.com/pinokiofactory/stable-diffusion-webui-forge/commit/e44fda22458c495919a1c90ed9e7d5c63c37adfb) \| [14](https://github.com/pinokiofactory/stable-diffusion-webui-forge/blob/e44fda22458c495919a1c90ed9e7d5c63c37adfb/pinokio.js#L14) \| float8 / FP8 \| checkpoint / config \| "download-flux1-dev-fp8.json", \|` |
| [quantization.md](../analysis/quantization.md) | *5 more rows omitted* |
| [fusion.md](../analysis/fusion.md) | `\| [stable-diffusion-webui-forge](https://github.com/pinokiofactory/stable-diffusion-webui-forge) \| [e44fda2](https://github.com/pinokiofactory/stable-diffusion-webui-forge/commit/e44fda22458c495919a1c90ed9e7d5c63c37adfb) \| 404 \| `to_q.weight` / `to_k.weight` / `to_v.weight` in `model.diffusion_model.input_blocks.1.1.time_stack.0.attn1` (cocktailpeanut/sv, B=`[320, 320]`) \| [`stable-diffusion-webui-forge.md`](../flows/stable-diffusion-webui-forge.md) \|` |
| [fusion.md](../analysis/fusion.md) | `\| [stable-diffusion-webui-forge](https://github.com/pinokiofactory/stable-diffusion-webui-forge) \| [e44fda2](https://github.com/pinokiofactory/stable-diffusion-webui-forge/commit/e44fda22458c495919a1c90ed9e7d5c63c37adfb) \| 10 \| none \| [`stable-diffusion-webui-forge.md`](../flows/stable-diffusion-webui-forge.md) \|` |
| [fusion.md](../analysis/fusion.md) | `\| [stable-diffusion-webui-forge](https://github.com/pinokiofactory/stable-diffusion-webui-forge) \| [e44fda2](https://github.com/pinokiofactory/stable-diffusion-webui-forge/commit/e44fda22458c495919a1c90ed9e7d5c63c37adfb) \| 3,724 \| [`stable-diffusion-webui-forge.md`](../flows/stable-diffusion-webui-forge.md) \|` |
| [models.md](../analysis/models.md) | No model pull/shape row matched in models.md. |
| [cpu.md](../analysis/cpu.md) | CPU category: **CPU-capable with shipped fallback** |
| [tpu.md](../analysis/tpu.md) | TPU suitability: **Difficult - high-effort port** — replace CUDA torch wheel with TPU-supported runtime; NF4/bitsandbytes quantization needs dequant/upcast or TPU-supported path; FP8 GEMMs need upcast or TPU FP8 kernel support/validation; large BF16/FP16 GEMM workload; expect XLA compile/memory tuning; many CUDA-specific dependencies/quantization/runtime constraints |

### Related analysis

- [CPU analysis](../analysis/cpu.md)
- [TPU analysis](../analysis/tpu.md)
- [Effort ranking](../analysis/effort.md)
- [Kernel evidence](../analysis/kernels.md)
- [Quantization evidence](../analysis/quantization.md)
- [Fusion evidence](../analysis/fusion.md)
- [Model pulls/shapes](../analysis/models.md)
- [Flow graphs](../analysis/flows.md)
- [App flow graph](../flows/stable-diffusion-webui-forge.md)
<!-- cross-analysis:end -->
