# Matrix-multiply flow — yue

Companion to [`results/pinokio-apps.md`](../results/pinokio-apps.md) and [`analysis/flows.md`](../analysis/flows.md). Interactive viewer: [`yue.html`](yue.html).

**Models whose checkpoints were analysed:** [m-a-p/xcodec_mini_infer](https://huggingface.co/m-a-p/xcodec_mini_infer)

No safetensors checkpoint was pulled by this launcher, so no weight-level matrix-multiply graph can be reconstructed. Launcher code may still call framework matmuls; any local source evidence is listed below.

No explicit matmul/attention call was found in the vendored Python source.

## Snapdragon note
- Deep scan: torch=10, triton=5, xformers=5. Contains CUDA/Triton/TensorRT signals; Snapdragon path requires replacement or ONNX conversion.
