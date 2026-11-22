# StreamDiffusion — portability analysis

- **Package name:** StreamDiffusion (`StreamDiffusion`)
- **Description:** StreamDiffusion: A Pipeline-Level Solution for Real-Time Interactive Generation
- **Original git URL:** https://github.com/pinokiofactory/StreamDiffusion
- **Analyzed commit:** `0e529aaff2ff344ce15565420e0c484688eb1bc9`
- **Platforms supported:** NVIDIA only
- **Porting difficulty:** Very high
- **CUDA-only packages:** stable-fast, tensorrt, torch (CUDA wheel), triton, xformers

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

accelerate, av, compel, controlnet-aux, diffusers, fastapi, gradio, markdown2, matplotlib, mss, peft, pillow, stable-fast, torch, transformers, uvicorn, xformers

Requirements files: `demo/realtime-img2img/requirements.txt`, `demo/realtime-txt2img/requirements.txt`, `demo/vid2vid/requirements.txt`, `examples/screen/requirements.txt`, `examples/vid2vid/requirements.txt`.

Third-party Python imports detected in local source: cuda, diffusers, fastapi, fire, gradio, markdown2, mss, numpy, onnx, onnx-graphsurgeon, packaging, pil, polygraphy, pydantic, requests, setuptools, sfast, starlette, streamdiffusion, tensorrt, torch, torchvision, tqdm, transformers, triton, utils, uvicorn, xformers.

Wheel indexes referenced: cu121.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 6347
- **CUDA-related functions used:** `cudaGraphInstantiate`, `cudaGraphLaunch`, `cudaMemGetInfo`, `cudaStreamBeginCapture`, `cudaStreamEndCapture`, `cudaStreamSynchronize`, `torch.cuda.Event`, `torch.cuda.empty_cache`, `torch.cuda.is_available`, `torch.cuda.synchronize`

## Evidence and notes

- `torch.js` routes present: none.
- Requirements from: demo/realtime-img2img/requirements.txt, demo/realtime-txt2img/requirements.txt, demo/vid2vid/requirements.txt, examples/screen/requirements.txt, examples/vid2vid/requirements.txt
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Difficulty score: 15.0 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- dependencies installed and streamdiffusion imported successfully on CPU (TensorRT not required for import).
- Result: **CPU port imports successfully.**

## CPU port attempt

- **Attempt order:** #98 of 101 (by porting effort, easiest first).
- **Status:** Blocked.
- **Changes applied / required:** use existing non-GPU launcher route; keep explicit device='cpu' branch; replace direct torch.cuda calls with devicetorch or cpu fallback; disable fused GPU kernels (xformers/flash/sage) in config; substitute GPU-only attention libs with SDPA math backend; remove GPU runtimes (onnxruntime-gpu/deepspeed/cudnn/tensorrt); +2.
- **Smoke check:** pass (36/36 files).
- **Blockers:** hard CUDA/TensorRT blocker; GPU-only attention: triton/xformers; GPU runtime: tensorrt; CUDA-only torch wheel; +2.
- **Scope note:** static portability review of the Pinokio wrapper; no install or model download was executed.
<!-- cross-analysis:start -->
## Cross-analysis details

- **CPU category (cpu.md):** Hard-blocked on CUDA
- **TPU suitability:** Hard - major rewrite/replacement required
- **TPU work needed:** CUDA/TensorRT/compiled CUDA extension dependency
- **Effort ranking (effort.md):** #98 — Very high
- **Effort blockers:** hard CUDA/TensorRT blocker in code; GPU-only attention: triton/xformers; CUDA-only torch wheel; direct `torch.cuda` calls; CUDA-only fused kernels need config change; +1 more
- **Precisions noted:** FP32, FP16, INT8, UINT8, INT16, INT32, INT64, FP64, BOOL, COMPLEX
- **Models/flows noted:** [KBlueLeaf/kohaku-v2.1](https://huggingface.co/KBlueLeaf/kohaku-v2.1), [latent-consistency/lcm-lora-sdv1-5](https://huggingface.co/latent-consistency/lcm-lora-sdv1-5), [madebyollin/taesd](https://huggingface.co/madebyollin/taesd), [stabilityai/sd-turbo](https://huggingface.co/stabilityai/sd-turbo)
- **Flow graph:** [flows/StreamDiffusion.md](../flows/StreamDiffusion.md)

### Snapshot verification (cloned analyzed commit)

- **Snapshot source:** `https://codeload.github.com/pinokiofactory/StreamDiffusion/tar.gz/<analyzed commit>` extracted to `/tmp/opencode/pinokio-snapshots/StreamDiffusion`
- **Files scanned:** 139 total (36 .py, 4 .js, 99 other)
- **Key files present:** pyproject.toml
- **TPU/CUDA-relevant signals:**
  - `torch_cuda`: 20 match(es) (e.g. utils/wrapper.py:621, src/streamdiffusion/pipeline.py:443)
  - `xformers`: 57 match(es) (e.g. README.md:100, README.md:106)
  - `triton`: 3 match(es) (e.g. src/streamdiffusion/acceleration/sfast/__init__.py:14, src/streamdiffusion/acceleration/sfast/__init__.py:22)
  - `tensorrt`: 125 match(es) (e.g. README.md:119, README.md:126)
  - `cuda_graph`: 2 match(es) (e.g. src/streamdiffusion/acceleration/tensorrt/utilities.py:270, src/streamdiffusion/acceleration/tensorrt/utilities.py:283)

### Evidence from analysis files

| Source | Evidence |
|---|---|
| [kernels.md](../analysis/kernels.md) | `\| [StreamDiffusion](https://github.com/pinokiofactory/StreamDiffusion) \| [0e529aa](https://github.com/pinokiofactory/StreamDiffusion/commit/0e529aaff2ff344ce15565420e0c484688eb1bc9) \| direct code \| src/streamdiffusion/acceleration/sfast/__init__.py \| [src/streamdiffusion/acceleration/sfast/__init__.py:14](https://github.com/pinokiofactory/StreamDiffusion/blob/0e529aaff2ff344ce15565420e0c484688eb1bc9/src/streamdiffusion/acceleration/sfast/__init__.py#L14) — # xformers and Triton are suggested for achieving best performance. \|` |
| [quantization.md](../analysis/quantization.md) | `\| [StreamDiffusion](https://github.com/pinokiofactory/StreamDiffusion) \| reference \| `src/streamdiffusion/acceleration/tensorrt/utilities.py:52` — np.int8: torch.int8, \|` |
| [quantization.md](../analysis/quantization.md) | `\| [StreamDiffusion](https://github.com/pinokiofactory/StreamDiffusion) \| [0e529aa](https://github.com/pinokiofactory/StreamDiffusion/commit/0e529aaff2ff344ce15565420e0c484688eb1bc9) \| [198](https://github.com/pinokiofactory/StreamDiffusion/blob/0e529aaff2ff344ce15565420e0c484688eb1bc9/README-ko.md#L198) \| float16 / FP16 \| checkpoint / config \| dtype=torch.float16, \|` |
| [quantization.md](../analysis/quantization.md) | `\| [StreamDiffusion](https://github.com/pinokiofactory/StreamDiffusion) \| [0e529aa](https://github.com/pinokiofactory/StreamDiffusion/commit/0e529aaff2ff344ce15565420e0c484688eb1bc9) \| [205](https://github.com/pinokiofactory/StreamDiffusion/blob/0e529aaff2ff344ce15565420e0c484688eb1bc9/README-ko.md#L205) \| float16 / FP16 \| checkpoint / config \| torch_dtype=torch.float16, \|` |
| [quantization.md](../analysis/quantization.md) | `\| [StreamDiffusion](https://github.com/pinokiofactory/StreamDiffusion) \| [0e529aa](https://github.com/pinokiofactory/StreamDiffusion/commit/0e529aaff2ff344ce15565420e0c484688eb1bc9) \| [249](https://github.com/pinokiofactory/StreamDiffusion/blob/0e529aaff2ff344ce15565420e0c484688eb1bc9/README-ko.md#L249) \| float16 / FP16 \| checkpoint / config \| dtype=torch.float16, \|` |
| [quantization.md](../analysis/quantization.md) | `\| [StreamDiffusion](https://github.com/pinokiofactory/StreamDiffusion) \| [0e529aa](https://github.com/pinokiofactory/StreamDiffusion/commit/0e529aaff2ff344ce15565420e0c484688eb1bc9) \| [258](https://github.com/pinokiofactory/StreamDiffusion/blob/0e529aaff2ff344ce15565420e0c484688eb1bc9/README-ko.md#L258) \| float16 / FP16 \| checkpoint / config \| torch_dtype=torch.float16, \|` |
| [quantization.md](../analysis/quantization.md) | `\| [StreamDiffusion](https://github.com/pinokiofactory/StreamDiffusion) \| [0e529aa](https://github.com/pinokiofactory/StreamDiffusion/commit/0e529aaff2ff344ce15565420e0c484688eb1bc9) \| [322](https://github.com/pinokiofactory/StreamDiffusion/blob/0e529aaff2ff344ce15565420e0c484688eb1bc9/README-ko.md#L322) \| float16 / FP16 \| checkpoint / config \| torch_dtype=torch.float16, \|` |
| [quantization.md](../analysis/quantization.md) | `\| [StreamDiffusion](https://github.com/pinokiofactory/StreamDiffusion) \| [0e529aa](https://github.com/pinokiofactory/StreamDiffusion/commit/0e529aaff2ff344ce15565420e0c484688eb1bc9) \| [360](https://github.com/pinokiofactory/StreamDiffusion/blob/0e529aaff2ff344ce15565420e0c484688eb1bc9/README-ko.md#L360) \| float16 / FP16 \| checkpoint / config \| torch_dtype=torch.float16, \|` |
| [quantization.md](../analysis/quantization.md) | `\| [StreamDiffusion](https://github.com/pinokiofactory/StreamDiffusion) \| [0e529aa](https://github.com/pinokiofactory/StreamDiffusion/commit/0e529aaff2ff344ce15565420e0c484688eb1bc9) \| [203](https://github.com/pinokiofactory/StreamDiffusion/blob/0e529aaff2ff344ce15565420e0c484688eb1bc9/README-ja.md#L203) \| float16 / FP16 \| checkpoint / config \| dtype=torch.float16, \|` |
| [quantization.md](../analysis/quantization.md) | *66 more rows omitted* |
| [fusion.md](../analysis/fusion.md) | `\| Graph-engine fusion (TensorRT) \| 1 \| StreamDiffusion builds and refits TensorRT engines \|` |
| [fusion.md](../analysis/fusion.md) | `\| CUDA Graph capture (launch fusion) \| 1 \| StreamDiffusion TensorRT path; see [`kernels.md`](kernels.md) \|` |
| [fusion.md](../analysis/fusion.md) | `\| [StreamDiffusion](https://github.com/pinokiofactory/StreamDiffusion) \| [0e529aa](https://github.com/pinokiofactory/StreamDiffusion/commit/0e529aaff2ff344ce15565420e0c484688eb1bc9) \| direct code \| [utils/wrapper.py:469](https://github.com/pinokiofactory/StreamDiffusion/blob/0e529aaff2ff344ce15565420e0c484688eb1bc9/utils/wrapper.py#L469) — `stream.pipe.enable_xformers_memory_efficient_attention()` \|` |
| [models.md](../analysis/models.md) | No model pull/shape row matched in models.md. |
| [cpu.md](../analysis/cpu.md) | CPU category: **Hard-blocked on CUDA** |
| [tpu.md](../analysis/tpu.md) | TPU suitability: **Hard - major rewrite/replacement required** — CUDA/TensorRT/compiled CUDA extension dependency |

### Related analysis

- [CPU analysis](../analysis/cpu.md)
- [TPU analysis](../analysis/tpu.md)
- [Effort ranking](../analysis/effort.md)
- [Kernel evidence](../analysis/kernels.md)
- [Quantization evidence](../analysis/quantization.md)
- [Fusion evidence](../analysis/fusion.md)
- [Model pulls/shapes](../analysis/models.md)
- [Flow graphs](../analysis/flows.md)
- [App flow graph](../flows/StreamDiffusion.md)
<!-- cross-analysis:end -->

## Snapdragon evaluation (deep clone)
- **Clone/scan status:** cloned and scanned
- **Files scanned:** 139 total (36 .py, 15 .js/.ts, 88 other)
- **Snapdragon-relevant signals:** cuda=97, torch=246, triton=4, xformers=59, tensorrt=101, mps=2, jax=3, safetensors=1
- **Example evidence:**
  - cuda: `README-ja.md:99`
  - torch: `README-ja.md:97`
  - triton: `src/streamdiffusion/acceleration/sfast/__init__.py:14`
  - xformers: `README-ja.md:104`
  - tensorrt: `README-ja.md:123`
  - mps: `demo/realtime-img2img/frontend/package-lock.json:2704`
  - jax: `demo/realtime-txt2img/frontend/pnpm-lock.yaml:69`
  - safetensors: `demo/realtime-txt2img/config.py:30`
- **Snapdragon verdict:** Contains CUDA/Triton/TensorRT signals; Snapdragon path requires replacement or ONNX conversion.
