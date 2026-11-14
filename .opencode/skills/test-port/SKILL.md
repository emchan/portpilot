---
name: Test port
description: Auto-select the relevant port for the current platform, then clone, patch, and run Fooocus in an isolated folder with its own dependencies, ending in a smoke test.
---

# Test port

Validate a port end-to-end without touching the user's existing checkout. The
goal is a clean, reproducible answer to "does this port actually work on this
machine?" in one command.

## 1. Auto-select the port

Detect the platform and pick the matching port:

| Platform signal | Port |
| --- | --- |
| `torch.cuda` available, device name contains "Radeon" / `gfx110x` | AMD iGPU (ROCm) |
| `torch.accelerator` reports `tpu` | Google TPU |
| `torch.backends.mps.is_available()` | Apple Silicon (MPS) |
| `platform.machine()` in (`AMD64`, `x86_64`) on Windows + QNN env present | Qualcomm Snapdragon X |
| CPU with `amx` in `/proc/cpuinfo` flags | Intel AMX |
| otherwise | CPU fallback (Intel AMX `none` mode) |

Prefer the vendor's native stack (ROCm PyTorch, native `torch_tpu`) over
compatibility layers. If two signals match (e.g. a Mac with an eGPU), prefer
the more native path and record the choice.

## 2. Isolated folder

Never test in the user's checkout. Create a fresh directory:

```
/tmp/opencode/test-port-<port>-<timestamp>/
```

Everything (clone, patch, venv, models, logs) lives there. Delete it when done,
or keep it for debugging. This guarantees the test does not depend on (or pollute)
any existing environment.

## 3. Clone, patch, run

For the selected port:

1. Clone Fooocus at the pinned tag (`v2.5.5`, commit `ae05379` for Snapdragon).
2. Apply the port's diff with `git apply --check` first, then `git apply`.
3. Create an isolated venv (Python version per the port's write-up).
4. Install the port's dependency set (not the CUDA-era `requirements_versions.txt`
   on accelerator stacks).
5. Run the port's launcher with the documented flags.

Each port's write-up and setup script already encode these steps; reuse them
rather than re-deriving. The launcher should print the device it selected and
serve the UI on a known port.

## 4. Smoke test ladder

After launch, verify in order; stop at the first failure:

1. **Import** — `import webui` (or the port's entry) completes without traceback.
2. **Device probe** — the framework reports the intended accelerator and dtype.
3. **Kernel proof** — the intended kernel dispatched (oneDNN verbose, rocminfo,
   PJRT compile, etc.).
4. **Weight load** — checkpoint keys match and a non-zero number loaded.
5. **Finite audit** — conditioning and first latent are finite.
6. **One image** — a headless generation produces a non-flat PNG (mean/std check).
7. **UI serve** — HTTP 200 on the documented port; a real Generate completes with
   `process_completed success=True`.

Record the command, output, and result for each step in the port write-up.

## 5. Cleanup and report

- Stop the server.
- Keep the log and the generated image.
- Delete the isolated folder unless debugging.
- Report pass/fail per step, with the failing step and its log if any.

## Reference

The orchestrator is at [`references/test-port.py`](references/test-port.py). It
detects the platform, selects the port, and executes the clone/patch/run steps
in an isolated folder by default; use `--dry-run` to preview the commands.