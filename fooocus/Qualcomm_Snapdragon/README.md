# Porting Fooocus to Snapdragon X (Hexagon NPU)

Fooocus on a Snapdragon X PC, with the diffusion work offloaded to the Hexagon
NPU through ONNX Runtime's QNN plugin execution provider. The stock Fooocus web
UI is kept; only the model execution moves to a native ARM64 process.

- Base: Fooocus 2.5.5, commit `ae05379cc97bc4361ec8b4ec90193dab21be763f`
- Host: Surface Pro 11, Snapdragon X Plus X1P64100 (10 cores), 16 GiB LPDDR5x,
  Windows 11 26H2
- Accelerator: Hexagon NPU (45 TOPS INT8) via ONNX Runtime QNN
- Result: 1024×1024 SDXL in ~22 s for 8 steps, warm, through the normal Fooocus
  UI; SD 2.1 at 512×512 in ~2.9 s; SDXL inpaint in ~26 s

| Item | Value |
| --- | --- |
| Platform | Snapdragon X Elite / X Plus (ARM64), Windows 11 |
| Runtime | x64-emulated Fooocus UI + native ARM64 QNN server |
| Precision | UNet w8a16, CLIP/VAE fp16 |
| Status | Tested with Fooocus; text-to-image, inpaint, and assist models on NPU |

**Scope:** 8,846 changed lines across 45 files (+8,842/−4), including ~6.9k lines
of vendored `npu/sdxl` pipeline code. **Difficulty:** very high — ONNX/QNN
conversion, a two-process x64/ARM64 bridge, and fixed-shape constraints.

**Architecture map:** [`architecture.html#port=snap`](../architecture/architecture.html#port=snap) shows the rerouted request path and the x64/ARM64 boundary.

## Contents

- `run_snapdragon.bat` — bootstrap + launcher (double-click, or run in `cmd`)
- `fooocus_snapdragon_win.diff` — the porting patch (keep next to the `.bat`)
- `README.md` — this file: architecture, request flow, environment notes,
  dependency analysis, measured performance, troubleshooting

## Quick start

### Requirements

- Windows 11 on Snapdragon X Elite or X Plus
- [Git for Windows](https://git-scm.com/download/win)
- Python 3.10, 64-bit **x86** installer
  (<https://www.python.org/downloads/windows/>)
- Python 3.12, **ARM64** installer
  (<https://www.python.org/downloads/windows/>)
- ~20 GB free disk, internet access, no admin rights needed

The script looks for the usual python.org install locations first, then falls
back to the `py` launcher, and verifies the architecture. Override the paths
with `FOOOCUS_X64_PYTHON` and `FOOOCUS_ARM64_PYTHON`.

### What the launcher does

1. Clones <https://github.com/lllyasviel/Fooocus> at commit `ae05379`
   (v2.5.5 + 5).
2. Applies `fooocus_snapdragon_win.diff`.
3. Creates two environments:
   - `fooocus-snapdragon-npu-experiment\Fooocus\fooocus_env` — x64 Python 3.10
   - `fooocus-snapdragon-npu-experiment\qnn_env` — ARM64 Python 3.12
4. Downloads the precompiled SDXL w8a16 QNN assets (~4.4 GB) from HuggingFace.
5. Starts Fooocus with the NPU bridge (default when the assets exist) and a
   public Gradio share link (`--share` is on by default; `--no-share` disables
   it).

The NPU is selected automatically when `qnn_env` and `sd_xl_npu` are siblings of
`Fooocus`; set `FOOOCUS_NPU=0` to force the CPU pipeline. The torch SDXL
pipeline is imported lazily, so NPU text-to-image keeps the UI process near
1 GB instead of ~16 GB. The default preset is still downloaded on first launch;
it is only loaded if a task falls back to the CPU path (enhance, upscale). Pass
`--disable-preset-download` if you do not need those tasks and want to skip the
7 GB download.

The UI carries a live status bar above the gallery: accelerator (NPU or CPU),
model family (SDXL, SD 2.1, SD 1.5), quantization (w8a16 UNet / fp16 CLIP+VAE by
default), system RAM, and the UI/NPU-server commit. It refreshes every two
seconds and keeps updating during generation.

### First run

Expect roughly 10–30 minutes, dominated by pip and the two model downloads.
Later runs skip completed steps and go straight to the UI (about 30–40 s). The
first NPU request then pays roughly 60–90 s to load the five UNet contexts and
text encoders; later images take about 2 s/step on a Surface Pro 11 X1P64100.

The console prints a `https://….gradio.live` link when the UI is ready. Anyone
with that link can use the app while it runs; stop it with Ctrl+C to close the
tunnel.

### Layout after setup

```
<this folder>\
  run_snapdragon.bat
  fooocus_snapdragon_win.diff
  fooocus-snapdragon-npu-experiment\
    Fooocus\             git checkout + patch + fooocus_env
    qnn_env\             ARM64 ONNX Runtime + QNN 2.51
    sd_xl_npu\           text encoders, tokenizers, 5-part w8a16 UNet, VAE
    .fooocus-deps-ok     pip completion markers (delete to reinstall)
    .qnn-deps-ok
```

### Rerunning

Just run the `.bat` again. It skips the clone, patch, pip, and download steps
when they are already done. To force a clean state, delete the
`fooocus-snapdragon-npu-experiment` folder.

## Architecture

### What changed at a glance

The web UI is untouched. Prompting, presets, queueing, the gallery, and the
metadata log are stock Fooocus. The diffusion work is intercepted at one place
and sent to an NPU server process.

```python
modules/async_worker.py::handler()
    if npu_bridge.enabled() and npu_bridge.supports_task(task):
        npu_bridge.run_task(...)     # NPU path
        return                       # PyTorch pipeline never runs
```

That single early return is why the port keeps working when Fooocus changes:
everything upstream of `handler()` is still Fooocus, everything downstream is
optional for the NPU path.

### Why two processes

QNN ships ARM64 DLLs. The 2023-era Fooocus stack (gradio 3.41, pydantic 2.5,
torch 2.1) only has a usable Windows x64 build, so Fooocus runs under x64
emulation and cannot load the ARM64 QNN library. There is no x64 QNN EP and no
ARM64 torch wheel for this stack.

The split is therefore mandatory, not a design preference:

| Process | Architecture | Responsibility |
|---|---|---|
| Fooocus | x64 (emulated) | web UI, queue, prompt conditioning, scheduler, inpaint crop/composite, logging |
| NPU server | ARM64 native | text encoders, UNet, VAE, WD14, U2Net |

The two talk over loopback HTTP on `127.0.0.1:7867`. Because Snapdragon X is a
unified-memory SoC, the PNGs and JSON cross a socket, not PCIe; the transfer is a
few hundred kilobytes per image and is not on the critical path.

At startup `launch.py` enables the NPU automatically when `qnn_env` and
`sd_xl_npu` sit next to `Fooocus`; `FOOOCUS_NPU=0` forces the CPU pipeline. The
torch pipeline is imported through a lazy proxy in `modules/async_worker.py`, so
NPU generation never loads the 7 GB checkpoint: the UI process measured 16.2 GB
of private commit before the change and 1.0 GB after it. The import happens only
when a task falls through to the CPU path.

### Runtime topology

```
+---------------------------- x64 process ----------------------------+
|  Fooocus UI (gradio 3.41.2)                                         |
|                                                                     |
|  async_worker.handler() -> modules/npu_bridge.py -> npu/client.py   |
|  sampler / sigma schedule (numpy), prompt prep, inpaint compositing |
+----------------------------------+----------------------------------+
                                   |  HTTP 127.0.0.1:7867
                                   |  JSON requests, NDJSON progress,
                                   |  base64 PNG results
+----------------------------------v----------------------------------+
|  ARM64 process: npu/server.py                                       |
|  ThreadingHTTPServer, one global generation lock                    |
|                                                                     |
|  qnn_sdxl.py / qnn_sd21.py                                          |
|  onnxruntime + QNN plugin EP -> HTP backend (w8a16)                 |
+----------------------------------+----------------------------------+
                                   |
                            Hexagon NPU (45 TOPS INT8)
```

The server is started lazily by `client.ensure_server()` on the first NPU task.
It writes `npu/server_7867.log` and is not restarted per image; the five UNet
contexts stay resident.

### What runs where

| Stage | Runs on | Notes |
|---|---|---|
| Tokenizers | CPU (x64) | HuggingFace CLIP tokenizers, milliseconds |
| CLIP-L + CLIP-G | NPU | QNN graphs, cond + uncond, once per prompt |
| UNet | NPU | 5 w8a16 parts, 2 forwards per step (CFG) |
| Sigma schedule, CFG combine, latent math | CPU (x64, numpy) | vendored scheduler shim aliases numpy as torch |
| VAE decoder | NPU | 1024×1024 graph, ~1 s |
| VAE encoder | NPU | inpaint only |
| Inpaint crop/fill/composite | CPU (x64) | `InpaintWorker`, ESRGAN pre-upscale skipped |
| WD14 tagger | NPU or ARM64 CPU | `/tagger` |
| U2Net matting | NPU or ARM64 CPU | `/mask` |
| LoRA, refiner, ControlNet, IP-Adapter, upscale | not wired | stock CPU pipeline if requested |

### Repository changes

The diff touches 45 files (~8.8k added lines, 4 removed). Grouped by purpose:

| Path | Change |
|---|---|
| `modules/async_worker.py` | +19 lines: route tasks to the bridge before the torch pipeline; lazy pipeline proxy |
| `launch.py` | +14 lines: default to the NPU when `qnn_env` and `sd_xl_npu` exist |
| `modules/npu_bridge.py` | new: task gating, inpaint prep/composite, assist helpers |
| `npu/client.py` | new: x64 client, server auto-spawn, NDJSON streaming |
| `npu/server.py` | new: ARM64 HTTP server, backend detection, endpoints |
| `npu/qnn_sdxl.py` | new: SDXL pipeline wrapper, VAE encoder, masked-latent inpaint |
| `npu/qnn_sd21.py` | new: SD 2.1 (AI Hub assets) pipeline |
| `npu/sdxl/` | new: vendored SDXL QNN pipeline (MIT), numpy scheduler shim |
| `extras/wd14tagger.py` | +9 lines: try the NPU tagger first |
| `extras/inpaint_mask.py` | +14 lines: try the NPU matting endpoint first |
| `webui.py` | +12 lines: resource meter iframe at the top of the UI |
| `modules/resource_monitor.py` | new: stats collection plus `/resource-meter` and `/resource-metrics` routes |
| `args_manager.py` | share mode on by default; `--no-share` disables it |
| `npu/README.md`, `npu/ENVIRONMENT.md` | new: usage, assets, pins, gotchas (inside the patched `Fooocus/` checkout) |
| `.gitignore` | ignore `npu/*.log`, `npu/sdxl_out/`, `console.log` |

`npu/sdxl/` is a vendored community pipeline
([`Buuta/dreamshaper-xl-lightning-for-Snapdragon-X-Elite`](https://huggingface.co/Buuta/dreamshaper-xl-lightning-for-Snapdragon-X-Elite),
MIT). It is kept inside the repo because it is small Python glue, not model
weights.

## QNN integration

### The one runtime detail that matters most

Registering the QNN execution provider through the classic ORT provider list
does not fail loudly; it silently runs on the CPU:

```python
# silently falls back to CPU
ort.InferenceSession(path, providers=["QNNExecutionProvider"])
```

The working form is the plugin API, followed by device binding:

```python
import onnxruntime as ort
import onnxruntime_qnn as qnn

ort.register_execution_provider_library(qnn.EP_NAME, qnn.get_library_path())

opts = ort.SessionOptions()
opts.add_provider_for_devices(
    [d for d in ort.get_ep_devices()
     if d.ep_name == qnn.EP_NAME and d.device.type == ort.OrtHardwareDeviceType.NPU],
    {
        "backend_path": qnn.get_qnn_htp_path(),
        "enable_htp_fp16_precision": "1",
        "htp_performance_mode": "burst",
    },
)
opts.add_session_config_entry("session.disable_cpu_ep_fallback", "1")
```

`session.disable_cpu_ep_fallback = 1` is deliberate: with fallback enabled, an
unsupported op quietly moves the graph to the CPU and the benchmark becomes a
lie. See [Environment notes](#environment-notes) for the version archaeology
(QNN 2.51 / `onnxruntime-qnn` 2.7.0; 2.3.0 cannot load these contexts).

### SDXL: five graphs, two forwards per step

The precompiled SDXL UNet is split into five EPContext binaries because of QNN
context size limits. They are executed in order, once per forward:

| Part | Content | Outputs |
|---|---|---|
| `part0` | conditioning / time-embedding path | shared conditioning tensor |
| `part1` | down blocks | skip connections + main tensor |
| `part2` | mid block | bottleneck tensor |
| `part3` | first up block | up1 tensor |
| `part4` | remaining up blocks + head | noise prediction |

Skip connections are returned to the host and fed back into parts 3 and 4, so
the host sees several megabytes per boundary. Shapes are static (batch 1,
1024×1024), which is why other aspect ratios are not supported without
recompiling.

Each sampling step runs the full five-part chain twice, once for the negative
prompt and once for the positive prompt, then combines them with the CFG scale on
the host. A measured A/B at 8 steps: 19.6 s at `cfg=2.0` versus 10.9 s at
`cfg=1.0`, a ratio of 1.80×. The two forwards are submitted to a thread pool but
are effectively serialized by the HTP backend. Batched CFG is the largest
remaining optimisation.

### Inpainting

Fooocus's parameterized inpaint head injects features into internal UNet blocks;
that is impossible against a fixed compiled graph. The port uses Fooocus's
non-parameterized path instead:

1. `InpaintWorker` crops the region, fills it, and produces a 1024×1024 fill
   image plus a mask.
2. The QNN VAE encoder turns the fill into a latent.
3. The UNet runs with masked-latent blending: the fill latent is mixed into both
   the model input and the predicted noise at every step, so the known region
   stays pinned while the masked region denoises.
4. The QNN VAE decoder produces the image; `InpaintWorker.post_process()`
   composites it back into the original canvas.

Denoise strength is honored by slicing the sigma schedule, like
`KSampler.set_steps`. Large masked areas are lower quality than the CPU
parameterized path; this is the main known gap of the port.

### Assist models

| Endpoint | Model | Wired into |
|---|---|---|
| `POST /tagger` | WD14 `wd-v1-4-moat-tagger-v2.onnx` (311 MB) | `extras/wd14tagger.py` (Interrogate) |
| `POST /mask` | U2Net family (`u2net`, `u2netp`, `u2net_human_seg`, `silueta`) | `extras/inpaint_mask.py` |

Both are plain single-graph ONNX. The server tries QNN first and falls back to
native ARM64 CPU per model if the graph does not compile, which is still much
faster than the x64-emulated process.

## Request flow

Paths are relative to `fooocus-snapdragon-npu-experiment\`.

### Process start-up

```
run_snapdragon.bat
  -> fooocus_env\Scripts\python.exe launch.py --always-cpu --share
       -> FOOOCUS_NPU unset and qnn_env + sd_xl_npu present: set FOOOCUS_NPU=1
       -> gradio UI on 127.0.0.1:7865 and a public gradio.live link
          (share is on by default; --no-share disables it)
       -> async_worker uses a lazy pipeline proxy; the torch checkpoint is not
          loaded for NPU tasks (UI ~1 GB instead of ~16 GB)

first NPU task
  -> modules/npu_bridge.py: npu_client.ensure_server()
       -> probes GET /health on 127.0.0.1:7867
       -> if absent, spawns:
          qnn_env\Scripts\python.exe npu\server.py --model-dir ..\sd_xl_npu --port 7867
       -> polls /health until ready (180 s budget); log at npu\server_7867.log

server start
  -> detects backend from the model dir
       metadata.json + text_encoder/model.onnx  -> sd21
       unet_w8a16_quantized/ or unet/           -> sdxl
  -> does not load graphs yet; the first request does
```

The first request pays the context load (five UNet parts plus text encoders and
VAE). Expect roughly 60–90 s before the first denoise step; later images are
warm.

### Text to image (NPU path)

```
Fooocus UI / queue
      |
      v
modules/async_worker.py :: handler(task)
      |  FOOOCUS_NPU=1 and npu_bridge.supports_task(task)
      v
modules/npu_bridge.py :: run_task()
      |  read steps, cfg, seed, prompt, negative, aspect ratio
      |  SDXL clamps: steps > 8 -> 8, cfg > 2.5 -> 2.0, size -> 1024x1024
      |            (the only compiled shape today)
      |  progressbar("Preparing NPU backend")
      v
npu/client.py :: ensure_server()          (spawn once, keep resident)
      |
      v
POST http://127.0.0.1:7867/generate
     {"prompt", "negative", "steps", "cfg", "seed", "count",
      "disable_seed_increment", "width", "height"}
      |
      v
npu/server.py                                   ARM64 process
      |  with generation_lock:
      |    qnn_sdxl.py / qnn_sd21.py
      |      text encoders (CLIP-L + CLIP-G) -> cond and uncond embeddings
      |      latents = randn * sigma_max
      |      for each step:
      |          UNet(cond)   -> parts 0..4
      |          UNet(uncond) -> parts 0..4
      |          noise = uncond + cfg * (cond - uncond)
      |          scheduler step (Euler ancestral, host numpy)
      |      VAE decode -> RGB
      |      encode PNG -> base64
      v
NDJSON stream back to client.py
      {"type":"progress","index":0,"step":1,"total":8,"elapsed":1.9}
      ...
      {"type":"image","index":0,"seed":42,"png":"<base64>"}
      {"type":"done"}
      |
      v
npu_bridge.py
      |  decode PNG -> numpy RGB
      |  yield_result(task, image, "SDXL Lightning on Hexagon NPU", ...)
      v
Fooocus gallery + outputs\<date>\log.html
```

Notes:

- The sampler and sigma schedule stay in the x64 process. Only tensors for the
  text encoders, UNet and VAE cross the socket.
- `count` images are generated in one request, each with its own seed and
  progress `index`.
- The server serializes generations with a lock; parallel queue workers wait.
- The final image is a base64 PNG, which Fooocus treats like any other result.

### Wire protocol

| Endpoint | Request | Response |
|---|---|---|
| `GET /health` | — | `{"ready": true, "backend": "sdxl", "sizes": [[1024,1024]]}` |
| `POST /generate` | JSON fields above | NDJSON, one object per line |
| `POST /inpaint` | `fill_png`, `mask_png`, `prompt`, `negative`, `steps`, `cfg`, `seed`, `strength` | JSON `{"png": "<base64>"}` |
| `POST /tagger` | `png`, `model_onnx`, `model_csv`, thresholds | JSON `{"tags": "..."}` |
| `POST /mask` | `png`, `model_path` | JSON `{"png": "<base64>"}` |

`/generate` event types:

| Type | Fields | Meaning |
|---|---|---|
| `progress` | `index`, `step`, `total`, `elapsed` | one line per denoise step |
| `image` | `index`, `seed`, `png` | finished image, base64 |
| `error` | `message` | generation failed; client raises |
| `start` | `count`, `steps`, `backend` | generation accepted |
| `done` | `elapsed` | stream complete |

### Inpainting flow

```
Fooocus Inpaint tab or outpaint
      |
      v
async_worker.handler()
      |  npu_bridge.supports_inpaint(task, goals)
      v
npu_bridge.run_inpaint_task()
      |  InpaintWorker: crop / fill / mask, ESRGAN pre-upscale skipped
      |  (that pre-upscale alone takes minutes on the CPU path)
      v
POST /inpaint  {fill_png, mask_png, prompt, steps, cfg, seed, strength}
      |
      v
npu/server.py
      |  VAE encoder (QNN)  -> 4-channel latent of the fill
      |  mask downsampled to 128x128 latent space
      |  for each step:
      |      x = latents * mask + (fill_latent + noise) * (1 - mask)
      |      UNet cond/uncond + CFG
      |      blend fill_latent into the known region of the prediction
      |      Euler ancestral update, sigma slice for strength
      |  VAE decoder (QNN)
      v
{"png": "<base64>"}
      |
      v
InpaintWorker.post_process() -> composite into the original canvas
      -> Fooocus logger -> gallery
```

Measured warm inpaint: 4.3 s prep + 21.9 s server + 0.2 s composite = 26.4 s.
The Fooocus inpaint head is not used; this is masked-latent blending, which is
the quality trade-off of the port.

### Assist model flow

```
Interrogate button
  -> extras/wd14tagger.py
       if FOOOCUS_NPU: modules/npu_bridge.tagger_via_npu(...)
            -> POST /tagger -> WD14 on QNN (0.92 s) or ARM64 CPU
       on exception: stock local onnxruntime path

Inpaint mask / subject selection
  -> extras/inpaint_mask.py
       if FOOOCUS_NPU: modules/npu_bridge.mask_via_npu(...)
            -> POST /mask -> U2Net on QNN (~1 s) or ARM64 CPU
       on exception: stock rembg / ORT path
```

The server decides QNN vs ARM64 CPU per model: if the graph fails to compile, it
logs a warning and uses the native CPU session for that model. Either way it
avoids the x64-emulated process.

### Fallbacks and failure paths

| Situation | Behaviour |
|---|---|
| `FOOOCUS_NPU` unset | NPU is on when `qnn_env` and `sd_xl_npu` exist; otherwise stock CPU pipeline |
| `FOOOCUS_NPU=0` | stock CPU pipeline; the first task imports the torch pipeline and loads the preset |
| `qnn_env` or `sd_xl_npu` missing | NPU stays off; stock CPU pipeline |
| Server cannot start | task fails with "NPU backend unavailable"; UI keeps running |
| Unsupported task (enhance, upscale, LoRA, ControlNet) | falls through to the CPU pipeline with a log line, never a wrong NPU image |
| SDXL size not compiled | clamped to 1024×1024 |
| SDXL steps > 8 or CFG > 2.5 | clamped to 8 and 2.0 for Lightning |
| QNN rejects an assist graph | that model runs on ARM64 CPU |
| QNN op unsupported in the UNet | would fall back to CPU only if `session.disable_cpu_ep_fallback` were off; it is on, so this fails loudly instead of silently |
| QNN library registered twice | `qnn_ep.py` wraps registration in try/except so SDXL and SD 2.1 can coexist |

### Timing model

```
warm image = CLIP (~0.5-1 s) + steps * (2 forwards + scheduler)
             + VAE decode (~1 s) + PNG/HTTP (~0.2 s)

SDXL: 8 steps * 2.0 s/it ~= 16 s UNet + ~6 s everything else  ~= 22 s
SD 2.1: 8 steps * 0.36 s/it ~= 2.9 s total
```

`cfg=2.0` costs 1.80× the `cfg=1.0` run (19.6 s vs 10.9 s at 8 steps): the two
forwards are effectively serialized. Batching cond+uncond into one batch-2 graph
is the largest remaining win, followed by 6-step sampling.

### UI status bar

The bar above the gallery is a same-origin iframe (`/resource-meter`) that polls
`/resource-metrics` every two seconds. The routes are added to Gradio's FastAPI
app by `modules/resource_monitor.install_routes()`, which wraps
`gradio.networking.start_server()` before `launch()`.

Fields: `accel`/`dot` (NPU, NPU idle, CPU, CPU fallback), `family`/`detail`
(SDXL, SD 2.1, SD 1.5), `quant` (for example `w8a16 UNet / fp16 CLIP+VAE`),
`ram_used`/`ram_total`/`ram_pct`/`ram_color`, `ui_gb` (UI private commit),
`npu_gb` (server private commit, cached PID), and `updated`.

It deliberately does not use `load(..., every=2)`: Gradio 3.41 wraps that
callback in an infinite generator that holds a queue worker for the life of the
page, and Fooocus's queue has a concurrency count of one. The iframe keeps the
meter independent of generation. A snapshot costs ~5 ms once warm; the first
call pays ~1 s for the psutil process scan.

## Measured performance

All numbers through the bridge on the X1P64100, 16 GiB:

| Workload | Precision | Time |
|---|---|---|
| SD 2.1, 512×512, 8 steps | w8a16 | 2.9 s |
| SDXL, 1024×1024, 8 steps | UNet w8a16, CLIP/VAE fp16 | ~22 s warm, ~2.0 s/step |
| SDXL, 1024×1024, 6 steps | same | ~24 s cold |
| SDXL inpaint, 1024×1024, 8 steps | same | 26.4 s warm (prep 4.3 + server 21.9 + composite 0.2) |
| WD14 interrogate | fp32 graph on QNN | 0.92 s |
| U2Net mask | fp32 graph on QNN | ~1 s |

The UNet is 6.44 TFLOP per forward and 2.49 B parameters. At ~1 s per forward it
sustains ~6.5 TOPS effective, about 14% of the 45 TOPS INT8 peak, while moving
~2.3 GB/s of a 135 GB/s memory system. It is latency- and dispatch-limited at
batch 1, not bandwidth-limited.

The NPU server's model set is ~4.36 GB. The Fooocus UI process stays near 1.0 GB
because the torch pipeline is lazy-loaded and never touches the checkpoint during
NPU generation; before that change it committed 16.2 GB.

## Dependency analysis

Scope: Fooocus 2.5.5 (`ae05379`), Snapdragon X Plus X1P64100, 16 GB, Windows
26H2. Method: import scan over `modules/`, `ldm_patched/`, `extras/` (136 files
import torch), hot-path trace, then feasibility of each third-party library /
vendored model on ONNX Runtime QNN (HTP NPU and Adreno GPU).

### What actually runs per image

```
async_worker.handler()
  -> process_prompt()                 modules/default_pipeline.py:147-199
       core.clip_encode()             CLIP-L + CLIP-G, cond + uncond, pooled  (once)
  -> process_diffusion()              modules/default_pipeline.py:336
       ldm_patched.modules.samplers.sample()        samplers.py:586
         per step: sampling_function()  (CFG, samplers.py:242)
                   model.apply_model()  -> UNetModel.forward()  openaimodel.py:816   (x2 for CFG)
         sampler loop + sigma schedule   k_diffusion/sampling.py
  -> VAE.decode()                     ldm_patched/modules/sd.py:230  (AutoencoderKL decoder)
  -> postprocess                      modules/core.py:256 (einops) + cv2/PIL
```

Optional branches: refiner UNet (second pass), ControlNet (per step), LoRA
(merged at load time), FreeU/ADM patches, inpaint/enhance (rembg + SAM +
GroundingDINO), face swap (facexlib), upscale models (`ldm_patched/pfn`), WD14
interrogate, BLIP, prompt expansion, NSFW censor (off by default,
`modules/config.py:641`).

Compute share is overwhelmingly the UNet: ~90% of wall time on CPU. VAE decode
is the next largest; CLIP encode is a one-off per prompt.

### Dependency inventory

| Library | Where used | Hot path | Notes |
|---|---|---|---|
| `torch` (2.1.0+cpu, x64) | 136 files | yes | no NPU/DirectML backend on win_arm64; native CPU wheel exists (2.9.1+cpu) |
| `ldm_patched` (vendored ComfyUI fork) | models, samplers, ControlNet, pfn upscalers, TAESD | yes | the real "library to port": UNet/CLIP/VAE/sampler implementation |
| `numpy` | 44 files | yes (light) | scheduler sigmas, latent math, pre/post |
| `transformers` | `sd1_clip.py` (only `CLIPTokenizer`), `extras/expansion.py:62`, `extras/censor.py:29`, BLIP | tokenizer yes, models no | CLIP math is Fooocus's own `torch.nn` (`SDClipModel`), so it is exportable; tokenizer must stay CPU |
| `einops` | 13 files, only 1 real use `modules/core.py:256` | no | `rearrange('b c h w -> b h w c')` — replace with `permute`, zero gain |
| `torchsde` | `k_diffusion/sampling.py:6,64` only | marginal | Brownian-tree noise for `*_sde` samplers (default is `dpmpp_2m_sde_gpu`); tiny CPU tensor math |
| `scipy` | `k_diffusion/sampling.py`, `contrib/external_mask.py` | no | CPU math |
| `cv2` | 10 files: resize, warp, mask composite | no | ARM64 OpenCV wheels are already NEON-optimized; no Vulkan/OpenCL ICD registered |
| `torchvision` | LaMa, facexlib, BLIP only | no | not on the SDXL path |
| `timm` | BLIP only (`extras/BLIP/*`) | no | interrogate feature only |
| `xformers` | `attention.py`, `model_management.py` | optional | no ARM64 wheel; startup falls back to `attention_sub_quad` (chunked attention) |
| `onnxruntime` | `extras/wd14tagger.py:47` only | no | already ONNX — easiest QNN port |
| `rembg` | `extras/inpaint_mask.py:8` | no | u2net/isnet are ONNX under the hood |
| `segment_anything` | `inpaint_mask.py:9`, `extras/sam` | no | torch, dynamic point prompts |
| `groundingdino` + `supervision` | `extras/GroundingDINO`, `inpaint_mask.py:6` | no | deformable attention, top-k — hard to export |
| `safetensors` | loaders | no | keep |
| `skimage` | `modules/gradio_hijack.py` | no | UI only |
| `gradio`, `gradio_client`, `httpx` | UI | no | CPU |
| `pytorch_lightning`, `accelerate`, `omegaconf`, `pygit2` | **not imported** in `modules`/`ldm_patched`/`extras` | no | dead weight in requirements; drop for a lean port |
| `psutil`, `packaging`, `tqdm`, `Pillow` | utility | no | keep |

### Portability matrix

Tier A = biggest payoff, Tier B = easy/feature-specific, Tier C = hard or low
value.

| # | Component | Source | Share of runtime | Best target | Feasibility | Effort | Expected gain |
|---|---|---|---|---|---|---|---|
| A1 | **SDXL UNet** (base, optionally refiner) | `ldm_patched/ldm/modules/diffusionmodules/openaimodel.py:365` | ~90% | **NPU (HTP, w8a16)** | ONNX export works (community SDXL-NPU repo proves it); fixed shapes required | High | 10–50× vs CPU; ~2 s/it w8a16 |
| A2 | **VAE decoder** | `ldm_patched/modules/sd.py:150`, `ldm/modules/diffusionmodules/model.py` | ~5–10% | NPU fp16, or QNN GPU fp16 | conv/resblock/attention, exportable; tile 64×64 latents | Medium | 5–10×; avoids CPU decode spike |
| A3 | **CLIP-L + CLIP-G text encoders** | `ldm_patched/modules/sd1_clip.py:61` (`SDClipModel`, `SDXLClipModel`) | ~2–5% (once/prompt) | NPU/GPU | pure torch modules, fixed 77 tokens, clip-skip can be baked in | Medium | 5–10× on encode; small absolute win |
| B1 | **WD14 tagger** | `extras/wd14tagger.py:47` | feature | NPU or native CPU | already `onnxruntime` — only needs the QNN plugin EP wired | Low | tagger becomes instant |
| B2 | **rembg masks** (u2net/isnet) | `extras/inpaint_mask.py:8` | feature | NPU | ONNX; rembg accepts a custom session | Low | 3–10× on mask prep |
| B3 | **Upscale models** (ESRGAN/RRDB, DAT, HAT, SCUNet, OmniSR) | `modules/upscaler.py:5-6`, `ldm_patched/pfn/architecture/*` | feature | NPU | conv / window-attention, ONNX-exportable; tile by crop | Medium | 3–10× on upscale |
| B4 | **TAESD preview decoder** | `ldm_patched/taesd` | feature | NPU/CPU | tiny conv net, trivial ONNX | Low | smoother previews |
| B5 | **Safety checker / censor** | `extras/censor.py:29` | feature (off) | NPU/CPU | CLIP ViT + linear, ONNX-able | Low | negligible (off by default) |
| B6 | **Face restore** (GFPGAN/CodeFormer via facexlib) | `extras/facexlib`, `face_crop.py` | feature | NPU | conv/transformer on 512² face crops → ONNX | Medium | 3–5× on face swap |
| B7 | **Prompt expansion GPT-2** | `extras/expansion.py:62` (335 MB ckpt) | once/prompt | CPU (or NPU) | ONNX generation with KV cache; 124 M params | Low–Med | low value; keep on CPU |
| C1 | **SAM** (mask decoder) | `segment_anything`, `inpaint_mask.py:83` | feature | encoder→NPU, decoder→CPU | encoder exportable at 1024²; decoder has dynamic point inputs | High | partial |
| C2 | **GroundingDINO** | `extras/GroundingDINO` | feature | CPU | deformable attention, top-k, dynamic shapes | High | not worth it |
| C3 | **ControlNet** (SDXL) | `ldm_patched/controlnet/cldm.py:22` | feature | NPU (second graph) | exportable but +2.5 B params, residuals joined host-side | High | only for CN workflows |
| C4 | **IP-Adapter** | `extras/ip_adapter.py` + CLIP-ViT-H | feature | NPU (extra UNet input) | image encoder exportable; UNet needs extra cross-attn embeddings baked in | High | only for IP-Adapter workflows |
| C5 | **BLIP interrogate** | `extras/BLIP`, `timm` | feature | CPU | keep | — | — |

### Why these targets

- **NPU (HTP)**: validated on this machine — QNN EP via the plugin API
  (`register_execution_provider_library` + `add_provider_for_devices`), w8a16,
  fp16 activations. Measured 1.66 ms vs 10.63 ms CPU (6.4×) on an SDXL-sized
  conv block. Full SD 2.1 512² pipeline already runs at 0.36 s/step (2.89 s for
  8 steps).
- **Adreno GPU (QNN GPU backend)**: also works (3.68 ms, 2.9× CPU) but slower
  than HTP. Its value is fallback: fp32 ops, layers HTP rejects, or running VAE
  in parallel with the UNet on the NPU (separate sessions, different EP devices).
- **DirectML / Vulkan / OpenCL**: not viable — no win_arm64 DirectML wheels, no
  Vulkan ICD / OpenCL vendor entry registered on the Adreno driver. QNN is the
  only GPU path.
- **Native ARM64 PyTorch (CPU)**: real wheels exist (2.9.1+cpu cp311/312/313) but
  only on `download.pytorch.org/whl/cpu`; ~1.5–2.5× over the current x64-emulated
  venv. Useful for everything that stays on CPU (tokenizer, cv2, scheduler,
  optional models).

### Hard constraints for the port

1. **Static shapes.** QNN compiles per shape. SDXL needs buckets such as 1024²,
   832×1216, 1216×832, 896×1152, 1152×896, 768×1344, 1344×768 (UNet latent =
   H/8 × W/8). Shape changes at runtime force a recompile or a new context.
2. **CFG batching.** Feed cond+uncond as batch 2 in one UNet call to halve
   per-step overhead; otherwise two calls per step.
3. **Precision.** w8a16 for the UNet (per-channel int8 weights, fp16
   activations, `enable_htp_fp16_precision=1`); keep CLIP and VAE in fp16 (do not
   quantize them) to preserve detail.
4. **LoRA must be merged before export** (`modules/lora.py` applies deltas at
   load time); the compiled graph has fixed weights. Either pre-merge per
   checkpoint or compile per-LoRA (expensive).
5. **Attention must be baked in.** xformers is unavailable on ARM64; export the
   UNet with plain MatMul+Softmax (or fixed chunked sub-quadratic) attention — no
   runtime dispatch.
6. **VAE tiling** for 1024² (decode 64×64 latent tiles, 16 overlap) to bound NPU
   memory.
7. **Sampler stays host-side.** Euler/DPM++/SDE math and `torchsde`/`scipy`
   noise are tiny float ops on 128×128×4 tensors; porting them buys nothing and
   breaks sampler choice. Only the UNet (and optionally CLIP/VAE) go to the
   accelerator.
8. **QNN EP only supports one device per session**, so "NPU + GPU together"
   means two sessions (e.g. UNet on HTP, VAE on Adreno), not one mixed graph.
9. **Custom checkpoints** (Juggernaut etc.) need ONNX export + compile. Qualcomm
   AI Hub cloud compile or the local AI Engine Direct SDK
   (`qairt-converter`/quantizer). Precompiled public assets exist only for stock
   SD 1.5 / 2.1 (AI Hub) and SDXL (community repo, ~13 GB, fixed resolutions).

### What not to port

- **Gradio / gradio_client / httpx / skimage**: UI stack, CPU, already fine.
- **einops**: one call in `core.py`; replace with `permute` if dropping torch.
- **torchsde**: only SDE noise; keep CPU or swap the default sampler to a
  non-SDE one (`dpmpp_2m`) for deterministic NPU runs.
- **scipy**: sigma schedules and mask helpers, CPU.
- **cv2**: ARM64 NEON build; no GPU path exposed by the driver.
- **pytorch_lightning / accelerate / omegaconf / pygit2**: not imported at
  runtime.
- **xformers**: no ARM64 build; irrelevant once attention is inside the ONNX
  graph.

### Recommended sequence

1. **Done:** SD 2.1 NPU bridge (UI → `npu/server.py` → HTP, w8a16) — proves the
   split architecture: Fooocus keeps UI/config/logging; models run in an ARM64
   ONNX/QNN process; sampler stays host-side in numpy.
2. **Done:** generalized engine — `npu/qnn_sdxl.py` + backend auto-detection in
   `server.py`, model-agnostic protocol with `width`/`height` and per-step
   progress.
3. **Done:** SDXL on NPU — DreamShaper XL Lightning, w8a16, 5-part UNet,
   1024×1024, Euler-ancestral host scheduler, batchless CFG. Measured ~2.0 s/it,
   ~22 s warm for 8 steps; wired through `modules/npu_bridge.py`.
   **Inpaint is also ported:** QNN VAE encoder + masked-latent blending on the
   same UNet (no Fooocus inpaint head), ~20–30 s for 8 steps at 1024².
4. **Done (partial):** assist models on the ARM64 server — `/tagger` (WD14) and
   `/mask` (U2Net family) run on QNN and are wired into `extras/wd14tagger.py`
   and `extras/inpaint_mask.py`. Enhance and upscale now fall back to the CPU
   pipeline instead of being misrouted to txt2img; inpaint has its own NPU path.
   Upscalers/face restore still need ONNX exports of the `pfn`/facexlib weights
   before they can be added to the server.
5. **Later / optional:** ControlNet, IP-Adapter, SAM encoder. GroundingDINO stays
   CPU.

### Measured reference points

| Measurement | Result |
|---|---|
| QNN conv block, 320 ch @ 64×64 | CPU 10.63 ms, NPU 1.66 ms (6.4×), GPU 3.68 ms (2.9×) |
| SD 2.1 512², 8 steps, w8a16 | 2.89 s total, 0.36 s/step, 3.3 s model load |
| SD 2.1 512², 30 steps via Fooocus UI | 2 images generated in seconds, metadata logged |
| Community SDXL NPU (X Elite, w8a16) | ~2.0 s/it quantized, ~3.9 s/it fp16, peak RAM ~2.8 / 5.2 GB |

## Environment notes

These are steps that live outside the repo files (Python packages), recorded so
the setup can be reproduced.

### ARM64 NPU runtime (`qnn_env`)

- Python 3.12 ARM64 (native), not the x64-emulated Fooocus venv.
- `onnxruntime` 1.31.1 + `onnxruntime-qnn` **2.7.0** (bundles QNN 2.51).
  `onnxruntime-qnn` 2.3.0 bundles QNN 2.47 and fails to load these EPContext
  graphs (`QNN_CONTEXT_ERROR_INVALID_ARGUMENT`).
- `transformers==4.56.2`, `onnx`, `pillow`, `numpy`.
- QNN EP must be registered via the plugin API:
  `ort.register_execution_provider_library(qnn.EP_NAME, qnn.get_library_path())`
  followed by `SessionOptions.add_provider_for_devices(...)`. Passing
  `providers=["QNNExecutionProvider"]` silently falls back to CPU.
- Both backends share the process: registration is wrapped so a second backend
  loading in the same process does not fail with "EP library is already
  registered".
- SDXL pieces come from
  [`Buuta/dreamshaper-xl-lightning-for-Snapdragon-X-Elite`](https://huggingface.co/Buuta/dreamshaper-xl-lightning-for-Snapdragon-X-Elite)
  on HuggingFace (MIT). Required paths: `text_encoder`, `text_encoder_2`,
  `tokenizer`, `tokenizer_2`, `unet_w8a16_quantized`, `vae_decoder/1024x1024`,
  and `vae_encoder/1024x1024` for inpainting.
- The vendored SDXL scheduler shim aliases numpy as `torch` and calls
  `cumprod(..., dim=0)`. Its monkeypatch was made signature-compatible so
  `numpy.cumprod` keeps working for the SD 2.1 pipeline in the same process.
- Assist models (WD14 311 MB, U2Net 168 MB) are plain ONNX; the server opens them
  on QNN and falls back to native ARM64 CPU per model if the graph does not
  compile.

### Fooocus venv (`fooocus_env`) web-stack pins

Fooocus 2.5.5 pins `gradio==3.41.2`, so fastapi/starlette/pydantic must be from
that era. With modern packages the UI fails at startup:

| Symptom | Cause | Fix |
|---|---|---|
| `TypeError: unhashable type: 'dict'` in jinja2 | starlette >= 0.29 changed `TemplateResponse(name, context)` to `TemplateResponse(request, name, ...)`, so gradio's template name lands in the context slot | `starlette==0.27.0` |
| `'FieldInfo' object has no attribute 'in_'` in fastapi | pydantic 2.12 changed field-info internals used by fastapi 0.100 | `pydantic==2.5.3` |
| OAuth2 login route fails under newer fastapi | fastapi >= 0.104 incompatibility with gradio 3.41.2 | `fastapi==0.100.1` |

```powershell
.\fooocus_env\Scripts\python.exe -m pip install fastapi==0.100.1 starlette==0.27.0 pydantic==2.5.3 jinja2==3.0.3
```

Additionally, gradio 3.41.2's localhost reachability check
(`gradio/networking.py::url_ok`) fails behind a proxy and aborts `launch()` with
"When localhost is not accessible …". Local fix applied in site-packages:

```python
def url_ok(url: str) -> bool:
    return True
```

Launch with `--always-cpu` (no CUDA/DirectML) and `no_proxy=127.0.0.1`.
`launch.py` enables the NPU automatically when `..\qnn_env` and `..\sd_xl_npu`
exist; set `FOOOCUS_NPU=0` to force the CPU pipeline.

```powershell
$env:no_proxy = "127.0.0.1"
.\fooocus_env\Scripts\python.exe launch.py --always-cpu --listen 127.0.0.1 --port 7865
```

The torch SDXL pipeline is imported lazily (`modules/async_worker.py`), so NPU
text-to-image never loads the 7 GB checkpoint into RAM: the UI process stays
around 1 GB instead of ~16 GB. A task that falls through to the CPU pipeline
(enhance, upscale) imports it on demand and needs the preset checkpoint on disk.

### Verified result (Surface Pro 11, X1P64100)

- SDXL (default): 1024×1024, 6 steps = 24 s cold, 8 steps ~22 s warm
  (~2.0 s/it), visually comparable w8a16 output (no PSNR study); through the
  Fooocus bridge.
- SDXL inpaint: 1024×1024 region, 8 steps ≈ 20–30 s warm (masked-latent
  blending, no Fooocus inpaint head); VAE encoder + decoder both on QNN.
- SD 2.1: 512×512, ~0.36 s/step, 4 steps in 1.7 s warm.
- Metadata in `outputs/<date>/log.html` records the active backend
  (`SDXL Lightning on Hexagon NPU` / `SD 2.1 on Hexagon NPU`).

## Limits

- SDXL is fixed at 1024×1024; other aspect ratios need precompiled,
  weight-shared UNet/VAE variants.
- LoRA, refiner, ControlNet, IP-Adapter, enhance, and upscale are not wired to
  the NPU backend. Requests fall through to the CPU pipeline.
- Inpaint uses masked-latent blending, not the Fooocus inpaint head.
- Steps are clamped to 8 and CFG above 2.5 falls back to 2.0 for the Lightning
  model.
- The server serializes generations with a process-wide lock; it is a
  single-image backend, not a batch engine.
- The first request after a server start loads the five contexts and the text
  encoders; expect tens of seconds before the first step.
- CPU fallback tasks (enhance, upscale) still need Fooocus's default preset
  checkpoint on disk. `--disable-preset-download` skips the 7 GB download, but
  those tasks will fail until the checkpoint is present.
- Recompiling requires Qualcomm AI Hub or the AI Engine Direct SDK, which this
  machine cannot do locally.

## Troubleshooting

| Symptom | Fix |
|---|---|
| "64-bit x86 Python 3.10 not found" | Install the x64 (not ARM64) 3.10 build; the launcher checks `platform.machine() == AMD64`. |
| "Native ARM64 Python 3.12 not found" | Install the ARM64 3.12 build. The QNN wheel is ARM64-only. |
| UI stops with "When localhost is not accessible" | The script redefines `gradio.networking.url_ok` at the end of the module; that normally fixes it. `no_proxy`/`NO_PROXY` are set to `127.0.0.1,localhost`. |
| Share link never appears | `--share` needs outbound HTTPS to Gradio's tunnel service. Corporate proxies/firewalls can block it; the local UI still works on `http://127.0.0.1:7865`. |
| NPU tasks fail or fall back | See `fooocus-snapdragon-npu-experiment\Fooocus\npu\server_7867.log`. The first request loads the five UNet parts and can take ~60–90 s. |
| NPU not used | `launch.py` prints `[NPU] ... using the Hexagon NPU backend` when it selects the NPU. Confirm `qnn_env\Scripts\python.exe` and `sd_xl_npu` exist next to `Fooocus`. `FOOOCUS_NPU=1` forces it, `FOOOCUS_NPU=0` disables it. |
| Patch does not apply | Delete `fooocus-snapdragon-npu-experiment\Fooocus` and rerun. The diff is pinned to commit `ae05379cc97bc4361ec8b4ec90193dab21be763f`. |

## Assets and versions

| Item | Version / source |
|---|---|
| QNN runtime | `onnxruntime-qnn==2.7.0` (QNN 2.51) + `onnxruntime==1.31.1` |
| SDXL assets | `Buuta/dreamshaper-xl-lightning-for-Snapdragon-X-Elite` (MIT) |
| SD 2.1 assets | Qualcomm AI Hub `stable_diffusion_v2_1` w8a16 |
| Fooocus web stack | `gradio==3.41.2`, `fastapi==0.100.1`, `starlette==0.27.0`, `pydantic==2.5.3`, `jinja2==3.0.3` |
| Runtime layout | `sd_xl_npu/` and `qnn_env/` as siblings of `Fooocus/` |

Model directory layout:

```
sd_xl_npu/
  text_encoder/            CLIP-L
  text_encoder_2/          CLIP-G
  tokenizer/ tokenizer_2/  CLIP tokenizers
  unet_w8a16_quantized/    part0..part4 (2.5 GB total)
  vae_decoder/1024x1024/   decoder
  vae_encoder/1024x1024/   encoder, inpaint only
```

## Notes and licenses

- The UI stays on the CPU (x64 emulation); UNet, CLIP, VAE, and the assist
  models run on the Hexagon NPU through ONNX Runtime's QNN plugin EP.
- SDXL is fixed at 1024×1024, 8 steps, CFG 2.0 for the Lightning model.
- Inpainting uses masked-latent blending, not the original Fooocus inpaint head.
- This bundle only automates setup. Fooocus is GPL-3.0; the vendored SDXL
  pipeline is MIT. Review those licenses before redistribution.
