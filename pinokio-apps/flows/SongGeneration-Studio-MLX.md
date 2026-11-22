# Matrix-multiply flow — SongGeneration-Studio-MLX

Companion to [`results/pinokio-apps.md`](../results/pinokio-apps.md) and [`analysis/flows.md`](../analysis/flows.md). Interactive viewer: [`SongGeneration-Studio-MLX.html`](SongGeneration-Studio-MLX.html).

**Models whose checkpoints were analysed:** [AITRADER/SongGeneration-Large-MLX](https://huggingface.co/AITRADER/SongGeneration-Large-MLX)

No safetensors checkpoint was pulled by this launcher, so no weight-level matrix-multiply graph can be reconstructed. Launcher code may still call framework matmuls; any local source evidence is listed below.

No explicit matmul/attention call was found in the vendored Python source.

## Snapdragon note
- Deep scan: mlx=17. Unsuitable (MLX/Apple-only runtime) for Snapdragon unless ported to CPU/ONNX.
