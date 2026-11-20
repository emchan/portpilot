# Matrix-multiply flow — liveportrait

Companion to [`results/pinokio-apps.md`](../results/pinokio-apps.md) and [`analysis/flows.md`](../analysis/flows.md). Interactive viewer: [`liveportrait.html`](liveportrait.html).

**Models whose checkpoints were analysed:** [KwaiVGI/LivePortrait](https://huggingface.co/KwaiVGI/LivePortrait), [cleardusk/LivePortrait-Windows](https://huggingface.co/cleardusk/LivePortrait-Windows)

No safetensors checkpoint was pulled by this launcher, so no weight-level matrix-multiply graph can be reconstructed. Launcher code may still call framework matmuls; any local source evidence is listed below.

No explicit matmul/attention call was found in the vendored Python source.
