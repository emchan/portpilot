# Fooocus on an AMD Radeon 780M iGPU (gfx1103) under WSL2

Date: 2026-11-12
Repo: `lllyasviel/Fooocus` @ `ae05379` (Fooocus 2.5.5)
Host: WSL2 Ubuntu 24.04 on a Ryzen 7 7840HS / Radeon 780M
Status: **UI verified on the ROCm/PyTorch stack; image generation not benchmarked
in this write-up.**

**Scope:** 247 new lines across 6 files (+247/−0); no tracked Fooocus source was
modified. **Difficulty:** medium — the work was ROCm/WSL environment setup and a
`gfx1103` → `gfx1100` compatibility shim, not application code.

**Architecture map:** [`architecture.html#port=amd`](../architecture/architecture.html#port=amd) highlights where this port hooks into the upstream flow.

This document records the exact steps that were run, every bug that was hit,
and how each one was resolved. The result is a working ROCm/PyTorch stack that
runs Fooocus's web UI on the iGPU, plus a set of small helper files that are
captured in `fooocus-rocm.diff`.

---

## 1. Result summary

| Item | Result |
|---|---|
| Acceleration path | ROCm 7.2.4 + PyTorch 2.14.1 ROCm wheels |
| Device seen by PyTorch | `AMD Radeon 780M Graphics` (`gfx1103`, RDNA3) |
| `torch.cuda.is_available()` | `True` |
| fp16 matmul (4096³) | **33.1–33.8 ms → ~4.1 TFLOPS** (run-to-run) |
| SDPA fp16 (4096 tokens) | **5.1–6.2 ms** (run-to-run) |
| MIOpen Conv2d (320×64×64) | ~1.78 ms |
| Fooocus UI | Starts, serves HTTP 200, share link works |
| Image generation | Default 6.7 GB SDXL checkpoint downloaded; benchmark image not run during bring-up |

The UI is fully usable for browsing and queueing. Preset download is enabled by
default, so the first `./run-rocm.sh` fetches the ~6.6 GB default SDXL
checkpoint before starting the UI. Without a checkpoint (for example when
launched with `--disable-preset-download`), the worker thread logs
`ValueError: No such file or directory: .../juggernautXL_v8Rundiffusion.safetensors`
and the UI still serves normally.

---

## 2. Options considered

The 780M is `gfx1103`. WSL2 exposes it through `/dev/dxg` (not `/dev/kfd` or
`/dev/dri`), and AMD's ROCm 7.x WSL path uses the Windows driver. The options,
ranked:

1. **ROCm + PyTorch ROCm wheels inside WSL2 — recommended.** The only option
   that is both GPU-accelerated and runs Fooocus unmodified. It uses the
   `/dev/dxg` passthrough and keeps the same Linux workflow.
   *Caveats:* `gfx1103` is not an officially supported PyTorch/ROCm target, so
   it needs `HSA_OVERRIDE_GFX_VERSION=11.0.0`; WSL's RAM cap and the 4 GB UMA
   carve-out are the real limits.
   *Wheel used:* `torch==2.14.1+rocm7.2`, `torchvision==0.29.1+rocm7.2`
   (`https://download.pytorch.org/whl/rocm7.2`, Python 3.12). Older
   `rocm7.0`/`7.1` wheels (torch 2.10/2.11) are also available if 2.14
   misbehaves.
2. **DirectML via `torch-directml` — fallback.** Officially supports WSL2 and
   works on any DX12 GPU, including the 780M; Fooocus has a built-in
   `--directml` flag. It is pinned to `torch==2.4.1` / `torchvision==0.19.1`,
   has been in maintenance since 2024, and Fooocus's DirectML path forces fp32
   and disables low-VRAM handling, so SDXL will be slow and may OOM. See
   [Fallbacks](#10-fallbacks).
3. **Native Windows ROCm — not applicable.** ROCm-on-Windows only targets
   selected RX 7000/9000 discrete cards; the 780M iGPU is not supported.
4. **ZLUDA on Windows — not recommended.** CUDA-to-HIP translation works for
   some apps, but it is version-sensitive, Windows-only, and there is no
   maintained Fooocus-ZLUDA path.
5. **Vulkan / `stable-diffusion.cpp` — different application.** It can use the
   780M without ROCm, but it is not Fooocus: no Fooocus UI, presets, refiner, or
   inpaint pipeline.
6. **CPU only — last resort.** `--always-cpu` runs, but SDXL on this 16-thread
   CPU is on the order of tens of seconds per step.

---

## 3. Environment

| Item | Value |
|---|---|
| WSL | Ubuntu 24.04, kernel `6.18.33.2-microsoft-standard-WSL2` |
| CPU/APU | AMD Ryzen 7 7840HS w/ Radeon 780M |
| GPU | `gfx1103`, RDNA3, 12 CUs / 6 WGPs, 2.70 GHz |
| Host RAM | 16.97 GB |
| RAM visible to WSL | 7.7 GB (default WSL cap) |
| Windows GPU driver | `32.0.31041.5005` |
| GPU memory reported by Windows | 4 GB `AdapterRAM` (UMA carve-out) |
| GPU memory reported inside WSL | 25.57 GB (shared; **not** a real budget) |
| ROCm | 7.2.4 (`/opt/rocm`), `hipcc`, hipBLAS, rocBLAS present |
| ROCDXG | `rocdxg-roct` 1.2.2 (WSL user-space runtime) |
| Python | 3.12.3 in `.venv` |
| PyTorch | `2.14.1+rocm7.2` (HIP 7.2.53211) |
| torchvision | `0.29.1+rocm7.2` |
| Device nodes | no `/dev/kfd`, no `/dev/dri`, **`/dev/dxg` present** |

`rocminfo` prints `WSL environment detected.` and finds:

```
Name:                    gfx1103
Marketing Name:          AMD Radeon 780M Graphics
Compute Unit:            12
```

PyTorch's `get_device_properties(0).multi_processor_count` reports `6` because
it counts WGPs rather than CUs. That is expected.

---

## 4. Verified on this machine

* A raw HIP kernel compiled with `hipcc --offload-arch=gfx1103` runs successfully.
* A hipBLAS SGEMM runs successfully, **but only with**
  `HSA_OVERRIDE_GFX_VERSION=11.0.0` (or `11.0.2`). Without the override rocBLAS
  aborts: ROCm 7.2's system rocBLAS ships Tensile kernels for `gfx1100`,
  `gfx1102`, `gfx1030`, `gfx90a`, `gfx942`, `gfx1151`, `gfx1201`, and others,
  but **not `gfx1103`**. The override makes the 780M use `gfx1100` kernels. (The
  wheel's hipBLASLt does ship 53 `gfx1103` kernels, but the rocBLAS path is
  still hit and fails.)
* `hipDeviceProp_t` reports 6 CUs (WGP view) and 25.57 GB global memory;
  `rocminfo` reports the expected 12 CUs. The 25.57 GB is shared host memory, so
  it must not be treated as VRAM.
* **PyTorch 2.14.1+rocm7.2 works**: `torch.cuda.is_available() == True`, the
  device is `AMD Radeon 780M Graphics`, and the arch list contains `gfx1103`.
  Benchmarks are in [section 1](#1-result-summary).
* The ops SDXL needs all execute correctly on `gfx1103` (fp16): MIOpen `Conv2d`
  320×64×64, `GroupNorm`, `LayerNorm`, `SiLU`, `interpolate`, `Linear`, and
  SDPA. AOTriton ships `amd-gfx110x` flash-attention images.
* **The Fooocus UI starts** on this stack. With `--disable-preset-download` it
  prints `Total VRAM 24388 MB, total RAM 7842 MB`, `Using pytorch cross
  attention`, and serves **HTTP 200**. Without a checkpoint, generation fails
  with `No such file .../juggernautXL_v8Rundiffusion.safetensors`, as expected.
* Two WSL-specific fixes are mandatory: `ROCPROFILER_REGISTER_ENABLED=0` and
  leaving `PYTORCH_HIP_ALLOC_CONF=expandable_segments:True` unset. See
  [Bugs 3 and 4](#7-bugs-encountered-and-resolutions).

---

## 5. Expected performance

**These are public reference points, not measurements from this machine.** The
bring-up stopped at a serving UI, so no image was generated here.

Public 780M numbers (Windows 11, 64 GB RAM, SDXL int8, 1024×1536, cfg 4) are
around **3.3 s/it** baseline and **2.9 s/it** with iGPU-tuned kernels. At
1024×1024 fp16, expect roughly **2–4 s/it**, or **~1–2.5 minutes for a 30-step
image**, plus model load. SD1.5 at 512×512 is far faster.

The 7.7 GB WSL RAM cap and low-VRAM offloading will push this toward the slower
end until WSL memory is raised.

---

## 6. Exact setup steps

### 6.0 Get the source

The manual equivalent of the bootstrap script (section 9) is:

```bash
git clone --depth 1 https://github.com/lllyasviel/Fooocus.git /tmp/opencode/Fooocus
cp -a /tmp/opencode/Fooocus/. /home/<you>/opencode/fooocus/
cd /home/<you>/opencode/fooocus
git log --oneline -1    # ae05379 ci: bump actions/checkout from 4 to 5 (#4085)
```

The investigation used commit `ae05379` (version 2.5.5). The release tag
`v2.5.5` (`8da1d3f`) is the default for `setup-fooocus-amd.sh`; the diff only
adds new files, so it applies to either ref.

### 6.1 Add the ROCm 7.2.4 repository and install the HIP SDK

The Ubuntu 24.04 `hipcc` packages are ROCm 5.7 and do not support `gfx1103`
properly, so they were removed and the AMD repository was used instead.

```bash
# Remove the distro ROCm 5.7 HIP stack first (if present).
sudo apt-get purge -y hipcc libamd-comgr-dev libamd-comgr2:amd64 libamdhip64-5 \
  libamdhip64-dev libhiprtc-builtins5 libhsa-runtime-dev libhsa-runtime64-1 \
  libhsakmt1:amd64 librocm-smi64-1 rocm-cmake rocm-device-libs-17 rocm-smi rocminfo

sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://repo.radeon.com/rocm/rocm.gpg.key \
  | sudo gpg --dearmor -o /etc/apt/keyrings/rocm.gpg

echo 'deb [arch=amd64 signed-by=/etc/apt/keyrings/rocm.gpg] https://repo.radeon.com/rocm/apt/7.2.4 noble main' \
  | sudo tee /etc/apt/sources.list.d/rocm.list

sudo apt update
sudo apt-get install -y rocm-hip-sdk rocminfo rocm-smi-lib

# ROCDXG is the WSL user-space runtime, distributed separately from the ROCm
# apt repo. Point this at the rocdxg-roct .deb you obtained for your WSL setup.
sudo dpkg -i /tmp/opencode/rocdxg-roct_1.2.2_amd64.deb
```

Verify:

```bash
rocminfo | grep -E 'WSL environment|Name:|Marketing Name:|Compute Unit:'
ls -l /dev/dxg /dev/kfd /dev/dri 2>&1
```

The second command confirms `/dev/dxg` exists while `/dev/kfd` and `/dev/dri`
do not.

### 6.2 Create the Python environment with `uv`

```bash
cd /home/<you>/opencode/fooocus

# uv was installed with:
#   curl -LsSf https://astral.sh/uv/install.sh | sh
~/.local/bin/uv venv --python 3.12 .venv

# The ROCm wheel index shadows PyPI for some packages (notably tqdm),
# so uv needs unsafe-best-match to resolve correctly.
~/.local/bin/uv pip install \
  --index-strategy unsafe-best-match \
  --index-url https://download.pytorch.org/whl/rocm7.2 \
  -r constraints-rocm.txt

~/.local/bin/uv pip install \
  --index-strategy unsafe-best-match \
  -r requirements_versions.txt
```

`constraints-rocm.txt` pins the ROCm build of torch/torchvision:

```
torch==2.14.1
torchvision==0.29.1
```

`uv` initially resolved these to `2.14.1+rocm7.2` / `0.29.1+rocm7.2`
(a 5.8 GiB torch download). Key installed versions:

```
torch            2.14.1+rocm7.2
torchvision      0.29.1+rocm7.2
gradio           3.41.2
pydantic         1.10.13
fastapi          0.99.1
starlette        0.27.0
uvicorn          0.23.2
httpx            0.27.0
python-multipart 0.0.6
numpy            1.26.4
safetensors      0.4.3
transformers     4.42.4
accelerate       0.32.1
```

`launch.py` calls `python -m pip` when it thinks requirements are missing, and
a `uv` venv has no `pip`, so install it once:

```bash
~/.local/bin/uv pip install pip
```

### 6.3 Pin the 2023-era Gradio web stack

Fooocus pins `gradio==3.41.2`, which is from 2023. A fresh 2026 install pulls
`pydantic 2.x`, `fastapi 0.162.x`, and `starlette 1.x`, which break Gradio.
Install the known-good set:

```bash
~/.local/bin/uv pip install -r requirements-web-pins.txt
```

`requirements-web-pins.txt`:

```
pydantic==1.10.13
fastapi==0.99.1
starlette==0.27.0
uvicorn==0.23.2
httpx==0.27.0
python-multipart==0.0.6
```

### 6.4 Verify the GPU

```bash
cd /home/<you>/opencode/fooocus
./test-rocm.sh
```

`test-rocm.sh` sets the required environment and runs `test-rocm.py`:

```bash
#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
export HSA_OVERRIDE_GFX_VERSION="${HSA_OVERRIDE_GFX_VERSION:-11.0.0}"
export ROCPROFILER_REGISTER_ENABLED=0
export HIP_VISIBLE_DEVICES="${HIP_VISIBLE_DEVICES:-0}"
exec .venv/bin/python test-rocm.py
```

Actual output:

```
torch: 2.14.1+rocm7.2
hip: 7.2.53211 | cuda: None
cuda available: True
device: AMD Radeon 780M Graphics
arch list: ['gfx900', 'gfx906', 'gfx908', 'gfx90a', 'gfx942', 'gfx950', 'gfx1030', 'gfx1100', 'gfx1101', 'gfx1102', 'gfx1103', 'gfx1200', 'gfx1201', 'gfx1150', 'gfx1151']
total_memory: 25.57 GB | CUs: 6 | cc: 11.0
bf16 supported: True
mem_get_info: free 24.92 GB / total 25.57 GB
fp16 4096^3 matmul: 33.1 ms -> 4.15 TFLOPS
SDPA fp16 4096 tokens: 5.1 ms
```

### 6.5 Launch Fooocus

```bash
cd /home/<you>/opencode/fooocus
./run-rocm.sh
```

`run-rocm.sh` exports the required variables and launches with
`--attention-pytorch --vae-in-fp16 --always-low-vram --disable-xformers
--disable-in-browser --share`. Preset download is on by default.

The server was started with:

```bash
GRADIO_SERVER_PORT=7865 ./run-rocm.sh
```

On the first run this fetches the default checkpoint before the UI appears:

```
Downloading: "https://huggingface.co/lllyasviel/fav_models/resolve/main/fav/juggernautXL_v8Rundiffusion.safetensors" to /home/<you>/opencode/fooocus/models/checkpoints/juggernautXL_v8Rundiffusion.safetensors
```

Observed startup after the 6.7 GB download:

```
Total VRAM 24388 MB, total RAM 7842 MB
Set vram state to: LOW_VRAM
Always offload VRAM
Device: cuda:0 AMD Radeon 780M Graphics : native
VAE dtype: torch.float16
Using pytorch cross attention
Running on local URL:  http://127.0.0.1:7865
Running on public URL: https://<random>.gradio.live
```

The public URL is created by Gradio's `frpc` tunnel and expires after 72 hours.
`--share` requires outbound access to `*.gradio.live` and the Gradio API server.

To run without downloading the 6.6 GB default checkpoint:

```bash
./run-rocm.sh --disable-preset-download
```

Why each flag and environment variable:

| Flag / env | Why |
|---|---|
| `HSA_OVERRIDE_GFX_VERSION=11.0.0` | **Required.** No `gfx1103` rocBLAS kernels in ROCm 7.2. |
| `--attention-pytorch` | Fooocus only enables PyTorch SDPA automatically for NVIDIA/Intel. Without this it falls back to slow sub-quadratic attention. |
| `--vae-in-fp16` | Default VAE dtype on ROCm is fp32; fp16 saves memory/time on RDNA3. Use `--vae-in-bf16` if you see NaNs. |
| `--always-low-vram` | Fooocus sees 25.6 GB "VRAM" but WSL only has 7.7 GB RAM. Low-VRAM keeps the model on CPU and streams it. Drop this after raising WSL memory. |
| `--disable-xformers` | xformers is not installed for ROCm; this avoids probing for it. |
| `ROCPROFILER_REGISTER_ENABLED=0` | **Required.** Prevents the bundled rocprofiler-sdk from aborting on WSL/DXG. |
| `MIOPEN_FIND_MODE=FAST` | Skips exhaustive MIOpen conv search; first-run kernel discovery is faster. |
| *(do not set)* `PYTORCH_HIP_ALLOC_CONF=expandable_segments:True` | Breaks allocations on WSL/DXG (`hipErrorInvalidValue`). Leave the allocator default. |

---

## 7. Bugs encountered and resolutions

### Bug 1 — Ubuntu's `hipcc` is ROCm 5.7 and does not handle `gfx1103`

**Symptom:** HIP binaries built against the distro packages failed or produced
no kernels for `gfx1103`.

**Cause:** Ubuntu 24.04 ships ROCm 5.7-era `hipcc`, `libamdhip64`, and
`rocminfo`. RDNA3 (`gfx1103`) support in that stack is incomplete.

**Resolution:** Purge the distro HIP packages and install ROCm 7.2.4 from
`repo.radeon.com` (`rocm-hip-sdk`, `rocminfo`, `rocm-smi-lib`). Confirm with
`rocminfo` that `gfx1103` is listed.

### Bug 2 — rocBLAS has no Tensile kernels for `gfx1103`

**Symptom:** hipBLAS calls fail with a missing-kernel/Tensile-library error
(`Cannot read TensileLibrary.dat ... gfx1103`) or fall back to an unusable path.

**Cause:** ROCm 7.2.4's rocBLAS package ships Tensile kernels for `gfx1100`
(RX 7900 / Navi 31) but not for the 780M's `gfx1103`.

**Resolution:** Pretend to be `gfx1100`:

```bash
export HSA_OVERRIDE_GFX_VERSION=11.0.0
```

`11.0.0` and `11.0.2` both work. This is set in `run-rocm.sh` and
`test-rocm.sh`. It is the single most important workaround in this setup.

### Bug 3 — rocprofiler aborts on WSL2/DXG

**Symptom:** Python dies with SIGABRT during `torch.cuda.device_count()`:

```
F ... agent.cpp:1093] Found 0 rocprofiler agents and 2 HSA agents.
HSA agents contained 2 internal node ids not found by rocprofiler: 0, 1
...
timeout: the monitored command dumped core
```

**Cause:** `rocprofiler-register` expects `/sys/class/kfd/...`, which does not
exist in WSL2 because the `amdgpu` kernel module is not loaded. `/dev/dxg` is
the WSL transport.

**Resolution:** Disable profiler registration for normal inference:

```bash
export ROCPROFILER_REGISTER_ENABLED=0
```

Profiling is not needed to run Fooocus.

### Bug 4 — `expandable_segments` breaks WSL/DXG allocations

**Symptom:** `hipErrorInvalidValue` when `PYTORCH_HIP_ALLOC_CONF` contains
`expandable_segments:True`.

**Cause:** The WSL/DXG backend does not support the VMM path PyTorch uses for
expandable segments.

**Resolution:** Do **not** set `expandable_segments:True`. Leave
`PYTORCH_HIP_ALLOC_CONF` unset. This is called out in `run-rocm.sh`.

### Bug 5 — `uv` resolves an incorrect `tqdm`

**Symptom:** Dependency resolution failed or picked an incompatible `tqdm`
when the ROCm wheel index was used.

**Cause:** The ROCm index also publishes packages that exist on PyPI, so it can
shadow the real PyPI version.

**Resolution:** Always pass `--index-strategy unsafe-best-match` to `uv pip
install` when the ROCm index is in play.

### Bug 6 — Gradio 3.41.2 + 2026 FastAPI/Pydantic

**Symptom:** The UI fails at startup with:

```
TypeError: unhashable type: 'dict'
```

and a failed localhost health check. The initially installed versions were
`fastapi 0.162.5`, `pydantic 2.14.3`, `starlette 1.10.0`, `uvicorn 0.54.0`.

**Cause:** Gradio 3.41.2 was written for Pydantic 1.x and FastAPI 0.99-era
Starlette.

**Resolution:** Install `requirements-web-pins.txt` (Pydantic 1.10.13, FastAPI
0.99.1, Starlette 0.27.0, Uvicorn 0.23.2, httpx 0.27.0, python-multipart
0.0.6). After this the UI starts and returns HTTP 200.

### Bug 7 — `rocm-smi` does not work in WSL

**Symptom:** `rocm-smi` reports that the `amdgpu` module is not loaded.

**Cause:** WSL uses the Windows driver via `/dev/dxg`; the Linux `amdgpu`
module is not present.

**Resolution:** Use `rocminfo` or PyTorch for device queries. `rocm-smi` is not
usable here and is not required.

### Bug 8 — WSL reports 25.57 GB VRAM but only has 7.7 GB RAM

**Symptom:** Fooocus sees `Total VRAM 24388 MB` while WSL has only ~7.7 GB of
RAM. Loading an SDXL checkpoint can exhaust memory or trigger heavy swapping.

**Cause:** The Windows driver reports the shared GPU memory aperture. It is not
a real budget in this VM.

**Resolution:** Run with `--always-low-vram` (already in `run-rocm.sh`). To get
more headroom, raise the WSL memory cap in `C:\Users\<you>\.wslconfig`:

```ini
[wsl2]
memory=12GB
swap=16GB
```

Then run `wsl --shutdown` from Windows and reopen the shell. Remove
`--always-low-vram` only after confirming the new limit.

### Bug 9 — missing checkpoint

**Symptom:** With `--disable-preset-download`, the worker thread logs:

```
ValueError: No such file or directory:
  /home/<you>/opencode/fooocus/models/checkpoints/juggernautXL_v8Rundiffusion.safetensors
```

The UI still serves HTTP 200; only generation is unavailable.

**Resolution:** Preset download is on by default, so a normal `./run-rocm.sh`
fetches the default checkpoint. To skip it, pass `--disable-preset-download`.
Alternatively, place an SDXL checkpoint in `models/checkpoints/` and select it
in the UI.

### Bug 10 — `python -m pip` is missing in the `uv` venv

**Symptom:** `launch.py` tries to install a missing requirement and fails with
`No module named pip`.

**Cause:** `uv venv` creates a virtual environment without `pip` by default,
but Fooocus's `launch.py` shells out to `python -m pip`.

**Resolution:** Install `pip` into the environment once:

```bash
~/.local/bin/uv pip install pip
```

---

## 8. Files added

These are the only changes relative to upstream `ae05379`; no tracked Fooocus
source files were modified.

| File | Purpose |
|---|---|
| [`setup-fooocus-amd.sh`](setup-fooocus-amd.sh) | One-command clone + patch + install + share-mode launch |
| `run-rocm.sh` | Launcher with all required env vars, `--share`, and low-VRAM flags |
| `test-rocm.sh` | Wrapper that sets the ROCm env and runs the self-test |
| `test-rocm.py` | Device, memory, matmul, and SDPA benchmark |
| `constraints-rocm.txt` | Pins `torch==2.14.1`, `torchvision==0.29.1` |
| `requirements-web-pins.txt` | Pins the Gradio-3.41.2-compatible web stack |

[`fooocus-rocm.diff`](fooocus-rocm.diff) contains the unified diff of all six
files. Only the bootstrap script is checked in next to this README; `git apply`
the diff (or run the bootstrap script) to create the rest. The former
`AMD_IGPU_OPTIONS.md` exploration notes have been merged into this document.

---

## 9. Quick start

### One command from a clean checkout

With ROCm 7.2.4 and `uv` installed:

```bash
cd /home/<you>/opencode/fooocus
./setup-fooocus-amd.sh
```

The script:

1. clones `https://github.com/lllyasviel/Fooocus.git` into `./fooocus-amd`
2. checks out `v2.5.5` (override with `--ref ae05379` or `FOOOCUS_REF=...`)
3. applies `fooocus-rocm.diff` (idempotent)
4. creates `.venv` and installs the ROCm torch + Fooocus + web pins
5. runs `./run-rocm.sh`, which starts the WebUI with `--share`

Useful options:

```bash
./setup-fooocus-amd.sh --dir /path/to/fooocus-amd --ref v2.5.5
./setup-fooocus-amd.sh --no-install --no-start   # clone + patch only
./setup-fooocus-amd.sh -- --disable-preset-download
```

### Manual start in the existing checkout

```bash
cd /home/<you>/opencode/fooocus

# one-time environment check
./test-rocm.sh

# start the UI (local + public gradio.live link)
./run-rocm.sh

# start without downloading the default 6.6 GB checkpoint
./run-rocm.sh --disable-preset-download
```

Required environment (already handled by both scripts):

```bash
export HSA_OVERRIDE_GFX_VERSION=11.0.0
export ROCPROFILER_REGISTER_ENABLED=0
export HIP_VISIBLE_DEVICES=0
```

Do not set `PYTORCH_HIP_ALLOC_CONF=expandable_segments:True`.

---

## 10. Fallbacks

### DirectML

If ROCm turns out to be unstable, a DirectML venv is a small, official
alternative:

```bash
~/.local/bin/uv venv .venv-dml --python 3.12
~/.local/bin/uv pip install --python .venv-dml/bin/python \
  torch==2.4.1 torchvision==0.19.1 --index-url https://download.pytorch.org/whl/cpu
# torch-directml pins torch 2.4.1 / torchvision 0.19.1, so install it next
~/.local/bin/uv pip install --python .venv-dml/bin/python torch-directml pip
# Fooocus's Python deps are the same as the ROCm venv. Do not apply
# constraints-rocm.txt here: it pins the ROCm torch build, not torch-directml's.
~/.local/bin/uv pip install --python .venv-dml/bin/python \
  -r requirements_versions.txt --index-strategy unsafe-best-match
~/.local/bin/uv pip install --python .venv-dml/bin/python -r requirements-web-pins.txt
# then launch with: .venv-dml/bin/python launch.py --directml
```

Expect fp32 and no low-VRAM management on that path, so SDXL is likely to OOM on
the 4 GB UMA carve-out. Treat it as a diagnostic/fallback, not the primary setup.

### CPU

```bash
.venv/bin/python launch.py --always-cpu
```

---

## 11. Caveats

* `HSA_OVERRIDE_GFX_VERSION=11.0.0` is a compatibility shim. It works, but it is
  not an officially validated configuration. Kernel updates can change behavior.
* The `gfx1103` device is not in AMD's official ROCm support matrix; this is a
  best-effort setup.
* The Gradio share link is a temporary tunnel, not a production deployment. Do
  not expose it without authentication (`--auth`).
* The 780M shares system RAM. Generation speed depends heavily on the WSL memory
  cap and on swap; 7.7 GB is tight for SDXL. Raise it in
  `C:\Users\<you>\.wslconfig` (`memory=12GB`, `swap=16GB`), then run
  `wsl --shutdown` from Windows and reopen the shell. Remove
  `--always-low-vram` only after confirming the new limit.
* Windows reports a 4 GB `AdapterRAM` UMA carve-out. If the BIOS exposes a "UMA
  Frame Buffer Size" setting, 8 GB may help, but it takes RAM away from an
  already RAM-limited 16 GB machine.
* The first normal launch downloads about 7 GB (JuggernautXL plus VAE/expansion
  files) into `models/`. This is a one-time wait.
* Fooocus defaults SDXL to fp16 and, on ROCm, VAE to fp32. Keep
  `--vae-in-fp16` (or use `--vae-in-bf16`); do not use `--all-in-fp32`.
* Do not use `--always-normal-vram` or `--always-high-vram` with the 7.7 GB WSL
  limit: Fooocus will trust the 25.6 GB "VRAM" number and can exhaust RAM.
* `rocm-smi` does not work in WSL because the `amdgpu` module is not loaded; use
  `rocminfo` or PyTorch for device queries.
* `torch.jit.interface` / `torch.jit.script` deprecation warnings from PyTorch
  2.14 are harmless.
