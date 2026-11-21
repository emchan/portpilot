# mcp — portability analysis

- **Package name:** MCP (`mcp`)
- **Description:** Model Context Protocol https://modelcontextprotocol.io/introduction
- **Original git URL:** https://github.com/pinokiofactory/mcp
- **Analyzed commit:** `01d5096c5ab4d4aaec70a074896c281fd204f8f5`
- **Platforms supported:** Cross-platform
- **Porting difficulty:** Low
- **CUDA-only packages:** —

## Dependencies (from `requirements*.txt` / `install.js` / `torch.js`)

No package dependencies were declared in the repository. Installers that only run `npm install` or clone another app do not name packages here.

## CUDA footprint

- **Number of CUDA kernels:** 0
- **Lines of CUDA code:** 0
- **Lines of non-CUDA code:** 616
- **CUDA-related functions used:** None found in this repository

## Evidence and notes

- `torch.js` routes present: none.
- No CUDA kernels in the wrapper repository; compute is delegated to the upstream app or PyTorch wheels.
- Difficulty score: 0.0 (heuristic; see the methodology in [pinokio-apps.md](pinokio-apps.md#method-and-limitations)).

## CPU test run (2026-11-21)

- All 21 JS files pass node --check. Configuration-only Pinokio app; no runtime test possible without Pinokio/Claude Desktop.
- Result: **static/environment-limited verification only.**

## CPU port attempt

- **Attempt order:** #8 of 101 (by porting effort, easiest first).
- **Status:** CPU-ready (no changes).
- **Changes applied / required:** no change required (no local GEMM workload); add a CPU wheel branch / remove GPU-only wheel pins.
- **Smoke check:** n/a (no Python source in snapshot).
- **Blockers:** none identified.
- **Scope note:** static portability review of the Pinokio wrapper; no install or model download was executed.
