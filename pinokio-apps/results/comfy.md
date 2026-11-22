# comfy — portability analysis

- **Package name:** Comfyui (`comfy`)
- **Description:** The most powerful and modular diffusion model GUI, api and backend with a graph/nodes interface. https://github.com/comfyanonymous/ComfyUI
- **Original git URL:** https://github.com/pinokiofactory/comfy
- **Analyzed commit:** `ba110479f88835d64c603044c2fe69102833fa55`
- **Platforms supported:** NVIDIA / AMD / Mac
- **Porting difficulty:** Very high
- **CUDA-only packages:** bitsandbytes, flash-attn, sageattention, triton, triton-windows, xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

bitsandbytes, flash-attn, numpy, sageattention, torch, torch-directml, torchaudio, torchvision, triton, triton-windows, xformers

Wheel indexes referenced: cpu, cu128, rocm6.3.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 1262
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- `torch.js` routes present: nvidia, amd, mac, cpu.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): xformers
- Difficulty score: 12.5 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- dependencies installed; server started on CPU with --cpu flag.
- Result: **CPU port works with --cpu.**

## CPU port attempt

- **Attempt order:** #96 of 101 (by porting effort, easiest first).
- **Status:** CPU-capable (shipped fallback).
- **Changes applied / required:** use existing CPU wheel branch in torch.js; use existing non-NVIDIA/non-AMD branch in torch.js; use existing non-GPU launcher route; disable fused GPU kernels (xformers/flash/sage) in config; substitute GPU-only attention libs with SDPA math backend; remove bitsandbytes/torchao GPU quantisers or switch to GGUF; +3.
- **Smoke check:** n/a (no Python source in snapshot).
- **Blockers:** GPU-only attention: flash-attn/sageattention/triton/triton-windows/xformers; GPU quantisers: bitsandbytes; CUDA-only fused kernels; 2916 FP8 GEMMs; +1.
- **Scope note:** static portability review of the Pinokio wrapper; no install or model download was executed.
<!-- cross-analysis:start -->
## Cross-analysis details

- **CPU category (cpu.md):** CPU-capable with shipped fallback
- **TPU suitability:** Difficult - significant port
- **TPU work needed:** replace CUDA attention kernels with TPU-compatible attention/SDPA/XLA; NF4/bitsandbytes quantization needs dequant/upcast or TPU-supported path; FP8 GEMMs need upcast or TPU FP8 kernel support/validation; multiple CUDA-specific dependencies or large model/dtype constraints
- **Effort ranking (effort.md):** #96 — Very high
- **Effort blockers:** GPU-only attention: flash-attn/sageattention/triton/triton-windows/xformers; GPU quantisers: bitsandbytes; CUDA-only fused kernels need config change; 2916 FP8 GEMMs need upcast; 626 packed 4-bit weights need dequantisation; +1 more
- **Precisions noted:** FP32, FP16, BF16, FP8, NF4, UINT8
- **Models/flows noted:** [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged), [Comfy-Org/flux1-dev](https://huggingface.co/Comfy-Org/flux1-dev), [Comfy-Org/flux1-schnell](https://huggingface.co/Comfy-Org/flux1-schnell), [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged), [Comfy-Org/sigclip_vision_384](https://huggingface.co/Comfy-Org/sigclip_vision_384), [Comfy-Org/stable-diffusion-3.5-fp8](https://huggingface.co/Comfy-Org/stable-diffusion-3.5-fp8), [Kijai/HunyuanVideo_comfy](https://huggingface.co/Kijai/HunyuanVideo_comfy), [Kijai/llava-llama-3-8b-text-encoder-tokenizer](https://huggingface.co/Kijai/llava-llama-3-8b-text-encoder-tokenizer), [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video), [city96/FLUX.1-dev-gguf](https://huggingface.co/city96/FLUX.1-dev-gguf), [city96/FLUX.1-schnell-gguf](https://huggingface.co/city96/FLUX.1-schnell-gguf), [cocktailpeanut/fcanny](https://huggingface.co/cocktailpeanut/fcanny), [cocktailpeanut/fdepth](https://huggingface.co/cocktailpeanut/fdepth), [cocktailpeanut/fill](https://huggingface.co/cocktailpeanut/fill), [cocktailpeanut/redux](https://huggingface.co/cocktailpeanut/redux), [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv), [cocktailpeanut/xulf-dev](https://huggingface.co/cocktailpeanut/xulf-dev), [cocktailpeanut/xulf-schnell](https://huggingface.co/cocktailpeanut/xulf-schnell), [comfyanonymous/flux_text_encoders](https://huggingface.co/comfyanonymous/flux_text_encoders), [drbaph/FLUX.1-schnell-dev-merged-fp8-4step](https://huggingface.co/drbaph/FLUX.1-schnell-dev-merged-fp8-4step), [latent-consistency/lcm-lora-sdxl](https://huggingface.co/latent-consistency/lcm-lora-sdxl), [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4), [openai/clip-vit-large-patch14](https://huggingface.co/openai/clip-vit-large-patch14), [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5), [silveroxides/flux1-nf4-weights](https://huggingface.co/silveroxides/flux1-nf4-weights), [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo), [stabilityai/stable-diffusion-2-1](https://huggingface.co/stabilityai/stable-diffusion-2-1), [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0)
- **Flow graph:** [flows/comfy.md](../flows/comfy.md)

### Snapshot verification (cloned analyzed commit)

- **Snapshot source:** `https://codeload.github.com/pinokiofactory/comfy/tar.gz/<analyzed commit>` extracted to `/tmp/opencode/pinokio-snapshots/comfy`
- **Files scanned:** 54 total (0 .py, 16 .js, 38 other)
- **Key files present:** pinokio.js, install.js, torch.js, start.js
- **TPU/CUDA-relevant signals:**
  - `xformers`: 5 match(es) (e.g. torch.js:11, torch.js:11)
  - `flash_attn`: 3 match(es) (e.g. torch.js:14, torch.js:61)
  - `sageattention`: 4 match(es) (e.g. torch.js:13, torch.js:13)
  - `triton`: 5 match(es) (e.g. torch.js:12, torch.js:59)
  - `bitsandbytes`: 5 match(es) (e.g. download-flux-dev-nf4.json:7, download-flux-dev-nf4.json:8)
  - `fp8`: 34 match(es) (e.g. mochi-lite.json:11, h.js:7)
  - `nf4`: 11 match(es) (e.g. download-flux-dev-nf4.json:7, download-flux-dev-nf4.json:8)
  - `gguf`: 10 match(es) (e.g. download-flux-schnell-gguf-q4-0.json:7, download-flux-schnell-gguf-q4-0.json:8)
  - `directml`: 3 match(es) (e.g. torch.js:26, start.js:19)

### Evidence from analysis files

| Source | Evidence |
|---|---|
| [kernels.md](../analysis/kernels.md) | `\| [comfy](https://github.com/pinokiofactory/comfy) \| [ba11047](https://github.com/pinokiofactory/comfy/commit/ba110479f88835d64c603044c2fe69102833fa55) \| optional flag + launcher install \| h.js, torch.js \| [h.js:63](https://github.com/pinokiofactory/comfy/blob/ba110479f88835d64c603044c2fe69102833fa55/h.js#L63) — //          "{{platform === 'win32' ? 'pip install https://github.com/woct0rdho/triton-windows/releases/download/v3.0.0-windows.post3/triton-3.0.0-cp310-cp310-win... \|` |
| [kernels.md](../analysis/kernels.md) | `\| [comfy](https://github.com/pinokiofactory/comfy) \| [ba11047](https://github.com/pinokiofactory/comfy/commit/ba110479f88835d64c603044c2fe69102833fa55) \| launcher install \| [torch.js:14](https://github.com/pinokiofactory/comfy/blob/ba110479f88835d64c603044c2fe69102833fa55/torch.js#L14) — "uv pip install https://huggingface.co/cocktailpeanut/wheels/resolve/main/flash_attn-2.8.2%2Bcu128torch2.7-cp310-cp310-win_amd64.whl"<br>[torch.js:60](https://github.com/pinokiofactory/comfy/blob/ba110479f88835d64c603044c2fe69102833fa55/torch.js#L60) — "uv pip install https://huggingface.co/MonsterMMORPG/SECourses_Premium_Flash_Attention/resolve/main/sageattention-2.1.1-cp310-cp310-linux_x86_64.whl", \|` |
| [kernels.md](../analysis/kernels.md) | `\| [comfy](https://github.com/pinokiofactory/comfy) \| [ba11047](https://github.com/pinokiofactory/comfy/commit/ba110479f88835d64c603044c2fe69102833fa55) \| launcher install \| [h.js:62](https://github.com/pinokiofactory/comfy/blob/ba110479f88835d64c603044c2fe69102833fa55/h.js#L62) — //          "pip install sageattention",<br>[torch.js:13](https://github.com/pinokiofactory/comfy/blob/ba110479f88835d64c603044c2fe69102833fa55/torch.js#L13) — "uv pip install https://github.com/woct0rdho/SageAttention/releases/download/v2.1.1-windows/sageattention-2.1.1+cu128torch2.7.0-cp310-cp310-win_amd64.whl", \|` |
| [quantization.md](../analysis/quantization.md) | `\| [comfy](https://github.com/pinokiofactory/comfy) \| reference \| `download-flux-dev-fp8.json:8` — "files": "flux1-dev-fp8.safetensors",<br>`download-flux-schnell-fp8.json:8` — "files": "flux1-schnell-fp8.safetensors", \|` |
| [quantization.md](../analysis/quantization.md) | `\| [comfy](https://github.com/pinokiofactory/comfy) \| reference \| `download-flux-schnell-gguf-q4-0.json:7` — "repo": "city96/FLUX.1-schnell-gguf",<br>`download-flux-schnell-gguf-q4-0.json:8` — "files": "flux1-schnell-Q4_0.gguf", \|` |
| [quantization.md](../analysis/quantization.md) | `\| [comfy](https://github.com/pinokiofactory/comfy) \| launcher install \| `download-flux-dev-nf4.json:7` — "repo": "lllyasviel/flux1-dev-bnb-nf4",<br>`download-flux-dev-nf4.json:8` — "files": "flux1-dev-bnb-nf4.safetensors", \|` |
| [quantization.md](../analysis/quantization.md) | `\| [comfy](https://github.com/pinokiofactory/comfy) \| [ba11047](https://github.com/pinokiofactory/comfy/commit/ba110479f88835d64c603044c2fe69102833fa55) \| [8](https://github.com/pinokiofactory/comfy/blob/ba110479f88835d64c603044c2fe69102833fa55/download-flux-dev-fp8.json#L8) \| float8 / FP8 \| checkpoint / config \| "files": "flux1-dev-fp8.safetensors", \|` |
| [quantization.md](../analysis/quantization.md) | `\| [comfy](https://github.com/pinokiofactory/comfy) \| [ba11047](https://github.com/pinokiofactory/comfy/commit/ba110479f88835d64c603044c2fe69102833fa55) \| [8](https://github.com/pinokiofactory/comfy/blob/ba110479f88835d64c603044c2fe69102833fa55/download-flux-schnell-fp8.json#L8) \| float8 / FP8 \| checkpoint / config \| "files": "flux1-schnell-fp8.safetensors", \|` |
| [quantization.md](../analysis/quantization.md) | `\| [comfy](https://github.com/pinokiofactory/comfy) \| [ba11047](https://github.com/pinokiofactory/comfy/commit/ba110479f88835d64c603044c2fe69102833fa55) \| [7](https://github.com/pinokiofactory/comfy/blob/ba110479f88835d64c603044c2fe69102833fa55/download-flux-merged-fp8.json#L7) \| float8 / FP8 \| checkpoint / config \| "repo": "drbaph/FLUX.1-schnell-dev-merged-fp8-4step", \|` |
| [quantization.md](../analysis/quantization.md) | `\| [comfy](https://github.com/pinokiofactory/comfy) \| [ba11047](https://github.com/pinokiofactory/comfy/commit/ba110479f88835d64c603044c2fe69102833fa55) \| [8](https://github.com/pinokiofactory/comfy/blob/ba110479f88835d64c603044c2fe69102833fa55/download-flux-merged-fp8.json#L8) \| float8 / FP8 \| checkpoint / config \| "files": "FLUX.1-schnell-dev-merged-fp8-4step.safetensors", \|` |
| [quantization.md](../analysis/quantization.md) | `\| [comfy](https://github.com/pinokiofactory/comfy) \| [ba11047](https://github.com/pinokiofactory/comfy/commit/ba110479f88835d64c603044c2fe69102833fa55) \| [7](https://github.com/pinokiofactory/comfy/blob/ba110479f88835d64c603044c2fe69102833fa55/download-flux-dev-nf4.json#L7) \| NF4 / bnb 4-bit \| checkpoint / config \| "repo": "lllyasviel/flux1-dev-bnb-nf4", \|` |
| [quantization.md](../analysis/quantization.md) | *23 more rows omitted* |
| [fusion.md](../analysis/fusion.md) | `\| [comfy](https://github.com/pinokiofactory/comfy) \| [ba11047](https://github.com/pinokiofactory/comfy/commit/ba110479f88835d64c603044c2fe69102833fa55) \| installed by launcher \| [torch.js:13](https://github.com/pinokiofactory/comfy/blob/ba110479f88835d64c603044c2fe69102833fa55/torch.js#L13) — `"uv pip install https://github.com/woct0rdho/SageAttention/releases/download/v2.1.1-windows/sageattention-2.1.1+cu128torch2.7.0-cp310-cp310-win_amd64.` \|` |
| [fusion.md](../analysis/fusion.md) | `\| [comfy](https://github.com/pinokiofactory/comfy) \| [ba11047](https://github.com/pinokiofactory/comfy/commit/ba110479f88835d64c603044c2fe69102833fa55) \| 745 \| `q.weight` / `k.weight` / `v.weight` in `blocks.0.cross_attn` (Comfy-Org/Wan_2.1_ComfyUI_repackaged, B=`[5120, 5120]`) \| [`comfy.md`](../flows/comfy.md) \|` |
| [fusion.md](../analysis/fusion.md) | `\| [comfy](https://github.com/pinokiofactory/comfy) \| [ba11047](https://github.com/pinokiofactory/comfy/commit/ba110479f88835d64c603044c2fe69102833fa55) \| 29 \| installed by launcher \| [`comfy.md`](../flows/comfy.md) \|` |
| [models.md](../analysis/models.md) | No model pull/shape row matched in models.md. |
| [cpu.md](../analysis/cpu.md) | CPU category: **CPU-capable with shipped fallback** |
| [tpu.md](../analysis/tpu.md) | TPU suitability: **Difficult - significant port** — replace CUDA attention kernels with TPU-compatible attention/SDPA/XLA; NF4/bitsandbytes quantization needs dequant/upcast or TPU-supported path; FP8 GEMMs need upcast or TPU FP8 kernel support/validation; multiple CUDA-specific dependencies or large model/dtype constraints |

### Related analysis

- [CPU analysis](../analysis/cpu.md)
- [TPU analysis](../analysis/tpu.md)
- [Effort ranking](../analysis/effort.md)
- [Kernel evidence](../analysis/kernels.md)
- [Quantization evidence](../analysis/quantization.md)
- [Fusion evidence](../analysis/fusion.md)
- [Model pulls/shapes](../analysis/models.md)
- [Flow graphs](../analysis/flows.md)
- [App flow graph](../flows/comfy.md)
<!-- cross-analysis:end -->

## Snapdragon evaluation (deep clone)
- **Clone/scan status:** cloned and scanned
- **Files scanned:** 54 total (0 .py, 16 .js/.ts, 38 other)
- **Snapdragon-relevant signals:** torch=14, triton=3, xformers=3, sageattention=3, bitsandbytes=1, mps=3, directml=3, gguf=8, safetensors=92
- **Example evidence:**
  - torch: `download-lcm-lora.json:8`
  - triton: `h.js:63`
  - xformers: `install.js:46`
  - sageattention: `h.js:62`
  - bitsandbytes: `install.js:35`
  - mps: `install.js:105`
  - directml: `install.js:110`
  - gguf: `download-flux-dev-gguf-q4-0.json:7`
  - safetensors: `download-flux-dev-fp8.json:8`
- **Snapdragon verdict:** Contains CUDA/Triton/TensorRT signals; Snapdragon path requires replacement or ONNX conversion.
