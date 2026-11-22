# Matrix-multiply flow — hertz

Companion to [`results/pinokio-apps.md`](../results/pinokio-apps.md) and [`analysis/flows.md`](../analysis/flows.md). Interactive viewer: [`hertz.html`](hertz.html).

**Models:** none could be identified from this launcher's snapshots.

No safetensors checkpoint was pulled by this launcher, so no weight-level matrix-multiply graph can be reconstructed. Launcher code may still call framework matmuls; any local source evidence is listed below.

No explicit matmul/attention call was found in the vendored Python source.

## Snapdragon note
- Deep scan: cuda=5, torch=19, xformers=1, mps=1, directml=1. Contains CUDA/Triton/TensorRT signals; Snapdragon path requires replacement or ONNX conversion.
