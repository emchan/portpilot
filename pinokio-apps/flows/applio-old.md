# Matrix-multiply flow — applio-old

Companion to [`results/pinokio-apps.md`](../results/pinokio-apps.md) and [`analysis/flows.md`](../analysis/flows.md). Interactive viewer: [`applio-old.html`](applio-old.html).

**Models whose checkpoints were analysed:** [IAHispano/Applio](https://huggingface.co/IAHispano/Applio)

No safetensors checkpoint was pulled by this launcher, so no weight-level matrix-multiply graph can be reconstructed. Launcher code may still call framework matmuls; any local source evidence is listed below.

No explicit matmul/attention call was found in the vendored Python source.
