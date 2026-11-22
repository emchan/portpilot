# Kokoro-TTS — portability analysis

- **Package name:** Kokoro-TTS (`Kokoro-TTS`)
- **Description:** Welcome to Kokoro, a high-quality text-to-speech synthesis program powered by deep learning. This tool converts any text into high-fidelity speech in just a few seconds. Simply input text, select a voice, adjust the speed, and enjoy the generated audio.
- **Original git URL:** https://github.com/pinokiofactory/Kokoro-TTS
- **Analyzed commit:** `491a369bdca03b320586bd230f1c819562c03558`
- **Platforms supported:** NVIDIA / AMD / Mac
- **Porting difficulty:** Low
- **CUDA-only packages:** xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

accelerate, diffusers, espeak-ng, espeakng-loader, ffmpeg, gradio, hf-xet, huggingface-hub, imageio-ffmpeg, kokoro, libaio-dev, misaki, numpy, phonemizer-fork, pydub, scipy, setuptools, soundfile, torch, torch-directml, torchaudio, torchvision, transformers, wheel, xformers

Requirements files: `requirements.txt`.

Third-party Python imports detected in local source: gradio, imageio-ffmpeg, kokoro, scipy, torch, tqdm.

Wheel indexes referenced: cpu, cu128, rocm6.3.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 3518
- **CUDA-related functions used:** `torch.cuda.is_available`

## Evidence and notes

- `torch.js` routes present: nvidia, amd, mac, cpu.
- Requirements from: requirements.txt
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): xformers
- Difficulty score: 0.5 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- retested on Python 3.12; dependencies installed but importing app.py hung in this container.
- Result: **not runnable in this container.**
<!-- cross-analysis:start -->
## Cross-analysis details

- **CPU category (cpu.md):** CPU-capable with shipped fallback
- **TPU suitability:** Difficult - significant port
- **TPU work needed:** replace CUDA attention kernels with TPU-compatible attention/SDPA/XLA; remove direct torch.cuda device assumptions; multiple CUDA-specific dependencies or large model/dtype constraints
- **Effort ranking (effort.md):** #43 — Low–medium
- **Effort blockers:** GPU-only attention: xformers; direct `torch.cuda` calls
- **Precisions noted:** FP32
- **Models/flows noted:** [hexgrad/Kokoro-82M](https://huggingface.co/hexgrad/Kokoro-82M)
- **Flow graph:** [flows/Kokoro-TTS.md](../flows/Kokoro-TTS.md)

### Snapshot verification (cloned analyzed commit)

- **Snapshot source:** `https://codeload.github.com/pinokiofactory/Kokoro-TTS/tar.gz/<analyzed commit>` extracted to `/tmp/opencode/pinokio-snapshots/Kokoro-TTS`
- **Files scanned:** 12 total (1 .py, 7 .js, 4 other)
- **Key files present:** pinokio.js, install.js, torch.js, start.js, requirements.txt
- **TPU/CUDA-relevant signals:**
  - `torch_cuda`: 1 match(es) (e.g. app.py:34)
  - `xformers`: 4 match(es) (e.g. torch.js:11, torch.js:11)
  - `directml`: 1 match(es) (e.g. torch.js:38)

### Evidence from analysis files

| Source | Evidence |
|---|---|
| [kernels.md](../analysis/kernels.md) | No per-repo kernel table row matched; see kernels.md for global signals. |
| [quantization.md](../analysis/quantization.md) | `\| [Kokoro-TTS](https://github.com/pinokiofactory/Kokoro-TTS) \| [491a369](https://github.com/pinokiofactory/Kokoro-TTS/commit/491a369bdca03b320586bd230f1c819562c03558) \| [505](https://github.com/pinokiofactory/Kokoro-TTS/blob/491a369bdca03b320586bd230f1c819562c03558/app.py#L505) \| float / FP32 \| dtype declaration \| weight = float(parts[1].strip()) \|` |
| [quantization.md](../analysis/quantization.md) | `\| [Kokoro-TTS](https://github.com/pinokiofactory/Kokoro-TTS) \| [491a369](https://github.com/pinokiofactory/Kokoro-TTS/commit/491a369bdca03b320586bd230f1c819562c03558) \| [1043](https://github.com/pinokiofactory/Kokoro-TTS/blob/491a369bdca03b320586bd230f1c819562c03558/app.py#L1043) \| float / FP32 \| dtype declaration \| audio_tensor = torch.tensor(audio_data, dtype=torch.float32) \|` |
| [fusion.md](../analysis/fusion.md) | No direct fusion table row matched; see fusion.md for global context. |
| [models.md](../analysis/models.md) | No model pull/shape row matched in models.md. |
| [cpu.md](../analysis/cpu.md) | CPU category: **CPU-capable with shipped fallback** |
| [tpu.md](../analysis/tpu.md) | TPU suitability: **Difficult - significant port** — replace CUDA attention kernels with TPU-compatible attention/SDPA/XLA; remove direct torch.cuda device assumptions; multiple CUDA-specific dependencies or large model/dtype constraints |

### Related analysis

- [CPU analysis](../analysis/cpu.md)
- [TPU analysis](../analysis/tpu.md)
- [Effort ranking](../analysis/effort.md)
- [Kernel evidence](../analysis/kernels.md)
- [Quantization evidence](../analysis/quantization.md)
- [Fusion evidence](../analysis/fusion.md)
- [Model pulls/shapes](../analysis/models.md)
- [Flow graphs](../analysis/flows.md)
- [App flow graph](../flows/Kokoro-TTS.md)
<!-- cross-analysis:end -->

## Snapdragon evaluation (deep clone)
- **Clone/scan status:** cloned and scanned
- **Files scanned:** 12 total (1 .py, 7 .js/.ts, 4 other)
- **Snapdragon-relevant signals:** cuda=12, torch=37, xformers=2, directml=1
- **Example evidence:**
  - cuda: `app.py:34`
  - torch: `app.py:3`
  - xformers: `torch.js:11`
  - directml: `torch.js:38`
- **Snapdragon verdict:** Contains CUDA/Triton/TensorRT signals; Snapdragon path requires replacement or ONNX conversion.
