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
