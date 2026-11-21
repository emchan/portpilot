# mlx-video-ui — portability analysis

- **Package name:** MLX Video UI (`mlx-video-ui`)
- **Description:** Local UI for MLX Video (Next.js frontend + FastAPI backend).
- **Original git URL:** https://github.com/pinokiofactory/mlx-video-ui
- **Analyzed commit:** `2f91ff7c3749a11dfcb3ed3e555a375cb5400421`
- **Platforms supported:** Mac (Apple Silicon) only
- **Porting difficulty:** Low
- **CUDA-only packages:** —

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

mlx-video, ok, printmlx-video

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 652
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- `torch.js` routes present: none.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Difficulty score: 1.0 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- requires MLX/Apple Silicon and Python 3.11; not runnable on this Linux CPU container.
- Result: **not runnable in this container.**

## CPU port attempt

- **Attempt order:** #65 of 101 (by porting effort, easiest first).
- **Status:** Blocked (Apple-only).
- **Changes applied / required:** no change identified.
- **Smoke check:** n/a (no Python source in snapshot).
- **Blockers:** Apple-silicon-only MLX runtime.
- **Scope note:** static portability review of the Pinokio wrapper; no install or model download was executed.
<!-- cross-analysis:start -->
## Cross-analysis details

- **CPU category (cpu.md):** Apple-silicon-only runtime
- **TPU suitability:** Unsuitable - Apple MLX-only runtime
- **TPU work needed:** MLX/Apple-silicon runtime; not a PyTorch/XLA TPU target
- **Effort ranking (effort.md):** #65 — Medium–high
- **Effort blockers:** Apple-silicon-only MLX runtime
- **Precisions noted:** unspecified
- **Models/flows noted:** —
- **Flow graph:** [flows/mlx-video-ui.md](../flows/mlx-video-ui.md)

### Snapshot verification (cloned analyzed commit)

- **Snapshot source:** `https://codeload.github.com/pinokiofactory/mlx-video-ui/tar.gz/<analyzed commit>` extracted to `/tmp/opencode/pinokio-snapshots/mlx-video-ui`
- **Files scanned:** 13 total (0 .py, 8 .js, 5 other)
- **Key files present:** pinokio.js, install.js, start.js
- **TPU/CUDA-relevant signals:**
  - `mlx`: 32 match(es) (e.g. pinokio.json:2, pinokio.json:3)

### Evidence from analysis files

| Source | Evidence |
|---|---|
| [kernels.md](../analysis/kernels.md) | No per-repo kernel table row matched; see kernels.md for global signals. |
| [quantization.md](../analysis/quantization.md) | `\| [mlx-video-ui](https://github.com/pinokiofactory/mlx-video-ui) \| env/config flag \| `backend.js:39` — // Default to runtime quantization for stability (avoid broken pre-quant snapshots).<br>`backend.js:41` — //   LTX_USE_PREQUANT=1 \|` |
| [quantization.md](../analysis/quantization.md) | `\| [mlx-video-ui](https://github.com/pinokiofactory/mlx-video-ui) \| env/config flag \| `backend.js:39` — // Default to runtime quantization for stability (avoid broken pre-quant snapshots).<br>`backend.js:41` — //   LTX_USE_PREQUANT=1<br>`backend.js:42` — //   LTX_ALLOW_UNSAFE_PREQUANT=1<br>`backend.js:43` — LTX_USE_PREQUANT: "{{envs.LTX_USE_PREQUANT \\|\\| '0'}}",<br>`backend.js:44` — LTX_ALLOW_UNSAFE_PREQUANT: "{{envs.LTX_ALLOW_UNSAFE_PREQUANT \\|\\| '0'}}",<br>`backend.js:45` — LTX_FORCE_RUNTIME_QUANT: "{{envs.LTX_FORCE_RUNTIME_QUANT \\|\\| '1'}}", \|` |
| [fusion.md](../analysis/fusion.md) | No direct fusion table row matched; see fusion.md for global context. |
| [models.md](../analysis/models.md) | No model pull/shape row matched in models.md. |
| [cpu.md](../analysis/cpu.md) | CPU category: **Apple-silicon-only runtime** |
| [tpu.md](../analysis/tpu.md) | TPU suitability: **Unsuitable - Apple MLX-only runtime** — MLX/Apple-silicon runtime; not a PyTorch/XLA TPU target |

### Related analysis

- [CPU analysis](../analysis/cpu.md)
- [TPU analysis](../analysis/tpu.md)
- [Effort ranking](../analysis/effort.md)
- [Kernel evidence](../analysis/kernels.md)
- [Quantization evidence](../analysis/quantization.md)
- [Fusion evidence](../analysis/fusion.md)
- [Model pulls/shapes](../analysis/models.md)
- [Flow graphs](../analysis/flows.md)
- [App flow graph](../flows/mlx-video-ui.md)
<!-- cross-analysis:end -->
