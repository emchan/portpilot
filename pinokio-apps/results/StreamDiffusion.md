# StreamDiffusion — portability analysis

- **Package name:** StreamDiffusion (`StreamDiffusion`)
- **Description:** StreamDiffusion: A Pipeline-Level Solution for Real-Time Interactive Generation
- **Original git URL:** https://github.com/pinokiofactory/StreamDiffusion
- **Analyzed commit:** `0e529aaff2ff344ce15565420e0c484688eb1bc9`
- **Platforms supported:** NVIDIA only
- **Porting difficulty:** Very high
- **CUDA-only packages:** stable-fast, tensorrt, torch (CUDA wheel), triton, xformers

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

accelerate, av, compel, controlnet-aux, diffusers, fastapi, gradio, markdown2, matplotlib, mss, peft, pillow, stable-fast, torch, transformers, uvicorn, xformers

Requirements files: `demo/realtime-img2img/requirements.txt`, `demo/realtime-txt2img/requirements.txt`, `demo/vid2vid/requirements.txt`, `examples/screen/requirements.txt`, `examples/vid2vid/requirements.txt`.

Third-party Python imports detected in local source: cuda, diffusers, fastapi, fire, gradio, markdown2, mss, numpy, onnx, onnx-graphsurgeon, packaging, pil, polygraphy, pydantic, requests, setuptools, sfast, starlette, streamdiffusion, tensorrt, torch, torchvision, tqdm, transformers, triton, utils, uvicorn, xformers.

Wheel indexes referenced: cu121.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 6347
- **CUDA-related functions used:** `cudaGraphInstantiate`, `cudaGraphLaunch`, `cudaMemGetInfo`, `cudaStreamBeginCapture`, `cudaStreamEndCapture`, `cudaStreamSynchronize`, `torch.cuda.Event`, `torch.cuda.empty_cache`, `torch.cuda.is_available`, `torch.cuda.synchronize`

## Evidence and notes

- `torch.js` routes present: none.
- Requirements from: demo/realtime-img2img/requirements.txt, demo/realtime-txt2img/requirements.txt, demo/vid2vid/requirements.txt, examples/screen/requirements.txt, examples/vid2vid/requirements.txt
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Difficulty score: 15.0 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- dependencies installed and streamdiffusion imported successfully on CPU (TensorRT not required for import).
- Result: **CPU port imports successfully.**

## CPU port attempt

- **Attempt order:** #98 of 101 (by porting effort, easiest first).
- **Status:** Blocked.
- **Changes applied / required:** use existing non-GPU launcher route; keep explicit device='cpu' branch; replace direct torch.cuda calls with devicetorch or cpu fallback; disable fused GPU kernels (xformers/flash/sage) in config; substitute GPU-only attention libs with SDPA math backend; remove GPU runtimes (onnxruntime-gpu/deepspeed/cudnn/tensorrt); +2.
- **Smoke check:** pass (36/36 files).
- **Blockers:** hard CUDA/TensorRT blocker; GPU-only attention: triton/xformers; GPU runtime: tensorrt; CUDA-only torch wheel; +2.
- **Scope note:** static portability review of the Pinokio wrapper; no install or model download was executed.
