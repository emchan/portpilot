# dia — portability analysis

- **Package name:** Dia (`dia`)
- **Description:** Dia is a 1.6B parameter text to speech model created by Nari Labs. Dia directly generates highly realistic dialogue from a transcript. You can condition the output on audio, enabling emotion and tone control. The model can also produce nonverbal communications like laughter, coughing, clearing throa
- **Original git URL:** https://github.com/pinokiofactory/dia
- **Analyzed commit:** `17e1912e77363efc198d52a5ae813caaa8d3da90`
- **Platforms supported:** NVIDIA / AMD / Mac
- **Porting difficulty:** Medium
- **CUDA-only packages:** sageattention *(optional)*, triton-windows, xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

gradio, numpy, sageattention, torch, torch-directml, torchaudio, torchvision, triton-windows, xformers

Wheel indexes referenced: cpu, cu128, rocm6.3.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 292
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- `torch.js` routes present: nvidia, amd, mac, cpu.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): sageattention, triton, xformers
- Difficulty score: 4.0 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- retested on Python 3.12; importing app.py hung in this container.
- Result: **not runnable in this container.**
<!-- cross-analysis:start -->
## Cross-analysis details

- **CPU category (cpu.md):** CPU-capable with shipped fallback
- **TPU suitability:** Possible - moderate port
- **TPU work needed:** replace CUDA attention kernels with TPU-compatible attention/SDPA/XLA; moderate device/kernel/runtime adaptation
- **Effort ranking (effort.md):** #56 — Medium
- **Effort blockers:** GPU-only attention: sageattention/triton-windows/xformers; CUDA-only fused kernels need config change
- **Precisions noted:** unspecified
- **Models/flows noted:** —
- **Flow graph:** [flows/dia.md](../flows/dia.md)

### Snapshot verification (cloned analyzed commit)

- **Snapshot source:** `https://codeload.github.com/pinokiofactory/dia/tar.gz/<analyzed commit>` extracted to `/tmp/opencode/pinokio-snapshots/dia`
- **Files scanned:** 11 total (0 .py, 7 .js, 4 other)
- **Key files present:** pinokio.js, install.js, torch.js, start.js
- **TPU/CUDA-relevant signals:**
  - `xformers`: 5 match(es) (e.g. torch.js:11, torch.js:11)
  - `sageattention`: 6 match(es) (e.g. torch.js:13, torch.js:13)
  - `triton`: 3 match(es) (e.g. torch.js:12, torch.js:12)
  - `directml`: 1 match(es) (e.g. torch.js:26)

### Evidence from analysis files

| Source | Evidence |
|---|---|
| [kernels.md](../analysis/kernels.md) | `\| [dia](https://github.com/pinokiofactory/dia) \| [17e1912](https://github.com/pinokiofactory/dia/commit/17e1912e77363efc198d52a5ae813caaa8d3da90) \| optional flag + launcher install \| install.js, torch.js \| [torch.js:12](https://github.com/pinokiofactory/dia/blob/17e1912e77363efc198d52a5ae813caaa8d3da90/torch.js#L12) — "{{args && args.triton ? 'uv pip install triton-windows==3.3.1.post19' : ''}}", \|` |
| [kernels.md](../analysis/kernels.md) | `\| [dia](https://github.com/pinokiofactory/dia) \| [17e1912](https://github.com/pinokiofactory/dia/commit/17e1912e77363efc198d52a5ae813caaa8d3da90) \| optional flag + launcher install \| [torch.js:13](https://github.com/pinokiofactory/dia/blob/17e1912e77363efc198d52a5ae813caaa8d3da90/torch.js#L13) — "{{args && args.sageattention ? 'uv pip install https://github.com/woct0rdho/SageAttention/releases/download/v2.1.1-windows/sageattention-2.1.1+cu128torch2.7.0-cp...<br>[torch.js:63](https://github.com/pinokiofactory/dia/blob/17e1912e77363efc198d52a5ae813caaa8d3da90/torch.js#L63) — "{{args && args.sageattention ? 'uv pip install git+https://github.com/thu-ml/SageAttention.git' : ''}}" \|` |
| [quantization.md](../analysis/quantization.md) | No per-repo quantization table row matched; see quantization.md. |
| [fusion.md](../analysis/fusion.md) | `\| [Nari-Dia-TTS](https://github.com/pinokiofactory/Nari-Dia-TTS) \| [e5b630d](https://github.com/pinokiofactory/Nari-Dia-TTS/commit/e5b630df297c7f47f6c518a00d6c3f44be4e25b5) \| [dia/model.py:341](https://github.com/pinokiofactory/Nari-Dia-TTS/blob/e5b630df297c7f47f6c518a00d6c3f44be4e25b5/dia/model.py#L341) \| Direct `torch.compile(..., mode='default')` on the decoder decode step \|` |
| [fusion.md](../analysis/fusion.md) | `\| [dia](https://github.com/pinokiofactory/dia) \| [17e1912](https://github.com/pinokiofactory/dia/commit/17e1912e77363efc198d52a5ae813caaa8d3da90) \| optional launcher flag \| [torch.js:13](https://github.com/pinokiofactory/dia/blob/17e1912e77363efc198d52a5ae813caaa8d3da90/torch.js#L13) — `"{{args && args.sageattention ? 'uv pip install https://github.com/woct0rdho/SageAttention/releases/download/v2.1.1-windows/sageattention-2.1.1+cu128t` \|` |
| [fusion.md](../analysis/fusion.md) | `\| [Nari-Dia-TTS](https://github.com/pinokiofactory/Nari-Dia-TTS) \| [e5b630d](https://github.com/pinokiofactory/Nari-Dia-TTS/commit/e5b630df297c7f47f6c518a00d6c3f44be4e25b5) \| direct code \| [dia/layers.py:392](https://github.com/pinokiofactory/Nari-Dia-TTS/blob/e5b630df297c7f47f6c518a00d6c3f44be4e25b5/dia/layers.py#L392) — `attn_output = F.scaled_dot_product_attention(` \|` |
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
- [App flow graph](../flows/dia.md)
<!-- cross-analysis:end -->
