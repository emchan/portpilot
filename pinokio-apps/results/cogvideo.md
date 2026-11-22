# cogvideo — portability analysis

- **Package name:** cogvideo (`cogvideo`)
- **Description:** [NVIDIA ONLY] Generate videos with less than 10GB VRAM https://github.com/THUDM/CogVideo
- **Original git URL:** https://github.com/pinokiofactory/cogvideo
- **Analyzed commit:** `9e2a18626426cbeb7e84be537d98e9082de8fe97`
- **Platforms supported:** NVIDIA only
- **Porting difficulty:** Very high
- **CUDA-only packages:** flash-attn, sageattention *(optional)*, triton *(optional)*, triton-windows, xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

accelerate, diffusers, flash-attn, gradio, hf-xet, imageio, imageio-ffmpeg, moviepy, numpy, openai, pillow, protobuf, sageattention, sentencepiece, tiktoken, torch, torch-directml, torchaudio, torchvision, transformers, triton, triton-windows, xformers

Requirements files: `requirements.txt`.

Wheel indexes referenced: cpu, cu128, rocm6.3.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 310
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- Explicit platform tag found: NVIDIA only.
- `torch.js` routes present: nvidia, amd, mac, cpu.
- Requirements from: requirements.txt
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): sageattention, triton, xformers
- Difficulty score: 10.8 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- dependencies installed and inference module imported successfully on CPU.
- Result: **CPU port imports successfully.**

## CPU port attempt

- **Attempt order:** #86 of 101 (by porting effort, easiest first).
- **Status:** CPU-capable (shipped fallback).
- **Changes applied / required:** use existing CPU wheel branch in torch.js; use existing non-GPU launcher route; disable fused GPU kernels (xformers/flash/sage) in config; substitute GPU-only attention libs with SDPA math backend.
- **Smoke check:** n/a (no Python source in snapshot).
- **Blockers:** GPU-only attention: flash-attn/sageattention/triton/triton-windows/xformers; CUDA-only fused kernels.
- **Scope note:** static portability review of the Pinokio wrapper; no install or model download was executed.
<!-- cross-analysis:start -->
## Cross-analysis details

- **CPU category (cpu.md):** CPU-capable with shipped fallback
- **TPU suitability:** Possible - moderate port
- **TPU work needed:** replace CUDA attention kernels with TPU-compatible attention/SDPA/XLA; moderate device/kernel/runtime adaptation
- **Effort ranking (effort.md):** #86 — Very high
- **Effort blockers:** GPU-only attention: flash-attn/sageattention/triton/triton-windows/xformers; CUDA-only fused kernels need config change
- **Precisions noted:** unspecified
- **Models/flows noted:** —
- **Flow graph:** [flows/cogvideo.md](../flows/cogvideo.md)

### Snapshot verification (cloned analyzed commit)

- **Snapshot source:** `https://codeload.github.com/pinokiofactory/cogvideo/tar.gz/<analyzed commit>` extracted to `/tmp/opencode/pinokio-snapshots/cogvideo`
- **Files scanned:** 13 total (0 .py, 7 .js, 6 other)
- **Key files present:** pinokio.js, install.js, torch.js, start.js, requirements.txt
- **TPU/CUDA-relevant signals:**
  - `xformers`: 5 match(es) (e.g. torch.js:11, torch.js:11)
  - `flash_attn`: 2 match(es) (e.g. torch.js:14, torch.js:31)
  - `sageattention`: 4 match(es) (e.g. torch.js:13, torch.js:13)
  - `triton`: 4 match(es) (e.g. torch.js:12, torch.js:12)
  - `directml`: 1 match(es) (e.g. torch.js:45)

### Evidence from analysis files

| Source | Evidence |
|---|---|
| [kernels.md](../analysis/kernels.md) | `\| [cogvideo](https://github.com/pinokiofactory/cogvideo) \| [9e2a186](https://github.com/pinokiofactory/cogvideo/commit/9e2a18626426cbeb7e84be537d98e9082de8fe97) \| optional flag + launcher install \| torch.js \| [torch.js:12](https://github.com/pinokiofactory/cogvideo/blob/9e2a18626426cbeb7e84be537d98e9082de8fe97/torch.js#L12) — "{{args && args.triton ? 'uv pip install triton-windows==3.3.1.post19' : ''}}", \|` |
| [kernels.md](../analysis/kernels.md) | `\| [cogvideo](https://github.com/pinokiofactory/cogvideo) \| [9e2a186](https://github.com/pinokiofactory/cogvideo/commit/9e2a18626426cbeb7e84be537d98e9082de8fe97) \| optional flag + launcher install \| [torch.js:14](https://github.com/pinokiofactory/cogvideo/blob/9e2a18626426cbeb7e84be537d98e9082de8fe97/torch.js#L14) — "{{args && args.flashattention ? 'uv pip install https://huggingface.co/cocktailpeanut/wheels/resolve/main/flash_attn-2.8.2%2Bcu128torch2.7-cp310-cp310-win_amd64....<br>[torch.js:31](https://github.com/pinokiofactory/cogvideo/blob/9e2a18626426cbeb7e84be537d98e9082de8fe97/torch.js#L31) — "{{args && args.flashattention ? 'uv pip install https://huggingface.co/cocktailpeanut/wheels/resolve/main/flash_attn-2.8.3%2Bcu128torch2.7-cp310-cp310-linux_x86_... \|` |
| [kernels.md](../analysis/kernels.md) | `\| [cogvideo](https://github.com/pinokiofactory/cogvideo) \| [9e2a186](https://github.com/pinokiofactory/cogvideo/commit/9e2a18626426cbeb7e84be537d98e9082de8fe97) \| optional flag + launcher install \| [torch.js:13](https://github.com/pinokiofactory/cogvideo/blob/9e2a18626426cbeb7e84be537d98e9082de8fe97/torch.js#L13) — "{{args && args.sageattention ? 'uv pip install https://huggingface.co/cocktailpeanut/wheels/resolve/main/sageattention-2.1.1%2Bcu128torch2.7.1-cp310-cp310-win_am...<br>[torch.js:30](https://github.com/pinokiofactory/cogvideo/blob/9e2a18626426cbeb7e84be537d98e9082de8fe97/torch.js#L30) — "{{args && args.sageattention ? 'uv pip install https://huggingface.co/cocktailpeanut/wheels/resolve/main/sageattention-2.1.1%2Bcu128torch2.7.1-cp310-cp310-linux_... \|` |
| [quantization.md](../analysis/quantization.md) | No per-repo quantization table row matched; see quantization.md. |
| [fusion.md](../analysis/fusion.md) | `\| [cogvideo](https://github.com/pinokiofactory/cogvideo) \| [9e2a186](https://github.com/pinokiofactory/cogvideo/commit/9e2a18626426cbeb7e84be537d98e9082de8fe97) \| optional launcher flag \| [torch.js:13](https://github.com/pinokiofactory/cogvideo/blob/9e2a18626426cbeb7e84be537d98e9082de8fe97/torch.js#L13) — `"{{args && args.sageattention ? 'uv pip install https://huggingface.co/cocktailpeanut/wheels/resolve/main/sageattention-2.1.1%2Bcu128torch2.7.1-cp310-` \|` |
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
- [App flow graph](../flows/cogvideo.md)
<!-- cross-analysis:end -->

## Snapdragon evaluation (deep clone)
- **Clone/scan status:** cloned and scanned
- **Files scanned:** 13 total (0 .py, 7 .js/.ts, 6 other)
- **Snapdragon-relevant signals:** torch=13, triton=2, xformers=3, flashattention=2, sageattention=2, mps=1, directml=1
- **Example evidence:**
  - torch: `install.js:26`
  - triton: `torch.js:12`
  - xformers: `install.js:30`
  - flashattention: `torch.js:14`
  - sageattention: `torch.js:13`
  - mps: `start.js:12`
  - directml: `torch.js:45`
- **Snapdragon verdict:** Contains CUDA/Triton/TensorRT signals; Snapdragon path requires replacement or ONNX conversion.
