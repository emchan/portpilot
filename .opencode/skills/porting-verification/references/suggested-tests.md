# Suggested tests, derived from real port bugs

Use this set before declaring a port working. Each test names what it catches
and the real failure it would have caught in the Fooocus ports. Keep a saved
command and log for each one, and turn any silent failure into a regression
test.

## Test ladder (cheapest first)

1. Import the app with no device-specific code running.
2. Probe the accelerator and print its type.
3. Run core ops at the target dtype.
4. Audit checkpoint keys and load counts.
5. Audit conditioning and the first latent for NaN/Inf.
6. Generate one headless image and check it is non-flat.
7. Drive the app's own UI queue end to end.
8. Measure cold and warm timing, plus real memory.
9. Fill in a feature-coverage matrix.

If any step fails, stop. Do not tune performance yet.

## 1. Checkpoint key audit

**Catches:** `strict=False` masking a layout change; `no_init_weights()`
leaving parameters uninitialised; a major-version loader that silently matches
nothing.

```python
import torch
sd = torch.load(path, map_location="cpu", weights_only=True)
model = build_model()
keys = model.state_dict()
matched = [k for k in sd if k in keys]
missing = [k for k in keys if k not in sd]
extra = [k for k in sd if k not in keys]
print("matched", len(matched), "missing", len(missing), "extra", len(extra))
assert matched, "no checkpoint keys loaded"
assert all(torch.isfinite(v).all() for v in model.parameters())
```

**Bit us:** TPU — Transformers 5 flattened `CLIPTextModel`; `strict=False` loaded
zero keys and uninitialised TPU memory was NaN, so every image was black. AMX —
the same layout change needed a key remap.

## 2. Finite-conditioning audit

**Catches:** NaN conditioning and black images with no exception.

```python
for name, t in [("c_crossattn", cond), ("pooled", pooled), ("adm", adm),
                ("latent", latent)]:
    print(name, tuple(t.shape), t.dtype, "finite=", torch.isfinite(t).all().item())
assert all(torch.isfinite(t).all() for t in (cond, pooled, adm, latent))
```

**Bit us:** TPU — all-NaN `c_crossattn` / `pooled_output`.

## 3. Random-weight control

**Catches:** wasted debugging on the compute path when loading is the problem.

Build the same model from random weights. If random weights are finite but
checkpoint weights are not, loading is broken; if both are non-finite, look at
compute and dtype.

**Bit us:** TPU — random-weight instances were finite, which proved the compute
path was fine and pointed at weight loading.

## 4. Non-flat image check

**Catches:** a pipeline that "runs" but emits black or flat output; a missing
checkpoint behind a UI that serves HTTP 200.

```python
from PIL import Image
import numpy as np
a = np.asarray(Image.open(path).convert("RGB"), dtype=np.float32)
print("mean", a.mean(), "std", a.std(), "min", a.min(), "max", a.max())
assert a.std() > 10 and a.max() > 40, "image looks flat or black"
```

**Bit us:** AMD — the UI served HTTP 200 while the checkpoint was missing, so
generation never worked. TPU — saved images were checked with mean/std
(mean 110, std 58.5 at 1024²; mean 84.8, std 54.6 through the UI).

## 5. Accelerator-usage proof

**Catches:** silent CPU fallback; a backend API that reports success while
running on the CPU; the wrong device selected.

- Print `torch.accelerator.current_accelerator()` / `device.type` and the model's
  parameter device.
- For oneDNN/AMX: `ONEDNN_VERBOSE=1` and `processwatch`.
- For ROCm: `rocminfo`, PyTorch device properties.
- Disable CPU fallback during the test so an unsupported op fails loudly.

**Bit us:** Snapdragon — `providers=["QNNExecutionProvider"]` silently fell back
to CPU; the plugin EP had to be registered explicitly. AMX — `ONEDNN_VERBOSE`
confirmed `avx10_1_512_amx` kernels.

## 6. Real-allocatable memory probe

**Catches:** reported VRAM that is shared, carved out, or compile-time inflated.

```python
# Compare driver-reported memory with what the runtime can actually allocate.
free, total = torch.cuda.mem_get_info()  # or the backend equivalent
print("reported free MiB", free // 2**20, "total", total // 2**20)
blobs = []
try:
    while True:
        blobs.append(torch.empty(256, 256, 256, device=dev))
except torch.OutOfMemoryError:
    print("allocated before OOM:", sum(b.numel() for b in blobs) * 4 / 2**30, "GiB")
```

**Bit us:** AMD/WSL — Fooocus saw 25.6 GB of shared GPU memory while the VM had
7.7 GB of RAM; the 780M has a 4 GB UMA carve-out. Apple — SDXL needs ~26 GB on
unified memory, so a 16 GB Mac swaps even with int4.

## 7. Cold-vs-warm timing

**Catches:** compile time or first-load time reported as per-step speed.

- Time the first request at a new shape, then a repeated request at the same
  shape.
- Log peak memory for both.
- On static-shape backends, treat every new shape as a cold start.

**Bit us:** TPU — the first 1152×896 shape took ~90 s to compile, then ~2.4
it/s. Snapdragon — the first NPU request pays a 60–90 s context load.

## 8. Core-op dtype ladder

**Catches:** dtype mismatches and backend-missing ops that only appear in a full
generation.

For the target dtype, run matmul, SDPA, conv, layer norm, and SiLU; assert the
output dtype and finiteness.

**Bit us:** TPU — bf16 tensors could not convert to NumPy without `.float()`;
`aten::std_mean.correction` was unimplemented; `torch.autocast(device_type="cuda")`
failed. Apple — `std_mean` is missing on MPS and relies on fallback.

## 9. Dependency dry-run

**Catches:** an install step that quietly replaces or downgrades the accelerator
stack.

- Build the environment in a throwaway venv first.
- Diff installed versions against the preinstalled accelerator stack.
- Do not run CUDA-era requirements over a preinstalled backend stack.
- Check that `pip` itself exists when the app shells out to it.

**Bit us:** TPU — `pip` downgraded numpy and broke `torch_tpu`; the port skips
`requirements_versions.txt`. AMD — the ROCm index shadowed PyPI for `tqdm`, and a
`uv` venv had no `pip` for `launch.py`.

## 10. UI worker end-to-end

**Catches:** a UI that serves but never completes a generation.

- Serve the app and confirm HTTP 200.
- Drive the app's own queue (for Fooocus: the websocket `/queue/join` +
  `/queue/data` chain behind `generate_clicked`), not a helper script.
- Assert `process_completed success=True` and a non-flat gallery image.
- Raise or disable the queue HTTP timeout when the first step includes a long
  compile.

**Bit us:** AMD — page serving passed while generation was unavailable. TPU —
Gradio's 5 s httpx timeout closed the websocket before the first TPU step
finished. Snapdragon — the two-process bridge must return a PNG over HTTP.

## 11. Feature-coverage matrix

**Catches:** untested request paths reported as working; silent fallback for
unsupported tasks.

List every entry point (text-to-image, inpaint, outpaint, upscale, vary,
enhance, describe, ControlNet, IP-Adapter, refiner) and mark each as tested,
fallback, or untested. Make fallback explicit in the UI or the logs.

**Bit us:** Snapdragon — LoRA, refiner, ControlNet, IP-Adapter, enhance, and
upscale are not wired to the NPU and fall through to CPU. TPU — inpaint,
upscale, enhance, face, and ControlNet were not exercised.

## What to record

For every test, keep in the port write-up:

- the exact command,
- the observed output or a saved log,
- the expected result, and
- a regression test for any failure that was silent.

See [failure patterns](failure-patterns.md) for triage order when a test fails.
