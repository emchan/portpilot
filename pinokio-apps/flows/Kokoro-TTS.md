# Matrix-multiply flow — Kokoro-TTS

Companion to [`results/pinokio-apps.md`](../results/pinokio-apps.md) and [`analysis/flows.md`](../analysis/flows.md). Interactive viewer: [`Kokoro-TTS.html`](Kokoro-TTS.html).

**Models whose checkpoints were analysed:** [hexgrad/Kokoro-82M](https://huggingface.co/hexgrad/Kokoro-82M)

No safetensors checkpoint was pulled by this launcher, so no weight-level matrix-multiply graph can be reconstructed. Launcher code may still call framework matmuls; any local source evidence is listed below.

No explicit matmul/attention call was found in the vendored Python source.

## Snapdragon note
- Deep scan: cuda=12, torch=37, xformers=2, directml=1. Contains CUDA/Triton/TensorRT signals; Snapdragon path requires replacement or ONNX conversion.
