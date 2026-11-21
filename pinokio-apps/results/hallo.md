# hallo — portability analysis

- **Package name:** hallo (`hallo`)
- **Description:** [NVIDIA Only] Hierarchical Audio-Driven Visual Synthesis for Portrait Image Animation https://github.com/fudan-generative-vision/hallo
- **Original git URL:** https://github.com/pinokiofactory/hallo
- **Analyzed commit:** `c72097c6c23be58e7435bc48fbe9d0be5d0da1e5`
- **Platforms supported:** NVIDIA only
- **Porting difficulty:** Medium–high
- **CUDA-only packages:** bitsandbytes, xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

accelerate, audio-separator, av, bitsandbytes, decord, devicetorch, diffusers, einops, eva-decord, gradio, hf-xet, huggingface-hub, insightface, install, isort, librosa, mediapipe, mlflow, moviepy, numpy, omegaconf, onnx, onnx2torch, onnxruntime, opencv-contrib-python, opencv-python, opencv-python-headless, pillow, pre-commit, pylint, setuptools, torch, torch-directml, torchaudio, torchvision, tqdm, transformers, xformers

Requirements files: `requirements.txt`.

Wheel indexes referenced: cpu, cu128, rocm6.3.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 296
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- Explicit platform tag found: NVIDIA only.
- `torch.js` routes present: nvidia, amd, mac, cpu.
- Requirements from: requirements.txt
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): xformers
- Difficulty score: 6.0 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- retested on Python 3.10 with gcc; dependencies installed and hallo imported successfully on CPU.
- Result: **CPU port imports successfully.**
<!-- cross-analysis:start -->
## Cross-analysis details

- **CPU category (cpu.md):** CPU-capable with shipped fallback
- **TPU suitability:** Difficult - significant port
- **TPU work needed:** replace CUDA attention kernels with TPU-compatible attention/SDPA/XLA; NF4/bitsandbytes quantization needs dequant/upcast or TPU-supported path; multiple CUDA-specific dependencies or large model/dtype constraints
- **Effort ranking (effort.md):** #74 — Medium–high
- **Effort blockers:** GPU-only attention: xformers; GPU quantisers: bitsandbytes
- **Precisions noted:** FP32
- **Models/flows noted:** [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo)
- **Flow graph:** [flows/hallo.md](../flows/hallo.md)

### Snapshot verification (cloned analyzed commit)

- **Snapshot source:** `https://codeload.github.com/pinokiofactory/hallo/tar.gz/<analyzed commit>` extracted to `/tmp/opencode/pinokio-snapshots/hallo`
- **Files scanned:** 11 total (0 .py, 7 .js, 4 other)
- **Key files present:** pinokio.js, install.js, torch.js, start.js, requirements.txt
- **TPU/CUDA-relevant signals:**
  - `xformers`: 6 match(es) (e.g. requirements.txt:32, torch.js:10)
  - `bitsandbytes`: 2 match(es) (e.g. requirements.txt:4, requirements.txt:5)
  - `directml`: 1 match(es) (e.g. torch.js:20)

### Evidence from analysis files

| Source | Evidence |
|---|---|
| [kernels.md](../analysis/kernels.md) | No per-repo kernel table row matched; see kernels.md for global signals. |
| [quantization.md](../analysis/quantization.md) | `\| [hallo](https://github.com/pinokiofactory/hallo) \| requirements \| `requirements.txt:4` — #bitsandbytes==0.43.1<br>`requirements.txt:5` — bitsandbytes \|` |
| [fusion.md](../analysis/fusion.md) | `\| [hallo](https://github.com/pinokiofactory/hallo) \| [c72097c](https://github.com/pinokiofactory/hallo/commit/c72097c6c23be58e7435bc48fbe9d0be5d0da1e5) \| 30 \| `to_q.weight` / `to_k.weight` / `to_v.weight` in `down_blocks.0.attentions.0.transformer_blocks.0.attn1` (fudan-generative-ai/hallo, B=`[320, 320]`) \| [`hallo.md`](../flows/hallo.md) \|` |
| [fusion.md](../analysis/fusion.md) | `\| [hallo](https://github.com/pinokiofactory/hallo) \| [c72097c](https://github.com/pinokiofactory/hallo/commit/c72097c6c23be58e7435bc48fbe9d0be5d0da1e5) \| 3 \| none \| [`hallo.md`](../flows/hallo.md) \|` |
| [fusion.md](../analysis/fusion.md) | `\| [hallo](https://github.com/pinokiofactory/hallo) \| [c72097c](https://github.com/pinokiofactory/hallo/commit/c72097c6c23be58e7435bc48fbe9d0be5d0da1e5) \| 162 \| 0 \|` |
| [models.md](../analysis/models.md) | No model pull/shape row matched in models.md. |
| [cpu.md](../analysis/cpu.md) | CPU category: **CPU-capable with shipped fallback** |
| [tpu.md](../analysis/tpu.md) | TPU suitability: **Difficult - significant port** — replace CUDA attention kernels with TPU-compatible attention/SDPA/XLA; NF4/bitsandbytes quantization needs dequant/upcast or TPU-supported path; multiple CUDA-specific dependencies or large model/dtype constraints |

### Related analysis

- [CPU analysis](../analysis/cpu.md)
- [TPU analysis](../analysis/tpu.md)
- [Effort ranking](../analysis/effort.md)
- [Kernel evidence](../analysis/kernels.md)
- [Quantization evidence](../analysis/quantization.md)
- [Fusion evidence](../analysis/fusion.md)
- [Model pulls/shapes](../analysis/models.md)
- [Flow graphs](../analysis/flows.md)
- [App flow graph](../flows/hallo.md)
<!-- cross-analysis:end -->
