---
name: Porting bring-up
description: Get an AI application running on a new accelerator — record a reproducible baseline, pick the most native access path, gate device-specific code, and handle dependency upgrades and dtype/kernel selection.
---

# Porting bring-up

## 1. Record a reproducible baseline

Before changing code, record what "working" means and what you started from.

- Pin the upstream repo, branch, tag, commit, and date.
- Record hardware, OS, driver, Python, framework, and accelerator stack versions.
- Capture the upstream install command and any upstream pins.
- Establish a known-good baseline on an existing backend if possible.
- Define the finish line: import, device detected, one image, UI loads, UI generates, timing.

**Why:** Most porting regressions are version or environment drift, not algorithmic mistakes. A baseline turns "it broke" into "this changed."

## 2. Choose the most native access path

Prefer the path with the fewest translation layers:

1. Vendor-supported framework build (for example ROCm PyTorch, native `torch_tpu`).
2. Official compatibility layer (for example DirectML).
3. Fallback application or CPU.

Check the official support matrix before committing. An unsupported device can often be made to work with a compatibility override, but treat that as a shim, not a supported configuration.

**Example findings:**

- ROCm on WSL2 was the recommended path and the only GPU-accelerated option that ran Fooocus unmodified on the 780M.
- Native Windows ROCm does not target the 780M, and ZLUDA had no maintained Fooocus path.
- TPU needed `torch_tpu` directly; `torch_xla` was not part of the port.
- Intel AMX needed no IPEX `optimize` for the baseline speedup — plain bf16 autocast was enough.

## 3. Keep the new backend conditional

Make device selection explicit and conservative. A single probe should drive device, dtype, memory accounting, attention backend, OOM handling, and launcher behavior.

```python
def has_accelerator(kind: str) -> bool:
    return (
        torch.accelerator.is_available()
        and torch.accelerator.current_accelerator().type == kind
    )
```

Make these conditional:

- `torch.cuda.*` calls
- `torch.backends.cuda.*` and `torch.backends.cudnn.*`
- `torch.autocast(device_type="cuda", ...)` — use the tensor's device type instead
- CUDA-only OOM exception classes
- CUDA memory query APIs
- xformers and other CUDA-only attention kernels
- FP8 and other vendor-specific paths

**Rule:** if the new backend is unavailable, every change should be inert.

## 4. Treat dependency upgrades as code changes

Porting to new hardware often forces new library versions. That is not a neutral operation.

- Align Python and wheel availability first. Old pins may simply not exist for the target Python.
- Do **not** install CUDA-era requirements over a preinstalled accelerator stack. The TPU port skips `requirements_versions.txt` for this reason.
- Pin the UI web stack separately when an old app needs old FastAPI/Pydantic/Starlette versions.
- Expect API moves and layout changes in `transformers`, `numpy`, and similar libraries.
- Re-read loaders and constructors after a major-version bump; do not assume the old call still means the same thing.
- Record the final tested versions in the write-up.

**Key lesson:** a dependency bump can introduce a correctness bug with no API error. Transformers 5 flattened CLIP's `text_model` layout, and Fooocus's `strict=False` load silently matched zero keys. On TPU that produced NaN conditioning and black images. The bug did not exist on the original Transformers 4.x stack.

## 5. Use backend-native compute and dtype

Prefer the framework's fused, portable kernels over vendor-specific ones.

- Use `torch.autocast` with `bfloat16` where the backend has a fast path.
- Use PyTorch SDPA (`F.scaled_dot_product_attention`) when available.
- Disable xformers, split, or sub-quadratic kernels when they are not supported.
- Keep precision-sensitive pieces in fp32 if upstream does; Fooocus keeps CLIP text embeddings in fp32 while UNet/VAE run in bf16.
- Avoid manual per-op weight casting when storage and compute dtypes already match.
- Confirm fused kernels are actually selected; do not infer it from code.

**Backend notes:**

- Intel AMX: bf16 inputs plus oneDNN dispatch gave AMX kernels without IPEX.
- AMD ROCm: `HSA_OVERRIDE_GFX_VERSION` was required because ROCm 7.2 shipped no rocBLAS kernels for `gfx1103`.
- Google TPU: bf16 + SDPA is the intended path; FP16 did not use the TPU SDPA fast path.

## Bring-up checklist

- [ ] Pin source commit/tag and record the date.
- [ ] Record hardware, OS, driver, Python, torch, and accelerator versions.
- [ ] Run the app on a known-good backend if possible.
- [ ] Check the vendor support matrix and choose the native path first.
- [ ] Probe the accelerator and gate all vendor-specific code.
- [ ] Replace hard-coded `cuda` device and autocast assumptions.
- [ ] Make OOM handling and memory queries backend-aware.
- [ ] Select bf16/SDPA or the backend's equivalent fast path.
- [ ] Disable unsupported attention backends explicitly.
- [ ] Pin a compatible web stack.

Next: load `porting-verification` before tuning performance.
