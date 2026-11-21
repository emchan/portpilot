# Nari-Dia-TTS — portability analysis

- **Package name:** Nari-Dia-TTS (`Nari-Dia-TTS`)
- **Description:** Nari Dia is a powerful text-to-speech (TTS) application based on the Dia-1.6B model from Nari Labs. This application allows you to convert text into natural-sounding speech with various customization options.
- **Original git URL:** https://github.com/pinokiofactory/Nari-Dia-TTS
- **Analyzed commit:** `e5b630df297c7f47f6c518a00d6c3f44be4e25b5`
- **Platforms supported:** NVIDIA / AMD / Mac
- **Porting difficulty:** Medium
- **CUDA-only packages:** sageattention *(optional)*, triton-windows, xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

descript-audio-codec, gradio, huggingface-hub, numpy, pydantic, sageattention, soundfile, torch, torch-directml, torchaudio, torchvision, triton-windows, xformers

Requirements files: `requirements.txt`.

Third-party Python imports detected in local source: dac, dia, gradio, huggingface-hub, numpy, pydantic, soundfile, the, torch, torchaudio.

Wheel indexes referenced: cpu, cu124, nightly, rocm6.2.4.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 2634
- **CUDA-related functions used:** `torch.cuda.is_available`

## Evidence and notes

- `torch.js` routes present: nvidia, amd, mac, cpu.
- Requirements from: requirements.txt
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): sageattention, triton, xformers
- Difficulty score: 4.0 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- retested on Python 3.12; blocked by torchaudio extension loading failure.
- Result: **not runnable in this container.**
<!-- cross-analysis:start -->
## Cross-analysis details

- **CPU category (cpu.md):** CPU-capable with shipped fallback
- **TPU suitability:** Difficult - significant port
- **TPU work needed:** replace CUDA attention kernels with TPU-compatible attention/SDPA/XLA; remove direct torch.cuda device assumptions; MPS-specific branch irrelevant on TPU; keep device abstraction clean; multiple CUDA-specific dependencies or large model/dtype constraints
- **Effort ranking (effort.md):** #59 — Medium–high
- **Effort blockers:** GPU-only attention: sageattention/triton-windows/xformers; direct `torch.cuda` calls; CUDA-only fused kernels need config change; MPS branch is Apple-only
- **Precisions noted:** FP32, FP16, BF16, UINT8, INT16, INT32, BOOL
- **Models/flows noted:** [nari-labs/Dia-1.6B](https://huggingface.co/nari-labs/Dia-1.6B)
- **Flow graph:** [flows/Nari-Dia-TTS.md](../flows/Nari-Dia-TTS.md)

### Snapshot verification (cloned analyzed commit)

- **Snapshot source:** `https://codeload.github.com/pinokiofactory/Nari-Dia-TTS/tar.gz/<analyzed commit>` extracted to `/tmp/opencode/pinokio-snapshots/Nari-Dia-TTS`
- **Files scanned:** 22 total (6 .py, 7 .js, 9 other)
- **Key files present:** pinokio.js, install.js, torch.js, start.js, requirements.txt
- **TPU/CUDA-relevant signals:**
  - `torch_cuda`: 1 match(es) (e.g. app.py:33)
  - `xformers`: 6 match(es) (e.g. torch.js:26, torch.js:26)
  - `sageattention`: 12 match(es) (e.g. torch.js:13, torch.js:13)
  - `triton`: 6 match(es) (e.g. torch.js:12, torch.js:12)
  - `directml`: 1 match(es) (e.g. torch.js:40)
  - `mps`: 6 match(es) (e.g. README.md:68, app.py:23)
  - `jax`: 3 match(es) (e.g. dia/model.py:141, dia/model.py:157)

### Evidence from analysis files

| Source | Evidence |
|---|---|
| [kernels.md](../analysis/kernels.md) | `\| [Nari-Dia-TTS](https://github.com/pinokiofactory/Nari-Dia-TTS) \| [e5b630d](https://github.com/pinokiofactory/Nari-Dia-TTS/commit/e5b630df297c7f47f6c518a00d6c3f44be4e25b5) \| optional flag + launcher install \| install.js, torch.js \| [torch.js:12](https://github.com/pinokiofactory/Nari-Dia-TTS/blob/e5b630df297c7f47f6c518a00d6c3f44be4e25b5/torch.js#L12) — "{{args && args.triton ? 'uv pip install -U --pre triton-windows' : ''}}", \|` |
| [kernels.md](../analysis/kernels.md) | `\| [Nari-Dia-TTS](https://github.com/pinokiofactory/Nari-Dia-TTS) \| [e5b630d](https://github.com/pinokiofactory/Nari-Dia-TTS/commit/e5b630df297c7f47f6c518a00d6c3f44be4e25b5) \| direct code \| [app.py:23](https://github.com/pinokiofactory/Nari-Dia-TTS/blob/e5b630df297c7f47f6c518a00d6c3f44be4e25b5/app.py#L23) — "--device", type=str, default=None, help="Force device (e.g., 'cuda', 'mps', 'cpu')"<br>[app.py:35](https://github.com/pinokiofactory/Nari-Dia-TTS/blob/e5b630df297c7f47f6c518a00d6c3f44be4e25b5/app.py#L35) — # Simplified MPS check for broader compatibility \|` |
| [kernels.md](../analysis/kernels.md) | `\| [Nari-Dia-TTS](https://github.com/pinokiofactory/Nari-Dia-TTS) \| [e5b630d](https://github.com/pinokiofactory/Nari-Dia-TTS/commit/e5b630df297c7f47f6c518a00d6c3f44be4e25b5) \| optional flag + launcher install \| [torch.js:13](https://github.com/pinokiofactory/Nari-Dia-TTS/blob/e5b630df297c7f47f6c518a00d6c3f44be4e25b5/torch.js#L13) — "{{args && args.sageattention ? 'uv pip install https://github.com/woct0rdho/SageAttention/releases/download/v2.1.1-windows/sageattention-2.1.1+cu128torch2.7.0-cp...<br>[torch.js:28](https://github.com/pinokiofactory/Nari-Dia-TTS/blob/e5b630df297c7f47f6c518a00d6c3f44be4e25b5/torch.js#L28) — "{{args && args.sageattention ? 'uv pip install https://github.com/deepbeepmeep/SageAttention/raw/refs/heads/main/releases/sageattention-2.1.0-cp310-cp310-win_amd... \|` |
| [quantization.md](../analysis/quantization.md) | `\| [Nari-Dia-TTS](https://github.com/pinokiofactory/Nari-Dia-TTS) \| direct code \| `dia/audio.py:234` — audio_values = model.quantizer.from_codes(audio_codes) \|` |
| [quantization.md](../analysis/quantization.md) | `\| [Nari-Dia-TTS](https://github.com/pinokiofactory/Nari-Dia-TTS) \| [e5b630d](https://github.com/pinokiofactory/Nari-Dia-TTS/commit/e5b630df297c7f47f6c518a00d6c3f44be4e25b5) \| [74](https://github.com/pinokiofactory/Nari-Dia-TTS/blob/e5b630df297c7f47f6c518a00d6c3f44be4e25b5/app.py#L74) \| float / FP32 \| dtype declaration \| output_audio = (44100, np.zeros(1, dtype=np.float32)) \|` |
| [quantization.md](../analysis/quantization.md) | `\| [Nari-Dia-TTS](https://github.com/pinokiofactory/Nari-Dia-TTS) \| [e5b630d](https://github.com/pinokiofactory/Nari-Dia-TTS/commit/e5b630df297c7f47f6c518a00d6c3f44be4e25b5) \| [93](https://github.com/pinokiofactory/Nari-Dia-TTS/blob/e5b630df297c7f47f6c518a00d6c3f44be4e25b5/app.py#L93) \| float / FP32 \| dtype declaration \| # Convert to float32 in [-1, 1] range if integer type \|` |
| [quantization.md](../analysis/quantization.md) | `\| [Nari-Dia-TTS](https://github.com/pinokiofactory/Nari-Dia-TTS) \| [e5b630d](https://github.com/pinokiofactory/Nari-Dia-TTS/commit/e5b630df297c7f47f6c518a00d6c3f44be4e25b5) \| [96](https://github.com/pinokiofactory/Nari-Dia-TTS/blob/e5b630df297c7f47f6c518a00d6c3f44be4e25b5/app.py#L96) \| float / FP32 \| explicit cast \| audio_data = audio_data.astype(np.float32) / max_val \|` |
| [quantization.md](../analysis/quantization.md) | `\| [Nari-Dia-TTS](https://github.com/pinokiofactory/Nari-Dia-TTS) \| [e5b630d](https://github.com/pinokiofactory/Nari-Dia-TTS/commit/e5b630df297c7f47f6c518a00d6c3f44be4e25b5) \| [103](https://github.com/pinokiofactory/Nari-Dia-TTS/blob/e5b630df297c7f47f6c518a00d6c3f44be4e25b5/app.py#L103) \| float / FP32 \| explicit cast \| audio_data = audio_data.astype(np.float32) \|` |
| [quantization.md](../analysis/quantization.md) | `\| [Nari-Dia-TTS](https://github.com/pinokiofactory/Nari-Dia-TTS) \| [e5b630d](https://github.com/pinokiofactory/Nari-Dia-TTS/commit/e5b630df297c7f47f6c518a00d6c3f44be4e25b5) \| [106](https://github.com/pinokiofactory/Nari-Dia-TTS/blob/e5b630df297c7f47f6c518a00d6c3f44be4e25b5/app.py#L106) \| float / FP32 \| dtype declaration \| f"Failed to convert audio prompt to float32: {conv_e}" \|` |
| [quantization.md](../analysis/quantization.md) | `\| [Nari-Dia-TTS](https://github.com/pinokiofactory/Nari-Dia-TTS) \| [e5b630d](https://github.com/pinokiofactory/Nari-Dia-TTS/commit/e5b630df297c7f47f6c518a00d6c3f44be4e25b5) \| [182](https://github.com/pinokiofactory/Nari-Dia-TTS/blob/e5b630df297c7f47f6c518a00d6c3f44be4e25b5/app.py#L182) \| float / FP32 \| explicit cast \| resampled_audio_np.astype(np.float32), \|` |
| [quantization.md](../analysis/quantization.md) | `\| [Nari-Dia-TTS](https://github.com/pinokiofactory/Nari-Dia-TTS) \| [e5b630d](https://github.com/pinokiofactory/Nari-Dia-TTS/commit/e5b630df297c7f47f6c518a00d6c3f44be4e25b5) \| [13](https://github.com/pinokiofactory/Nari-Dia-TTS/blob/e5b630df297c7f47f6c518a00d6c3f44be4e25b5/dia/audio.py#L13) \| int32 \| dtype declaration \| delay_arr = torch.tensor(delay_pattern, dtype=torch.int32) \|` |
| [quantization.md](../analysis/quantization.md) | *42 more rows omitted* |
| [fusion.md](../analysis/fusion.md) | `\| Fused activation (`GELU(approximate='tanh')`, SiLU) \| 3 \| Allegro-txt2vid, Nari-Dia-TTS, diffusers-image-fill \|` |
| [fusion.md](../analysis/fusion.md) | `\| [Nari-Dia-TTS](https://github.com/pinokiofactory/Nari-Dia-TTS) \| [e5b630d](https://github.com/pinokiofactory/Nari-Dia-TTS/commit/e5b630df297c7f47f6c518a00d6c3f44be4e25b5) \| [dia/model.py:341](https://github.com/pinokiofactory/Nari-Dia-TTS/blob/e5b630df297c7f47f6c518a00d6c3f44be4e25b5/dia/model.py#L341) \| Direct `torch.compile(..., mode='default')` on the decoder decode step \|` |
| [fusion.md](../analysis/fusion.md) | `\| [Nari-Dia-TTS](https://github.com/pinokiofactory/Nari-Dia-TTS) \| [e5b630d](https://github.com/pinokiofactory/Nari-Dia-TTS/commit/e5b630df297c7f47f6c518a00d6c3f44be4e25b5) \| [app.py:155](https://github.com/pinokiofactory/Nari-Dia-TTS/blob/e5b630df297c7f47f6c518a00d6c3f44be4e25b5/app.py#L155) \| `use_torch_compile=False # Keep False for Gradio stability` — compile available but disabled in the shipped app \|` |
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
- [App flow graph](../flows/Nari-Dia-TTS.md)
<!-- cross-analysis:end -->
