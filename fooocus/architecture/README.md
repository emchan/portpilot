# Fooocus architecture and port overlays

How Fooocus turns a Gradio request into an image, where the accelerator seams are,
and what each of the five ports changed.

- **Interactive map:** [`architecture.html`](architecture.html) — zoom, pan, click a
  node for the upstream code path, or pick a port to highlight its changes.
- **Model details:** [`model_details.html`](model_details.html) — operators,
  weight/activation shapes and dtypes, and where each port changed the model.
- **Source of truth:** upstream [Fooocus 2.5.5](https://github.com/lllyasviel/Fooocus/tree/v2.5.5).
  The ports were tested against `v2.5.5` except Intel AMX, which used `main` at
  snapshot time. Line numbers below refer to `v2.5.5`.
- **Port write-ups:** [Intel AMX](../Intel_AMX/README.md) ·
  [AMD iGPU](../AMD_iGPU/README.md) · [Google TPU](../Google_TPU/README.md) ·
  [Apple Silicon](../Apple_Silicon/README.md) ·
  [Snapdragon X](../Qualcomm_Snapdragon/README.md)

## How to read the map

| Element | Meaning |
| --- | --- |
| Solid grey box | Upstream Fooocus module or function |
| Solid line | Upstream call path |
| Port-coloured ring, badge, and line | Code path touched by the selected port |
| Coloured dots on a node | Ports that changed it; click for details |
| Right panel | Port summary, change list, and links to the write-up |

Open the file directly in a browser. No server or build step is needed. To deep-link
a view, use `architecture.html#port=tpu` or
`architecture.html#port=snapdragon&node=npu_server`. Clicking a change in the
right panel selects and centres the matching node.

## 1. Process shape

Fooocus is three layers in one process: a Gradio UI, a single queue worker that
owns the pipeline, and a patched copy of ComfyUI's model/sampling code under
`ldm_patched/`.

```
launch.py
  prepare_environment()                         launch.py:29
    check/install deps, download models/presets
  import webui
        |
        v
webui.py
  gr.Blocks(...).queue()                        webui.py:153
  generate_clicked(args)                        webui.py:33
    -> worker.AsyncTask(args)                   async_worker.py:10
        |
        v
async_worker.worker()                           async_worker.py:168
  task = queue.get()
  handler(task)                                 async_worker.py:1071
```

`modules/patch.py::patch_all()` runs once when `async_worker` is imported
(`patch.py:488`). It replaces the model loader, UNet forward, ControlNet forward,
CFG function, and weight loader with Fooocus-aware versions. This is the main
reason a port can be small: most accelerators only need a policy change or a
wrapper at this seam.

## 2. Request path

```
handler(task)                                   async_worker.py:1071
  process_prompt(...)                           async_worker.py:641
    pipeline.refresh_everything(...)            default_pipeline.py:234
      refresh_base_model()                      default_pipeline.py:62
      refresh_refiner_model()                   default_pipeline.py:82
      refresh_loras()                           default_pipeline.py:133
    pipeline.clip_encode(...)                   default_pipeline.py:182
  apply_control_nets / apply_inpaint /
  apply_vary / apply_upscale                    async_worker.py:396-628
  process_task(...)                             async_worker.py:280
    pipeline.process_diffusion(...)             default_pipeline.py:336
```

Task type decides the branch: text-to-image goes straight to `process_diffusion`;
inpaint, outpaint, upscale, and vary build a latent or image first, then reuse the
same sampler. `process_diffusion` also owns the refiner swap, initial latent, and
sigma calculation (`default_pipeline.py:307`).

## 3. Sampling loop

```
process_diffusion()                             default_pipeline.py:336
  core.generate_empty_latent()                  core.py:154
  core.ksampler()                               core.py:265
    prepare_noise()                             sample.py:9
    get_previewer()                             core.py:224
    samplers.sample = sample_hijacked           sample_hijack.py:89
    ldm_patched.modules.sample.sample()         sample.py:92
      samplers.KSampler                         samplers.py:652
        for sigma in sigmas:
          model.apply_model(x, sigma, cond)
            -> UNetModel.forward                openaimodel.py:816
               -> patched_unet_forward          patch.py:376
          sampling_function(...)                samplers.py:242
            -> patched_sampling_function        patch.py:226
          scheduler.step(...)
  core.decode_vae()                             core.py:160
  core.pytorch_to_numpy()                       core.py:330
```

Two details matter when porting:

- **CFG doubles the UNet work.** `sampling_function` runs the model on the
  positive and negative conditioning, so every per-step change is paid twice.
- **Attention is inside every transformer block.** `optimized_attention` is
  selected once at import (`attention.py:332`) and then called from the UNet's
  spatial transformer blocks, not from a single central kernel.

## 4. Model load, dtype, and attention

```
ModelPatcher.load()                             model_patcher.py
  model_management.load_models_gpu()            model_management.py:379
    get_torch_device()                          model_management.py
    get_total_memory() / get_free_memory()      model_management.py:652
    unet_inital_load_device()                   model_management.py:475
    should_use_fp16()                           model_management.py:704
    VRAMState / lowvram offload
  ModelPatcher.patch_model()                    model_patcher.py:177
    calculate_weight()                          patch.py:52 (patched)
```

Attention dispatch:

```
ldm_patched/ldm/modules/attention.py
  optimized_attention = attention_basic          attention.py:332
  if model_management.xformers_enabled():
      optimized_attention = attention_xformers   attention.py:285
  elif model_management.pytorch_attention_enabled():
      optimized_attention = attention_pytorch    attention.py:317  (SDPA)
  elif attention_split / attention_quad ...
```

This is the highest-leverage seam after dtype. A backend without xformers must
either use PyTorch SDPA or fall back to the pure-PyTorch split/quadratic paths,
which changes both memory and speed.

## 5. Where ports actually hook in

| Port | Entry | Device / dtype | Attention | Text encoder | Output |
| --- | --- | --- | --- | --- | --- |
| **Intel AMX** | `--always-cpu 8 --amx bf16` | bf16 autocast around UNet, VAE, CLIP | SDPA on CPU; optional IPEX prepack | Transformers 5 key remap | Same |
| **AMD iGPU** | `run-rocm.sh` | ROCm sees `cuda:0`; fp16 VAE | PyTorch SDPA + AOTriton `gfx110x` | Unchanged | Same |
| **Google TPU** | `torch_tpu` detection | bf16 UNet/VAE; fp32 CLIP embeddings | Forced PyTorch SDPA | `_LegacyCLIPTextModelLayout` | bf16 → float before NumPy |
| **Apple Silicon** | MPS + `--quantize-int4` | NF4 UNet, fp16 compute | PyTorch SDPA | Unchanged | Resource meter in UI |
| **Snapdragon X** | `FOOOCUS_NPU=1` | w8a16 UNet on HTP | Fixed in the QNN graph | CLIP-L/G ONNX graphs | NPU VAE → PNG base64 |

## 6. Port overlays

### 6.1 Intel AMX (CPU)

```
fooocus-amx.sh
  torch 2.8.0+cpu + IPEX 2.8.0
  webui.py --always-cpu 8 --amx bf16
        |
        v
patch_all()                                     patch.py:488
  amx.configure("bf16")                         modules/amx.py
  UNetModel.forward       -> autocast(bfloat16)
  VAEDecode.decode        -> autocast(bfloat16)
  SDClipModel.encode_token_weights -> autocast(bfloat16)
        |
        v
oneDNN selects AMX_BF16 kernels (avx10_1_512_amx)
```

- **No GPU and no IPEX requirement for the baseline.** bf16 autocast is enough
  for oneDNN to pick AMX kernels; IPEX `weights_prepack` was slower on
  `ModelPatcher` and stays opt-in.
- **Most of the port was dependency work**, not AMX: Python 3.13 forced
  Transformers 5 and numpy 2, which changed CLIP's parameter layout.
- **Files:** [`fooocus-amx.diff`](../Intel_AMX/fooocus-amx.diff) ·
  [write-up](../Intel_AMX/README.md)

### 6.2 AMD Radeon 780M (ROCm)

```
run-rocm.sh
  HSA_OVERRIDE_GFX_VERSION=11.0.0
  ROCPROFILER_REGISTER_ENABLED=0
  --attention-pytorch --vae-in-fp16
  --always-low-vram --disable-xformers
        |
        v
ROCm 7.2.4 -> HIP -> rocBLAS gfx1100 Tensile kernels
        |
        v
PyTorch sees "cuda:0" and Fooocus runs unmodified
```

- **No source patch.** The port is environment plus flags; the diff only adds
  scripts and pins.
- **`gfx1103` is not an official target.** The `gfx1100` override borrows
  kernels that exist in ROCm 7.2's rocBLAS.
- **WSL's 25.6 GB VRAM number is not a budget.** The VM has 7.7 GB of RAM, so
  low-VRAM offload is forced.
- **Files:** [`fooocus-rocm.diff`](../AMD_iGPU/fooocus-rocm.diff) ·
  [write-up](../AMD_iGPU/README.md)

### 6.3 Google TPU

```
launch.py
  is_tpu_backend() -> skip pinned requirements_versions.txt
  numpy 1.x aliases, Gradio queue timeout
        |
        v
model_management.py
  _detect_tpu() -> device "tpu", bf16, TPU OOM type
        |
        v
attention.py -> optimized_attention = attention_pytorch (SDPA)
        |
        v
patch_clip.py -> _LegacyCLIPTextModelLayout
  restore transformer.text_model.* keys
        |
        v
core.py -> cast bf16 previews to float before NumPy
```

- **Conditional backend, not a fork.** Every change is inert unless
  `torch.accelerator` reports `tpu`.
- **The worst bug was silent weight loss.** Transformers 5 flattened
  `CLIPTextModel`, `strict=False` loaded zero keys, and TPU's uninitialised
  memory is NaN, so every image was black.
- **bf16 everywhere for UNet/VAE**, but CLIP text embeddings stay fp32.
- **Files:** [`fooocus_tpu_patch.diff`](../Google_TPU/fooocus_tpu_patch.diff) ·
  [write-up](../Google_TPU/README.md)

### 6.4 Apple Silicon (MPS)

```
webui.py
  get_resource_meter() -> gr.HTML every 1 s
        |
        v
ModelPatcher.load()                             model_management.py
  quantize_model_int4() -> NF4Linear            modules/quantization.py
  optional torch.compile
        |
        v
MPS backend: unified memory, SDPA, fp16 compute
```

- **MPS already exists upstream.** The additions are int4 quantization, extra
  flags, and the resource meter.
- **NF4 is a capacity win, not a speed win.** Weights are dequantized every
  forward; no int4 GEMM kernel exists in this torch build.
- **SDXL still needs ~26 GB**, so a 16 GB Mac may swap even with int4.
- **Files:** [`changes.diff`](../Apple_Silicon/changes.diff) ·
  [`quantization.py`](../Apple_Silicon/quantization.py) ·
  [write-up](../Apple_Silicon/README.md)

### 6.5 Qualcomm Snapdragon X (Hexagon NPU)

This port reroutes the request instead of patching the UNet path:

```
launch.py -> FOOOCUS_NPU=1
        |
        v
handler(task)                                   async_worker.py:1071
  lazy torch pipeline proxy                     async_worker.py
  npu_bridge.supports_task()                    modules/npu_bridge.py
        |
        v  x64 process
npu/client.ensure_server()
  GET /health on 127.0.0.1:7867
  spawn qnn_env\Scripts\python.exe npu\server.py
  POST /generate
        |
        v  HTTP, PNG base64
npu/server.py                                   native ARM64 process
  CLIP-L + CLIP-G -> cond / uncond
  UNet w8a16, two forwards per step
  numpy schedulers
  VAE decode -> PNG
        |
        v  back in the x64 process
decode PNG -> composite inpaint -> Fooocus gallery
```

- **Two processes are required.** The x64-emulated UI cannot load the ARM64 QNN
  library, so the UI and the NPU runtime cannot share an address space.
- **Provider registration is the trap.** Passing
  `providers=["QNNExecutionProvider"]` silently falls back to CPU; the plugin EP
  must be registered explicitly.
- **The NPU wants fixed shapes.** SDXL is compiled for 1024×1024, steps are
  clamped to 8, and CFG to 2.5.
- **Files:** [`fooocus_snapdragon_win.diff`](../Qualcomm_Snapdragon/fooocus_snapdragon_win.diff) ·
  [write-up](../Qualcomm_Snapdragon/README.md)

## 7. Module map

| Path | Responsibility |
| --- | --- |
| `launch.py` | Environment check, model download, imports `webui` |
| `webui.py` | Gradio UI, `generate_clicked`, resource meter |
| `modules/async_worker.py` | Queue worker, task dispatch, image save |
| `modules/default_pipeline.py` | Model refresh, CLIP encode, sigmas, diffusion |
| `modules/core.py` | Latent helpers, `ksampler`, VAE decode, NumPy conversion |
| `modules/patch.py` | One-time monkeypatches for loading, UNet, CFG, ControlNet |
| `modules/sample_hijack.py` | Fooocus' sampler wrapper: masks, refiner, CFG |
| `modules/patch_clip.py` | CLIP compatibility (Transformers versions) |
| `ldm_patched/modules/model_management.py` | Device, dtype, VRAM, offload |
| `ldm_patched/modules/model_patcher.py` | Weight patches, LoRA, quantization hook |
| `ldm_patched/modules/samplers.py` | `KSampler`, CFG `sampling_function` |
| `ldm_patched/ldm/modules/attention.py` | Attention backend selection |
| `ldm_patched/ldm/modules/diffusionmodules/openaimodel.py` | UNet forward |
| `ldm_patched/modules/sd.py` | Checkpoint loading, CLIP key mapping |

## 8. Scope notes

- The map describes the **upstream architecture**, not every Fooocus feature.
  Enhance, describe, and face-restore paths are folded into `handler` branches.
- Port overlays show the code path that changed. Quantities and status come from
  each port's write-up; see the [top-level README](../../README.md) for the
  comparison table.
- The interactive page is self-contained: no CDN, no build step, no external
  JavaScript.
