# Matrix-multiply flow — Ultimate-TTS-Studio

Companion to [`results/pinokio-apps.md`](../results/pinokio-apps.md) and [`analysis/flows.md`](../analysis/flows.md). Interactive viewer: [`Ultimate-TTS-Studio.html`](Ultimate-TTS-Studio.html).

**Models whose checkpoints were analysed:** [cocktailpeanut/oa](https://huggingface.co/cocktailpeanut/oa)

No safetensors checkpoint was pulled by this launcher, so no weight-level matrix-multiply graph can be reconstructed. Launcher code may still call framework matmuls; any local source evidence is listed below.

No explicit matmul/attention call was found in the vendored Python source.

## Snapdragon note
- Deep scan: torch=12, triton=3, xformers=1, sageattention=2, directml=1, onnxruntime-gpu=1. Contains CUDA/Triton/TensorRT signals; Snapdragon path requires replacement or ONNX conversion.
