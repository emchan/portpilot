# Matrix-multiply flow — RMBG-2-Studio

Companion to [`results/pinokio-apps.md`](../results/pinokio-apps.md) and [`analysis/flows.md`](../analysis/flows.md). Interactive viewer: [`RMBG-2-Studio.html`](RMBG-2-Studio.html).

**Models whose checkpoints were analysed:** [briaai/RMBG-2.0](https://huggingface.co/briaai/RMBG-2.0)

No safetensors checkpoint was pulled by this launcher, so no weight-level matrix-multiply graph can be reconstructed. Launcher code may still call framework matmuls; any local source evidence is listed below.

No explicit matmul/attention call was found in the vendored Python source.

## Snapdragon note
- Deep scan: torch=21, xformers=2, mps=1, directml=1. Unsuitable (MLX/Apple-only runtime) for Snapdragon unless ported to CPU/ONNX.
