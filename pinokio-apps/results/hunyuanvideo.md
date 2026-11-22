# hunyuanvideo — portability analysis

- **Package name:** HunyuanVideo (`hunyuanvideo`)
- **Description:** [NVIDIA ONLY] Super Optimized Gradio UI for Hunyuan Video Generator that works on GPU poor machines. Generate up to 10~14 sec videos https://github.com/deepbeepmeep/HunyuanVideoGP
- **Original git URL:** https://github.com/pinokiofactory/hunyuanvideo
- **Analyzed commit:** `c65cb772466eea61e0a330f52ed7764a9d4e821d`
- **Platforms supported:** NVIDIA only
- **Porting difficulty:** Very high
- **CUDA-only packages:** flash-attn, sageattention *(optional)*, triton *(optional)*, triton-windows, xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

accelerate, av, diffusers, einops, fire, flash-attn, gradio, hf-xet, imageio, imageio-ffmpeg, lightning, loguru, mmgp, moviepy, numpy, omegaconf, opencv-python, pandas, peft, pydantic, safetensors, sageattention, tokenizers, torch, torchaudio, torchvision, tqdm, transformers, triton, triton-windows, xformers

Requirements files: `requirements.txt`.

Wheel indexes referenced: cu128.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 462
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- Explicit platform tag found: NVIDIA only.
- `torch.js` routes present: nvidia.
- Requirements from: requirements.txt
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): sageattention, triton, xformers
- Difficulty score: 12.8 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- retested packaging path; still blocked by explicit NVIDIA-only guard and pandas build failure.
- Result: **not runnable in this container.**
<!-- cross-analysis:start -->
## Cross-analysis details

- **CPU category (cpu.md):** Hard-blocked on CUDA
- **TPU suitability:** Hard - major rewrite/replacement required
- **TPU work needed:** CUDA/TensorRT/compiled CUDA extension dependency
- **Effort ranking (effort.md):** #97 — Very high
- **Effort blockers:** hard CUDA/TensorRT blocker in code; GPU-only attention: flash-attn/sageattention/triton/triton-windows/xformers; CUDA-only fused kernels need config change
- **Precisions noted:** unspecified
- **Models/flows noted:** —
- **Flow graph:** [flows/hunyuanvideo.md](../flows/hunyuanvideo.md)

### Snapshot verification (cloned analyzed commit)

- **Snapshot source:** `https://codeload.github.com/pinokiofactory/hunyuanvideo/tar.gz/<analyzed commit>` extracted to `/tmp/opencode/pinokio-snapshots/hunyuanvideo`
- **Files scanned:** 14 total (0 .py, 6 .js, 8 other)
- **Key files present:** pinokio.js, install.js, torch.js, start.js, requirements.txt
- **TPU/CUDA-relevant signals:**
  - `xformers`: 4 match(es) (e.g. torch.js:11, torch.js:11)
  - `flash_attn`: 4 match(es) (e.g. torch.js:14, torch.js:14)
  - `sageattention`: 6 match(es) (e.g. torch.js:13, torch.js:13)
  - `triton`: 5 match(es) (e.g. torch.js:12, torch.js:12)

### Evidence from analysis files

| Source | Evidence |
|---|---|
| [kernels.md](../analysis/kernels.md) | `\| [hunyuanvideo](https://github.com/pinokiofactory/hunyuanvideo) \| [c65cb77](https://github.com/pinokiofactory/hunyuanvideo/commit/c65cb772466eea61e0a330f52ed7764a9d4e821d) \| optional flag + launcher install \| install.js, torch.js \| [torch.js:12](https://github.com/pinokiofactory/hunyuanvideo/blob/c65cb772466eea61e0a330f52ed7764a9d4e821d/torch.js#L12) — "{{args && args.triton ? 'uv pip install triton-windows==3.3.1.post19' : ''}}", \|` |
| [kernels.md](../analysis/kernels.md) | `\| [hunyuanvideo](https://github.com/pinokiofactory/hunyuanvideo) \| [c65cb77](https://github.com/pinokiofactory/hunyuanvideo/commit/c65cb772466eea61e0a330f52ed7764a9d4e821d) \| optional flag + launcher install \| [torch.js:14](https://github.com/pinokiofactory/hunyuanvideo/blob/c65cb772466eea61e0a330f52ed7764a9d4e821d/torch.js#L14) — "uv pip install https://github.com/kingbri1/flash-attention/releases/download/v2.7.4.post1/flash_attn-2.7.4.post1+cu128torch2.7.0cxx11abiFALSE-cp310-cp310-win_amd...<br>[torch.js:29](https://github.com/pinokiofactory/hunyuanvideo/blob/c65cb772466eea61e0a330f52ed7764a9d4e821d/torch.js#L29) — "{{args && args.sageattention ? 'uv pip install https://huggingface.co/MonsterMMORPG/SECourses_Premium_Flash_Attention/resolve/main/sageattention-2.1.1-cp310-cp31... \|` |
| [kernels.md](../analysis/kernels.md) | `\| [hunyuanvideo](https://github.com/pinokiofactory/hunyuanvideo) \| [c65cb77](https://github.com/pinokiofactory/hunyuanvideo/commit/c65cb772466eea61e0a330f52ed7764a9d4e821d) \| optional flag + launcher install \| [torch.js:13](https://github.com/pinokiofactory/hunyuanvideo/blob/c65cb772466eea61e0a330f52ed7764a9d4e821d/torch.js#L13) — "{{args && args.sageattention ? 'uv pip install https://github.com/woct0rdho/SageAttention/releases/download/v2.1.1-windows/sageattention-2.1.1+cu128torch2.7.0-cp...<br>[torch.js:29](https://github.com/pinokiofactory/hunyuanvideo/blob/c65cb772466eea61e0a330f52ed7764a9d4e821d/torch.js#L29) — "{{args && args.sageattention ? 'uv pip install https://huggingface.co/MonsterMMORPG/SECourses_Premium_Flash_Attention/resolve/main/sageattention-2.1.1-cp310-cp31... \|` |
| [quantization.md](../analysis/quantization.md) | No per-repo quantization table row matched; see quantization.md. |
| [fusion.md](../analysis/fusion.md) | `\| [hunyuanvideo](https://github.com/pinokiofactory/hunyuanvideo) \| [c65cb77](https://github.com/pinokiofactory/hunyuanvideo/commit/c65cb772466eea61e0a330f52ed7764a9d4e821d) \| [start.js:19](https://github.com/pinokiofactory/hunyuanvideo/blob/c65cb772466eea61e0a330f52ed7764a9d4e821d/start.js#L19) \| Launcher forwards `--compile` to the upstream Gradio server \|` |
| [fusion.md](../analysis/fusion.md) | `\| [hunyuanvideo](https://github.com/pinokiofactory/hunyuanvideo) \| [c65cb77](https://github.com/pinokiofactory/hunyuanvideo/commit/c65cb772466eea61e0a330f52ed7764a9d4e821d) \| installed by launcher \| [torch.js:14](https://github.com/pinokiofactory/hunyuanvideo/blob/c65cb772466eea61e0a330f52ed7764a9d4e821d/torch.js#L14) — `"uv pip install https://github.com/kingbri1/flash-attention/releases/download/v2.7.4.post1/flash_attn-2.7.4.post1+cu128torch2.7.0cxx11abiFALSE-cp310-c` \|` |
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
- [App flow graph](../flows/hunyuanvideo.md)
<!-- cross-analysis:end -->

## Snapdragon evaluation (deep clone)
- **Clone/scan status:** cloned and scanned
- **Files scanned:** 14 total (0 .py, 6 .js/.ts, 8 other)
- **Snapdragon-relevant signals:** torch=6, triton=3, xformers=2, sageattention=3, safetensors=1
- **Example evidence:**
  - torch: `install.js:35`
  - triton: `install.js:39`
  - xformers: `torch.js:11`
  - sageattention: `install.js:40`
  - safetensors: `requirements.txt:20`
- **Snapdragon verdict:** Contains CUDA/Triton/TensorRT signals; Snapdragon path requires replacement or ONNX conversion.
