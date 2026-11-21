# factory — portability analysis

- **Package name:** factory (`factory`)
- **Description:** No description provided in the repository.
- **Original git URL:** https://github.com/pinokiofactory/factory
- **Analyzed commit:** N/A (empty repository)
- **Platforms supported:** N/A (empty repository)
- **Porting difficulty:** N/A (empty repository)
- **CUDA-only packages:** —

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

No package dependencies were declared in the repository. Installers that only run `npm install` or clone another app do not name packages here.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 0
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- Difficulty score: 0 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- Empty repository; no install, dependency, or runtime test possible.
- Result: **N/A (empty repository).**

## CPU port attempt

- **Attempt order:** #100 of 101 (by porting effort, easiest first).
- **Status:** N/A (empty).
- **Changes applied / required:** none — empty repository.
- **Smoke check:** n/a (no Python source in snapshot).
- **Blockers:** empty repository.
- **Scope note:** static portability review of the Pinokio wrapper; no install or model download was executed.
<!-- cross-analysis:start -->
## Cross-analysis details

- **CPU category (cpu.md):** Unclassified in cpu.md
- **TPU suitability:** N/A - empty repository
- **TPU work needed:** Empty repository; no runtime to port
- **Effort ranking (effort.md):** #100 — N/A
- **Effort blockers:** Empty repository
- **Precisions noted:** unspecified
- **Models/flows noted:** —
- **Flow graph:** [flows/factory.md](../flows/factory.md)

### Snapshot verification (cloned analyzed commit)

- **Snapshot source:** `https://codeload.github.com/pinokiofactory/factory/tar.gz/<analyzed commit>` extracted to `/tmp/opencode/pinokio-snapshots/factory`
- **Files scanned:** 0 total (0 .py, 0 .js, 0 other)
- **Key files present:** none of the common launcher files found
- **TPU/CUDA-relevant signals:** none detected by text scan (still inspect runtime behavior before porting)

### Evidence from analysis files

| Source | Evidence |
|---|---|
| [kernels.md](../analysis/kernels.md) | No per-repo kernel table row matched; see kernels.md for global signals. |
| [quantization.md](../analysis/quantization.md) | No per-repo quantization table row matched; see quantization.md. |
| [fusion.md](../analysis/fusion.md) | `\| [Nari-Dia-TTS](https://github.com/pinokiofactory/Nari-Dia-TTS) \| [e5b630d](https://github.com/pinokiofactory/Nari-Dia-TTS/commit/e5b630df297c7f47f6c518a00d6c3f44be4e25b5) \| [dia/model.py:341](https://github.com/pinokiofactory/Nari-Dia-TTS/blob/e5b630df297c7f47f6c518a00d6c3f44be4e25b5/dia/model.py#L341) \| Direct `torch.compile(..., mode='default')` on the decoder decode step \|` |
| [fusion.md](../analysis/fusion.md) | `\| [Nari-Dia-TTS](https://github.com/pinokiofactory/Nari-Dia-TTS) \| [e5b630d](https://github.com/pinokiofactory/Nari-Dia-TTS/commit/e5b630df297c7f47f6c518a00d6c3f44be4e25b5) \| [app.py:155](https://github.com/pinokiofactory/Nari-Dia-TTS/blob/e5b630df297c7f47f6c518a00d6c3f44be4e25b5/app.py#L155) \| `use_torch_compile=False # Keep False for Gradio stability` — compile available but disabled in the shipped app \|` |
| [fusion.md](../analysis/fusion.md) | `\| [hunyuanvideo](https://github.com/pinokiofactory/hunyuanvideo) \| [c65cb77](https://github.com/pinokiofactory/hunyuanvideo/commit/c65cb772466eea61e0a330f52ed7764a9d4e821d) \| [start.js:19](https://github.com/pinokiofactory/hunyuanvideo/blob/c65cb772466eea61e0a330f52ed7764a9d4e821d/start.js#L19) \| Launcher forwards `--compile` to the upstream Gradio server \|` |
| [models.md](../analysis/models.md) | No model pull/shape row matched in models.md. |
| [cpu.md](../analysis/cpu.md) | CPU category: **Unclassified in cpu.md** |
| [tpu.md](../analysis/tpu.md) | TPU suitability: **N/A - empty repository** — Empty repository; no runtime to port |

### Related analysis

- [CPU analysis](../analysis/cpu.md)
- [TPU analysis](../analysis/tpu.md)
- [Effort ranking](../analysis/effort.md)
- [Kernel evidence](../analysis/kernels.md)
- [Quantization evidence](../analysis/quantization.md)
- [Fusion evidence](../analysis/fusion.md)
- [Model pulls/shapes](../analysis/models.md)
- [Flow graphs](../analysis/flows.md)
- [App flow graph](../flows/factory.md)
<!-- cross-analysis:end -->
