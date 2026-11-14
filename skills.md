# Porting Skills

Practical skills distilled from the Fooocus ports in this repo:

- [Intel AMX CPU](fooocus/Intel_AMX/README.md)
- [AMD Radeon 780M iGPU via ROCm/WSL2](fooocus/AMD_iGPU/README.md)
- [Google TPU via native `torch_tpu`](fooocus/Google_TPU/README.md)
- [Apple Silicon via MPS](fooocus/Apple_Silicon/README.md)
- [Qualcomm Snapdragon X via Hexagon NPU](fooocus/Qualcomm_Snapdragon/README.md)

The details differ by vendor, but the same skills keep showing up.

> **OpenCode:** these lessons are also packaged as focused, auto-generated skills in [`.opencode/skills/`](.opencode/skills/). This file is the consolidated human-readable version.

| OpenCode skill | Covers |
| --- | --- |
| [`porting`](.opencode/skills/porting/SKILL.md) | Universal rules, phase map, definition of done |
| [`hardware-probe`](.opencode/skills/hardware-probe/SKILL.md) | FLOPS, numerics, memory capacity and bandwidth, kernel dispatch |
| [`porting-bringup`](.opencode/skills/porting-bringup/SKILL.md) | Baseline, native path, conditional backend, dependencies, dtype/kernels |
| [`model-analysis`](.opencode/skills/model-analysis/SKILL.md) | Operators, weight shapes, activation shapes, weight/activation precision |
| [`porting-verification`](.opencode/skills/porting-verification/SKILL.md) | Weight loading, NaN audits, memory, verification ladder, bug-driven test set, UI stack |
| [`porting-performance`](.opencode/skills/porting-performance/SKILL.md) | Host tuning, cold vs steady state, memory budgets, backend reference |
| [`porting-agents`](.opencode/skills/porting-agents/SKILL.md) | Agent workflow and escalation |
| [`anonymize`](.opencode/skills/anonymize/SKILL.md) | Path, username, host, IP, email, and secret scrubbing |
| [`polite-language`](.opencode/skills/polite-language/SKILL.md) | Non-disparaging wording; neutral status phrasing |
| [`test-port`](.opencode/skills/test-port/SKILL.md) | Auto-select port, isolated clone/patch/run, smoke test |

## Universal rules

1. **Correctness first, speed second.** A fast port that silently loads no weights is worse than a slow one that works.
2. **New hardware rarely breaks compute; device assumptions and dependency changes do.**
3. **Keep the new backend conditional.** Existing CUDA/MPS/XPU/CPU paths should behave exactly as before.
4. **Silent fallbacks are the enemy.** Assert that the intended backend, kernels, and weights were actually used.
5. **Measure cold and steady state separately.** Compilation and first-run caches distort benchmarks.

---

## Skill 1 — Establish a reproducible baseline

Before changing code, record what "working" means and what you started from.

- Pin the upstream repo, branch, tag, and commit.
- Record the hardware, OS, driver, Python, framework, and accelerator stack versions.
- Capture the upstream install command and any upstream pins.
- Establish a known-good baseline on an existing backend if possible.
- Define the finish line: import, device detected, one image, UI loads, UI generates, timing.

**Why:** Most porting regressions are version or environment drift, not algorithmic mistakes. A baseline turns "it broke" into "this changed."

---

## Skill 2 — Choose the most native access path

Prefer the path with the fewest translation layers:

1. Vendor-supported framework build (for example ROCm PyTorch, native `torch_tpu`).
2. Official compatibility layer (for example DirectML).
3. Fallback application or CPU.

Check the official support matrix before committing. An unsupported device can often be made to work with a compatibility override, but treat that as a shim, not a supported configuration.

**Example findings:**

- ROCm on WSL2 was the recommended path and the only GPU-accelerated option that ran Fooocus unmodified.
- Native Windows ROCm does not target the 780M, and ZLUDA had no maintained Fooocus path.
- TPU needed `torch_tpu` directly; `torch_xla` was not part of the port.
- Intel AMX needed no IPEX `optimize` for the baseline speedup — plain bf16 autocast was enough.

---

## Skill 3 — Detect the backend, don't fork the codebase

Make device selection explicit and conservative. A single probe should drive device, dtype, memory accounting, attention backend, OOM handling, and launcher behavior.

Illustrative pattern:

```python
def has_accelerator(kind: str) -> bool:
    return (
        torch.accelerator.is_available()
        and torch.accelerator.current_accelerator().type == kind
    )
```

Things that must become conditional:

- `torch.cuda.*` calls
- `torch.backends.cuda.*` and `torch.backends.cudnn.*`
- `torch.autocast(device_type="cuda", ...)` — use the tensor's device type instead
- CUDA-only OOM exception classes
- CUDA memory query APIs
- xformers and other CUDA-only attention kernels
- FP8 and other vendor-specific paths

**Rule:** if the new backend is unavailable, every change should be inert.

---

## Skill 4 — Treat dependency upgrades as code changes

Porting to new hardware often forces new library versions. That is not a neutral operation.

- Align Python and wheel availability first. Old pins may simply not exist for the target Python.
- Do **not** install CUDA-era requirements over a preinstalled accelerator stack. The TPU port skips `requirements_versions.txt` for this reason.
- Pin the UI web stack separately when an old app needs old FastAPI/Pydantic/Starlette versions.
- Expect API moves and layout changes in `transformers`, `numpy`, and similar libraries.
- Re-read loaders and constructors after a major-version bump; do not assume the old call still means the same thing.
- Record the final tested versions in the write-up.

**Key lesson:** a dependency bump can introduce a correctness bug with no API error. Transformers 5 flattened CLIP's `text_model` layout, and Fooocus's `strict=False` load silently matched zero keys. On TPU that produced NaN conditioning and black images. The bug did not exist on the original Transformers 4.x stack.

---

## Skill 5 — Verify weight loading before debugging kernels

Black, flat, or NaN output is usually a loading or dtype problem, not a sampler problem.

- Compare checkpoint keys with the instantiated model's `state_dict` keys.
- Check how many keys were loaded; do not rely on `strict=False` to tell you.
- Be suspicious of `no_init_weights()` plus `strict=False`: unmatched parameters may stay uninitialised.
- Run a finite/NaN audit on conditioning tensors and the first sampled latent.
- Sanity-check with random weights: if random weights are finite but checkpoint weights are not, the compute path is probably fine and loading is broken.
- Add a regression check so the failure cannot return silently.

**Symptoms:** all-NaN `c_crossattn` / `pooled_output`, solid black images, or plausible-looking but meaningless output.

---

## Skill 6 — Use backend-native compute and dtype

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

---

## Skill 7 — Measure real memory, not reported memory

Reported VRAM can be shared, carved out, or compile-time inflated.

- Check what the OS/driver reports versus what the runtime can actually allocate.
- In WSL, Fooocus saw 25.6 GB of shared GPU memory while only 7.7 GB of RAM was available.
- On the 780M, Windows reported a 4 GB UMA carve-out, which is the practical limit.
- On TPU, a 1152×896 run peaked at ~15.0 GiB of 15.75 GiB; 1024×1024 was the safer default.
- Use low-VRAM/offload flags when the reported number is not a real limit.
- Keep tiled VAE decode as an escape hatch when full-resolution decode runs out of memory.
- Prefer stable batch sizes and resolutions on static-shape backends; every new shape may recompile.

---

## Skill 8 — Tune the host and warm up the backend

Host-level settings often matter as much as the kernel path.

- Tune thread affinity/NUMA placement where applicable (`OMP_PROC_BIND`, `OMP_PLACES`).
- Consider `torch.set_flush_denormal(True)` on x86.
- Warm caches: oneDNN cache on CPU, MIOpen find mode on ROCm, PJRT compilation on TPU.
- Distinguish cold-start time from steady-state throughput.
- On TPU, the first request at a new shape took ~90 s; later 30-step runs took ~23–36 s.
- On AMX, proper thread/denormal tuning produced measurable gains.

---

## Skill 9 — Stabilize the UI stack separately

Old AI apps often carry old web stacks. Treat the UI as its own porting problem.

- Pin Gradio and its FastAPI/Pydantic/Starlette/websockets dependencies together.
- Expect symptoms such as `unhashable type: 'dict'`, changed `TemplateResponse` signatures, removed Pydantic fields, or client/server websocket mismatches.
- Restore removed NumPy aliases (`np.bool8`, `np.float_`) when old Gradio code needs them.
- Raise or disable queue HTTP timeouts when the first generation includes a long compile step; otherwise the browser websocket closes before the image arrives.
- Test the headless pipeline first, then page serving, then a real generation through the UI's own worker.

---

## Skill 10 — Build a verification ladder

Do not jump from "it imports" to "the port works." Validate in layers.

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

Keep a headless reproducer for each layer. It is faster than the UI and isolates failures.

---

## Skill 11 — Instrument the layer that can prove your claim

Match the tool to the question:

| Question | Tool |
| --- | --- |
| Did oneDNN select AMX kernels? | `ONEDNN_VERBOSE`, `processwatch` |
| Does ROCm see the GPU? | `rocminfo`, PyTorch device properties |
| Are the tensors finite? | `torch.isfinite` on conditioning, latents, outputs |
| Is the image real or flat? | mean/std of the saved PNG, visual check |
| Did the UI path finish? | websocket queue result, `process_completed success=True` |
| Was compilation the bottleneck? | time first shape vs repeated shape |

A passing smoke test is not proof. Prove the specific claim you are making.

---

## Skill 12 — Work effectively with agents

Agent-driven porting works best when the loop is tight and evidence-based.

- Start with fast/free models, then escalate to stronger models when progress stalls.
- Ask for the smallest reproducible failure, not a full rewrite.
- Prefer patches at existing extension points (`modules/patch.py`) over model surgery.
- Require commands, logs, and diffs to be captured in the repo.
- Re-check assumptions against the installed library. Agents often assume return arity, property names, or API shapes.
- Watch for late-binding bugs in monkeypatches; bind the original function explicitly.
- Make the agent explain the root cause before accepting a fix.
- Add a regression check for every silent failure it finds.

---

## Skill 13 — Anonymize before publishing

A working port is not ready to share until it stops describing your machine.

- Scan READMEs, diffs, scripts, and logs for `/home/<name>`, `/Users/<name>`,
  `C:\Users\<name>`, extra drive letters, UNC shares, internal hostnames,
  private IPs, personal emails, and secrets.
- Replace only the identifying segment, and keep one placeholder convention:
  `/home/<you>`, `/Users/<you>`, `C:\Users\<you>`, `Z:\path\to\...`.
- Use RFC 5737 documentation ranges for IPs and `example.com` for hosts.
- Keep upstream URLs, vendor names, and any intentionally published author
  contact as documented exceptions.
- Do not `sed` paths containing backslashes; edit the raw text so patches keep
  single escapes and still parse.
- Re-run the scanner, `git apply --stat` on every diff, and a link check. If the
  identifier was already committed, rewrite history and rotate any secret.
- Check commit metadata separately with
  `git log --all --format='%h %an <%ae>'`; the file scanner does not read git
  objects, and author emails are published with the commit.

The `anonymize` skill includes a report-only scanner at
[`references/anonymize-scan.py`](.opencode/skills/anonymize/references/anonymize-scan.py).

---

## Skill 13b — Use polite, non-disparaging language

Technical writing describes what happened; it does not judge people, vendors, or
code. A slow kernel is "not yet optimized"; a failing test is "not yet passing";
an unfinished feature is "planned", not "broken".

- Describe status, not character: "the test did not complete" beats "the test failed".
- Attribute limits to the work, not the vendor: "not yet optimized on this backend".
- Keep numbers: "2.9 s for SD 2.1" is neutral; "slow" is not.
- Do not soften facts that matter for correctness. A NaN is a NaN.
- Run the scanner over READMEs, diffs, commit messages, and issue text before publishing.

The report-only scanner is at
[`polite-language/references/polite-scan.py`](.opencode/skills/polite-language/references/polite-scan.py).

---

## Skill 14 — Probe hardware capability

Do not plan a port from a spec sheet. Reported TFLOPS, VRAM, and bandwidth are
upper bounds; real numbers depend on dtype, shape, kernel selection, allocator
behaviour, and whether the runtime can actually allocate that memory.

- Record device, driver, Python, torch, and accelerator-stack versions.
- Measure reported and allocatable memory (allocate-until-OOM, capped).
- Measure memory bandwidth with a large copy at the target dtype.
- Measure FLOPS for fp32/fp16/bf16 at two sizes, cold and warm.
- Run numerics micro-tests: accumulation precision, NaN/Inf rules, uninitialised
  memory, dtype conversion, reduction availability.
- Confirm kernel dispatch with the backend's verbose/profiler tool.

The runnable probe is in
[`hardware-probe/references/probe.py`](.opencode/skills/hardware-probe/references/probe.py).

---

## Skill 15 — Analyse the model

A port is planned against the model, not the app. Before changing code, know
which operators run, how large the weights are, what shapes flow through the
network, and at what precision.

- Enumerate operators (conv, attention, norms, activations, reductions) and
  flag ops with no native kernel on the target.
- Print weight shapes, dtypes, and parameter counts per component.
- Record activation shapes at the default resolution (latent, attention
  sequence length).
- Record storage vs compute dtype for every component, and any quantization
  scheme (NF4 int4, w8a16).
- Use the results for memory budgets, kernel selection, shape stability, and
  numerics.

The interactive model map is in
[`fooocus/architecture/model_details.html`](fooocus/architecture/model_details.html).

---

## Skill 16 — Run the bug-driven test set

The generic ladder is necessary but not sufficient. Every Fooocus port had a bug
that one specific check would have caught. Run this set before calling a port
working; the runnable snippets live in the
[`porting-verification` skill](.opencode/skills/porting-verification/SKILL.md).

| Test | What it catches | Where it bit |
| --- | --- | --- |
| Checkpoint key audit | `strict=False` hiding a layout change; uninitialised params | TPU CLIP, AMX CLIP |
| Finite-conditioning audit | NaN conditioning and black images | TPU |
| Random-weight control | Broken loading vs broken compute | TPU |
| Non-flat image check | Black/flat output; missing checkpoint behind HTTP 200 | AMD, TPU |
| Accelerator-usage proof | Silent CPU fallback; wrong device | Snapdragon, AMX |
| Real-allocatable memory probe | Shared VRAM, UMA carve-out, compile peak | AMD, Apple |
| Cold-vs-warm timing | Compile time reported as per-step speed | TPU, Snapdragon |
| Core-op dtype ladder | bf16→NumPy, CUDA-only autocast, missing ops | TPU, Apple |
| Dependency dry-run | Downgraded numpy/`torch_tpu`, index shadowing, missing `pip` | TPU, AMD |
| UI worker end-to-end | UI serves but generation never finishes | AMD, TPU, Snapdragon |
| Feature-coverage matrix | Untested paths reported as working | Snapdragon, TPU |

Cheapest first: import → device probe → key audit → finite audit → one image →
UI queue → timing. Save the command, output, and expected result for each test,
and write a regression test for any failure that was silent.

---

## Skill 17 — Test a port end-to-end

Validate a port in an isolated folder without touching the user's checkout.

- Auto-select the port from platform signals (CUDA/ROCm, TPU, MPS, Windows+QNN, AMX).
- Clone Fooocus at the pinned tag into `/tmp/opencode/test-port-<port>-<ts>/`.
- Apply the port's diff (`git apply --check` first).
- Create an isolated venv and install the port's dependency set.
- Run the launcher and execute the smoke-test ladder: import → device probe →
  kernel proof → weight load → finite audit → one image → UI serve.
- Record the command, output, and result for each step; keep the log and image.

The orchestrator is at
[`test-port/references/test-port.py`](.opencode/skills/test-port/references/test-port.py).

---

## Reusable porting checklist

### Recon

- [ ] Pin source commit/tag and record the date.
- [ ] Record hardware, OS, driver, Python, torch, and accelerator versions.
- [ ] Run the app on a known-good backend if possible.
- [ ] Check the vendor support matrix and choose the native path first.

### Bring-up

- [ ] Probe the accelerator and gate all vendor-specific code.
- [ ] Replace hard-coded `cuda` device and autocast assumptions.
- [ ] Make OOM handling and memory queries backend-aware.
- [ ] Select bf16/SDPA or the backend's equivalent fast path.
- [ ] Disable unsupported attention backends explicitly.
- [ ] Pin a compatible web stack.

### Correctness

- [ ] Verify checkpoint key matching and load counts.
- [ ] Audit conditioning and latents for NaN/Inf.
- [ ] Confirm a real, non-flat image is produced.
- [ ] Prove the intended accelerator and kernels are used, with CPU fallback disabled.
- [ ] Compare reported memory with real allocatable memory.
- [ ] Measure cold start and steady state separately.
- [ ] Exercise the app's own UI worker, not just a helper script.
- [ ] Record a feature-coverage matrix; mark fallbacks explicitly.
- [ ] Run the bug-driven test set and save each command and result.
- [ ] Add regression checks for silent failures.

### Performance

- [ ] Measure cold start and steady state separately.
- [ ] Verify the intended kernels actually dispatch.
- [ ] Tune threads/NUMA/denormals and caches.
- [ ] Document memory ceilings and safe defaults.

---

## Common failure patterns

| Symptom | Likely cause | First check |
| --- | --- | --- |
| Black or flat images | Weights not loaded, dtype mismatch, NaN | state-dict keys, finite audit |
| Import-time CUDA crash | Unconditional `torch.cuda.*` | gate CUDA calls behind a probe |
| Wrong device selected | Backend detection too broad | print accelerator and device type |
| Missing kernels on AMD | Unsupported `gfx` target | `rocminfo`, `HSA_OVERRIDE_GFX_VERSION` |
| OOM despite "free" memory | Shared memory / UMA / compile peak | real allocatable memory, low-VRAM mode |
| Very slow attention | xformers unavailable, basic attention selected | force SDPA |
| UI exits before serving | Gradio/web-stack version mismatch | pin FastAPI/Pydantic/Starlette/websockets |
| Websocket closes mid-generation | HTTP queue timeout shorter than first step | disable/raise queue client timeout |
| `pip` breaks the accelerator stack | CUDA-era requirements installed over it | skip `requirements_versions.txt` |
| Plausible output but wrong result | Silent API or layout drift | compare library version behavior, load reports |
| Nothing loads but no error | `strict=False` plus a layout change | key audit, finite audit, random-weight control |
| UI serves but generation never completes | Queue timeout or missing asset | drive the UI worker; assert `success=True` |
| Backend API reports success but runs on CPU | EP/provider silently ignored | device proof, kernel counters, disable fallback |

---

## Backend quick reference

| Target | Working stack | Key gotchas | Verification |
| --- | --- | --- | --- |
| Intel AMX CPU | PyTorch CPU + oneDNN, bf16 autocast | Python 3.13 wheel gaps; IPEX `optimize` may be slower; thread/denormal tuning | `ONEDNN_VERBOSE`, `processwatch` |
| AMD Radeon 780M iGPU | ROCm 7.2.4 + PyTorch ROCm wheels in WSL2 | `gfx1103` needs `HSA_OVERRIDE_GFX_VERSION`; WSL/DXG profiler and allocator quirks; shared-memory illusion | `rocminfo`, PyTorch device props, image test |
| Google TPU | Native `torch_tpu`, bf16 + SDPA | Transformers 5 CLIP layout; Gradio timeouts/NumPy aliases; PJRT compile on new shapes | finite audit, full generation, UI queue test |
