#!/usr/bin/env bash
# Clone Fooocus at a pinned tag, apply the ROCm diff, install the Python
# environment if needed, and launch the WebUI in share mode.
#
# Usage:
#   ./setup-fooocus-amd.sh [--dir DIR] [--ref REF] [--diff FILE]
#                          [--no-install] [--no-start] [-- EXTRA_ARGS...]
#
# Environment overrides:
#   FOOOCUS_REPO  git URL              (default: upstream Fooocus)
#   FOOOCUS_REF   tag, branch or commit (default: v2.5.5)
#   FOOOCUS_DIR   destination directory (default: ./fooocus-amd)
#   FOOOCUS_DIFF  path to the patch     (default: next to this script)
#   UV            path to uv            (default: uv on PATH, then ~/.local/bin/uv)
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_URL="${FOOOCUS_REPO:-https://github.com/lllyasviel/Fooocus.git}"
REF="${FOOOCUS_REF:-v2.5.5}"
DEST="${FOOOCUS_DIR:-$PWD/fooocus-amd}"
DIFF="${FOOOCUS_DIFF:-$SCRIPT_DIR/fooocus-rocm.diff}"
DO_INSTALL=1
DO_START=1

usage() {
  cat <<'EOF'
Clone Fooocus at a pinned tag, apply the ROCm diff, install the Python
environment if needed, and launch the WebUI in share mode.

Usage:
  ./setup-fooocus-amd.sh [--dir DIR] [--ref REF] [--diff FILE]
                         [--no-install] [--no-start] [-- EXTRA_ARGS...]

Environment overrides:
  FOOOCUS_REPO  git URL              (default: upstream Fooocus)
  FOOOCUS_REF   tag, branch or commit (default: v2.5.5)
  FOOOCUS_DIR   destination directory (default: ./fooocus-amd)
  FOOOCUS_DIFF  path to the patch     (default: next to this script)
  UV            path to uv            (default: uv on PATH, then ~/.local/bin/uv)
EOF
}

while [ $# -gt 0 ]; do
  case "$1" in
    --dir)        DEST="${2:?--dir needs a value}"; shift 2 ;;
    --ref)        REF="${2:?--ref needs a value}"; shift 2 ;;
    --diff)       DIFF="${2:?--diff needs a value}"; shift 2 ;;
    --no-install) DO_INSTALL=0; shift ;;
    --no-start)   DO_START=0; shift ;;
    -h|--help)    usage; exit 0 ;;
    --)           shift; break ;;
    *)            break ;;
  esac
done
EXTRA_ARGS=("$@")

die() { echo "error: $*" >&2; exit 1; }
log() { echo "==> $*"; }

command -v git >/dev/null 2>&1 || die "git is not installed"
[ -f "$DIFF" ] || die "diff not found: $DIFF"

# --- clone / checkout -------------------------------------------------------
if [ -d "$DEST/.git" ]; then
  log "Using existing clone at $DEST"
  git -C "$DEST" fetch --tags --force origin || \
    echo "warning: could not fetch; using the existing clone" >&2
else
  log "Cloning $REPO_URL"
  mkdir -p "$(dirname "$DEST")"
  git clone "$REPO_URL" "$DEST"
fi

log "Checking out $REF"
git -C "$DEST" checkout --force "$REF"

# --- apply diff -------------------------------------------------------------
if git -C "$DEST" apply --reverse --check "$DIFF" >/dev/null 2>&1; then
  log "Diff already applied"
else
  log "Applying $DIFF"
  git -C "$DEST" apply --check "$DIFF"
  git -C "$DEST" apply "$DIFF"
fi

chmod +x "$DEST/run-rocm.sh" "$DEST/test-rocm.sh" 2>/dev/null || true

# --- Python environment -----------------------------------------------------
if [ "$DO_INSTALL" = 1 ]; then
  UV_BIN="${UV:-}"
  if [ -z "$UV_BIN" ]; then
    UV_BIN="$(command -v uv 2>/dev/null || true)"
  fi
  if [ -z "$UV_BIN" ] && [ -x "$HOME/.local/bin/uv" ]; then
    UV_BIN="$HOME/.local/bin/uv"
  fi
  [ -n "$UV_BIN" ] || die "uv not found; install it or pass UV=/path/to/uv (see the port README)"

  if [ ! -x "$DEST/.venv/bin/python" ]; then
    log "Creating Python 3.12 venv"
    "$UV_BIN" venv --python 3.12 "$DEST/.venv"
  fi

  PY="$DEST/.venv/bin/python"
  log "Installing ROCm PyTorch wheels"
  "$UV_BIN" pip install --python "$PY" \
    --index-strategy unsafe-best-match \
    --index-url https://download.pytorch.org/whl/rocm7.2 \
    -r "$DEST/constraints-rocm.txt"

  log "Installing Fooocus requirements"
  "$UV_BIN" pip install --python "$PY" \
    --index-strategy unsafe-best-match \
    -r "$DEST/requirements_versions.txt"

  log "Installing Gradio-compatible web pins"
  "$UV_BIN" pip install --python "$PY" -r "$DEST/requirements-web-pins.txt"

  # launch.py shells out to "python -m pip" when requirements look missing.
  "$UV_BIN" pip install --python "$PY" pip
else
  log "Skipping Python environment setup (--no-install)"
fi

if ! command -v rocminfo >/dev/null 2>&1 && [ ! -x /opt/rocm/bin/rocminfo ]; then
  echo "warning: rocminfo not found; install ROCm 7.2.4 first (see the port README)" >&2
fi

# --- start ------------------------------------------------------------------
if [ "$DO_START" = 1 ]; then
  [ -x "$DEST/.venv/bin/python" ] || die "no .venv in $DEST; rerun without --no-install"
  log "Starting Fooocus in share mode"
  cd "$DEST"
  exec ./run-rocm.sh "${EXTRA_ARGS[@]}"
else
  log "Ready. Start with: cd \"$DEST\" && ./run-rocm.sh"
fi
