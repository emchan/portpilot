# audiocraft_plus — portability analysis

- **Package name:** audiocraft_plus (`audiocraft_plus`)
- **Description:** AudioCraft Plus is an all-in-one WebUI for the original AudioCraft, adding many quality features on top https://github.com/GrandaddyShmax/audiocraft_plus
- **Original git URL:** https://github.com/pinokiofactory/audiocraft_plus
- **Analyzed commit:** `a8e0d2731e8dbb7185a4a0ffd53b495d003586ab`
- **Platforms supported:** NVIDIA / AMD / Mac
- **Porting difficulty:** Low–medium
- **CUDA-only packages:** triton-windows, xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

av, demucs, einops, encodec, fastapi, flashy, gradio, gradio-client, huggingface-hub, hydra-colorlog, hydra-core, julius, librosa, num2words, numpy, pytaglib, sentencepiece, spacy, torch, torch-directml, torchaudio, torchmetrics, torchvision, tqdm, transformers, triton-windows, wheel, xformers

Requirements files: `requirements.txt`.

Wheel indexes referenced: cpu, cu128, rocm6.3.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 297
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- `torch.js` routes present: nvidia, amd, mac, cpu.
- Requirements from: requirements.txt
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): xformers
- Difficulty score: 2.5 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- blocked by spacy build failure on Python 3.14.
- Result: **not runnable in this container.**
<!-- cross-analysis:start -->
## Cross-analysis details

- **CPU category (cpu.md):** CPU-capable with shipped fallback
- **TPU suitability:** Possible - moderate port
- **TPU work needed:** replace CUDA attention kernels with TPU-compatible attention/SDPA/XLA; moderate device/kernel/runtime adaptation
- **Effort ranking (effort.md):** #47 — Low–medium
- **Effort blockers:** GPU-only attention: triton-windows/xformers
- **Precisions noted:** unspecified
- **Models/flows noted:** —
- **Flow graph:** [flows/audiocraft_plus.md](../flows/audiocraft_plus.md)

### Snapshot verification (cloned analyzed commit)

- **Snapshot source:** `https://codeload.github.com/pinokiofactory/audiocraft_plus/tar.gz/<analyzed commit>` extracted to `/tmp/opencode/pinokio-snapshots/audiocraft_plus`
- **Files scanned:** 12 total (0 .py, 7 .js, 5 other)
- **Key files present:** pinokio.js, install.js, torch.js, start.js, requirements.txt
- **TPU/CUDA-relevant signals:**
  - `xformers`: 6 match(es) (e.g. torch.js:11, torch.js:11)
  - `triton`: 1 match(es) (e.g. torch.js:12)
  - `directml`: 1 match(es) (e.g. torch.js:25)

### Evidence from analysis files

| Source | Evidence |
|---|---|
| [kernels.md](../analysis/kernels.md) | `\| [audiocraft_plus](https://github.com/pinokiofactory/audiocraft_plus) \| [a8e0d27](https://github.com/pinokiofactory/audiocraft_plus/commit/a8e0d2731e8dbb7185a4a0ffd53b495d003586ab) \| launcher install \| torch.js \| [torch.js:12](https://github.com/pinokiofactory/audiocraft_plus/blob/a8e0d2731e8dbb7185a4a0ffd53b495d003586ab/torch.js#L12) — "uv pip install triton-windows==3.3.1.post19" \|` |
| [quantization.md](../analysis/quantization.md) | No per-repo quantization table row matched; see quantization.md. |
| [fusion.md](../analysis/fusion.md) | No direct fusion table row matched; see fusion.md for global context. |
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
- [App flow graph](../flows/audiocraft_plus.md)
<!-- cross-analysis:end -->
