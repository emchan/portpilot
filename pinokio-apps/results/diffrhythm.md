# diffrhythm — portability analysis

- **Package name:** DiffRhythm (`diffrhythm`)
- **Description:** Generate songs with AI (up to 4 min 45 sec). Both with lyrics or instrumental https://github.com/ASLP-lab/DiffRhythm
- **Original git URL:** https://github.com/pinokiofactory/diffrhythm
- **Analyzed commit:** `15166cfd3b677d7fd6294b4d9fb88e7f4845d3ee`
- **Platforms supported:** NVIDIA / AMD / Mac
- **Porting difficulty:** High
- **CUDA-only packages:** bitsandbytes, onnxruntime-gpu, triton *(optional)*, triton-windows, xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

accelerate, bitsandbytes, cn2an, ema-pytorch, espeak-ng, jieba, langsegment, libaio-dev, librosa, muq, mutagen, numpy, onnxruntime, onnxruntime-gpu, openai, pandas, phonemizer, prefigure, pyarrow, pykakasi, pylance, pyopenjtalk, pypinyin, spaces, torch, torch-directml, torchaudio, torchdiffeq, torchvision, transformers, triton, triton-windows, unidecode, x-transformers, xformers

Requirements files: `requirements.txt`.

Wheel indexes referenced: cpu, cu128, rocm6.3.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 409
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- `torch.js` routes present: nvidia, amd, mac, cpu.
- Requirements from: requirements.txt
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): triton, xformers
- Difficulty score: 7.8 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- retested on Python 3.10; blocked by torchvision operator mismatch (torchvision::nms).
- Result: **not runnable in this container.**
<!-- cross-analysis:start -->
## Cross-analysis details

- **CPU category (cpu.md):** CPU-capable with shipped fallback
- **TPU suitability:** Difficult - significant port
- **TPU work needed:** replace CUDA attention kernels with TPU-compatible attention/SDPA/XLA; NF4/bitsandbytes quantization needs dequant/upcast or TPU-supported path; replace onnxruntime-gpu with TPU-compatible runtime; multiple CUDA-specific dependencies or large model/dtype constraints
- **Effort ranking (effort.md):** #83 — High
- **Effort blockers:** GPU-only attention: triton/triton-windows/xformers; GPU quantisers: bitsandbytes; GPU runtime: onnxruntime-gpu
- **Precisions noted:** unspecified
- **Models/flows noted:** —
- **Flow graph:** [flows/diffrhythm.md](../flows/diffrhythm.md)

### Snapshot verification (cloned analyzed commit)

- **Snapshot source:** `https://codeload.github.com/pinokiofactory/diffrhythm/tar.gz/<analyzed commit>` extracted to `/tmp/opencode/pinokio-snapshots/diffrhythm`
- **Files scanned:** 15 total (0 .py, 7 .js, 8 other)
- **Key files present:** pinokio.js, install.js, torch.js, start.js, requirements.txt, package.json
- **TPU/CUDA-relevant signals:**
  - `xformers`: 4 match(es) (e.g. torch.js:11, torch.js:11)
  - `triton`: 5 match(es) (e.g. torch.js:12, torch.js:12)
  - `bitsandbytes`: 1 match(es) (e.g. requirements.txt:12)
  - `onnxruntime_gpu`: 2 match(es) (e.g. requirements.txt:21, install.js:44)
  - `directml`: 1 match(es) (e.g. torch.js:23)

### Evidence from analysis files

| Source | Evidence |
|---|---|
| [kernels.md](../analysis/kernels.md) | `\| [diffrhythm](https://github.com/pinokiofactory/diffrhythm) \| [15166cf](https://github.com/pinokiofactory/diffrhythm/commit/15166cfd3b677d7fd6294b4d9fb88e7f4845d3ee) \| optional flag + launcher install \| install.js, torch.js \| [torch.js:12](https://github.com/pinokiofactory/diffrhythm/blob/15166cfd3b677d7fd6294b4d9fb88e7f4845d3ee/torch.js#L12) — "{{args && args.triton ? 'uv pip install triton-windows==3.3.1.post19' : ''}}" \|` |
| [quantization.md](../analysis/quantization.md) | `\| [diffrhythm](https://github.com/pinokiofactory/diffrhythm) \| requirements \| `requirements.txt:12` — bitsandbytes==0.45.3 \|` |
| [fusion.md](../analysis/fusion.md) | No direct fusion table row matched; see fusion.md for global context. |
| [models.md](../analysis/models.md) | No model pull/shape row matched in models.md. |
| [cpu.md](../analysis/cpu.md) | CPU category: **CPU-capable with shipped fallback** |
| [tpu.md](../analysis/tpu.md) | TPU suitability: **Difficult - significant port** — replace CUDA attention kernels with TPU-compatible attention/SDPA/XLA; NF4/bitsandbytes quantization needs dequant/upcast or TPU-supported path; replace onnxruntime-gpu with TPU-compatible runtime; multiple CUDA-specific dependencies or large model/dtype constraints |

### Related analysis

- [CPU analysis](../analysis/cpu.md)
- [TPU analysis](../analysis/tpu.md)
- [Effort ranking](../analysis/effort.md)
- [Kernel evidence](../analysis/kernels.md)
- [Quantization evidence](../analysis/quantization.md)
- [Fusion evidence](../analysis/fusion.md)
- [Model pulls/shapes](../analysis/models.md)
- [Flow graphs](../analysis/flows.md)
- [App flow graph](../flows/diffrhythm.md)
<!-- cross-analysis:end -->
