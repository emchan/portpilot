# TRELLIS — portability analysis

- **Package name:** TRELLIS (`TRELLIS`)
- **Description:** A pinokio script for https://github.com/microsoft/TRELLIS
- **Original git URL:** https://github.com/pinokiofactory/TRELLIS
- **Analyzed commit:** `3d6dec1fada102cba537ce7f6926061b0af7b962`
- **Platforms supported:** NVIDIA / AMD / Mac
- **Porting difficulty:** Very high
- **CUDA-only packages:** ccimport, cumm-cu120, diff-gaussian-rasterization, diffoctreerast, flash-attn, kaolin, nvdiffrast, nvidia-cublas-cu12, nvidia-cuda-cupti-cu12, nvidia-cuda-nvrtc-cu12, nvidia-cuda-runtime-cu12, nvidia-cudnn-cu12, nvidia-cufft-cu12, nvidia-curand-cu12, nvidia-cusolver-cu12, nvidia-cusparse-cu12, nvidia-nccl-cu12, nvidia-nvjitlink-cu12, nvidia-nvtx-cu12, pccm, spconv-cu120, triton, warp-lang, xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

aiofiles, annotated-types, anyio, asttokens, attrs, blinker, ccimport, certifi, cffi, charset-normalizer, click, colorama, coloredlogs, comm, contourpy, cumm-cu120, cycler, dataclasses-json, decorator, deprecated, diff-gaussian-rasterization, diffoctreerast, easydict, einops, entrypoints, exceptiongroup, executing, fastapi, ffmpy, filelock, fire, flash-attn, flask, flatbuffers, fonttools, fsspec, glcontext, gradio, gradio-client, gradio-litmodel3d, h11, httpcore, httpx, huggingface-hub, humanfriendly, idna, igraph, imageio, imageio-ffmpeg, importlib-resources, ipycanvas, ipyevents, ipython, ipywidgets, itsdangerous, jedi, jinja2, jsonschema, jsonschema-specifications, jupyter-client, jupyter-core, jupyterlab-widgets, kaolin, kiwisolver, lark, lazy-loader, llvmlite, markdown-it-py, markupsafe, marshmallow, matplotlib, matplotlib-inline, mdurl, moderngl, mpmath, mypy-extensions, nest-asyncio, networkx, ninja, numba, numpy, nvdiffrast, nvidia-cublas-cu12, nvidia-cuda-cupti-cu12, nvidia-cuda-nvrtc-cu12, nvidia-cuda-runtime-cu12, nvidia-cudnn-cu12, nvidia-cufft-cu12, nvidia-curand-cu12, nvidia-cusolver-cu12, nvidia-cusparse-cu12, nvidia-nccl-cu12, nvidia-nvjitlink-cu12, nvidia-nvtx-cu12, onnxruntime, open3d, opencv-python-headless, orjson, packaging, pandas, parso, pccm, pexpect, pillow, platformdirs, plyfile, pooch, portalocker, prompt-toolkit, protobuf, ptyprocess, pure-eval, pybind11, pycparser, pydantic, pydantic-core, pydub, pygltflib, pygments, pymatting, pymeshfix, pyparsing, pyreadline3, python-dateutil, python-multipart, pytz, pyvista, pywin32, pyyaml, pyzmq, referencing, regex, rembg, requests, rich, rpds-py, ruff, safetensors, scikit-image, scipy, scooby, semantic-version, setuptools, shellingham, six, sniffio, spconv-cu120, stack-data, starlette, sympy, termcolor, texttable, tifffile, tokenizers, tomlkit, torch, torch-directml, torchaudio, torchvision, tornado, tqdm, traitlets, transformers, trimesh, triton, typer, typing-extensions, typing-inspect, tzdata, urllib3, usd-core, utils3d, uvicorn, vox2seq, vtk, warp-lang, wcwidth, websockets, werkzeug, wheel, widgetsnbextension, wrapt, xatlas, xformers

Requirements files: `requirements-uv.txt`, `requirements.txt`.

Wheel indexes referenced: cpu, cu124, rocm6.0.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 277
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- `torch.js` routes present: nvidia, amd, mac, cpu.
- Requirements from: requirements-uv.txt, requirements.txt
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): xformers
- Difficulty score: 57.5 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- blocked by CUDA-only compiled extensions (nvdiffrast, diff-gaussian-rasterization, kaolin).
- Result: **not runnable in this container.**

## CPU port attempt

- **Attempt order:** #99 of 101 (by porting effort, easiest first).
- **Status:** Blocked.
- **Changes applied / required:** use existing CPU wheel branch in torch.js; use existing non-NVIDIA/non-AMD branch in torch.js; use existing non-GPU launcher route; disable fused GPU kernels (xformers/flash/sage) in config; substitute GPU-only attention libs with SDPA math backend; remove/disable compiled CUDA extensions or provide CPU fallback.
- **Smoke check:** n/a (no Python source in snapshot).
- **Blockers:** hard CUDA/TensorRT blocker; GPU-only attention: flash-attn/triton/xformers; compiled CUDA extensions: ccimport/cumm-cu120/diff-gaussian-rasterization...; CUDA-only fused kernels.
- **Scope note:** static portability review of the Pinokio wrapper; no install or model download was executed.
<!-- cross-analysis:start -->
## Cross-analysis details

- **CPU category (cpu.md):** Hard-blocked on CUDA
- **TPU suitability:** Hard - major rewrite/replacement required
- **TPU work needed:** CUDA/TensorRT/compiled CUDA extension dependency
- **Effort ranking (effort.md):** #99 — Very high
- **Effort blockers:** hard CUDA/TensorRT blocker in code; GPU-only attention: flash-attn/triton/xformers; compiled CUDA extensions: ccimport/cumm-cu120/diff-gaussian-rasterization/diffoctreerast...; 12 NVIDIA runtime libs; CUDA-only fused kernels need config change
- **Precisions noted:** unspecified
- **Models/flows noted:** —
- **Flow graph:** [flows/TRELLIS.md](../flows/TRELLIS.md)

### Snapshot verification (cloned analyzed commit)

- **Snapshot source:** `https://codeload.github.com/pinokiofactory/TRELLIS/tar.gz/<analyzed commit>` extracted to `/tmp/opencode/pinokio-snapshots/TRELLIS`
- **Files scanned:** 11 total (0 .py, 6 .js, 5 other)
- **Key files present:** pinokio.js, install.js, torch.js, start.js, requirements.txt
- **TPU/CUDA-relevant signals:**
  - `xformers`: 8 match(es) (e.g. requirements.txt:7, torch.js:10)
  - `flash_attn`: 20 match(es) (e.g. requirements.txt:34, requirements.txt:34)
  - `triton`: 18 match(es) (e.g. requirements.txt:41, requirements.txt:41)
  - `directml`: 1 match(es) (e.g. torch.js:20)

### Evidence from analysis files

| Source | Evidence |
|---|---|
| [kernels.md](../analysis/kernels.md) | `\| [TRELLIS](https://github.com/pinokiofactory/TRELLIS) \| [3d6dec1](https://github.com/pinokiofactory/TRELLIS/commit/3d6dec1fada102cba537ce7f6926061b0af7b962) \| requirements \| requirements-uv.txt, requirements.txt \| [requirements-uv.txt:90](https://github.com/pinokiofactory/TRELLIS/blob/3d6dec1fada102cba537ce7f6926061b0af7b962/requirements-uv.txt#L90) — #   triton \|` |
| [kernels.md](../analysis/kernels.md) | `\| [TRELLIS](https://github.com/pinokiofactory/TRELLIS) \| [3d6dec1](https://github.com/pinokiofactory/TRELLIS/commit/3d6dec1fada102cba537ce7f6926061b0af7b962) \| requirements \| [requirements-uv.txt:72](https://github.com/pinokiofactory/TRELLIS/blob/3d6dec1fada102cba537ce7f6926061b0af7b962/requirements-uv.txt#L72) — # via flash-attn<br>[requirements-uv.txt:96](https://github.com/pinokiofactory/TRELLIS/blob/3d6dec1fada102cba537ce7f6926061b0af7b962/requirements-uv.txt#L96) — flash-attn @ https://github.com/bdashore3/flash-attention/releases/download/v2.7.1.post1/flash_attn-2.7.1.post1+cu124torch2.5.1cxx11abiFALSE-cp310-cp310-win_amd64... \|` |
| [quantization.md](../analysis/quantization.md) | No per-repo quantization table row matched; see quantization.md. |
| [fusion.md](../analysis/fusion.md) | `\| [TRELLIS](https://github.com/pinokiofactory/TRELLIS) \| [3d6dec1](https://github.com/pinokiofactory/TRELLIS/commit/3d6dec1fada102cba537ce7f6926061b0af7b962) \| dependency only \| [requirements-uv.txt:96](https://github.com/pinokiofactory/TRELLIS/blob/3d6dec1fada102cba537ce7f6926061b0af7b962/requirements-uv.txt#L96) — `flash-attn @ https://github.com/bdashore3/flash-attention/releases/download/v2.7.1.post1/flash_attn-2.7.1.post1+cu124torch2.5.1cxx11abiFALSE-cp310-cp3` \|` |
| [models.md](../analysis/models.md) | No model pull/shape row matched in models.md. |
| [cpu.md](../analysis/cpu.md) | CPU category: **Hard-blocked on CUDA** |
| [tpu.md](../analysis/tpu.md) | TPU suitability: **Hard - major rewrite/replacement required** — CUDA/TensorRT/compiled CUDA extension dependency |

### Related analysis

- [CPU analysis](../analysis/cpu.md)
- [TPU analysis](../analysis/tpu.md)
- [Effort ranking](../analysis/effort.md)
- [Kernel evidence](../analysis/kernels.md)
- [Quantization evidence](../analysis/quantization.md)
- [Fusion evidence](../analysis/fusion.md)
- [Model pulls/shapes](../analysis/models.md)
- [Flow graphs](../analysis/flows.md)
- [App flow graph](../flows/TRELLIS.md)
<!-- cross-analysis:end -->

## Snapdragon evaluation (deep clone)
- **Clone/scan status:** cloned and scanned
- **Files scanned:** 11 total (0 .py, 6 .js/.ts, 5 other)
- **Snapdragon-relevant signals:** cuda=3, torch=55, triton=9, xformers=5, directml=1, safetensors=1
- **Example evidence:**
  - cuda: `requirements-uv.txt:285`
  - torch: `install.js:12`
  - triton: `requirements-uv.txt:90`
  - xformers: `install.js:20`
  - directml: `torch.js:20`
  - safetensors: `requirements-uv.txt:452`
- **Snapdragon verdict:** Contains CUDA/Triton/TensorRT signals; Snapdragon path requires replacement or ONNX conversion.
