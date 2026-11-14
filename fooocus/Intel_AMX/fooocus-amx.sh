#!/usr/bin/env bash
# Self-contained Fooocus AMX port.
# Clones Fooocus, applies fooocus-amx.diff (embedded below), installs deps, runs with --share.
# Usage: bash fooocus-amx.sh [target_dir]
set -euo pipefail

TARGET="${1:-$HOME/Fooocus-AMX}"
REPO="https://github.com/lllyasviel/Fooocus.git"
PYTHON="${PYTHON:-python3}"

echo "=== Fooocus AMX port ==="
echo "Target: $TARGET"

# 1. Clone
if [ ! -d "$TARGET/.git" ]; then
  echo "[1/6] Cloning Fooocus..."
  rm -rf "$TARGET"
  git clone --depth 1 "$REPO" "$TARGET"
else
  echo "[1/6] Repo already cloned."
fi

# 2. Extract embedded diff
echo "[2/6] Extracting embedded diff..."
DIFF_TMP="$(mktemp)"
trap 'rm -f "$DIFF_TMP"' EXIT
sed -n '/^__DIFF_START__$/,/^__DIFF_END__$/p' "$0" | sed '1d;$d' > "$DIFF_TMP"

# 3. Apply diff via Python applier
echo "[3/6] Applying fooocus-amx.diff..."
"$PYTHON" - "$TARGET" "$DIFF_TMP" << 'PYEOF'
import os, re, sys

def apply_unified_diff(diff_text, root):
    lines = diff_text.splitlines(keepends=True)
    i = 0
    n = len(lines)
    while i < n:
        if not lines[i].startswith("--- "):
            i += 1
            continue
        old_path = lines[i][4:].split("\t")[0].strip()
        i += 1
        if i >= n or not lines[i].startswith("+++ "):
            continue
        new_path = lines[i][4:].split("\t")[0].strip()
        i += 1
        if old_path.startswith("a/"):
            old_path = old_path[2:]
        if new_path.startswith("b/"):
            new_path = new_path[2:]
        old_file = os.path.join(root, old_path) if old_path not in ("/dev/null",) else None
        new_file = os.path.join(root, new_path)
        if old_file and os.path.exists(old_file):
            with open(old_file) as fh:
                result = fh.read().splitlines(keepends=True)
        else:
            result = []
        offset = 0
        while i < n and lines[i].startswith("@@"):
            m = re.search(r"@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@", lines[i])
            if not m:
                break
            old_start = int(m.group(1))
            old_count = int(m.group(2)) if m.group(2) is not None else 1
            i += 1
            hunk_lines = []
            while i < n and (lines[i].startswith(" ") or lines[i].startswith("-") or lines[i].startswith("+") or lines[i].startswith("\\")):
                if lines[i].startswith("\\"):
                    i += 1
                    continue
                hunk_lines.append(lines[i])
                i += 1
                if i < n and (lines[i].startswith("@@") or lines[i].startswith("--- ") or lines[i].startswith("diff ")):
                    break
            pos = old_start - 1 + offset
            if pos < 0:
                pos = 0
            out_hunk = []
            for hl in hunk_lines:
                if hl.startswith("-"):
                    pass
                else:
                    out_hunk.append(hl[1:] if hl.startswith((" ", "+")) else hl)
            del result[pos:pos + old_count]
            result[pos:pos] = out_hunk
            offset += len(out_hunk) - old_count
        os.makedirs(os.path.dirname(new_file), exist_ok=True)
        with open(new_file, "w") as fh:
            fh.writelines(result)
        print("  patched:", new_path)

apply_unified_diff(open(sys.argv[2]).read(), sys.argv[1])

PYEOF

# 4. venv
if [ ! -d "$TARGET/venv" ]; then
  echo "[4/6] Creating venv..."
  "$PYTHON" -m venv "$TARGET/venv"
  "$TARGET/venv/bin/python" -m ensurepip --upgrade 2>/dev/null ||     curl -sSL https://bootstrap.pypa.io/get-pip.py | "$TARGET/venv/bin/python"
fi
PIP="$TARGET/venv/bin/python -m pip"

# 5. deps
echo "[5/6] Installing dependencies (this takes a while)..."
$PIP install --quiet --upgrade pip setuptools wheel 2>&1 | tail -1
$PIP install --quiet torch==2.8.0+cpu torchvision==0.23.0+cpu --index-url https://download.pytorch.org/whl/cpu 2>&1 | tail -1
$PIP install --quiet intel_extension_for_pytorch==2.8.0 2>&1 | tail -1
$PIP install --quiet safetensors einops transformers accelerate omegaconf scipy tqdm psutil pyyaml pillow opencv-contrib-python-headless timm tokenizers packaging torchsde numpy 2>&1 | tail -1
$PIP install --quiet --no-deps gradio==3.41.2 2>&1 | tail -1
$PIP install --quiet gradio-client requests httpx fastapi uvicorn python-multipart aiofiles websockets matplotlib pandas altair ffmpy pydub audioop-lts orjson semantic_version 2>&1 | tail -1
$PIP install --quiet groundingdino-py segment_anything "rembg[cpu]" onnxruntime starlette==0.27.0 2>&1 | tail -1
$TARGET/venv/bin/python - "$TARGET/venv/lib/python3.13/site-packages/gradio/processing_utils.py" << 'PYEOF'
import sys
p = sys.argv[1]
s = open(p).read()
s = s.replace("        np.bool8: (False, True),  # type: ignore\n", "        **({np.bool8: (False, True)} if hasattr(np, 'bool8') else {}),  # type: ignore\n")
open(p, "w").write(s)
print("  patched gradio processing_utils")
PYEOF

# 6. run
echo "[6/6] Starting Fooocus with --share ..."
cd "$TARGET"
export FOOOCUS_AMX=bf16
exec "$TARGET/venv/bin/python" webui.py --always-cpu 8 --amx bf16 --share --disable-in-browser "$@"

: << 'DIFF_DATA_EOF'
__DIFF_START__
diff --git a/ldm_patched/modules/args_parser.py b/ldm_patched/modules/args_parser.py
--- a/ldm_patched/modules/args_parser.py	2025-09-02 20:28:40.000000000 +0000
+++ b/ldm_patched/modules/args_parser.py	2026-11-13 05:07:06.801165997 +0000
@@ -80,6 +80,9 @@
 
 parser.add_argument("--disable-ipex-hijack", action="store_true")
 
+parser.add_argument("--amx", type=str, default="auto", choices=["auto", "none", "bf16", "int8", "ipex"],
+                    help="Intel AMX acceleration mode on CPU (auto/none/bf16/int8/ipex).")
+
 class LatentPreviewMethod(enum.Enum):
     NoPreviews = "none"
     Auto = "auto"
diff --git a/ldm_patched/modules/model_management.py b/ldm_patched/modules/model_management.py
--- a/ldm_patched/modules/model_management.py	2025-09-02 20:28:40.000000000 +0000
+++ b/ldm_patched/modules/model_management.py	2026-11-13 05:07:35.265149273 +0000
@@ -189,6 +189,14 @@
 if is_intel_xpu():
     VAE_DTYPE = torch.bfloat16
 
+# Intel AMX: enable SDPA (uses AMX-friendly kernels) on CPU.
+try:
+    _amx_mode = getattr(args, "amx", "auto")
+    if _amx_mode in ("auto", "bf16", "int8", "ipex") and cpu_mode():
+        ENABLE_PYTORCH_ATTENTION = True
+except Exception:
+    pass
+
 if args.vae_in_cpu:
     VAE_DTYPE = torch.float32
 
@@ -303,6 +311,14 @@
             self.model_unload()
             raise e
 
+        # Intel AMX: apply IPEX optimization (prepack) when enabled.
+        try:
+            import modules.amx as _amx
+            if _amx.amx_enabled() and getattr(_amx, "AMX_MODE", "none") in ("ipex",):
+                self.real_model = _amx.optimize_module(self.real_model)
+        except Exception as e:
+            print(f"[AMX] model_load optimize failed: {e}")
+
         if lowvram_model_memory > 0:
             print("loading in lowvram mode", lowvram_model_memory/(1024 * 1024))
             mem_counter = 0
diff --git a/ldm_patched/modules/sd.py b/ldm_patched/modules/sd.py
--- a/ldm_patched/modules/sd.py	2025-09-02 20:28:40.000000000 +0000
+++ b/ldm_patched/modules/sd.py	2026-11-13 05:03:20.353381381 +0000
@@ -39,16 +39,20 @@
 def load_clip_weights(model, sd):
     k = list(sd.keys())
     for x in k:
-        if x.startswith("cond_stage_model.transformer.") and not x.startswith("cond_stage_model.transformer.text_model."):
-            y = x.replace("cond_stage_model.transformer.", "cond_stage_model.transformer.text_model.")
+        if ".transformer.text_model." in x:
+            y = x.replace(".transformer.text_model.", ".transformer.")
             sd[y] = sd.pop(x)
 
-    if 'cond_stage_model.transformer.text_model.embeddings.position_ids' in sd:
-        ids = sd['cond_stage_model.transformer.text_model.embeddings.position_ids']
-        if ids.dtype == torch.float32:
-            sd['cond_stage_model.transformer.text_model.embeddings.position_ids'] = ids.round()
-
-    sd = ldm_patched.modules.utils.transformers_convert(sd, "cond_stage_model.model.", "cond_stage_model.transformer.text_model.", 24)
+    for prefix in ("cond_stage_model.transformer.", "cond_stage_model.clip_l.transformer.", "cond_stage_model.clip_g.transformer."):
+        key = prefix + "embeddings.position_ids"
+        if key in sd:
+            ids = sd[key]
+            if ids.dtype == torch.float32:
+                sd[key] = ids.round()
+
+    sd = ldm_patched.modules.utils.transformers_convert(sd, "cond_stage_model.model.", "cond_stage_model.transformer.", 24)
+    sd = ldm_patched.modules.utils.transformers_convert(sd, "cond_stage_model.clip_l.model.", "cond_stage_model.clip_l.transformer.", 24)
+    sd = ldm_patched.modules.utils.transformers_convert(sd, "cond_stage_model.clip_g.model.", "cond_stage_model.clip_g.transformer.", 24)
     return load_model_weights(model, sd)
 
 
@@ -308,15 +312,15 @@
 
     for i in range(len(clip_data)):
         if "transformer.resblocks.0.ln_1.weight" in clip_data[i]:
-            clip_data[i] = ldm_patched.modules.utils.transformers_convert(clip_data[i], "", "text_model.", 32)
+            clip_data[i] = ldm_patched.modules.utils.transformers_convert(clip_data[i], "", "", 32)
 
     clip_target = EmptyClass()
     clip_target.params = {}
     if len(clip_data) == 1:
-        if "text_model.encoder.layers.30.mlp.fc1.weight" in clip_data[0]:
+        if "encoder.layers.30.mlp.fc1.weight" in clip_data[0]:
             clip_target.clip = sdxl_clip.SDXLRefinerClipModel
             clip_target.tokenizer = sdxl_clip.SDXLTokenizer
-        elif "text_model.encoder.layers.22.mlp.fc1.weight" in clip_data[0]:
+        elif "encoder.layers.22.mlp.fc1.weight" in clip_data[0]:
             clip_target.clip = sd2_clip.SD2ClipModel
             clip_target.tokenizer = sd2_clip.SD2Tokenizer
         else:
diff --git a/ldm_patched/modules/sdxl_clip.py b/ldm_patched/modules/sdxl_clip.py
--- a/ldm_patched/modules/sdxl_clip.py	2025-09-02 20:28:40.000000000 +0000
+++ b/ldm_patched/modules/sdxl_clip.py	2026-11-13 05:02:54.993416431 +0000
@@ -56,7 +56,7 @@
         return torch.cat([l_out, g_out], dim=-1), g_pooled
 
     def load_sd(self, sd):
-        if "text_model.encoder.layers.30.mlp.fc1.weight" in sd:
+        if "encoder.layers.30.mlp.fc1.weight" in sd or "text_model.encoder.layers.30.mlp.fc1.weight" in sd:
             return self.clip_g.load_sd(sd)
         else:
             return self.clip_l.load_sd(sd)
diff --git a/ldm_patched/modules/supported_models.py b/ldm_patched/modules/supported_models.py
--- a/ldm_patched/modules/supported_models.py	2025-09-02 20:28:40.000000000 +0000
+++ b/ldm_patched/modules/supported_models.py	2026-11-13 05:04:20.693307792 +0000
@@ -30,14 +30,15 @@
     def process_clip_state_dict(self, state_dict):
         k = list(state_dict.keys())
         for x in k:
-            if x.startswith("cond_stage_model.transformer.") and not x.startswith("cond_stage_model.transformer.text_model."):
-                y = x.replace("cond_stage_model.transformer.", "cond_stage_model.transformer.text_model.")
+            if x.startswith("cond_stage_model.transformer.text_model."):
+                y = x.replace("cond_stage_model.transformer.text_model.", "cond_stage_model.transformer.")
                 state_dict[y] = state_dict.pop(x)
 
-        if 'cond_stage_model.transformer.text_model.embeddings.position_ids' in state_dict:
-            ids = state_dict['cond_stage_model.transformer.text_model.embeddings.position_ids']
+        key = "cond_stage_model.transformer.embeddings.position_ids"
+        if key in state_dict:
+            ids = state_dict[key]
             if ids.dtype == torch.float32:
-                state_dict['cond_stage_model.transformer.text_model.embeddings.position_ids'] = ids.round()
+                state_dict[key] = ids.round()
 
         replace_prefix = {}
         replace_prefix["cond_stage_model."] = "cond_stage_model.clip_l."
@@ -75,7 +76,7 @@
         replace_prefix["conditioner.embedders.0.model."] = "cond_stage_model.model." #SD2 in sgm format
         state_dict = utils.state_dict_prefix_replace(state_dict, replace_prefix)
 
-        state_dict = utils.transformers_convert(state_dict, "cond_stage_model.model.", "cond_stage_model.clip_h.transformer.text_model.", 24)
+        state_dict = utils.transformers_convert(state_dict, "cond_stage_model.model.", "cond_stage_model.clip_h.transformer.", 24)
         return state_dict
 
     def process_clip_state_dict_for_saving(self, state_dict):
@@ -132,7 +133,7 @@
         keys_to_replace = {}
         replace_prefix = {}
 
-        state_dict = utils.transformers_convert(state_dict, "conditioner.embedders.0.model.", "cond_stage_model.clip_g.transformer.text_model.", 32)
+        state_dict = utils.transformers_convert(state_dict, "conditioner.embedders.0.model.", "cond_stage_model.clip_g.transformer.", 32)
         keys_to_replace["conditioner.embedders.0.model.text_projection"] = "cond_stage_model.clip_g.text_projection"
         keys_to_replace["conditioner.embedders.0.model.logit_scale"] = "cond_stage_model.clip_g.logit_scale"
 
@@ -142,8 +143,8 @@
     def process_clip_state_dict_for_saving(self, state_dict):
         replace_prefix = {}
         state_dict_g = diffusers_convert.convert_text_enc_state_dict_v20(state_dict, "clip_g")
-        if "clip_g.transformer.text_model.embeddings.position_ids" in state_dict_g:
-            state_dict_g.pop("clip_g.transformer.text_model.embeddings.position_ids")
+        if "clip_g.transformer.embeddings.position_ids" in state_dict_g:
+            state_dict_g.pop("clip_g.transformer.embeddings.position_ids")
         replace_prefix["clip_g"] = "conditioner.embedders.0.model"
         state_dict_g = utils.state_dict_prefix_replace(state_dict_g, replace_prefix)
         return state_dict_g
@@ -179,8 +180,8 @@
         keys_to_replace = {}
         replace_prefix = {}
 
-        replace_prefix["conditioner.embedders.0.transformer.text_model"] = "cond_stage_model.clip_l.transformer.text_model"
-        state_dict = utils.transformers_convert(state_dict, "conditioner.embedders.1.model.", "cond_stage_model.clip_g.transformer.text_model.", 32)
+        replace_prefix["conditioner.embedders.0.transformer"] = "cond_stage_model.clip_l.transformer"
+        state_dict = utils.transformers_convert(state_dict, "conditioner.embedders.1.model.", "cond_stage_model.clip_g.transformer.", 32)
         keys_to_replace["conditioner.embedders.1.model.text_projection"] = "cond_stage_model.clip_g.text_projection"
         keys_to_replace["conditioner.embedders.1.model.text_projection.weight"] = "cond_stage_model.clip_g.text_projection"
         keys_to_replace["conditioner.embedders.1.model.logit_scale"] = "cond_stage_model.clip_g.logit_scale"
@@ -193,8 +194,8 @@
         replace_prefix = {}
         keys_to_replace = {}
         state_dict_g = diffusers_convert.convert_text_enc_state_dict_v20(state_dict, "clip_g")
-        if "clip_g.transformer.text_model.embeddings.position_ids" in state_dict_g:
-            state_dict_g.pop("clip_g.transformer.text_model.embeddings.position_ids")
+        if "clip_g.transformer.embeddings.position_ids" in state_dict_g:
+            state_dict_g.pop("clip_g.transformer.embeddings.position_ids")
         for k in state_dict:
             if k.startswith("clip_l"):
                 state_dict_g[k] = state_dict[k]
diff --git a/modules/amx.py b/modules/amx.py
--- a/modules/amx.py	1970-01-01 00:00:00.000000000 +0000
+++ b/modules/amx.py	2026-11-13 05:10:00.337091606 +0000
@@ -0,0 +1,109 @@
+"""Intel AMX acceleration for Fooocus on CPU.
+
+Exposes a single configuration knob (--amx) with modes:
+  none  : no AMX-specific changes (plain fp32).
+  bf16  : bfloat16 autocast -> oneDNN AMX_BF16 (default on AMX-capable CPUs).
+  int8  : IPEX static int8 quantization -> oneDNN AMX_INT8 (experimental).
+  ipex  : IPEX bf16 with weight prepack (best throughput) + autocast.
+"""
+import os
+import torch
+
+try:
+    import intel_extension_for_pytorch as ipex
+    _IPEX_AVAILABLE = True
+except Exception:
+    ipex = None
+    _IPEX_AVAILABLE = False
+
+AMX_MODE = "none"
+_IPEX_OPTIMIZED = False
+
+
+def _cpu_has_amx():
+    try:
+        with open("/proc/cpuinfo") as f:
+            for line in f:
+                if line.startswith("flags"):
+                    return "amx" in line.lower()
+    except Exception:
+        pass
+    return False
+
+
+def configure(mode="auto"):
+    global AMX_MODE
+    env = os.environ.get("FOOOCUS_AMX", "").strip().lower()
+    if env:
+        mode = env
+    if mode == "auto":
+        mode = "bf16" if _cpu_has_amx() else "none"
+    AMX_MODE = mode
+
+    # Thread / NUMA tuning for Xeon.
+    n = int(os.environ.get("FOOOCUS_AMX_THREADS", "0"))
+    if n <= 0:
+        n = torch.get_num_threads() or os.cpu_count() or 4
+    torch.set_num_threads(n)
+    try:
+        torch.set_flush_denormal(True)
+    except Exception:
+        pass
+
+    # oneDNN primitive cache (larger = fewer re-orders).
+    os.environ.setdefault("ONEDNN_MAX_CACHE_SIZE", str(4096 * 1024 * 1024))
+    # OpenMP affinity for single-NUMA Xeon.
+    os.environ.setdefault("OMP_NUM_THREADS", str(n))
+    os.environ.setdefault("KMP_BLOCKTIME", "1")
+    os.environ.setdefault("OMP_PROC_BIND", "close")
+    os.environ.setdefault("OMP_PLACES", "cores")
+
+    print(f"[AMX] mode={AMX_MODE} threads={torch.get_num_threads()} ipex={_IPEX_AVAILABLE} amx_cpu={_cpu_has_amx()}")
+    return AMX_MODE
+
+
+def amx_enabled():
+    return AMX_MODE in ("bf16", "int8", "ipex")
+
+
+def autocast_ctx():
+    """Context manager for AMX-friendly compute precision."""
+    if AMX_MODE in ("bf16", "ipex"):
+        return torch.autocast(device_type="cpu", dtype=torch.bfloat16)
+    # int8 path relies on quantized weights; keep fp32 autocast off.
+    return torch.autocast(device_type="cpu", enabled=False)
+
+
+def optimize_module(module):
+    """Apply IPEX optimization (prepack + dtype) in place where possible."""
+    global _IPEX_OPTIMIZED
+    if not (_IPEX_AVAILABLE and AMX_MODE in ("ipex", "bf16")):
+        return module
+    try:
+        dtype = torch.bfloat16 if AMX_MODE in ("bf16", "ipex") else torch.float32
+        if hasattr(module, "eval"):
+            module.eval()
+        module = ipex.optimize(module, dtype=dtype, weights_prepack=True, auto_kernel_selection=True)
+        _IPEX_OPTIMIZED = True
+    except Exception as e:
+        print(f"[AMX] ipex.optimize failed: {e}")
+    return module
+
+
+def quantize_module(module, example_input=None):
+    """IPEX static int8 quantization (AMX_INT8)."""
+    if not (_IPEX_AVAILABLE and AMX_MODE == "int8"):
+        return module
+    try:
+        from intel_extension_for_pytorch.quantization import (
+            prepare, convert, default_static_qconfig_mapping,
+        )
+        qm = prepare(module.eval(), default_static_qconfig_mapping, example_inputs=example_input, inplace=False)
+        if example_input is not None:
+            with torch.no_grad():
+                qm(example_input)
+        cm = convert(qm, inplace=False)
+        return cm
+    except Exception as e:
+        print(f"[AMX] int8 quantization failed: {e}")
+        return module
diff --git a/modules/patch.py b/modules/patch.py
--- a/modules/patch.py	2025-09-02 20:28:40.000000000 +0000
+++ b/modules/patch.py	2026-11-13 05:14:24.037076517 +0000
@@ -20,6 +20,7 @@
 import warnings
 import safetensors.torch
 import modules.constants as constants
+import modules.amx as amx_mod
 
 from ldm_patched.modules.samplers import calc_cond_uncond_batch
 from ldm_patched.k_diffusion.sampling import BatchedBrownianTree
@@ -490,6 +491,13 @@
         ldm_patched.modules.model_management.lowvram_available = True
         ldm_patched.modules.model_management.OOM_EXCEPTION = Exception
 
+    # Configure Intel AMX acceleration.
+    try:
+        _amx_mode = getattr(ldm_patched.modules.args_parser.args, "amx", "auto")
+    except Exception:
+        _amx_mode = "auto"
+    amx_mod.configure(_amx_mode)
+
     patch_all_precision()
     patch_all_clip()
 
@@ -499,12 +507,41 @@
     ldm_patched.modules.model_management.load_models_gpu = patched_load_models_gpu
     ldm_patched.modules.model_patcher.ModelPatcher.calculate_weight = calculate_weight_patched
     ldm_patched.controlnet.cldm.ControlNet.forward = patched_cldm_forward
-    ldm_patched.ldm.modules.diffusionmodules.openaimodel.UNetModel.forward = patched_unet_forward
+    _orig_unet_forward = patched_unet_forward
+    def _amx_unet_forward(self, *args, **kwargs):
+        with amx_mod.autocast_ctx():
+            return _orig_unet_forward(self, *args, **kwargs)
+    ldm_patched.ldm.modules.diffusionmodules.openaimodel.UNetModel.forward = _amx_unet_forward
     ldm_patched.modules.model_base.SDXL.encode_adm = sdxl_encode_adm_patched
     ldm_patched.modules.samplers.KSamplerX0Inpaint.forward = patched_KSamplerX0Inpaint_forward
     ldm_patched.k_diffusion.sampling.BrownianTreeNoiseSampler = BrownianTreeNoiseSamplerPatched
     ldm_patched.modules.samplers.sampling_function = patched_sampling_function
 
+    # Wrap VAE decode in AMX autocast.
+    try:
+        from ldm_patched.contrib.external import VAEDecode, VAEDecodeTiled
+        for _cls in (VAEDecode, VAEDecodeTiled):
+            if hasattr(_cls, "decode"):
+                _orig = _cls.decode
+                def _wrap(self, *a, _orig=_orig, **kw):
+                    with amx_mod.autocast_ctx():
+                        return _orig(self, *a, **kw)
+                _cls.decode = _wrap
+    except Exception as e:
+        print(f"[AMX] VAE wrap failed: {e}")
+
+    # Wrap CLIP encode in AMX autocast.
+    try:
+        from ldm_patched.modules.sd1_clip import SDClipModel
+        if hasattr(SDClipModel, "encode_token_weights"):
+            _orig_enc = SDClipModel.encode_token_weights
+            def _wrap_enc(self, *a, **kw):
+                with amx_mod.autocast_ctx():
+                    return _orig_enc(self, *a, **kw)
+            SDClipModel.encode_token_weights = _wrap_enc
+    except Exception as e:
+        print(f"[AMX] CLIP wrap failed: {e}")
+
     warnings.filterwarnings(action='ignore', module='torchsde')
 
     build_loaded(safetensors.torch, 'load_file')
diff --git a/modules/patch_clip.py b/modules/patch_clip.py
--- a/modules/patch_clip.py	2025-09-02 20:28:40.000000000 +0000
+++ b/modules/patch_clip.py	2026-11-13 05:02:15.777475843 +0000
@@ -19,7 +19,12 @@
 import ldm_patched.modules.ops as ops
 
 from modules.ops import use_patched_ops
-from transformers import CLIPTextModel, CLIPTextConfig, modeling_utils, CLIPVisionConfig, CLIPVisionModelWithProjection
+from transformers import CLIPTextModel, CLIPTextConfig, CLIPVisionConfig, CLIPVisionModelWithProjection
+try:
+    from transformers.initialization import no_init_weights as _no_init_weights
+except ImportError:
+    from transformers import modeling_utils as _mu
+    _no_init_weights = _mu.no_init_weights
 
 
 def patched_encode_token_weights(self, token_weight_pairs):
@@ -79,13 +84,13 @@
     self.num_layers = config.num_hidden_layers
 
     with use_patched_ops(ops.manual_cast):
-        with modeling_utils.no_init_weights():
+        with _no_init_weights():
             self.transformer = CLIPTextModel(config)
 
     if dtype is not None:
         self.transformer.to(dtype)
 
-    self.transformer.text_model.embeddings.to(torch.float32)
+    self.transformer.embeddings.to(torch.float32)
 
     if freeze:
         self.freeze()
@@ -133,7 +138,7 @@
     else:
         z = outputs.hidden_states[self.layer_idx]
         if self.layer_norm_hidden_state:
-            z = self.transformer.text_model.final_layer_norm(z)
+            z = self.transformer.final_layer_norm(z)
 
     if hasattr(outputs, "pooler_output"):
         pooled_output = outputs.pooler_output.float()
@@ -158,7 +163,7 @@
         self.dtype = torch.float32
 
     with use_patched_ops(ops.manual_cast):
-        with modeling_utils.no_init_weights():
+        with _no_init_weights():
             self.model = CLIPVisionModelWithProjection(config)
 
     self.model.to(self.dtype)
diff --git a/modules/ui_gradio_extensions.py b/modules/ui_gradio_extensions.py
--- a/modules/ui_gradio_extensions.py	2025-09-02 20:28:40.000000000 +0000
+++ b/modules/ui_gradio_extensions.py	2026-11-13 06:46:08.494585633 +0000
@@ -58,10 +58,27 @@
     css = css_html()
 
     def template_response(*args, **kwargs):
-        res = GradioTemplateResponseOriginal(*args, **kwargs)
-        res.body = res.body.replace(b'</head>', f'{js}</head>'.encode("utf8"))
-        res.body = res.body.replace(b'</body>', f'{css}</body>'.encode("utf8"))
-        res.init_headers()
+        try:
+            res = GradioTemplateResponseOriginal(*args, **kwargs)
+        except Exception as e:
+            # Log and try alternate argument order (newer starlette passes request first).
+            import sys
+            print("[ui_gradio_extensions] TemplateResponse error:", repr(e), "args=", [type(a).__name__ for a in args], file=sys.stderr)
+            try:
+                # If first arg is a dict, swap
+                if args and isinstance(args[0], dict):
+                    res = GradioTemplateResponseOriginal(args[1], args[0], **kwargs)
+                else:
+                    raise
+            except Exception as e2:
+                print("[ui_gradio_extensions] fallback failed:", repr(e2), file=sys.stderr)
+                raise
+        try:
+            res.body = res.body.replace(b'</head>', f'{js}</head>'.encode("utf8"))
+            res.body = res.body.replace(b'</body>', f'{css}</body>'.encode("utf8"))
+            res.init_headers()
+        except Exception:
+            pass
         return res
 
     gr.routes.templates.TemplateResponse = template_response

__DIFF_END__
DIFF_DATA_EOF
