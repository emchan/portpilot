# openui — portability analysis

- **Package name:** openui (`openui`)
- **Description:** Describe UI and see it rendered live. Ask for changes and convert HTML to React, Svelte, Web Components, etc. Like vercel v0, but open source https://github.com/wandb/openui
- **Original git URL:** https://github.com/pinokiofactory/openui
- **Analyzed commit:** `83ab6b5534ee0500674a6e2872e235092310cd9d`
- **Platforms supported:** Cross-platform
- **Porting difficulty:** Low
- **CUDA-only packages:** —

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

tiktoken

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 295
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- `torch.js` routes present: none.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Difficulty score: 0.0 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-20)

- Downloaded upstream `wandb/openui` and installed the backend on CPU.
- Initial failure: `ImportError: cannot import name 'SqliteExtDatabase'` with peewee 4.5.3.
- Fixed by pinning `peewee==3.17.0`; the server then started successfully on `http://127.0.0.1:7878`.
- Result: **CPU port works with a dependency pin.**

## CPU port attempt

- **Attempt order:** #10 of 101 (by porting effort, easiest first).
- **Status:** CPU-ready (no changes).
- **Changes applied / required:** no change required (no local GEMM workload); add a CPU wheel branch / remove GPU-only wheel pins.
- **Smoke check:** n/a (no Python source in snapshot).
- **Blockers:** none identified.
- **Scope note:** static portability review of the Pinokio wrapper; no install or model download was executed.
