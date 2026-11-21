# vibevoice-realtime — portability analysis

- **Package name:** VibeVoice Realtime (`vibevoice-realtime`)
- **Description:** Realtime streaming TTS demo using microsoft/VibeVoice-Realtime-0.5B
- **Original git URL:** https://github.com/pinokiofactory/vibevoice-realtime
- **Analyzed commit:** `e8f4b7bd22f65e45b19cd4e67cd0c1a982109102`
- **Platforms supported:** NVIDIA / AMD / Mac
- **Porting difficulty:** Low
- **CUDA-only packages:** —

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

numpy, torch, torch-directml, torchaudio, torchvision

Wheel indexes referenced: cpu, cu128, rocm6.3.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 320
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- `torch.js` routes present: nvidia, amd, mac, cpu.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Difficulty score: 0.0 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-20)

- Downloaded upstream `microsoft/VibeVoice`; installed CPU torch and package.
- First run failed on `torch.load(..., weights_only=True)` for cached voice presets.
- Patched `demo/web/app.py` to `weights_only=False`; demo then started on `http://0.0.0.0:3000`.
- Result: **CPU port works with a source patch.**

## CPU port attempt

- **Attempt order:** #12 of 101 (by porting effort, easiest first).
- **Status:** CPU-capable (shipped fallback).
- **Changes applied / required:** use existing CPU wheel branch in torch.js; use existing non-GPU launcher route; keep explicit device='cpu' branch; tune oneDNN/MKL threads for FP16/BF16 GEMMs.
- **Smoke check:** n/a (no Python source in snapshot).
- **Blockers:** none identified.
- **Scope note:** static portability review of the Pinokio wrapper; no install or model download was executed.
<!-- cross-analysis:start -->
## Cross-analysis details

- **CPU category (cpu.md):** CPU-capable with shipped fallback
- **TPU suitability:** Possible - moderate port
- **TPU work needed:** large BF16/FP16 GEMM workload; expect XLA compile/memory tuning; moderate device/kernel/runtime adaptation
- **Effort ranking (effort.md):** #12 — Low
- **Effort blockers:** large FP16/BF16 GEMM load
- **Precisions noted:** BF16, INT16
- **Models/flows noted:** [microsoft/VibeVoice-Realtime-0.5B](https://huggingface.co/microsoft/VibeVoice-Realtime-0.5B)
- **Flow graph:** [flows/vibevoice-realtime.md](../flows/vibevoice-realtime.md)

### Snapshot verification (cloned analyzed commit)

- **Snapshot source:** `https://codeload.github.com/pinokiofactory/vibevoice-realtime/tar.gz/<analyzed commit>` extracted to `/tmp/opencode/pinokio-snapshots/vibevoice-realtime`
- **Files scanned:** 10 total (0 .py, 6 .js, 4 other)
- **Key files present:** pinokio.js, install.js, torch.js, start.js
- **TPU/CUDA-relevant signals:**
  - `directml`: 1 match(es) (e.g. torch.js:34)
  - `mps`: 1 match(es) (e.g. start.js:10)

### Evidence from analysis files

| Source | Evidence |
|---|---|
| [kernels.md](../analysis/kernels.md) | `\| [vibevoice-realtime](https://github.com/pinokiofactory/vibevoice-realtime) \| [e8f4b7b](https://github.com/pinokiofactory/vibevoice-realtime/commit/e8f4b7bd22f65e45b19cd4e67cd0c1a982109102) \| optional flag + env/config flag \| [start.js:10](https://github.com/pinokiofactory/vibevoice-realtime/blob/e8f4b7bd22f65e45b19cd4e67cd0c1a982109102/start.js#L10) — MODEL_DEVICE: "{{gpu === 'apple' ? 'mps' : (gpu === 'nvidia' ? 'cuda' : 'cpu')}}" \|` |
| [quantization.md](../analysis/quantization.md) | `\| [vibevoice-realtime](https://github.com/pinokiofactory/vibevoice-realtime) \| [e8f4b7b](https://github.com/pinokiofactory/vibevoice-realtime/commit/e8f4b7bd22f65e45b19cd4e67cd0c1a982109102) \| [112](https://github.com/pinokiofactory/vibevoice-realtime/blob/e8f4b7bd22f65e45b19cd4e67cd0c1a982109102/README.md#L112) \| int16 \| checkpoint / config \| // Binary audio chunk (Int16 PCM at 24 kHz) \|` |
| [fusion.md](../analysis/fusion.md) | No direct fusion table row matched; see fusion.md for global context. |
| [models.md](../analysis/models.md) | No model pull/shape row matched in models.md. |
| [cpu.md](../analysis/cpu.md) | CPU category: **CPU-capable with shipped fallback** |
| [tpu.md](../analysis/tpu.md) | TPU suitability: **Possible - moderate port** — large BF16/FP16 GEMM workload; expect XLA compile/memory tuning; moderate device/kernel/runtime adaptation |

### Related analysis

- [CPU analysis](../analysis/cpu.md)
- [TPU analysis](../analysis/tpu.md)
- [Effort ranking](../analysis/effort.md)
- [Kernel evidence](../analysis/kernels.md)
- [Quantization evidence](../analysis/quantization.md)
- [Fusion evidence](../analysis/fusion.md)
- [Model pulls/shapes](../analysis/models.md)
- [Flow graphs](../analysis/flows.md)
- [App flow graph](../flows/vibevoice-realtime.md)
<!-- cross-analysis:end -->
