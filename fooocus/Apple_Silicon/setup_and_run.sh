#!/usr/bin/env bash
# Self-contained script: clone Fooocus, apply Mac porting patches, run in shared mode with int4 on.
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_DIR="${1:-$SCRIPT_DIR/Fooocus}"

# Mac Python framework support: prefer a 3.10+ interpreter
PYBIN=""
for cand in "python3.10" "python3.11" "python3.12" "python3"; do
  if command -v "$cand" >/dev/null 2>&1; then
    PYVER=$("$cand" -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")' 2>/dev/null)
    MAJOR=${PYVER%%.*}; MINOR=${PYVER##*.}
    if [ "$MAJOR" = "3" ] && [ "$MINOR" -ge "10" ] 2>/dev/null; then
      PYBIN=$(command -v "$cand"); break
    fi
  fi
done
# Search common macOS framework locations
if [ -z "$PYBIN" ]; then
  for base in "/Library/Frameworks/Python.framework/Versions" "$HOME/Library/Frameworks/Python.framework/Versions"; do
    for v in 3.12 3.11 3.10; do
      if [ -x "$base/$v/bin/python3" ]; then
        PYBIN="$base/$v/bin/python3"
        export DYLD_FRAMEWORK_PATH="$(dirname "$(dirname "$base")")"
        export DYLD_LIBRARY_PATH="$base/$v/lib"
        break 2
      fi
    done
  done
fi
if [ -z "$PYBIN" ]; then
  echo "No Python 3.10+ found. Install from python.org first." >&2
  exit 1
fi
# Use PYBIN explicitly instead of relying on PATH
PYTHON="$PYBIN"
export PATH="$(dirname "$PYBIN"):$PATH"

# --- Python check (done above in PYBIN search) ---
echo "Using Python: $PYTHON"
$PYTHON -c 'import sys; print(sys.version)'
# --- Clone ---
if [ ! -d "$REPO_DIR/.git" ]; then
  echo "Cloning Fooocus..."
  git clone https://github.com/lllyasviel/Fooocus.git "$REPO_DIR"
fi

cd "$REPO_DIR"

# --- Apply tracked changes ---
if [ -f "$SCRIPT_DIR/changes.diff" ]; then
  echo "Applying changes.diff..."
  git apply --whitespace=nowarn "$SCRIPT_DIR/changes.diff" || echo "diff already applied or conflict (continuing)"
fi

# --- Copy new files ---
if [ -f "$SCRIPT_DIR/quantization.py" ]; then
  cp "$SCRIPT_DIR/quantization.py" "$REPO_DIR/modules/quantization.py"
fi
# ACCELERATION_OPTIONS content is now merged into README.md

# --- Environment (Mac MPS) ---
export PYTORCH_ENABLE_MPS_FALLBACK=1
export PYTORCH_MPS_HIGH_WATERMARK_RATIO=0.0
export TOKENIZERS_PARALLELISM=false

# --- Dependencies ---
echo "Installing dependencies..."
$PYTHON -m pip install --upgrade pip >/dev/null 2>&1 || true
$PYTHON -m pip install torch torchvision 2>&1 | tail -2
if [ -f requirements_versions.txt ]; then
  $PYTHON -m pip install -r requirements_versions.txt 2>&1 | tail -3
fi
# gradio 3.41.2 compatibility pins
$PYTHON -m pip install "fastapi==0.104.1" "starlette==0.27.0" "jinja2==3.1.2" "pydantic==1.10.13" 2>&1 | tail -2

# --- Run ---
echo "Starting Fooocus in shared mode with int4 enabled..."
exec "$PYTHON" -u launch.py --listen --share --disable-in-browser "$@"
