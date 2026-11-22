# Matrix-multiply flow — macOS-use

Companion to [`results/pinokio-apps.md`](../results/pinokio-apps.md) and [`analysis/flows.md`](../analysis/flows.md). Interactive viewer: [`macOS-use.html`](macOS-use.html).

**Models:** none could be identified from this launcher's snapshots.

No safetensors checkpoint was pulled by this launcher, so no weight-level matrix-multiply graph can be reconstructed. Launcher code may still call framework matmuls; any local source evidence is listed below.

No explicit matmul/attention call was found in the vendored Python source.

## Snapdragon note
- Deep scan: no CUDA/MLX signals. No CUDA signals; feasible on Snapdragon CPU via ARM64 wheels; GPU/NPU only via ONNX conversion.
