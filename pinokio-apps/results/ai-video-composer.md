# ai-video-composer — portability analysis

- **Package name:** ai-video-composer (`ai-video-composer`)
- **Description:** The ultimate video editor powered by natural language and FFMPEG https://huggingface.co/spaces/huggingface-projects/ai-video-composer
- **Original git URL:** https://github.com/pinokiofactory/ai-video-composer
- **Analyzed commit:** `0cc7921ff899b4d8ce6e5b8f419f9144e50fa43d`
- **Platforms supported:** Cross-platform
- **Porting difficulty:** Low
- **CUDA-only packages:** —

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

huggingface-hub, pydantic

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 198
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- `torch.js` routes present: none.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Difficulty score: 0.0 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- Installed on Python 3.12 with huggingface_hub==0.25.2; Gradio server launched on CPU (proxy/share limitation only).
- Result: **CPU port works with dependency/version fixes.**
<!-- cross-analysis:start -->
## Cross-analysis details

- **CPU category (cpu.md):** CPU-native / no local GEMM
- **TPU suitability:** Irrelevant - no local GEMM workload
- **TPU work needed:** No local GEMM/model workload; TPU gives no acceleration benefit
- **Effort ranking (effort.md):** #1 — Low
- **Effort blockers:** none — no local GEMM workload
- **Precisions noted:** unspecified
- **Models/flows noted:** —
- **Flow graph:** [flows/ai-video-composer.md](../flows/ai-video-composer.md)

### Snapshot verification (cloned analyzed commit)

- **Snapshot source:** `https://codeload.github.com/pinokiofactory/ai-video-composer/tar.gz/<analyzed commit>` extracted to `/tmp/opencode/pinokio-snapshots/ai-video-composer`
- **Files scanned:** 12 total (0 .py, 6 .js, 6 other)
- **Key files present:** pinokio.js, install.js, start.js
- **TPU/CUDA-relevant signals:** none detected by text scan (still inspect runtime behavior before porting)

### Evidence from analysis files

| Source | Evidence |
|---|---|
| [kernels.md](../analysis/kernels.md) | No per-repo kernel table row matched; see kernels.md for global signals. |
| [quantization.md](../analysis/quantization.md) | No per-repo quantization table row matched; see quantization.md. |
| [fusion.md](../analysis/fusion.md) | No direct fusion table row matched; see fusion.md for global context. |
| [models.md](../analysis/models.md) | No model pull/shape row matched in models.md. |
| [cpu.md](../analysis/cpu.md) | CPU category: **CPU-native / no local GEMM** |
| [tpu.md](../analysis/tpu.md) | TPU suitability: **Irrelevant - no local GEMM workload** — No local GEMM/model workload; TPU gives no acceleration benefit |

### Related analysis

- [CPU analysis](../analysis/cpu.md)
- [TPU analysis](../analysis/tpu.md)
- [Effort ranking](../analysis/effort.md)
- [Kernel evidence](../analysis/kernels.md)
- [Quantization evidence](../analysis/quantization.md)
- [Fusion evidence](../analysis/fusion.md)
- [Model pulls/shapes](../analysis/models.md)
- [Flow graphs](../analysis/flows.md)
- [App flow graph](../flows/ai-video-composer.md)
<!-- cross-analysis:end -->

## Snapdragon evaluation (deep clone)

- **Cloned snapshot:** yes (shallow clone of `main` tip); no Python source present in wrapper repo.
- **Snapdragon CPU:** Ready (no local GEMM; normal ARM64 Python app).
- **Snapdragon GPU (Adreno):** N/A (no local model to convert).
- **Snapdragon NPU (Hexagon):** N/A (no local model to convert).
- **Deep findings:** No `torch.cuda`, Triton, TensorRT, xformers, bitsandbytes, MLX or ONNX Runtime GPU signals in launcher files; compute is delegated upstream. No dependency/version blocker specific to ARM64 beyond standard Node/Python launcher tooling.
