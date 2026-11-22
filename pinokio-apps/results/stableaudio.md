# stableaudio — portability analysis

- **Package name:** StableAudio (`stableaudio`)
- **Description:** An Open Source Model for Audio Samples and Sound Design https://github.com/Stability-AI/stable-audio-tools
- **Original git URL:** https://github.com/pinokiofactory/stableaudio
- **Analyzed commit:** `14c9fbb56ef0054d8fae55bcee825216d30be047`
- **Platforms supported:** NVIDIA / AMD / Mac
- **Porting difficulty:** Low
- **CUDA-only packages:** xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

devicetorch, gradio, hf-xet, libsndfile, numpy, soxr, torch, torch-directml, torchaudio, torchvision, xformers

Wheel indexes referenced: cpu, cu128, rocm6.3.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 324
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- `torch.js` routes present: nvidia, amd, mac, cpu.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): xformers
- Difficulty score: 0.5 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- retested on Python 3.10; stable_audio_tools imported, but run_gradio fails on torchvision::nms operator mismatch.
- Result: **not runnable in this container.**
<!-- cross-analysis:start -->
## Cross-analysis details

- **CPU category (cpu.md):** CPU-capable with shipped fallback
- **TPU suitability:** Possible - moderate port
- **TPU work needed:** replace CUDA attention kernels with TPU-compatible attention/SDPA/XLA; moderate device/kernel/runtime adaptation
- **Effort ranking (effort.md):** #36 — Low
- **Effort blockers:** GPU-only attention: xformers
- **Precisions noted:** unspecified
- **Models/flows noted:** —
- **Flow graph:** [flows/stableaudio.md](../flows/stableaudio.md)

### Snapshot verification (cloned analyzed commit)

- **Snapshot source:** `https://codeload.github.com/pinokiofactory/stableaudio/tar.gz/<analyzed commit>` extracted to `/tmp/opencode/pinokio-snapshots/stableaudio`
- **Files scanned:** 11 total (0 .py, 7 .js, 4 other)
- **Key files present:** pinokio.js, install.js, torch.js, start.js
- **TPU/CUDA-relevant signals:**
  - `xformers`: 5 match(es) (e.g. torch.js:10, torch.js:10)
  - `directml`: 1 match(es) (e.g. torch.js:21)

### Evidence from analysis files

| Source | Evidence |
|---|---|
| [kernels.md](../analysis/kernels.md) | No per-repo kernel table row matched; see kernels.md for global signals. |
| [quantization.md](../analysis/quantization.md) | No per-repo quantization table row matched; see quantization.md. |
| [fusion.md](../analysis/fusion.md) | `\| [rc-stableaudio](https://github.com/pinokiofactory/rc-stableaudio) \| [b3a7d5a](https://github.com/pinokiofactory/rc-stableaudio/commit/b3a7d5abecbee8fed08717405830126911825e81) \| optional launcher flag \| [torch.js:13](https://github.com/pinokiofactory/rc-stableaudio/blob/b3a7d5abecbee8fed08717405830126911825e81/torch.js#L13) — `"{{args && args.sageattention ? 'uv pip install https://huggingface.co/cocktailpeanut/wheels/resolve/main/sageattention-2.1.1%2Bcu128torch2.7.1-cp310-` \|` |
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
- [App flow graph](../flows/stableaudio.md)
<!-- cross-analysis:end -->

## Snapdragon evaluation (deep clone)
- **Clone/scan status:** cloned and scanned
- **Files scanned:** 11 total (0 .py, 7 .js/.ts, 4 other)
- **Snapdragon-relevant signals:** torch=11, xformers=3, mps=1, directml=1
- **Example evidence:**
  - torch: `install.js:17`
  - xformers: `install.js:21`
  - mps: `start.js:5`
  - directml: `torch.js:21`
- **Snapdragon verdict:** Unsuitable (MLX/Apple-only runtime) for Snapdragon unless ported to CPU/ONNX.
