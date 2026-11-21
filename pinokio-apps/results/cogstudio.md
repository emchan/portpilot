# cogstudio — portability analysis

- **Package name:** CogStudio (`cogstudio`)
- **Description:** [NVIDIA ONLY] Advanced Web UI for CogVideo (text to video, image to video, video to video, extend video, etc) -- Generate videos with less than 10GB VRAM
- **Original git URL:** https://github.com/pinokiofactory/cogstudio
- **Analyzed commit:** `7dfb014a636513c5b42de070c43e285c9bf7cce7`
- **Platforms supported:** NVIDIA only
- **Porting difficulty:** Medium
- **CUDA-only packages:** xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

diffusers, gradio, hf-xet, moviepy, numpy, protobuf, tiktoken, torch, torchaudio, torchvision, tqdm, transformers, xformers

Requirements files: `requirements.txt`.

Third-party Python imports detected in local source: cv2, diffusers, gradio, huggingface-hub, imageio-ffmpeg, moviepy, openai, pil, rife-model, torch, utils.

Wheel indexes referenced: cu128, rocm6.3.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 1147
- **CUDA-related functions used:** `torch.cuda.empty_cache`, `torch.cuda.is_available`

## Evidence and notes

- Explicit platform tag found: NVIDIA only.
- `torch.js` routes present: nvidia, amd.
- Requirements from: requirements.txt
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): xformers
- Difficulty score: 4.5 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- dependencies installed and cogstudio imported successfully on CPU (with warnings).
- Result: **CPU port imports successfully.**

## CPU port attempt

- **Attempt order:** #63 of 101 (by porting effort, easiest first).
- **Status:** CPU-capable (shipped fallback).
- **Changes applied / required:** use existing non-GPU launcher route; keep explicit device='cpu' branch; replace direct torch.cuda calls with devicetorch or cpu fallback; substitute GPU-only attention libs with SDPA math backend; tune oneDNN/MKL threads for FP16/BF16 GEMMs.
- **Smoke check:** pass (1/1 files).
- **Blockers:** GPU-only attention: xformers; direct torch.cuda calls.
- **Scope note:** static portability review of the Pinokio wrapper; no install or model download was executed.
<!-- cross-analysis:start -->
## Cross-analysis details

- **CPU category (cpu.md):** CPU-capable with shipped fallback
- **TPU suitability:** Difficult - significant port
- **TPU work needed:** replace CUDA attention kernels with TPU-compatible attention/SDPA/XLA; remove direct torch.cuda device assumptions; large BF16/FP16 GEMM workload; expect XLA compile/memory tuning; multiple CUDA-specific dependencies or large model/dtype constraints
- **Effort ranking (effort.md):** #63 — Medium–high
- **Effort blockers:** GPU-only attention: xformers; direct `torch.cuda` calls; large FP16/BF16 GEMM load
- **Precisions noted:** FP16, BF16
- **Models/flows noted:** [AlexWortega/RIFE](https://huggingface.co/AlexWortega/RIFE), [THUDM/CogVideoX-2B](https://huggingface.co/THUDM/CogVideoX-2B), [THUDM/CogVideoX-5b-I2V](https://huggingface.co/THUDM/CogVideoX-5b-I2V), [ai-forever/Real-ESRGAN](https://huggingface.co/ai-forever/Real-ESRGAN)
- **Flow graph:** [flows/cogstudio.md](../flows/cogstudio.md)

### Snapshot verification (cloned analyzed commit)

- **Snapshot source:** `https://codeload.github.com/pinokiofactory/cogstudio/tar.gz/<analyzed commit>` extracted to `/tmp/opencode/pinokio-snapshots/cogstudio`
- **Files scanned:** 19 total (1 .py, 7 .js, 11 other)
- **Key files present:** pinokio.js, install.js, torch.js, start.js, requirements.txt
- **TPU/CUDA-relevant signals:**
  - `torch_cuda`: 7 match(es) (e.g. cogstudio.py:41, cogstudio.py:41)
  - `xformers`: 5 match(es) (e.g. torch.js:10, torch.js:10)

### Evidence from analysis files

| Source | Evidence |
|---|---|
| [kernels.md](../analysis/kernels.md) | No per-repo kernel table row matched; see kernels.md for global signals. |
| [quantization.md](../analysis/quantization.md) | `\| [cogstudio](https://github.com/pinokiofactory/cogstudio) \| [7dfb014](https://github.com/pinokiofactory/cogstudio/commit/7dfb014a636513c5b42de070c43e285c9bf7cce7) \| [62](https://github.com/pinokiofactory/cogstudio/blob/7dfb014a636513c5b42de070c43e285c9bf7cce7/cogstudio.py#L62) \| bfloat16 / BF16 \| dtype declaration \| if dtype_str == "bfloat16": \|` |
| [quantization.md](../analysis/quantization.md) | `\| [cogstudio](https://github.com/pinokiofactory/cogstudio) \| [7dfb014](https://github.com/pinokiofactory/cogstudio/commit/7dfb014a636513c5b42de070c43e285c9bf7cce7) \| [63](https://github.com/pinokiofactory/cogstudio/blob/7dfb014a636513c5b42de070c43e285c9bf7cce7/cogstudio.py#L63) \| bfloat16 / BF16 \| dtype declaration \| dtype = torch.bfloat16 \|` |
| [quantization.md](../analysis/quantization.md) | `\| [cogstudio](https://github.com/pinokiofactory/cogstudio) \| [7dfb014](https://github.com/pinokiofactory/cogstudio/commit/7dfb014a636513c5b42de070c43e285c9bf7cce7) \| [64](https://github.com/pinokiofactory/cogstudio/blob/7dfb014a636513c5b42de070c43e285c9bf7cce7/cogstudio.py#L64) \| float16 / FP16 \| dtype declaration \| elif dtype_str == "float16": \|` |
| [quantization.md](../analysis/quantization.md) | `\| [cogstudio](https://github.com/pinokiofactory/cogstudio) \| [7dfb014](https://github.com/pinokiofactory/cogstudio/commit/7dfb014a636513c5b42de070c43e285c9bf7cce7) \| [65](https://github.com/pinokiofactory/cogstudio/blob/7dfb014a636513c5b42de070c43e285c9bf7cce7/cogstudio.py#L65) \| float16 / FP16 \| dtype declaration \| dtype = torch.float16 \|` |
| [quantization.md](../analysis/quantization.md) | `\| [cogstudio](https://github.com/pinokiofactory/cogstudio) \| [7dfb014](https://github.com/pinokiofactory/cogstudio/commit/7dfb014a636513c5b42de070c43e285c9bf7cce7) \| [111](https://github.com/pinokiofactory/cogstudio/blob/7dfb014a636513c5b42de070c43e285c9bf7cce7/cogstudio.py#L111) \| bfloat16 / BF16 \| dtype declaration \| if dtype_str == "bfloat16": \|` |
| [quantization.md](../analysis/quantization.md) | `\| [cogstudio](https://github.com/pinokiofactory/cogstudio) \| [7dfb014](https://github.com/pinokiofactory/cogstudio/commit/7dfb014a636513c5b42de070c43e285c9bf7cce7) \| [112](https://github.com/pinokiofactory/cogstudio/blob/7dfb014a636513c5b42de070c43e285c9bf7cce7/cogstudio.py#L112) \| bfloat16 / BF16 \| dtype declaration \| dtype = torch.bfloat16 \|` |
| [quantization.md](../analysis/quantization.md) | `\| [cogstudio](https://github.com/pinokiofactory/cogstudio) \| [7dfb014](https://github.com/pinokiofactory/cogstudio/commit/7dfb014a636513c5b42de070c43e285c9bf7cce7) \| [113](https://github.com/pinokiofactory/cogstudio/blob/7dfb014a636513c5b42de070c43e285c9bf7cce7/cogstudio.py#L113) \| float16 / FP16 \| dtype declaration \| elif dtype_str == "float16": \|` |
| [quantization.md](../analysis/quantization.md) | `\| [cogstudio](https://github.com/pinokiofactory/cogstudio) \| [7dfb014](https://github.com/pinokiofactory/cogstudio/commit/7dfb014a636513c5b42de070c43e285c9bf7cce7) \| [114](https://github.com/pinokiofactory/cogstudio/blob/7dfb014a636513c5b42de070c43e285c9bf7cce7/cogstudio.py#L114) \| float16 / FP16 \| dtype declaration \| dtype = torch.float16 \|` |
| [quantization.md](../analysis/quantization.md) | *4 more rows omitted* |
| [fusion.md](../analysis/fusion.md) | `\| [cogstudio](https://github.com/pinokiofactory/cogstudio) \| [7dfb014](https://github.com/pinokiofactory/cogstudio/commit/7dfb014a636513c5b42de070c43e285c9bf7cce7) \| 97 \| `to_q.weight` / `to_k.weight` / `to_v.weight` in `transformer_blocks.0.attn1` (THUDM/CogVideoX-2B, B=`[1920, 1920]`) \| [`cogstudio.md`](../flows/cogstudio.md) \|` |
| [fusion.md](../analysis/fusion.md) | `\| [cogstudio](https://github.com/pinokiofactory/cogstudio) \| [7dfb014](https://github.com/pinokiofactory/cogstudio/commit/7dfb014a636513c5b42de070c43e285c9bf7cce7) \| 6 \| none \| [`cogstudio.md`](../flows/cogstudio.md) \|` |
| [fusion.md](../analysis/fusion.md) | `\| [cogstudio](https://github.com/pinokiofactory/cogstudio) \| [7dfb014](https://github.com/pinokiofactory/cogstudio/commit/7dfb014a636513c5b42de070c43e285c9bf7cce7) \| 397 \| [`cogstudio.md`](../flows/cogstudio.md) \|` |
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
- [App flow graph](../flows/cogstudio.md)
<!-- cross-analysis:end -->
