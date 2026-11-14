"""Minimal hardware capability probe.

Run:  python probe.py
Optional env:  PROBE_DEV=cpu|cuda|mps|tpu   PROBE_SIZES=2048,4096   PROBE_ITERS=5

Reports device identity, reported vs allocatable memory, bandwidth, FLOPS for
fp32/fp16/bf16, and a few numerics checks. Results depend on dtype, shape,
kernel selection and allocator settings; record the command and output.
"""
import os, time, math

import torch

DEV_SPEC = os.environ.get("PROBE_DEV", "auto")
SIZES = [int(x) for x in os.environ.get("PROBE_SIZES", "1024,4096").split(",")]
ITERS = int(os.environ.get("PROBE_ITERS", "5"))
WARMUP = 2


def pick_device():
    if DEV_SPEC != "auto":
        return torch.device(DEV_SPEC)
    if torch.cuda.is_available():
        return torch.device("cuda")
    if getattr(torch.backends, "mps", None) and torch.backends.mps.is_available():
        return torch.device("mps")
    if hasattr(torch, "accelerator") and torch.accelerator.is_available():
        acc = torch.accelerator.current_accelerator()
        if acc is not None and acc.type == "tpu":
            return torch.device("tpu")
    return torch.device("cpu")


def sync(dev):
    if dev.type == "cuda":
        torch.cuda.synchronize()
    elif dev.type == "mps":
        torch.mps.synchronize()
    elif dev.type == "tpu":
        torch.accelerator.synchronize() if hasattr(torch.accelerator, "synchronize") else None


def section(t):
    print("\n" + "=" * 20, t, "=" * 20)


def device_info(dev):
    section("DEVICE")
    print("torch:", torch.__version__)
    print("device:", dev)
    if dev.type == "cuda":
        p = torch.cuda.get_device_properties(dev)
        print("name:", p.name, "cc:", p.major, ".", p.minor)
        print("reported total MiB:", p.total_memory // (1024 * 1024))
        print("multi_processor_count:", p.multi_processor_count)
    elif dev.type == "mps":
        print("mps available:", torch.backends.mps.is_available())
    elif dev.type == "tpu":
        print("accelerator:", torch.accelerator.current_accelerator())
    else:
        print("cpu threads:", torch.get_num_threads())
        try:
            import platform
            print("machine:", platform.machine(), platform.processor())
        except Exception:
            pass
    print("allocator config:")
    for k in ("PYTORCH_HIP_ALLOC_CONF", "PYTORCH_CUDA_ALLOC_CONF",
              "PYTORCH_MPS_HIGH_WATERMARK_RATIO", "OMP_NUM_THREADS",
              "OMP_PROC_BIND", "OMP_PLACES"):
        v = os.environ.get(k)
        if v is not None:
            print("  ", k, "=", v)


def reported_memory(dev):
    section("MEMORY (reported)")
    if dev.type == "cuda":
        free, total = torch.cuda.mem_get_info(dev)
        print("reported free MiB:", free // (1024 * 1024))
        print("reported total MiB:", total // (1024 * 1024))
    elif dev.type == "tpu":
        try:
            free = torch.accelerator.memory.memory_reserved(dev)  # best effort
        except Exception:
            free = None
        print("reported (best effort) MiB:", free)
    else:
        try:
            import psutil
            vm = psutil.virtual_memory()
            print("system total GiB:", round(vm.total / 1024 ** 3, 2))
            print("system available GiB:", round(vm.available / 1024 ** 3, 2))
        except Exception:
            print("psutil not available; skipping system memory report")


MAX_ALLOC_GIB = float(os.environ.get("PROBE_MAX_ALLOC_GIB", "8"))

def allocatable_memory(dev, dtype):
    # Cap the probe so it cannot fill all of RAM/swap on large machines.
    elems_per_mb = (1024 * 1024) // torch.tensor([], dtype=dtype).element_size()
    cap_bytes = int(MAX_ALLOC_GIB * (1024 ** 3))
    blobs, total = [], 0
    try:
        while total + elems_per_mb * torch.tensor([], dtype=dtype).element_size() <= cap_bytes:
            b = torch.empty(elems_per_mb, device=dev, dtype=dtype)
            blobs.append(b)
            total += b.numel() * b.element_size()
    except (torch.OutOfMemoryError, RuntimeError, Exception):
        pass
    del blobs
    if dev.type == "cuda":
        torch.cuda.empty_cache()
    return total / (1024 ** 3)


def memory_probe(dev):
    section("MEMORY (allocatable)")
    for dtype in (torch.float16, torch.bfloat16, torch.float32):
        try:
            gib = allocatable_memory(dev, dtype)
            print(f"  {str(dtype):>14}: {gib:.2f} GiB allocatable")
        except Exception as e:
            print(f"  {str(dtype):>14}: error {e}")


def bandwidth(dev, n=64 * 1024 * 1024, iters=5):
    section("BANDWIDTH")
    for dtype in (torch.float16, torch.float32):
        try:
            a = torch.empty(n, device=dev, dtype=dtype)
            b = torch.empty_like(a)
            a.random_()
            for _ in range(WARMUP):
                b.copy_(a)
            sync(dev)
            t0 = time.perf_counter()
            for _ in range(iters):
                b.copy_(a)
            sync(dev)
            dt = time.perf_counter() - t0
            gb_s = a.numel() * a.element_size() * iters / dt / 1e9
            print(f"  copy {str(dtype):>13}: {gb_s:6.1f} GB/s  (n={n})")
        except Exception as e:
            print(f"  {str(dtype):>13}: error {e}")


def matmul_ms(m, n, k, dtype, dev):
    a = torch.randn(m, k, device=dev, dtype=dtype)
    b = torch.randn(k, n, device=dev, dtype=dtype)
    for _ in range(WARMUP):
        torch.matmul(a, b)
    sync(dev)
    t0 = time.perf_counter()
    for _ in range(ITERS):
        torch.matmul(a, b)
    sync(dev)
    return (time.perf_counter() - t0) / ITERS * 1000.0


def flops_probe(dev):
    section("FLOPS (matmul)")
    for dtype in (torch.float32, torch.float16, torch.bfloat16):
        for size in SIZES:
            try:
                ms = matmul_ms(size, size, size, dtype, dev)
                tflops = 2 * size * size * size / (ms / 1000.0) / 1e12
                print(f"  {str(dtype):>13}  {size}^3 : {ms:7.2f} ms  -> {tflops:6.2f} TFLOPS")
            except Exception as e:
                print(f"  {str(dtype):>13}  {size}^3 : error {e}")


def numerics_probe(dev):
    section("NUMERICS")
    # accumulation precision
    try:
        n = 1 << 20
        x = torch.ones(n, device=dev, dtype=torch.float16)
        s16 = x.sum().item()
        x32 = torch.ones(n, device=dev, dtype=torch.float32)
        s32 = x32.sum().item()
        print(f"  sum of {n} ones: fp16={s16:.3f}  fp32={s32:.3f}  (exact {n})")
    except Exception as e:
        print("  sum test error:", e)
    # NaN / inf rules
    try:
        inf = torch.tensor(float("inf"), device=dev)
        nan = torch.tensor(float("nan"), device=dev)
        print("  0 * inf =", (torch.tensor(0.0, device=dev) * inf).item())
        print("  inf - inf =", (inf - inf).item())
        print("  nan == nan =", bool((nan == nan).item()))
    except Exception as e:
        print("  nan/inf test error:", e)
    # uninitialised memory
    try:
        b = torch.empty(1024, device=dev, dtype=torch.float32)
        finite = torch.isfinite(b).all().item()
        print("  empty(1024) all finite:", finite, "(False suggests NaN/inf garbage)")
    except Exception as e:
        print("  uninit test error:", e)
    # dtype conversion round trip
    try:
        v = torch.tensor(1.234567, device=dev, dtype=torch.bfloat16)
        print("  bf16 round trip:", v.item(), "-> float:", v.float().item())
    except Exception as e:
        print("  dtype conversion error:", e)
    # std_mean availability
    try:
        t = torch.randn(1024, device=dev, dtype=torch.float32)
        m, s = torch.std_mean(t)
        print("  std_mean: ok (mean=%.4f std=%.4f)" % (m.item(), s.item()))
    except Exception as e:
        print("  std_mean: UNAVAILABLE -", e)


def main():
    dev = pick_device()
    print("probe device:", dev)
    device_info(dev)
    reported_memory(dev)
    memory_probe(dev)
    bandwidth(dev)
    flops_probe(dev)
    numerics_probe(dev)
    section("DONE")
    print("record torch, device, driver and allocator settings with these numbers.")


if __name__ == "__main__":
    main()
