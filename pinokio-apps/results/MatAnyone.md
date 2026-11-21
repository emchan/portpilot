# MatAnyone — portability analysis

- **Package name:** MatAnyone (`MatAnyone`)
- **Description:** MatAnyone AI is a tool for editing videos by separating objects from their backgrounds. It is an AI to remove the background from videos effectively. Stable Video Matting with Consistent Memory Propagation: https://github.com/pq-yang/MatAnyone.git
- **Original git URL:** https://github.com/pinokiofactory/MatAnyone
- **Analyzed commit:** `84831993029bc83f5942f0401bc8a32dd315b217`
- **Platforms supported:** NVIDIA only
- **Porting difficulty:** Medium
- **CUDA-only packages:** xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

av, cchardet, charset-normalizer, cython, easydict, einops, fastapi, ffmpeg-python, gdown, gitpython, gradio, hickle, hydra-core, imageio, matplotlib, netifaces, numpy, opencv-python, openmim, pillow, progressbar2, psutil, pycocotools, pyqtdarktheme, pyside6, pyyaml, requests, scipy, tensorboard, torch, torch-directml, torchaudio, torchvision, tqdm, xformers

Requirements files: `requirements.txt`.

Third-party Python imports detected in local source: cv2, ffmpeg, gradio, imageio, matanyone, matanyone-wrapper, numpy, pil, psutil, tools, torch.

Wheel indexes referenced: cpu, cu124, cu128, rocm6.2.4.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 1528
- **CUDA-related functions used:** `torch.cuda.is_available`

## Evidence and notes

- Explicit platform tag found: NVIDIA only.
- `torch.js` routes present: nvidia, amd, mac, cpu.
- Requirements from: requirements.txt
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): xformers
- Difficulty score: 3.5 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- retested on Python 3.12; blocked by torchvision operator mismatch (torchvision::nms).
- Result: **not runnable in this container.**
<!-- cross-analysis:start -->
## Cross-analysis details

- **CPU category (cpu.md):** CPU-capable with shipped fallback
- **TPU suitability:** Difficult - significant port
- **TPU work needed:** replace CUDA attention kernels with TPU-compatible attention/SDPA/XLA; remove direct torch.cuda device assumptions; MPS-specific branch irrelevant on TPU; keep device abstraction clean; multiple CUDA-specific dependencies or large model/dtype constraints
- **Effort ranking (effort.md):** #57 — Medium
- **Effort blockers:** GPU-only attention: xformers; direct `torch.cuda` calls; MPS branch is Apple-only
- **Precisions noted:** UINT8
- **Models/flows noted:** —
- **Flow graph:** [flows/MatAnyone.md](../flows/MatAnyone.md)

### Snapshot verification (cloned analyzed commit)

- **Snapshot source:** `https://codeload.github.com/pinokiofactory/MatAnyone/tar.gz/<analyzed commit>` extracted to `/tmp/opencode/pinokio-snapshots/MatAnyone`
- **Files scanned:** 12 total (1 .py, 7 .js, 4 other)
- **Key files present:** pinokio.js, install.js, torch.js, start.js, requirements.txt
- **TPU/CUDA-relevant signals:**
  - `torch_cuda`: 2 match(es) (e.g. app.py:55, app.py:56)
  - `xformers`: 5 match(es) (e.g. torch.js:23, torch.js:23)
  - `directml`: 1 match(es) (e.g. torch.js:33)
  - `mps`: 3 match(es) (e.g. app.py:53, app.py:53)

### Evidence from analysis files

| Source | Evidence |
|---|---|
| [kernels.md](../analysis/kernels.md) | `\| [MatAnyone](https://github.com/pinokiofactory/MatAnyone) \| [8483199](https://github.com/pinokiofactory/MatAnyone/commit/84831993029bc83f5942f0401bc8a32dd315b217) \| direct code + optional flag \| [app.py:53](https://github.com/pinokiofactory/MatAnyone/blob/84831993029bc83f5942f0401bc8a32dd315b217/app.py#L53) — if hasattr(torch.backends, 'mps') and torch.backends.mps.is_available():<br>[app.py:54](https://github.com/pinokiofactory/MatAnyone/blob/84831993029bc83f5942f0401bc8a32dd315b217/app.py#L54) — args.device = "mps" + gpu_str \|` |
| [quantization.md](../analysis/quantization.md) | `\| [MatAnyone](https://github.com/pinokiofactory/MatAnyone) \| [8483199](https://github.com/pinokiofactory/MatAnyone/commit/84831993029bc83f5942f0401bc8a32dd315b217) \| [100](https://github.com/pinokiofactory/MatAnyone/blob/84831993029bc83f5942f0401bc8a32dd315b217/app.py#L100) \| uint8 \| dtype declaration \| "masks": [np.zeros((frames[0].shape[0],frames[0].shape[1]), np.uint8)]*len(frames), \|` |
| [quantization.md](../analysis/quantization.md) | `\| [MatAnyone](https://github.com/pinokiofactory/MatAnyone) \| [8483199](https://github.com/pinokiofactory/MatAnyone/commit/84831993029bc83f5942f0401bc8a32dd315b217) \| [253](https://github.com/pinokiofactory/MatAnyone/blob/84831993029bc83f5942f0401bc8a32dd315b217/app.py#L253) \| uint8 \| dtype declaration \| "masks": [np.zeros((frames[0].shape[0],frames[0].shape[1]), np.uint8)]*len(frames), \|` |
| [quantization.md](../analysis/quantization.md) | `\| [MatAnyone](https://github.com/pinokiofactory/MatAnyone) \| [8483199](https://github.com/pinokiofactory/MatAnyone/commit/84831993029bc83f5942f0401bc8a32dd315b217) \| [376](https://github.com/pinokiofactory/MatAnyone/blob/84831993029bc83f5942f0401bc8a32dd315b217/app.py#L376) \| uint8 \| explicit cast \| select_frame = mask_painter(select_frame, mask.astype('uint8'), mask_color=mask_number+2) \|` |
| [fusion.md](../analysis/fusion.md) | No direct fusion table row matched; see fusion.md for global context. |
| [models.md](../analysis/models.md) | No model pull/shape row matched in models.md. |
| [cpu.md](../analysis/cpu.md) | CPU category: **CPU-capable with shipped fallback** |
| [tpu.md](../analysis/tpu.md) | TPU suitability: **Difficult - significant port** — replace CUDA attention kernels with TPU-compatible attention/SDPA/XLA; remove direct torch.cuda device assumptions; MPS-specific branch irrelevant on TPU; keep device abstraction clean; multiple CUDA-specific dependencies or large model/dtype constraints |

### Related analysis

- [CPU analysis](../analysis/cpu.md)
- [TPU analysis](../analysis/tpu.md)
- [Effort ranking](../analysis/effort.md)
- [Kernel evidence](../analysis/kernels.md)
- [Quantization evidence](../analysis/quantization.md)
- [Fusion evidence](../analysis/fusion.md)
- [Model pulls/shapes](../analysis/models.md)
- [Flow graphs](../analysis/flows.md)
- [App flow graph](../flows/MatAnyone.md)
<!-- cross-analysis:end -->
