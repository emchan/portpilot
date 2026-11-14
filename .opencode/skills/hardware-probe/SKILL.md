---
name: Hardware capability probe
description: Probe an accelerator before and during a port — FLOPS, numerics, memory capacity and bandwidth, and kernel dispatch — so ports are planned against real hardware limits rather than reported specs.
---

# Hardware capability probe

Do not plan a port from a spec sheet. Reported TFLOPS, VRAM, and bandwidth are
upper bounds; real numbers depend on dtype, shape, kernel selection, allocator
behaviour, and whether the runtime can actually allocate that memory.

Run this probe before bring-up (to choose a backend and a safe default) and again
after the port (to confirm the intended kernels and dtype are in use).

## 1. What to probe

| Quantity | Why it matters | Typical tool |
| --- | --- | --- |
| Device identity | Confirms the backend you think you are using | `torch.accelerator`, `rocminfo`, device props |
| Reported memory | Upper bound only | framework memory API, driver tools |
| Allocatable memory | Real budget after allocator and fragmentation | allocate-until-OOM probe |
| Memory bandwidth | Whether you are compute- or memory-bound | large tensor copy / reduction |
| FLOPS (fp32/fp16/bf16) | Whether the accelerator's fast path is engaged | timed matmul at a few sizes |
| Numerics | Accumulation precision, NaN/Inf rules, dtype conversion | targeted micro-tests |
| Kernel dispatch | Whether fused kernels actually ran | verbose env vars, profilers |

## 2. Device identity

```python
import torch
acc = torch.accelerator.current_accelerator() if torch.accelerator.is_available() else None
print("accelerator:", acc)
print("device type:", acc.type if acc is not None else "cpu")
print("device count:", torch.cuda.device_count() if torch.cuda.is_available() else 1)
```

Also print the driver/stack versions (ROCm, oneDNN, PJRT, MPS) and the Python
and torch versions. A probe without versions is not reproducible.

## 3. Memory capacity

Reported numbers lie, especially on shared/UMA setups.

- **WSL** reported 25.6 GB of shared GPU memory while the VM had 7.7 GB of RAM.
- The **Radeon 780M** has a 4 GB UMA carve-out, which is the real limit.
- **TPU** reports 16,126 MiB but a 1152×896 SDXL run peaked at ~15.0 GiB.
- **Apple Silicon** has no separate VRAM; unified memory plus swap is the budget.

Always run the allocatable probe:

```python
def allocatable(dev, dtype=torch.float16, chunk_mb=256):
    blobs, total = [], 0
    try:
        while True:
            b = torch.empty(chunk_mb * 1024 * 1024 // torch.tensor([], dtype=dtype).element_size(),
                            device=dev, dtype=dtype)
            blobs.append(b); total += b.numel() * b.element_size()
    except (torch.OutOfMemoryError, RuntimeError):
        pass
    return total / (1024 ** 3)
```

Record both the reported and the allocatable number, and the allocator config
(`PYTORCH_HIP_ALLOC_CONF`, `PYTORCH_MPS_HIGH_WATERMARK_RATIO`, expandable
segments). The same hardware can have different allocatable memory depending on
those settings.

## 4. Memory bandwidth

Use a large tensor copy or reduction; warm up first and time the steady state.

```python
a = torch.empty(N, device=dev, dtype=torch.float16)
b = torch.empty_like(a)
torch.cuda.synchronize() if torch.cuda.is_available() else None
t0 = time.perf_counter()
for _ in range(iters):
    b.copy_(a)
torch.cuda.synchronize() if torch.cuda.is_available() else None
gb_s = a.numel() * a.element_size() * iters / (time.perf_counter() - t0) / 1e9
```

Compare against the vendor's published bandwidth. A large shortfall usually
means the copy went through a slow path or the wrong memory (host vs device).

## 5. FLOPS

Time a matmul at a few sizes and dtypes. Use a size large enough to saturate
the device (e.g. 4096³) and a small number of warm-up iterations.

```python
def matmul_ms(m, n, k, dtype, dev, iters=10, warmup=3):
    a = torch.randn(m, k, device=dev, dtype=dtype)
    b = torch.randn(k, n, device=dev, dtype=dtype)
    for _ in range(warmup):
        torch.matmul(a, b)
    sync(dev)
    t0 = time.perf_counter()
    for _ in range(iters):
        torch.matmul(a, b)
    sync(dev)
    return (time.perf_counter() - t0) / iters * 1000
```

- Report TFLOPS = `2 * m * n * k / (ms/1000) / 1e12`.
- Test fp32, fp16, and bf16. If bf16 or fp16 is not much faster than fp32,
  the fast path is not engaged (wrong kernel, wrong dtype, or no tensor cores).
- On static-shape backends, the first call compiles; time it separately.

**Interpretation pitfalls:**

- A single size can hit a tuned kernel; test at least two sizes.
- Tiny matrices measure launch overhead, not throughput.
- Report cold and warm numbers separately.

## 6. Numerics

Backends differ in accumulation precision, NaN/Inf rules, and conversion
behaviour. Probe these before trusting a port's output.

- **Accumulation precision:** sum a long vector in fp16/bf16 and compare to an
  fp64 reference; report relative error.
- **Associativity:** `(a + b) + c` vs `a + (b + c)`; non-associative
  accumulation changes results across backends.
- **NaN/Inf propagation:** `0 * inf`, `inf - inf`, `nan == nan`, and whether
  uninitialised memory is NaN (TPU) or zero (CPU/CUDA).
- **Dtype conversion:** bf16 → NumPy (NumPy has no bf16, so cast to float
  first); fp16 matmul output dtype; autocast behaviour.
- **Reductions:** `torch.std_mean`, `correction=` argument availability;
  `std_mean` is missing on MPS and TPU in some versions.
- **Determinism:** same seed, same input, same output across runs.

A failing numeric probe is often the root cause of "plausible but wrong" output.

## 7. Kernel dispatch

Prove the intended kernel ran; do not infer it from code.

| Backend | How to confirm |
| --- | --- |
| Intel AMX / oneDNN | `ONEDNN_VERBOSE=1`, `processwatch` |
| AMD ROCm | `rocminfo`, PyTorch device properties, TFLOPS vs published |
| Google TPU | PJRT logs, compile time, SDPA selected |
| Apple MPS | `PYTORCH_ENABLE_MPS_FALLBACK` logs, op coverage |
| Qualcomm QNN | provider registration log, effective TOPS vs peak |

If a kernel did not dispatch, the FLOPS probe will show it: throughput far
below the published peak means a fallback path is in use.

## 8. How to use the results

- Choose the backend whose real FLOPS and bandwidth meet the app's needs.
- Set the default resolution/batch/precision from the allocatable memory, not
  the reported VRAM.
- When a port is slow, re-run the probe and compare against the baseline: a
  drop in TFLOPS points at kernel selection, not the model.
- When output is wrong, run the numerics probe before debugging the sampler.

## Probe checklist

- [ ] Record device, driver, Python, torch, and accelerator-stack versions.
- [ ] Report both reported and allocatable memory.
- [ ] Report memory bandwidth at the target dtype.
- [ ] Report FLOPS for fp32, fp16, and bf16 at two sizes.
- [ ] Report cold and warm numbers separately.
- [ ] Run the numerics micro-tests and record any deviations.
- [ ] Confirm kernel dispatch with the backend's verbose/profiler tool.
- [ ] Save the probe command and output in the port write-up.

For the full probe implementation, read
[probe.py](references/probe.py).

See also `porting-bringup` for baseline and backend selection, and
`porting-performance` for tuning after the port works.