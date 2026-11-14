# Porting Fooocus to Apple Silicon (MPS)

This package ports Fooocus (https://github.com/lllyasviel/Fooocus) to macOS
(Apple Silicon) with GPU (MPS) support, int4 (NF4) quantization by default,
a resource meter in the web UI, and one-click shared-mode launch.

**Status:** ported to Fooocus on Apple Silicon. MPS generation runs, but this
write-up has no benchmark numbers.

**Scope:** 298 changed lines — +174/−1 across 3 tracked files, plus the 123-line
`quantization.py`. **Difficulty:** low–medium — MPS already exists upstream; the
additions are quantization, flags, and the resource meter.

**Architecture map:** [`architecture.html#port=apple`](../architecture/architecture.html#port=apple) highlights where this port hooks into the upstream flow.

## Contents

- `changes.diff` — unified diff of tracked file changes (args_parser, model_management, webui).
- `quantization.py` — block-wise NF4 int4 quantization module (new file; copied to `modules/quantization.py`).
- `setup_and_run.sh` — self-contained clone + patch + run script.

## Porting details

### Device support
- Auto-detects Apple MPS (Metal) via `torch.backends.mps.is_available()`.
- Sets `PYTORCH_ENABLE_MPS_FALLBACK=1` and `PYTORCH_MPS_HIGH_WATERMARK_RATIO=0.0`.
- VRAM state becomes SHARED (unified memory).

### New accelerator flags
- `--torch-npu` — Huawei Ascend NPU via torch_npu (new CPUState.NPU).
- `--enable-tf32`, `--cudnn-benchmark` — NVIDIA-only tuning.
- `--torch-compile` — torch.compile the UNet (experimental).
- `--quantize-int4` / `--no-quantize-int4` — NF4 int4 quantization (default ON).

### Int4 (NF4) quantization
- Block-wise Normal Float 4 (QLoRA-style), 64-element blocks, per-block fp16 scale.
- ~3.8x weight memory reduction, ~20% weight-quantization error.
- Implemented in `modules/quantization.py` (`NF4Linear`, `quantize_model_int4`).
- Applied to the UNet (and refiner) Linear layers in `ModelPatcher.load()`.
- Memory-only: dequantizes to the input dtype on forward (no int4 GEMM kernel in torch 2.1).

### Resource meter
- Added to `webui.py`: a `gr.HTML` component updated every second via
  `Blocks.load(..., every=1)`.
- Shows accelerator (MPS/CUDA/NPU/XPU/CPU), RAM used/total, and VRAM/NPU/XPU when applicable.

### Dependency compatibility (Mac)
Gradio 3.41.2 needs older versions than pip's resolver picks:
- fastapi==0.104.1, starlette==0.27.0, jinja2==3.1.2, pydantic==1.10.13.

### Known limitations
- Apple MPS std_mean op missing -> handled by MPS_FALLBACK (slower).
- Memory pressure on 16GB Macs: SDXL footprint ~26GB; int4 helps but swap may still be needed.
- The bundled package's stated minimum is 4GB VRAM + 8GB RAM + ~40GB swap;
  Apple Silicon has no separate VRAM, so treat that as "unified memory plus swap".
- The `--torch-npu`, `--torch-compile`, `--enable-tf32`, `--cudnn-benchmark`,
  and `--quantize-int4` flags are experimental and not benchmarked in this
  write-up.

## Usage

```
cd fooocus/Apple_Silicon
bash setup_and_run.sh
```

Or manually:
```
git clone https://github.com/lllyasviel/Fooocus.git
cd Fooocus
git apply ../changes.diff
cp ../quantization.py modules/quantization.py
# install deps (see setup_and_run.sh)
TOKENIZERS_PARALLELISM=false python launch.py --listen --share --disable-in-browser
```

Int4 is on by default; disable with `--no-quantize-int4`.

## Access
- Local: http://localhost:7865/
- Public share URL printed on startup (expires in 72h).

## Acceleration options (GPU / NPU)

This document analyses the Fooocus codebase (SDXL-based image generation) and
enumerates concrete options to accelerate inference on **GPUs** and **NPUs**,
ordered from "already supported / low effort" to "research-grade".

Fooocus already has a device/precision/attention stack built on top of
`ldm_patched`. See `ldm_patched/modules/model_management.py`,
`modules/patch_precision.py`, `modules/core.py` and `launch.py`.

---

### 1. What Fooocus already does

#### GPU (NVIDIA CUDA)
- Device selection via `get_torch_device()` → `torch.cuda.current_device()` when
  `cpu_state == CPUState.GPU` and not XPU/MPS/DirectML.
- `is_nvidia()` gates NVIDIA-specific paths.
- **Scaled Dot Product Attention** is auto-enabled on torch ≥ 2.0 when no
  explicit `--attention-*` flag is set:
  `torch.backends.cuda.enable_math_sdp/flash_sdp/mem_efficient_sdp(True)`.
- **xformers** optional (`--disable-xformers`), version-checked.
- **Attention upcast** control (`--disable-attention-upcast`).
- **Precision flags**: `--all-in-fp32/fp16`, `--unet-in-{bf16,fp16,fp8-e4m3fn,fp8-e5m2}`,
  `--vae-in-{fp16,fp32,bf16}`, `--clip-in-{fp8,fp16,fp32}`, `--vae-in-cpu`.
- **VAE dtype** auto-promoted to bf16 on Ampere+ (SM ≥ 8) when supported.
- **cuDNN / allocator**: `--async-cuda-allocation` / `--disable-async-cuda-allocation`,
  `--gpu-device-id`, `CUDA_VISIBLE_DEVICES`.
- **Memory management**: VRAM states (`--always-low-vram`, `--always-no-vram`,
  `--always-high-vram`, `--always-gpu`, `--always-normal-vram`), `--vae-in-cpu`,
  `--always-offload-from-vram`, tiled VAE encode/decode (`VAEEncodeTiled` /
  `VAEDecodeTiled`), low-VRAM module streaming in `ModelPatcher`.
- **FreeU, Hypertile, TOME SD** available as contrib toggles (throughput/quality).

#### Apple Silicon (MPS)
- `CPUState.MPS` when `torch.backends.mps.is_available()`.
- `PYTORCH_ENABLE_MPS_FALLBACK=1` set in `launch.py`.
- VRAM state becomes `SHARED` (unified memory).

#### Intel
- **XPU (Arc / iGPU / dGPU)** via `intel_extension_for_pytorch` (IPEX):
  `torch.xpu.is_available()`, `is_intel_xpu()`, `get_torch_device() → xpu`.
  `torch.xpu.optimize(..., auto_kernel_selection=True, graph_mode=True)` applied
  to the UNet in `ModelPatcher.load()` (unless `--disable-ipex-hijack`).
- **DirectML** via `torch_directml` (`--directml [DEVICE]`).
- **CPU threads** (`--always-cpu N`).

#### Gaps / limitations
- Upstream has no **torch.compile** / `torch._dynamo` usage; this branch adds an
  experimental `--torch-compile` flag.
- No **CUDA graphs** capture for the sampling loop.
- No **TensorRT** or **ONNX Runtime** execution providers upstream; the separate
  [Snapdragon port](../Qualcomm_Snapdragon/README.md) uses a process-split ONNX
  Runtime/QNN backend.
- Upstream has no **NPU** backend (no OpenVINO NPU, no QNN, no CoreML/ANE, no
  CANN, no XDNA/VitisAI, no RKNN). This branch adds an experimental `--torch-npu`
  path for Huawei Ascend; the Snapdragon port covers Qualcomm QNN.
- Upstream has no **quantization** (bitsandbytes / GGUF / AWQ) path; only manual
  fp8 casts. This branch adds block-wise NF4 for the UNet.
- No **FlashAttention-2/3** explicit (relies on SDPA).
- No **DeepSpeed** / **FasterTransformer**.

---

### 2. GPU acceleration options

#### 2.1 Already present — verify/enable
| Option | How | Where |
|---|---|---|
| SDPA (flash/mem-efficient/math) | default on torch≥2 | `model_management.py` |
| xformers | install + remove `--disable-xformers` | `model_management.py` |
| bf16 UNet/VAE/CLIP | `--unet-in-bf16 --vae-in-bf16 --clip-in-fp16` | args |
| fp8 weights | `--unet-in-fp8-e4m3fn`, `--clip-in-fp8-*` | args |
| VAE on CPU | `--vae-in-cpu` | args |
| Low/no VRAM streaming | `--always-low-vram` / `--always-no-vram` | args |
| Intel XPU graph mode | default (disable with `--disable-ipex-hijack`) | `ModelPatcher` |
| Async CUDA alloc | `--async-cuda-allocation` | args |

#### 2.2 High-impact, low/medium effort (recommended next)
1. **`torch.compile` the UNet and VAE.**
   - Wrap `real_model` / diffusion model with `torch.compile(mode="reduce-overhead")`
     or `mode="max-autotune"`. Expected 1.2–2× on Ampere/Ada.
   - Touchpoint: `ModelPatcher.load()` after `patch_model()`, gated by a new
     `--torch-compile` flag and a warmup step.
   - Caveat: dynamic shapes in SDXL (variable batch/latent size) → use
     `dynamic=True` or bucket sizes; first run compiles.
2. **CUDA graphs for the sampler hot loop.**
   - Capture the per-step UNet forward in `modules/sample_hijack.sample_hacked`
     / `ldm_patched/modules/samplers.py`. Big win for small batch, fixed shapes.
   - Requires static shapes and disabling some sync points.
3. **TF32 + cuDNN benchmark.**
   - `torch.backends.cuda.matmul.allow_tf32 = True`,
     `torch.backends.cudnn.allow_tf32 = True`,
     `torch.backends.cudnn.benchmark = True`. Cheap, +5–15%.
4. **Memory-efficient attention already; add FlashAttention-2 explicitly.**
   - Install `flash-attn` and route attention to it when available; SDPA already
     picks flash on SM≥8, but explicit FA2 can help certain head dims.
5. **Fused kernels for activations/norms.**
   - `apex` or `torch.nn.functional` fused (e.g. `scaled_dot_product_attention`
     already fused). Mostly covered by torch.compile.
6. **Batching / micro-batching in the pipeline.**
   - `modules/default_pipeline.py` generates per-image in some paths; ensure
     `batch_size` is actually used for multi-image requests.
7. **Tiled VAE defaults for high-res** (already available; expose in UI).
8. **Model caching / keep-loaded.**
   - Avoid unload/reload between refiner switches; `--disable-offload-from-vram`
     already helps on Mac/low-VRAM.

#### 2.3 Medium effort
- **TensorRT for UNet/VAE/CLIP**: convert via `torch2trt` or `polygraphy`;
  huge win (2–4×) but engine build is slow and shape-specific. Best as an
  optional backend, not default.
- **ONNX Runtime (CUDA EP)**: export UNet to ONNX; ORT CUDA/TensorRT EP.
  Good portability; operator coverage for SDXL attention needs care.
- **DeepSpeed Inference** (`deepspeed-inference`): kernel injection for
  transformers; mainly for the CLIP text encoder / large LLM-style blocks.
- **bitsandbytes 8-bit/4-bit** for text encoders and UNet (memory + speed on
  memory-bound GPUs).
- **torchao** (PyTorch native quantization) for int8/int4 weights.

#### 2.4 Low priority / niche
- **cuBLASLt heuristic tuning**, **persistent kernels**, **CUDA 12.4+ graphs**.
- **Multi-GPU tensor/pipeline parallelism** (overkill for single-image SDXL).
- **MIG / MPS** for concurrent users.

---

#### 2.5 Int4 / NF4 quantization (new)

- **Block-wise NF4** (QLoRA-style): 4-bit normal-float levels with per-64-element
  block scales. ~3.8x weight memory reduction, ~20% weight-quantization error in tests.
- Implemented in `modules/quantization.py` (`NF4Linear`, `quantize_model_int4`),
  wired via `--quantize-int4` in `ModelPatcher.load()`.
- **Memory-only**: dequantizes to fp16 on forward; no speedup without int4 GEMM
  kernels. Real speedup needs CUTLASS/CK int4 kernels or vendor libraries.
- Alternative int4 paths worth exploring:
  - **GGUF (llama.cpp-style)**: mature CPU int4 kernels; could run the text
    encoder or a distilled UNet on CPU.
  - **AWQ/GPTQ**: activation-aware; better quality but needs calibration data.
  - **torchao Int4WeightOnly** (PyTorch native) in newer torch versions.
  - **bitsandbytes NF4** (not available on MPS/CPU in this env).

### 3. NPU acceleration options

NPUs (Neural Processing Units) are power-efficient accelerators found on
modern SoCs/CPUs: Intel Core Ultra NPU, Qualcomm Hexagon, Apple Neural Engine,
Huawei Ascend, AMD Ryzen AI (XDNA), Rockchip RKNN, MediaTek APU, etc.
Upstream Fooocus has **no NPU path**. This branch adds an experimental
`--torch-npu` device path for Huawei Ascend, and the separate
[Snapdragon port](../Qualcomm_Snapdragon/README.md) runs SDXL's UNet on the
Qualcomm Hexagon NPU through ONNX Runtime/QNN. A general NPU path still needs
(a) a device abstraction and (b) a model execution backend that can run SDXL's
UNet/VAE/CLIP.

#### 3.1 Intel NPU (Core Ultra / Meteor Lake+)
- **OpenVINO** with `NPU` device: export UNet/VAE/CLIP to OpenVINO IR and run
  via `openvino` runtime. OpenVINO already supports SD 1.5/SDXL in the
  OpenVINO notebooks; NPU support for SDXL is improving but operator coverage
  (attention, group norm) may require CPU fallback for some ops.
- Distinct from IPEX XPU (Arc GPU). Fooocus already does XPU; NPU needs a
  separate `--device npu` + OpenVINO backend.
- Precision: NPU prefers **int8/fp16**; use OpenVINO POT/NNCF quantization.
- Effort: high (new backend, model export, tiled execution).

#### 3.2 Qualcomm (Snapdragon X Elite/Plus, Hexagon NPU)
- **ONNX Runtime QNN EP** (`onnxruntime-qnn`) or **Qualcomm AI Stack (QNN SDK)**.
- Export models to ONNX, run with QNN EP targeting HTP (Hexagon Tensor Processor).
- Memory: unified; large SDXL UNet (~2.6B params) may exceed NPU memory →
  CPU/GPU fallback or smaller models.
- Effort: high; needs Windows-on-ARM or Linux ARM64.
- **Implemented separately:** the [Snapdragon port](../Qualcomm_Snapdragon/README.md)
  keeps the Fooocus UI on x64 and runs a native ARM64 QNN server for the UNet,
  with w8a16 quantization, 1024×1024 SDXL at ~2 s/step on a Surface Pro 11.

#### 3.3 Apple Neural Engine (ANE)
- **CoreML** (`coremltools`) conversion of UNet/VAE/CLIP; run via
  `coreml` backend or ONNX→CoreML.
- ANE has strict op/shape constraints (fixed shapes, specific layouts,
  fp16). SDXL UNet attention blocks may fall back to GPU/CPU.
- Fooocus already supports MPS (GPU) which is usually faster than ANE for SDXL
  today; ANE mainly benefits power/thermal on laptops.
- Effort: high; conversion + shape bucketing.

#### 3.4 Huawei Ascend (Atlas / Ascend NPU)
- **CANN** + **MindSpore** or **PyTorch (torch_npu)**.
- `torch_npu` provides a near-drop-in CUDA-like API (`npu` device) and
  Ascend-optimized kernels; could plug into Fooocus's existing
  `cpu_state`/`get_torch_device()` machinery similarly to XPU.
- This is the *lowest-friction* NPU option because it mimics CUDA.
- Effort: medium (add `CPUState.NPU` + `torch_npu` import + memory stats).

#### 3.5 AMD Ryzen AI (XDNA NPU)
- **VitisAI EP** for ONNX Runtime (`onnxruntime-vitisai`) or Ryzen AI SDK.
- Similar to Qualcomm path: ONNX export + VitisAI EP.
- Effort: high.

#### 3.6 Rockchip / other embedded NPUs
- **RKNN** toolkit: convert ONNX→RKNN; very constrained (small models, int8).
- SDXL too large; not practical for Fooocus's default models. Only relevant
  for distilled/tiny SD variants.

#### 3.7 Generic ONNX Runtime (CPU/GPU/NPU EPs)
- A single **ONNX Runtime backend** with selectable EP
  (`CPUExecutionProvider`, `CUDAExecutionProvider`, `OpenVINOExecutionProvider`,
  `QNNExecutionProvider`, `CoreMLExecutionProvider`, `VitisAIExecutionProvider`)
  gives the broadest NPU coverage with one code path.
- Requires exporting UNet/VAE/CLIP (and controlnets, upscalers) to ONNX and
  handling dynamic axes. Biggest investment but most reusable.

---

### 4. Cross-cutting concerns

- **Precision**: NPUs strongly prefer fp16/int8. Fooocus's manual fp8 paths
  (`--unet-in-fp8-*`) target CUDA; for NPU use int8 (POT/NNCF/QNN quant) or
  fp16. Keep fp32 fallback for unsupported ops.
- **Memory**: SDXL UNet ~6.5GB fp16 weights; NPUs often have 8–16GB shared.
  Need streaming/offload and possibly smaller/distilled models.
- **Operator coverage**: attention (softmax, matmul), group norm, SiLU, up/down
  sampling, RoPE/positional. Most NPUs handle these but may require specific
  layouts (NCHW vs NHWC) and fixed shapes.
- **Dynamic shapes**: samplers change latent H/W per request. NPU backends
  prefer static shapes → bucketing or padding to fixed sizes.
- **VAE tiling** already in code; essential for NPU memory.
- **Text encoder**: CLIP is small; easy to move to NPU/CPU; keep on CPU to
  save NPU memory for UNet.
- **ControlNet / IP-Adapter / upscalers**: each needs its own conversion; defer.

---

### 5. Recommended roadmap

#### Phase 0 — Quick wins (GPU) [days]
- Add `--torch-compile` flag; compile UNet+VAE in `ModelPatcher.load()`.
  **Implemented** (UNet only, `--torch-compile`, experimental).
- Enable TF32 + cuDNN benchmark by default on NVIDIA.
  **Implemented as flags** (`--enable-tf32`, `--cudnn-benchmark`), not default.
- Expose tiled VAE in UI; default on for ≥1024px.
- Add warmup step to avoid first-image latency.

#### Phase 1 — Device abstraction [1–2 weeks]
- Introduce `CPUState.NPU` and `get_torch_device()` branch for `torch_npu`
  (Ascend) — lowest-friction NPU, mimics CUDA. **Implemented** behind
  `--torch-npu` (experimental, not benchmarked).
- Add `--npu` / `--device {cuda,cpu,mps,xpu,directml,npu}` selector.
  **Partially implemented:** `--torch-npu` selects the device; there is no
  unified `--device` selector yet.
- Route memory stats/free-memory through `torch_npu` APIs. **Implemented** for
  the basic paths.
- Gate IPEX-style `optimize()` behind device capability.

#### Phase 2 — ONNX Runtime backend [3–6 weeks]
- Export UNet/VAE/CLIP to ONNX with dynamic axes + shape bucketing.
- Implement an ORT-backed model wrapper selectable via `--backend onnxrt`.
- Support EP selection: CUDA, OpenVINO (NPU), QNN, CoreML, VitisAI.
- Keep PyTorch backend as default; ORT opt-in.

#### Phase 3 — OpenVINO NPU [2–4 weeks, depends on Phase 2]
- Add OpenVINO NPU device path; quantize with NNCF int8.
- Validate SDXL operator coverage; fallback unsupported ops to CPU.

#### Phase 4 — Vendor NPUs [ongoing]
- Qualcomm QNN (Windows-on-ARM), Apple ANE (CoreML), AMD VitisAI.
- Each behind its own EP/flag; gated by availability.

#### Phase 5 — Quantization & polish
- bitsandbytes/torchao int8/int4 for text encoders + UNet.
- CUDA graphs for sampler.
- TensorRT optional backend.

---

### 6. Concrete code touchpoints in this repo

- `ldm_patched/modules/model_management.py`
  - `CPUState` enum, `get_torch_device()`, `is_intel_xpu()`,
    `get_free_memory()`, `get_total_memory()`, `ModelPatcher.load()`
    (ipex optimize spot), `VAE_DTYPE` logic.
- `ldm_patched/modules/args_parser.py` + `args_manager.py`
  - Add flags: `--torch-compile`, `--device`, `--backend`, `--npu`,
    `--enable-tf32`, `--cudnn-benchmark`.
- `modules/core.py` — model load + sampling entry; place compile here.
- `modules/default_pipeline.py` — batching, tiled VAE calls.
- `modules/sample_hijack.py` — sampler hot loop; CUDA graphs candidate.
- `launch.py` — env vars (`PYTORCH_ENABLE_MPS_FALLBACK`, etc.), install
  optional deps (onnxruntime, openvino, torch_npu) conditionally.
- `modules/patch_precision.py` — extend with NPU-friendly precision defaults.

---

### 7. Effort/impact summary

| Approach | Effort | Impact | Risk |
|---|---|---|---|
| torch.compile (GPU) | Low | High | Medium (compile time, dynamic shapes) |
| TF32 + cuDNN benchmark | Trivial | Low-Med | Low |
| Tiled VAE default | Trivial | Medium (memory) | Low |
| CUDA graphs (sampler) | Medium | High | Medium |
| bitsandbytes/torchao | Medium | Medium | Medium |
| TensorRT backend | High | Very High | High |
| ONNX Runtime (generic) | High | High | Medium |
| torch_npu (Ascend) | Medium | High (on Ascend) | Medium |
| OpenVINO NPU | High | Medium-High | High |
| QNN / CoreML / VitisAI | Very High | Medium | High |

---

### 8. Notes on this environment

The original code analysis was done on an Intel Mac, where Fooocus was cloned
into `/Users/<you>/opencode/Fooocus`. No torch / ipex / directml was installed
in that host Python (3.9), so the analysis commands were not executed there;
Fooocus requires Python ≥ 3.10. To experiment, create a venv with Python 3.10+
and install per `requirements_versions.txt` (CUDA 12.1 build by default) or use
the Docker image (`docker compose up`).

The port was later run on Apple Silicon; this write-up records no benchmark
numbers.

Recommended first experiment on an NVIDIA machine:
```
python launch.py --listen --torch-compile --enable-tf32 \
  --unet-in-bf16 --vae-in-bf16 --clip-in-fp16 --always-gpu
```
Implemented in this branch (behind flags, guarded by availability; experimental
and not benchmarked):
- `--torch-npu` (Huawei Ascend via torch_npu): new `CPUState.NPU`, device/memory/empty_cache
  handling in `model_management.py`.
- `--enable-tf32`, `--cudnn-benchmark` (NVIDIA only).
- `--torch-compile` (wraps the UNet in `ModelPatcher.load()`).
- `--quantize-int4`: block-wise NF4 (QLoRA-style) quantization of UNet Linear
  weights (~3.8x memory reduction, ~20% weight-quantization error). Implemented in
  `modules/quantization.py` (`NF4Linear`, `quantize_model_int4`). Memory-only:
  dequantizes to fp16 on the fly (no int4 GEMM kernel in torch 2.1).

Other items remain proposed.
