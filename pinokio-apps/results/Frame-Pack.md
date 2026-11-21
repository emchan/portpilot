# Frame-Pack — portability analysis

- **Package name:** FramePack (`Frame-Pack`)
- **Description:** [NVIDIA ONLY] Generate Video Progressively. FramePack is a next-frame (next-frame-section) prediction neural network structure that generates videos progressively. https://github.com/lllyasviel/FramePack
- **Original git URL:** https://github.com/pinokiofactory/Frame-Pack
- **Analyzed commit:** `f0d7d1eba4155f5985a465d0476a9f926d0c6179`
- **Platforms supported:** NVIDIA only
- **Porting difficulty:** Very high
- **CUDA-only packages:** sageattention, triton, triton-windows, xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

devicetorch, diffusers, diffusers-helper, einops, gradio, hf-xet, numpy, pil, safetensors, sageattention, torch, torch-directml, torchaudio, torchvision, transformers, triton, triton-windows, xformers

Third-party Python imports detected in local source: diffusers, diffusers-helper, einops, gradio, numpy, pil, safetensors, torch, transformers.

Wheel indexes referenced: cpu, cu128, rocm6.3.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 1231
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- Explicit platform tag found: NVIDIA only.
- `torch.js` routes present: nvidia, amd, mac, cpu.
- No requirements file; third-party Python imports used as a fallback signal.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): xformers
- Difficulty score: 10.0 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- retested on Python 3.10; import failed on CUDA-only module-level code (torch.cuda.current_device()).
- Result: **not runnable in this container.**
<!-- cross-analysis:start -->
## Cross-analysis details

- **CPU category (cpu.md):** CPU-capable with shipped fallback
- **TPU suitability:** Possible - moderate port
- **TPU work needed:** replace CUDA attention kernels with TPU-compatible attention/SDPA/XLA; large BF16/FP16 GEMM workload; expect XLA compile/memory tuning; moderate device/kernel/runtime adaptation
- **Effort ranking (effort.md):** #85 — Very high
- **Effort blockers:** GPU-only attention: sageattention/triton/triton-windows/xformers; CUDA-only fused kernels need config change; large FP16/BF16 GEMM load
- **Precisions noted:** FP32, FP16, BF16, UINT8
- **Models/flows noted:** [hunyuanvideo-community/HunyuanVideo](https://huggingface.co/hunyuanvideo-community/HunyuanVideo), [lllyasviel/FramePackI2V_HY](https://huggingface.co/lllyasviel/FramePackI2V_HY), [lllyasviel/FramePack_F1_I2V_HY_20250503](https://huggingface.co/lllyasviel/FramePack_F1_I2V_HY_20250503), [lllyasviel/flux_redux_bfl](https://huggingface.co/lllyasviel/flux_redux_bfl)
- **Flow graph:** [flows/Frame-Pack.md](../flows/Frame-Pack.md)

### Snapshot verification (cloned analyzed commit)

- **Snapshot source:** `https://codeload.github.com/pinokiofactory/Frame-Pack/tar.gz/<analyzed commit>` extracted to `/tmp/opencode/pinokio-snapshots/Frame-Pack`
- **Files scanned:** 14 total (2 .py, 9 .js, 3 other)
- **Key files present:** pinokio.js, install.js, torch.js, start.js
- **TPU/CUDA-relevant signals:**
  - `xformers`: 5 match(es) (e.g. torch.js:11, torch.js:11)
  - `sageattention`: 4 match(es) (e.g. torch.js:13, torch.js:13)
  - `triton`: 3 match(es) (e.g. torch.js:12, torch.js:58)
  - `directml`: 1 match(es) (e.g. torch.js:25)

### Evidence from analysis files

| Source | Evidence |
|---|---|
| [kernels.md](../analysis/kernels.md) | `\| [Frame-Pack](https://github.com/pinokiofactory/Frame-Pack) \| [f0d7d1e](https://github.com/pinokiofactory/Frame-Pack/commit/f0d7d1eba4155f5985a465d0476a9f926d0c6179) \| launcher install \| install.js, torch.js \| [torch.js:12](https://github.com/pinokiofactory/Frame-Pack/blob/f0d7d1eba4155f5985a465d0476a9f926d0c6179/torch.js#L12) — "uv pip install triton-windows==3.3.1.post19", \|` |
| [kernels.md](../analysis/kernels.md) | `\| [Frame-Pack](https://github.com/pinokiofactory/Frame-Pack) \| [f0d7d1e](https://github.com/pinokiofactory/Frame-Pack/commit/f0d7d1eba4155f5985a465d0476a9f926d0c6179) \| launcher install \| [torch.js:13](https://github.com/pinokiofactory/Frame-Pack/blob/f0d7d1eba4155f5985a465d0476a9f926d0c6179/torch.js#L13) — "uv pip install https://github.com/woct0rdho/SageAttention/releases/download/v2.1.1-windows/sageattention-2.1.1+cu128torch2.7.0-cp310-cp310-win_amd64.whl",<br>[torch.js:59](https://github.com/pinokiofactory/Frame-Pack/blob/f0d7d1eba4155f5985a465d0476a9f926d0c6179/torch.js#L59) — "uv pip install https://huggingface.co/cocktailpeanut/wheels/resolve/main/sageattention-2.1.1%2Bcu128torch2.7.1-cp310-cp310-linux_x86_64.whl", \|` |
| [quantization.md](../analysis/quantization.md) | `\| [Frame-Pack](https://github.com/pinokiofactory/Frame-Pack) \| [f0d7d1e](https://github.com/pinokiofactory/Frame-Pack/commit/f0d7d1eba4155f5985a465d0476a9f926d0c6179) \| [49](https://github.com/pinokiofactory/Frame-Pack/blob/f0d7d1eba4155f5985a465d0476a9f926d0c6179/demo_gradio_f1.py#L49) \| float16 / FP16 \| dtype declaration \| text_encoder = LlamaModel.from_pretrained("hunyuanvideo-community/HunyuanVideo", subfolder='text_encoder', torch_dtype=torch.float16... \|` |
| [quantization.md](../analysis/quantization.md) | `\| [Frame-Pack](https://github.com/pinokiofactory/Frame-Pack) \| [f0d7d1e](https://github.com/pinokiofactory/Frame-Pack/commit/f0d7d1eba4155f5985a465d0476a9f926d0c6179) \| [50](https://github.com/pinokiofactory/Frame-Pack/blob/f0d7d1eba4155f5985a465d0476a9f926d0c6179/demo_gradio_f1.py#L50) \| float16 / FP16 \| dtype declaration \| text_encoder_2 = CLIPTextModel.from_pretrained("hunyuanvideo-community/HunyuanVideo", subfolder='text_encoder_2', torch_dtype=torch.... \|` |
| [quantization.md](../analysis/quantization.md) | `\| [Frame-Pack](https://github.com/pinokiofactory/Frame-Pack) \| [f0d7d1e](https://github.com/pinokiofactory/Frame-Pack/commit/f0d7d1eba4155f5985a465d0476a9f926d0c6179) \| [53](https://github.com/pinokiofactory/Frame-Pack/blob/f0d7d1eba4155f5985a465d0476a9f926d0c6179/demo_gradio_f1.py#L53) \| float16 / FP16 \| dtype declaration \| vae = AutoencoderKLHunyuanVideo.from_pretrained("hunyuanvideo-community/HunyuanVideo", subfolder='vae', torch_dtype=torch.float16).c... \|` |
| [quantization.md](../analysis/quantization.md) | `\| [Frame-Pack](https://github.com/pinokiofactory/Frame-Pack) \| [f0d7d1e](https://github.com/pinokiofactory/Frame-Pack/commit/f0d7d1eba4155f5985a465d0476a9f926d0c6179) \| [56](https://github.com/pinokiofactory/Frame-Pack/blob/f0d7d1eba4155f5985a465d0476a9f926d0c6179/demo_gradio_f1.py#L56) \| float16 / FP16 \| dtype declaration \| image_encoder = SiglipVisionModel.from_pretrained("lllyasviel/flux_redux_bfl", subfolder='image_encoder', torch_dtype=torch.float16)... \|` |
| [quantization.md](../analysis/quantization.md) | `\| [Frame-Pack](https://github.com/pinokiofactory/Frame-Pack) \| [f0d7d1e](https://github.com/pinokiofactory/Frame-Pack/commit/f0d7d1eba4155f5985a465d0476a9f926d0c6179) \| [58](https://github.com/pinokiofactory/Frame-Pack/blob/f0d7d1eba4155f5985a465d0476a9f926d0c6179/demo_gradio_f1.py#L58) \| bfloat16 / BF16 \| dtype declaration \| transformer = HunyuanVideoTransformer3DModelPacked.from_pretrained('lllyasviel/FramePack_F1_I2V_HY_20250503', torch_dtype=torch.bflo... \|` |
| [quantization.md](../analysis/quantization.md) | `\| [Frame-Pack](https://github.com/pinokiofactory/Frame-Pack) \| [f0d7d1e](https://github.com/pinokiofactory/Frame-Pack/commit/f0d7d1eba4155f5985a465d0476a9f926d0c6179) \| [73](https://github.com/pinokiofactory/Frame-Pack/blob/f0d7d1eba4155f5985a465d0476a9f926d0c6179/demo_gradio_f1.py#L73) \| bfloat16 / BF16 \| explicit cast \| transformer.to(dtype=torch.bfloat16) \|` |
| [quantization.md](../analysis/quantization.md) | `\| [Frame-Pack](https://github.com/pinokiofactory/Frame-Pack) \| [f0d7d1e](https://github.com/pinokiofactory/Frame-Pack/commit/f0d7d1eba4155f5985a465d0476a9f926d0c6179) \| [74](https://github.com/pinokiofactory/Frame-Pack/blob/f0d7d1eba4155f5985a465d0476a9f926d0c6179/demo_gradio_f1.py#L74) \| float16 / FP16 \| explicit cast \| vae.to(dtype=torch.float16) \|` |
| [quantization.md](../analysis/quantization.md) | `\| [Frame-Pack](https://github.com/pinokiofactory/Frame-Pack) \| [f0d7d1e](https://github.com/pinokiofactory/Frame-Pack/commit/f0d7d1eba4155f5985a465d0476a9f926d0c6179) \| [75](https://github.com/pinokiofactory/Frame-Pack/blob/f0d7d1eba4155f5985a465d0476a9f926d0c6179/demo_gradio_f1.py#L75) \| float16 / FP16 \| explicit cast \| image_encoder.to(dtype=torch.float16) \|` |
| [quantization.md](../analysis/quantization.md) | *21 more rows omitted* |
| [fusion.md](../analysis/fusion.md) | `\| [Frame-Pack](https://github.com/pinokiofactory/Frame-Pack) \| [f0d7d1e](https://github.com/pinokiofactory/Frame-Pack/commit/f0d7d1eba4155f5985a465d0476a9f926d0c6179) \| installed by launcher \| [torch.js:13](https://github.com/pinokiofactory/Frame-Pack/blob/f0d7d1eba4155f5985a465d0476a9f926d0c6179/torch.js#L13) — `"uv pip install https://github.com/woct0rdho/SageAttention/releases/download/v2.1.1-windows/sageattention-2.1.1+cu128torch2.7.0-cp310-cp310-win_amd64.` \|` |
| [fusion.md](../analysis/fusion.md) | `\| [Frame-Pack](https://github.com/pinokiofactory/Frame-Pack) \| [f0d7d1e](https://github.com/pinokiofactory/Frame-Pack/commit/f0d7d1eba4155f5985a465d0476a9f926d0c6179) \| 151 \| `to_q.weight` / `to_k.weight` / `to_v.weight` in `context_embedder.token_refiner.refiner_blocks.0.attn` (lllyasviel/FramePackI2V_HY, B=`[3072, 3072]`) \| [`Frame-Pack.md`](../flows/Frame-Pack.md) \|` |
| [fusion.md](../analysis/fusion.md) | `\| [Frame-Pack](https://github.com/pinokiofactory/Frame-Pack) \| [f0d7d1e](https://github.com/pinokiofactory/Frame-Pack/commit/f0d7d1eba4155f5985a465d0476a9f926d0c6179) \| 10 \| installed by launcher \| [`Frame-Pack.md`](../flows/Frame-Pack.md) \|` |
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
- [App flow graph](../flows/Frame-Pack.md)
<!-- cross-analysis:end -->
