# Quantization, GGUF and quantization libraries in Pinokio apps

Companion to [`results/pinokio-apps.md`](../results/pinokio-apps.md) and [`kernels.md`](kernels.md). This note records which Pinokio Factory repositories reference quantized weights, GGUF files, or quantization libraries. Evidence is from a case-insensitive scan of text files in all 101 repository snapshots, cited as `file:line`. A match in a launcher script means the app installs or downloads the format; a match in `.py` means the wrapper itself uses a quantization API. Matches that are merely dtype names (`torch.int8`), audio codec quantizers, or false positives are called out explicitly. All snapshots were taken from the default branch `main` on 2026-11-20; the exact commit SHA analyzed for each repository is recorded in its `../results/<repo>.md` report.

## At a glance

| Signal | Repos | Examples |
| --- | --- | --- |
| Quantized weights / runtime quantization | 9 | comfy, flux-webui, mlx-video-ui, Nari-Dia-TTS, stable-diffusion-webui-forge, StreamDiffusion … |
| GGUF / llama.cpp | 3 | comfy, Orpheus-TTS-FastAPI, wan |
| bitsandbytes / NF4 | 7 | comfy, diffrhythm, hallo, llamafactory, MagicQuill, stable-diffusion-webui-forge … |
| torchao / torch.ao | 2 | echomimic2, ominicontrol |
| optimum-quanto | 1 | flux-webui |
| GPTQ | 0 | none |
| AWQ | 0 | none |
| ExLlama | 0 | none |
| HQQ | 0 | none |
| ONNX Runtime quantization | 0 | none |
| TensorRT INT8/FP8 | 0 | none |
| vLLM quantization | 0 | none |
| MLX runtime quantization flags | 1 | mlx-video-ui |

## Quantized weights and runtime quantization

Six wrappers actively use quantized weights or quantization settings (ComfyUI, Flux WebUI, MLX Video UI, Forge, UNO and Yue); the other three matches are not weight quantization (dtype tables or an audio codec).

| Project | How used | Evidence |
| --- | --- | --- |
| [comfy](https://github.com/pinokiofactory/comfy) | reference | `download-flux-dev-fp8.json:8` — "files": "flux1-dev-fp8.safetensors",<br>`download-flux-schnell-fp8.json:8` — "files": "flux1-schnell-fp8.safetensors", |
| [flux-webui](https://github.com/pinokiofactory/flux-webui) | direct code | `app.py:7` — from optimum.quanto import QuantizedDiffusersModel, QuantizedTransformersModel<br>`app.py:35` — class QuantizedFluxTransformer2DModel(QuantizedDiffusersModel): |
| [mlx-video-ui](https://github.com/pinokiofactory/mlx-video-ui) | env/config flag | `backend.js:39` — // Default to runtime quantization for stability (avoid broken pre-quant snapshots).<br>`backend.js:41` — //   LTX_USE_PREQUANT=1 |
| [Nari-Dia-TTS](https://github.com/pinokiofactory/Nari-Dia-TTS) | direct code | `dia/audio.py:234` — audio_values = model.quantizer.from_codes(audio_codes) |
| [stable-diffusion-webui-forge](https://github.com/pinokiofactory/stable-diffusion-webui-forge) | reference | `install.js:99` — "hf download lllyasviel/flux1-dev-bnb-nf4 flux1-dev-bnb-nf4-v2.safetensors --local-dir app/models/Stable-diffusion"<br>`install.js:108` — "hf download lllyasviel/flux1_dev flux1-dev-fp8.safetensors --local-dir app/models/Stable-diffusion" |
| [StreamDiffusion](https://github.com/pinokiofactory/StreamDiffusion) | reference | `src/streamdiffusion/acceleration/tensorrt/utilities.py:52` — np.int8: torch.int8, |
| [uno](https://github.com/pinokiofactory/uno) | reference | `pinokio.js:69` — text: "Start FP8 Model (Low VRAM)",<br>`pinokio.js:72` — name: "flux-dev-fp8" |
| [yue](https://github.com/pinokiofactory/yue) | reference | `pinokio.js:77` — text: "12g vram (quantized)",<br>`pinokio.js:84` — text: "10g vram (quantized)", |
| [zonos](https://github.com/pinokiofactory/zonos) | reference | `cpp.py:148` — torch.int8,<br>`cpp.py:158` — torch.int8, |

The `Nari-Dia-TTS` `model.quantizer` call is Dia's residual-vector-quantizer audio tokenizer, `StreamDiffusion`'s `np.int8` and `zonos`' `torch.int8` lines are dtype mappings/Inductor internals — none of them quantize model weights.

## GGUF

Three repositories reference GGUF or a GGUF-capable runtime:

| Project | How used | Evidence |
| --- | --- | --- |
| [comfy](https://github.com/pinokiofactory/comfy) | reference | `download-flux-schnell-gguf-q4-0.json:7` — "repo": "city96/FLUX.1-schnell-gguf",<br>`download-flux-schnell-gguf-q4-0.json:8` — "files": "flux1-schnell-Q4_0.gguf", |
| [Orpheus-TTS-FastAPI](https://github.com/pinokiofactory/Orpheus-TTS-FastAPI) | reference | `start.js:16` — '{{which("lms")}} get https://huggingface.co/lex-au/Orpheus-3b-FT-Q8_0.gguf/resolve/main/Orpheus-3b-FT-Q8_0.gguf -y',<br>`start.js:17` — '{{which("lms")}} load orpheus-3b-ft.gguf -y' |
| [wan](https://github.com/pinokiofactory/wan) | launcher install | `torch.js:29` — "uv pip install https://github.com/deepbeepmeep/kernels/releases/download/gguf-v1.0.29/llamacpp_gguf_cuda-1.0.29%2Btorch210cu130py311-cp311-cp311-win_amd64.whl --...<br>`torch.js:52` — "uv pip install https://github.com/deepbeepmeep/kernels/releases/download/gguf-v1.0.29/llamacpp_gguf_cuda-1.0.29%2Btorch210cu130py311-cp311-cp311-win_amd64.whl --... |

**Porting note:** GGUF is a container format; the compute comes from the loader. llama.cpp has CPU, CUDA, Vulkan and Metal backends, so GGUF is potentially the most portable quantization route here. Wan, however, installs a CUDA-only `llamacpp_gguf_cuda` wheel, so its current path still needs a ROCm/Metal replacement. Orpheus-TTS-FastAPI delegates to LM Studio, inheriting that tool's backend support.

## Quantization libraries

### bitsandbytes / NF4

| Project | How used | Evidence |
| --- | --- | --- |
| [comfy](https://github.com/pinokiofactory/comfy) | launcher install | `download-flux-dev-nf4.json:7` — "repo": "lllyasviel/flux1-dev-bnb-nf4",<br>`download-flux-dev-nf4.json:8` — "files": "flux1-dev-bnb-nf4.safetensors", |
| [diffrhythm](https://github.com/pinokiofactory/diffrhythm) | requirements | `requirements.txt:12` — bitsandbytes==0.45.3 |
| [hallo](https://github.com/pinokiofactory/hallo) | requirements | `requirements.txt:4` — #bitsandbytes==0.43.1<br>`requirements.txt:5` — bitsandbytes |
| [llamafactory](https://github.com/pinokiofactory/llamafactory) | launcher install | `install.js:32` — "uv pip install bitsandbytes --no-deps", |
| [MagicQuill](https://github.com/pinokiofactory/MagicQuill) | launcher install | `torch.js:75` — "uv pip install https://github.com/bitsandbytes-foundation/bitsandbytes/releases/download/continuous-release_multi-backend-refactor/bitsandbytes-0.44.1.dev0-py3-n... |
| [stable-diffusion-webui-forge](https://github.com/pinokiofactory/stable-diffusion-webui-forge) | reference | `install.js:99` — "hf download lllyasviel/flux1-dev-bnb-nf4 flux1-dev-bnb-nf4-v2.safetensors --local-dir app/models/Stable-diffusion"<br>`download-flux1-schnell-nf4.json:5` — "uri": "https://huggingface.co/silveroxides/flux1-nf4-weights/resolve/main/flux1-schnell-bnb-nf4.safetensors?download=true", |
| [wan](https://github.com/pinokiofactory/wan) | launcher install | `torch.js:32` — "uv pip install bitsandbytes==0.49.2 --no-deps"<br>`torch.js:55` — "uv pip install bitsandbytes==0.49.2 --no-deps" |

### torchao

| Project | How used | Evidence |
| --- | --- | --- |
| [echomimic2](https://github.com/pinokiofactory/echomimic2) | launcher install | `torch.js:13` — "uv pip install torchao==0.12.0"<br>`torch.js:27` — "uv pip install torchao==0.14.1 --index-url https://download.pytorch.org/whl/cu128", |
| [ominicontrol](https://github.com/pinokiofactory/ominicontrol) | launcher install | `install.js:35` — "pip install --pre torchao --index-url https://download.pytorch.org/whl/nightly/cu121" |

### optimum-quanto

| Project | How used | Evidence |
| --- | --- | --- |
| [flux-webui](https://github.com/pinokiofactory/flux-webui) | direct code + requirements | `app.py:7` — from optimum.quanto import QuantizedDiffusersModel, QuantizedTransformersModel<br>`requirements.txt:4` — git+https://github.com/peanutcocktail/optimum-quanto.git@feat-hub-support |

### MLX runtime quantization

| Project | How used | Evidence |
| --- | --- | --- |
| [mlx-video-ui](https://github.com/pinokiofactory/mlx-video-ui) | env/config flag | `backend.js:39` — // Default to runtime quantization for stability (avoid broken pre-quant snapshots).<br>`backend.js:41` — //   LTX_USE_PREQUANT=1<br>`backend.js:42` — //   LTX_ALLOW_UNSAFE_PREQUANT=1<br>`backend.js:43` — LTX_USE_PREQUANT: "{{envs.LTX_USE_PREQUANT \|\| '0'}}",<br>`backend.js:44` — LTX_ALLOW_UNSAFE_PREQUANT: "{{envs.LTX_ALLOW_UNSAFE_PREQUANT \|\| '0'}}",<br>`backend.js:45` — LTX_FORCE_RUNTIME_QUANT: "{{envs.LTX_FORCE_RUNTIME_QUANT \|\| '1'}}", |

MLX Video UI sets `LTX_USE_PREQUANT=0` and `LTX_FORCE_RUNTIME_QUANT=1` by default, preferring runtime quantization of the LTX model on Apple Silicon. No Python-level MLX quantization API call appears in the wrapper.

**Not found:** GPTQ / AutoGPTQ, AWQ / AutoAWQ, ExLlama, HQQ, ONNX Runtime quantization, TensorRT INT8/FP8, and vLLM quantization flags. FP8/NF4 in this collection arrives as pre-quantized checkpoint files rather than through those toolchains.

## Porting implications

- bitsandbytes is the most common quantization dependency (7 repos), including NF4 FLUX checkpoints in ComfyUI and Forge. Its kernels are CUDA-first; current multi-backend builds improve ROCm support but there is no MPS equivalent, so Apple ports must use unquantized or SDPA-based alternatives.
- torchao is installed from CUDA/nightly indexes in Echomimic2 and Ominicontrol; it is PyTorch-native and therefore more portable than bitsandbytes, but the pinned wheel URLs must be replaced on AMD/Apple.
- optimum-quanto in Flux WebUI is pure PyTorch and comparatively portable; its int8 FLUX checkpoints can run wherever the underlying ops exist, though speed varies.
- MLX Video UI's runtime quantization is Apple-only by design (MLX on Metal); an AMD or NVIDIA port needs a different quantization backend such as bitsandbytes or torchao.
- GGUF is format-portable but backend-dependent: prefer a llama.cpp build for the target GPU (CUDA / Vulkan / Metal) rather than the CUDA-only wheel used by Wan.
- Pre-quantized FP8/NF4 weights (ComfyUI, Forge, UNO, Yue) avoid a quantization library at port time, but FP8 needs hardware support that AMD consumer GPUs and Apple Silicon generally lack; NF4 loaders must still be available on the target.
