# openaudio — portability analysis

- **Package name:** OpenAudio (`openaudio`)
- **Description:** Multilingual Text-to-Speech with Voice Cloning (Supports: English, Japanese, Korean, Chinese, French, German, Arabic, and Spanish) https://github.com/fishaudio/fish-speech
- **Original git URL:** https://github.com/pinokiofactory/openaudio
- **Analyzed commit:** `6a69e7903d7430cc3d08dae6673caf85b9032fcf`
- **Platforms supported:** NVIDIA / AMD / Mac
- **Porting difficulty:** High
- **CUDA-only packages:** flash-attn, sageattention *(optional)*, triton *(optional)*, triton-windows, xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

cachetools, flash-attn, gradio, livekit, livekit-agents, numpy, portaudio, sageattention, torch, torch-directml, torchaudio, torchvision, triton, triton-windows, xformers

Wheel indexes referenced: cpu, cu128, rocm6.3.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 313
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- `torch.js` routes present: nvidia, amd, mac, cpu.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): sageattention, triton, xformers
- Difficulty score: 7.8 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- blocked by torch==2.8.0 pin unavailable on Python 3.14.
- Result: **not runnable in this container.**

## CPU port attempt

- **Attempt order:** #79 of 101 (by porting effort, easiest first).
- **Status:** CPU-capable (shipped fallback).
- **Changes applied / required:** use existing CPU wheel branch in torch.js; use existing non-GPU launcher route; disable fused GPU kernels (xformers/flash/sage) in config; substitute GPU-only attention libs with SDPA math backend.
- **Smoke check:** n/a (no Python source in snapshot).
- **Blockers:** GPU-only attention: flash-attn/sageattention/triton/triton-windows/xformers; CUDA-only fused kernels.
- **Scope note:** static portability review of the Pinokio wrapper; no install or model download was executed.
<!-- cross-analysis:start -->
## Cross-analysis details

- **CPU category (cpu.md):** CPU-capable with shipped fallback
- **TPU suitability:** Possible - moderate port
- **TPU work needed:** replace CUDA attention kernels with TPU-compatible attention/SDPA/XLA; moderate device/kernel/runtime adaptation
- **Effort ranking (effort.md):** #79 — High
- **Effort blockers:** GPU-only attention: flash-attn/sageattention/triton/triton-windows/xformers; CUDA-only fused kernels need config change
- **Precisions noted:** unspecified
- **Models/flows noted:** —
- **Flow graph:** [flows/openaudio.md](../flows/openaudio.md)

### Snapshot verification (cloned analyzed commit)

- **Snapshot source:** `https://codeload.github.com/pinokiofactory/openaudio/tar.gz/<analyzed commit>` extracted to `/tmp/opencode/pinokio-snapshots/openaudio`
- **Files scanned:** 10 total (0 .py, 7 .js, 3 other)
- **Key files present:** pinokio.js, install.js, torch.js, start.js
- **TPU/CUDA-relevant signals:**
  - `xformers`: 5 match(es) (e.g. torch.js:11, torch.js:11)
  - `flash_attn`: 2 match(es) (e.g. torch.js:14, torch.js:31)
  - `sageattention`: 4 match(es) (e.g. torch.js:13, torch.js:13)
  - `triton`: 4 match(es) (e.g. torch.js:12, torch.js:12)
  - `directml`: 1 match(es) (e.g. torch.js:44)
  - `mps`: 1 match(es) (e.g. start.js:14)

### Evidence from analysis files

| Source | Evidence |
|---|---|
| [kernels.md](../analysis/kernels.md) | `\| [openaudio](https://github.com/pinokiofactory/openaudio) \| [6a69e79](https://github.com/pinokiofactory/openaudio/commit/6a69e7903d7430cc3d08dae6673caf85b9032fcf) \| optional flag + launcher install \| torch.js \| [torch.js:12](https://github.com/pinokiofactory/openaudio/blob/6a69e7903d7430cc3d08dae6673caf85b9032fcf/torch.js#L12) — "{{args && args.triton ? 'uv pip install triton-windows==3.3.1.post19' : ''}}", \|` |
| [kernels.md](../analysis/kernels.md) | `\| [openaudio](https://github.com/pinokiofactory/openaudio) \| [6a69e79](https://github.com/pinokiofactory/openaudio/commit/6a69e7903d7430cc3d08dae6673caf85b9032fcf) \| optional flag \| [start.js:14](https://github.com/pinokiofactory/openaudio/blob/6a69e7903d7430cc3d08dae6673caf85b9032fcf/start.js#L14) — "python run_webui.py --device {{(platform === 'darwin' ? 'mps' : (gpu === 'nvidia' ? 'cuda' : 'cpu'))}}", \|` |
| [kernels.md](../analysis/kernels.md) | `\| [openaudio](https://github.com/pinokiofactory/openaudio) \| [6a69e79](https://github.com/pinokiofactory/openaudio/commit/6a69e7903d7430cc3d08dae6673caf85b9032fcf) \| optional flag + launcher install \| [torch.js:14](https://github.com/pinokiofactory/openaudio/blob/6a69e7903d7430cc3d08dae6673caf85b9032fcf/torch.js#L14) — "{{args && args.flashattention ? 'uv pip install https://huggingface.co/cocktailpeanut/wheels/resolve/main/flash_attn-2.8.2%2Bcu128torch2.7-cp310-cp310-win_amd64....<br>[torch.js:31](https://github.com/pinokiofactory/openaudio/blob/6a69e7903d7430cc3d08dae6673caf85b9032fcf/torch.js#L31) — "{{args && args.flashattention ? 'uv pip install https://huggingface.co/cocktailpeanut/wheels/resolve/main/flash_attn-2.8.3%2Bcu128torch2.7-cp310-cp310-linux_x86_... \|` |
| [kernels.md](../analysis/kernels.md) | `\| [openaudio](https://github.com/pinokiofactory/openaudio) \| [6a69e79](https://github.com/pinokiofactory/openaudio/commit/6a69e7903d7430cc3d08dae6673caf85b9032fcf) \| optional flag + launcher install \| [torch.js:13](https://github.com/pinokiofactory/openaudio/blob/6a69e7903d7430cc3d08dae6673caf85b9032fcf/torch.js#L13) — "{{args && args.sageattention ? 'uv pip install https://huggingface.co/cocktailpeanut/wheels/resolve/main/sageattention-2.1.1%2Bcu128torch2.7.1-cp310-cp310-win_am...<br>[torch.js:30](https://github.com/pinokiofactory/openaudio/blob/6a69e7903d7430cc3d08dae6673caf85b9032fcf/torch.js#L30) — "{{args && args.sageattention ? 'uv pip install https://huggingface.co/cocktailpeanut/wheels/resolve/main/sageattention-2.1.1%2Bcu128torch2.7.1-cp310-cp310-linux_... \|` |
| [quantization.md](../analysis/quantization.md) | No per-repo quantization table row matched; see quantization.md. |
| [fusion.md](../analysis/fusion.md) | `\| [openaudio](https://github.com/pinokiofactory/openaudio) \| [6a69e79](https://github.com/pinokiofactory/openaudio/commit/6a69e7903d7430cc3d08dae6673caf85b9032fcf) \| optional launcher flag \| [torch.js:13](https://github.com/pinokiofactory/openaudio/blob/6a69e7903d7430cc3d08dae6673caf85b9032fcf/torch.js#L13) — `"{{args && args.sageattention ? 'uv pip install https://huggingface.co/cocktailpeanut/wheels/resolve/main/sageattention-2.1.1%2Bcu128torch2.7.1-cp310-` \|` |
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
- [App flow graph](../flows/openaudio.md)
<!-- cross-analysis:end -->
