---
name: Porting verification
description: Prove a ported AI app is correct before optimizing — verify weight loading, audit NaN/Inf conditioning, measure real memory, run a layered test ladder, run the bug-driven regression set, instrument the specific claim, and triage common failures.
---

# Porting verification

Do not jump from "it imports" to "the port works." Validate in layers and keep a headless reproducer for each layer.

## 1. Verify weight loading before debugging kernels

Black, flat, or NaN output is usually a loading or dtype problem, not a sampler problem.

- Compare checkpoint keys with the instantiated model's `state_dict` keys.
- Check how many keys were loaded; do not rely on `strict=False` to tell you.
- Be suspicious of `no_init_weights()` plus `strict=False`: unmatched parameters may stay uninitialised.
- Sanity-check with random weights: if random weights are finite but checkpoint weights are not, the compute path is probably fine and loading is broken.
- Add a regression check so the failure cannot return silently.

**Symptoms:** all-NaN `c_crossattn` / `pooled_output`, solid black images, or plausible-looking but meaningless output.

## 2. Audit conditioning and latents

- Run `torch.isfinite` over text and ADM conditioning before sampling.
- Audit the first sampled latent, not only the final image.
- Check the dtype and shape of conditioning tensors.
- Save a diagnostic script so the audit is repeatable.

## 3. Measure real memory, not reported memory

Reported VRAM can be shared, carved out, or compile-time inflated.

- Compare OS/driver reporting with what the runtime can actually allocate.
- In WSL, Fooocus saw 25.6 GB of shared GPU memory while only 7.7 GB of RAM was available.
- On the 780M, Windows reported a 4 GB UMA carve-out, which is the practical limit.
- On TPU, a 1152×896 run peaked at ~15.0 GiB of 15.75 GiB; 1024×1024 was the safer default.
- Prefer stable batch sizes and resolutions on static-shape backends; every new shape may recompile.

## 4. Follow a layered verification ladder

| Stage | Check | Useful signal |
| --- | --- | --- |
| 1. Imports | App imports without CUDA assumptions | clean import, no traceback |
| 2. Device | Framework sees the intended accelerator | `torch.accelerator`, `rocminfo`, device props |
| 3. Ops | Core ops run at the target dtype | matmul, SDPA, conv, norms, SiLU |
| 4. Weights | Checkpoint keys match and load | key counts, load report, finite parameters |
| 5. Conditioning | Text/ADM tensors are finite | `torch.isfinite` audit |
| 6. Generation | Full pipeline produces a real image | PNG with non-flat mean/std |
| 7. UI | Page serves and Generate completes | HTTP 200 plus `process_completed success=True` |
| 8. Performance | Cold and steady-state timings | compile time vs it/s vs baseline |

## 5. Instrument the layer that proves the claim

| Question | Tool |
| --- | --- |
| Did oneDNN select AMX kernels? | `ONEDNN_VERBOSE`, `processwatch` |
| Does ROCm see the GPU? | `rocminfo`, PyTorch device properties |
| Are the tensors finite? | `torch.isfinite` on conditioning, latents, outputs |
| Is the image real or flat? | mean/std of the saved PNG, visual check |
| Did the UI path finish? | websocket queue result, `process_completed success=True` |
| Was compilation the bottleneck? | time first shape vs repeated shape |

A passing smoke test is not proof. Prove the specific claim you are making.

## 6. Stabilize the UI stack separately

Old AI apps often carry old web stacks. Treat the UI as its own porting problem.

- Pin Gradio and its FastAPI/Pydantic/Starlette/websockets dependencies together.
- Expect symptoms such as `unhashable type: 'dict'`, changed `TemplateResponse` signatures, removed Pydantic fields, or client/server websocket mismatches.
- Restore removed NumPy aliases (`np.bool8`, `np.float_`) when old Gradio code needs them.
- Raise or disable queue HTTP timeouts when the first generation includes a long compile step; otherwise the browser websocket closes before the image arrives.
- Test the headless pipeline first, then page serving, then a real generation through the UI's own worker.

## 7. Run the bug-driven tests

The generic ladder above is necessary but not sufficient. Each Fooocus port had
a bug that a specific check would have caught: silent weight loss, NaN
conditioning, black output, silent CPU fallback, shared-memory VRAM, cold-start
time, a missing backend op, a downgraded dependency, a UI that serves but never
generates, and untested feature paths.

Run the full set in [suggested tests](references/suggested-tests.md) before
calling a port working. It includes runnable snippets for the key audit, the
finite audit, the non-flat image check, the memory probe, and the UI queue test.

Cheapest first: import → device probe → key audit → finite audit → one image →
UI queue → timing. Stop at the first failure; do not tune performance yet.

## Correctness checklist

- [ ] Verify checkpoint key matching and load counts.
- [ ] Audit conditioning and latents for NaN/Inf.
- [ ] Confirm a real, non-flat image is produced.
- [ ] Prove the intended accelerator and kernels are used, with CPU fallback disabled.
- [ ] Compare reported memory with real allocatable memory.
- [ ] Measure cold start and steady state separately.
- [ ] Exercise the app's own UI worker, not just a helper script.
- [ ] Record a feature-coverage matrix; mark fallbacks explicitly.
- [ ] Add regression checks for silent failures.

If output is wrong, black, or OOMs, read
[failure patterns](references/failure-patterns.md).

Next: load `porting-performance` only after this ladder passes.
