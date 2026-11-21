# zonos — portability analysis

- **Package name:** zonos (`zonos`)
- **Description:** Zonos-v0.1 is a leading open-weight text-to-speech model trained on more than 200k hours of varied multilingual speech, delivering expressiveness and quality on par with—or even surpassing—top TTS providers. https://github.com/Zyphra/Zonos
- **Original git URL:** https://github.com/pinokiofactory/zonos
- **Analyzed commit:** `0be13e4e803fe0834bae8326240633ac8e53bffc`
- **Platforms supported:** NVIDIA / AMD / Mac
- **Porting difficulty:** High
- **CUDA-only packages:** flash-attn, triton, triton-windows, xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

espeak-ng, flash-attn, gradio, hf-xet, libaio-dev, numpy, sympy, torch, torch-directml, torchaudio, torchvision, triton, triton-windows, wheel, xformers

Third-party Python imports detected in local source: sympy, torch, triton.

Wheel indexes referenced: cpu, cu128, rocm6.3.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 7276
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- `torch.js` routes present: nvidia, amd, mac, cpu.
- No requirements file; third-party Python imports used as a fallback signal.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): xformers
- Difficulty score: 7.0 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- dependencies installed and package imported successfully on CPU.
- Result: **CPU port imports successfully.**

## CPU port attempt

- **Attempt order:** #77 of 101 (by porting effort, easiest first).
- **Status:** CPU-capable (shipped fallback).
- **Changes applied / required:** use existing CPU wheel branch in torch.js; use existing non-NVIDIA/non-AMD branch in torch.js; use existing non-GPU launcher route; disable fused GPU kernels (xformers/flash/sage) in config; substitute GPU-only attention libs with SDPA math backend.
- **Smoke check:** pass (2/2 files).
- **Blockers:** GPU-only attention: flash-attn/triton/triton-windows/xformers; CUDA-only fused kernels.
- **Scope note:** static portability review of the Pinokio wrapper; no install or model download was executed.
<!-- cross-analysis:start -->
## Cross-analysis details

- **CPU category (cpu.md):** CPU-capable with shipped fallback
- **TPU suitability:** Possible - moderate port
- **TPU work needed:** replace CUDA attention kernels with TPU-compatible attention/SDPA/XLA; moderate device/kernel/runtime adaptation
- **Effort ranking (effort.md):** #77 — High
- **Effort blockers:** GPU-only attention: flash-attn/triton/triton-windows/xformers; CUDA-only fused kernels need config change
- **Precisions noted:** FP32, FP16, BF16, INT8, UINT8, INT32, INT64, FP64, BOOL
- **Models/flows noted:** —
- **Flow graph:** [flows/zonos.md](../flows/zonos.md)

### Snapshot verification (cloned analyzed commit)

- **Snapshot source:** `https://codeload.github.com/pinokiofactory/zonos/tar.gz/<analyzed commit>` extracted to `/tmp/opencode/pinokio-snapshots/zonos`
- **Files scanned:** 16 total (2 .py, 8 .js, 6 other)
- **Key files present:** pinokio.js, install.js, torch.js, start.js, package.json
- **TPU/CUDA-relevant signals:**
  - `xformers`: 5 match(es) (e.g. torch.js:11, torch.js:11)
  - `flash_attn`: 4 match(es) (e.g. torch.js:13, torch.js:13)
  - `triton`: 6 match(es) (e.g. torch.js:12, torch.js:59)
  - `nf4`: 1 match(es) (e.g. cpp.py:3292)
  - `directml`: 1 match(es) (e.g. torch.js:26)

### Evidence from analysis files

| Source | Evidence |
|---|---|
| [kernels.md](../analysis/kernels.md) | `\| [zonos](https://github.com/pinokiofactory/zonos) \| [0be13e4](https://github.com/pinokiofactory/zonos/commit/0be13e4e803fe0834bae8326240633ac8e53bffc) \| direct code + launcher install \| clear_cache.js, cpp.py, cpp_builder.py \| [clear_cache.js:9](https://github.com/pinokiofactory/zonos/blob/0be13e4e803fe0834bae8326240633ac8e53bffc/clear_cache.js#L9) — const triton_cache_dir = path.resolve(homedir, ".triton/cache"); \|` |
| [kernels.md](../analysis/kernels.md) | `\| [zonos](https://github.com/pinokiofactory/zonos) \| [0be13e4](https://github.com/pinokiofactory/zonos/commit/0be13e4e803fe0834bae8326240633ac8e53bffc) \| launcher install \| [torch.js:13](https://github.com/pinokiofactory/zonos/blob/0be13e4e803fe0834bae8326240633ac8e53bffc/torch.js#L13) — "uv pip install https://huggingface.co/lldacing/flash-attention-windows-wheel/resolve/main/flash_attn-2.7.4.post1%2Bcu128torch2.7.0cxx11abiFALSE-cp310-cp310-win_a...<br>[torch.js:60](https://github.com/pinokiofactory/zonos/blob/0be13e4e803fe0834bae8326240633ac8e53bffc/torch.js#L60) — "uv pip install https://github.com/kingbri1/flash-attention/releases/download/v2.7.4.post1/flash_attn-2.7.4.post1+cu128torch2.7.0cxx11abiFALSE-cp310-cp310-linux_x... \|` |
| [quantization.md](../analysis/quantization.md) | `\| [zonos](https://github.com/pinokiofactory/zonos) \| reference \| `cpp.py:148` — torch.int8,<br>`cpp.py:158` — torch.int8, \|` |
| [quantization.md](../analysis/quantization.md) | `\| [zonos](https://github.com/pinokiofactory/zonos) \| [0be13e4](https://github.com/pinokiofactory/zonos/commit/0be13e4e803fe0834bae8326240633ac8e53bffc) \| [137](https://github.com/pinokiofactory/zonos/blob/0be13e4e803fe0834bae8326240633ac8e53bffc/cpp.py#L137) \| bfloat16 / BF16 \| dtype declaration \| torch.bfloat16, \|` |
| [quantization.md](../analysis/quantization.md) | `\| [zonos](https://github.com/pinokiofactory/zonos) \| [0be13e4](https://github.com/pinokiofactory/zonos/commit/0be13e4e803fe0834bae8326240633ac8e53bffc) \| [138](https://github.com/pinokiofactory/zonos/blob/0be13e4e803fe0834bae8326240633ac8e53bffc/cpp.py#L138) \| float16 / FP16 \| dtype declaration \| torch.float16, \|` |
| [quantization.md](../analysis/quantization.md) | `\| [zonos](https://github.com/pinokiofactory/zonos) \| [0be13e4](https://github.com/pinokiofactory/zonos/commit/0be13e4e803fe0834bae8326240633ac8e53bffc) \| [142](https://github.com/pinokiofactory/zonos/blob/0be13e4e803fe0834bae8326240633ac8e53bffc/cpp.py#L142) \| float64 \| dtype declaration \| torch.float64, \|` |
| [quantization.md](../analysis/quantization.md) | `\| [zonos](https://github.com/pinokiofactory/zonos) \| [0be13e4](https://github.com/pinokiofactory/zonos/commit/0be13e4e803fe0834bae8326240633ac8e53bffc) \| [143](https://github.com/pinokiofactory/zonos/blob/0be13e4e803fe0834bae8326240633ac8e53bffc/cpp.py#L143) \| float / FP32 \| dtype declaration \| torch.float, \|` |
| [quantization.md](../analysis/quantization.md) | `\| [zonos](https://github.com/pinokiofactory/zonos) \| [0be13e4](https://github.com/pinokiofactory/zonos/commit/0be13e4e803fe0834bae8326240633ac8e53bffc) \| [144](https://github.com/pinokiofactory/zonos/blob/0be13e4e803fe0834bae8326240633ac8e53bffc/cpp.py#L144) \| bfloat16 / BF16 \| dtype declaration \| torch.bfloat16, \|` |
| [quantization.md](../analysis/quantization.md) | `\| [zonos](https://github.com/pinokiofactory/zonos) \| [0be13e4](https://github.com/pinokiofactory/zonos/commit/0be13e4e803fe0834bae8326240633ac8e53bffc) \| [145](https://github.com/pinokiofactory/zonos/blob/0be13e4e803fe0834bae8326240633ac8e53bffc/cpp.py#L145) \| float16 / FP16 \| dtype declaration \| torch.float16, \|` |
| [quantization.md](../analysis/quantization.md) | `\| [zonos](https://github.com/pinokiofactory/zonos) \| [0be13e4](https://github.com/pinokiofactory/zonos/commit/0be13e4e803fe0834bae8326240633ac8e53bffc) \| [146](https://github.com/pinokiofactory/zonos/blob/0be13e4e803fe0834bae8326240633ac8e53bffc/cpp.py#L146) \| bool / bool_ \| dtype declaration \| torch.bool, \|` |
| [quantization.md](../analysis/quantization.md) | *117 more rows omitted* |
| [fusion.md](../analysis/fusion.md) | `\| [zonos](https://github.com/pinokiofactory/zonos) \| [0be13e4](https://github.com/pinokiofactory/zonos/commit/0be13e4e803fe0834bae8326240633ac8e53bffc) \| [cpp.py:4845](https://github.com/pinokiofactory/zonos/blob/0be13e4e803fe0834bae8326240633ac8e53bffc/cpp.py#L4845) \| Patched Inductor `cpp_epilogue_fusion_counter` — fused epilogues in Inductor's C++ backend \|` |
| [fusion.md](../analysis/fusion.md) | `\| [zonos](https://github.com/pinokiofactory/zonos) \| [0be13e4](https://github.com/pinokiofactory/zonos/commit/0be13e4e803fe0834bae8326240633ac8e53bffc) \| [start.js:6](https://github.com/pinokiofactory/zonos/blob/0be13e4e803fe0834bae8326240633ac8e53bffc/start.js#L6) \| `TORCHINDUCTOR_CACHE_DIR` set so compiled kernels are cached between runs \|` |
| [fusion.md](../analysis/fusion.md) | `\| [zonos](https://github.com/pinokiofactory/zonos) \| [0be13e4](https://github.com/pinokiofactory/zonos/commit/0be13e4e803fe0834bae8326240633ac8e53bffc) \| installed by launcher \| [torch.js:13](https://github.com/pinokiofactory/zonos/blob/0be13e4e803fe0834bae8326240633ac8e53bffc/torch.js#L13) — `"uv pip install https://huggingface.co/lldacing/flash-attention-windows-wheel/resolve/main/flash_attn-2.7.4.post1%2Bcu128torch2.7.0cxx11abiFALSE-cp310` \|` |
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
- [App flow graph](../flows/zonos.md)
<!-- cross-analysis:end -->
