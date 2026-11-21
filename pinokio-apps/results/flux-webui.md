# flux-webui — portability analysis

- **Package name:** flux-webui (`flux-webui`)
- **Description:** Minimal Flux Web UI powered by Gradio & Diffusers (Flux Schnell + Flux Merged)
- **Original git URL:** https://github.com/pinokiofactory/flux-webui
- **Analyzed commit:** `62d2f5692da1e0aaf776c3dceef0a720a6a24bb6`
- **Platforms supported:** NVIDIA / AMD / Mac
- **Porting difficulty:** High
- **CUDA-only packages:** flash-attn, sageattention *(optional)*, triton *(optional)*, triton-windows, xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

devicetorch, flash-attn, gradio, hf-xet, numpy, protobuf, sageattention, sentencepiece, torch, torch-directml, torchaudio, torchvision, transformers, triton, triton-windows, xformers

Requirements files: `requirements.txt`.

Third-party Python imports detected in local source: devicetorch, diffusers, gradio, numpy, optimum, pil, torch, transformers.

Wheel indexes referenced: cpu, cu128, rocm6.3.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 487
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- `torch.js` routes present: nvidia, amd, mac, cpu.
- Requirements from: requirements.txt
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): sageattention, triton, xformers
- Difficulty score: 7.8 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- retested on Python 3.12 with full requirements; importing app.py hung in this container.
- Result: **not runnable in this container.**
<!-- cross-analysis:start -->
## Cross-analysis details

- **CPU category (cpu.md):** CPU-capable with shipped fallback
- **TPU suitability:** Possible - moderate port
- **TPU work needed:** replace CUDA attention kernels with TPU-compatible attention/SDPA/XLA; large BF16/FP16 GEMM workload; expect XLA compile/memory tuning; moderate device/kernel/runtime adaptation
- **Effort ranking (effort.md):** #81 — High
- **Effort blockers:** GPU-only attention: flash-attn/sageattention/triton/triton-windows/xformers; CUDA-only fused kernels need config change; large FP16/BF16 GEMM load
- **Precisions noted:** FP32, BF16, INT8, INT32
- **Models/flows noted:** [black-forest-labs/FLUX.1-schnell](https://huggingface.co/black-forest-labs/FLUX.1-schnell), [cocktailpeanut/flux1-merged-q8](https://huggingface.co/cocktailpeanut/flux1-merged-q8), [cocktailpeanut/flux1-merged-qint8](https://huggingface.co/cocktailpeanut/flux1-merged-qint8), [cocktailpeanut/flux1-schnell-q8](https://huggingface.co/cocktailpeanut/flux1-schnell-q8), [cocktailpeanut/flux1-schnell-qint8](https://huggingface.co/cocktailpeanut/flux1-schnell-qint8), [sayakpaul/FLUX.1-merged](https://huggingface.co/sayakpaul/FLUX.1-merged)
- **Flow graph:** [flows/flux-webui.md](../flows/flux-webui.md)

### Snapshot verification (cloned analyzed commit)

- **Snapshot source:** `https://codeload.github.com/pinokiofactory/flux-webui/tar.gz/<analyzed commit>` extracted to `/tmp/opencode/pinokio-snapshots/flux-webui`
- **Files scanned:** 15 total (1 .py, 8 .js, 6 other)
- **Key files present:** pinokio.js, install.js, torch.js, start.js, requirements.txt
- **TPU/CUDA-relevant signals:**
  - `xformers`: 6 match(es) (e.g. torch.js:11, torch.js:11)
  - `flash_attn`: 2 match(es) (e.g. torch.js:14, torch.js:31)
  - `sageattention`: 4 match(es) (e.g. torch.js:13, torch.js:13)
  - `triton`: 5 match(es) (e.g. torch.js:12, torch.js:12)
  - `directml`: 1 match(es) (e.g. torch.js:44)
  - `mps`: 3 match(es) (e.g. README.md:26, app.py:74)

### Evidence from analysis files

| Source | Evidence |
|---|---|
| [kernels.md](../analysis/kernels.md) | `\| [flux-webui](https://github.com/pinokiofactory/flux-webui) \| [62d2f56](https://github.com/pinokiofactory/flux-webui/commit/62d2f5692da1e0aaf776c3dceef0a720a6a24bb6) \| optional flag + launcher install \| install.js, torch.js \| [torch.js:12](https://github.com/pinokiofactory/flux-webui/blob/62d2f5692da1e0aaf776c3dceef0a720a6a24bb6/torch.js#L12) — "{{args && args.triton ? 'uv pip install triton-windows==3.3.1.post19' : ''}}", \|` |
| [kernels.md](../analysis/kernels.md) | `\| [flux-webui](https://github.com/pinokiofactory/flux-webui) \| [62d2f56](https://github.com/pinokiofactory/flux-webui/commit/62d2f5692da1e0aaf776c3dceef0a720a6a24bb6) \| direct code \| [app.py:74](https://github.com/pinokiofactory/flux-webui/blob/62d2f5692da1e0aaf776c3dceef0a720a6a24bb6/app.py#L74) — if device == "mps":<br>[app.py:82](https://github.com/pinokiofactory/flux-webui/blob/62d2f5692da1e0aaf776c3dceef0a720a6a24bb6/app.py#L82) — if device == "mps": \|` |
| [kernels.md](../analysis/kernels.md) | `\| [flux-webui](https://github.com/pinokiofactory/flux-webui) \| [62d2f56](https://github.com/pinokiofactory/flux-webui/commit/62d2f5692da1e0aaf776c3dceef0a720a6a24bb6) \| optional flag + launcher install \| [torch.js:14](https://github.com/pinokiofactory/flux-webui/blob/62d2f5692da1e0aaf776c3dceef0a720a6a24bb6/torch.js#L14) — "{{args && args.flashattention ? 'uv pip install https://huggingface.co/cocktailpeanut/wheels/resolve/main/flash_attn-2.8.2%2Bcu128torch2.7-cp310-cp310-win_amd64....<br>[torch.js:31](https://github.com/pinokiofactory/flux-webui/blob/62d2f5692da1e0aaf776c3dceef0a720a6a24bb6/torch.js#L31) — "{{args && args.flashattention ? 'uv pip install https://huggingface.co/cocktailpeanut/wheels/resolve/main/flash_attn-2.8.3%2Bcu128torch2.7-cp310-cp310-linux_x86_... \|` |
| [kernels.md](../analysis/kernels.md) | `\| [flux-webui](https://github.com/pinokiofactory/flux-webui) \| [62d2f56](https://github.com/pinokiofactory/flux-webui/commit/62d2f5692da1e0aaf776c3dceef0a720a6a24bb6) \| optional flag + launcher install \| [torch.js:13](https://github.com/pinokiofactory/flux-webui/blob/62d2f5692da1e0aaf776c3dceef0a720a6a24bb6/torch.js#L13) — "{{args && args.sageattention ? 'uv pip install https://huggingface.co/cocktailpeanut/wheels/resolve/main/sageattention-2.1.1%2Bcu128torch2.7.1-cp310-cp310-win_am...<br>[torch.js:30](https://github.com/pinokiofactory/flux-webui/blob/62d2f5692da1e0aaf776c3dceef0a720a6a24bb6/torch.js#L30) — "{{args && args.sageattention ? 'uv pip install https://huggingface.co/cocktailpeanut/wheels/resolve/main/sageattention-2.1.1%2Bcu128torch2.7.1-cp310-cp310-linux_... \|` |
| [quantization.md](../analysis/quantization.md) | `\| [flux-webui](https://github.com/pinokiofactory/flux-webui) \| direct code \| `app.py:7` — from optimum.quanto import QuantizedDiffusersModel, QuantizedTransformersModel<br>`app.py:35` — class QuantizedFluxTransformer2DModel(QuantizedDiffusersModel): \|` |
| [quantization.md](../analysis/quantization.md) | `\| [flux-webui](https://github.com/pinokiofactory/flux-webui) \| direct code + requirements \| `app.py:7` — from optimum.quanto import QuantizedDiffusersModel, QuantizedTransformersModel<br>`requirements.txt:4` — git+https://github.com/peanutcocktail/optimum-quanto.git@feat-hub-support \|` |
| [quantization.md](../analysis/quantization.md) | `\| [flux-webui](https://github.com/pinokiofactory/flux-webui) \| [62d2f56](https://github.com/pinokiofactory/flux-webui/commit/62d2f5692da1e0aaf776c3dceef0a720a6a24bb6) \| [7](https://github.com/pinokiofactory/flux-webui/blob/62d2f5692da1e0aaf776c3dceef0a720a6a24bb6/app.py#L7) \| — \| quantization API \| from optimum.quanto import QuantizedDiffusersModel, QuantizedTransformersModel \|` |
| [quantization.md](../analysis/quantization.md) | `\| [flux-webui](https://github.com/pinokiofactory/flux-webui) \| [62d2f56](https://github.com/pinokiofactory/flux-webui/commit/62d2f5692da1e0aaf776c3dceef0a720a6a24bb6) \| [37](https://github.com/pinokiofactory/flux-webui/blob/62d2f5692da1e0aaf776c3dceef0a720a6a24bb6/app.py#L37) \| bfloat16 / BF16 \| dtype declaration \| dtype = torch.bfloat16 \|` |
| [quantization.md](../analysis/quantization.md) | `\| [flux-webui](https://github.com/pinokiofactory/flux-webui) \| [62d2f56](https://github.com/pinokiofactory/flux-webui/commit/62d2f5692da1e0aaf776c3dceef0a720a6a24bb6) \| [38](https://github.com/pinokiofactory/flux-webui/blob/62d2f5692da1e0aaf776c3dceef0a720a6a24bb6/app.py#L38) \| float / FP32 \| dtype declaration \| #dtype = torch.float32 \|` |
| [quantization.md](../analysis/quantization.md) | `\| [flux-webui](https://github.com/pinokiofactory/flux-webui) \| [62d2f56](https://github.com/pinokiofactory/flux-webui/commit/62d2f5692da1e0aaf776c3dceef0a720a6a24bb6) \| [40](https://github.com/pinokiofactory/flux-webui/blob/62d2f5692da1e0aaf776c3dceef0a720a6a24bb6/app.py#L40) \| int32 \| dtype declaration \| MAX_SEED = np.iinfo(np.int32).max \|` |
| [quantization.md](../analysis/quantization.md) | `\| [flux-webui](https://github.com/pinokiofactory/flux-webui) \| [62d2f56](https://github.com/pinokiofactory/flux-webui/commit/62d2f5692da1e0aaf776c3dceef0a720a6a24bb6) \| [75](https://github.com/pinokiofactory/flux-webui/blob/62d2f5692da1e0aaf776c3dceef0a720a6a24bb6/app.py#L75) \| int8 / qint8 \| dtype declaration \| transformer = QuantizedFluxTransformer2DModel.from_pretrained("cocktailpeanut/flux1-merged-qint8") \|` |
| [quantization.md](../analysis/quantization.md) | `\| [flux-webui](https://github.com/pinokiofactory/flux-webui) \| [62d2f56](https://github.com/pinokiofactory/flux-webui/commit/62d2f5692da1e0aaf776c3dceef0a720a6a24bb6) \| [83](https://github.com/pinokiofactory/flux-webui/blob/62d2f5692da1e0aaf776c3dceef0a720a6a24bb6/app.py#L83) \| int8 / qint8 \| dtype declaration \| transformer = QuantizedFluxTransformer2DModel.from_pretrained("cocktailpeanut/flux1-schnell-qint8") \|` |
| [quantization.md](../analysis/quantization.md) | *2 more rows omitted* |
| [fusion.md](../analysis/fusion.md) | `\| [flux-webui](https://github.com/pinokiofactory/flux-webui) \| [62d2f56](https://github.com/pinokiofactory/flux-webui/commit/62d2f5692da1e0aaf776c3dceef0a720a6a24bb6) \| optional launcher flag \| [torch.js:13](https://github.com/pinokiofactory/flux-webui/blob/62d2f5692da1e0aaf776c3dceef0a720a6a24bb6/torch.js#L13) — `"{{args && args.sageattention ? 'uv pip install https://huggingface.co/cocktailpeanut/wheels/resolve/main/sageattention-2.1.1%2Bcu128torch2.7.1-cp310-` \|` |
| [fusion.md](../analysis/fusion.md) | `\| [flux-webui](https://github.com/pinokiofactory/flux-webui) \| [62d2f56](https://github.com/pinokiofactory/flux-webui/commit/62d2f5692da1e0aaf776c3dceef0a720a6a24bb6) \| 36 \| `q_proj.weight` / `k_proj.weight` / `v_proj.weight` in `text_model.encoder.layers.0.self_attn` (sayakpaul/FLUX.1-merged, B=`[768, 768]`) \| [`flux-webui.md`](../flows/flux-webui.md) \|` |
| [fusion.md](../analysis/fusion.md) | `\| [flux-webui](https://github.com/pinokiofactory/flux-webui) \| [62d2f56](https://github.com/pinokiofactory/flux-webui/commit/62d2f5692da1e0aaf776c3dceef0a720a6a24bb6) \| 3 \| optional launcher flag \| [`flux-webui.md`](../flows/flux-webui.md) \|` |
| [models.md](../analysis/models.md) | No model pull/shape row matched in models.md. |
| [cpu.md](../analysis/cpu.md) | CPU category: **CPU-capable with shipped fallback** |
| [tpu.md](../analysis/tpu.md) | TPU suitability: **Possible - moderate port** — replace CUDA attention kernels with TPU-compatible attention/SDPA/XLA; large BF16/FP16 GEMM workload; expect XLA compile/memory tuning; moderate device/kernel/runtime adaptation |

### Related analysis

- [CPU analysis](../analysis/cpu.md)
- [TPU analysis](../analysis/tpu.md)
- [Effort ranking](../analysis/effort.md)
- [Kernel evidence](../analysis/kernels.md)
- [Quantization evidence](../analysis/quantization.md)
- [Fusion evidence](../analysis/fusion.md)
- [Model pulls/shapes](../analysis/models.md)
- [Flow graphs](../analysis/flows.md)
- [App flow graph](../flows/flux-webui.md)
<!-- cross-analysis:end -->
