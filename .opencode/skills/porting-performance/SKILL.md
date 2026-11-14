---
name: Porting performance
description: Tune a working accelerator port — select backend-native kernels and dtypes, tune the host and warm caches, separate cold-start from steady state, and set honest memory budgets for AMX, ROCm, and TPU.
---

# Porting performance

Only start here after `porting-verification` passes. A fast wrong answer is still wrong.

## 1. Use the backend's fused, portable kernels

- Use `torch.autocast` with `bfloat16` where the backend has a fast path.
- Use PyTorch SDPA (`F.scaled_dot_product_attention`) when available.
- Disable xformers, split, or sub-quadratic kernels when they are not supported.
- Keep precision-sensitive pieces in fp32 if upstream does; Fooocus keeps CLIP text embeddings in fp32 while UNet/VAE run in bf16.
- Avoid manual per-op weight casting when storage and compute dtypes already match.
- Confirm the fused kernels are actually selected; do not infer it from code.

**Backend notes:**

- Intel AMX: bf16 inputs plus oneDNN dispatch gave AMX kernels without IPEX. IPEX `optimize` added overhead on Fooocus's `ModelPatcher`.
- AMD ROCm: `HSA_OVERRIDE_GFX_VERSION` was required because ROCm 7.2 shipped no rocBLAS kernels for `gfx1103`.
- Google TPU: bf16 + SDPA is the intended path; FP16 did not use the TPU SDPA fast path.

## 2. Tune the host and warm up the backend

Host-level settings often matter as much as the kernel path.

- Tune thread affinity/NUMA placement where applicable (`OMP_PROC_BIND`, `OMP_PLACES`).
- Consider `torch.set_flush_denormal(True)` on x86.
- Warm caches: oneDNN cache on CPU, MIOpen find mode on ROCm, PJRT compilation on TPU.
- On AMX, proper thread/denormal tuning produced measurable gains.

## 3. Measure cold and steady state separately

- Report first-run compile/discovery time separately from steady-state throughput.
- On TPU, the first request at a new shape took ~90 s; later 30-step runs took ~23–36 s.
- Keep shapes stable on static-shape backends; changing resolution, batch size, or tiled-decode settings may recompile. Seed changes do not.
- Compare against the baseline recorded during bring-up.

## 4. Set a real memory budget

- Check what the OS/driver reports versus what the runtime can actually allocate.
- Use low-VRAM/offload flags when the reported number is not a real budget.
- Keep tiled VAE decode as an escape hatch when full-resolution decode runs out of memory.
- Document the safe default resolution and batch size for the target.

## Performance checklist

- [ ] Measure cold start and steady state separately.
- [ ] Verify the intended kernels actually dispatch.
- [ ] Tune threads/NUMA/denormals and caches.
- [ ] Document memory ceilings and safe defaults.

For tested stacks and gotchas by target, read
[backend stacks](references/backend-stacks.md).
