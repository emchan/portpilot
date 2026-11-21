# ACE-Step — portability analysis

- **Package name:** ACE-Step (`ACE-Step`)
- **Description:** A Step Towards Music Generation Foundation Model
- **Original git URL:** https://github.com/pinokiofactory/ACE-Step
- **Analyzed commit:** `8cf2fac2765b1383e6d078b399acc3e38374949e`
- **Platforms supported:** NVIDIA only
- **Porting difficulty:** High
- **CUDA-only packages:** triton, triton-windows, xformers *(optional)*

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

gradio, peft, torch, torchaudio, torchcodec, torchvision, triton, triton-windows, xformers

Wheel indexes referenced: cu128.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 245
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- `torch.js` routes present: nvidia.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Optional (user-enabled only): xformers
- Difficulty score: 9.0 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- blocked by matplotlib build failure on Python 3.14.
- Result: **not runnable in this container.**
<!-- cross-analysis:start -->
## Cross-analysis details

- **CPU category (cpu.md):** CPU possible, but launcher must change
- **TPU suitability:** Difficult - significant port
- **TPU work needed:** replace CUDA attention kernels with TPU-compatible attention/SDPA/XLA; add TPU launcher/runtime branch; multiple CUDA-specific dependencies or large model/dtype constraints
- **Effort ranking (effort.md):** #88 — Very high
- **Effort blockers:** no CPU/AMD launcher branch; GPU-only attention: triton/triton-windows/xformers; CUDA-only fused kernels need config change
- **Precisions noted:** unspecified
- **Models/flows noted:** —
- **Flow graph:** [flows/ACE-Step.md](../flows/ACE-Step.md)

### Snapshot verification (cloned analyzed commit)

- **Snapshot source:** `https://codeload.github.com/pinokiofactory/ACE-Step/tar.gz/<analyzed commit>` extracted to `/tmp/opencode/pinokio-snapshots/ACE-Step`
- **Files scanned:** 10 total (0 .py, 7 .js, 3 other)
- **Key files present:** pinokio.js, install.js, torch.js, start.js
- **TPU/CUDA-relevant signals:**
  - `xformers`: 6 match(es) (e.g. torch.js:12, torch.js:12)
  - `sageattention`: 2 match(es) (e.g. install.js:35, install.js:35)
  - `triton`: 4 match(es) (e.g. torch.js:14, torch.js:30)

### Evidence from analysis files

| Source | Evidence |
|---|---|
| [kernels.md](../analysis/kernels.md) | `\| [ACE-Step](https://github.com/pinokiofactory/ACE-Step) \| [8cf2fac](https://github.com/pinokiofactory/ACE-Step/commit/8cf2fac2765b1383e6d078b399acc3e38374949e) \| launcher install \| install.js, torch.js \| [torch.js:14](https://github.com/pinokiofactory/ACE-Step/blob/8cf2fac2765b1383e6d078b399acc3e38374949e/torch.js#L14) — "uv pip install triton-windows==3.3.1.post19" \|` |
| [kernels.md](../analysis/kernels.md) | `\| [ACE-Step](https://github.com/pinokiofactory/ACE-Step) \| [8cf2fac](https://github.com/pinokiofactory/ACE-Step/commit/8cf2fac2765b1383e6d078b399acc3e38374949e) \| mention/hint \| [install.js:35](https://github.com/pinokiofactory/ACE-Step/blob/8cf2fac2765b1383e6d078b399acc3e38374949e/install.js#L35) — // sageattention: true   // uncomment this line if your project requires sageattention \|` |
| [quantization.md](../analysis/quantization.md) | No per-repo quantization table row matched; see quantization.md. |
| [fusion.md](../analysis/fusion.md) | `\| [ACE-Step](https://github.com/pinokiofactory/ACE-Step) \| [8cf2fac](https://github.com/pinokiofactory/ACE-Step/commit/8cf2fac2765b1383e6d078b399acc3e38374949e) \| commented-out flag \| [install.js:35](https://github.com/pinokiofactory/ACE-Step/blob/8cf2fac2765b1383e6d078b399acc3e38374949e/install.js#L35) — `// sageattention: true // uncomment this line if your project requires sageattention` \|` |
| [models.md](../analysis/models.md) | No model pull/shape row matched in models.md. |
| [cpu.md](../analysis/cpu.md) | CPU category: **CPU possible, but launcher must change** |
| [tpu.md](../analysis/tpu.md) | TPU suitability: **Difficult - significant port** — replace CUDA attention kernels with TPU-compatible attention/SDPA/XLA; add TPU launcher/runtime branch; multiple CUDA-specific dependencies or large model/dtype constraints |

### Related analysis

- [CPU analysis](../analysis/cpu.md)
- [TPU analysis](../analysis/tpu.md)
- [Effort ranking](../analysis/effort.md)
- [Kernel evidence](../analysis/kernels.md)
- [Quantization evidence](../analysis/quantization.md)
- [Fusion evidence](../analysis/fusion.md)
- [Model pulls/shapes](../analysis/models.md)
- [Flow graphs](../analysis/flows.md)
- [App flow graph](../flows/ACE-Step.md)
<!-- cross-analysis:end -->
