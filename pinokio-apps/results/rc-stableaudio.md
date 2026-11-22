# rc-stableaudio — portability analysis

- **Package name:** RC Stable Audio Tools (`rc-stableaudio`)
- **Description:** Advanced Gradio UI for Stable Audio https://github.com/RoyalCities/RC-stable-audio-tools
- **Original git URL:** https://github.com/pinokiofactory/rc-stableaudio
- **Analyzed commit:** `b3a7d5abecbee8fed08717405830126911825e81`
- **Platforms supported:** NVIDIA / AMD / Mac
- **Porting difficulty:** High
- **CUDA-only packages:** flash-attn, sageattention *(optional)*, triton *(optional)*, triton-windows, xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

flash-attn, gradio, libsndfile, numpy, sageattention, torch, torch-directml, torchaudio, torchvision, triton, triton-windows, xformers

Wheel indexes referenced: cpu, cu128, rocm6.3.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 349
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- `torch.js` routes present: nvidia, amd, mac, cpu.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): sageattention, triton, xformers
- Difficulty score: 7.8 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- retested on Python 3.10; run_gradio still fails on torchvision::nms operator mismatch.
- Result: **not runnable in this container.**
<!-- cross-analysis:start -->
## Cross-analysis details

- **CPU category (cpu.md):** CPU-capable with shipped fallback
- **TPU suitability:** Possible - moderate port
- **TPU work needed:** replace CUDA attention kernels with TPU-compatible attention/SDPA/XLA; moderate device/kernel/runtime adaptation
- **Effort ranking (effort.md):** #80 — High
- **Effort blockers:** GPU-only attention: flash-attn/sageattention/triton/triton-windows/xformers; CUDA-only fused kernels need config change
- **Precisions noted:** unspecified
- **Models/flows noted:** —
- **Flow graph:** [flows/rc-stableaudio.md](../flows/rc-stableaudio.md)

### Snapshot verification (cloned analyzed commit)

- **Snapshot source:** `https://codeload.github.com/pinokiofactory/rc-stableaudio/tar.gz/<analyzed commit>` extracted to `/tmp/opencode/pinokio-snapshots/rc-stableaudio`
- **Files scanned:** 12 total (0 .py, 8 .js, 4 other)
- **Key files present:** pinokio.js, install.js, torch.js, start.js
- **TPU/CUDA-relevant signals:**
  - `xformers`: 5 match(es) (e.g. torch.js:11, torch.js:11)
  - `flash_attn`: 2 match(es) (e.g. torch.js:14, torch.js:31)
  - `sageattention`: 4 match(es) (e.g. torch.js:13, torch.js:13)
  - `triton`: 4 match(es) (e.g. torch.js:12, torch.js:12)
  - `directml`: 1 match(es) (e.g. torch.js:44)

### Evidence from analysis files

| Source | Evidence |
|---|---|
| [kernels.md](../analysis/kernels.md) | `\| [rc-stableaudio](https://github.com/pinokiofactory/rc-stableaudio) \| [b3a7d5a](https://github.com/pinokiofactory/rc-stableaudio/commit/b3a7d5abecbee8fed08717405830126911825e81) \| optional flag + launcher install \| torch.js \| [torch.js:12](https://github.com/pinokiofactory/rc-stableaudio/blob/b3a7d5abecbee8fed08717405830126911825e81/torch.js#L12) — "{{args && args.triton ? 'uv pip install triton-windows==3.3.1.post19' : ''}}", \|` |
| [kernels.md](../analysis/kernels.md) | `\| [rc-stableaudio](https://github.com/pinokiofactory/rc-stableaudio) \| [b3a7d5a](https://github.com/pinokiofactory/rc-stableaudio/commit/b3a7d5abecbee8fed08717405830126911825e81) \| optional flag + launcher install \| [torch.js:14](https://github.com/pinokiofactory/rc-stableaudio/blob/b3a7d5abecbee8fed08717405830126911825e81/torch.js#L14) — "{{args && args.flashattention ? 'uv pip install https://huggingface.co/cocktailpeanut/wheels/resolve/main/flash_attn-2.8.2%2Bcu128torch2.7-cp310-cp310-win_amd64....<br>[torch.js:31](https://github.com/pinokiofactory/rc-stableaudio/blob/b3a7d5abecbee8fed08717405830126911825e81/torch.js#L31) — "{{args && args.flashattention ? 'uv pip install https://huggingface.co/cocktailpeanut/wheels/resolve/main/flash_attn-2.8.3%2Bcu128torch2.7-cp310-cp310-linux_x86_... \|` |
| [kernels.md](../analysis/kernels.md) | `\| [rc-stableaudio](https://github.com/pinokiofactory/rc-stableaudio) \| [b3a7d5a](https://github.com/pinokiofactory/rc-stableaudio/commit/b3a7d5abecbee8fed08717405830126911825e81) \| optional flag + launcher install \| [torch.js:13](https://github.com/pinokiofactory/rc-stableaudio/blob/b3a7d5abecbee8fed08717405830126911825e81/torch.js#L13) — "{{args && args.sageattention ? 'uv pip install https://huggingface.co/cocktailpeanut/wheels/resolve/main/sageattention-2.1.1%2Bcu128torch2.7.1-cp310-cp310-win_am...<br>[torch.js:30](https://github.com/pinokiofactory/rc-stableaudio/blob/b3a7d5abecbee8fed08717405830126911825e81/torch.js#L30) — "{{args && args.sageattention ? 'uv pip install https://huggingface.co/cocktailpeanut/wheels/resolve/main/sageattention-2.1.1%2Bcu128torch2.7.1-cp310-cp310-linux_... \|` |
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
- [App flow graph](../flows/rc-stableaudio.md)
<!-- cross-analysis:end -->

## Snapdragon evaluation (deep clone)
- **Clone/scan status:** cloned and scanned
- **Files scanned:** 12 total (0 .py, 8 .js/.ts, 4 other)
- **Snapdragon-relevant signals:** torch=13, triton=2, xformers=3, flashattention=2, sageattention=2, mps=1, directml=1
- **Example evidence:**
  - torch: `install.js:28`
  - triton: `torch.js:12`
  - xformers: `install.js:32`
  - flashattention: `torch.js:14`
  - sageattention: `torch.js:13`
  - mps: `start.js:5`
  - directml: `torch.js:44`
- **Snapdragon verdict:** Contains CUDA/Triton/TensorRT signals; Snapdragon path requires replacement or ONNX conversion.
