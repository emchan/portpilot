# ovis — portability analysis

- **Package name:** Ovis-Image 7B (`ovis`)
- **Description:** Generate text-accurate images with the official Ovis-Image-7B diffusers pipeline.
- **Original git URL:** https://github.com/pinokiofactory/ovis
- **Analyzed commit:** `00a570258ba7370090037bb14bcfa67e1e81194e`
- **Platforms supported:** NVIDIA only
- **Porting difficulty:** Medium
- **CUDA-only packages:** torch (CUDA wheel)

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

accelerate, gradio, huggingface-hub, numpy, pillow, safetensors, sentencepiece, torch, torchaudio, torchvision, transformers

Requirements files: `app/requirements.txt`.

Third-party Python imports detected in local source: diffusers, gradio, torch.

Wheel indexes referenced: cpu, cu121, cu124, rocm6.0.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 383
- **CUDA-related functions used:** `torch.cuda.is_available`

## Evidence and notes

- `torch.js` routes present: none.
- Requirements from: app/requirements.txt
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Difficulty score: 4.0 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- dependencies installed and app.py imported successfully on CPU.
- Result: **CPU port imports successfully.**

## CPU port attempt

- **Attempt order:** #60 of 101 (by porting effort, easiest first).
- **Status:** CPU-capable (shipped fallback).
- **Changes applied / required:** use existing CPU wheel branch in torch.js; use existing non-NVIDIA/non-AMD branch in torch.js; use existing non-GPU launcher route; keep explicit device='cpu' branch; replace direct torch.cuda calls with devicetorch or cpu fallback; replace CUDA-only torch wheel with CPU wheel; +1.
- **Smoke check:** pass (1/1 files).
- **Blockers:** CUDA-only torch wheel; direct torch.cuda calls; MPS branch Apple-only.
- **Scope note:** static portability review of the Pinokio wrapper; no install or model download was executed.
<!-- cross-analysis:start -->
## Cross-analysis details

- **CPU category (cpu.md):** CPU-capable with shipped fallback
- **TPU suitability:** Difficult - significant port
- **TPU work needed:** remove direct torch.cuda device assumptions; replace CUDA torch wheel with TPU-supported runtime; MPS-specific branch irrelevant on TPU; keep device abstraction clean; multiple CUDA-specific dependencies or large model/dtype constraints
- **Effort ranking (effort.md):** #60 — Medium–high
- **Effort blockers:** CUDA-only torch wheel; direct `torch.cuda` calls; MPS branch is Apple-only
- **Precisions noted:** FP32, FP16, BF16
- **Models/flows noted:** [AIDC-AI/Ovis-Image-7B](https://huggingface.co/AIDC-AI/Ovis-Image-7B)
- **Flow graph:** [flows/ovis.md](../flows/ovis.md)

### Snapshot verification (cloned analyzed commit)

- **Snapshot source:** `https://codeload.github.com/pinokiofactory/ovis/tar.gz/<analyzed commit>` extracted to `/tmp/opencode/pinokio-snapshots/ovis`
- **Files scanned:** 10 total (1 .py, 5 .js, 4 other)
- **Key files present:** pinokio.js, install.js, start.js
- **TPU/CUDA-relevant signals:**
  - `torch_cuda`: 4 match(es) (e.g. app/app.py:19, app/app.py:27)
  - `mps`: 22 match(es) (e.g. README.md:11, README.md:11)

### Evidence from analysis files

| Source | Evidence |
|---|---|
| [kernels.md](../analysis/kernels.md) | `\| [ovis](https://github.com/pinokiofactory/ovis) \| [00a5702](https://github.com/pinokiofactory/ovis/commit/00a570258ba7370090037bb14bcfa67e1e81194e) \| direct code \| [README.md:11](https://github.com/pinokiofactory/ovis/blob/00a570258ba7370090037bb14bcfa67e1e81194e/README.md#L11) — - Works on NVIDIA CUDA (fastest), Apple MPS, and CPU. CPU/MPS will be extremely slow and may OOM on modest hardware; the app auto-detects (prefers MPS on macOS, o...<br>[README.md:25](https://github.com/pinokiofactory/ovis/blob/00a570258ba7370090037bb14bcfa67e1e81194e/README.md#L25) — - `Device` (`auto`, `cuda`, `mps`, `cpu`) \|` |
| [quantization.md](../analysis/quantization.md) | `\| [ovis](https://github.com/pinokiofactory/ovis) \| [00a5702](https://github.com/pinokiofactory/ovis/commit/00a570258ba7370090037bb14bcfa67e1e81194e) \| [74](https://github.com/pinokiofactory/ovis/blob/00a570258ba7370090037bb14bcfa67e1e81194e/README.md#L74) \| bfloat16 / BF16, float16 / FP16, float / FP32 \| checkpoint / config \| - The launcher uses the official `OvisImagePipeline` from the diffusers `ovis-image` branch and picks device/dtype automatically (CU... \|` |
| [quantization.md](../analysis/quantization.md) | `\| [ovis](https://github.com/pinokiofactory/ovis) \| [00a5702](https://github.com/pinokiofactory/ovis/commit/00a570258ba7370090037bb14bcfa67e1e81194e) \| [36](https://github.com/pinokiofactory/ovis/blob/00a570258ba7370090037bb14bcfa67e1e81194e/app/app.py#L36) \| bfloat16 / BF16 \| dtype declaration \| return torch.bfloat16 \|` |
| [quantization.md](../analysis/quantization.md) | `\| [ovis](https://github.com/pinokiofactory/ovis) \| [00a5702](https://github.com/pinokiofactory/ovis/commit/00a570258ba7370090037bb14bcfa67e1e81194e) \| [38](https://github.com/pinokiofactory/ovis/blob/00a570258ba7370090037bb14bcfa67e1e81194e/app/app.py#L38) \| float16 / FP16 \| dtype declaration \| return torch.float16 \|` |
| [quantization.md](../analysis/quantization.md) | `\| [ovis](https://github.com/pinokiofactory/ovis) \| [00a5702](https://github.com/pinokiofactory/ovis/commit/00a570258ba7370090037bb14bcfa67e1e81194e) \| [39](https://github.com/pinokiofactory/ovis/blob/00a570258ba7370090037bb14bcfa67e1e81194e/app/app.py#L39) \| float / FP32 \| dtype declaration \| return torch.float32 \|` |
| [quantization.md](../analysis/quantization.md) | `\| [ovis](https://github.com/pinokiofactory/ovis) \| [00a5702](https://github.com/pinokiofactory/ovis/commit/00a570258ba7370090037bb14bcfa67e1e81194e) \| [78](https://github.com/pinokiofactory/ovis/blob/00a570258ba7370090037bb14bcfa67e1e81194e/app/app.py#L78) \| float / FP32 \| dtype declaration \| true_cfg_scale=float(cfg_scale), \|` |
| [fusion.md](../analysis/fusion.md) | No direct fusion table row matched; see fusion.md for global context. |
| [models.md](../analysis/models.md) | No model pull/shape row matched in models.md. |
| [cpu.md](../analysis/cpu.md) | CPU category: **CPU-capable with shipped fallback** |
| [tpu.md](../analysis/tpu.md) | TPU suitability: **Difficult - significant port** — remove direct torch.cuda device assumptions; replace CUDA torch wheel with TPU-supported runtime; MPS-specific branch irrelevant on TPU; keep device abstraction clean; multiple CUDA-specific dependencies or large model/dtype constraints |

### Related analysis

- [CPU analysis](../analysis/cpu.md)
- [TPU analysis](../analysis/tpu.md)
- [Effort ranking](../analysis/effort.md)
- [Kernel evidence](../analysis/kernels.md)
- [Quantization evidence](../analysis/quantization.md)
- [Fusion evidence](../analysis/fusion.md)
- [Model pulls/shapes](../analysis/models.md)
- [Flow graphs](../analysis/flows.md)
- [App flow graph](../flows/ovis.md)
<!-- cross-analysis:end -->
