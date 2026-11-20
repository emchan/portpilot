# Matrix-multiply flow — diffusers-image-fill

Companion to [`results/pinokio-apps.md`](../results/pinokio-apps.md) and [`analysis/flows.md`](../analysis/flows.md). Interactive viewer: [`diffusers-image-fill.html`](diffusers-image-fill.html).

**Models:** none could be identified from this launcher's snapshots.

No safetensors checkpoint was pulled by this launcher, so no weight-level matrix-multiply graph can be reconstructed. Launcher code may still call framework matmuls; any local source evidence is listed below.

## Local source evidence

| File | Line | Evidence |
| --- | --- | --- |
| controlnet_union.py | [controlnet_union.py:76](https://github.com/pinokiofactory/diffusers-image-fill/blob/a8b6497483d956df7ca1ffc882bf29af03476a26/controlnet_union.py#L76) | ("c_fc", nn.Linear(d_model, d_model * 4)), |
| controlnet_union.py | [controlnet_union.py:78](https://github.com/pinokiofactory/diffusers-image-fill/blob/a8b6497483d956df7ca1ffc882bf29af03476a26/controlnet_union.py#L78) | ("c_proj", nn.Linear(d_model * 4, d_model)), |
| controlnet_union.py | [controlnet_union.py:356](https://github.com/pinokiofactory/diffusers-image-fill/blob/a8b6497483d956df7ca1ffc882bf29af03476a26/controlnet_union.py#L356) | self.encoder_hid_proj = nn.Linear(encoder_hid_dim, cross_attention_dim) |
| controlnet_union.py | [controlnet_union.py:460](https://github.com/pinokiofactory/diffusers-image-fill/blob/a8b6497483d956df7ca1ffc882bf29af03476a26/controlnet_union.py#L460) | nn.Linear(num_trans_channel, num_proj_channel) |
| pipeline_fill_sd_xl.py | [pipeline_fill_sd_xl.py:40](https://github.com/pinokiofactory/diffusers-image-fill/blob/a8b6497483d956df7ca1ffc882bf29af03476a26/pipeline_fill_sd_xl.py#L40) | rgb_tensor = torch.einsum( |
