#!/usr/bin/env python3
"""Test a port end-to-end in an isolated folder.

Usage:
    python3 test-port.py            # detect platform, clone/patch/setup/run (executes)
    python3 test-port.py --dry-run  # print the selected port and commands only
    python3 test-port.py --port amx # force a port

By default this executes the clone/patch/setup steps in an isolated folder. Use
--dry-run to preview the commands without running them.
"""
from __future__ import annotations

import argparse
import os
import platform
import shutil
import subprocess
import sys
import time
from pathlib import Path

REPO = "https://github.com/lllyasviel/Fooocus.git"
TAG = "v2.5.5"
SNAP_COMMIT = "ae05379cc97bc4361ec8b4ec90193dab21be763f"

PORTS = {
    "amx": {
        "name": "Intel AMX",
        "patch": "fooocus/Intel_AMX/fooocus-amx.diff",
        "setup": "fooocus/Intel_AMX/fooocus-amx.sh",
        "python": "3.13",
        "launch": "webui.py --always-cpu 8 --amx bf16 --share",
        "check": "amx",
    },
    "amd": {
        "name": "AMD Radeon 780M (ROCm)",
        "patch": "fooocus/AMD_iGPU/fooocus-rocm.diff",
        "setup": "fooocus/AMD_iGPU/setup-fooocus-amd.sh",
        "python": "3.12",
        "launch": "run-rocm.sh",
        "check": "amd",
    },
    "tpu": {
        "name": "Google TPU (torch_tpu)",
        "patch": "fooocus/Google_TPU/fooocus_tpu_patch.diff",
        "setup": "fooocus/Google_TPU/fooocus-tpu.sh",
        "python": "3.13",
        "launch": "fooocus-tpu.sh",
        "check": "tpu",
    },
    "apple": {
        "name": "Apple Silicon (MPS)",
        "patch": "fooocus/Apple_Silicon/changes.diff",
        "setup": "fooocus/Apple_Silicon/setup_and_run.sh",
        "python": "3.11",
        "launch": "setup_and_run.sh",
        "check": "apple",
    },
    "snap": {
        "name": "Qualcomm Snapdragon X (NPU)",
        "patch": "fooocus/Qualcomm_Snapdragon/fooocus_snapdragon_win.diff",
        "setup": "fooocus/Qualcomm_Snapdragon/run_snapdragon.bat",
        "python": "3.10/3.12",
        "launch": "run_snapdragon.bat",
        "check": "snap",
    },
}


def detect_port():
    # TPU
    try:
        import torch
        if hasattr(torch, "accelerator") and torch.accelerator.is_available():
            acc = torch.accelerator.current_accelerator()
            if acc is not None and getattr(acc, "type", None) == "tpu":
                return "tpu"
        # MPS
        if getattr(torch.backends, "mps", None) and torch.backends.mps.is_available():
            return "apple"
        # CUDA / ROCm
        if torch.cuda.is_available():
            name = ""
            try:
                name = torch.cuda.get_device_name(0)
            except Exception:
                pass
            if "radeon" in name.lower() or "amd" in name.lower():
                return "amd"
    except Exception:
        pass
    # CPU AMX
    try:
        with open("/proc/cpuinfo") as f:
            for line in f:
                if line.startswith("flags") and "amx" in line.lower():
                    return "amx"
    except Exception:
        pass
    # Windows + QNN
    if platform.system() == "Windows":
        if os.environ.get("FOOOCUS_NPU") == "1":
            return "snap"
        # heuristic: qnn env present next to fooocus
        return "snap"
    return "amx"  # default to CPU path


def run(cmd, cwd=None, check=True):
    print(f"$ {cmd}")
    if check:
        subprocess.run(cmd, shell=True, cwd=cwd, check=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true", help="print commands without executing")
    ap.add_argument("--port", choices=list(PORTS), help="force a port")
    ap.add_argument("--keep", action="store_true", help="keep the isolated folder")
    args = ap.parse_args()

    port = args.port or detect_port()
    info = PORTS[port]
    print(f"Selected port: {info['name']} ({port})")
    print(f"Platform: {platform.system()} {platform.machine()}  Python {sys.version.split()[0]}")
    print()

    base = Path("/tmp/opencode") / f"test-port-{port}-{int(time.time())}"
    fooocus = base / "Fooocus"
    repo_root = Path(__file__).resolve().parents[4]  # repo root

    steps = []
    steps.append(("clone", f"git clone --depth 1 --branch {TAG} {REPO} {fooocus}"))
    if port == "snap":
        steps.append(("checkout", f"cd {fooocus} && git fetch --depth 1 origin {SNAP_COMMIT} && git checkout {SNAP_COMMIT}"))
    patch_src = repo_root / info["patch"]
    steps.append(("patch check", f"cd {fooocus} && git apply --check {patch_src}"))
    steps.append(("patch apply", f"cd {fooocus} && git apply {patch_src}"))
    steps.append(("setup", f"cd {fooocus} && bash {repo_root / info['setup']}"))
    steps.append(("launch", f"cd {fooocus} && {info['launch']}"))

    print("Steps:")
    for name, cmd in steps:
        print(f"  [{name}] {cmd}")
    print()
    print("Smoke test ladder (run after launch):")
    for i, s in enumerate([
        "1. import webui (no traceback)",
        "2. device probe reports intended accelerator + dtype",
        "3. kernel proof (verbose env / profiler)",
        "4. checkpoint keys match, non-zero loaded",
        "5. conditioning + first latent finite",
        "6. one headless image, non-flat (mean/std)",
        "7. HTTP 200 + process_completed success=True",
    ], 1):
        print(f"  {s}")
    print()

    if args.dry_run:
        print("Dry run. Re-run without --dry-run to execute (may take a while).")
        return

    base.mkdir(parents=True, exist_ok=True)
    for name, cmd in steps:
        print(f"\n>>> {name}")
        run(cmd)
    print(f"\nIsolated folder: {base}")
    if not args.keep:
        print("Pass --keep to retain it for debugging.")


if __name__ == "__main__":
    main()
