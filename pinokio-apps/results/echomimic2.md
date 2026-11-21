# echomimic2 — portability analysis

- **Package name:** echomimic2 (`echomimic2`)
- **Description:** [NVIDIA ONLY] Make virtual avatars talk whatever you want with an image and an audio clip https://github.com/antgroup/echomimic_v2
- **Original git URL:** https://github.com/pinokiofactory/echomimic2
- **Analyzed commit:** `eb7915a14420505c7c8b929a2dbba570f1639831`
- **Platforms supported:** NVIDIA only
- **Porting difficulty:** High
- **CUDA-only packages:** onnxruntime-gpu, triton-windows, xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

accelerate, av, clip, controlnet-aux, decord, diffusers, einops, facenet-pytorch, ffmpeg-python, gradio, gradio-client, hf-xet, huggingface-hub, imageio, imageio-ffmpeg, ipython, mediapipe, mlflow, moviepy, numpy, omegaconf, onnxruntime-gpu, open-clip-torch, opencv-contrib-python, opencv-python, pillow, pydantic, scenedetect, scikit-image, scikit-learn, scipy, soundfile, torch, torchao, torchaudio, torchdiffeq, torchmetrics, torchsde, torchtyping, torchvision, tqdm, transformers, triton-windows, wheel, xformers

Requirements files: `requirements.txt`.

Wheel indexes referenced: cu128.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 275
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- Explicit platform tag found: NVIDIA only.
- `torch.js` routes present: nvidia.
- Requirements from: requirements.txt
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): triton, xformers
- Difficulty score: 9.5 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- retested on Python 3.10; blocked by CLIP build failure (pkg_resources).
- Result: **not runnable in this container.**
<!-- cross-analysis:start -->
## Cross-analysis details

- **CPU category (cpu.md):** CPU possible, but launcher must change
- **TPU suitability:** Difficult - significant port
- **TPU work needed:** replace CUDA attention kernels with TPU-compatible attention/SDPA/XLA; add TPU launcher/runtime branch; replace onnxruntime-gpu with TPU-compatible runtime; multiple CUDA-specific dependencies or large model/dtype constraints
- **Effort ranking (effort.md):** #93 — Very high
- **Effort blockers:** no CPU/AMD launcher branch; GPU-only attention: triton-windows/xformers; GPU runtime: onnxruntime-gpu
- **Precisions noted:** FP32
- **Models/flows noted:** [BadToBest/EchoMimicV2](https://huggingface.co/BadToBest/EchoMimicV2), [cocktailpeanut/audio_processor](https://huggingface.co/cocktailpeanut/audio_processor), [lambdalabs/sd-image-variations-diffusers](https://huggingface.co/lambdalabs/sd-image-variations-diffusers), [stabilityai/sd-vae-ft-mse](https://huggingface.co/stabilityai/sd-vae-ft-mse)
- **Flow graph:** [flows/echomimic2.md](../flows/echomimic2.md)

### Snapshot verification (cloned analyzed commit)

- **Snapshot source:** `https://codeload.github.com/pinokiofactory/echomimic2/tar.gz/<analyzed commit>` extracted to `/tmp/opencode/pinokio-snapshots/echomimic2`
- **Files scanned:** 12 total (0 .py, 7 .js, 5 other)
- **Key files present:** pinokio.js, install.js, torch.js, start.js, requirements.txt
- **TPU/CUDA-relevant signals:**
  - `xformers`: 5 match(es) (e.g. torch.js:11, torch.js:11)
  - `triton`: 3 match(es) (e.g. torch.js:12, torch.js:12)
  - `onnxruntime_gpu`: 1 match(es) (e.g. requirements.txt:20)

### Evidence from analysis files

| Source | Evidence |
|---|---|
| [kernels.md](../analysis/kernels.md) | `\| [echomimic2](https://github.com/pinokiofactory/echomimic2) \| [eb7915a](https://github.com/pinokiofactory/echomimic2/commit/eb7915a14420505c7c8b929a2dbba570f1639831) \| optional flag + launcher install \| install.js, torch.js \| [torch.js:12](https://github.com/pinokiofactory/echomimic2/blob/eb7915a14420505c7c8b929a2dbba570f1639831/torch.js#L12) — "{{args && args.triton ? 'uv pip install triton-windows==3.3.1.post19' : ''}}", \|` |
| [quantization.md](../analysis/quantization.md) | `\| [echomimic2](https://github.com/pinokiofactory/echomimic2) \| launcher install \| `torch.js:13` — "uv pip install torchao==0.12.0"<br>`torch.js:27` — "uv pip install torchao==0.14.1 --index-url https://download.pytorch.org/whl/cu128", \|` |
| [fusion.md](../analysis/fusion.md) | No direct fusion table row matched; see fusion.md for global context. |
| [models.md](../analysis/models.md) | No model pull/shape row matched in models.md. |
| [cpu.md](../analysis/cpu.md) | CPU category: **CPU possible, but launcher must change** |
| [tpu.md](../analysis/tpu.md) | TPU suitability: **Difficult - significant port** — replace CUDA attention kernels with TPU-compatible attention/SDPA/XLA; add TPU launcher/runtime branch; replace onnxruntime-gpu with TPU-compatible runtime; multiple CUDA-specific dependencies or large model/dtype constraints |

### Related analysis

- [CPU analysis](../analysis/cpu.md)
- [TPU analysis](../analysis/tpu.md)
- [Effort ranking](../analysis/effort.md)
- [Kernel evidence](../analysis/kernels.md)
- [Quantization evidence](../analysis/quantization.md)
- [Fusion evidence](../analysis/fusion.md)
- [Model pulls/shapes](../analysis/models.md)
- [Flow graphs](../analysis/flows.md)
- [App flow graph](../flows/echomimic2.md)
<!-- cross-analysis:end -->
