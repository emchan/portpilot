# AllTalk-TTS — portability analysis

- **Package name:** AllTalk-TTS v2 (`AllTalk-TTS`)
- **Description:** [NVIDIA ONLY] AllTalk-TTS is a unified UI for E5-TTS, XTTS, Vite TTS, Piper TTS, Parler TTS and RVC, based on CoquiTTS, including a finetune mode.
- **Original git URL:** https://github.com/pinokiofactory/AllTalk-TTS
- **Analyzed commit:** `7b6ed78e5a661eeafccdf446f0772be475390a5c`
- **Platforms supported:** NVIDIA only
- **Porting difficulty:** Medium–high
- **CUDA-only packages:** deepspeed, xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

cxx-compiler, deepspeed, espeak-ng, faiss-cpu, fastapi, ffmpeg, gcc, gfortran-osx-arm64, git-lfs, gradio, libaio-dev, numpy, pydantic, torch, torch-directml, torchaudio, torchvision, xformers

Wheel indexes referenced: cpu, cu121, rocm6.0.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 429
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- Explicit platform tag found: NVIDIA only.
- `torch.js` routes present: nvidia, amd, mac, cpu.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): xformers
- Difficulty score: 5.5 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- retested on Python 3.10; standalone requirements installation hung/timed out.
- Result: **not runnable in this container.**
<!-- cross-analysis:start -->
## Cross-analysis details

- **CPU category (cpu.md):** CPU-capable with shipped fallback
- **TPU suitability:** Difficult - significant port
- **TPU work needed:** replace CUDA attention kernels with TPU-compatible attention/SDPA/XLA; DeepSpeed training/runtime path is CUDA-oriented; multiple CUDA-specific dependencies or large model/dtype constraints
- **Effort ranking (effort.md):** #67 — Medium–high
- **Effort blockers:** GPU-only attention: xformers; GPU runtime: deepspeed
- **Precisions noted:** unspecified
- **Models/flows noted:** —
- **Flow graph:** [flows/AllTalk-TTS.md](../flows/AllTalk-TTS.md)

### Snapshot verification (cloned analyzed commit)

- **Snapshot source:** `https://codeload.github.com/pinokiofactory/AllTalk-TTS/tar.gz/<analyzed commit>` extracted to `/tmp/opencode/pinokio-snapshots/AllTalk-TTS`
- **Files scanned:** 9 total (0 .py, 7 .js, 2 other)
- **Key files present:** pinokio.js, install.js, torch.js, start.js
- **TPU/CUDA-relevant signals:**
  - `xformers`: 4 match(es) (e.g. torch.js:10, torch.js:10)
  - `deepspeed`: 3 match(es) (e.g. install.js:69, install.js:69)
  - `directml`: 1 match(es) (e.g. torch.js:20)

### Evidence from analysis files

| Source | Evidence |
|---|---|
| [kernels.md](../analysis/kernels.md) | No per-repo kernel table row matched; see kernels.md for global signals. |
| [quantization.md](../analysis/quantization.md) | No per-repo quantization table row matched; see quantization.md. |
| [fusion.md](../analysis/fusion.md) | No direct fusion table row matched; see fusion.md for global context. |
| [models.md](../analysis/models.md) | No model pull/shape row matched in models.md. |
| [cpu.md](../analysis/cpu.md) | CPU category: **CPU-capable with shipped fallback** |
| [tpu.md](../analysis/tpu.md) | TPU suitability: **Difficult - significant port** — replace CUDA attention kernels with TPU-compatible attention/SDPA/XLA; DeepSpeed training/runtime path is CUDA-oriented; multiple CUDA-specific dependencies or large model/dtype constraints |

### Related analysis

- [CPU analysis](../analysis/cpu.md)
- [TPU analysis](../analysis/tpu.md)
- [Effort ranking](../analysis/effort.md)
- [Kernel evidence](../analysis/kernels.md)
- [Quantization evidence](../analysis/quantization.md)
- [Fusion evidence](../analysis/fusion.md)
- [Model pulls/shapes](../analysis/models.md)
- [Flow graphs](../analysis/flows.md)
- [App flow graph](../flows/AllTalk-TTS.md)
<!-- cross-analysis:end -->

## Snapdragon evaluation (deep clone)
- **Clone/scan status:** cloned and scanned
- **Files scanned:** 9 total (0 .py, 7 .js/.ts, 2 other)
- **Snapdragon-relevant signals:** torch=11, xformers=2, directml=1
- **Example evidence:**
  - torch: `install.js:72`
  - xformers: `torch.js:10`
  - directml: `torch.js:20`
- **Snapdragon verdict:** No Python GEMM in wrapper; Snapdragon CPU-ready as launcher/wrapper (no model port).
