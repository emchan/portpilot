# Ultimate-TTS-Studio — portability analysis

- **Package name:** Ultimate-TTS-Studio (`Ultimate-TTS-Studio`)
- **Description:** Kokoro, KittenTTS, Higgs audio, Chatterbox/Multi, Fish-Speech, F5 & index-tts & indextts2, VoxCPM and VibeVoice in one app
- **Original git URL:** https://github.com/pinokiofactory/Ultimate-TTS-Studio
- **Analyzed commit:** `b8c15efaead5a5e8744783fd443466333d2b1805`
- **Platforms supported:** NVIDIA only
- **Porting difficulty:** Very high
- **CUDA-only packages:** flash-attn, onnxruntime-gpu, sageattention *(optional)*, triton *(optional)*, triton-windows, xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

devicetorch, espeak-ng, flash-attn, gradio, libaio-dev, libsox-fmt-all, numpy, onnxruntime-gpu, openai-whisper, phonemizer-fork, portaudio, pynini, sageattention, setuptools, sox, torch, torch-directml, torchaudio, torchvision, triton, triton-windows, voxcpm, wetextprocessing, xformers

Wheel indexes referenced: cpu, cu128, rocm6.3.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 374
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- Explicit platform tag found: NVIDIA only.
- `torch.js` routes present: nvidia, amd, mac, cpu.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): sageattention, triton, xformers
- Difficulty score: 12.8 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- retested on Python 3.10; requirements installation hung/timed out in this container.
- Result: **not runnable in this container.**
<!-- cross-analysis:start -->
## Cross-analysis details

- **CPU category (cpu.md):** CPU-capable with shipped fallback
- **TPU suitability:** Difficult - significant port
- **TPU work needed:** replace CUDA attention kernels with TPU-compatible attention/SDPA/XLA; replace onnxruntime-gpu with TPU-compatible runtime; multiple CUDA-specific dependencies or large model/dtype constraints
- **Effort ranking (effort.md):** #94 — Very high
- **Effort blockers:** GPU-only attention: flash-attn/sageattention/triton/triton-windows/xformers; GPU runtime: onnxruntime-gpu; CUDA-only fused kernels need config change
- **Precisions noted:** unspecified
- **Models/flows noted:** [cocktailpeanut/oa](https://huggingface.co/cocktailpeanut/oa)
- **Flow graph:** [flows/Ultimate-TTS-Studio.md](../flows/Ultimate-TTS-Studio.md)

### Snapshot verification (cloned analyzed commit)

- **Snapshot source:** `https://codeload.github.com/pinokiofactory/Ultimate-TTS-Studio/tar.gz/<analyzed commit>` extracted to `/tmp/opencode/pinokio-snapshots/Ultimate-TTS-Studio`
- **Files scanned:** 10 total (0 .py, 7 .js, 3 other)
- **Key files present:** pinokio.js, install.js, torch.js, start.js
- **TPU/CUDA-relevant signals:**
  - `xformers`: 2 match(es) (e.g. torch.js:11, torch.js:11)
  - `flash_attn`: 4 match(es) (e.g. torch.js:12, torch.js:12)
  - `sageattention`: 5 match(es) (e.g. torch.js:14, torch.js:14)
  - `triton`: 4 match(es) (e.g. torch.js:13, torch.js:13)
  - `onnxruntime_gpu`: 1 match(es) (e.g. install.js:27)
  - `directml`: 1 match(es) (e.g. torch.js:26)

### Evidence from analysis files

| Source | Evidence |
|---|---|
| [kernels.md](../analysis/kernels.md) | `\| [Ultimate-TTS-Studio](https://github.com/pinokiofactory/Ultimate-TTS-Studio) \| [b8c15ef](https://github.com/pinokiofactory/Ultimate-TTS-Studio/commit/b8c15efaead5a5e8744783fd443466333d2b1805) \| optional flag + launcher install \| install.js, torch.js \| [torch.js:13](https://github.com/pinokiofactory/Ultimate-TTS-Studio/blob/b8c15efaead5a5e8744783fd443466333d2b1805/torch.js#L13) — "{{args && args.triton ? 'uv pip install triton-windows==3.3.1.post19' : ''}}", \|` |
| [kernels.md](../analysis/kernels.md) | `\| [Ultimate-TTS-Studio](https://github.com/pinokiofactory/Ultimate-TTS-Studio) \| [b8c15ef](https://github.com/pinokiofactory/Ultimate-TTS-Studio/commit/b8c15efaead5a5e8744783fd443466333d2b1805) \| launcher install \| [torch.js:12](https://github.com/pinokiofactory/Ultimate-TTS-Studio/blob/b8c15efaead5a5e8744783fd443466333d2b1805/torch.js#L12) — "uv pip install https://github.com/mjun0812/flash-attention-prebuild-wheels/releases/download/v0.4.10/flash_attn-2.8.2+cu128torch2.7-cp310-cp310-win_amd64.whl",<br>[torch.js:61](https://github.com/pinokiofactory/Ultimate-TTS-Studio/blob/b8c15efaead5a5e8744783fd443466333d2b1805/torch.js#L61) — "uv pip install https://github.com/mjun0812/flash-attention-prebuild-wheels/releases/download/v0.4.11/flash_attn-2.8.3+cu128torch2.7-cp310-cp310-linux_x86_64.whl", \|` |
| [kernels.md](../analysis/kernels.md) | `\| [Ultimate-TTS-Studio](https://github.com/pinokiofactory/Ultimate-TTS-Studio) \| [b8c15ef](https://github.com/pinokiofactory/Ultimate-TTS-Studio/commit/b8c15efaead5a5e8744783fd443466333d2b1805) \| optional flag + launcher install \| [torch.js:14](https://github.com/pinokiofactory/Ultimate-TTS-Studio/blob/b8c15efaead5a5e8744783fd443466333d2b1805/torch.js#L14) — "{{args && args.sageattention ? 'uv pip install https://github.com/woct0rdho/SageAttention/releases/download/v2.1.1-windows/sageattention-2.1.1+cu128torch2.7.0-cp...<br>[torch.js:64](https://github.com/pinokiofactory/Ultimate-TTS-Studio/blob/b8c15efaead5a5e8744783fd443466333d2b1805/torch.js#L64) — "{{args && args.sageattention ? 'uv pip install git+https://github.com/thu-ml/SageAttention.git' : ''}}" \|` |
| [quantization.md](../analysis/quantization.md) | No per-repo quantization table row matched; see quantization.md. |
| [fusion.md](../analysis/fusion.md) | `\| [Ultimate-TTS-Studio](https://github.com/pinokiofactory/Ultimate-TTS-Studio) \| [b8c15ef](https://github.com/pinokiofactory/Ultimate-TTS-Studio/commit/b8c15efaead5a5e8744783fd443466333d2b1805) \| installed by launcher \| [torch.js:12](https://github.com/pinokiofactory/Ultimate-TTS-Studio/blob/b8c15efaead5a5e8744783fd443466333d2b1805/torch.js#L12) — `"uv pip install https://github.com/mjun0812/flash-attention-prebuild-wheels/releases/download/v0.4.10/flash_attn-2.8.2+cu128torch2.7-cp310-cp310-win_a` \|` |
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
- [App flow graph](../flows/Ultimate-TTS-Studio.md)
<!-- cross-analysis:end -->
