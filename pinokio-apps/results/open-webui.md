# open-webui — portability analysis

- **Package name:** Open WebUI (`open-webui`)
- **Description:** User-friendly WebUI for LLMs, supported LLM runners include Ollama and OpenAI-compatible APIs https://github.com/open-webui/open-webui
- **Original git URL:** https://github.com/pinokiofactory/open-webui
- **Analyzed commit:** `d7c59329e3758cac350a1b5f1b834038727bec6c`
- **Platforms supported:** Cross-platform
- **Porting difficulty:** Low
- **CUDA-only packages:** —

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

itsdangerous, onnxruntime, open-webui

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 269
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- `torch.js` routes present: none.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Difficulty score: 0.0 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- retested on Python 3.12; open-webui installation hung/timed out in this container.
- Result: **not runnable in this container.**
<!-- cross-analysis:start -->
## Cross-analysis details

- **CPU category (cpu.md):** CPU-native / no local GEMM
- **TPU suitability:** Irrelevant - no local GEMM workload
- **TPU work needed:** No local GEMM/model workload; TPU gives no acceleration benefit
- **Effort ranking (effort.md):** #9 — Low
- **Effort blockers:** none — no local GEMM workload
- **Precisions noted:** unspecified
- **Models/flows noted:** —
- **Flow graph:** [flows/open-webui.md](../flows/open-webui.md)

### Snapshot verification (cloned analyzed commit)

- **Snapshot source:** `https://codeload.github.com/pinokiofactory/open-webui/tar.gz/<analyzed commit>` extracted to `/tmp/opencode/pinokio-snapshots/open-webui`
- **Files scanned:** 13 total (0 .py, 7 .js, 6 other)
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
- [App flow graph](../flows/open-webui.md)
<!-- cross-analysis:end -->

## Snapdragon evaluation (deep clone)
- **Clone/scan status:** cloned and scanned
- **Files scanned:** 13 total (0 .py, 7 .js/.ts, 6 other)
 - **Snapdragon-relevant signals:** none detected by text scan
- **Snapdragon verdict:** No Python GEMM in wrapper; Snapdragon CPU-ready as launcher/wrapper (no model port).
