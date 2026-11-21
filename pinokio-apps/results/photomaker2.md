# photomaker2 — portability analysis

- **Package name:** PhotoMaker2 (`photomaker2`)
- **Description:** Customizing Realistic Human Photos via Stacked ID Embedding https://huggingface.co/spaces/TencentARC/PhotoMaker-V2
- **Original git URL:** https://github.com/pinokiofactory/photomaker2
- **Analyzed commit:** `2c48cd3f30a305069aad6de30bfe4c3f0fe900f7`
- **Platforms supported:** NVIDIA / AMD / Mac
- **Porting difficulty:** Medium–high
- **CUDA-only packages:** cudnn, onnxruntime-gpu, xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

cudnn, devicetorch, gradio, huggingface-hub, numpy, onnxruntime, onnxruntime-directml, onnxruntime-gpu, onnxruntime-rocm, peft, torch, torch-directml, torchaudio, torchvision, transformers, xformers

Wheel indexes referenced: cpu, cu128, rocm6.3.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 316
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- `torch.js` routes present: nvidia, amd, mac, cpu.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): xformers
- Difficulty score: 5.0 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- retested on Python 3.10; blocked by torchvision 0.19.1 installation hang.
- Result: **not runnable in this container.**
<!-- cross-analysis:start -->
## Cross-analysis details

- **CPU category (cpu.md):** CPU-capable with shipped fallback
- **TPU suitability:** Difficult - significant port
- **TPU work needed:** replace CUDA attention kernels with TPU-compatible attention/SDPA/XLA; replace onnxruntime-gpu with TPU-compatible runtime; multiple CUDA-specific dependencies or large model/dtype constraints
- **Effort ranking (effort.md):** #66 — Medium–high
- **Effort blockers:** GPU-only attention: xformers; GPU runtime: cudnn/onnxruntime-gpu
- **Precisions noted:** unspecified
- **Models/flows noted:** —
- **Flow graph:** [flows/photomaker2.md](../flows/photomaker2.md)

### Snapshot verification (cloned analyzed commit)

- **Snapshot source:** `https://codeload.github.com/pinokiofactory/photomaker2/tar.gz/<analyzed commit>` extracted to `/tmp/opencode/pinokio-snapshots/photomaker2`
- **Files scanned:** 11 total (0 .py, 7 .js, 4 other)
- **Key files present:** pinokio.js, install.js, torch.js, start.js
- **TPU/CUDA-relevant signals:**
  - `xformers`: 5 match(es) (e.g. torch.js:11, torch.js:11)
  - `onnxruntime_gpu`: 2 match(es) (e.g. torch.js:12, torch.js:79)
  - `directml`: 2 match(es) (e.g. torch.js:25, torch.js:26)

### Evidence from analysis files

| Source | Evidence |
|---|---|
| [kernels.md](../analysis/kernels.md) | No per-repo kernel table row matched; see kernels.md for global signals. |
| [quantization.md](../analysis/quantization.md) | No per-repo quantization table row matched; see quantization.md. |
| [fusion.md](../analysis/fusion.md) | `\| [photomaker2](https://github.com/pinokiofactory/photomaker2) \| [2c48cd3](https://github.com/pinokiofactory/photomaker2/commit/2c48cd3f30a305069aad6de30bfe4c3f0fe900f7) \| [torch.js:12](https://github.com/pinokiofactory/photomaker2/blob/2c48cd3f30a305069aad6de30bfe4c3f0fe900f7/torch.js#L12) — `"uv pip install onnxruntime-gpu"` \| ONNX Runtime wheel installs (no session code in the launcher) \|` |
| [models.md](../analysis/models.md) | No model pull/shape row matched in models.md. |
| [cpu.md](../analysis/cpu.md) | CPU category: **CPU-capable with shipped fallback** |
| [tpu.md](../analysis/tpu.md) | TPU suitability: **Difficult - significant port** — replace CUDA attention kernels with TPU-compatible attention/SDPA/XLA; replace onnxruntime-gpu with TPU-compatible runtime; multiple CUDA-specific dependencies or large model/dtype constraints |

### Related analysis

- [CPU analysis](../analysis/cpu.md)
- [TPU analysis](../analysis/tpu.md)
- [Effort ranking](../analysis/effort.md)
- [Kernel evidence](../analysis/kernels.md)
- [Quantization evidence](../analysis/quantization.md)
- [Fusion evidence](../analysis/fusion.md)
- [Model pulls/shapes](../analysis/models.md)
- [Flow graphs](../analysis/flows.md)
- [App flow graph](../flows/photomaker2.md)
<!-- cross-analysis:end -->
