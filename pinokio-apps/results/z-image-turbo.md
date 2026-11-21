# z-image-turbo — portability analysis

- **Package name:** Z-Image-Turbo (`z-image-turbo`)
- **Description:** Simple Gradio app for generating images with Tongyi-MAI/Z-Image-Turbo.
- **Original git URL:** https://github.com/pinokiofactory/z-image-turbo
- **Analyzed commit:** `54899fdb5c023072de43c8b91ad2b0f0bee5b5c4`
- **Platforms supported:** NVIDIA / AMD / Mac
- **Porting difficulty:** High
- **CUDA-only packages:** flash-attn, sageattention *(optional)*, triton *(optional)*, triton-windows, xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

accelerate, diffusers, fastapi, flash-attn, gradio, huggingface-hub, numpy, pillow, pydantic, safetensors, sageattention, torch, torch-directml, torchaudio, torchvision, transformers, triton, triton-windows, xformers

Requirements files: `app/requirements.txt`.

Third-party Python imports detected in local source: diffusers, gradio, torch.

Wheel indexes referenced: cpu, cu128, rocm6.3.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 361
- **CUDA-related functions used:** `torch.cuda.is_available`

## Evidence and notes

- `torch.js` routes present: nvidia, amd, mac, cpu.
- Requirements from: app/requirements.txt
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): sageattention, triton, xformers
- Difficulty score: 7.8 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- Installed CPU torch + dependencies; patched moviepy import.
-  succeeded.
- Result: **CPU port imports successfully (model not downloaded).**

## CPU port attempt

- **Attempt order:** #84 of 101 (by porting effort, easiest first).
- **Status:** CPU-capable (shipped fallback).
- **Changes applied / required:** use existing CPU wheel branch in torch.js; use existing non-GPU launcher route; keep explicit device='cpu' branch; replace direct torch.cuda calls with devicetorch or cpu fallback; disable fused GPU kernels (xformers/flash/sage) in config; substitute GPU-only attention libs with SDPA math backend; +2.
- **Smoke check:** pass (1/1 files).
- **Blockers:** GPU-only attention: flash-attn/sageattention/triton/triton-windows/xformers; direct torch.cuda calls; CUDA-only fused kernels; MPS branch Apple-only.
- **Scope note:** static portability review of the Pinokio wrapper; no install or model download was executed.
<!-- cross-analysis:start -->
## Cross-analysis details

- **CPU category (cpu.md):** CPU-capable with shipped fallback
- **TPU suitability:** Difficult - significant port
- **TPU work needed:** replace CUDA attention kernels with TPU-compatible attention/SDPA/XLA; remove direct torch.cuda device assumptions; large BF16/FP16 GEMM workload; expect XLA compile/memory tuning; MPS-specific branch irrelevant on TPU; keep device abstraction clean; multiple CUDA-specific dependencies or large model/dtype constraints
- **Effort ranking (effort.md):** #84 — High
- **Effort blockers:** GPU-only attention: flash-attn/sageattention/triton/triton-windows/xformers; direct `torch.cuda` calls; CUDA-only fused kernels need config change; large FP16/BF16 GEMM load; MPS branch is Apple-only
- **Precisions noted:** FP32, BF16
- **Models/flows noted:** [Tongyi-MAI/Z-Image-Turbo](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo)
- **Flow graph:** [flows/z-image-turbo.md](../flows/z-image-turbo.md)

### Snapshot verification (cloned analyzed commit)

- **Snapshot source:** `https://codeload.github.com/pinokiofactory/z-image-turbo/tar.gz/<analyzed commit>` extracted to `/tmp/opencode/pinokio-snapshots/z-image-turbo`
- **Files scanned:** 12 total (1 .py, 6 .js, 5 other)
- **Key files present:** pinokio.js, install.js, torch.js, start.js
- **TPU/CUDA-relevant signals:**
  - `torch_cuda`: 2 match(es) (e.g. app/app.py:30, app/app.py:72)
  - `xformers`: 4 match(es) (e.g. torch.js:11, torch.js:11)
  - `flash_attn`: 2 match(es) (e.g. torch.js:14, torch.js:30)
  - `sageattention`: 4 match(es) (e.g. torch.js:13, torch.js:13)
  - `triton`: 4 match(es) (e.g. torch.js:12, torch.js:12)
  - `directml`: 1 match(es) (e.g. torch.js:42)
  - `mps`: 3 match(es) (e.g. app/app.py:28, app/app.py:28)

### Evidence from analysis files

| Source | Evidence |
|---|---|
| [kernels.md](../analysis/kernels.md) | `\| [z-image-turbo](https://github.com/pinokiofactory/z-image-turbo) \| [54899fd](https://github.com/pinokiofactory/z-image-turbo/commit/54899fdb5c023072de43c8b91ad2b0f0bee5b5c4) \| optional flag + launcher install \| torch.js \| [torch.js:12](https://github.com/pinokiofactory/z-image-turbo/blob/54899fdb5c023072de43c8b91ad2b0f0bee5b5c4/torch.js#L12) — "{{args && args.triton ? 'uv pip install triton-windows==3.3.1.post19' : ''}}", \|` |
| [kernels.md](../analysis/kernels.md) | `\| [z-image-turbo](https://github.com/pinokiofactory/z-image-turbo) \| [54899fd](https://github.com/pinokiofactory/z-image-turbo/commit/54899fdb5c023072de43c8b91ad2b0f0bee5b5c4) \| direct code \| [app/app.py:28](https://github.com/pinokiofactory/z-image-turbo/blob/54899fdb5c023072de43c8b91ad2b0f0bee5b5c4/app/app.py#L28) — if hasattr(torch.backends, "mps") and torch.backends.mps.is_available():<br>[app/app.py:29](https://github.com/pinokiofactory/z-image-turbo/blob/54899fdb5c023072de43c8b91ad2b0f0bee5b5c4/app/app.py#L29) — return "mps" \|` |
| [kernels.md](../analysis/kernels.md) | `\| [z-image-turbo](https://github.com/pinokiofactory/z-image-turbo) \| [54899fd](https://github.com/pinokiofactory/z-image-turbo/commit/54899fdb5c023072de43c8b91ad2b0f0bee5b5c4) \| optional flag + launcher install \| [torch.js:14](https://github.com/pinokiofactory/z-image-turbo/blob/54899fdb5c023072de43c8b91ad2b0f0bee5b5c4/torch.js#L14) — "{{args && args.flashattention ? 'uv pip install https://huggingface.co/cocktailpeanut/wheels/resolve/main/flash_attn-2.8.2%2Bcu128torch2.7-cp310-cp310-win_amd64....<br>[torch.js:30](https://github.com/pinokiofactory/z-image-turbo/blob/54899fdb5c023072de43c8b91ad2b0f0bee5b5c4/torch.js#L30) — "{{args && args.flashattention ? 'uv pip install https://huggingface.co/cocktailpeanut/wheels/resolve/main/flash_attn-2.8.3%2Bcu128torch2.7-cp310-cp310-linux_x86_... \|` |
| [kernels.md](../analysis/kernels.md) | `\| [z-image-turbo](https://github.com/pinokiofactory/z-image-turbo) \| [54899fd](https://github.com/pinokiofactory/z-image-turbo/commit/54899fdb5c023072de43c8b91ad2b0f0bee5b5c4) \| optional flag + launcher install \| [torch.js:13](https://github.com/pinokiofactory/z-image-turbo/blob/54899fdb5c023072de43c8b91ad2b0f0bee5b5c4/torch.js#L13) — "{{args && args.sageattention ? 'uv pip install https://huggingface.co/cocktailpeanut/wheels/resolve/main/sageattention-2.1.1%2Bcu128torch2.7.1-cp310-cp310-win_am...<br>[torch.js:29](https://github.com/pinokiofactory/z-image-turbo/blob/54899fdb5c023072de43c8b91ad2b0f0bee5b5c4/torch.js#L29) — "{{args && args.sageattention ? 'uv pip install https://huggingface.co/cocktailpeanut/wheels/resolve/main/sageattention-2.1.1%2Bcu128torch2.7.1-cp310-cp310-linux_... \|` |
| [quantization.md](../analysis/quantization.md) | `\| [z-image-turbo](https://github.com/pinokiofactory/z-image-turbo) \| [54899fd](https://github.com/pinokiofactory/z-image-turbo/commit/54899fdb5c023072de43c8b91ad2b0f0bee5b5c4) \| [44](https://github.com/pinokiofactory/z-image-turbo/blob/54899fdb5c023072de43c8b91ad2b0f0bee5b5c4/app/app.py#L44) \| bfloat16 / BF16 \| dtype declaration \| kwargs["torch_dtype"] = torch.bfloat16 \|` |
| [quantization.md](../analysis/quantization.md) | `\| [z-image-turbo](https://github.com/pinokiofactory/z-image-turbo) \| [54899fd](https://github.com/pinokiofactory/z-image-turbo/commit/54899fdb5c023072de43c8b91ad2b0f0bee5b5c4) \| [80](https://github.com/pinokiofactory/z-image-turbo/blob/54899fdb5c023072de43c8b91ad2b0f0bee5b5c4/app/app.py#L80) \| float / FP32 \| dtype declaration \| guidance_scale=float(guidance_scale), \|` |
| [fusion.md](../analysis/fusion.md) | `\| [z-image-turbo](https://github.com/pinokiofactory/z-image-turbo) \| [54899fd](https://github.com/pinokiofactory/z-image-turbo/commit/54899fdb5c023072de43c8b91ad2b0f0bee5b5c4) \| optional launcher flag \| [torch.js:13](https://github.com/pinokiofactory/z-image-turbo/blob/54899fdb5c023072de43c8b91ad2b0f0bee5b5c4/torch.js#L13) — `"{{args && args.sageattention ? 'uv pip install https://huggingface.co/cocktailpeanut/wheels/resolve/main/sageattention-2.1.1%2Bcu128torch2.7.1-cp310-` \|` |
| [fusion.md](../analysis/fusion.md) | `\| [z-image-turbo](https://github.com/pinokiofactory/z-image-turbo) \| [54899fd](https://github.com/pinokiofactory/z-image-turbo/commit/54899fdb5c023072de43c8b91ad2b0f0bee5b5c4) \| 108 \| [`z-image-turbo.md`](../flows/z-image-turbo.md) \|` |
| [models.md](../analysis/models.md) | No model pull/shape row matched in models.md. |
| [cpu.md](../analysis/cpu.md) | CPU category: **CPU-capable with shipped fallback** |
| [tpu.md](../analysis/tpu.md) | TPU suitability: **Difficult - significant port** — replace CUDA attention kernels with TPU-compatible attention/SDPA/XLA; remove direct torch.cuda device assumptions; large BF16/FP16 GEMM workload; expect XLA compile/memory tuning; MPS-specific branch irrelevant on TPU; keep device abstraction clean; multiple CUDA-specific dependencies or large model/dtype constraints |

### Related analysis

- [CPU analysis](../analysis/cpu.md)
- [TPU analysis](../analysis/tpu.md)
- [Effort ranking](../analysis/effort.md)
- [Kernel evidence](../analysis/kernels.md)
- [Quantization evidence](../analysis/quantization.md)
- [Fusion evidence](../analysis/fusion.md)
- [Model pulls/shapes](../analysis/models.md)
- [Flow graphs](../analysis/flows.md)
- [App flow graph](../flows/z-image-turbo.md)
<!-- cross-analysis:end -->
