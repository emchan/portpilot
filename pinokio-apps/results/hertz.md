# hertz — portability analysis

- **Package name:** hertz (`hertz`)
- **Description:** # hertz
- **Original git URL:** https://github.com/pinokiofactory/hertz
- **Analyzed commit:** `306ecc634eea5a51a3d20729d44cc94f5650d45d`
- **Platforms supported:** NVIDIA / AMD / Mac
- **Porting difficulty:** Low
- **CUDA-only packages:** —

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

ipython, matplotlib, model, numpy, tokenizer, torch, torch-directml, torchaudio, torchvision, utils

Third-party Python imports detected in local source: ipython, matplotlib, model, tokenizer, torch, torchaudio, utils.

Wheel indexes referenced: cu121, nightly.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 476
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- `torch.js` routes present: nvidia, amd, mac.
- No requirements file; third-party Python imports used as a fallback signal.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Difficulty score: 0.0 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-20)

- Downloaded upstream `peanutcocktail/hertz-dev`; installed CPU torch plus `requirements.txt`.
- Patched `app.py`: `device='cpu'`, removed `T.cuda.set_device(0)`, `autocast(device_type='cpu')`, dropped the BF16 `.to()` cast.
- Run completed and downloaded `inference_apatosaurus_95000.pt`; no runtime error after the patches.
- Result: **CPU port works with source patches.**

## CPU port attempt

- **Attempt order:** #40 of 101 (by porting effort, easiest first).
- **Status:** CPU-capable (shipped fallback).
- **Changes applied / required:** use existing non-NVIDIA/non-AMD branch in torch.js; use existing non-GPU launcher route; keep explicit device='cpu' branch; replace direct torch.cuda calls with devicetorch or cpu fallback.
- **Smoke check:** pass (1/1 files).
- **Blockers:** direct torch.cuda calls.
- **Scope note:** static portability review of the Pinokio wrapper; no install or model download was executed.
<!-- cross-analysis:start -->
## Cross-analysis details

- **CPU category (cpu.md):** CPU-capable with shipped fallback
- **TPU suitability:** Possible - moderate port
- **TPU work needed:** remove direct torch.cuda device assumptions; moderate device/kernel/runtime adaptation
- **Effort ranking (effort.md):** #40 — Low
- **Effort blockers:** direct `torch.cuda` calls
- **Precisions noted:** BF16
- **Models/flows noted:** —
- **Flow graph:** [flows/hertz.md](../flows/hertz.md)

### Snapshot verification (cloned analyzed commit)

- **Snapshot source:** `https://codeload.github.com/pinokiofactory/hertz/tar.gz/<analyzed commit>` extracted to `/tmp/opencode/pinokio-snapshots/hertz`
- **Files scanned:** 12 total (1 .py, 8 .js, 3 other)
- **Key files present:** pinokio.js, install.js, torch.js, start.js
- **TPU/CUDA-relevant signals:**
  - `torch_cuda`: 1 match(es) (e.g. app.py:16)
  - `xformers`: 2 match(es) (e.g. install.js:19, install.js:19)
  - `directml`: 1 match(es) (e.g. torch.js:20)

### Evidence from analysis files

| Source | Evidence |
|---|---|
| [kernels.md](../analysis/kernels.md) | `\| [hertz](https://github.com/pinokiofactory/hertz) \| [306ecc6](https://github.com/pinokiofactory/hertz/commit/306ecc634eea5a51a3d20729d44cc94f5650d45d) \| env/config flag \| [start.js:9](https://github.com/pinokiofactory/hertz/blob/306ecc634eea5a51a3d20729d44cc94f5650d45d/start.js#L9) — //          USE_FLASH_ATTENTION: 1,<br>[server.js:9](https://github.com/pinokiofactory/hertz/blob/306ecc634eea5a51a3d20729d44cc94f5650d45d/server.js#L9) — USE_FLASH_ATTENTION: 1, \|` |
| [quantization.md](../analysis/quantization.md) | `\| [hertz](https://github.com/pinokiofactory/hertz) \| [306ecc6](https://github.com/pinokiofactory/hertz/commit/306ecc634eea5a51a3d20729d44cc94f5650d45d) \| [33](https://github.com/pinokiofactory/hertz/blob/306ecc634eea5a51a3d20729d44cc94f5650d45d/app.py#L33) \| bfloat16 / BF16 \| dtype declaration \| generator = generator.eval().to(T.bfloat16).to(device) \|` |
| [quantization.md](../analysis/quantization.md) | `\| [hertz](https://github.com/pinokiofactory/hertz) \| [306ecc6](https://github.com/pinokiofactory/hertz/commit/306ecc634eea5a51a3d20729d44cc94f5650d45d) \| [73](https://github.com/pinokiofactory/hertz/blob/306ecc634eea5a51a3d20729d44cc94f5650d45d/app.py#L73) \| — \| explicit cast \| audio_tensor = audio_tensor.float() \|` |
| [quantization.md](../analysis/quantization.md) | `\| [hertz](https://github.com/pinokiofactory/hertz) \| [306ecc6](https://github.com/pinokiofactory/hertz/commit/306ecc634eea5a51a3d20729d44cc94f5650d45d) \| [96](https://github.com/pinokiofactory/hertz/blob/306ecc634eea5a51a3d20729d44cc94f5650d45d/app.py#L96) \| bfloat16 / BF16 \| mixed precision \| with T.autocast(device_type='cuda', dtype=T.bfloat16): \|` |
| [quantization.md](../analysis/quantization.md) | `\| [hertz](https://github.com/pinokiofactory/hertz) \| [306ecc6](https://github.com/pinokiofactory/hertz/commit/306ecc634eea5a51a3d20729d44cc94f5650d45d) \| [110](https://github.com/pinokiofactory/hertz/blob/306ecc634eea5a51a3d20729d44cc94f5650d45d/app.py#L110) \| bfloat16 / BF16 \| mixed precision \| with T.autocast(device_type='cuda', dtype=T.bfloat16): \|` |
| [quantization.md](../analysis/quantization.md) | `\| [hertz](https://github.com/pinokiofactory/hertz) \| [306ecc6](https://github.com/pinokiofactory/hertz/commit/306ecc634eea5a51a3d20729d44cc94f5650d45d) \| [119](https://github.com/pinokiofactory/hertz/blob/306ecc634eea5a51a3d20729d44cc94f5650d45d/app.py#L119) \| bfloat16 / BF16 \| explicit cast \| decoded_completion_ch1 = audio_tokenizer.data_from_latent(completed_audio[:, :, :32].bfloat16()) \|` |
| [quantization.md](../analysis/quantization.md) | `\| [hertz](https://github.com/pinokiofactory/hertz) \| [306ecc6](https://github.com/pinokiofactory/hertz/commit/306ecc634eea5a51a3d20729d44cc94f5650d45d) \| [120](https://github.com/pinokiofactory/hertz/blob/306ecc634eea5a51a3d20729d44cc94f5650d45d/app.py#L120) \| bfloat16 / BF16 \| explicit cast \| decoded_completion_ch2 = audio_tokenizer.data_from_latent(completed_audio[:, :, 32:].bfloat16()) \|` |
| [quantization.md](../analysis/quantization.md) | `\| [hertz](https://github.com/pinokiofactory/hertz) \| [306ecc6](https://github.com/pinokiofactory/hertz/commit/306ecc634eea5a51a3d20729d44cc94f5650d45d) \| [123](https://github.com/pinokiofactory/hertz/blob/306ecc634eea5a51a3d20729d44cc94f5650d45d/app.py#L123) \| bfloat16 / BF16 \| explicit cast \| decoded_completion = audio_tokenizer.data_from_latent(completed_audio.bfloat16()) \|` |
| [quantization.md](../analysis/quantization.md) | `\| [hertz](https://github.com/pinokiofactory/hertz) \| [306ecc6](https://github.com/pinokiofactory/hertz/commit/306ecc634eea5a51a3d20729d44cc94f5650d45d) \| [131](https://github.com/pinokiofactory/hertz/blob/306ecc634eea5a51a3d20729d44cc94f5650d45d/app.py#L131) \| — \| explicit cast \| audio_tensor = audio_tensor.float() \|` |
| [fusion.md](../analysis/fusion.md) | No direct fusion table row matched; see fusion.md for global context. |
| [models.md](../analysis/models.md) | No model pull/shape row matched in models.md. |
| [cpu.md](../analysis/cpu.md) | CPU category: **CPU-capable with shipped fallback** |
| [tpu.md](../analysis/tpu.md) | TPU suitability: **Possible - moderate port** — remove direct torch.cuda device assumptions; moderate device/kernel/runtime adaptation |

### Related analysis

- [CPU analysis](../analysis/cpu.md)
- [TPU analysis](../analysis/tpu.md)
- [Effort ranking](../analysis/effort.md)
- [Kernel evidence](../analysis/kernels.md)
- [Quantization evidence](../analysis/quantization.md)
- [Fusion evidence](../analysis/fusion.md)
- [Model pulls/shapes](../analysis/models.md)
- [Flow graphs](../analysis/flows.md)
- [App flow graph](../flows/hertz.md)
<!-- cross-analysis:end -->

## Snapdragon evaluation (deep clone)
- **Clone/scan status:** cloned and scanned
- **Files scanned:** 12 total (1 .py, 8 .js/.ts, 3 other)
- **Snapdragon-relevant signals:** cuda=5, torch=19, xformers=1, mps=1, directml=1
- **Example evidence:**
  - cuda: `app.py:13`
  - torch: `app.py:1`
  - xformers: `install.js:19`
  - mps: `app.py:113`
  - directml: `torch.js:20`
- **Snapdragon verdict:** Contains CUDA/Triton/TensorRT signals; Snapdragon path requires replacement or ONNX conversion.
