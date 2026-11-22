# Matrix-multiply flow — flashdiffusion

Companion to [`results/pinokio-apps.md`](../results/pinokio-apps.md) and [`analysis/flows.md`](../analysis/flows.md). Interactive viewer: [`flashdiffusion.html`](flashdiffusion.html).

**Models:** none could be identified from this launcher's snapshots.

No safetensors checkpoint was pulled by this launcher, so no weight-level matrix-multiply graph can be reconstructed. Launcher code may still call framework matmuls; any local source evidence is listed below.

No explicit matmul/attention call was found in the vendored Python source.

## Snapdragon note
- Deep scan: torch=12, xformers=3, directml=1. No Python GEMM in wrapper; Snapdragon CPU-ready as launcher/wrapper (no model port).
