# forge — portability analysis

- **Package name:** Stable Diffusion Forge (`forge`)
- **Description:** Stable Diffusion WebUI Forge is a platform on top of Stable Diffusion WebUI (based on Gradio) to make development easier, optimize resource management, and speed up inference. https://github.com/lllyasviel/stable-diffusion-webui-forge?tab=readme-ov-file
- **Original git URL:** https://github.com/pinokiofactory/forge
- **Analyzed commit:** `e3378c35f7f1c4fec2f600c33b9d17ab6d330b4c`
- **Platforms supported:** Cross-platform
- **Porting difficulty:** Low
- **CUDA-only packages:** —

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

No package dependencies were declared in the repository. Installers that only run `npm install` or clone another app do not name packages here.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 323
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- `torch.js` routes present: none.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Difficulty score: 0.0 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- retested on Python 3.12; tokenizers build failure.
- Result: **not runnable in this container.**
<!-- cross-analysis:start -->
## Cross-analysis details

- **CPU category (cpu.md):** CPU possible, but launcher must change
- **TPU suitability:** Possible - moderate port
- **TPU work needed:** add TPU launcher/runtime branch; large BF16/FP16 GEMM workload; expect XLA compile/memory tuning; moderate device/kernel/runtime adaptation
- **Effort ranking (effort.md):** #46 — Low–medium
- **Effort blockers:** no CPU/AMD launcher branch; large FP16/BF16 GEMM load
- **Precisions noted:** FP32, FP16
- **Models/flows noted:** [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv), [latent-consistency/lcm-lora-sdxl](https://huggingface.co/latent-consistency/lcm-lora-sdxl), [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5), [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo), [stabilityai/stable-diffusion-2-1](https://huggingface.co/stabilityai/stable-diffusion-2-1), [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0), [stabilityai/stable-diffusion-xl-refiner-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0), [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt), [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid)
- **Flow graph:** [flows/forge.md](../flows/forge.md)

### Snapshot verification (cloned analyzed commit)

- **Snapshot source:** `https://codeload.github.com/pinokiofactory/forge/tar.gz/<analyzed commit>` extracted to `/tmp/opencode/pinokio-snapshots/forge`
- **Files scanned:** 19 total (0 .py, 6 .js, 13 other)
- **Key files present:** pinokio.js, install.js, start.js
- **TPU/CUDA-relevant signals:** none detected by text scan (still inspect runtime behavior before porting)

### Evidence from analysis files

| Source | Evidence |
|---|---|
| [kernels.md](../analysis/kernels.md) | No per-repo kernel table row matched; see kernels.md for global signals. |
| [quantization.md](../analysis/quantization.md) | No per-repo quantization table row matched; see quantization.md. |
| [fusion.md](../analysis/fusion.md) | `\| [stable-diffusion-webui-forge](https://github.com/pinokiofactory/stable-diffusion-webui-forge) \| [e44fda2](https://github.com/pinokiofactory/stable-diffusion-webui-forge/commit/e44fda22458c495919a1c90ed9e7d5c63c37adfb) \| 404 \| `to_q.weight` / `to_k.weight` / `to_v.weight` in `model.diffusion_model.input_blocks.1.1.time_stack.0.attn1` (cocktailpeanut/sv, B=`[320, 320]`) \| [`stable-diffusion-webui-forge.md`](../flows/stable-diffusion-webui-forge.md) \|` |
| [fusion.md](../analysis/fusion.md) | `\| [forge](https://github.com/pinokiofactory/forge) \| [e3378c3](https://github.com/pinokiofactory/forge/commit/e3378c35f7f1c4fec2f600c33b9d17ab6d330b4c) \| 332 \| `to_q.weight` / `to_k.weight` / `to_v.weight` in `model.diffusion_model.input_blocks.1.1.time_stack.0.attn1` (cocktailpeanut/sv, B=`[320, 320]`) \| [`forge.md`](../flows/forge.md) \|` |
| [fusion.md](../analysis/fusion.md) | `\| [stable-diffusion-webui-forge](https://github.com/pinokiofactory/stable-diffusion-webui-forge) \| [e44fda2](https://github.com/pinokiofactory/stable-diffusion-webui-forge/commit/e44fda22458c495919a1c90ed9e7d5c63c37adfb) \| 10 \| none \| [`stable-diffusion-webui-forge.md`](../flows/stable-diffusion-webui-forge.md) \|` |
| [models.md](../analysis/models.md) | No model pull/shape row matched in models.md. |
| [cpu.md](../analysis/cpu.md) | CPU category: **CPU possible, but launcher must change** |
| [tpu.md](../analysis/tpu.md) | TPU suitability: **Possible - moderate port** — add TPU launcher/runtime branch; large BF16/FP16 GEMM workload; expect XLA compile/memory tuning; moderate device/kernel/runtime adaptation |

### Related analysis

- [CPU analysis](../analysis/cpu.md)
- [TPU analysis](../analysis/tpu.md)
- [Effort ranking](../analysis/effort.md)
- [Kernel evidence](../analysis/kernels.md)
- [Quantization evidence](../analysis/quantization.md)
- [Fusion evidence](../analysis/fusion.md)
- [Model pulls/shapes](../analysis/models.md)
- [Flow graphs](../analysis/flows.md)
- [App flow graph](../flows/forge.md)
<!-- cross-analysis:end -->
