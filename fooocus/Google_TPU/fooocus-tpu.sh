#!/usr/bin/env bash
#
# fooocus-tpu.sh — clone Fooocus, apply the TPU port patch, and launch it
# on a PyTorch-native TPU backend with a public Gradio share link.
#
# Usage:
#   ./fooocus-tpu.sh                       # clone, install deps, and run
#   REPO_DIR=/opt/Fooocus ./fooocus-tpu.sh # custom checkout location
#   PORT=7865 ./fooocus-tpu.sh            # custom port
#   INSTALL_DEPS=0 ./fooocus-tpu.sh        # skip dependency installation
#
# Environment overrides:
#   REPO_URL   (default: https://github.com/lllyasviel/Fooocus.git)
#   TAG        (default: v2.5.5)
#   REPO_DIR   (default: ./Fooocus)
#   PATCH      (default: ./fooocus_tpu_patch.diff next to this script)
#   PORT       (default: 7860)
#   INSTALL_DEPS (default: 1)
#
set -euo pipefail

REPO_URL="${REPO_URL:-https://github.com/lllyasviel/Fooocus.git}"
TAG="${TAG:-v2.5.5}"
REPO_DIR="${REPO_DIR:-./Fooocus}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PATCH="${PATCH:-${SCRIPT_DIR}/fooocus_tpu_patch.diff}"
PORT="${PORT:-7860}"
INSTALL_DEPS="${INSTALL_DEPS:-1}"

if [[ ! -f "${PATCH}" ]]; then
    echo "ERROR: patch file not found: ${PATCH}" >&2
    exit 1
fi

# --- clone (or reuse) -------------------------------------------------------
if [[ ! -d "${REPO_DIR}/.git" ]]; then
    echo "Cloning ${REPO_URL} (tag ${TAG}) into ${REPO_DIR} ..."
    git clone --branch "${TAG}" --depth 1 "${REPO_URL}" "${REPO_DIR}"
else
    echo "Reusing existing checkout at ${REPO_DIR}"
fi

cd "${REPO_DIR}"
git fetch --tags --quiet 2>/dev/null || true
git checkout --quiet "${TAG}"

# --- apply the TPU port patch (idempotent) ----------------------------------
if git apply --check "${PATCH}" >/dev/null 2>&1; then
    echo "Applying TPU port patch ..."
    git apply "${PATCH}"
else
    # Already applied (or partial): verify the tree at least has the marker.
    if grep -q "is_tpu_backend" launch.py 2>/dev/null; then
        echo "TPU patch already applied; skipping."
    else
        echo "ERROR: patch does not apply cleanly and tree is not patched." >&2
        exit 1
    fi
fi

# --- dependency installation (TPU-safe, on by default) ----------------------
if [[ "${INSTALL_DEPS}" == "1" ]]; then
    # Re-running the script should not pay for pip resolution every time.
    if python - <<'PY' >/dev/null 2>&1
import importlib.metadata as md

expected = {
    "gradio": "3.41.2",
    "gradio-client": "0.5.0",
    "torchsde": "0.2.6",
    "fastapi": "0.104.1",
    "starlette": "0.27.0",
    "pydantic": "2.9.2",
    "websockets": "11.0.3",
}
for name, version in expected.items():
    try:
        if md.version(name) != version:
            raise SystemExit(1)
    except md.PackageNotFoundError:
        raise SystemExit(1)

required = ["trampoline", "timm", "supervision", "rembg", "onnxruntime"]
for name in required:
    try:
        md.version(name)
    except md.PackageNotFoundError:
        raise SystemExit(1)

try:
    md.version("opencv-python-headless")
except md.PackageNotFoundError:
    raise SystemExit(1)
PY
    then
        echo "TPU-safe extras already installed; skipping."
    else
        echo "Installing TPU-safe runtime extras ..."
        python -m pip install --quiet torchsde==0.2.6 trampoline
        python -m pip install --quiet --no-deps opencv-python-headless
        python -m pip install --quiet supervision timm pycocotools addict \
            segment-anything groundingdino-py onnxruntime rembg
        echo "Installing Gradio UI stack ..."
        python -m pip install --quiet --no-deps gradio==3.41.2 gradio-client==0.5.0
        python -m pip install --quiet fastapi==0.104.1 starlette==0.27.0 \
            pydantic==2.9.2 websockets==11.0.3
        python -m pip install --quiet ffmpy pydub semantic-version orjson importlib-resources
    fi
fi

# --- launch -----------------------------------------------------------------
echo "Starting Fooocus on TPU (port ${PORT}, share=true) ..."
exec python launch.py \
    --disable-analytics \
    --disable-in-browser \
    --port "${PORT}" \
    --share
