# Hugging Face models pulled by Pinokio apps

Companion to [`results/pinokio-apps.md`](../results/pinokio-apps.md).

Scanned all 101 Pinokio Factory repository snapshots for Hugging Face model pulls (manifest `repo`/`uri` fields, `hf download`, `snapshot_download`, `from_pretrained`, and `huggingface.co` URLs). Found **90 distinct model repositories** used by **33 apps**. Three non-model repositories (wheel hosts/attention wheel downloads) were excluded.

**Precision** is read from the model's own safetensors header JSON where possible: the launcher-requested `.safetensors` file is fetched with an HTTP Range request, its header parsed, and parameter counts computed from each tensor's dtype and shape. This is exact for the file actually pulled. Where the launcher names no file or the repo is gated, Hugging Face's aggregated `safetensors` metadata is used instead (marked *repo aggregate*), and where neither is available the older filename/config inference is kept. Percentages are by parameter count; small integer tensors used for indices/metadata are excluded from the precision labels.

## Summary

| Format | Models |
| --- | --- |
| Other / unspecified | 53 |
| PyTorch | 34 |
| GGUF | 3 |

| Precision source | Models |
| --- | --- |
| safetensors header | 65 |
| filename / config | 23 |
| HF repo metadata | 2 |

| Default precision (dominant tensor dtype) | Models |
| --- | --- |
| FP16 | 21 |
| unspecified | 19 |
| FP32 | 18 |
| BF16 | 17 |
| FP8 (E4M3FN) | 8 |
| INT8 | 2 |
| INT4/qint4 | 2 |
| UINT8 | 1 |
| NF4 | 1 |
| INT8/qint8 | 1 |

**16 models contain tensors in more than one precision** (each dtype holding ≥0.1% of parameters). For those, the table below and the detail section list every dtype rather than a single value. Note that NF4/INT4 weights are stored as packed `UINT8` tensors in safetensors headers, so the label reflects both.

## Models

| Model | Projects | Format | Precision (tensor dtypes) | Files requested | Evidence |
| --- | --- | --- | --- | --- | --- |
| [AlexWortega/RIFE](https://huggingface.co/AlexWortega/RIFE) | [Allegro-txt2vid](https://github.com/pinokiofactory/Allegro-txt2vid), [Allegro-txt2vid-install](https://github.com/pinokiofactory/Allegro-txt2vid-install), [cogstudio](https://github.com/pinokiofactory/cogstudio) | Other / unspecified | unspecified | — | [Allegro-txt2vid](https://github.com/pinokiofactory/Allegro-txt2vid): [gradio_app.py:426](https://github.com/pinokiofactory/Allegro-txt2vid/blob/f8327e3172834ee8d932d7284641a5e9a0065cbc/gradio_app.py#L426)<br>[Allegro-txt2vid-install](https://github.com/pinokiofactory/Allegro-txt2vid-install): [README.md:7](https://github.com/pinokiofactory/Allegro-txt2vid-install/blob/6000ff1e395f6238eaa89e68b45a571e84d324e1/README.md#L7)<br>[cogstudio](https://github.com/pinokiofactory/cogstudio): [cogstudio.py:43](https://github.com/pinokiofactory/cogstudio/blob/7dfb014a636513c5b42de070c43e285c9bf7cce7/cogstudio.py#L43) |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | [comfy](https://github.com/pinokiofactory/comfy), [forge](https://github.com/pinokiofactory/forge), [stable-diffusion-webui-forge](https://github.com/pinokiofactory/stable-diffusion-webui-forge) | PyTorch | FP16 100.0% | `svd_xt_1_1.safetensors` | [comfy](https://github.com/pinokiofactory/comfy): [download-svd-xt-1.1.json:7](https://github.com/pinokiofactory/comfy/blob/ba110479f88835d64c603044c2fe69102833fa55/download-svd-xt-1.1.json#L7)<br>[forge](https://github.com/pinokiofactory/forge): [download-svd-xt-1.1.json:5](https://github.com/pinokiofactory/forge/blob/e3378c35f7f1c4fec2f600c33b9d17ab6d330b4c/download-svd-xt-1.1.json#L5)<br>[stable-diffusion-webui-forge](https://github.com/pinokiofactory/stable-diffusion-webui-forge): [download-svd-xt-1.1.json:5](https://github.com/pinokiofactory/stable-diffusion-webui-forge/blob/e44fda22458c495919a1c90ed9e7d5c63c37adfb/download-svd-xt-1.1.json#L5) |
| [latent-consistency/lcm-lora-sdxl](https://huggingface.co/latent-consistency/lcm-lora-sdxl) | [comfy](https://github.com/pinokiofactory/comfy), [forge](https://github.com/pinokiofactory/forge), [stable-diffusion-webui-forge](https://github.com/pinokiofactory/stable-diffusion-webui-forge) | PyTorch | FP16 100.0% | `pytorch_lora_weights.safetensors` | [comfy](https://github.com/pinokiofactory/comfy): [download-lcm-lora.json:7](https://github.com/pinokiofactory/comfy/blob/ba110479f88835d64c603044c2fe69102833fa55/download-lcm-lora.json#L7)<br>[forge](https://github.com/pinokiofactory/forge): [download-lcm-lora.json:5](https://github.com/pinokiofactory/forge/blob/e3378c35f7f1c4fec2f600c33b9d17ab6d330b4c/download-lcm-lora.json#L5)<br>[stable-diffusion-webui-forge](https://github.com/pinokiofactory/stable-diffusion-webui-forge): [download-lcm-lora.json:5](https://github.com/pinokiofactory/stable-diffusion-webui-forge/blob/e44fda22458c495919a1c90ed9e7d5c63c37adfb/download-lcm-lora.json#L5) |
| [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | [comfy](https://github.com/pinokiofactory/comfy), [forge](https://github.com/pinokiofactory/forge), [stable-diffusion-webui-forge](https://github.com/pinokiofactory/stable-diffusion-webui-forge) | PyTorch | FP32 100.0% | `v1-5-pruned.safetensors` | [comfy](https://github.com/pinokiofactory/comfy): [download-sd15.json:7](https://github.com/pinokiofactory/comfy/blob/ba110479f88835d64c603044c2fe69102833fa55/download-sd15.json#L7)<br>[forge](https://github.com/pinokiofactory/forge): [download-sd15.json:5](https://github.com/pinokiofactory/forge/blob/e3378c35f7f1c4fec2f600c33b9d17ab6d330b4c/download-sd15.json#L5)<br>[stable-diffusion-webui-forge](https://github.com/pinokiofactory/stable-diffusion-webui-forge): [download-sd15.json:5](https://github.com/pinokiofactory/stable-diffusion-webui-forge/blob/e44fda22458c495919a1c90ed9e7d5c63c37adfb/download-sd15.json#L5) |
| [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) | [comfy](https://github.com/pinokiofactory/comfy), [forge](https://github.com/pinokiofactory/forge), [stable-diffusion-webui-forge](https://github.com/pinokiofactory/stable-diffusion-webui-forge) | PyTorch | FP16 100.0% | `sd_xl_turbo_1.0_fp16.safetensors` | [comfy](https://github.com/pinokiofactory/comfy): [download-turbo.json:7](https://github.com/pinokiofactory/comfy/blob/ba110479f88835d64c603044c2fe69102833fa55/download-turbo.json#L7)<br>[forge](https://github.com/pinokiofactory/forge): [install.js:57](https://github.com/pinokiofactory/forge/blob/e3378c35f7f1c4fec2f600c33b9d17ab6d330b4c/install.js#L57)<br>[stable-diffusion-webui-forge](https://github.com/pinokiofactory/stable-diffusion-webui-forge): [download-turbo.json:5](https://github.com/pinokiofactory/stable-diffusion-webui-forge/blob/e44fda22458c495919a1c90ed9e7d5c63c37adfb/download-turbo.json#L5) |
| [stabilityai/stable-diffusion-2-1](https://huggingface.co/stabilityai/stable-diffusion-2-1) | [comfy](https://github.com/pinokiofactory/comfy), [forge](https://github.com/pinokiofactory/forge), [stable-diffusion-webui-forge](https://github.com/pinokiofactory/stable-diffusion-webui-forge) | PyTorch | unspecified | `v2-1_768-ema-pruned.safetensors` | [comfy](https://github.com/pinokiofactory/comfy): [download-sd21.json:7](https://github.com/pinokiofactory/comfy/blob/ba110479f88835d64c603044c2fe69102833fa55/download-sd21.json#L7)<br>[forge](https://github.com/pinokiofactory/forge): [download-sd21.json:5](https://github.com/pinokiofactory/forge/blob/e3378c35f7f1c4fec2f600c33b9d17ab6d330b4c/download-sd21.json#L5)<br>[stable-diffusion-webui-forge](https://github.com/pinokiofactory/stable-diffusion-webui-forge): [download-sd21.json:5](https://github.com/pinokiofactory/stable-diffusion-webui-forge/blob/e44fda22458c495919a1c90ed9e7d5c63c37adfb/download-sd21.json#L5) |
| [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | [comfy](https://github.com/pinokiofactory/comfy), [forge](https://github.com/pinokiofactory/forge), [stable-diffusion-webui-forge](https://github.com/pinokiofactory/stable-diffusion-webui-forge) | PyTorch | FP16 100.0% | `sd_xl_base_1.0.safetensors` | [comfy](https://github.com/pinokiofactory/comfy): [download-sdxl.json:7](https://github.com/pinokiofactory/comfy/blob/ba110479f88835d64c603044c2fe69102833fa55/download-sdxl.json#L7)<br>[forge](https://github.com/pinokiofactory/forge): [download-sdxl.json:5](https://github.com/pinokiofactory/forge/blob/e3378c35f7f1c4fec2f600c33b9d17ab6d330b4c/download-sdxl.json#L5)<br>[stable-diffusion-webui-forge](https://github.com/pinokiofactory/stable-diffusion-webui-forge): [download-sdxl.json:5](https://github.com/pinokiofactory/stable-diffusion-webui-forge/blob/e44fda22458c495919a1c90ed9e7d5c63c37adfb/download-sdxl.json#L5) |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | [comfy](https://github.com/pinokiofactory/comfy), [stable-diffusion-webui-forge](https://github.com/pinokiofactory/stable-diffusion-webui-forge) | PyTorch | NF4 (packed U8) 54.4%; FP8 (E4M3FN) 42.9%; FP32 1.6%; FP16 1.1% | `flux1-dev-bnb-nf4-v2.safetensors`, `flux1-dev-bnb-nf4.safetensors` | [comfy](https://github.com/pinokiofactory/comfy): [download-flux-dev-nf4.json:7](https://github.com/pinokiofactory/comfy/blob/ba110479f88835d64c603044c2fe69102833fa55/download-flux-dev-nf4.json#L7)<br>[stable-diffusion-webui-forge](https://github.com/pinokiofactory/stable-diffusion-webui-forge): [install.js:99](https://github.com/pinokiofactory/stable-diffusion-webui-forge/blob/e44fda22458c495919a1c90ed9e7d5c63c37adfb/install.js#L99) |
| [silveroxides/flux1-nf4-weights](https://huggingface.co/silveroxides/flux1-nf4-weights) | [comfy](https://github.com/pinokiofactory/comfy), [stable-diffusion-webui-forge](https://github.com/pinokiofactory/stable-diffusion-webui-forge) | PyTorch | NF4 | `flux1-schnell-bnb-nf4.safetensors` | [comfy](https://github.com/pinokiofactory/comfy): [download-flux-schnell-nf4.json:7](https://github.com/pinokiofactory/comfy/blob/ba110479f88835d64c603044c2fe69102833fa55/download-flux-schnell-nf4.json#L7)<br>[stable-diffusion-webui-forge](https://github.com/pinokiofactory/stable-diffusion-webui-forge): [download-flux1-schnell-nf4.json:5](https://github.com/pinokiofactory/stable-diffusion-webui-forge/blob/e44fda22458c495919a1c90ed9e7d5c63c37adfb/download-flux1-schnell-nf4.json#L5) |
| [stabilityai/stable-diffusion-xl-refiner-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0) | [forge](https://github.com/pinokiofactory/forge), [stable-diffusion-webui-forge](https://github.com/pinokiofactory/stable-diffusion-webui-forge) | PyTorch | FP16 100.0% | `sd_xl_refiner_1.0.safetensors` | [forge](https://github.com/pinokiofactory/forge): [download-sdxl.json:11](https://github.com/pinokiofactory/forge/blob/e3378c35f7f1c4fec2f600c33b9d17ab6d330b4c/download-sdxl.json#L11)<br>[stable-diffusion-webui-forge](https://github.com/pinokiofactory/stable-diffusion-webui-forge): [download-sdxl.json:11](https://github.com/pinokiofactory/stable-diffusion-webui-forge/blob/e44fda22458c495919a1c90ed9e7d5c63c37adfb/download-sdxl.json#L11) |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | [forge](https://github.com/pinokiofactory/forge), [stable-diffusion-webui-forge](https://github.com/pinokiofactory/stable-diffusion-webui-forge) | PyTorch | FP32 100.0% | `svd.safetensors` | [forge](https://github.com/pinokiofactory/forge): [download-svd.json:5](https://github.com/pinokiofactory/forge/blob/e3378c35f7f1c4fec2f600c33b9d17ab6d330b4c/download-svd.json#L5)<br>[stable-diffusion-webui-forge](https://github.com/pinokiofactory/stable-diffusion-webui-forge): [download-svd.json:5](https://github.com/pinokiofactory/stable-diffusion-webui-forge/blob/e44fda22458c495919a1c90ed9e7d5c63c37adfb/download-svd.json#L5) |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | [forge](https://github.com/pinokiofactory/forge), [stable-diffusion-webui-forge](https://github.com/pinokiofactory/stable-diffusion-webui-forge) | PyTorch | FP32 100.0% | `svd_xt.safetensors` | [forge](https://github.com/pinokiofactory/forge): [download-svd-xt.json:5](https://github.com/pinokiofactory/forge/blob/e3378c35f7f1c4fec2f600c33b9d17ab6d330b4c/download-svd-xt.json#L5)<br>[stable-diffusion-webui-forge](https://github.com/pinokiofactory/stable-diffusion-webui-forge): [download-svd-xt.json:5](https://github.com/pinokiofactory/stable-diffusion-webui-forge/blob/e44fda22458c495919a1c90ed9e7d5c63c37adfb/download-svd-xt.json#L5) |
| [ai-forever/Real-ESRGAN](https://huggingface.co/ai-forever/Real-ESRGAN) | [cogstudio](https://github.com/pinokiofactory/cogstudio) | PyTorch | unspecified | `RealESRGAN_x4.pt` | [cogstudio](https://github.com/pinokiofactory/cogstudio): [cogstudio.py:42](https://github.com/pinokiofactory/cogstudio/blob/7dfb014a636513c5b42de070c43e285c9bf7cce7/cogstudio.py#L42) |
| [AIDC-AI/Ovis-Image-7B](https://huggingface.co/AIDC-AI/Ovis-Image-7B) | [ovis](https://github.com/pinokiofactory/ovis) | Other / unspecified | FP32 100.0% | — | [ovis](https://github.com/pinokiofactory/ovis): [pinokio.json:8](https://github.com/pinokiofactory/ovis/blob/00a570258ba7370090037bb14bcfa67e1e81194e/pinokio.json#L8) |
| [AITRADER/SongGeneration-Large-MLX](https://huggingface.co/AITRADER/SongGeneration-Large-MLX) | [SongGeneration-Studio-MLX](https://github.com/pinokiofactory/SongGeneration-Studio-MLX) | Other / unspecified | unspecified | — | [SongGeneration-Studio-MLX](https://github.com/pinokiofactory/SongGeneration-Studio-MLX): [pinokio.json:16](https://github.com/pinokiofactory/SongGeneration-Studio-MLX/blob/49e365c88512ffd1a4bf17d800c5508e7d5781da/pinokio.json#L16) |
| [amaai-lab/text2midi](https://huggingface.co/amaai-lab/text2midi) | [text2midi](https://github.com/pinokiofactory/text2midi) | Other / unspecified | unspecified | — | [text2midi](https://github.com/pinokiofactory/text2midi): [install.js:39](https://github.com/pinokiofactory/text2midi/blob/8e5f742a1313c9b6f89bcf779fd0f4cf798864b7/install.js#L39) |
| [BadToBest/EchoMimicV2](https://huggingface.co/BadToBest/EchoMimicV2) | [echomimic2](https://github.com/pinokiofactory/echomimic2) | Other / unspecified | unspecified | — | [echomimic2](https://github.com/pinokiofactory/echomimic2): [install.js:55](https://github.com/pinokiofactory/echomimic2/blob/eb7915a14420505c7c8b929a2dbba570f1639831/install.js#L55) |
| [black-forest-labs/FLUX.1-schnell](https://huggingface.co/black-forest-labs/FLUX.1-schnell) | [flux-webui](https://github.com/pinokiofactory/flux-webui) | Other / unspecified | BF16 100.0% (repo aggregate) | — | [flux-webui](https://github.com/pinokiofactory/flux-webui): [README.md:7](https://github.com/pinokiofactory/flux-webui/blob/62d2f5692da1e0aaf776c3dceef0a720a6a24bb6/README.md#L7) |
| [briaai/RMBG-2.0](https://huggingface.co/briaai/RMBG-2.0) | [RMBG-2-Studio](https://github.com/pinokiofactory/RMBG-2-Studio) | Other / unspecified | FP32 99.8% (repo aggregate) | — | [RMBG-2-Studio](https://github.com/pinokiofactory/RMBG-2-Studio): [pinokio.js:5](https://github.com/pinokiofactory/RMBG-2-Studio/blob/a2c3a0d0f1618c74c115d3221eb665bab5e8df10/pinokio.js#L5) |
| [city96/FLUX.1-dev-gguf](https://huggingface.co/city96/FLUX.1-dev-gguf) | [comfy](https://github.com/pinokiofactory/comfy) | GGUF | INT4/qint4 | `flux1-dev-Q4_0.gguf` | [comfy](https://github.com/pinokiofactory/comfy): [download-flux-dev-gguf-q4-0.json:7](https://github.com/pinokiofactory/comfy/blob/ba110479f88835d64c603044c2fe69102833fa55/download-flux-dev-gguf-q4-0.json#L7) |
| [city96/FLUX.1-schnell-gguf](https://huggingface.co/city96/FLUX.1-schnell-gguf) | [comfy](https://github.com/pinokiofactory/comfy) | GGUF | INT4/qint4 | `flux1-schnell-Q4_0.gguf` | [comfy](https://github.com/pinokiofactory/comfy): [download-flux-schnell-gguf-q4-0.json:7](https://github.com/pinokiofactory/comfy/blob/ba110479f88835d64c603044c2fe69102833fa55/download-flux-schnell-gguf-q4-0.json#L7) |
| [cleardusk/LivePortrait-Windows](https://huggingface.co/cleardusk/LivePortrait-Windows) | [liveportrait](https://github.com/pinokiofactory/liveportrait) | Other / unspecified | unspecified | — | [liveportrait](https://github.com/pinokiofactory/liveportrait): [win.js:7](https://github.com/pinokiofactory/liveportrait/blob/b5fb16ce6df50e79d11d7c1a2d7b39faa720411e/win.js#L7) |
| [cocktailpeanut/audio_processor](https://huggingface.co/cocktailpeanut/audio_processor) | [echomimic2](https://github.com/pinokiofactory/echomimic2) | Other / unspecified | unspecified | — | [echomimic2](https://github.com/pinokiofactory/echomimic2): [install.js:76](https://github.com/pinokiofactory/echomimic2/blob/eb7915a14420505c7c8b929a2dbba570f1639831/install.js#L76) |
| [cocktailpeanut/fcanny](https://huggingface.co/cocktailpeanut/fcanny) | [comfy](https://github.com/pinokiofactory/comfy) | PyTorch | BF16 100.0% | `flux1-canny-dev.safetensors` | [comfy](https://github.com/pinokiofactory/comfy): [fluxtools/canny.json:7](https://github.com/pinokiofactory/comfy/blob/ba110479f88835d64c603044c2fe69102833fa55/fluxtools/canny.json#L7) |
| [cocktailpeanut/fdepth](https://huggingface.co/cocktailpeanut/fdepth) | [comfy](https://github.com/pinokiofactory/comfy) | PyTorch | BF16 100.0% | `flux1-depth-dev.safetensors` | [comfy](https://github.com/pinokiofactory/comfy): [fluxtools/depth.json:7](https://github.com/pinokiofactory/comfy/blob/ba110479f88835d64c603044c2fe69102833fa55/fluxtools/depth.json#L7) |
| [cocktailpeanut/fill](https://huggingface.co/cocktailpeanut/fill) | [comfy](https://github.com/pinokiofactory/comfy) | PyTorch | BF16 100.0% | `flux1-fill-dev.safetensors` | [comfy](https://github.com/pinokiofactory/comfy): [fluxtools/fill.json:27](https://github.com/pinokiofactory/comfy/blob/ba110479f88835d64c603044c2fe69102833fa55/fluxtools/fill.json#L27) |
| [cocktailpeanut/flux1-merged-q8](https://huggingface.co/cocktailpeanut/flux1-merged-q8) | [flux-webui](https://github.com/pinokiofactory/flux-webui) | Other / unspecified | FP8 (E4M3FN) 99.9% | — | [flux-webui](https://github.com/pinokiofactory/flux-webui): [app.py:78](https://github.com/pinokiofactory/flux-webui/blob/62d2f5692da1e0aaf776c3dceef0a720a6a24bb6/app.py#L78) |
| [cocktailpeanut/flux1-merged-qint8](https://huggingface.co/cocktailpeanut/flux1-merged-qint8) | [flux-webui](https://github.com/pinokiofactory/flux-webui) | Other / unspecified | INT8 99.9% | — | [flux-webui](https://github.com/pinokiofactory/flux-webui): [app.py:75](https://github.com/pinokiofactory/flux-webui/blob/62d2f5692da1e0aaf776c3dceef0a720a6a24bb6/app.py#L75) |
| [cocktailpeanut/flux1-schnell-q8](https://huggingface.co/cocktailpeanut/flux1-schnell-q8) | [flux-webui](https://github.com/pinokiofactory/flux-webui) | Other / unspecified | FP8 (E4M3FN) 99.9% | — | [flux-webui](https://github.com/pinokiofactory/flux-webui): [app.py:86](https://github.com/pinokiofactory/flux-webui/blob/62d2f5692da1e0aaf776c3dceef0a720a6a24bb6/app.py#L86) |
| [cocktailpeanut/flux1-schnell-qint8](https://huggingface.co/cocktailpeanut/flux1-schnell-qint8) | [flux-webui](https://github.com/pinokiofactory/flux-webui) | Other / unspecified | INT8 99.9% | — | [flux-webui](https://github.com/pinokiofactory/flux-webui): [app.py:83](https://github.com/pinokiofactory/flux-webui/blob/62d2f5692da1e0aaf776c3dceef0a720a6a24bb6/app.py#L83) |
| [cocktailpeanut/oa](https://huggingface.co/cocktailpeanut/oa) | [Ultimate-TTS-Studio](https://github.com/pinokiofactory/Ultimate-TTS-Studio) | Other / unspecified | unspecified | — | [Ultimate-TTS-Studio](https://github.com/pinokiofactory/Ultimate-TTS-Studio): [install.js:47](https://github.com/pinokiofactory/Ultimate-TTS-Studio/blob/b8c15efaead5a5e8744783fd443466333d2b1805/install.js#L47) |
| [cocktailpeanut/redux](https://huggingface.co/cocktailpeanut/redux) | [comfy](https://github.com/pinokiofactory/comfy) | PyTorch | BF16 100.0% | `flux1-redux-dev.safetensors` | [comfy](https://github.com/pinokiofactory/comfy): [fluxtools/redux_schnell.json:17](https://github.com/pinokiofactory/comfy/blob/ba110479f88835d64c603044c2fe69102833fa55/fluxtools/redux_schnell.json#L17) |
| [cocktailpeanut/sd35](https://huggingface.co/cocktailpeanut/sd35) | [sd35](https://github.com/pinokiofactory/sd35) | PyTorch | FP16 99.0%; BF16 1.0% | `sd3.5_large.safetensors` | [sd35](https://github.com/pinokiofactory/sd35): [app.py:48](https://github.com/pinokiofactory/sd35/blob/1e820d785879752bf27626cce260c49cdbfe149d/app.py#L48) |
| [cocktailpeanut/sd35turbo](https://huggingface.co/cocktailpeanut/sd35turbo) | [sd35](https://github.com/pinokiofactory/sd35) | PyTorch | FP16 99.0%; BF16 1.0% | `sd3.5_large_turbo.safetensors` | [sd35](https://github.com/pinokiofactory/sd35): [app.py:50](https://github.com/pinokiofactory/sd35/blob/1e820d785879752bf27626cce260c49cdbfe149d/app.py#L50) |
| [cocktailpeanut/sf3d](https://huggingface.co/cocktailpeanut/sf3d) | [stable-fast-3d](https://github.com/pinokiofactory/stable-fast-3d) | Other / unspecified | FP32 100.0% | — | [stable-fast-3d](https://github.com/pinokiofactory/stable-fast-3d): [README.md:3](https://github.com/pinokiofactory/stable-fast-3d/blob/00fdb293b784f223c100971f37a23f2e8a801654/README.md#L3) |
| [cocktailpeanut/sisao](https://huggingface.co/cocktailpeanut/sisao) | [oasis](https://github.com/pinokiofactory/oasis) | PyTorch | FP32 100.0% | `oasis500m.pt`, `vit-l-20.pt` | [oasis](https://github.com/pinokiofactory/oasis): [install.js:46](https://github.com/pinokiofactory/oasis/blob/a84069d12ae3165aa0c8c955f9a93314ecf3d3d8/install.js#L46) |
| [cocktailpeanut/xulf-dev](https://huggingface.co/cocktailpeanut/xulf-dev) | [comfy](https://github.com/pinokiofactory/comfy) | PyTorch | BF16 99.3%; FP32 0.7% | `ae.safetensors`, `flux1-dev.safetensors` | [comfy](https://github.com/pinokiofactory/comfy): [download-flux-dev.json:37](https://github.com/pinokiofactory/comfy/blob/ba110479f88835d64c603044c2fe69102833fa55/download-flux-dev.json#L37) |
| [cocktailpeanut/xulf-schnell](https://huggingface.co/cocktailpeanut/xulf-schnell) | [comfy](https://github.com/pinokiofactory/comfy) | PyTorch | BF16 99.3%; FP32 0.7% | `ae.safetensors`, `flux1-schnell.safetensors` | [comfy](https://github.com/pinokiofactory/comfy): [initialize-models-mac-arm64.js:31](https://github.com/pinokiofactory/comfy/blob/ba110479f88835d64c603044c2fe69102833fa55/initialize-models-mac-arm64.js#L31) |
| [Comfy-Org/flux1-dev](https://huggingface.co/Comfy-Org/flux1-dev) | [comfy](https://github.com/pinokiofactory/comfy) | PyTorch | FP8 (E4M3FN) 98.8%; FP16 0.7%; FP32 0.5% | `flux1-dev-fp8.safetensors` | [comfy](https://github.com/pinokiofactory/comfy): [download-flux-dev-fp8.json:7](https://github.com/pinokiofactory/comfy/blob/ba110479f88835d64c603044c2fe69102833fa55/download-flux-dev-fp8.json#L7) |
| [Comfy-Org/flux1-schnell](https://huggingface.co/Comfy-Org/flux1-schnell) | [comfy](https://github.com/pinokiofactory/comfy) | PyTorch | FP8 (E4M3FN) 98.8%; FP16 0.7%; FP32 0.5% | `flux1-schnell-fp8.safetensors` | [comfy](https://github.com/pinokiofactory/comfy): [download-flux-schnell-fp8.json:7](https://github.com/pinokiofactory/comfy/blob/ba110479f88835d64c603044c2fe69102833fa55/download-flux-schnell-fp8.json#L7) |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | [comfy](https://github.com/pinokiofactory/comfy) | PyTorch | FP8 (E4M3FN) 47.9%; BF16 32.7%; FP16 19.4% | `mochi_preview_bf16.safetensors`, `mochi_preview_fp8_scaled.safetensors`, `mochi_vae.safetensors`, `t5xxl_fp16.safetensors`, `t5xxl_fp8_e4m3fn_scaled.safetensors` | [comfy](https://github.com/pinokiofactory/comfy): [mochi-mac.json:5](https://github.com/pinokiofactory/comfy/blob/ba110479f88835d64c603044c2fe69102833fa55/mochi-mac.json#L5) |
| [Comfy-Org/sigclip_vision_384](https://huggingface.co/Comfy-Org/sigclip_vision_384) | [comfy](https://github.com/pinokiofactory/comfy) | PyTorch | FP16 100.0% | `sigclip_vision_patch14_384.safetensors` | [comfy](https://github.com/pinokiofactory/comfy): [fluxtools/redux_schnell.json:7](https://github.com/pinokiofactory/comfy/blob/ba110479f88835d64c603044c2fe69102833fa55/fluxtools/redux_schnell.json#L7) |
| [Comfy-Org/stable-diffusion-3.5-fp8](https://huggingface.co/Comfy-Org/stable-diffusion-3.5-fp8) | [comfy](https://github.com/pinokiofactory/comfy) | PyTorch | FP16 100.0% | `text_encoders/clip_l.safetensors`, `text_encoders/t5xxl_fp16.safetensors` | [comfy](https://github.com/pinokiofactory/comfy): [ltx.json:17](https://github.com/pinokiofactory/comfy/blob/ba110479f88835d64c603044c2fe69102833fa55/ltx.json#L17) |
| [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged) | [comfy](https://github.com/pinokiofactory/comfy) | PyTorch | BF16 83.8%; FP8 (E4M3FN) 11.8%; FP16 4.3% | `clip_vision_h.safetensors`, `umt5_xxl_fp8_e4m3fn_scaled.safetensors`, `wan2.1_i2v_480p_14B_bf16.safetensors`, `wan2.1_i2v_720p_14B_bf16.safetensors`, `wan2.1_t2v_1.3B_bf16.safetensors` (+2 more) | [comfy](https://github.com/pinokiofactory/comfy): [wan/text1.3b.js:6](https://github.com/pinokiofactory/comfy/blob/ba110479f88835d64c603044c2fe69102833fa55/wan/text1.3b.js#L6) |
| [comfyanonymous/flux_text_encoders](https://huggingface.co/comfyanonymous/flux_text_encoders) | [comfy](https://github.com/pinokiofactory/comfy) | PyTorch | FP16 50.6%; FP8 (E4M3FN) 49.4% | `clip_l.safetensors`, `t5xxl_fp16.safetensors`, `t5xxl_fp8_e4m3fn.safetensors` | [comfy](https://github.com/pinokiofactory/comfy): [initialize-models-mac-arm64.js:9](https://github.com/pinokiofactory/comfy/blob/ba110479f88835d64c603044c2fe69102833fa55/initialize-models-mac-arm64.js#L9) |
| [drbaph/FLUX.1-schnell-dev-merged-fp8-4step](https://huggingface.co/drbaph/FLUX.1-schnell-dev-merged-fp8-4step) | [comfy](https://github.com/pinokiofactory/comfy) | PyTorch | FP8 (E4M3FN) 70.5%; FP16 29.0%; BF16 0.5% | `FLUX.1-schnell-dev-merged-fp8-4step.safetensors` | [comfy](https://github.com/pinokiofactory/comfy): [download-flux-merged-fp8.json:7](https://github.com/pinokiofactory/comfy/blob/ba110479f88835d64c603044c2fe69102833fa55/download-flux-merged-fp8.json#L7) |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | [hallo](https://github.com/pinokiofactory/hallo) | Other / unspecified | FP32 100.0% | — | [hallo](https://github.com/pinokiofactory/hallo): [install.js:41](https://github.com/pinokiofactory/hallo/blob/c72097c6c23be58e7435bc48fbe9d0be5d0da1e5/install.js#L41) |
| [genmo/mochi-1-preview](https://huggingface.co/genmo/mochi-1-preview) | [mochi](https://github.com/pinokiofactory/mochi) | Other / unspecified | FP32 100.0% | — | [mochi](https://github.com/pinokiofactory/mochi): [install.js:67](https://github.com/pinokiofactory/mochi/blob/93d4b2bddb16f3ce883f47336f1de7c126955d6e/install.js#L67) |
| [hexgrad/Kokoro-82M](https://huggingface.co/hexgrad/Kokoro-82M) | [Kokoro-TTS](https://github.com/pinokiofactory/Kokoro-TTS) | Other / unspecified | unspecified | — | [Kokoro-TTS](https://github.com/pinokiofactory/Kokoro-TTS): [app.py:47](https://github.com/pinokiofactory/Kokoro-TTS/blob/491a369bdca03b320586bd230f1c819562c03558/app.py#L47) |
| [HKUSTAudio/AudioX](https://huggingface.co/HKUSTAudio/AudioX) | [AudioX](https://github.com/pinokiofactory/AudioX) | PyTorch | unspecified | `model.ckpt` | [AudioX](https://github.com/pinokiofactory/AudioX): [install.js:44](https://github.com/pinokiofactory/AudioX/blob/7a0ff7b5ca8d5eeb6054edf84196a23389545d1d/install.js#L44) |
| [hunyuanvideo-community/HunyuanVideo](https://huggingface.co/hunyuanvideo-community/HunyuanVideo) | [Frame-Pack](https://github.com/pinokiofactory/Frame-Pack) | Other / unspecified | FP16 100.0% | — | [Frame-Pack](https://github.com/pinokiofactory/Frame-Pack): [demo_gradio_f1.py:49](https://github.com/pinokiofactory/Frame-Pack/blob/f0d7d1eba4155f5985a465d0476a9f926d0c6179/demo_gradio_f1.py#L49) |
| [IAHispano/Applio](https://huggingface.co/IAHispano/Applio) | [applio-old](https://github.com/pinokiofactory/applio-old) | Other / unspecified | unspecified | — | [applio-old](https://github.com/pinokiofactory/applio-old): [install.js:14](https://github.com/pinokiofactory/applio-old/blob/a8d276c8f426304428755974392b5e42d4ef29a5/install.js#L14) |
| [KBlueLeaf/kohaku-v2.1](https://huggingface.co/KBlueLeaf/kohaku-v2.1) | [StreamDiffusion](https://github.com/pinokiofactory/StreamDiffusion) | Other / unspecified | FP16 100.0% | — | [StreamDiffusion](https://github.com/pinokiofactory/StreamDiffusion): [README-ko.md:196](https://github.com/pinokiofactory/StreamDiffusion/blob/0e529aaff2ff344ce15565420e0c484688eb1bc9/README-ko.md#L196) |
| [Kijai/HunyuanVideo_comfy](https://huggingface.co/Kijai/HunyuanVideo_comfy) | [comfy](https://github.com/pinokiofactory/comfy) | PyTorch | FP8 (E4M3FN) 95.3%; BF16 4.7% | `hunyuan_video_720_cfgdistill_fp8_e4m3fn.safetensors`, `hunyuan_video_vae_bf16.safetensors` | [comfy](https://github.com/pinokiofactory/comfy): [h.js:7](https://github.com/pinokiofactory/comfy/blob/ba110479f88835d64c603044c2fe69102833fa55/h.js#L7) |
| [Kijai/llava-llama-3-8b-text-encoder-tokenizer](https://huggingface.co/Kijai/llava-llama-3-8b-text-encoder-tokenizer) | [comfy](https://github.com/pinokiofactory/comfy) | Other / unspecified | FP16 100.0% | — | [comfy](https://github.com/pinokiofactory/comfy): [h.js:22](https://github.com/pinokiofactory/comfy/blob/ba110479f88835d64c603044c2fe69102833fa55/h.js#L22) |
| [KwaiVGI/LivePortrait](https://huggingface.co/KwaiVGI/LivePortrait) | [liveportrait](https://github.com/pinokiofactory/liveportrait) | Other / unspecified | unspecified | — | [liveportrait](https://github.com/pinokiofactory/liveportrait): [common.js:71](https://github.com/pinokiofactory/liveportrait/blob/b5fb16ce6df50e79d11d7c1a2d7b39faa720411e/common.js#L71) |
| [lambdalabs/sd-image-variations-diffusers](https://huggingface.co/lambdalabs/sd-image-variations-diffusers) | [echomimic2](https://github.com/pinokiofactory/echomimic2) | Other / unspecified | unspecified | — | [echomimic2](https://github.com/pinokiofactory/echomimic2): [install.js:69](https://github.com/pinokiofactory/echomimic2/blob/eb7915a14420505c7c8b929a2dbba570f1639831/install.js#L69) |
| [latent-consistency/lcm-lora-sdv1-5](https://huggingface.co/latent-consistency/lcm-lora-sdv1-5) | [StreamDiffusion](https://github.com/pinokiofactory/StreamDiffusion) | Other / unspecified | FP16 100.0% | — | [StreamDiffusion](https://github.com/pinokiofactory/StreamDiffusion): [README-ko.md:389](https://github.com/pinokiofactory/StreamDiffusion/blob/0e529aaff2ff344ce15565420e0c484688eb1bc9/README-ko.md#L389) |
| [lex-au/Orpheus-3b-FT-Q8_0.gguf](https://huggingface.co/lex-au/Orpheus-3b-FT-Q8_0.gguf) | [Orpheus-TTS-FastAPI](https://github.com/pinokiofactory/Orpheus-TTS-FastAPI) | GGUF | INT8/qint8 | `Orpheus-3b-FT-Q8_0.gguf` | [Orpheus-TTS-FastAPI](https://github.com/pinokiofactory/Orpheus-TTS-FastAPI): [start.js:16](https://github.com/pinokiofactory/Orpheus-TTS-FastAPI/blob/36afb50f8c7355238763680480dca601789cae82/start.js#L16) |
| [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video) | [comfy](https://github.com/pinokiofactory/comfy) | PyTorch | BF16 57.5%; FP32 42.5% | `ltx-video-2b-v0.9.5.safetensors`, `ltx-video-2b-v0.9.safetensors` | [comfy](https://github.com/pinokiofactory/comfy): [ltx.json:7](https://github.com/pinokiofactory/comfy/blob/ba110479f88835d64c603044c2fe69102833fa55/ltx.json#L7) |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | [MagicQuill](https://github.com/pinokiofactory/MagicQuill) | Other / unspecified | FP16 100.0% | — | [MagicQuill](https://github.com/pinokiofactory/MagicQuill): [install.js:101](https://github.com/pinokiofactory/MagicQuill/blob/bfdae2847a85d7b00761b4e93fbcb91be5e6d494/install.js#L101) |
| [lllyasviel/flux1_dev](https://huggingface.co/lllyasviel/flux1_dev) | [stable-diffusion-webui-forge](https://github.com/pinokiofactory/stable-diffusion-webui-forge) | PyTorch | FP8 (E4M3FN) 98.8%; FP16 0.7%; FP32 0.5% | `flux1-dev-fp8.safetensors` | [stable-diffusion-webui-forge](https://github.com/pinokiofactory/stable-diffusion-webui-forge): [install.js:108](https://github.com/pinokiofactory/stable-diffusion-webui-forge/blob/e44fda22458c495919a1c90ed9e7d5c63c37adfb/install.js#L108) |
| [lllyasviel/flux_redux_bfl](https://huggingface.co/lllyasviel/flux_redux_bfl) | [Frame-Pack](https://github.com/pinokiofactory/Frame-Pack) | Other / unspecified | BF16 100.0% | — | [Frame-Pack](https://github.com/pinokiofactory/Frame-Pack): [demo_gradio_f1.py:55](https://github.com/pinokiofactory/Frame-Pack/blob/f0d7d1eba4155f5985a465d0476a9f926d0c6179/demo_gradio_f1.py#L55) |
| [lllyasviel/FramePack_F1_I2V_HY_20250503](https://huggingface.co/lllyasviel/FramePack_F1_I2V_HY_20250503) | [Frame-Pack](https://github.com/pinokiofactory/Frame-Pack) | Other / unspecified | BF16 100.0% | — | [Frame-Pack](https://github.com/pinokiofactory/Frame-Pack): [demo_gradio_f1.py:58](https://github.com/pinokiofactory/Frame-Pack/blob/f0d7d1eba4155f5985a465d0476a9f926d0c6179/demo_gradio_f1.py#L58) |
| [lllyasviel/FramePackI2V_HY](https://huggingface.co/lllyasviel/FramePackI2V_HY) | [Frame-Pack](https://github.com/pinokiofactory/Frame-Pack) | Other / unspecified | BF16 100.0% | — | [Frame-Pack](https://github.com/pinokiofactory/Frame-Pack): [demo_gradio_k.py:57](https://github.com/pinokiofactory/Frame-Pack/blob/f0d7d1eba4155f5985a465d0476a9f926d0c6179/demo_gradio_k.py#L57) |
| [m-a-p/xcodec_mini_infer](https://huggingface.co/m-a-p/xcodec_mini_infer) | [yue](https://github.com/pinokiofactory/yue) | Other / unspecified | unspecified | — | [yue](https://github.com/pinokiofactory/yue): [install.js:19](https://github.com/pinokiofactory/yue/blob/3261118f111c8d2bb098b82b2870458dfbc486c7/install.js#L19) |
| [madebyollin/taesd](https://huggingface.co/madebyollin/taesd) | [StreamDiffusion](https://github.com/pinokiofactory/StreamDiffusion) | Other / unspecified | FP32 100.0% | — | [StreamDiffusion](https://github.com/pinokiofactory/StreamDiffusion): [README-ko.md:212](https://github.com/pinokiofactory/StreamDiffusion/blob/0e529aaff2ff344ce15565420e0c484688eb1bc9/README-ko.md#L212) |
| [microsoft/OmniParser](https://huggingface.co/microsoft/OmniParser) | [omniparser](https://github.com/pinokiofactory/omniparser) | Other / unspecified | FP32 98.9%; FP16 1.1% | — | [omniparser](https://github.com/pinokiofactory/omniparser): [install.js:52](https://github.com/pinokiofactory/omniparser/blob/b2f7de9607dcc3087229feaee36c6c2f0345fc80/install.js#L52) |
| [microsoft/VibeVoice-Realtime-0.5B](https://huggingface.co/microsoft/VibeVoice-Realtime-0.5B) | [vibevoice-realtime](https://github.com/pinokiofactory/vibevoice-realtime) | Other / unspecified | BF16 100.0% | — | [vibevoice-realtime](https://github.com/pinokiofactory/vibevoice-realtime): [pinokio.json:4](https://github.com/pinokiofactory/vibevoice-realtime/blob/e8f4b7bd22f65e45b19cd4e67cd0c1a982109102/pinokio.json#L4) |
| [multimodalart/Florence-2-large-no-flash-attn](https://huggingface.co/multimodalart/Florence-2-large-no-flash-attn) | [clarity-refiners-ui](https://github.com/pinokiofactory/clarity-refiners-ui) | Other / unspecified | unspecified | — | [clarity-refiners-ui](https://github.com/pinokiofactory/clarity-refiners-ui): [README.md:42](https://github.com/pinokiofactory/clarity-refiners-ui/blob/a632fb6b948fa6b1a55d816982655d6dc8ed995e/README.md#L42) |
| [nari-labs/Dia-1.6B](https://huggingface.co/nari-labs/Dia-1.6B) | [Nari-Dia-TTS](https://github.com/pinokiofactory/Nari-Dia-TTS) | Other / unspecified | FP32 100.0% | — | [Nari-Dia-TTS](https://github.com/pinokiofactory/Nari-Dia-TTS): [app.py:48](https://github.com/pinokiofactory/Nari-Dia-TTS/blob/e5b630df297c7f47f6c518a00d6c3f44be4e25b5/app.py#L48) |
| [openai/clip-vit-large-patch14](https://huggingface.co/openai/clip-vit-large-patch14) | [comfy](https://github.com/pinokiofactory/comfy) | Other / unspecified | FP32 100.0% | — | [comfy](https://github.com/pinokiofactory/comfy): [h.js:29](https://github.com/pinokiofactory/comfy/blob/ba110479f88835d64c603044c2fe69102833fa55/h.js#L29) |
| [philz1337x/embeddings](https://huggingface.co/philz1337x/embeddings) | [clarity-refiners-ui](https://github.com/pinokiofactory/clarity-refiners-ui) | Other / unspecified | unspecified | — | [clarity-refiners-ui](https://github.com/pinokiofactory/clarity-refiners-ui): [app/app.py:85](https://github.com/pinokiofactory/clarity-refiners-ui/blob/a632fb6b948fa6b1a55d816982655d6dc8ed995e/app/app.py#L85) |
| [philz1337x/loras](https://huggingface.co/philz1337x/loras) | [clarity-refiners-ui](https://github.com/pinokiofactory/clarity-refiners-ui) | Other / unspecified | FP16 97.4%; FP32 2.6% | — | [clarity-refiners-ui](https://github.com/pinokiofactory/clarity-refiners-ui): [app/app.py:95](https://github.com/pinokiofactory/clarity-refiners-ui/blob/a632fb6b948fa6b1a55d816982655d6dc8ed995e/app/app.py#L95) |
| [philz1337x/upscaler](https://huggingface.co/philz1337x/upscaler) | [clarity-refiners-ui](https://github.com/pinokiofactory/clarity-refiners-ui) | Other / unspecified | unspecified | — | [clarity-refiners-ui](https://github.com/pinokiofactory/clarity-refiners-ui): [app/app.py:78](https://github.com/pinokiofactory/clarity-refiners-ui/blob/a632fb6b948fa6b1a55d816982655d6dc8ed995e/app/app.py#L78) |
| [PixArt-alpha/PixArt-alpha](https://huggingface.co/PixArt-alpha/PixArt-alpha) | [Allegro-txt2vid](https://github.com/pinokiofactory/Allegro-txt2vid) | Other / unspecified | unspecified | — | [Allegro-txt2vid](https://github.com/pinokiofactory/Allegro-txt2vid): [allegro/pipelines/pipeline_allegro.py:129](https://github.com/pinokiofactory/Allegro-txt2vid/blob/f8327e3172834ee8d932d7284641a5e9a0065cbc/allegro/pipelines/pipeline_allegro.py#L129) |
| [refiners/controlnet.sd1_5.tile](https://huggingface.co/refiners/controlnet.sd1_5.tile) | [clarity-refiners-ui](https://github.com/pinokiofactory/clarity-refiners-ui) | Other / unspecified | FP16 100.0% | — | [clarity-refiners-ui](https://github.com/pinokiofactory/clarity-refiners-ui): [app/app.py:71](https://github.com/pinokiofactory/clarity-refiners-ui/blob/a632fb6b948fa6b1a55d816982655d6dc8ed995e/app/app.py#L71) |
| [refiners/juggernaut.reborn.sd1_5.autoencoder](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.autoencoder) | [clarity-refiners-ui](https://github.com/pinokiofactory/clarity-refiners-ui) | Other / unspecified | FP16 100.0% | — | [clarity-refiners-ui](https://github.com/pinokiofactory/clarity-refiners-ui): [app/app.py:64](https://github.com/pinokiofactory/clarity-refiners-ui/blob/a632fb6b948fa6b1a55d816982655d6dc8ed995e/app/app.py#L64) |
| [refiners/juggernaut.reborn.sd1_5.text_encoder](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.text_encoder) | [clarity-refiners-ui](https://github.com/pinokiofactory/clarity-refiners-ui) | Other / unspecified | FP16 100.0% | — | [clarity-refiners-ui](https://github.com/pinokiofactory/clarity-refiners-ui): [app/app.py:57](https://github.com/pinokiofactory/clarity-refiners-ui/blob/a632fb6b948fa6b1a55d816982655d6dc8ed995e/app/app.py#L57) |
| [refiners/juggernaut.reborn.sd1_5.unet](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.unet) | [clarity-refiners-ui](https://github.com/pinokiofactory/clarity-refiners-ui) | Other / unspecified | FP16 100.0% | — | [clarity-refiners-ui](https://github.com/pinokiofactory/clarity-refiners-ui): [app/app.py:50](https://github.com/pinokiofactory/clarity-refiners-ui/blob/a632fb6b948fa6b1a55d816982655d6dc8ed995e/app/app.py#L50) |
| [rhymes-ai/Allegro](https://huggingface.co/rhymes-ai/Allegro) | [Allegro-txt2vid](https://github.com/pinokiofactory/Allegro-txt2vid) | Other / unspecified | FP32 100.0% | — | [Allegro-txt2vid](https://github.com/pinokiofactory/Allegro-txt2vid): [gradio_app.py:122](https://github.com/pinokiofactory/Allegro-txt2vid/blob/f8327e3172834ee8d932d7284641a5e9a0065cbc/gradio_app.py#L122) |
| [Roblox/cube3d-v0.1](https://huggingface.co/Roblox/cube3d-v0.1) | [cube](https://github.com/pinokiofactory/cube) | Other / unspecified | FP32 100.0% | — | [cube](https://github.com/pinokiofactory/cube): [install.js:41](https://github.com/pinokiofactory/cube/blob/58844658cfc9eab4f8e956bab4883fa8d867cf44/install.js#L41) |
| [sayakpaul/FLUX.1-merged](https://huggingface.co/sayakpaul/FLUX.1-merged) | [flux-webui](https://github.com/pinokiofactory/flux-webui) | Other / unspecified | BF16 100.0% | — | [flux-webui](https://github.com/pinokiofactory/flux-webui): [README.md:8](https://github.com/pinokiofactory/flux-webui/blob/62d2f5692da1e0aaf776c3dceef0a720a6a24bb6/README.md#L8) |
| [stabilityai/sd-turbo](https://huggingface.co/stabilityai/sd-turbo) | [StreamDiffusion](https://github.com/pinokiofactory/StreamDiffusion) | Other / unspecified | FP32 100.0% | — | [StreamDiffusion](https://github.com/pinokiofactory/StreamDiffusion): [README-ko.md:395](https://github.com/pinokiofactory/StreamDiffusion/blob/0e529aaff2ff344ce15565420e0c484688eb1bc9/README-ko.md#L395) |
| [stabilityai/sd-vae-ft-mse](https://huggingface.co/stabilityai/sd-vae-ft-mse) | [echomimic2](https://github.com/pinokiofactory/echomimic2) | Other / unspecified | FP32 100.0% | — | [echomimic2](https://github.com/pinokiofactory/echomimic2): [install.js:62](https://github.com/pinokiofactory/echomimic2/blob/eb7915a14420505c7c8b929a2dbba570f1639831/install.js#L62) |
| [stabilityai/sd-vae-ft-mse-original](https://huggingface.co/stabilityai/sd-vae-ft-mse-original) | [Allegro-txt2vid](https://github.com/pinokiofactory/Allegro-txt2vid) | Other / unspecified | FP32 100.0% | — | [Allegro-txt2vid](https://github.com/pinokiofactory/Allegro-txt2vid): [README.md:174](https://github.com/pinokiofactory/Allegro-txt2vid/blob/f8327e3172834ee8d932d7284641a5e9a0065cbc/README.md#L174) |
| [THUDM/CogVideoX-2B](https://huggingface.co/THUDM/CogVideoX-2B) | [cogstudio](https://github.com/pinokiofactory/cogstudio) | Other / unspecified | FP16 100.0% | — | [cogstudio](https://github.com/pinokiofactory/cogstudio): [cogstudio.py:402](https://github.com/pinokiofactory/cogstudio/blob/7dfb014a636513c5b42de070c43e285c9bf7cce7/cogstudio.py#L402) |
| [THUDM/CogVideoX-5b-I2V](https://huggingface.co/THUDM/CogVideoX-5b-I2V) | [cogstudio](https://github.com/pinokiofactory/cogstudio) | Other / unspecified | BF16 100.0% | — | [cogstudio](https://github.com/pinokiofactory/cogstudio): [cogstudio.py:120](https://github.com/pinokiofactory/cogstudio/blob/7dfb014a636513c5b42de070c43e285c9bf7cce7/cogstudio.py#L120) |
| [Tongyi-MAI/Z-Image-Turbo](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo) | [z-image-turbo](https://github.com/pinokiofactory/z-image-turbo) | Other / unspecified | BF16 100.0% | — | [z-image-turbo](https://github.com/pinokiofactory/z-image-turbo): [pinokio.json:2](https://github.com/pinokiofactory/z-image-turbo/blob/54899fdb5c023072de43c8b91ad2b0f0bee5b5c4/pinokio.json#L2) |
| [XLabs-AI/flux-lora-collection](https://huggingface.co/XLabs-AI/flux-lora-collection) | [stable-diffusion-webui-forge](https://github.com/pinokiofactory/stable-diffusion-webui-forge) | PyTorch | BF16 100.0% | `anime_lora_comfy_converted.safetensors`, `art_lora_comfy_converted.safetensors`, `disney_lora_comfy_converted.safetensors`, `mjv6_lora_comfy_converted.safetensors`, `realism_lora_comfy_converted.safetensors` (+1 more) | [stable-diffusion-webui-forge](https://github.com/pinokiofactory/stable-diffusion-webui-forge): [download-xlabs.json:6](https://github.com/pinokiofactory/stable-diffusion-webui-forge/blob/e44fda22458c495919a1c90ed9e7d5c63c37adfb/download-xlabs.json#L6) |

## Tensor dtype detail (from safetensors headers / HF metadata)

Every dtype holding at least 0.1% of a model's parameters is listed. `Params` is the summed product of tensor shapes for that dtype; `Tensors` is the number of tensors (0 where only repo-aggregate metadata was available).

| Model | Dtype | Params | Tensors | Share | Source |
| --- | --- | --- | --- | --- | --- |
| [AIDC-AI/Ovis-Image-7B](https://huggingface.co/AIDC-AI/Ovis-Image-7B) | FP32 | 7.45B | 641 | 100.0% | safetensors header |
| [black-forest-labs/FLUX.1-schnell](https://huggingface.co/black-forest-labs/FLUX.1-schnell) | BF16 | 11.89B | — | 100.0% | HF repo metadata |
| [briaai/RMBG-2.0](https://huggingface.co/briaai/RMBG-2.0) | FP32 | 220.2M | — | 99.8% | HF repo metadata |
| [cocktailpeanut/fcanny](https://huggingface.co/cocktailpeanut/fcanny) | BF16 | 11.90B | 780 | 100.0% | safetensors header |
| [cocktailpeanut/fdepth](https://huggingface.co/cocktailpeanut/fdepth) | BF16 | 11.90B | 780 | 100.0% | safetensors header |
| [cocktailpeanut/fill](https://huggingface.co/cocktailpeanut/fill) | BF16 | 11.90B | 780 | 100.0% | safetensors header |
| [cocktailpeanut/flux1-merged-q8](https://huggingface.co/cocktailpeanut/flux1-merged-q8) | FP8 (E4M3FN) | 11.90B | 504 | 99.9% | safetensors header |
| [cocktailpeanut/flux1-merged-qint8](https://huggingface.co/cocktailpeanut/flux1-merged-qint8) | INT8 | 11.90B | 504 | 99.9% | safetensors header |
| [cocktailpeanut/flux1-schnell-q8](https://huggingface.co/cocktailpeanut/flux1-schnell-q8) | FP8 (E4M3FN) | 11.89B | 502 | 99.9% | safetensors header |
| [cocktailpeanut/flux1-schnell-qint8](https://huggingface.co/cocktailpeanut/flux1-schnell-qint8) | INT8 | 11.89B | 502 | 99.9% | safetensors header |
| [cocktailpeanut/redux](https://huggingface.co/cocktailpeanut/redux) | BF16 | 64.5M | 4 | 100.0% | safetensors header |
| [cocktailpeanut/sd35](https://huggingface.co/cocktailpeanut/sd35) | FP16 | 8.15B | 923 | 99.0% | safetensors header |
| [cocktailpeanut/sd35](https://huggingface.co/cocktailpeanut/sd35) | BF16 | 83.8M | 244 | 1.0% | safetensors header |
| [cocktailpeanut/sd35turbo](https://huggingface.co/cocktailpeanut/sd35turbo) | FP16 | 8.15B | 923 | 99.0% | safetensors header |
| [cocktailpeanut/sd35turbo](https://huggingface.co/cocktailpeanut/sd35turbo) | BF16 | 83.8M | 244 | 1.0% | safetensors header |
| [cocktailpeanut/sf3d](https://huggingface.co/cocktailpeanut/sf3d) | FP32 | 1.01B | 1276 | 100.0% | safetensors header |
| [cocktailpeanut/sisao](https://huggingface.co/cocktailpeanut/sisao) | FP32 | 837.2M | 530 | 100.0% | safetensors header |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | FP16 | 2.39B | 2446 | 100.0% | safetensors header |
| [cocktailpeanut/xulf-dev](https://huggingface.co/cocktailpeanut/xulf-dev) | BF16 | 11.90B | 780 | 99.3% | safetensors header |
| [cocktailpeanut/xulf-dev](https://huggingface.co/cocktailpeanut/xulf-dev) | FP32 | 83.8M | 244 | 0.7% | safetensors header |
| [cocktailpeanut/xulf-schnell](https://huggingface.co/cocktailpeanut/xulf-schnell) | BF16 | 11.89B | 776 | 99.3% | safetensors header |
| [cocktailpeanut/xulf-schnell](https://huggingface.co/cocktailpeanut/xulf-schnell) | FP32 | 83.8M | 244 | 0.7% | safetensors header |
| [Comfy-Org/flux1-dev](https://huggingface.co/Comfy-Org/flux1-dev) | FP8 (E4M3FN) | 16.66B | 999 | 98.8% | safetensors header |
| [Comfy-Org/flux1-dev](https://huggingface.co/Comfy-Org/flux1-dev) | FP16 | 123.7M | 197 | 0.7% | safetensors header |
| [Comfy-Org/flux1-dev](https://huggingface.co/Comfy-Org/flux1-dev) | FP32 | 83.8M | 246 | 0.5% | safetensors header |
| [Comfy-Org/flux1-schnell](https://huggingface.co/Comfy-Org/flux1-schnell) | FP8 (E4M3FN) | 16.65B | 995 | 98.8% | safetensors header |
| [Comfy-Org/flux1-schnell](https://huggingface.co/Comfy-Org/flux1-schnell) | FP16 | 123.7M | 197 | 0.7% | safetensors header |
| [Comfy-Org/flux1-schnell](https://huggingface.co/Comfy-Org/flux1-schnell) | FP32 | 83.8M | 246 | 0.5% | safetensors header |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | FP8 (E4M3FN) | 14.66B | 854 | 47.9% | safetensors header |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | BF16 | 10.03B | 1074 | 32.7% | safetensors header |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | FP16 | 5.95B | 1081 | 19.4% | safetensors header |
| [Comfy-Org/sigclip_vision_384](https://huggingface.co/Comfy-Org/sigclip_vision_384) | FP16 | 428.2M | 448 | 100.0% | safetensors header |
| [Comfy-Org/stable-diffusion-3.5-fp8](https://huggingface.co/Comfy-Org/stable-diffusion-3.5-fp8) | FP16 | 5.02B | 416 | 100.0% | safetensors header |
| [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged) | BF16 | 32.79B | 2606 | 83.8% | safetensors header |
| [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged) | FP8 (E4M3FN) | 4.63B | 169 | 11.8% | safetensors header |
| [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged) | FP16 | 1.68B | 594 | 4.3% | safetensors header |
| [comfyanonymous/flux_text_encoders](https://huggingface.co/comfyanonymous/flux_text_encoders) | FP16 | 5.02B | 416 | 50.6% | safetensors header |
| [comfyanonymous/flux_text_encoders](https://huggingface.co/comfyanonymous/flux_text_encoders) | FP8 (E4M3FN) | 4.89B | 220 | 49.4% | safetensors header |
| [drbaph/FLUX.1-schnell-dev-merged-fp8-4step](https://huggingface.co/drbaph/FLUX.1-schnell-dev-merged-fp8-4step) | FP8 (E4M3FN) | 11.89B | 776 | 70.5% | safetensors header |
| [drbaph/FLUX.1-schnell-dev-merged-fp8-4step](https://huggingface.co/drbaph/FLUX.1-schnell-dev-merged-fp8-4step) | FP16 | 4.89B | 416 | 29.0% | safetensors header |
| [drbaph/FLUX.1-schnell-dev-merged-fp8-4step](https://huggingface.co/drbaph/FLUX.1-schnell-dev-merged-fp8-4step) | BF16 | 83.8M | 244 | 0.5% | safetensors header |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | FP32 | 1.04B | 1146 | 100.0% | safetensors header |
| [genmo/mochi-1-preview](https://huggingface.co/genmo/mochi-1-preview) | FP32 | 10.49B | 1284 | 100.0% | safetensors header |
| [hunyuanvideo-community/HunyuanVideo](https://huggingface.co/hunyuanvideo-community/HunyuanVideo) | FP16 | 7.45B | 286 | 100.0% | safetensors header |
| [KBlueLeaf/kohaku-v2.1](https://huggingface.co/KBlueLeaf/kohaku-v2.1) | FP16 | 1.07B | 1130 | 100.0% | safetensors header |
| [Kijai/HunyuanVideo_comfy](https://huggingface.co/Kijai/HunyuanVideo_comfy) | FP8 (E4M3FN) | 12.46B | 320 | 95.3% | safetensors header |
| [Kijai/HunyuanVideo_comfy](https://huggingface.co/Kijai/HunyuanVideo_comfy) | BF16 | 610.4M | 784 | 4.7% | safetensors header |
| [Kijai/llava-llama-3-8b-text-encoder-tokenizer](https://huggingface.co/Kijai/llava-llama-3-8b-text-encoder-tokenizer) | FP16 | 7.45B | 286 | 100.0% | safetensors header |
| [latent-consistency/lcm-lora-sdv1-5](https://huggingface.co/latent-consistency/lcm-lora-sdv1-5) | FP16 | 67.3M | 834 | 100.0% | safetensors header |
| [latent-consistency/lcm-lora-sdxl](https://huggingface.co/latent-consistency/lcm-lora-sdxl) | FP16 | 196.8M | 2364 | 100.0% | safetensors header |
| [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video) | BF16 | 3.17B | 944 | 57.5% | safetensors header |
| [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video) | FP32 | 2.34B | 908 | 42.5% | safetensors header |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | FP16 | 3.33B | 3830 | 100.0% | safetensors header |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | NF4 (packed U8) | 12.08B | 1570 | 54.4% | safetensors header |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | FP8 (E4M3FN) | 9.52B | 438 | 42.9% | safetensors header |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | FP32 | 354.4M | 2366 | 1.6% | safetensors header |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | FP16 | 247.3M | 394 | 1.1% | safetensors header |
| [lllyasviel/flux1_dev](https://huggingface.co/lllyasviel/flux1_dev) | FP8 (E4M3FN) | 16.66B | 999 | 98.8% | safetensors header |
| [lllyasviel/flux1_dev](https://huggingface.co/lllyasviel/flux1_dev) | FP16 | 123.7M | 197 | 0.7% | safetensors header |
| [lllyasviel/flux1_dev](https://huggingface.co/lllyasviel/flux1_dev) | FP32 | 83.8M | 246 | 0.5% | safetensors header |
| [lllyasviel/flux_redux_bfl](https://huggingface.co/lllyasviel/flux_redux_bfl) | BF16 | 492.7M | 452 | 100.0% | safetensors header |
| [lllyasviel/FramePack_F1_I2V_HY_20250503](https://huggingface.co/lllyasviel/FramePack_F1_I2V_HY_20250503) | BF16 | 12.87B | 1274 | 100.0% | safetensors header |
| [lllyasviel/FramePackI2V_HY](https://huggingface.co/lllyasviel/FramePackI2V_HY) | BF16 | 12.87B | 1274 | 100.0% | safetensors header |
| [madebyollin/taesd](https://huggingface.co/madebyollin/taesd) | FP32 | 4.9M | 268 | 100.0% | safetensors header |
| [microsoft/OmniParser](https://huggingface.co/microsoft/OmniParser) | FP32 | 271.0M | 667 | 98.9% | safetensors header |
| [microsoft/OmniParser](https://huggingface.co/microsoft/OmniParser) | FP16 | 3.0M | 298 | 1.1% | safetensors header |
| [microsoft/VibeVoice-Realtime-0.5B](https://huggingface.co/microsoft/VibeVoice-Realtime-0.5B) | BF16 | 1.02B | 605 | 100.0% | safetensors header |
| [nari-labs/Dia-1.6B](https://huggingface.co/nari-labs/Dia-1.6B) | FP32 | 1.61B | 343 | 100.0% | safetensors header |
| [openai/clip-vit-large-patch14](https://huggingface.co/openai/clip-vit-large-patch14) | FP32 | 427.6M | 590 | 100.0% | safetensors header |
| [philz1337x/loras](https://huggingface.co/philz1337x/loras) | FP16 | 89.1M | 1368 | 97.4% | safetensors header |
| [philz1337x/loras](https://huggingface.co/philz1337x/loras) | FP32 | 2.4M | 792 | 2.6% | safetensors header |
| [refiners/controlnet.sd1_5.tile](https://huggingface.co/refiners/controlnet.sd1_5.tile) | FP16 | 361.3M | 340 | 100.0% | safetensors header |
| [refiners/juggernaut.reborn.sd1_5.autoencoder](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.autoencoder) | FP16 | 83.7M | 248 | 100.0% | safetensors header |
| [refiners/juggernaut.reborn.sd1_5.text_encoder](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.text_encoder) | FP16 | 123.1M | 196 | 100.0% | safetensors header |
| [refiners/juggernaut.reborn.sd1_5.unet](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.unet) | FP16 | 859.5M | 686 | 100.0% | safetensors header |
| [rhymes-ai/Allegro](https://huggingface.co/rhymes-ai/Allegro) | FP32 | 3.71B | 170 | 100.0% | safetensors header |
| [Roblox/cube3d-v0.1](https://huggingface.co/Roblox/cube3d-v0.1) | FP32 | 2.07B | 1092 | 100.0% | safetensors header |
| [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | FP32 | 1.93B | 1829 | 100.0% | safetensors header |
| [sayakpaul/FLUX.1-merged](https://huggingface.co/sayakpaul/FLUX.1-merged) | BF16 | 4.89B | 415 | 100.0% | safetensors header |
| [stabilityai/sd-turbo](https://huggingface.co/stabilityai/sd-turbo) | FP32 | 1.30B | 1229 | 100.0% | safetensors header |
| [stabilityai/sd-vae-ft-mse](https://huggingface.co/stabilityai/sd-vae-ft-mse) | FP32 | 83.7M | 248 | 100.0% | safetensors header |
| [stabilityai/sd-vae-ft-mse-original](https://huggingface.co/stabilityai/sd-vae-ft-mse-original) | FP32 | 83.7M | 249 | 100.0% | safetensors header |
| [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) | FP16 | 3.47B | 2515 | 100.0% | safetensors header |
| [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | FP16 | 3.47B | 2515 | 100.0% | safetensors header |
| [stabilityai/stable-diffusion-xl-refiner-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0) | FP16 | 3.04B | 1858 | 100.0% | safetensors header |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | FP32 | 2.39B | 2446 | 100.0% | safetensors header |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | FP32 | 2.39B | 2446 | 100.0% | safetensors header |
| [THUDM/CogVideoX-2B](https://huggingface.co/THUDM/CogVideoX-2B) | FP16 | 6.46B | 955 | 100.0% | safetensors header |
| [THUDM/CogVideoX-5b-I2V](https://huggingface.co/THUDM/CogVideoX-5b-I2V) | BF16 | 7.26B | 676 | 100.0% | safetensors header |
| [Tongyi-MAI/Z-Image-Turbo](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo) | BF16 | 4.02B | 398 | 100.0% | safetensors header |
| [XLabs-AI/flux-lora-collection](https://huggingface.co/XLabs-AI/flux-lora-collection) | BF16 | 246.5M | 608 | 100.0% | safetensors header |

## All tensor shapes

Every distinct tensor shape observed in the parsed safetensors headers of the launcher-requested files: **3118 shape entries** across 65 models. `Tensors` is how many tensors share that shape in the file(s), and `Params` is the shape product multiplied by that count. Shapes come directly from each safetensors header JSON, so they reflect the exact checkpoints the launchers download. Rows with only HF repo-aggregate metadata, or with no safetensors file (GGUF, `.pt`, gated repos), cannot contribute shapes.

| Model | File | Dtype | Shape | Tensors | Params |
| --- | --- | --- | --- | --- | --- |
| [AIDC-AI/Ovis-Image-7B](https://huggingface.co/AIDC-AI/Ovis-Image-7B) | `ovis_image.safetensors` | FP32 | `(33792, 3072)` | 27 | 2.80B |
| [AIDC-AI/Ovis-Image-7B](https://huggingface.co/AIDC-AI/Ovis-Image-7B) | `ovis_image.safetensors` | FP32 | `(3072, 15360)` | 27 | 1.27B |
| [AIDC-AI/Ovis-Image-7B](https://huggingface.co/AIDC-AI/Ovis-Image-7B) | `ovis_image.safetensors` | FP32 | `(9216, 3072)` | 39 | 1.10B |
| [AIDC-AI/Ovis-Image-7B](https://huggingface.co/AIDC-AI/Ovis-Image-7B) | `ovis_image.safetensors` | FP32 | `(12288, 3072)` | 24 | 906.0M |
| [AIDC-AI/Ovis-Image-7B](https://huggingface.co/AIDC-AI/Ovis-Image-7B) | `ovis_image.safetensors` | FP32 | `(18432, 3072)` | 12 | 679.5M |
| [AIDC-AI/Ovis-Image-7B](https://huggingface.co/AIDC-AI/Ovis-Image-7B) | `ovis_image.safetensors` | FP32 | `(3072, 12288)` | 12 | 453.0M |
| [AIDC-AI/Ovis-Image-7B](https://huggingface.co/AIDC-AI/Ovis-Image-7B) | `ovis_image.safetensors` | FP32 | `(3072, 3072)` | 13 | 122.7M |
| [AIDC-AI/Ovis-Image-7B](https://huggingface.co/AIDC-AI/Ovis-Image-7B) | `ae.safetensors` | FP32 | `(512, 512, 3, 3)` | 30 | 70.8M |
| [AIDC-AI/Ovis-Image-7B](https://huggingface.co/AIDC-AI/Ovis-Image-7B) | `ovis_image.safetensors` | FP32 | `(6144, 3072)` | 1 | 18.9M |
| [AIDC-AI/Ovis-Image-7B](https://huggingface.co/AIDC-AI/Ovis-Image-7B) | `ovis_image.safetensors` | FP32 | `(3072, 2048)` | 1 | 6.3M |
| [AIDC-AI/Ovis-Image-7B](https://huggingface.co/AIDC-AI/Ovis-Image-7B) | `ae.safetensors` | FP32 | `(256, 256, 3, 3)` | 10 | 5.9M |
| [AIDC-AI/Ovis-Image-7B](https://huggingface.co/AIDC-AI/Ovis-Image-7B) | `ae.safetensors` | FP32 | `(512, 512, 1, 1)` | 8 | 2.1M |
| [AIDC-AI/Ovis-Image-7B](https://huggingface.co/AIDC-AI/Ovis-Image-7B) | `ae.safetensors` | FP32 | `(128, 128, 3, 3)` | 10 | 1.5M |
| [AIDC-AI/Ovis-Image-7B](https://huggingface.co/AIDC-AI/Ovis-Image-7B) | `ae.safetensors` | FP32 | `(256, 512, 3, 3)` | 1 | 1.2M |
| [AIDC-AI/Ovis-Image-7B](https://huggingface.co/AIDC-AI/Ovis-Image-7B) | `ae.safetensors` | FP32 | `(512, 256, 3, 3)` | 1 | 1.2M |
| [AIDC-AI/Ovis-Image-7B](https://huggingface.co/AIDC-AI/Ovis-Image-7B) | `ovis_image.safetensors` | FP32 | `(33792)` | 27 | 912.4K |
| [AIDC-AI/Ovis-Image-7B](https://huggingface.co/AIDC-AI/Ovis-Image-7B) | `ovis_image.safetensors` | FP32 | `(3072, 256)` | 1 | 786.4K |
| [AIDC-AI/Ovis-Image-7B](https://huggingface.co/AIDC-AI/Ovis-Image-7B) | `ovis_image.safetensors` | FP32 | `(9216)` | 39 | 359.4K |
| [AIDC-AI/Ovis-Image-7B](https://huggingface.co/AIDC-AI/Ovis-Image-7B) | `ovis_image.safetensors` | FP32 | `(12288)` | 24 | 294.9K |
| [AIDC-AI/Ovis-Image-7B](https://huggingface.co/AIDC-AI/Ovis-Image-7B) | `ae.safetensors` | FP32 | `(128, 256, 3, 3)` | 1 | 294.9K |
| [AIDC-AI/Ovis-Image-7B](https://huggingface.co/AIDC-AI/Ovis-Image-7B) | `ae.safetensors` | FP32 | `(256, 128, 3, 3)` | 1 | 294.9K |
| [AIDC-AI/Ovis-Image-7B](https://huggingface.co/AIDC-AI/Ovis-Image-7B) | `ovis_image.safetensors` | FP32 | `(18432)` | 12 | 221.2K |
| [AIDC-AI/Ovis-Image-7B](https://huggingface.co/AIDC-AI/Ovis-Image-7B) | `ovis_image.safetensors` | FP32 | `(3072, 64)` | 1 | 196.6K |
| [AIDC-AI/Ovis-Image-7B](https://huggingface.co/AIDC-AI/Ovis-Image-7B) | `ovis_image.safetensors` | FP32 | `(64, 3072)` | 1 | 196.6K |
| [AIDC-AI/Ovis-Image-7B](https://huggingface.co/AIDC-AI/Ovis-Image-7B) | `ovis_image.safetensors` | FP32 | `(3072)` | 55 | 169.0K |
| [AIDC-AI/Ovis-Image-7B](https://huggingface.co/AIDC-AI/Ovis-Image-7B) | `ae.safetensors` | FP32 | `(32, 512, 3, 3)` | 1 | 147.5K |
| [AIDC-AI/Ovis-Image-7B](https://huggingface.co/AIDC-AI/Ovis-Image-7B) | `ae.safetensors` | FP32 | `(256, 512, 1, 1)` | 1 | 131.1K |
| [AIDC-AI/Ovis-Image-7B](https://huggingface.co/AIDC-AI/Ovis-Image-7B) | `ae.safetensors` | FP32 | `(512, 256, 1, 1)` | 1 | 131.1K |
| [AIDC-AI/Ovis-Image-7B](https://huggingface.co/AIDC-AI/Ovis-Image-7B) | `ae.safetensors` | FP32 | `(512, 16, 3, 3)` | 1 | 73.7K |
| [AIDC-AI/Ovis-Image-7B](https://huggingface.co/AIDC-AI/Ovis-Image-7B) | `ae.safetensors` | FP32 | `(512)` | 103 | 52.7K |
| [AIDC-AI/Ovis-Image-7B](https://huggingface.co/AIDC-AI/Ovis-Image-7B) | `ae.safetensors` | FP32 | `(128, 256, 1, 1)` | 1 | 32.8K |
| [AIDC-AI/Ovis-Image-7B](https://huggingface.co/AIDC-AI/Ovis-Image-7B) | `ae.safetensors` | FP32 | `(256, 128, 1, 1)` | 1 | 32.8K |
| [AIDC-AI/Ovis-Image-7B](https://huggingface.co/AIDC-AI/Ovis-Image-7B) | `ovis_image.safetensors` | FP32 | `(128)` | 78 | 10.0K |
| [AIDC-AI/Ovis-Image-7B](https://huggingface.co/AIDC-AI/Ovis-Image-7B) | `ae.safetensors` | FP32 | `(256)` | 34 | 8.7K |
| [AIDC-AI/Ovis-Image-7B](https://huggingface.co/AIDC-AI/Ovis-Image-7B) | `ovis_image.safetensors` | FP32 | `(6144)` | 1 | 6.1K |
| [AIDC-AI/Ovis-Image-7B](https://huggingface.co/AIDC-AI/Ovis-Image-7B) | `ae.safetensors` | FP32 | `(128)` | 35 | 4.5K |
| [AIDC-AI/Ovis-Image-7B](https://huggingface.co/AIDC-AI/Ovis-Image-7B) | `ae.safetensors` | FP32 | `(128, 3, 3, 3)` | 1 | 3.5K |
| [AIDC-AI/Ovis-Image-7B](https://huggingface.co/AIDC-AI/Ovis-Image-7B) | `ae.safetensors` | FP32 | `(3, 128, 3, 3)` | 1 | 3.5K |
| [AIDC-AI/Ovis-Image-7B](https://huggingface.co/AIDC-AI/Ovis-Image-7B) | `ovis_image.safetensors` | FP32 | `(2048)` | 1 | 2.0K |
| [AIDC-AI/Ovis-Image-7B](https://huggingface.co/AIDC-AI/Ovis-Image-7B) | `ovis_image.safetensors` | FP32 | `(64)` | 1 | 64 |
| [AIDC-AI/Ovis-Image-7B](https://huggingface.co/AIDC-AI/Ovis-Image-7B) | `ae.safetensors` | FP32 | `(32)` | 1 | 32 |
| [AIDC-AI/Ovis-Image-7B](https://huggingface.co/AIDC-AI/Ovis-Image-7B) | `ae.safetensors` | FP32 | `(3)` | 1 | 3 |
| [cocktailpeanut/fcanny](https://huggingface.co/cocktailpeanut/fcanny) | `flux1-canny-dev.safetensors` | BF16 | `(21504, 3072)` | 38 | 2.51B |
| [cocktailpeanut/fcanny](https://huggingface.co/cocktailpeanut/fcanny) | `flux1-canny-dev.safetensors` | BF16 | `(18432, 3072)` | 38 | 2.15B |
| [cocktailpeanut/fcanny](https://huggingface.co/cocktailpeanut/fcanny) | `flux1-canny-dev.safetensors` | BF16 | `(9216, 3072)` | 76 | 2.15B |
| [cocktailpeanut/fcanny](https://huggingface.co/cocktailpeanut/fcanny) | `flux1-canny-dev.safetensors` | BF16 | `(3072, 15360)` | 38 | 1.79B |
| [cocktailpeanut/fcanny](https://huggingface.co/cocktailpeanut/fcanny) | `flux1-canny-dev.safetensors` | BF16 | `(12288, 3072)` | 38 | 1.43B |
| [cocktailpeanut/fcanny](https://huggingface.co/cocktailpeanut/fcanny) | `flux1-canny-dev.safetensors` | BF16 | `(3072, 12288)` | 38 | 1.43B |
| [cocktailpeanut/fcanny](https://huggingface.co/cocktailpeanut/fcanny) | `flux1-canny-dev.safetensors` | BF16 | `(3072, 3072)` | 41 | 386.9M |
| [cocktailpeanut/fcanny](https://huggingface.co/cocktailpeanut/fcanny) | `flux1-canny-dev.safetensors` | BF16 | `(6144, 3072)` | 1 | 18.9M |
| [cocktailpeanut/fcanny](https://huggingface.co/cocktailpeanut/fcanny) | `flux1-canny-dev.safetensors` | BF16 | `(3072, 4096)` | 1 | 12.6M |
| [cocktailpeanut/fcanny](https://huggingface.co/cocktailpeanut/fcanny) | `flux1-canny-dev.safetensors` | BF16 | `(3072, 768)` | 1 | 2.4M |
| [cocktailpeanut/fcanny](https://huggingface.co/cocktailpeanut/fcanny) | `flux1-canny-dev.safetensors` | BF16 | `(3072, 256)` | 2 | 1.6M |
| [cocktailpeanut/fcanny](https://huggingface.co/cocktailpeanut/fcanny) | `flux1-canny-dev.safetensors` | BF16 | `(21504)` | 38 | 817.2K |
| [cocktailpeanut/fcanny](https://huggingface.co/cocktailpeanut/fcanny) | `flux1-canny-dev.safetensors` | BF16 | `(18432)` | 38 | 700.4K |
| [cocktailpeanut/fcanny](https://huggingface.co/cocktailpeanut/fcanny) | `flux1-canny-dev.safetensors` | BF16 | `(9216)` | 76 | 700.4K |
| [cocktailpeanut/fcanny](https://huggingface.co/cocktailpeanut/fcanny) | `flux1-canny-dev.safetensors` | BF16 | `(12288)` | 38 | 466.9K |
| [cocktailpeanut/fcanny](https://huggingface.co/cocktailpeanut/fcanny) | `flux1-canny-dev.safetensors` | BF16 | `(3072, 128)` | 1 | 393.2K |
| [cocktailpeanut/fcanny](https://huggingface.co/cocktailpeanut/fcanny) | `flux1-canny-dev.safetensors` | BF16 | `(3072)` | 122 | 374.8K |
| [cocktailpeanut/fcanny](https://huggingface.co/cocktailpeanut/fcanny) | `flux1-canny-dev.safetensors` | BF16 | `(64, 3072)` | 1 | 196.6K |
| [cocktailpeanut/fcanny](https://huggingface.co/cocktailpeanut/fcanny) | `flux1-canny-dev.safetensors` | BF16 | `(128)` | 152 | 19.5K |
| [cocktailpeanut/fcanny](https://huggingface.co/cocktailpeanut/fcanny) | `flux1-canny-dev.safetensors` | BF16 | `(6144)` | 1 | 6.1K |
| [cocktailpeanut/fcanny](https://huggingface.co/cocktailpeanut/fcanny) | `flux1-canny-dev.safetensors` | BF16 | `(64)` | 1 | 64 |
| [cocktailpeanut/fdepth](https://huggingface.co/cocktailpeanut/fdepth) | `flux1-depth-dev.safetensors` | BF16 | `(21504, 3072)` | 38 | 2.51B |
| [cocktailpeanut/fdepth](https://huggingface.co/cocktailpeanut/fdepth) | `flux1-depth-dev.safetensors` | BF16 | `(18432, 3072)` | 38 | 2.15B |
| [cocktailpeanut/fdepth](https://huggingface.co/cocktailpeanut/fdepth) | `flux1-depth-dev.safetensors` | BF16 | `(9216, 3072)` | 76 | 2.15B |
| [cocktailpeanut/fdepth](https://huggingface.co/cocktailpeanut/fdepth) | `flux1-depth-dev.safetensors` | BF16 | `(3072, 15360)` | 38 | 1.79B |
| [cocktailpeanut/fdepth](https://huggingface.co/cocktailpeanut/fdepth) | `flux1-depth-dev.safetensors` | BF16 | `(12288, 3072)` | 38 | 1.43B |
| [cocktailpeanut/fdepth](https://huggingface.co/cocktailpeanut/fdepth) | `flux1-depth-dev.safetensors` | BF16 | `(3072, 12288)` | 38 | 1.43B |
| [cocktailpeanut/fdepth](https://huggingface.co/cocktailpeanut/fdepth) | `flux1-depth-dev.safetensors` | BF16 | `(3072, 3072)` | 41 | 386.9M |
| [cocktailpeanut/fdepth](https://huggingface.co/cocktailpeanut/fdepth) | `flux1-depth-dev.safetensors` | BF16 | `(6144, 3072)` | 1 | 18.9M |
| [cocktailpeanut/fdepth](https://huggingface.co/cocktailpeanut/fdepth) | `flux1-depth-dev.safetensors` | BF16 | `(3072, 4096)` | 1 | 12.6M |
| [cocktailpeanut/fdepth](https://huggingface.co/cocktailpeanut/fdepth) | `flux1-depth-dev.safetensors` | BF16 | `(3072, 768)` | 1 | 2.4M |
| [cocktailpeanut/fdepth](https://huggingface.co/cocktailpeanut/fdepth) | `flux1-depth-dev.safetensors` | BF16 | `(3072, 256)` | 2 | 1.6M |
| [cocktailpeanut/fdepth](https://huggingface.co/cocktailpeanut/fdepth) | `flux1-depth-dev.safetensors` | BF16 | `(21504)` | 38 | 817.2K |
| [cocktailpeanut/fdepth](https://huggingface.co/cocktailpeanut/fdepth) | `flux1-depth-dev.safetensors` | BF16 | `(18432)` | 38 | 700.4K |
| [cocktailpeanut/fdepth](https://huggingface.co/cocktailpeanut/fdepth) | `flux1-depth-dev.safetensors` | BF16 | `(9216)` | 76 | 700.4K |
| [cocktailpeanut/fdepth](https://huggingface.co/cocktailpeanut/fdepth) | `flux1-depth-dev.safetensors` | BF16 | `(12288)` | 38 | 466.9K |
| [cocktailpeanut/fdepth](https://huggingface.co/cocktailpeanut/fdepth) | `flux1-depth-dev.safetensors` | BF16 | `(3072, 128)` | 1 | 393.2K |
| [cocktailpeanut/fdepth](https://huggingface.co/cocktailpeanut/fdepth) | `flux1-depth-dev.safetensors` | BF16 | `(3072)` | 122 | 374.8K |
| [cocktailpeanut/fdepth](https://huggingface.co/cocktailpeanut/fdepth) | `flux1-depth-dev.safetensors` | BF16 | `(64, 3072)` | 1 | 196.6K |
| [cocktailpeanut/fdepth](https://huggingface.co/cocktailpeanut/fdepth) | `flux1-depth-dev.safetensors` | BF16 | `(128)` | 152 | 19.5K |
| [cocktailpeanut/fdepth](https://huggingface.co/cocktailpeanut/fdepth) | `flux1-depth-dev.safetensors` | BF16 | `(6144)` | 1 | 6.1K |
| [cocktailpeanut/fdepth](https://huggingface.co/cocktailpeanut/fdepth) | `flux1-depth-dev.safetensors` | BF16 | `(64)` | 1 | 64 |
| [cocktailpeanut/fill](https://huggingface.co/cocktailpeanut/fill) | `flux1-fill-dev.safetensors` | BF16 | `(21504, 3072)` | 38 | 2.51B |
| [cocktailpeanut/fill](https://huggingface.co/cocktailpeanut/fill) | `flux1-fill-dev.safetensors` | BF16 | `(18432, 3072)` | 38 | 2.15B |
| [cocktailpeanut/fill](https://huggingface.co/cocktailpeanut/fill) | `flux1-fill-dev.safetensors` | BF16 | `(9216, 3072)` | 76 | 2.15B |
| [cocktailpeanut/fill](https://huggingface.co/cocktailpeanut/fill) | `flux1-fill-dev.safetensors` | BF16 | `(3072, 15360)` | 38 | 1.79B |
| [cocktailpeanut/fill](https://huggingface.co/cocktailpeanut/fill) | `flux1-fill-dev.safetensors` | BF16 | `(12288, 3072)` | 38 | 1.43B |
| [cocktailpeanut/fill](https://huggingface.co/cocktailpeanut/fill) | `flux1-fill-dev.safetensors` | BF16 | `(3072, 12288)` | 38 | 1.43B |
| [cocktailpeanut/fill](https://huggingface.co/cocktailpeanut/fill) | `flux1-fill-dev.safetensors` | BF16 | `(3072, 3072)` | 41 | 386.9M |
| [cocktailpeanut/fill](https://huggingface.co/cocktailpeanut/fill) | `flux1-fill-dev.safetensors` | BF16 | `(6144, 3072)` | 1 | 18.9M |
| [cocktailpeanut/fill](https://huggingface.co/cocktailpeanut/fill) | `flux1-fill-dev.safetensors` | BF16 | `(3072, 4096)` | 1 | 12.6M |
| [cocktailpeanut/fill](https://huggingface.co/cocktailpeanut/fill) | `flux1-fill-dev.safetensors` | BF16 | `(3072, 768)` | 1 | 2.4M |
| [cocktailpeanut/fill](https://huggingface.co/cocktailpeanut/fill) | `flux1-fill-dev.safetensors` | BF16 | `(3072, 256)` | 2 | 1.6M |
| [cocktailpeanut/fill](https://huggingface.co/cocktailpeanut/fill) | `flux1-fill-dev.safetensors` | BF16 | `(3072, 384)` | 1 | 1.2M |
| [cocktailpeanut/fill](https://huggingface.co/cocktailpeanut/fill) | `flux1-fill-dev.safetensors` | BF16 | `(21504)` | 38 | 817.2K |
| [cocktailpeanut/fill](https://huggingface.co/cocktailpeanut/fill) | `flux1-fill-dev.safetensors` | BF16 | `(18432)` | 38 | 700.4K |
| [cocktailpeanut/fill](https://huggingface.co/cocktailpeanut/fill) | `flux1-fill-dev.safetensors` | BF16 | `(9216)` | 76 | 700.4K |
| [cocktailpeanut/fill](https://huggingface.co/cocktailpeanut/fill) | `flux1-fill-dev.safetensors` | BF16 | `(12288)` | 38 | 466.9K |
| [cocktailpeanut/fill](https://huggingface.co/cocktailpeanut/fill) | `flux1-fill-dev.safetensors` | BF16 | `(3072)` | 122 | 374.8K |
| [cocktailpeanut/fill](https://huggingface.co/cocktailpeanut/fill) | `flux1-fill-dev.safetensors` | BF16 | `(64, 3072)` | 1 | 196.6K |
| [cocktailpeanut/fill](https://huggingface.co/cocktailpeanut/fill) | `flux1-fill-dev.safetensors` | BF16 | `(128)` | 152 | 19.5K |
| [cocktailpeanut/fill](https://huggingface.co/cocktailpeanut/fill) | `flux1-fill-dev.safetensors` | BF16 | `(6144)` | 1 | 6.1K |
| [cocktailpeanut/fill](https://huggingface.co/cocktailpeanut/fill) | `flux1-fill-dev.safetensors` | BF16 | `(64)` | 1 | 64 |
| [cocktailpeanut/flux1-merged-q8](https://huggingface.co/cocktailpeanut/flux1-merged-q8) | `diffusion_pytorch_model-00001-of-00002.safetensors` | BF16 | `(3072)` | 294 | 903.2K |
| [cocktailpeanut/flux1-merged-q8](https://huggingface.co/cocktailpeanut/flux1-merged-q8) | `diffusion_pytorch_model-00001-of-00002.safetensors` | BF16 | `(3072, 1)` | 294 | 903.2K |
| [cocktailpeanut/flux1-merged-q8](https://huggingface.co/cocktailpeanut/flux1-merged-q8) | `diffusion_pytorch_model-00001-of-00002.safetensors` | BF16 | `(12288)` | 63 | 774.1K |
| [cocktailpeanut/flux1-merged-q8](https://huggingface.co/cocktailpeanut/flux1-merged-q8) | `diffusion_pytorch_model-00001-of-00002.safetensors` | BF16 | `(12288, 1)` | 63 | 774.1K |
| [cocktailpeanut/flux1-merged-q8](https://huggingface.co/cocktailpeanut/flux1-merged-q8) | `diffusion_pytorch_model-00001-of-00002.safetensors` | BF16 | `(18432)` | 38 | 700.4K |
| [cocktailpeanut/flux1-merged-q8](https://huggingface.co/cocktailpeanut/flux1-merged-q8) | `diffusion_pytorch_model-00001-of-00002.safetensors` | BF16 | `(18432, 1)` | 38 | 700.4K |
| [cocktailpeanut/flux1-merged-q8](https://huggingface.co/cocktailpeanut/flux1-merged-q8) | `diffusion_pytorch_model-00001-of-00002.safetensors` | BF16 | `(9216)` | 25 | 230.4K |
| [cocktailpeanut/flux1-merged-q8](https://huggingface.co/cocktailpeanut/flux1-merged-q8) | `diffusion_pytorch_model-00001-of-00002.safetensors` | BF16 | `(9216, 1)` | 25 | 230.4K |
| [cocktailpeanut/flux1-merged-q8](https://huggingface.co/cocktailpeanut/flux1-merged-q8) | `diffusion_pytorch_model-00002-of-00002.safetensors` | BF16 | `(3072)` | 56 | 172.0K |
| [cocktailpeanut/flux1-merged-q8](https://huggingface.co/cocktailpeanut/flux1-merged-q8) | `diffusion_pytorch_model-00002-of-00002.safetensors` | BF16 | `(3072, 1)` | 56 | 172.0K |
| [cocktailpeanut/flux1-merged-q8](https://huggingface.co/cocktailpeanut/flux1-merged-q8) | `diffusion_pytorch_model-00002-of-00002.safetensors` | BF16 | `(12288)` | 13 | 159.7K |
| [cocktailpeanut/flux1-merged-q8](https://huggingface.co/cocktailpeanut/flux1-merged-q8) | `diffusion_pytorch_model-00002-of-00002.safetensors` | BF16 | `(12288, 1)` | 13 | 159.7K |
| [cocktailpeanut/flux1-merged-q8](https://huggingface.co/cocktailpeanut/flux1-merged-q8) | `diffusion_pytorch_model-00002-of-00002.safetensors` | BF16 | `(9216)` | 13 | 119.8K |
| [cocktailpeanut/flux1-merged-q8](https://huggingface.co/cocktailpeanut/flux1-merged-q8) | `diffusion_pytorch_model-00002-of-00002.safetensors` | BF16 | `(9216, 1)` | 13 | 119.8K |
| [cocktailpeanut/flux1-merged-q8](https://huggingface.co/cocktailpeanut/flux1-merged-q8) | `diffusion_pytorch_model-00001-of-00002.safetensors` | BF16 | `(128)` | 124 | 15.9K |
| [cocktailpeanut/flux1-merged-q8](https://huggingface.co/cocktailpeanut/flux1-merged-q8) | `diffusion_pytorch_model-00002-of-00002.safetensors` | BF16 | `(6144)` | 1 | 6.1K |
| [cocktailpeanut/flux1-merged-q8](https://huggingface.co/cocktailpeanut/flux1-merged-q8) | `diffusion_pytorch_model-00002-of-00002.safetensors` | BF16 | `(6144, 1)` | 1 | 6.1K |
| [cocktailpeanut/flux1-merged-q8](https://huggingface.co/cocktailpeanut/flux1-merged-q8) | `diffusion_pytorch_model-00002-of-00002.safetensors` | BF16 | `(128)` | 28 | 3.6K |
| [cocktailpeanut/flux1-merged-q8](https://huggingface.co/cocktailpeanut/flux1-merged-q8) | `diffusion_pytorch_model-00002-of-00002.safetensors` | BF16 | `(64)` | 1 | 64 |
| [cocktailpeanut/flux1-merged-q8](https://huggingface.co/cocktailpeanut/flux1-merged-q8) | `diffusion_pytorch_model-00002-of-00002.safetensors` | BF16 | `(64, 1)` | 1 | 64 |
| [cocktailpeanut/flux1-merged-q8](https://huggingface.co/cocktailpeanut/flux1-merged-q8) | `diffusion_pytorch_model-00001-of-00002.safetensors` | FP32 | `()` | 840 | 840 |
| [cocktailpeanut/flux1-merged-q8](https://huggingface.co/cocktailpeanut/flux1-merged-q8) | `diffusion_pytorch_model-00002-of-00002.safetensors` | FP32 | `()` | 168 | 168 |
| [cocktailpeanut/flux1-merged-q8](https://huggingface.co/cocktailpeanut/flux1-merged-q8) | `diffusion_pytorch_model-00001-of-00002.safetensors` | FP8 (E4M3FN) | `(12288, 3072)` | 63 | 2.38B |
| [cocktailpeanut/flux1-merged-q8](https://huggingface.co/cocktailpeanut/flux1-merged-q8) | `diffusion_pytorch_model-00001-of-00002.safetensors` | FP8 (E4M3FN) | `(18432, 3072)` | 38 | 2.15B |
| [cocktailpeanut/flux1-merged-q8](https://huggingface.co/cocktailpeanut/flux1-merged-q8) | `diffusion_pytorch_model-00001-of-00002.safetensors` | FP8 (E4M3FN) | `(3072, 3072)` | 227 | 2.14B |
| [cocktailpeanut/flux1-merged-q8](https://huggingface.co/cocktailpeanut/flux1-merged-q8) | `diffusion_pytorch_model-00001-of-00002.safetensors` | FP8 (E4M3FN) | `(3072, 12288)` | 38 | 1.43B |
| [cocktailpeanut/flux1-merged-q8](https://huggingface.co/cocktailpeanut/flux1-merged-q8) | `diffusion_pytorch_model-00001-of-00002.safetensors` | FP8 (E4M3FN) | `(3072, 15360)` | 24 | 1.13B |
| [cocktailpeanut/flux1-merged-q8](https://huggingface.co/cocktailpeanut/flux1-merged-q8) | `diffusion_pytorch_model-00001-of-00002.safetensors` | FP8 (E4M3FN) | `(9216, 3072)` | 25 | 707.8M |
| [cocktailpeanut/flux1-merged-q8](https://huggingface.co/cocktailpeanut/flux1-merged-q8) | `diffusion_pytorch_model-00002-of-00002.safetensors` | FP8 (E4M3FN) | `(3072, 15360)` | 14 | 660.6M |
| [cocktailpeanut/flux1-merged-q8](https://huggingface.co/cocktailpeanut/flux1-merged-q8) | `diffusion_pytorch_model-00002-of-00002.safetensors` | FP8 (E4M3FN) | `(12288, 3072)` | 13 | 490.7M |
| [cocktailpeanut/flux1-merged-q8](https://huggingface.co/cocktailpeanut/flux1-merged-q8) | `diffusion_pytorch_model-00002-of-00002.safetensors` | FP8 (E4M3FN) | `(3072, 3072)` | 42 | 396.4M |
| [cocktailpeanut/flux1-merged-q8](https://huggingface.co/cocktailpeanut/flux1-merged-q8) | `diffusion_pytorch_model-00002-of-00002.safetensors` | FP8 (E4M3FN) | `(9216, 3072)` | 13 | 368.1M |
| [cocktailpeanut/flux1-merged-q8](https://huggingface.co/cocktailpeanut/flux1-merged-q8) | `diffusion_pytorch_model-00002-of-00002.safetensors` | FP8 (E4M3FN) | `(6144, 3072)` | 1 | 18.9M |
| [cocktailpeanut/flux1-merged-q8](https://huggingface.co/cocktailpeanut/flux1-merged-q8) | `diffusion_pytorch_model-00001-of-00002.safetensors` | FP8 (E4M3FN) | `(3072, 4096)` | 1 | 12.6M |
| [cocktailpeanut/flux1-merged-q8](https://huggingface.co/cocktailpeanut/flux1-merged-q8) | `diffusion_pytorch_model-00001-of-00002.safetensors` | FP8 (E4M3FN) | `(3072, 768)` | 1 | 2.4M |
| [cocktailpeanut/flux1-merged-q8](https://huggingface.co/cocktailpeanut/flux1-merged-q8) | `diffusion_pytorch_model-00001-of-00002.safetensors` | FP8 (E4M3FN) | `(3072, 256)` | 2 | 1.6M |
| [cocktailpeanut/flux1-merged-q8](https://huggingface.co/cocktailpeanut/flux1-merged-q8) | `diffusion_pytorch_model-00001-of-00002.safetensors` | FP8 (E4M3FN) | `(3072, 64)` | 1 | 196.6K |
| [cocktailpeanut/flux1-merged-q8](https://huggingface.co/cocktailpeanut/flux1-merged-q8) | `diffusion_pytorch_model-00002-of-00002.safetensors` | FP8 (E4M3FN) | `(64, 3072)` | 1 | 196.6K |
| [cocktailpeanut/flux1-merged-qint8](https://huggingface.co/cocktailpeanut/flux1-merged-qint8) | `diffusion_pytorch_model-00001-of-00002.safetensors` | BF16 | `(3072)` | 294 | 903.2K |
| [cocktailpeanut/flux1-merged-qint8](https://huggingface.co/cocktailpeanut/flux1-merged-qint8) | `diffusion_pytorch_model-00001-of-00002.safetensors` | BF16 | `(3072, 1)` | 294 | 903.2K |
| [cocktailpeanut/flux1-merged-qint8](https://huggingface.co/cocktailpeanut/flux1-merged-qint8) | `diffusion_pytorch_model-00001-of-00002.safetensors` | BF16 | `(12288)` | 63 | 774.1K |
| [cocktailpeanut/flux1-merged-qint8](https://huggingface.co/cocktailpeanut/flux1-merged-qint8) | `diffusion_pytorch_model-00001-of-00002.safetensors` | BF16 | `(12288, 1)` | 63 | 774.1K |
| [cocktailpeanut/flux1-merged-qint8](https://huggingface.co/cocktailpeanut/flux1-merged-qint8) | `diffusion_pytorch_model-00001-of-00002.safetensors` | BF16 | `(18432)` | 38 | 700.4K |
| [cocktailpeanut/flux1-merged-qint8](https://huggingface.co/cocktailpeanut/flux1-merged-qint8) | `diffusion_pytorch_model-00001-of-00002.safetensors` | BF16 | `(18432, 1)` | 38 | 700.4K |
| [cocktailpeanut/flux1-merged-qint8](https://huggingface.co/cocktailpeanut/flux1-merged-qint8) | `diffusion_pytorch_model-00001-of-00002.safetensors` | BF16 | `(9216)` | 25 | 230.4K |
| [cocktailpeanut/flux1-merged-qint8](https://huggingface.co/cocktailpeanut/flux1-merged-qint8) | `diffusion_pytorch_model-00001-of-00002.safetensors` | BF16 | `(9216, 1)` | 25 | 230.4K |
| [cocktailpeanut/flux1-merged-qint8](https://huggingface.co/cocktailpeanut/flux1-merged-qint8) | `diffusion_pytorch_model-00002-of-00002.safetensors` | BF16 | `(3072)` | 56 | 172.0K |
| [cocktailpeanut/flux1-merged-qint8](https://huggingface.co/cocktailpeanut/flux1-merged-qint8) | `diffusion_pytorch_model-00002-of-00002.safetensors` | BF16 | `(3072, 1)` | 56 | 172.0K |
| [cocktailpeanut/flux1-merged-qint8](https://huggingface.co/cocktailpeanut/flux1-merged-qint8) | `diffusion_pytorch_model-00002-of-00002.safetensors` | BF16 | `(12288)` | 13 | 159.7K |
| [cocktailpeanut/flux1-merged-qint8](https://huggingface.co/cocktailpeanut/flux1-merged-qint8) | `diffusion_pytorch_model-00002-of-00002.safetensors` | BF16 | `(12288, 1)` | 13 | 159.7K |
| [cocktailpeanut/flux1-merged-qint8](https://huggingface.co/cocktailpeanut/flux1-merged-qint8) | `diffusion_pytorch_model-00002-of-00002.safetensors` | BF16 | `(9216)` | 13 | 119.8K |
| [cocktailpeanut/flux1-merged-qint8](https://huggingface.co/cocktailpeanut/flux1-merged-qint8) | `diffusion_pytorch_model-00002-of-00002.safetensors` | BF16 | `(9216, 1)` | 13 | 119.8K |
| [cocktailpeanut/flux1-merged-qint8](https://huggingface.co/cocktailpeanut/flux1-merged-qint8) | `diffusion_pytorch_model-00001-of-00002.safetensors` | BF16 | `(128)` | 124 | 15.9K |
| [cocktailpeanut/flux1-merged-qint8](https://huggingface.co/cocktailpeanut/flux1-merged-qint8) | `diffusion_pytorch_model-00002-of-00002.safetensors` | BF16 | `(6144)` | 1 | 6.1K |
| [cocktailpeanut/flux1-merged-qint8](https://huggingface.co/cocktailpeanut/flux1-merged-qint8) | `diffusion_pytorch_model-00002-of-00002.safetensors` | BF16 | `(6144, 1)` | 1 | 6.1K |
| [cocktailpeanut/flux1-merged-qint8](https://huggingface.co/cocktailpeanut/flux1-merged-qint8) | `diffusion_pytorch_model-00002-of-00002.safetensors` | BF16 | `(128)` | 28 | 3.6K |
| [cocktailpeanut/flux1-merged-qint8](https://huggingface.co/cocktailpeanut/flux1-merged-qint8) | `diffusion_pytorch_model-00002-of-00002.safetensors` | BF16 | `(64)` | 1 | 64 |
| [cocktailpeanut/flux1-merged-qint8](https://huggingface.co/cocktailpeanut/flux1-merged-qint8) | `diffusion_pytorch_model-00002-of-00002.safetensors` | BF16 | `(64, 1)` | 1 | 64 |
| [cocktailpeanut/flux1-merged-qint8](https://huggingface.co/cocktailpeanut/flux1-merged-qint8) | `diffusion_pytorch_model-00001-of-00002.safetensors` | FP32 | `()` | 840 | 840 |
| [cocktailpeanut/flux1-merged-qint8](https://huggingface.co/cocktailpeanut/flux1-merged-qint8) | `diffusion_pytorch_model-00002-of-00002.safetensors` | FP32 | `()` | 168 | 168 |
| [cocktailpeanut/flux1-merged-qint8](https://huggingface.co/cocktailpeanut/flux1-merged-qint8) | `diffusion_pytorch_model-00001-of-00002.safetensors` | INT8 | `(12288, 3072)` | 63 | 2.38B |
| [cocktailpeanut/flux1-merged-qint8](https://huggingface.co/cocktailpeanut/flux1-merged-qint8) | `diffusion_pytorch_model-00001-of-00002.safetensors` | INT8 | `(18432, 3072)` | 38 | 2.15B |
| [cocktailpeanut/flux1-merged-qint8](https://huggingface.co/cocktailpeanut/flux1-merged-qint8) | `diffusion_pytorch_model-00001-of-00002.safetensors` | INT8 | `(3072, 3072)` | 227 | 2.14B |
| [cocktailpeanut/flux1-merged-qint8](https://huggingface.co/cocktailpeanut/flux1-merged-qint8) | `diffusion_pytorch_model-00001-of-00002.safetensors` | INT8 | `(3072, 12288)` | 38 | 1.43B |
| [cocktailpeanut/flux1-merged-qint8](https://huggingface.co/cocktailpeanut/flux1-merged-qint8) | `diffusion_pytorch_model-00001-of-00002.safetensors` | INT8 | `(3072, 15360)` | 24 | 1.13B |
| [cocktailpeanut/flux1-merged-qint8](https://huggingface.co/cocktailpeanut/flux1-merged-qint8) | `diffusion_pytorch_model-00001-of-00002.safetensors` | INT8 | `(9216, 3072)` | 25 | 707.8M |
| [cocktailpeanut/flux1-merged-qint8](https://huggingface.co/cocktailpeanut/flux1-merged-qint8) | `diffusion_pytorch_model-00002-of-00002.safetensors` | INT8 | `(3072, 15360)` | 14 | 660.6M |
| [cocktailpeanut/flux1-merged-qint8](https://huggingface.co/cocktailpeanut/flux1-merged-qint8) | `diffusion_pytorch_model-00002-of-00002.safetensors` | INT8 | `(12288, 3072)` | 13 | 490.7M |
| [cocktailpeanut/flux1-merged-qint8](https://huggingface.co/cocktailpeanut/flux1-merged-qint8) | `diffusion_pytorch_model-00002-of-00002.safetensors` | INT8 | `(3072, 3072)` | 42 | 396.4M |
| [cocktailpeanut/flux1-merged-qint8](https://huggingface.co/cocktailpeanut/flux1-merged-qint8) | `diffusion_pytorch_model-00002-of-00002.safetensors` | INT8 | `(9216, 3072)` | 13 | 368.1M |
| [cocktailpeanut/flux1-merged-qint8](https://huggingface.co/cocktailpeanut/flux1-merged-qint8) | `diffusion_pytorch_model-00002-of-00002.safetensors` | INT8 | `(6144, 3072)` | 1 | 18.9M |
| [cocktailpeanut/flux1-merged-qint8](https://huggingface.co/cocktailpeanut/flux1-merged-qint8) | `diffusion_pytorch_model-00001-of-00002.safetensors` | INT8 | `(3072, 4096)` | 1 | 12.6M |
| [cocktailpeanut/flux1-merged-qint8](https://huggingface.co/cocktailpeanut/flux1-merged-qint8) | `diffusion_pytorch_model-00001-of-00002.safetensors` | INT8 | `(3072, 768)` | 1 | 2.4M |
| [cocktailpeanut/flux1-merged-qint8](https://huggingface.co/cocktailpeanut/flux1-merged-qint8) | `diffusion_pytorch_model-00001-of-00002.safetensors` | INT8 | `(3072, 256)` | 2 | 1.6M |
| [cocktailpeanut/flux1-merged-qint8](https://huggingface.co/cocktailpeanut/flux1-merged-qint8) | `diffusion_pytorch_model-00001-of-00002.safetensors` | INT8 | `(3072, 64)` | 1 | 196.6K |
| [cocktailpeanut/flux1-merged-qint8](https://huggingface.co/cocktailpeanut/flux1-merged-qint8) | `diffusion_pytorch_model-00002-of-00002.safetensors` | INT8 | `(64, 3072)` | 1 | 196.6K |
| [cocktailpeanut/flux1-schnell-q8](https://huggingface.co/cocktailpeanut/flux1-schnell-q8) | `diffusion_pytorch_model-00001-of-00002.safetensors` | BF16 | `(3072)` | 292 | 897.0K |
| [cocktailpeanut/flux1-schnell-q8](https://huggingface.co/cocktailpeanut/flux1-schnell-q8) | `diffusion_pytorch_model-00001-of-00002.safetensors` | BF16 | `(3072, 1)` | 292 | 897.0K |
| [cocktailpeanut/flux1-schnell-q8](https://huggingface.co/cocktailpeanut/flux1-schnell-q8) | `diffusion_pytorch_model-00001-of-00002.safetensors` | BF16 | `(12288)` | 63 | 774.1K |
| [cocktailpeanut/flux1-schnell-q8](https://huggingface.co/cocktailpeanut/flux1-schnell-q8) | `diffusion_pytorch_model-00001-of-00002.safetensors` | BF16 | `(12288, 1)` | 63 | 774.1K |
| [cocktailpeanut/flux1-schnell-q8](https://huggingface.co/cocktailpeanut/flux1-schnell-q8) | `diffusion_pytorch_model-00001-of-00002.safetensors` | BF16 | `(18432)` | 38 | 700.4K |
| [cocktailpeanut/flux1-schnell-q8](https://huggingface.co/cocktailpeanut/flux1-schnell-q8) | `diffusion_pytorch_model-00001-of-00002.safetensors` | BF16 | `(18432, 1)` | 38 | 700.4K |
| [cocktailpeanut/flux1-schnell-q8](https://huggingface.co/cocktailpeanut/flux1-schnell-q8) | `diffusion_pytorch_model-00001-of-00002.safetensors` | BF16 | `(9216)` | 25 | 230.4K |
| [cocktailpeanut/flux1-schnell-q8](https://huggingface.co/cocktailpeanut/flux1-schnell-q8) | `diffusion_pytorch_model-00001-of-00002.safetensors` | BF16 | `(9216, 1)` | 25 | 230.4K |
| [cocktailpeanut/flux1-schnell-q8](https://huggingface.co/cocktailpeanut/flux1-schnell-q8) | `diffusion_pytorch_model-00002-of-00002.safetensors` | BF16 | `(3072)` | 56 | 172.0K |
| [cocktailpeanut/flux1-schnell-q8](https://huggingface.co/cocktailpeanut/flux1-schnell-q8) | `diffusion_pytorch_model-00002-of-00002.safetensors` | BF16 | `(3072, 1)` | 56 | 172.0K |
| [cocktailpeanut/flux1-schnell-q8](https://huggingface.co/cocktailpeanut/flux1-schnell-q8) | `diffusion_pytorch_model-00002-of-00002.safetensors` | BF16 | `(12288)` | 13 | 159.7K |
| [cocktailpeanut/flux1-schnell-q8](https://huggingface.co/cocktailpeanut/flux1-schnell-q8) | `diffusion_pytorch_model-00002-of-00002.safetensors` | BF16 | `(12288, 1)` | 13 | 159.7K |
| [cocktailpeanut/flux1-schnell-q8](https://huggingface.co/cocktailpeanut/flux1-schnell-q8) | `diffusion_pytorch_model-00002-of-00002.safetensors` | BF16 | `(9216)` | 13 | 119.8K |
| [cocktailpeanut/flux1-schnell-q8](https://huggingface.co/cocktailpeanut/flux1-schnell-q8) | `diffusion_pytorch_model-00002-of-00002.safetensors` | BF16 | `(9216, 1)` | 13 | 119.8K |
| [cocktailpeanut/flux1-schnell-q8](https://huggingface.co/cocktailpeanut/flux1-schnell-q8) | `diffusion_pytorch_model-00001-of-00002.safetensors` | BF16 | `(128)` | 124 | 15.9K |
| [cocktailpeanut/flux1-schnell-q8](https://huggingface.co/cocktailpeanut/flux1-schnell-q8) | `diffusion_pytorch_model-00002-of-00002.safetensors` | BF16 | `(6144)` | 1 | 6.1K |
| [cocktailpeanut/flux1-schnell-q8](https://huggingface.co/cocktailpeanut/flux1-schnell-q8) | `diffusion_pytorch_model-00002-of-00002.safetensors` | BF16 | `(6144, 1)` | 1 | 6.1K |
| [cocktailpeanut/flux1-schnell-q8](https://huggingface.co/cocktailpeanut/flux1-schnell-q8) | `diffusion_pytorch_model-00002-of-00002.safetensors` | BF16 | `(128)` | 28 | 3.6K |
| [cocktailpeanut/flux1-schnell-q8](https://huggingface.co/cocktailpeanut/flux1-schnell-q8) | `diffusion_pytorch_model-00002-of-00002.safetensors` | BF16 | `(64)` | 1 | 64 |
| [cocktailpeanut/flux1-schnell-q8](https://huggingface.co/cocktailpeanut/flux1-schnell-q8) | `diffusion_pytorch_model-00002-of-00002.safetensors` | BF16 | `(64, 1)` | 1 | 64 |
| [cocktailpeanut/flux1-schnell-q8](https://huggingface.co/cocktailpeanut/flux1-schnell-q8) | `diffusion_pytorch_model-00001-of-00002.safetensors` | FP32 | `()` | 836 | 836 |
| [cocktailpeanut/flux1-schnell-q8](https://huggingface.co/cocktailpeanut/flux1-schnell-q8) | `diffusion_pytorch_model-00002-of-00002.safetensors` | FP32 | `()` | 168 | 168 |
| [cocktailpeanut/flux1-schnell-q8](https://huggingface.co/cocktailpeanut/flux1-schnell-q8) | `diffusion_pytorch_model-00001-of-00002.safetensors` | FP8 (E4M3FN) | `(12288, 3072)` | 63 | 2.38B |
| [cocktailpeanut/flux1-schnell-q8](https://huggingface.co/cocktailpeanut/flux1-schnell-q8) | `diffusion_pytorch_model-00001-of-00002.safetensors` | FP8 (E4M3FN) | `(18432, 3072)` | 38 | 2.15B |
| [cocktailpeanut/flux1-schnell-q8](https://huggingface.co/cocktailpeanut/flux1-schnell-q8) | `diffusion_pytorch_model-00001-of-00002.safetensors` | FP8 (E4M3FN) | `(3072, 3072)` | 226 | 2.13B |
| [cocktailpeanut/flux1-schnell-q8](https://huggingface.co/cocktailpeanut/flux1-schnell-q8) | `diffusion_pytorch_model-00001-of-00002.safetensors` | FP8 (E4M3FN) | `(3072, 12288)` | 38 | 1.43B |
| [cocktailpeanut/flux1-schnell-q8](https://huggingface.co/cocktailpeanut/flux1-schnell-q8) | `diffusion_pytorch_model-00001-of-00002.safetensors` | FP8 (E4M3FN) | `(3072, 15360)` | 24 | 1.13B |
| [cocktailpeanut/flux1-schnell-q8](https://huggingface.co/cocktailpeanut/flux1-schnell-q8) | `diffusion_pytorch_model-00001-of-00002.safetensors` | FP8 (E4M3FN) | `(9216, 3072)` | 25 | 707.8M |
| [cocktailpeanut/flux1-schnell-q8](https://huggingface.co/cocktailpeanut/flux1-schnell-q8) | `diffusion_pytorch_model-00002-of-00002.safetensors` | FP8 (E4M3FN) | `(3072, 15360)` | 14 | 660.6M |
| [cocktailpeanut/flux1-schnell-q8](https://huggingface.co/cocktailpeanut/flux1-schnell-q8) | `diffusion_pytorch_model-00002-of-00002.safetensors` | FP8 (E4M3FN) | `(12288, 3072)` | 13 | 490.7M |
| [cocktailpeanut/flux1-schnell-q8](https://huggingface.co/cocktailpeanut/flux1-schnell-q8) | `diffusion_pytorch_model-00002-of-00002.safetensors` | FP8 (E4M3FN) | `(3072, 3072)` | 42 | 396.4M |
| [cocktailpeanut/flux1-schnell-q8](https://huggingface.co/cocktailpeanut/flux1-schnell-q8) | `diffusion_pytorch_model-00002-of-00002.safetensors` | FP8 (E4M3FN) | `(9216, 3072)` | 13 | 368.1M |
| [cocktailpeanut/flux1-schnell-q8](https://huggingface.co/cocktailpeanut/flux1-schnell-q8) | `diffusion_pytorch_model-00002-of-00002.safetensors` | FP8 (E4M3FN) | `(6144, 3072)` | 1 | 18.9M |
| [cocktailpeanut/flux1-schnell-q8](https://huggingface.co/cocktailpeanut/flux1-schnell-q8) | `diffusion_pytorch_model-00001-of-00002.safetensors` | FP8 (E4M3FN) | `(3072, 4096)` | 1 | 12.6M |
| [cocktailpeanut/flux1-schnell-q8](https://huggingface.co/cocktailpeanut/flux1-schnell-q8) | `diffusion_pytorch_model-00001-of-00002.safetensors` | FP8 (E4M3FN) | `(3072, 768)` | 1 | 2.4M |
| [cocktailpeanut/flux1-schnell-q8](https://huggingface.co/cocktailpeanut/flux1-schnell-q8) | `diffusion_pytorch_model-00001-of-00002.safetensors` | FP8 (E4M3FN) | `(3072, 256)` | 1 | 786.4K |
| [cocktailpeanut/flux1-schnell-q8](https://huggingface.co/cocktailpeanut/flux1-schnell-q8) | `diffusion_pytorch_model-00001-of-00002.safetensors` | FP8 (E4M3FN) | `(3072, 64)` | 1 | 196.6K |
| [cocktailpeanut/flux1-schnell-q8](https://huggingface.co/cocktailpeanut/flux1-schnell-q8) | `diffusion_pytorch_model-00002-of-00002.safetensors` | FP8 (E4M3FN) | `(64, 3072)` | 1 | 196.6K |
| [cocktailpeanut/flux1-schnell-qint8](https://huggingface.co/cocktailpeanut/flux1-schnell-qint8) | `diffusion_pytorch_model-00001-of-00002.safetensors` | BF16 | `(3072)` | 292 | 897.0K |
| [cocktailpeanut/flux1-schnell-qint8](https://huggingface.co/cocktailpeanut/flux1-schnell-qint8) | `diffusion_pytorch_model-00001-of-00002.safetensors` | BF16 | `(3072, 1)` | 292 | 897.0K |
| [cocktailpeanut/flux1-schnell-qint8](https://huggingface.co/cocktailpeanut/flux1-schnell-qint8) | `diffusion_pytorch_model-00001-of-00002.safetensors` | BF16 | `(12288)` | 63 | 774.1K |
| [cocktailpeanut/flux1-schnell-qint8](https://huggingface.co/cocktailpeanut/flux1-schnell-qint8) | `diffusion_pytorch_model-00001-of-00002.safetensors` | BF16 | `(12288, 1)` | 63 | 774.1K |
| [cocktailpeanut/flux1-schnell-qint8](https://huggingface.co/cocktailpeanut/flux1-schnell-qint8) | `diffusion_pytorch_model-00001-of-00002.safetensors` | BF16 | `(18432)` | 38 | 700.4K |
| [cocktailpeanut/flux1-schnell-qint8](https://huggingface.co/cocktailpeanut/flux1-schnell-qint8) | `diffusion_pytorch_model-00001-of-00002.safetensors` | BF16 | `(18432, 1)` | 38 | 700.4K |
| [cocktailpeanut/flux1-schnell-qint8](https://huggingface.co/cocktailpeanut/flux1-schnell-qint8) | `diffusion_pytorch_model-00001-of-00002.safetensors` | BF16 | `(9216)` | 25 | 230.4K |
| [cocktailpeanut/flux1-schnell-qint8](https://huggingface.co/cocktailpeanut/flux1-schnell-qint8) | `diffusion_pytorch_model-00001-of-00002.safetensors` | BF16 | `(9216, 1)` | 25 | 230.4K |
| [cocktailpeanut/flux1-schnell-qint8](https://huggingface.co/cocktailpeanut/flux1-schnell-qint8) | `diffusion_pytorch_model-00002-of-00002.safetensors` | BF16 | `(3072)` | 56 | 172.0K |
| [cocktailpeanut/flux1-schnell-qint8](https://huggingface.co/cocktailpeanut/flux1-schnell-qint8) | `diffusion_pytorch_model-00002-of-00002.safetensors` | BF16 | `(3072, 1)` | 56 | 172.0K |
| [cocktailpeanut/flux1-schnell-qint8](https://huggingface.co/cocktailpeanut/flux1-schnell-qint8) | `diffusion_pytorch_model-00002-of-00002.safetensors` | BF16 | `(12288)` | 13 | 159.7K |
| [cocktailpeanut/flux1-schnell-qint8](https://huggingface.co/cocktailpeanut/flux1-schnell-qint8) | `diffusion_pytorch_model-00002-of-00002.safetensors` | BF16 | `(12288, 1)` | 13 | 159.7K |
| [cocktailpeanut/flux1-schnell-qint8](https://huggingface.co/cocktailpeanut/flux1-schnell-qint8) | `diffusion_pytorch_model-00002-of-00002.safetensors` | BF16 | `(9216)` | 13 | 119.8K |
| [cocktailpeanut/flux1-schnell-qint8](https://huggingface.co/cocktailpeanut/flux1-schnell-qint8) | `diffusion_pytorch_model-00002-of-00002.safetensors` | BF16 | `(9216, 1)` | 13 | 119.8K |
| [cocktailpeanut/flux1-schnell-qint8](https://huggingface.co/cocktailpeanut/flux1-schnell-qint8) | `diffusion_pytorch_model-00001-of-00002.safetensors` | BF16 | `(128)` | 124 | 15.9K |
| [cocktailpeanut/flux1-schnell-qint8](https://huggingface.co/cocktailpeanut/flux1-schnell-qint8) | `diffusion_pytorch_model-00002-of-00002.safetensors` | BF16 | `(6144)` | 1 | 6.1K |
| [cocktailpeanut/flux1-schnell-qint8](https://huggingface.co/cocktailpeanut/flux1-schnell-qint8) | `diffusion_pytorch_model-00002-of-00002.safetensors` | BF16 | `(6144, 1)` | 1 | 6.1K |
| [cocktailpeanut/flux1-schnell-qint8](https://huggingface.co/cocktailpeanut/flux1-schnell-qint8) | `diffusion_pytorch_model-00002-of-00002.safetensors` | BF16 | `(128)` | 28 | 3.6K |
| [cocktailpeanut/flux1-schnell-qint8](https://huggingface.co/cocktailpeanut/flux1-schnell-qint8) | `diffusion_pytorch_model-00002-of-00002.safetensors` | BF16 | `(64)` | 1 | 64 |
| [cocktailpeanut/flux1-schnell-qint8](https://huggingface.co/cocktailpeanut/flux1-schnell-qint8) | `diffusion_pytorch_model-00002-of-00002.safetensors` | BF16 | `(64, 1)` | 1 | 64 |
| [cocktailpeanut/flux1-schnell-qint8](https://huggingface.co/cocktailpeanut/flux1-schnell-qint8) | `diffusion_pytorch_model-00001-of-00002.safetensors` | FP32 | `()` | 836 | 836 |
| [cocktailpeanut/flux1-schnell-qint8](https://huggingface.co/cocktailpeanut/flux1-schnell-qint8) | `diffusion_pytorch_model-00002-of-00002.safetensors` | FP32 | `()` | 168 | 168 |
| [cocktailpeanut/flux1-schnell-qint8](https://huggingface.co/cocktailpeanut/flux1-schnell-qint8) | `diffusion_pytorch_model-00001-of-00002.safetensors` | INT8 | `(12288, 3072)` | 63 | 2.38B |
| [cocktailpeanut/flux1-schnell-qint8](https://huggingface.co/cocktailpeanut/flux1-schnell-qint8) | `diffusion_pytorch_model-00001-of-00002.safetensors` | INT8 | `(18432, 3072)` | 38 | 2.15B |
| [cocktailpeanut/flux1-schnell-qint8](https://huggingface.co/cocktailpeanut/flux1-schnell-qint8) | `diffusion_pytorch_model-00001-of-00002.safetensors` | INT8 | `(3072, 3072)` | 226 | 2.13B |
| [cocktailpeanut/flux1-schnell-qint8](https://huggingface.co/cocktailpeanut/flux1-schnell-qint8) | `diffusion_pytorch_model-00001-of-00002.safetensors` | INT8 | `(3072, 12288)` | 38 | 1.43B |
| [cocktailpeanut/flux1-schnell-qint8](https://huggingface.co/cocktailpeanut/flux1-schnell-qint8) | `diffusion_pytorch_model-00001-of-00002.safetensors` | INT8 | `(3072, 15360)` | 24 | 1.13B |
| [cocktailpeanut/flux1-schnell-qint8](https://huggingface.co/cocktailpeanut/flux1-schnell-qint8) | `diffusion_pytorch_model-00001-of-00002.safetensors` | INT8 | `(9216, 3072)` | 25 | 707.8M |
| [cocktailpeanut/flux1-schnell-qint8](https://huggingface.co/cocktailpeanut/flux1-schnell-qint8) | `diffusion_pytorch_model-00002-of-00002.safetensors` | INT8 | `(3072, 15360)` | 14 | 660.6M |
| [cocktailpeanut/flux1-schnell-qint8](https://huggingface.co/cocktailpeanut/flux1-schnell-qint8) | `diffusion_pytorch_model-00002-of-00002.safetensors` | INT8 | `(12288, 3072)` | 13 | 490.7M |
| [cocktailpeanut/flux1-schnell-qint8](https://huggingface.co/cocktailpeanut/flux1-schnell-qint8) | `diffusion_pytorch_model-00002-of-00002.safetensors` | INT8 | `(3072, 3072)` | 42 | 396.4M |
| [cocktailpeanut/flux1-schnell-qint8](https://huggingface.co/cocktailpeanut/flux1-schnell-qint8) | `diffusion_pytorch_model-00002-of-00002.safetensors` | INT8 | `(9216, 3072)` | 13 | 368.1M |
| [cocktailpeanut/flux1-schnell-qint8](https://huggingface.co/cocktailpeanut/flux1-schnell-qint8) | `diffusion_pytorch_model-00002-of-00002.safetensors` | INT8 | `(6144, 3072)` | 1 | 18.9M |
| [cocktailpeanut/flux1-schnell-qint8](https://huggingface.co/cocktailpeanut/flux1-schnell-qint8) | `diffusion_pytorch_model-00001-of-00002.safetensors` | INT8 | `(3072, 4096)` | 1 | 12.6M |
| [cocktailpeanut/flux1-schnell-qint8](https://huggingface.co/cocktailpeanut/flux1-schnell-qint8) | `diffusion_pytorch_model-00001-of-00002.safetensors` | INT8 | `(3072, 768)` | 1 | 2.4M |
| [cocktailpeanut/flux1-schnell-qint8](https://huggingface.co/cocktailpeanut/flux1-schnell-qint8) | `diffusion_pytorch_model-00001-of-00002.safetensors` | INT8 | `(3072, 256)` | 1 | 786.4K |
| [cocktailpeanut/flux1-schnell-qint8](https://huggingface.co/cocktailpeanut/flux1-schnell-qint8) | `diffusion_pytorch_model-00001-of-00002.safetensors` | INT8 | `(3072, 64)` | 1 | 196.6K |
| [cocktailpeanut/flux1-schnell-qint8](https://huggingface.co/cocktailpeanut/flux1-schnell-qint8) | `diffusion_pytorch_model-00002-of-00002.safetensors` | INT8 | `(64, 3072)` | 1 | 196.6K |
| [cocktailpeanut/redux](https://huggingface.co/cocktailpeanut/redux) | `flux1-redux-dev.safetensors` | BF16 | `(4096, 12288)` | 1 | 50.3M |
| [cocktailpeanut/redux](https://huggingface.co/cocktailpeanut/redux) | `flux1-redux-dev.safetensors` | BF16 | `(12288, 1152)` | 1 | 14.2M |
| [cocktailpeanut/redux](https://huggingface.co/cocktailpeanut/redux) | `flux1-redux-dev.safetensors` | BF16 | `(12288)` | 1 | 12.3K |
| [cocktailpeanut/redux](https://huggingface.co/cocktailpeanut/redux) | `flux1-redux-dev.safetensors` | BF16 | `(4096)` | 1 | 4.1K |
| [cocktailpeanut/sd35](https://huggingface.co/cocktailpeanut/sd35) | `sd3.5_large.safetensors` | BF16 | `(512, 512, 3, 3)` | 30 | 70.8M |
| [cocktailpeanut/sd35](https://huggingface.co/cocktailpeanut/sd35) | `sd3.5_large.safetensors` | BF16 | `(256, 256, 3, 3)` | 10 | 5.9M |
| [cocktailpeanut/sd35](https://huggingface.co/cocktailpeanut/sd35) | `sd3.5_large.safetensors` | BF16 | `(512, 512, 1, 1)` | 8 | 2.1M |
| [cocktailpeanut/sd35](https://huggingface.co/cocktailpeanut/sd35) | `sd3.5_large.safetensors` | BF16 | `(128, 128, 3, 3)` | 10 | 1.5M |
| [cocktailpeanut/sd35](https://huggingface.co/cocktailpeanut/sd35) | `sd3.5_large.safetensors` | BF16 | `(256, 512, 3, 3)` | 1 | 1.2M |
| [cocktailpeanut/sd35](https://huggingface.co/cocktailpeanut/sd35) | `sd3.5_large.safetensors` | BF16 | `(512, 256, 3, 3)` | 1 | 1.2M |
| [cocktailpeanut/sd35](https://huggingface.co/cocktailpeanut/sd35) | `sd3.5_large.safetensors` | BF16 | `(128, 256, 3, 3)` | 1 | 294.9K |
| [cocktailpeanut/sd35](https://huggingface.co/cocktailpeanut/sd35) | `sd3.5_large.safetensors` | BF16 | `(256, 128, 3, 3)` | 1 | 294.9K |
| [cocktailpeanut/sd35](https://huggingface.co/cocktailpeanut/sd35) | `sd3.5_large.safetensors` | BF16 | `(32, 512, 3, 3)` | 1 | 147.5K |
| [cocktailpeanut/sd35](https://huggingface.co/cocktailpeanut/sd35) | `sd3.5_large.safetensors` | BF16 | `(256, 512, 1, 1)` | 1 | 131.1K |
| [cocktailpeanut/sd35](https://huggingface.co/cocktailpeanut/sd35) | `sd3.5_large.safetensors` | BF16 | `(512, 256, 1, 1)` | 1 | 131.1K |
| [cocktailpeanut/sd35](https://huggingface.co/cocktailpeanut/sd35) | `sd3.5_large.safetensors` | BF16 | `(512, 16, 3, 3)` | 1 | 73.7K |
| [cocktailpeanut/sd35](https://huggingface.co/cocktailpeanut/sd35) | `sd3.5_large.safetensors` | BF16 | `(512)` | 103 | 52.7K |
| [cocktailpeanut/sd35](https://huggingface.co/cocktailpeanut/sd35) | `sd3.5_large.safetensors` | BF16 | `(128, 256, 1, 1)` | 1 | 32.8K |
| [cocktailpeanut/sd35](https://huggingface.co/cocktailpeanut/sd35) | `sd3.5_large.safetensors` | BF16 | `(256, 128, 1, 1)` | 1 | 32.8K |
| [cocktailpeanut/sd35](https://huggingface.co/cocktailpeanut/sd35) | `sd3.5_large.safetensors` | BF16 | `(256)` | 34 | 8.7K |
| [cocktailpeanut/sd35](https://huggingface.co/cocktailpeanut/sd35) | `sd3.5_large.safetensors` | BF16 | `(128)` | 35 | 4.5K |
| [cocktailpeanut/sd35](https://huggingface.co/cocktailpeanut/sd35) | `sd3.5_large.safetensors` | BF16 | `(128, 3, 3, 3)` | 1 | 3.5K |
| [cocktailpeanut/sd35](https://huggingface.co/cocktailpeanut/sd35) | `sd3.5_large.safetensors` | BF16 | `(3, 128, 3, 3)` | 1 | 3.5K |
| [cocktailpeanut/sd35](https://huggingface.co/cocktailpeanut/sd35) | `sd3.5_large.safetensors` | BF16 | `(32)` | 1 | 32 |
| [cocktailpeanut/sd35](https://huggingface.co/cocktailpeanut/sd35) | `sd3.5_large.safetensors` | BF16 | `(3)` | 1 | 3 |
| [cocktailpeanut/sd35](https://huggingface.co/cocktailpeanut/sd35) | `sd3.5_large.safetensors` | FP16 | `(14592, 2432)` | 75 | 2.66B |
| [cocktailpeanut/sd35](https://huggingface.co/cocktailpeanut/sd35) | `sd3.5_large.safetensors` | FP16 | `(2432, 9728)` | 75 | 1.77B |
| [cocktailpeanut/sd35](https://huggingface.co/cocktailpeanut/sd35) | `sd3.5_large.safetensors` | FP16 | `(9728, 2432)` | 75 | 1.77B |
| [cocktailpeanut/sd35](https://huggingface.co/cocktailpeanut/sd35) | `sd3.5_large.safetensors` | FP16 | `(7296, 2432)` | 76 | 1.35B |
| [cocktailpeanut/sd35](https://huggingface.co/cocktailpeanut/sd35) | `sd3.5_large.safetensors` | FP16 | `(2432, 2432)` | 77 | 455.4M |
| [cocktailpeanut/sd35](https://huggingface.co/cocktailpeanut/sd35) | `sd3.5_large.safetensors` | FP16 | `(1, 36864, 2432)` | 1 | 89.7M |
| [cocktailpeanut/sd35](https://huggingface.co/cocktailpeanut/sd35) | `sd3.5_large.safetensors` | FP16 | `(4864, 2432)` | 2 | 23.7M |
| [cocktailpeanut/sd35](https://huggingface.co/cocktailpeanut/sd35) | `sd3.5_large.safetensors` | FP16 | `(2432, 4096)` | 1 | 10.0M |
| [cocktailpeanut/sd35](https://huggingface.co/cocktailpeanut/sd35) | `sd3.5_large.safetensors` | FP16 | `(2432, 2048)` | 1 | 5.0M |
| [cocktailpeanut/sd35](https://huggingface.co/cocktailpeanut/sd35) | `sd3.5_large.safetensors` | FP16 | `(14592)` | 75 | 1.1M |
| [cocktailpeanut/sd35](https://huggingface.co/cocktailpeanut/sd35) | `sd3.5_large.safetensors` | FP16 | `(9728)` | 75 | 729.6K |
| [cocktailpeanut/sd35](https://huggingface.co/cocktailpeanut/sd35) | `sd3.5_large.safetensors` | FP16 | `(2432, 256)` | 1 | 622.6K |
| [cocktailpeanut/sd35](https://huggingface.co/cocktailpeanut/sd35) | `sd3.5_large.safetensors` | FP16 | `(7296)` | 76 | 554.5K |
| [cocktailpeanut/sd35](https://huggingface.co/cocktailpeanut/sd35) | `sd3.5_large.safetensors` | FP16 | `(2432)` | 156 | 379.4K |
| [cocktailpeanut/sd35](https://huggingface.co/cocktailpeanut/sd35) | `sd3.5_large.safetensors` | FP16 | `(2432, 16, 2, 2)` | 1 | 155.6K |
| [cocktailpeanut/sd35](https://huggingface.co/cocktailpeanut/sd35) | `sd3.5_large.safetensors` | FP16 | `(64, 2432)` | 1 | 155.6K |
| [cocktailpeanut/sd35](https://huggingface.co/cocktailpeanut/sd35) | `sd3.5_large.safetensors` | FP16 | `(64)` | 153 | 9.8K |
| [cocktailpeanut/sd35](https://huggingface.co/cocktailpeanut/sd35) | `sd3.5_large.safetensors` | FP16 | `(4864)` | 2 | 9.7K |
| [cocktailpeanut/sd35turbo](https://huggingface.co/cocktailpeanut/sd35turbo) | `sd3.5_large_turbo.safetensors` | BF16 | `(512, 512, 3, 3)` | 30 | 70.8M |
| [cocktailpeanut/sd35turbo](https://huggingface.co/cocktailpeanut/sd35turbo) | `sd3.5_large_turbo.safetensors` | BF16 | `(256, 256, 3, 3)` | 10 | 5.9M |
| [cocktailpeanut/sd35turbo](https://huggingface.co/cocktailpeanut/sd35turbo) | `sd3.5_large_turbo.safetensors` | BF16 | `(512, 512, 1, 1)` | 8 | 2.1M |
| [cocktailpeanut/sd35turbo](https://huggingface.co/cocktailpeanut/sd35turbo) | `sd3.5_large_turbo.safetensors` | BF16 | `(128, 128, 3, 3)` | 10 | 1.5M |
| [cocktailpeanut/sd35turbo](https://huggingface.co/cocktailpeanut/sd35turbo) | `sd3.5_large_turbo.safetensors` | BF16 | `(256, 512, 3, 3)` | 1 | 1.2M |
| [cocktailpeanut/sd35turbo](https://huggingface.co/cocktailpeanut/sd35turbo) | `sd3.5_large_turbo.safetensors` | BF16 | `(512, 256, 3, 3)` | 1 | 1.2M |
| [cocktailpeanut/sd35turbo](https://huggingface.co/cocktailpeanut/sd35turbo) | `sd3.5_large_turbo.safetensors` | BF16 | `(128, 256, 3, 3)` | 1 | 294.9K |
| [cocktailpeanut/sd35turbo](https://huggingface.co/cocktailpeanut/sd35turbo) | `sd3.5_large_turbo.safetensors` | BF16 | `(256, 128, 3, 3)` | 1 | 294.9K |
| [cocktailpeanut/sd35turbo](https://huggingface.co/cocktailpeanut/sd35turbo) | `sd3.5_large_turbo.safetensors` | BF16 | `(32, 512, 3, 3)` | 1 | 147.5K |
| [cocktailpeanut/sd35turbo](https://huggingface.co/cocktailpeanut/sd35turbo) | `sd3.5_large_turbo.safetensors` | BF16 | `(256, 512, 1, 1)` | 1 | 131.1K |
| [cocktailpeanut/sd35turbo](https://huggingface.co/cocktailpeanut/sd35turbo) | `sd3.5_large_turbo.safetensors` | BF16 | `(512, 256, 1, 1)` | 1 | 131.1K |
| [cocktailpeanut/sd35turbo](https://huggingface.co/cocktailpeanut/sd35turbo) | `sd3.5_large_turbo.safetensors` | BF16 | `(512, 16, 3, 3)` | 1 | 73.7K |
| [cocktailpeanut/sd35turbo](https://huggingface.co/cocktailpeanut/sd35turbo) | `sd3.5_large_turbo.safetensors` | BF16 | `(512)` | 103 | 52.7K |
| [cocktailpeanut/sd35turbo](https://huggingface.co/cocktailpeanut/sd35turbo) | `sd3.5_large_turbo.safetensors` | BF16 | `(128, 256, 1, 1)` | 1 | 32.8K |
| [cocktailpeanut/sd35turbo](https://huggingface.co/cocktailpeanut/sd35turbo) | `sd3.5_large_turbo.safetensors` | BF16 | `(256, 128, 1, 1)` | 1 | 32.8K |
| [cocktailpeanut/sd35turbo](https://huggingface.co/cocktailpeanut/sd35turbo) | `sd3.5_large_turbo.safetensors` | BF16 | `(256)` | 34 | 8.7K |
| [cocktailpeanut/sd35turbo](https://huggingface.co/cocktailpeanut/sd35turbo) | `sd3.5_large_turbo.safetensors` | BF16 | `(128)` | 35 | 4.5K |
| [cocktailpeanut/sd35turbo](https://huggingface.co/cocktailpeanut/sd35turbo) | `sd3.5_large_turbo.safetensors` | BF16 | `(128, 3, 3, 3)` | 1 | 3.5K |
| [cocktailpeanut/sd35turbo](https://huggingface.co/cocktailpeanut/sd35turbo) | `sd3.5_large_turbo.safetensors` | BF16 | `(3, 128, 3, 3)` | 1 | 3.5K |
| [cocktailpeanut/sd35turbo](https://huggingface.co/cocktailpeanut/sd35turbo) | `sd3.5_large_turbo.safetensors` | BF16 | `(32)` | 1 | 32 |
| [cocktailpeanut/sd35turbo](https://huggingface.co/cocktailpeanut/sd35turbo) | `sd3.5_large_turbo.safetensors` | BF16 | `(3)` | 1 | 3 |
| [cocktailpeanut/sd35turbo](https://huggingface.co/cocktailpeanut/sd35turbo) | `sd3.5_large_turbo.safetensors` | FP16 | `(14592, 2432)` | 75 | 2.66B |
| [cocktailpeanut/sd35turbo](https://huggingface.co/cocktailpeanut/sd35turbo) | `sd3.5_large_turbo.safetensors` | FP16 | `(2432, 9728)` | 75 | 1.77B |
| [cocktailpeanut/sd35turbo](https://huggingface.co/cocktailpeanut/sd35turbo) | `sd3.5_large_turbo.safetensors` | FP16 | `(9728, 2432)` | 75 | 1.77B |
| [cocktailpeanut/sd35turbo](https://huggingface.co/cocktailpeanut/sd35turbo) | `sd3.5_large_turbo.safetensors` | FP16 | `(7296, 2432)` | 76 | 1.35B |
| [cocktailpeanut/sd35turbo](https://huggingface.co/cocktailpeanut/sd35turbo) | `sd3.5_large_turbo.safetensors` | FP16 | `(2432, 2432)` | 77 | 455.4M |
| [cocktailpeanut/sd35turbo](https://huggingface.co/cocktailpeanut/sd35turbo) | `sd3.5_large_turbo.safetensors` | FP16 | `(1, 36864, 2432)` | 1 | 89.7M |
| [cocktailpeanut/sd35turbo](https://huggingface.co/cocktailpeanut/sd35turbo) | `sd3.5_large_turbo.safetensors` | FP16 | `(4864, 2432)` | 2 | 23.7M |
| [cocktailpeanut/sd35turbo](https://huggingface.co/cocktailpeanut/sd35turbo) | `sd3.5_large_turbo.safetensors` | FP16 | `(2432, 4096)` | 1 | 10.0M |
| [cocktailpeanut/sd35turbo](https://huggingface.co/cocktailpeanut/sd35turbo) | `sd3.5_large_turbo.safetensors` | FP16 | `(2432, 2048)` | 1 | 5.0M |
| [cocktailpeanut/sd35turbo](https://huggingface.co/cocktailpeanut/sd35turbo) | `sd3.5_large_turbo.safetensors` | FP16 | `(14592)` | 75 | 1.1M |
| [cocktailpeanut/sd35turbo](https://huggingface.co/cocktailpeanut/sd35turbo) | `sd3.5_large_turbo.safetensors` | FP16 | `(9728)` | 75 | 729.6K |
| [cocktailpeanut/sd35turbo](https://huggingface.co/cocktailpeanut/sd35turbo) | `sd3.5_large_turbo.safetensors` | FP16 | `(2432, 256)` | 1 | 622.6K |
| [cocktailpeanut/sd35turbo](https://huggingface.co/cocktailpeanut/sd35turbo) | `sd3.5_large_turbo.safetensors` | FP16 | `(7296)` | 76 | 554.5K |
| [cocktailpeanut/sd35turbo](https://huggingface.co/cocktailpeanut/sd35turbo) | `sd3.5_large_turbo.safetensors` | FP16 | `(2432)` | 156 | 379.4K |
| [cocktailpeanut/sd35turbo](https://huggingface.co/cocktailpeanut/sd35turbo) | `sd3.5_large_turbo.safetensors` | FP16 | `(2432, 16, 2, 2)` | 1 | 155.6K |
| [cocktailpeanut/sd35turbo](https://huggingface.co/cocktailpeanut/sd35turbo) | `sd3.5_large_turbo.safetensors` | FP16 | `(64, 2432)` | 1 | 155.6K |
| [cocktailpeanut/sd35turbo](https://huggingface.co/cocktailpeanut/sd35turbo) | `sd3.5_large_turbo.safetensors` | FP16 | `(64)` | 153 | 9.8K |
| [cocktailpeanut/sd35turbo](https://huggingface.co/cocktailpeanut/sd35turbo) | `sd3.5_large_turbo.safetensors` | FP16 | `(4864)` | 2 | 9.7K |
| [cocktailpeanut/sf3d](https://huggingface.co/cocktailpeanut/sf3d) | `model.safetensors` | FP32 | `(1024, 1024)` | 228 | 239.1M |
| [cocktailpeanut/sf3d](https://huggingface.co/cocktailpeanut/sf3d) | `model.safetensors` | FP32 | `(1024, 4096)` | 44 | 184.5M |
| [cocktailpeanut/sf3d](https://huggingface.co/cocktailpeanut/sf3d) | `model.safetensors` | FP32 | `(8192, 1024)` | 20 | 167.8M |
| [cocktailpeanut/sf3d](https://huggingface.co/cocktailpeanut/sf3d) | `model.safetensors` | FP32 | `(4096, 1024)` | 24 | 100.7M |
| [cocktailpeanut/sf3d](https://huggingface.co/cocktailpeanut/sf3d) | `model.safetensors` | FP32 | `(2048, 768)` | 48 | 75.5M |
| [cocktailpeanut/sf3d](https://huggingface.co/cocktailpeanut/sf3d) | `model.safetensors` | FP32 | `(1024, 1024, 3, 3)` | 3 | 28.3M |
| [cocktailpeanut/sf3d](https://huggingface.co/cocktailpeanut/sf3d) | `model.safetensors` | FP32 | `(3, 1024, 96, 96)` | 1 | 28.3M |
| [cocktailpeanut/sf3d](https://huggingface.co/cocktailpeanut/sf3d) | `model.safetensors` | FP32 | `(3072, 768)` | 12 | 28.3M |
| [cocktailpeanut/sf3d](https://huggingface.co/cocktailpeanut/sf3d) | `model.safetensors` | FP32 | `(768, 3072)` | 12 | 28.3M |
| [cocktailpeanut/sf3d](https://huggingface.co/cocktailpeanut/sf3d) | `model.safetensors` | FP32 | `(49408, 512)` | 1 | 25.3M |
| [cocktailpeanut/sf3d](https://huggingface.co/cocktailpeanut/sf3d) | `model.safetensors` | FP32 | `(2304, 768)` | 12 | 21.2M |
| [cocktailpeanut/sf3d](https://huggingface.co/cocktailpeanut/sf3d) | `model.safetensors` | FP32 | `(512, 3072, 3, 3)` | 1 | 14.2M |
| [cocktailpeanut/sf3d](https://huggingface.co/cocktailpeanut/sf3d) | `model.safetensors` | FP32 | `(2048, 512)` | 12 | 12.6M |
| [cocktailpeanut/sf3d](https://huggingface.co/cocktailpeanut/sf3d) | `model.safetensors` | FP32 | `(512, 2048)` | 12 | 12.6M |
| [cocktailpeanut/sf3d](https://huggingface.co/cocktailpeanut/sf3d) | `model.safetensors` | FP32 | `(1536, 512)` | 12 | 9.4M |
| [cocktailpeanut/sf3d](https://huggingface.co/cocktailpeanut/sf3d) | `model.safetensors` | FP32 | `(768, 768)` | 12 | 7.1M |
| [cocktailpeanut/sf3d](https://huggingface.co/cocktailpeanut/sf3d) | `model.safetensors` | FP32 | `(512, 512)` | 26 | 6.8M |
| [cocktailpeanut/sf3d](https://huggingface.co/cocktailpeanut/sf3d) | `model.safetensors` | FP32 | `(640, 1024, 3, 3)` | 1 | 5.9M |
| [cocktailpeanut/sf3d](https://huggingface.co/cocktailpeanut/sf3d) | `model.safetensors` | FP32 | `(512, 512, 3, 3)` | 1 | 2.4M |
| [cocktailpeanut/sf3d](https://huggingface.co/cocktailpeanut/sf3d) | `model.safetensors` | FP32 | `(768, 3, 32, 32)` | 1 | 2.4M |
| [cocktailpeanut/sf3d](https://huggingface.co/cocktailpeanut/sf3d) | `model.safetensors` | FP32 | `(1, 1792, 1024)` | 1 | 1.8M |
| [cocktailpeanut/sf3d](https://huggingface.co/cocktailpeanut/sf3d) | `model.safetensors` | FP32 | `(1, 1370, 1024)` | 1 | 1.4M |
| [cocktailpeanut/sf3d](https://huggingface.co/cocktailpeanut/sf3d) | `model.safetensors` | FP32 | `(1024, 3, 14, 14)` | 1 | 602.1K |
| [cocktailpeanut/sf3d](https://huggingface.co/cocktailpeanut/sf3d) | `model.safetensors` | FP32 | `(1024)` | 436 | 446.5K |
| [cocktailpeanut/sf3d](https://huggingface.co/cocktailpeanut/sf3d) | `model.safetensors` | FP32 | `(768, 512)` | 1 | 393.2K |
| [cocktailpeanut/sf3d](https://huggingface.co/cocktailpeanut/sf3d) | `model.safetensors` | FP32 | `(8192)` | 20 | 163.8K |
| [cocktailpeanut/sf3d](https://huggingface.co/cocktailpeanut/sf3d) | `model.safetensors` | FP32 | `(2048)` | 60 | 122.9K |
| [cocktailpeanut/sf3d](https://huggingface.co/cocktailpeanut/sf3d) | `model.safetensors` | FP32 | `(4096)` | 24 | 98.3K |
| [cocktailpeanut/sf3d](https://huggingface.co/cocktailpeanut/sf3d) | `model.safetensors` | FP32 | `(768)` | 78 | 59.9K |
| [cocktailpeanut/sf3d](https://huggingface.co/cocktailpeanut/sf3d) | `model.safetensors` | FP32 | `(512)` | 89 | 45.6K |
| [cocktailpeanut/sf3d](https://huggingface.co/cocktailpeanut/sf3d) | `model.safetensors` | FP32 | `(77, 512)` | 1 | 39.4K |
| [cocktailpeanut/sf3d](https://huggingface.co/cocktailpeanut/sf3d) | `model.safetensors` | FP32 | `(50, 768)` | 1 | 38.4K |
| [cocktailpeanut/sf3d](https://huggingface.co/cocktailpeanut/sf3d) | `model.safetensors` | FP32 | `(3072)` | 12 | 36.9K |
| [cocktailpeanut/sf3d](https://huggingface.co/cocktailpeanut/sf3d) | `model.safetensors` | FP32 | `(64, 120)` | 4 | 30.7K |
| [cocktailpeanut/sf3d](https://huggingface.co/cocktailpeanut/sf3d) | `model.safetensors` | FP32 | `(2304)` | 12 | 27.6K |
| [cocktailpeanut/sf3d](https://huggingface.co/cocktailpeanut/sf3d) | `model.safetensors` | FP32 | `(64, 64)` | 6 | 24.6K |
| [cocktailpeanut/sf3d](https://huggingface.co/cocktailpeanut/sf3d) | `model.safetensors` | FP32 | `(768, 25)` | 1 | 19.2K |
| [cocktailpeanut/sf3d](https://huggingface.co/cocktailpeanut/sf3d) | `model.safetensors` | FP32 | `(1536)` | 12 | 18.4K |
| [cocktailpeanut/sf3d](https://huggingface.co/cocktailpeanut/sf3d) | `model.safetensors` | FP32 | `(24, 512)` | 1 | 12.3K |
| [cocktailpeanut/sf3d](https://huggingface.co/cocktailpeanut/sf3d) | `model.safetensors` | FP32 | `(1, 512)` | 4 | 2.0K |
| [cocktailpeanut/sf3d](https://huggingface.co/cocktailpeanut/sf3d) | `model.safetensors` | FP32 | `(1, 1, 1024)` | 1 | 1.0K |
| [cocktailpeanut/sf3d](https://huggingface.co/cocktailpeanut/sf3d) | `model.safetensors` | FP32 | `(1, 1024)` | 1 | 1.0K |
| [cocktailpeanut/sf3d](https://huggingface.co/cocktailpeanut/sf3d) | `model.safetensors` | FP32 | `(64)` | 10 | 640 |
| [cocktailpeanut/sf3d](https://huggingface.co/cocktailpeanut/sf3d) | `model.safetensors` | FP32 | `(640)` | 1 | 640 |
| [cocktailpeanut/sf3d](https://huggingface.co/cocktailpeanut/sf3d) | `model.safetensors` | FP32 | `(3, 64)` | 3 | 576 |
| [cocktailpeanut/sf3d](https://huggingface.co/cocktailpeanut/sf3d) | `model.safetensors` | FP32 | `(1, 64)` | 1 | 64 |
| [cocktailpeanut/sf3d](https://huggingface.co/cocktailpeanut/sf3d) | `model.safetensors` | FP32 | `(24)` | 1 | 24 |
| [cocktailpeanut/sf3d](https://huggingface.co/cocktailpeanut/sf3d) | `model.safetensors` | FP32 | `(3)` | 3 | 9 |
| [cocktailpeanut/sf3d](https://huggingface.co/cocktailpeanut/sf3d) | `model.safetensors` | FP32 | `(2, 3)` | 1 | 6 |
| [cocktailpeanut/sf3d](https://huggingface.co/cocktailpeanut/sf3d) | `model.safetensors` | FP32 | `(1)` | 5 | 5 |
| [cocktailpeanut/sf3d](https://huggingface.co/cocktailpeanut/sf3d) | `model.safetensors` | FP32 | `()` | 1 | 1 |
| [cocktailpeanut/sisao](https://huggingface.co/cocktailpeanut/sisao) | `oasis500m.safetensors` | FP32 | `(6144, 1024)` | 32 | 201.3M |
| [cocktailpeanut/sisao](https://huggingface.co/cocktailpeanut/sisao) | `oasis500m.safetensors` | FP32 | `(1024, 4096)` | 32 | 134.2M |
| [cocktailpeanut/sisao](https://huggingface.co/cocktailpeanut/sisao) | `oasis500m.safetensors` | FP32 | `(4096, 1024)` | 32 | 134.2M |
| [cocktailpeanut/sisao](https://huggingface.co/cocktailpeanut/sisao) | `oasis500m.safetensors` | FP32 | `(3072, 1024)` | 32 | 100.7M |
| [cocktailpeanut/sisao](https://huggingface.co/cocktailpeanut/sisao) | `vit-l-20.safetensors` | FP32 | `(1024, 4096)` | 18 | 75.5M |
| [cocktailpeanut/sisao](https://huggingface.co/cocktailpeanut/sisao) | `vit-l-20.safetensors` | FP32 | `(4096, 1024)` | 18 | 75.5M |
| [cocktailpeanut/sisao](https://huggingface.co/cocktailpeanut/sisao) | `vit-l-20.safetensors` | FP32 | `(3072, 1024)` | 18 | 56.6M |
| [cocktailpeanut/sisao](https://huggingface.co/cocktailpeanut/sisao) | `oasis500m.safetensors` | FP32 | `(1024, 1024)` | 33 | 34.6M |
| [cocktailpeanut/sisao](https://huggingface.co/cocktailpeanut/sisao) | `vit-l-20.safetensors` | FP32 | `(1024, 1024)` | 18 | 18.9M |
| [cocktailpeanut/sisao](https://huggingface.co/cocktailpeanut/sisao) | `oasis500m.safetensors` | FP32 | `(2048, 1024)` | 1 | 2.1M |
| [cocktailpeanut/sisao](https://huggingface.co/cocktailpeanut/sisao) | `vit-l-20.safetensors` | FP32 | `(1024, 3, 20, 20)` | 1 | 1.2M |
| [cocktailpeanut/sisao](https://huggingface.co/cocktailpeanut/sisao) | `vit-l-20.safetensors` | FP32 | `(1200, 1024)` | 1 | 1.2M |
| [cocktailpeanut/sisao](https://huggingface.co/cocktailpeanut/sisao) | `oasis500m.safetensors` | FP32 | `(1024, 256)` | 1 | 262.1K |
| [cocktailpeanut/sisao](https://huggingface.co/cocktailpeanut/sisao) | `oasis500m.safetensors` | FP32 | `(6144)` | 32 | 196.6K |
| [cocktailpeanut/sisao](https://huggingface.co/cocktailpeanut/sisao) | `oasis500m.safetensors` | FP32 | `(4096)` | 32 | 131.1K |
| [cocktailpeanut/sisao](https://huggingface.co/cocktailpeanut/sisao) | `vit-l-20.safetensors` | FP32 | `(1024)` | 114 | 116.7K |
| [cocktailpeanut/sisao](https://huggingface.co/cocktailpeanut/sisao) | `vit-l-20.safetensors` | FP32 | `(4096)` | 18 | 73.7K |
| [cocktailpeanut/sisao](https://huggingface.co/cocktailpeanut/sisao) | `oasis500m.safetensors` | FP32 | `(1024)` | 68 | 69.6K |
| [cocktailpeanut/sisao](https://huggingface.co/cocktailpeanut/sisao) | `oasis500m.safetensors` | FP32 | `(1024, 16, 2, 2)` | 1 | 65.5K |
| [cocktailpeanut/sisao](https://huggingface.co/cocktailpeanut/sisao) | `oasis500m.safetensors` | FP32 | `(64, 1024)` | 1 | 65.5K |
| [cocktailpeanut/sisao](https://huggingface.co/cocktailpeanut/sisao) | `vit-l-20.safetensors` | FP32 | `(3072)` | 18 | 55.3K |
| [cocktailpeanut/sisao](https://huggingface.co/cocktailpeanut/sisao) | `vit-l-20.safetensors` | FP32 | `(32, 1024)` | 1 | 32.8K |
| [cocktailpeanut/sisao](https://huggingface.co/cocktailpeanut/sisao) | `oasis500m.safetensors` | FP32 | `(1024, 25)` | 1 | 25.6K |
| [cocktailpeanut/sisao](https://huggingface.co/cocktailpeanut/sisao) | `vit-l-20.safetensors` | FP32 | `(1024, 16)` | 1 | 16.4K |
| [cocktailpeanut/sisao](https://huggingface.co/cocktailpeanut/sisao) | `oasis500m.safetensors` | FP32 | `(2048)` | 1 | 2.0K |
| [cocktailpeanut/sisao](https://huggingface.co/cocktailpeanut/sisao) | `vit-l-20.safetensors` | FP32 | `(1200)` | 1 | 1.2K |
| [cocktailpeanut/sisao](https://huggingface.co/cocktailpeanut/sisao) | `oasis500m.safetensors` | FP32 | `(64)` | 1 | 64 |
| [cocktailpeanut/sisao](https://huggingface.co/cocktailpeanut/sisao) | `oasis500m.safetensors` | FP32 | `(32)` | 1 | 32 |
| [cocktailpeanut/sisao](https://huggingface.co/cocktailpeanut/sisao) | `vit-l-20.safetensors` | FP32 | `(32)` | 1 | 32 |
| [cocktailpeanut/sisao](https://huggingface.co/cocktailpeanut/sisao) | `oasis500m.safetensors` | FP32 | `(16)` | 1 | 16 |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | `svd_xt_1_1.safetensors` | FP16 | `(1280, 5120)` | 56 | 367.0M |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | `svd_xt_1_1.safetensors` | FP16 | `(1280, 1280, 3, 3)` | 20 | 294.9M |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | `svd_xt_1_1.safetensors` | FP16 | `(5120, 1280)` | 38 | 249.0M |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | `svd_xt_1_1.safetensors` | FP16 | `(10240, 1280)` | 18 | 235.9M |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | `svd_xt_1_1.safetensors` | FP16 | `(1280, 1280)` | 142 | 232.7M |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | `svd_xt_1_1.safetensors` | FP16 | `(3840, 1280)` | 32 | 157.3M |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | `svd_xt_1_1.safetensors` | FP16 | `(1280, 2560, 3, 3)` | 5 | 147.5M |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | `svd_xt_1_1.safetensors` | FP16 | `(512, 512, 3, 3)` | 60 | 141.6M |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | `svd_xt_1_1.safetensors` | FP16 | `(1280, 1280, 3, 1, 1)` | 24 | 118.0M |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | `svd_xt_1_1.safetensors` | FP16 | `(49408, 1024)` | 1 | 50.6M |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | `svd_xt_1_1.safetensors` | FP16 | `(5120, 640)` | 15 | 49.2M |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | `svd_xt_1_1.safetensors` | FP16 | `(1280, 1024)` | 25 | 32.8M |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | `svd_xt_1_1.safetensors` | FP16 | `(640, 2560)` | 20 | 32.8M |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | `svd_xt_1_1.safetensors` | FP16 | `(640, 640, 3, 3)` | 8 | 29.5M |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | `svd_xt_1_1.safetensors` | FP16 | `(640, 640)` | 70 | 28.7M |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | `svd_xt_1_1.safetensors` | FP16 | `(1280, 1920, 3, 3)` | 1 | 22.1M |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | `svd_xt_1_1.safetensors` | FP16 | `(1280, 2560, 1, 1)` | 5 | 16.4M |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | `svd_xt_1_1.safetensors` | FP16 | `(640, 1024)` | 20 | 13.1M |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | `svd_xt_1_1.safetensors` | FP16 | `(512, 512, 3, 1, 1)` | 16 | 12.6M |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | `svd_xt_1_1.safetensors` | FP16 | `(2560, 320)` | 15 | 12.3M |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | `svd_xt_1_1.safetensors` | FP16 | `(320, 1280)` | 30 | 12.3M |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | `svd_xt_1_1.safetensors` | FP16 | `(640, 640, 3, 1, 1)` | 10 | 12.3M |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | `svd_xt_1_1.safetensors` | FP16 | `(256, 256, 3, 3)` | 20 | 11.8M |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | `svd_xt_1_1.safetensors` | FP16 | `(640, 1920, 3, 3)` | 1 | 11.1M |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | `svd_xt_1_1.safetensors` | FP16 | `(2560, 640)` | 5 | 8.2M |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | `svd_xt_1_1.safetensors` | FP16 | `(640, 1280)` | 10 | 8.2M |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | `svd_xt_1_1.safetensors` | FP16 | `(1280, 640, 3, 3)` | 1 | 7.4M |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | `svd_xt_1_1.safetensors` | FP16 | `(320, 320, 3, 3)` | 8 | 7.4M |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | `svd_xt_1_1.safetensors` | FP16 | `(640, 1280, 3, 3)` | 1 | 7.4M |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | `svd_xt_1_1.safetensors` | FP16 | `(320, 320)` | 70 | 7.2M |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | `svd_xt_1_1.safetensors` | FP16 | `(320, 1024)` | 20 | 6.6M |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | `svd_xt_1_1.safetensors` | FP16 | `(640, 960, 3, 3)` | 1 | 5.5M |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | `svd_xt_1_1.safetensors` | FP16 | `(512, 512, 1, 1)` | 16 | 4.2M |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | `svd_xt_1_1.safetensors` | FP16 | `(320, 640, 3, 3)` | 2 | 3.7M |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | `svd_xt_1_1.safetensors` | FP16 | `(320, 320, 3, 1, 1)` | 10 | 3.1M |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | `svd_xt_1_1.safetensors` | FP16 | `(128, 128, 3, 3)` | 20 | 2.9M |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | `svd_xt_1_1.safetensors` | FP16 | `(320, 960, 3, 3)` | 1 | 2.8M |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | `svd_xt_1_1.safetensors` | FP16 | `(1280, 1920, 1, 1)` | 1 | 2.5M |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | `svd_xt_1_1.safetensors` | FP16 | `(1280, 320)` | 6 | 2.5M |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | `svd_xt_1_1.safetensors` | FP16 | `(256, 512, 3, 3)` | 2 | 2.4M |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | `svd_xt_1_1.safetensors` | FP16 | `(512, 256, 3, 3)` | 2 | 2.4M |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | `svd_xt_1_1.safetensors` | FP16 | `(640, 320, 3, 3)` | 1 | 1.8M |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | `svd_xt_1_1.safetensors` | FP16 | `(640, 1920, 1, 1)` | 1 | 1.2M |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | `svd_xt_1_1.safetensors` | FP16 | `(256, 256, 3, 1, 1)` | 6 | 1.2M |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | `svd_xt_1_1.safetensors` | FP16 | `(1024, 1024)` | 1 | 1.0M |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | `svd_xt_1_1.safetensors` | FP16 | `(1280, 768)` | 1 | 983.0K |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | `svd_xt_1_1.safetensors` | FP16 | `(1280, 640, 1, 1)` | 1 | 819.2K |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | `svd_xt_1_1.safetensors` | FP16 | `(640, 1280, 1, 1)` | 1 | 819.2K |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | `svd_xt_1_1.safetensors` | FP16 | `(1280, 3, 14, 14)` | 1 | 752.6K |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | `svd_xt_1_1.safetensors` | FP16 | `(1280)` | 528 | 675.8K |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | `svd_xt_1_1.safetensors` | FP16 | `(640, 960, 1, 1)` | 1 | 614.4K |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | `svd_xt_1_1.safetensors` | FP16 | `(128, 256, 3, 3)` | 2 | 589.8K |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | `svd_xt_1_1.safetensors` | FP16 | `(256, 128, 3, 3)` | 2 | 589.8K |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | `svd_xt_1_1.safetensors` | FP16 | `(320, 640, 1, 1)` | 2 | 409.6K |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | `svd_xt_1_1.safetensors` | FP16 | `(257, 1280)` | 1 | 329.0K |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | `svd_xt_1_1.safetensors` | FP16 | `(320, 960, 1, 1)` | 1 | 307.2K |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | `svd_xt_1_1.safetensors` | FP16 | `(128, 128, 3, 1, 1)` | 6 | 294.9K |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | `svd_xt_1_1.safetensors` | FP16 | `(5120)` | 53 | 271.4K |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | `svd_xt_1_1.safetensors` | FP16 | `(256, 512, 1, 1)` | 2 | 262.1K |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | `svd_xt_1_1.safetensors` | FP16 | `(512, 256, 1, 1)` | 2 | 262.1K |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | `svd_xt_1_1.safetensors` | FP16 | `(640, 320, 1, 1)` | 1 | 204.8K |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | `svd_xt_1_1.safetensors` | FP16 | `(10240)` | 18 | 184.3K |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | `svd_xt_1_1.safetensors` | FP16 | `(640)` | 204 | 130.6K |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | `svd_xt_1_1.safetensors` | FP16 | `(512)` | 254 | 130.0K |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | `svd_xt_1_1.safetensors` | FP16 | `(3840)` | 32 | 122.9K |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | `svd_xt_1_1.safetensors` | FP16 | `(77, 1024)` | 1 | 78.8K |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | `svd_xt_1_1.safetensors` | FP16 | `(2560)` | 30 | 76.8K |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | `svd_xt_1_1.safetensors` | FP16 | `(8, 512, 3, 3)` | 2 | 73.7K |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | `svd_xt_1_1.safetensors` | FP16 | `(128, 256, 1, 1)` | 2 | 65.5K |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | `svd_xt_1_1.safetensors` | FP16 | `(256, 128, 1, 1)` | 2 | 65.5K |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | `svd_xt_1_1.safetensors` | FP16 | `(320)` | 203 | 65.0K |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | `svd_xt_1_1.safetensors` | FP16 | `(512, 4, 3, 3)` | 2 | 36.9K |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | `svd_xt_1_1.safetensors` | FP16 | `(320, 8, 3, 3)` | 1 | 23.0K |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | `svd_xt_1_1.safetensors` | FP16 | `(256)` | 86 | 22.0K |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | `svd_xt_1_1.safetensors` | FP16 | `(4, 320, 3, 3)` | 1 | 11.5K |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | `svd_xt_1_1.safetensors` | FP16 | `(128)` | 88 | 11.3K |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | `svd_xt_1_1.safetensors` | FP16 | `(1920)` | 4 | 7.7K |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | `svd_xt_1_1.safetensors` | FP16 | `(128, 3, 3, 3)` | 2 | 6.9K |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | `svd_xt_1_1.safetensors` | FP16 | `(3, 128, 3, 3)` | 2 | 6.9K |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | `svd_xt_1_1.safetensors` | FP16 | `(960)` | 4 | 3.8K |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | `svd_xt_1_1.safetensors` | FP16 | `(1024)` | 2 | 2.0K |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | `svd_xt_1_1.safetensors` | FP16 | `(8, 8, 1, 1)` | 1 | 64 |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | `svd_xt_1_1.safetensors` | FP16 | `(1)` | 52 | 52 |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | `svd_xt_1_1.safetensors` | FP16 | `(3, 3, 3, 1, 1)` | 1 | 27 |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | `svd_xt_1_1.safetensors` | FP16 | `(8)` | 3 | 24 |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | `svd_xt_1_1.safetensors` | FP16 | `(4, 4, 1, 1)` | 1 | 16 |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | `svd_xt_1_1.safetensors` | FP16 | `(3)` | 3 | 9 |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | `svd_xt_1_1.safetensors` | FP16 | `(4)` | 2 | 8 |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | `svd_xt_1_1.safetensors` | FP16 | `()` | 1 | 1 |
| [cocktailpeanut/xulf-dev](https://huggingface.co/cocktailpeanut/xulf-dev) | `flux1-dev.safetensors` | BF16 | `(21504, 3072)` | 38 | 2.51B |
| [cocktailpeanut/xulf-dev](https://huggingface.co/cocktailpeanut/xulf-dev) | `flux1-dev.safetensors` | BF16 | `(18432, 3072)` | 38 | 2.15B |
| [cocktailpeanut/xulf-dev](https://huggingface.co/cocktailpeanut/xulf-dev) | `flux1-dev.safetensors` | BF16 | `(9216, 3072)` | 76 | 2.15B |
| [cocktailpeanut/xulf-dev](https://huggingface.co/cocktailpeanut/xulf-dev) | `flux1-dev.safetensors` | BF16 | `(3072, 15360)` | 38 | 1.79B |
| [cocktailpeanut/xulf-dev](https://huggingface.co/cocktailpeanut/xulf-dev) | `flux1-dev.safetensors` | BF16 | `(12288, 3072)` | 38 | 1.43B |
| [cocktailpeanut/xulf-dev](https://huggingface.co/cocktailpeanut/xulf-dev) | `flux1-dev.safetensors` | BF16 | `(3072, 12288)` | 38 | 1.43B |
| [cocktailpeanut/xulf-dev](https://huggingface.co/cocktailpeanut/xulf-dev) | `flux1-dev.safetensors` | BF16 | `(3072, 3072)` | 41 | 386.9M |
| [cocktailpeanut/xulf-dev](https://huggingface.co/cocktailpeanut/xulf-dev) | `flux1-dev.safetensors` | BF16 | `(6144, 3072)` | 1 | 18.9M |
| [cocktailpeanut/xulf-dev](https://huggingface.co/cocktailpeanut/xulf-dev) | `flux1-dev.safetensors` | BF16 | `(3072, 4096)` | 1 | 12.6M |
| [cocktailpeanut/xulf-dev](https://huggingface.co/cocktailpeanut/xulf-dev) | `flux1-dev.safetensors` | BF16 | `(3072, 768)` | 1 | 2.4M |
| [cocktailpeanut/xulf-dev](https://huggingface.co/cocktailpeanut/xulf-dev) | `flux1-dev.safetensors` | BF16 | `(3072, 256)` | 2 | 1.6M |
| [cocktailpeanut/xulf-dev](https://huggingface.co/cocktailpeanut/xulf-dev) | `flux1-dev.safetensors` | BF16 | `(21504)` | 38 | 817.2K |
| [cocktailpeanut/xulf-dev](https://huggingface.co/cocktailpeanut/xulf-dev) | `flux1-dev.safetensors` | BF16 | `(18432)` | 38 | 700.4K |
| [cocktailpeanut/xulf-dev](https://huggingface.co/cocktailpeanut/xulf-dev) | `flux1-dev.safetensors` | BF16 | `(9216)` | 76 | 700.4K |
| [cocktailpeanut/xulf-dev](https://huggingface.co/cocktailpeanut/xulf-dev) | `flux1-dev.safetensors` | BF16 | `(12288)` | 38 | 466.9K |
| [cocktailpeanut/xulf-dev](https://huggingface.co/cocktailpeanut/xulf-dev) | `flux1-dev.safetensors` | BF16 | `(3072)` | 122 | 374.8K |
| [cocktailpeanut/xulf-dev](https://huggingface.co/cocktailpeanut/xulf-dev) | `flux1-dev.safetensors` | BF16 | `(3072, 64)` | 1 | 196.6K |
| [cocktailpeanut/xulf-dev](https://huggingface.co/cocktailpeanut/xulf-dev) | `flux1-dev.safetensors` | BF16 | `(64, 3072)` | 1 | 196.6K |
| [cocktailpeanut/xulf-dev](https://huggingface.co/cocktailpeanut/xulf-dev) | `flux1-dev.safetensors` | BF16 | `(128)` | 152 | 19.5K |
| [cocktailpeanut/xulf-dev](https://huggingface.co/cocktailpeanut/xulf-dev) | `flux1-dev.safetensors` | BF16 | `(6144)` | 1 | 6.1K |
| [cocktailpeanut/xulf-dev](https://huggingface.co/cocktailpeanut/xulf-dev) | `flux1-dev.safetensors` | BF16 | `(64)` | 1 | 64 |
| [cocktailpeanut/xulf-dev](https://huggingface.co/cocktailpeanut/xulf-dev) | `ae.safetensors` | FP32 | `(512, 512, 3, 3)` | 30 | 70.8M |
| [cocktailpeanut/xulf-dev](https://huggingface.co/cocktailpeanut/xulf-dev) | `ae.safetensors` | FP32 | `(256, 256, 3, 3)` | 10 | 5.9M |
| [cocktailpeanut/xulf-dev](https://huggingface.co/cocktailpeanut/xulf-dev) | `ae.safetensors` | FP32 | `(512, 512, 1, 1)` | 8 | 2.1M |
| [cocktailpeanut/xulf-dev](https://huggingface.co/cocktailpeanut/xulf-dev) | `ae.safetensors` | FP32 | `(128, 128, 3, 3)` | 10 | 1.5M |
| [cocktailpeanut/xulf-dev](https://huggingface.co/cocktailpeanut/xulf-dev) | `ae.safetensors` | FP32 | `(256, 512, 3, 3)` | 1 | 1.2M |
| [cocktailpeanut/xulf-dev](https://huggingface.co/cocktailpeanut/xulf-dev) | `ae.safetensors` | FP32 | `(512, 256, 3, 3)` | 1 | 1.2M |
| [cocktailpeanut/xulf-dev](https://huggingface.co/cocktailpeanut/xulf-dev) | `ae.safetensors` | FP32 | `(128, 256, 3, 3)` | 1 | 294.9K |
| [cocktailpeanut/xulf-dev](https://huggingface.co/cocktailpeanut/xulf-dev) | `ae.safetensors` | FP32 | `(256, 128, 3, 3)` | 1 | 294.9K |
| [cocktailpeanut/xulf-dev](https://huggingface.co/cocktailpeanut/xulf-dev) | `ae.safetensors` | FP32 | `(32, 512, 3, 3)` | 1 | 147.5K |
| [cocktailpeanut/xulf-dev](https://huggingface.co/cocktailpeanut/xulf-dev) | `ae.safetensors` | FP32 | `(256, 512, 1, 1)` | 1 | 131.1K |
| [cocktailpeanut/xulf-dev](https://huggingface.co/cocktailpeanut/xulf-dev) | `ae.safetensors` | FP32 | `(512, 256, 1, 1)` | 1 | 131.1K |
| [cocktailpeanut/xulf-dev](https://huggingface.co/cocktailpeanut/xulf-dev) | `ae.safetensors` | FP32 | `(512, 16, 3, 3)` | 1 | 73.7K |
| [cocktailpeanut/xulf-dev](https://huggingface.co/cocktailpeanut/xulf-dev) | `ae.safetensors` | FP32 | `(512)` | 103 | 52.7K |
| [cocktailpeanut/xulf-dev](https://huggingface.co/cocktailpeanut/xulf-dev) | `ae.safetensors` | FP32 | `(128, 256, 1, 1)` | 1 | 32.8K |
| [cocktailpeanut/xulf-dev](https://huggingface.co/cocktailpeanut/xulf-dev) | `ae.safetensors` | FP32 | `(256, 128, 1, 1)` | 1 | 32.8K |
| [cocktailpeanut/xulf-dev](https://huggingface.co/cocktailpeanut/xulf-dev) | `ae.safetensors` | FP32 | `(256)` | 34 | 8.7K |
| [cocktailpeanut/xulf-dev](https://huggingface.co/cocktailpeanut/xulf-dev) | `ae.safetensors` | FP32 | `(128)` | 35 | 4.5K |
| [cocktailpeanut/xulf-dev](https://huggingface.co/cocktailpeanut/xulf-dev) | `ae.safetensors` | FP32 | `(128, 3, 3, 3)` | 1 | 3.5K |
| [cocktailpeanut/xulf-dev](https://huggingface.co/cocktailpeanut/xulf-dev) | `ae.safetensors` | FP32 | `(3, 128, 3, 3)` | 1 | 3.5K |
| [cocktailpeanut/xulf-dev](https://huggingface.co/cocktailpeanut/xulf-dev) | `ae.safetensors` | FP32 | `(32)` | 1 | 32 |
| [cocktailpeanut/xulf-dev](https://huggingface.co/cocktailpeanut/xulf-dev) | `ae.safetensors` | FP32 | `(3)` | 1 | 3 |
| [cocktailpeanut/xulf-schnell](https://huggingface.co/cocktailpeanut/xulf-schnell) | `flux1-schnell.safetensors` | BF16 | `(21504, 3072)` | 38 | 2.51B |
| [cocktailpeanut/xulf-schnell](https://huggingface.co/cocktailpeanut/xulf-schnell) | `flux1-schnell.safetensors` | BF16 | `(18432, 3072)` | 38 | 2.15B |
| [cocktailpeanut/xulf-schnell](https://huggingface.co/cocktailpeanut/xulf-schnell) | `flux1-schnell.safetensors` | BF16 | `(9216, 3072)` | 76 | 2.15B |
| [cocktailpeanut/xulf-schnell](https://huggingface.co/cocktailpeanut/xulf-schnell) | `flux1-schnell.safetensors` | BF16 | `(3072, 15360)` | 38 | 1.79B |
| [cocktailpeanut/xulf-schnell](https://huggingface.co/cocktailpeanut/xulf-schnell) | `flux1-schnell.safetensors` | BF16 | `(12288, 3072)` | 38 | 1.43B |
| [cocktailpeanut/xulf-schnell](https://huggingface.co/cocktailpeanut/xulf-schnell) | `flux1-schnell.safetensors` | BF16 | `(3072, 12288)` | 38 | 1.43B |
| [cocktailpeanut/xulf-schnell](https://huggingface.co/cocktailpeanut/xulf-schnell) | `flux1-schnell.safetensors` | BF16 | `(3072, 3072)` | 40 | 377.5M |
| [cocktailpeanut/xulf-schnell](https://huggingface.co/cocktailpeanut/xulf-schnell) | `flux1-schnell.safetensors` | BF16 | `(6144, 3072)` | 1 | 18.9M |
| [cocktailpeanut/xulf-schnell](https://huggingface.co/cocktailpeanut/xulf-schnell) | `flux1-schnell.safetensors` | BF16 | `(3072, 4096)` | 1 | 12.6M |
| [cocktailpeanut/xulf-schnell](https://huggingface.co/cocktailpeanut/xulf-schnell) | `flux1-schnell.safetensors` | BF16 | `(3072, 768)` | 1 | 2.4M |
| [cocktailpeanut/xulf-schnell](https://huggingface.co/cocktailpeanut/xulf-schnell) | `flux1-schnell.safetensors` | BF16 | `(21504)` | 38 | 817.2K |
| [cocktailpeanut/xulf-schnell](https://huggingface.co/cocktailpeanut/xulf-schnell) | `flux1-schnell.safetensors` | BF16 | `(3072, 256)` | 1 | 786.4K |
| [cocktailpeanut/xulf-schnell](https://huggingface.co/cocktailpeanut/xulf-schnell) | `flux1-schnell.safetensors` | BF16 | `(18432)` | 38 | 700.4K |
| [cocktailpeanut/xulf-schnell](https://huggingface.co/cocktailpeanut/xulf-schnell) | `flux1-schnell.safetensors` | BF16 | `(9216)` | 76 | 700.4K |
| [cocktailpeanut/xulf-schnell](https://huggingface.co/cocktailpeanut/xulf-schnell) | `flux1-schnell.safetensors` | BF16 | `(12288)` | 38 | 466.9K |
| [cocktailpeanut/xulf-schnell](https://huggingface.co/cocktailpeanut/xulf-schnell) | `flux1-schnell.safetensors` | BF16 | `(3072)` | 120 | 368.6K |
| [cocktailpeanut/xulf-schnell](https://huggingface.co/cocktailpeanut/xulf-schnell) | `flux1-schnell.safetensors` | BF16 | `(3072, 64)` | 1 | 196.6K |
| [cocktailpeanut/xulf-schnell](https://huggingface.co/cocktailpeanut/xulf-schnell) | `flux1-schnell.safetensors` | BF16 | `(64, 3072)` | 1 | 196.6K |
| [cocktailpeanut/xulf-schnell](https://huggingface.co/cocktailpeanut/xulf-schnell) | `flux1-schnell.safetensors` | BF16 | `(128)` | 152 | 19.5K |
| [cocktailpeanut/xulf-schnell](https://huggingface.co/cocktailpeanut/xulf-schnell) | `flux1-schnell.safetensors` | BF16 | `(6144)` | 1 | 6.1K |
| [cocktailpeanut/xulf-schnell](https://huggingface.co/cocktailpeanut/xulf-schnell) | `flux1-schnell.safetensors` | BF16 | `(64)` | 1 | 64 |
| [cocktailpeanut/xulf-schnell](https://huggingface.co/cocktailpeanut/xulf-schnell) | `ae.safetensors` | FP32 | `(512, 512, 3, 3)` | 30 | 70.8M |
| [cocktailpeanut/xulf-schnell](https://huggingface.co/cocktailpeanut/xulf-schnell) | `ae.safetensors` | FP32 | `(256, 256, 3, 3)` | 10 | 5.9M |
| [cocktailpeanut/xulf-schnell](https://huggingface.co/cocktailpeanut/xulf-schnell) | `ae.safetensors` | FP32 | `(512, 512, 1, 1)` | 8 | 2.1M |
| [cocktailpeanut/xulf-schnell](https://huggingface.co/cocktailpeanut/xulf-schnell) | `ae.safetensors` | FP32 | `(128, 128, 3, 3)` | 10 | 1.5M |
| [cocktailpeanut/xulf-schnell](https://huggingface.co/cocktailpeanut/xulf-schnell) | `ae.safetensors` | FP32 | `(256, 512, 3, 3)` | 1 | 1.2M |
| [cocktailpeanut/xulf-schnell](https://huggingface.co/cocktailpeanut/xulf-schnell) | `ae.safetensors` | FP32 | `(512, 256, 3, 3)` | 1 | 1.2M |
| [cocktailpeanut/xulf-schnell](https://huggingface.co/cocktailpeanut/xulf-schnell) | `ae.safetensors` | FP32 | `(128, 256, 3, 3)` | 1 | 294.9K |
| [cocktailpeanut/xulf-schnell](https://huggingface.co/cocktailpeanut/xulf-schnell) | `ae.safetensors` | FP32 | `(256, 128, 3, 3)` | 1 | 294.9K |
| [cocktailpeanut/xulf-schnell](https://huggingface.co/cocktailpeanut/xulf-schnell) | `ae.safetensors` | FP32 | `(32, 512, 3, 3)` | 1 | 147.5K |
| [cocktailpeanut/xulf-schnell](https://huggingface.co/cocktailpeanut/xulf-schnell) | `ae.safetensors` | FP32 | `(256, 512, 1, 1)` | 1 | 131.1K |
| [cocktailpeanut/xulf-schnell](https://huggingface.co/cocktailpeanut/xulf-schnell) | `ae.safetensors` | FP32 | `(512, 256, 1, 1)` | 1 | 131.1K |
| [cocktailpeanut/xulf-schnell](https://huggingface.co/cocktailpeanut/xulf-schnell) | `ae.safetensors` | FP32 | `(512, 16, 3, 3)` | 1 | 73.7K |
| [cocktailpeanut/xulf-schnell](https://huggingface.co/cocktailpeanut/xulf-schnell) | `ae.safetensors` | FP32 | `(512)` | 103 | 52.7K |
| [cocktailpeanut/xulf-schnell](https://huggingface.co/cocktailpeanut/xulf-schnell) | `ae.safetensors` | FP32 | `(128, 256, 1, 1)` | 1 | 32.8K |
| [cocktailpeanut/xulf-schnell](https://huggingface.co/cocktailpeanut/xulf-schnell) | `ae.safetensors` | FP32 | `(256, 128, 1, 1)` | 1 | 32.8K |
| [cocktailpeanut/xulf-schnell](https://huggingface.co/cocktailpeanut/xulf-schnell) | `ae.safetensors` | FP32 | `(256)` | 34 | 8.7K |
| [cocktailpeanut/xulf-schnell](https://huggingface.co/cocktailpeanut/xulf-schnell) | `ae.safetensors` | FP32 | `(128)` | 35 | 4.5K |
| [cocktailpeanut/xulf-schnell](https://huggingface.co/cocktailpeanut/xulf-schnell) | `ae.safetensors` | FP32 | `(128, 3, 3, 3)` | 1 | 3.5K |
| [cocktailpeanut/xulf-schnell](https://huggingface.co/cocktailpeanut/xulf-schnell) | `ae.safetensors` | FP32 | `(3, 128, 3, 3)` | 1 | 3.5K |
| [cocktailpeanut/xulf-schnell](https://huggingface.co/cocktailpeanut/xulf-schnell) | `ae.safetensors` | FP32 | `(32)` | 1 | 32 |
| [cocktailpeanut/xulf-schnell](https://huggingface.co/cocktailpeanut/xulf-schnell) | `ae.safetensors` | FP32 | `(3)` | 1 | 3 |
| [Comfy-Org/flux1-dev](https://huggingface.co/Comfy-Org/flux1-dev) | `flux1-dev-fp8.safetensors` | FP16 | `(49408, 768)` | 1 | 37.9M |
| [Comfy-Org/flux1-dev](https://huggingface.co/Comfy-Org/flux1-dev) | `flux1-dev-fp8.safetensors` | FP16 | `(768, 768)` | 49 | 28.9M |
| [Comfy-Org/flux1-dev](https://huggingface.co/Comfy-Org/flux1-dev) | `flux1-dev-fp8.safetensors` | FP16 | `(3072, 768)` | 12 | 28.3M |
| [Comfy-Org/flux1-dev](https://huggingface.co/Comfy-Org/flux1-dev) | `flux1-dev-fp8.safetensors` | FP16 | `(768, 3072)` | 12 | 28.3M |
| [Comfy-Org/flux1-dev](https://huggingface.co/Comfy-Org/flux1-dev) | `flux1-dev-fp8.safetensors` | FP16 | `(768)` | 110 | 84.5K |
| [Comfy-Org/flux1-dev](https://huggingface.co/Comfy-Org/flux1-dev) | `flux1-dev-fp8.safetensors` | FP16 | `(77, 768)` | 1 | 59.1K |
| [Comfy-Org/flux1-dev](https://huggingface.co/Comfy-Org/flux1-dev) | `flux1-dev-fp8.safetensors` | FP16 | `(3072)` | 12 | 36.9K |
| [Comfy-Org/flux1-dev](https://huggingface.co/Comfy-Org/flux1-dev) | `flux1-dev-fp8.safetensors` | FP32 | `(512, 512, 3, 3)` | 30 | 70.8M |
| [Comfy-Org/flux1-dev](https://huggingface.co/Comfy-Org/flux1-dev) | `flux1-dev-fp8.safetensors` | FP32 | `(256, 256, 3, 3)` | 10 | 5.9M |
| [Comfy-Org/flux1-dev](https://huggingface.co/Comfy-Org/flux1-dev) | `flux1-dev-fp8.safetensors` | FP32 | `(512, 512, 1, 1)` | 8 | 2.1M |
| [Comfy-Org/flux1-dev](https://huggingface.co/Comfy-Org/flux1-dev) | `flux1-dev-fp8.safetensors` | FP32 | `(128, 128, 3, 3)` | 10 | 1.5M |
| [Comfy-Org/flux1-dev](https://huggingface.co/Comfy-Org/flux1-dev) | `flux1-dev-fp8.safetensors` | FP32 | `(256, 512, 3, 3)` | 1 | 1.2M |
| [Comfy-Org/flux1-dev](https://huggingface.co/Comfy-Org/flux1-dev) | `flux1-dev-fp8.safetensors` | FP32 | `(512, 256, 3, 3)` | 1 | 1.2M |
| [Comfy-Org/flux1-dev](https://huggingface.co/Comfy-Org/flux1-dev) | `flux1-dev-fp8.safetensors` | FP32 | `(128, 256, 3, 3)` | 1 | 294.9K |
| [Comfy-Org/flux1-dev](https://huggingface.co/Comfy-Org/flux1-dev) | `flux1-dev-fp8.safetensors` | FP32 | `(256, 128, 3, 3)` | 1 | 294.9K |
| [Comfy-Org/flux1-dev](https://huggingface.co/Comfy-Org/flux1-dev) | `flux1-dev-fp8.safetensors` | FP32 | `(32, 512, 3, 3)` | 1 | 147.5K |
| [Comfy-Org/flux1-dev](https://huggingface.co/Comfy-Org/flux1-dev) | `flux1-dev-fp8.safetensors` | FP32 | `(256, 512, 1, 1)` | 1 | 131.1K |
| [Comfy-Org/flux1-dev](https://huggingface.co/Comfy-Org/flux1-dev) | `flux1-dev-fp8.safetensors` | FP32 | `(512, 256, 1, 1)` | 1 | 131.1K |
| [Comfy-Org/flux1-dev](https://huggingface.co/Comfy-Org/flux1-dev) | `flux1-dev-fp8.safetensors` | FP32 | `(512, 16, 3, 3)` | 1 | 73.7K |
| [Comfy-Org/flux1-dev](https://huggingface.co/Comfy-Org/flux1-dev) | `flux1-dev-fp8.safetensors` | FP32 | `(512)` | 103 | 52.7K |
| [Comfy-Org/flux1-dev](https://huggingface.co/Comfy-Org/flux1-dev) | `flux1-dev-fp8.safetensors` | FP32 | `(128, 256, 1, 1)` | 1 | 32.8K |
| [Comfy-Org/flux1-dev](https://huggingface.co/Comfy-Org/flux1-dev) | `flux1-dev-fp8.safetensors` | FP32 | `(256, 128, 1, 1)` | 1 | 32.8K |
| [Comfy-Org/flux1-dev](https://huggingface.co/Comfy-Org/flux1-dev) | `flux1-dev-fp8.safetensors` | FP32 | `(256)` | 34 | 8.7K |
| [Comfy-Org/flux1-dev](https://huggingface.co/Comfy-Org/flux1-dev) | `flux1-dev-fp8.safetensors` | FP32 | `(128)` | 35 | 4.5K |
| [Comfy-Org/flux1-dev](https://huggingface.co/Comfy-Org/flux1-dev) | `flux1-dev-fp8.safetensors` | FP32 | `(128, 3, 3, 3)` | 1 | 3.5K |
| [Comfy-Org/flux1-dev](https://huggingface.co/Comfy-Org/flux1-dev) | `flux1-dev-fp8.safetensors` | FP32 | `(3, 128, 3, 3)` | 1 | 3.5K |
| [Comfy-Org/flux1-dev](https://huggingface.co/Comfy-Org/flux1-dev) | `flux1-dev-fp8.safetensors` | FP32 | `(32)` | 1 | 32 |
| [Comfy-Org/flux1-dev](https://huggingface.co/Comfy-Org/flux1-dev) | `flux1-dev-fp8.safetensors` | FP32 | `(3)` | 1 | 3 |
| [Comfy-Org/flux1-dev](https://huggingface.co/Comfy-Org/flux1-dev) | `flux1-dev-fp8.safetensors` | FP32 | `()` | 2 | 2 |
| [Comfy-Org/flux1-dev](https://huggingface.co/Comfy-Org/flux1-dev) | `flux1-dev-fp8.safetensors` | FP8 (E4M3FN) | `(21504, 3072)` | 38 | 2.51B |
| [Comfy-Org/flux1-dev](https://huggingface.co/Comfy-Org/flux1-dev) | `flux1-dev-fp8.safetensors` | FP8 (E4M3FN) | `(18432, 3072)` | 38 | 2.15B |
| [Comfy-Org/flux1-dev](https://huggingface.co/Comfy-Org/flux1-dev) | `flux1-dev-fp8.safetensors` | FP8 (E4M3FN) | `(9216, 3072)` | 76 | 2.15B |
| [Comfy-Org/flux1-dev](https://huggingface.co/Comfy-Org/flux1-dev) | `flux1-dev-fp8.safetensors` | FP8 (E4M3FN) | `(10240, 4096)` | 48 | 2.01B |
| [Comfy-Org/flux1-dev](https://huggingface.co/Comfy-Org/flux1-dev) | `flux1-dev-fp8.safetensors` | FP8 (E4M3FN) | `(3072, 15360)` | 38 | 1.79B |
| [Comfy-Org/flux1-dev](https://huggingface.co/Comfy-Org/flux1-dev) | `flux1-dev-fp8.safetensors` | FP8 (E4M3FN) | `(4096, 4096)` | 96 | 1.61B |
| [Comfy-Org/flux1-dev](https://huggingface.co/Comfy-Org/flux1-dev) | `flux1-dev-fp8.safetensors` | FP8 (E4M3FN) | `(12288, 3072)` | 38 | 1.43B |
| [Comfy-Org/flux1-dev](https://huggingface.co/Comfy-Org/flux1-dev) | `flux1-dev-fp8.safetensors` | FP8 (E4M3FN) | `(3072, 12288)` | 38 | 1.43B |
| [Comfy-Org/flux1-dev](https://huggingface.co/Comfy-Org/flux1-dev) | `flux1-dev-fp8.safetensors` | FP8 (E4M3FN) | `(4096, 10240)` | 24 | 1.01B |
| [Comfy-Org/flux1-dev](https://huggingface.co/Comfy-Org/flux1-dev) | `flux1-dev-fp8.safetensors` | FP8 (E4M3FN) | `(3072, 3072)` | 41 | 386.9M |
| [Comfy-Org/flux1-dev](https://huggingface.co/Comfy-Org/flux1-dev) | `flux1-dev-fp8.safetensors` | FP8 (E4M3FN) | `(32128, 4096)` | 1 | 131.6M |
| [Comfy-Org/flux1-dev](https://huggingface.co/Comfy-Org/flux1-dev) | `flux1-dev-fp8.safetensors` | FP8 (E4M3FN) | `(6144, 3072)` | 1 | 18.9M |
| [Comfy-Org/flux1-dev](https://huggingface.co/Comfy-Org/flux1-dev) | `flux1-dev-fp8.safetensors` | FP8 (E4M3FN) | `(3072, 4096)` | 1 | 12.6M |
| [Comfy-Org/flux1-dev](https://huggingface.co/Comfy-Org/flux1-dev) | `flux1-dev-fp8.safetensors` | FP8 (E4M3FN) | `(3072, 768)` | 1 | 2.4M |
| [Comfy-Org/flux1-dev](https://huggingface.co/Comfy-Org/flux1-dev) | `flux1-dev-fp8.safetensors` | FP8 (E4M3FN) | `(3072, 256)` | 2 | 1.6M |
| [Comfy-Org/flux1-dev](https://huggingface.co/Comfy-Org/flux1-dev) | `flux1-dev-fp8.safetensors` | FP8 (E4M3FN) | `(21504)` | 38 | 817.2K |
| [Comfy-Org/flux1-dev](https://huggingface.co/Comfy-Org/flux1-dev) | `flux1-dev-fp8.safetensors` | FP8 (E4M3FN) | `(18432)` | 38 | 700.4K |
| [Comfy-Org/flux1-dev](https://huggingface.co/Comfy-Org/flux1-dev) | `flux1-dev-fp8.safetensors` | FP8 (E4M3FN) | `(9216)` | 76 | 700.4K |
| [Comfy-Org/flux1-dev](https://huggingface.co/Comfy-Org/flux1-dev) | `flux1-dev-fp8.safetensors` | FP8 (E4M3FN) | `(12288)` | 38 | 466.9K |
| [Comfy-Org/flux1-dev](https://huggingface.co/Comfy-Org/flux1-dev) | `flux1-dev-fp8.safetensors` | FP8 (E4M3FN) | `(3072)` | 122 | 374.8K |
| [Comfy-Org/flux1-dev](https://huggingface.co/Comfy-Org/flux1-dev) | `flux1-dev-fp8.safetensors` | FP8 (E4M3FN) | `(4096)` | 49 | 200.7K |
| [Comfy-Org/flux1-dev](https://huggingface.co/Comfy-Org/flux1-dev) | `flux1-dev-fp8.safetensors` | FP8 (E4M3FN) | `(3072, 64)` | 1 | 196.6K |
| [Comfy-Org/flux1-dev](https://huggingface.co/Comfy-Org/flux1-dev) | `flux1-dev-fp8.safetensors` | FP8 (E4M3FN) | `(64, 3072)` | 1 | 196.6K |
| [Comfy-Org/flux1-dev](https://huggingface.co/Comfy-Org/flux1-dev) | `flux1-dev-fp8.safetensors` | FP8 (E4M3FN) | `(128)` | 152 | 19.5K |
| [Comfy-Org/flux1-dev](https://huggingface.co/Comfy-Org/flux1-dev) | `flux1-dev-fp8.safetensors` | FP8 (E4M3FN) | `(6144)` | 1 | 6.1K |
| [Comfy-Org/flux1-dev](https://huggingface.co/Comfy-Org/flux1-dev) | `flux1-dev-fp8.safetensors` | FP8 (E4M3FN) | `(32, 64)` | 1 | 2.0K |
| [Comfy-Org/flux1-dev](https://huggingface.co/Comfy-Org/flux1-dev) | `flux1-dev-fp8.safetensors` | FP8 (E4M3FN) | `(64)` | 1 | 64 |
| [Comfy-Org/flux1-schnell](https://huggingface.co/Comfy-Org/flux1-schnell) | `flux1-schnell-fp8.safetensors` | FP16 | `(49408, 768)` | 1 | 37.9M |
| [Comfy-Org/flux1-schnell](https://huggingface.co/Comfy-Org/flux1-schnell) | `flux1-schnell-fp8.safetensors` | FP16 | `(768, 768)` | 49 | 28.9M |
| [Comfy-Org/flux1-schnell](https://huggingface.co/Comfy-Org/flux1-schnell) | `flux1-schnell-fp8.safetensors` | FP16 | `(3072, 768)` | 12 | 28.3M |
| [Comfy-Org/flux1-schnell](https://huggingface.co/Comfy-Org/flux1-schnell) | `flux1-schnell-fp8.safetensors` | FP16 | `(768, 3072)` | 12 | 28.3M |
| [Comfy-Org/flux1-schnell](https://huggingface.co/Comfy-Org/flux1-schnell) | `flux1-schnell-fp8.safetensors` | FP16 | `(768)` | 110 | 84.5K |
| [Comfy-Org/flux1-schnell](https://huggingface.co/Comfy-Org/flux1-schnell) | `flux1-schnell-fp8.safetensors` | FP16 | `(77, 768)` | 1 | 59.1K |
| [Comfy-Org/flux1-schnell](https://huggingface.co/Comfy-Org/flux1-schnell) | `flux1-schnell-fp8.safetensors` | FP16 | `(3072)` | 12 | 36.9K |
| [Comfy-Org/flux1-schnell](https://huggingface.co/Comfy-Org/flux1-schnell) | `flux1-schnell-fp8.safetensors` | FP32 | `(512, 512, 3, 3)` | 30 | 70.8M |
| [Comfy-Org/flux1-schnell](https://huggingface.co/Comfy-Org/flux1-schnell) | `flux1-schnell-fp8.safetensors` | FP32 | `(256, 256, 3, 3)` | 10 | 5.9M |
| [Comfy-Org/flux1-schnell](https://huggingface.co/Comfy-Org/flux1-schnell) | `flux1-schnell-fp8.safetensors` | FP32 | `(512, 512, 1, 1)` | 8 | 2.1M |
| [Comfy-Org/flux1-schnell](https://huggingface.co/Comfy-Org/flux1-schnell) | `flux1-schnell-fp8.safetensors` | FP32 | `(128, 128, 3, 3)` | 10 | 1.5M |
| [Comfy-Org/flux1-schnell](https://huggingface.co/Comfy-Org/flux1-schnell) | `flux1-schnell-fp8.safetensors` | FP32 | `(256, 512, 3, 3)` | 1 | 1.2M |
| [Comfy-Org/flux1-schnell](https://huggingface.co/Comfy-Org/flux1-schnell) | `flux1-schnell-fp8.safetensors` | FP32 | `(512, 256, 3, 3)` | 1 | 1.2M |
| [Comfy-Org/flux1-schnell](https://huggingface.co/Comfy-Org/flux1-schnell) | `flux1-schnell-fp8.safetensors` | FP32 | `(128, 256, 3, 3)` | 1 | 294.9K |
| [Comfy-Org/flux1-schnell](https://huggingface.co/Comfy-Org/flux1-schnell) | `flux1-schnell-fp8.safetensors` | FP32 | `(256, 128, 3, 3)` | 1 | 294.9K |
| [Comfy-Org/flux1-schnell](https://huggingface.co/Comfy-Org/flux1-schnell) | `flux1-schnell-fp8.safetensors` | FP32 | `(32, 512, 3, 3)` | 1 | 147.5K |
| [Comfy-Org/flux1-schnell](https://huggingface.co/Comfy-Org/flux1-schnell) | `flux1-schnell-fp8.safetensors` | FP32 | `(256, 512, 1, 1)` | 1 | 131.1K |
| [Comfy-Org/flux1-schnell](https://huggingface.co/Comfy-Org/flux1-schnell) | `flux1-schnell-fp8.safetensors` | FP32 | `(512, 256, 1, 1)` | 1 | 131.1K |
| [Comfy-Org/flux1-schnell](https://huggingface.co/Comfy-Org/flux1-schnell) | `flux1-schnell-fp8.safetensors` | FP32 | `(512, 16, 3, 3)` | 1 | 73.7K |
| [Comfy-Org/flux1-schnell](https://huggingface.co/Comfy-Org/flux1-schnell) | `flux1-schnell-fp8.safetensors` | FP32 | `(512)` | 103 | 52.7K |
| [Comfy-Org/flux1-schnell](https://huggingface.co/Comfy-Org/flux1-schnell) | `flux1-schnell-fp8.safetensors` | FP32 | `(128, 256, 1, 1)` | 1 | 32.8K |
| [Comfy-Org/flux1-schnell](https://huggingface.co/Comfy-Org/flux1-schnell) | `flux1-schnell-fp8.safetensors` | FP32 | `(256, 128, 1, 1)` | 1 | 32.8K |
| [Comfy-Org/flux1-schnell](https://huggingface.co/Comfy-Org/flux1-schnell) | `flux1-schnell-fp8.safetensors` | FP32 | `(256)` | 34 | 8.7K |
| [Comfy-Org/flux1-schnell](https://huggingface.co/Comfy-Org/flux1-schnell) | `flux1-schnell-fp8.safetensors` | FP32 | `(128)` | 35 | 4.5K |
| [Comfy-Org/flux1-schnell](https://huggingface.co/Comfy-Org/flux1-schnell) | `flux1-schnell-fp8.safetensors` | FP32 | `(128, 3, 3, 3)` | 1 | 3.5K |
| [Comfy-Org/flux1-schnell](https://huggingface.co/Comfy-Org/flux1-schnell) | `flux1-schnell-fp8.safetensors` | FP32 | `(3, 128, 3, 3)` | 1 | 3.5K |
| [Comfy-Org/flux1-schnell](https://huggingface.co/Comfy-Org/flux1-schnell) | `flux1-schnell-fp8.safetensors` | FP32 | `(32)` | 1 | 32 |
| [Comfy-Org/flux1-schnell](https://huggingface.co/Comfy-Org/flux1-schnell) | `flux1-schnell-fp8.safetensors` | FP32 | `(3)` | 1 | 3 |
| [Comfy-Org/flux1-schnell](https://huggingface.co/Comfy-Org/flux1-schnell) | `flux1-schnell-fp8.safetensors` | FP32 | `()` | 2 | 2 |
| [Comfy-Org/flux1-schnell](https://huggingface.co/Comfy-Org/flux1-schnell) | `flux1-schnell-fp8.safetensors` | FP8 (E4M3FN) | `(21504, 3072)` | 38 | 2.51B |
| [Comfy-Org/flux1-schnell](https://huggingface.co/Comfy-Org/flux1-schnell) | `flux1-schnell-fp8.safetensors` | FP8 (E4M3FN) | `(18432, 3072)` | 38 | 2.15B |
| [Comfy-Org/flux1-schnell](https://huggingface.co/Comfy-Org/flux1-schnell) | `flux1-schnell-fp8.safetensors` | FP8 (E4M3FN) | `(9216, 3072)` | 76 | 2.15B |
| [Comfy-Org/flux1-schnell](https://huggingface.co/Comfy-Org/flux1-schnell) | `flux1-schnell-fp8.safetensors` | FP8 (E4M3FN) | `(10240, 4096)` | 48 | 2.01B |
| [Comfy-Org/flux1-schnell](https://huggingface.co/Comfy-Org/flux1-schnell) | `flux1-schnell-fp8.safetensors` | FP8 (E4M3FN) | `(3072, 15360)` | 38 | 1.79B |
| [Comfy-Org/flux1-schnell](https://huggingface.co/Comfy-Org/flux1-schnell) | `flux1-schnell-fp8.safetensors` | FP8 (E4M3FN) | `(4096, 4096)` | 96 | 1.61B |
| [Comfy-Org/flux1-schnell](https://huggingface.co/Comfy-Org/flux1-schnell) | `flux1-schnell-fp8.safetensors` | FP8 (E4M3FN) | `(12288, 3072)` | 38 | 1.43B |
| [Comfy-Org/flux1-schnell](https://huggingface.co/Comfy-Org/flux1-schnell) | `flux1-schnell-fp8.safetensors` | FP8 (E4M3FN) | `(3072, 12288)` | 38 | 1.43B |
| [Comfy-Org/flux1-schnell](https://huggingface.co/Comfy-Org/flux1-schnell) | `flux1-schnell-fp8.safetensors` | FP8 (E4M3FN) | `(4096, 10240)` | 24 | 1.01B |
| [Comfy-Org/flux1-schnell](https://huggingface.co/Comfy-Org/flux1-schnell) | `flux1-schnell-fp8.safetensors` | FP8 (E4M3FN) | `(3072, 3072)` | 40 | 377.5M |
| [Comfy-Org/flux1-schnell](https://huggingface.co/Comfy-Org/flux1-schnell) | `flux1-schnell-fp8.safetensors` | FP8 (E4M3FN) | `(32128, 4096)` | 1 | 131.6M |
| [Comfy-Org/flux1-schnell](https://huggingface.co/Comfy-Org/flux1-schnell) | `flux1-schnell-fp8.safetensors` | FP8 (E4M3FN) | `(6144, 3072)` | 1 | 18.9M |
| [Comfy-Org/flux1-schnell](https://huggingface.co/Comfy-Org/flux1-schnell) | `flux1-schnell-fp8.safetensors` | FP8 (E4M3FN) | `(3072, 4096)` | 1 | 12.6M |
| [Comfy-Org/flux1-schnell](https://huggingface.co/Comfy-Org/flux1-schnell) | `flux1-schnell-fp8.safetensors` | FP8 (E4M3FN) | `(3072, 768)` | 1 | 2.4M |
| [Comfy-Org/flux1-schnell](https://huggingface.co/Comfy-Org/flux1-schnell) | `flux1-schnell-fp8.safetensors` | FP8 (E4M3FN) | `(21504)` | 38 | 817.2K |
| [Comfy-Org/flux1-schnell](https://huggingface.co/Comfy-Org/flux1-schnell) | `flux1-schnell-fp8.safetensors` | FP8 (E4M3FN) | `(3072, 256)` | 1 | 786.4K |
| [Comfy-Org/flux1-schnell](https://huggingface.co/Comfy-Org/flux1-schnell) | `flux1-schnell-fp8.safetensors` | FP8 (E4M3FN) | `(18432)` | 38 | 700.4K |
| [Comfy-Org/flux1-schnell](https://huggingface.co/Comfy-Org/flux1-schnell) | `flux1-schnell-fp8.safetensors` | FP8 (E4M3FN) | `(9216)` | 76 | 700.4K |
| [Comfy-Org/flux1-schnell](https://huggingface.co/Comfy-Org/flux1-schnell) | `flux1-schnell-fp8.safetensors` | FP8 (E4M3FN) | `(12288)` | 38 | 466.9K |
| [Comfy-Org/flux1-schnell](https://huggingface.co/Comfy-Org/flux1-schnell) | `flux1-schnell-fp8.safetensors` | FP8 (E4M3FN) | `(3072)` | 120 | 368.6K |
| [Comfy-Org/flux1-schnell](https://huggingface.co/Comfy-Org/flux1-schnell) | `flux1-schnell-fp8.safetensors` | FP8 (E4M3FN) | `(4096)` | 49 | 200.7K |
| [Comfy-Org/flux1-schnell](https://huggingface.co/Comfy-Org/flux1-schnell) | `flux1-schnell-fp8.safetensors` | FP8 (E4M3FN) | `(3072, 64)` | 1 | 196.6K |
| [Comfy-Org/flux1-schnell](https://huggingface.co/Comfy-Org/flux1-schnell) | `flux1-schnell-fp8.safetensors` | FP8 (E4M3FN) | `(64, 3072)` | 1 | 196.6K |
| [Comfy-Org/flux1-schnell](https://huggingface.co/Comfy-Org/flux1-schnell) | `flux1-schnell-fp8.safetensors` | FP8 (E4M3FN) | `(128)` | 152 | 19.5K |
| [Comfy-Org/flux1-schnell](https://huggingface.co/Comfy-Org/flux1-schnell) | `flux1-schnell-fp8.safetensors` | FP8 (E4M3FN) | `(6144)` | 1 | 6.1K |
| [Comfy-Org/flux1-schnell](https://huggingface.co/Comfy-Org/flux1-schnell) | `flux1-schnell-fp8.safetensors` | FP8 (E4M3FN) | `(32, 64)` | 1 | 2.0K |
| [Comfy-Org/flux1-schnell](https://huggingface.co/Comfy-Org/flux1-schnell) | `flux1-schnell-fp8.safetensors` | FP8 (E4M3FN) | `(64)` | 1 | 64 |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `split_files/diffusion_models/mochi_preview_bf16.safetensors` | BF16 | `(16384, 3072)` | 48 | 2.42B |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `split_files/diffusion_models/mochi_preview_bf16.safetensors` | BF16 | `(12288, 3072)` | 48 | 1.81B |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `split_files/diffusion_models/mochi_preview_bf16.safetensors` | BF16 | `(9216, 3072)` | 48 | 1.36B |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `split_files/diffusion_models/mochi_preview_bf16.safetensors` | BF16 | `(3072, 8192)` | 48 | 1.21B |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `split_files/diffusion_models/mochi_preview_bf16.safetensors` | BF16 | `(6144, 3072)` | 48 | 906.0M |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `split_files/diffusion_models/mochi_preview_bf16.safetensors` | BF16 | `(9216, 1536)` | 48 | 679.5M |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `split_files/diffusion_models/mochi_preview_bf16.safetensors` | BF16 | `(8192, 1536)` | 47 | 591.4M |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `split_files/diffusion_models/mochi_preview_bf16.safetensors` | BF16 | `(3072, 3072)` | 49 | 462.4M |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `split_files/diffusion_models/mochi_preview_bf16.safetensors` | BF16 | `(1536, 4096)` | 48 | 302.0M |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `split_files/diffusion_models/mochi_preview_bf16.safetensors` | BF16 | `(1536, 3072)` | 48 | 226.5M |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `split_files/diffusion_models/mochi_preview_bf16.safetensors` | BF16 | `(8192, 4096)` | 1 | 33.6M |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `split_files/diffusion_models/mochi_preview_bf16.safetensors` | BF16 | `(4096, 4096)` | 1 | 16.8M |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `split_files/diffusion_models/mochi_preview_bf16.safetensors` | BF16 | `(3072, 4096)` | 1 | 12.6M |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `split_files/diffusion_models/mochi_preview_bf16.safetensors` | BF16 | `(3072, 256)` | 1 | 786.4K |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `split_files/diffusion_models/mochi_preview_bf16.safetensors` | BF16 | `(12288)` | 48 | 589.8K |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `split_files/diffusion_models/mochi_preview_bf16.safetensors` | BF16 | `(6144)` | 48 | 294.9K |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `split_files/diffusion_models/mochi_preview_bf16.safetensors` | BF16 | `(3072)` | 52 | 159.7K |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `split_files/diffusion_models/mochi_preview_bf16.safetensors` | BF16 | `(3072, 12, 2, 2)` | 1 | 147.5K |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `all_in_one/mochi_preview_fp8_scaled.safetensors` | BF16 | `(3072, 12, 2, 2)` | 1 | 147.5K |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `split_files/diffusion_models/mochi_preview_bf16.safetensors` | BF16 | `(48, 3072)` | 1 | 147.5K |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `split_files/diffusion_models/mochi_preview_bf16.safetensors` | BF16 | `(1536)` | 49 | 75.3K |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `split_files/diffusion_models/mochi_preview_bf16.safetensors` | BF16 | `(128)` | 192 | 24.6K |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `all_in_one/mochi_preview_fp8_scaled.safetensors` | BF16 | `(128)` | 192 | 24.6K |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `split_files/diffusion_models/mochi_preview_bf16.safetensors` | BF16 | `(8192)` | 1 | 8.2K |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `split_files/diffusion_models/mochi_preview_bf16.safetensors` | BF16 | `(3, 24, 64)` | 1 | 4.6K |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `all_in_one/mochi_preview_fp8_scaled.safetensors` | BF16 | `(3, 24, 64)` | 1 | 4.6K |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `split_files/diffusion_models/mochi_preview_bf16.safetensors` | BF16 | `(4096)` | 1 | 4.1K |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `all_in_one/mochi_preview_fp8_scaled.safetensors` | BF16 | `(3072)` | 1 | 3.1K |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `split_files/diffusion_models/mochi_preview_bf16.safetensors` | BF16 | `(48)` | 1 | 48 |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `split_files/text_encoders/t5xxl_fp16.safetensors` | FP16 | `(10240, 4096)` | 48 | 2.01B |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `split_files/text_encoders/t5xxl_fp16.safetensors` | FP16 | `(4096, 4096)` | 96 | 1.61B |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `split_files/text_encoders/t5xxl_fp16.safetensors` | FP16 | `(4096, 10240)` | 24 | 1.01B |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `all_in_one/mochi_preview_fp8_scaled.safetensors` | FP16 | `(768, 768, 3, 3, 3)` | 18 | 286.7M |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `split_files/vae/mochi_vae.safetensors` | FP16 | `(768, 768, 3, 3, 3)` | 18 | 286.7M |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `split_files/text_encoders/t5xxl_fp16.safetensors` | FP16 | `(32128, 4096)` | 2 | 263.2M |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `all_in_one/mochi_preview_fp8_scaled.safetensors` | FP16 | `(32128, 4096)` | 1 | 131.6M |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `all_in_one/mochi_preview_fp8_scaled.safetensors` | FP16 | `(384, 384, 3, 3, 3)` | 18 | 71.7M |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `split_files/vae/mochi_vae.safetensors` | FP16 | `(384, 384, 3, 3, 3)` | 18 | 71.7M |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `all_in_one/mochi_preview_fp8_scaled.safetensors` | FP16 | `(512, 512, 3, 3, 3)` | 8 | 56.6M |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `split_files/vae/mochi_vae.safetensors` | FP16 | `(512, 512, 3, 3, 3)` | 8 | 56.6M |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `all_in_one/mochi_preview_fp8_scaled.safetensors` | FP16 | `(256, 256, 3, 3, 3)` | 14 | 24.8M |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `split_files/vae/mochi_vae.safetensors` | FP16 | `(256, 256, 3, 3, 3)` | 14 | 24.8M |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `all_in_one/mochi_preview_fp8_scaled.safetensors` | FP16 | `(128, 128, 3, 3, 3)` | 12 | 5.3M |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `split_files/vae/mochi_vae.safetensors` | FP16 | `(128, 128, 3, 3, 3)` | 12 | 5.3M |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `all_in_one/mochi_preview_fp8_scaled.safetensors` | FP16 | `(6144, 768)` | 1 | 4.7M |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `split_files/vae/mochi_vae.safetensors` | FP16 | `(6144, 768)` | 1 | 4.7M |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `all_in_one/mochi_preview_fp8_scaled.safetensors` | FP16 | `(1152, 384)` | 9 | 4.0M |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `split_files/vae/mochi_vae.safetensors` | FP16 | `(1152, 384)` | 9 | 4.0M |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `all_in_one/mochi_preview_fp8_scaled.safetensors` | FP16 | `(384, 384)` | 9 | 1.3M |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `split_files/vae/mochi_vae.safetensors` | FP16 | `(384, 384)` | 9 | 1.3M |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `all_in_one/mochi_preview_fp8_scaled.safetensors` | FP16 | `(384, 256, 3, 2, 2)` | 1 | 1.2M |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `split_files/vae/mochi_vae.safetensors` | FP16 | `(384, 256, 3, 2, 2)` | 1 | 1.2M |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `all_in_one/mochi_preview_fp8_scaled.safetensors` | FP16 | `(2048, 512)` | 1 | 1.0M |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `split_files/vae/mochi_vae.safetensors` | FP16 | `(2048, 512)` | 1 | 1.0M |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `all_in_one/mochi_preview_fp8_scaled.safetensors` | FP16 | `(768, 256)` | 4 | 786.4K |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `split_files/vae/mochi_vae.safetensors` | FP16 | `(768, 256)` | 4 | 786.4K |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `all_in_one/mochi_preview_fp8_scaled.safetensors` | FP16 | `(64, 64, 3, 3, 3)` | 6 | 663.6K |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `split_files/vae/mochi_vae.safetensors` | FP16 | `(64, 64, 3, 3, 3)` | 6 | 663.6K |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `all_in_one/mochi_preview_fp8_scaled.safetensors` | FP16 | `(256, 128, 2, 2, 2)` | 1 | 262.1K |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `split_files/vae/mochi_vae.safetensors` | FP16 | `(256, 128, 2, 2, 2)` | 1 | 262.1K |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `all_in_one/mochi_preview_fp8_scaled.safetensors` | FP16 | `(256, 256)` | 4 | 262.1K |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `split_files/vae/mochi_vae.safetensors` | FP16 | `(256, 256)` | 4 | 262.1K |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `all_in_one/mochi_preview_fp8_scaled.safetensors` | FP16 | `(4096)` | 49 | 200.7K |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `split_files/text_encoders/t5xxl_fp16.safetensors` | FP16 | `(4096)` | 49 | 200.7K |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `all_in_one/mochi_preview_fp8_scaled.safetensors` | FP16 | `(384, 128)` | 3 | 147.5K |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `split_files/vae/mochi_vae.safetensors` | FP16 | `(384, 128)` | 3 | 147.5K |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `all_in_one/mochi_preview_fp8_scaled.safetensors` | FP16 | `(512, 256)` | 1 | 131.1K |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `split_files/vae/mochi_vae.safetensors` | FP16 | `(512, 256)` | 1 | 131.1K |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `all_in_one/mochi_preview_fp8_scaled.safetensors` | FP16 | `(128, 128)` | 3 | 49.2K |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `split_files/vae/mochi_vae.safetensors` | FP16 | `(128, 128)` | 3 | 49.2K |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `all_in_one/mochi_preview_fp8_scaled.safetensors` | FP16 | `(768)` | 55 | 42.2K |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `split_files/vae/mochi_vae.safetensors` | FP16 | `(768)` | 55 | 42.2K |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `all_in_one/mochi_preview_fp8_scaled.safetensors` | FP16 | `(128, 64, 1, 2, 2)` | 1 | 32.8K |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `split_files/vae/mochi_vae.safetensors` | FP16 | `(128, 64, 1, 2, 2)` | 1 | 32.8K |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `all_in_one/mochi_preview_fp8_scaled.safetensors` | FP16 | `(384)` | 84 | 32.3K |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `split_files/vae/mochi_vae.safetensors` | FP16 | `(384)` | 84 | 32.3K |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `all_in_one/mochi_preview_fp8_scaled.safetensors` | FP16 | `(256)` | 55 | 14.1K |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `split_files/vae/mochi_vae.safetensors` | FP16 | `(256)` | 55 | 14.1K |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `all_in_one/mochi_preview_fp8_scaled.safetensors` | FP16 | `(512)` | 25 | 12.8K |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `split_files/vae/mochi_vae.safetensors` | FP16 | `(512)` | 25 | 12.8K |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `all_in_one/mochi_preview_fp8_scaled.safetensors` | FP16 | `(24, 384)` | 1 | 9.2K |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `split_files/vae/mochi_vae.safetensors` | FP16 | `(24, 384)` | 1 | 9.2K |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `all_in_one/mochi_preview_fp8_scaled.safetensors` | FP16 | `(768, 12, 1, 1, 1)` | 1 | 9.2K |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `split_files/vae/mochi_vae.safetensors` | FP16 | `(768, 12, 1, 1, 1)` | 1 | 9.2K |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `all_in_one/mochi_preview_fp8_scaled.safetensors` | FP16 | `(6144)` | 1 | 6.1K |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `split_files/vae/mochi_vae.safetensors` | FP16 | `(6144)` | 1 | 6.1K |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `all_in_one/mochi_preview_fp8_scaled.safetensors` | FP16 | `(128)` | 46 | 5.9K |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `split_files/vae/mochi_vae.safetensors` | FP16 | `(128)` | 46 | 5.9K |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `all_in_one/mochi_preview_fp8_scaled.safetensors` | FP16 | `(2048)` | 1 | 2.0K |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `split_files/vae/mochi_vae.safetensors` | FP16 | `(2048)` | 1 | 2.0K |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `all_in_one/mochi_preview_fp8_scaled.safetensors` | FP16 | `(32, 64)` | 1 | 2.0K |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `split_files/text_encoders/t5xxl_fp16.safetensors` | FP16 | `(32, 64)` | 1 | 2.0K |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `all_in_one/mochi_preview_fp8_scaled.safetensors` | FP16 | `(64)` | 19 | 1.2K |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `split_files/vae/mochi_vae.safetensors` | FP16 | `(64)` | 19 | 1.2K |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `all_in_one/mochi_preview_fp8_scaled.safetensors` | FP16 | `(64, 15)` | 1 | 960 |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `split_files/vae/mochi_vae.safetensors` | FP16 | `(64, 15)` | 1 | 960 |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `all_in_one/mochi_preview_fp8_scaled.safetensors` | FP16 | `(3, 128)` | 1 | 384 |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `split_files/vae/mochi_vae.safetensors` | FP16 | `(3, 128)` | 1 | 384 |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `all_in_one/mochi_preview_fp8_scaled.safetensors` | FP16 | `(3)` | 1 | 3 |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `split_files/vae/mochi_vae.safetensors` | FP16 | `(3)` | 1 | 3 |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `all_in_one/mochi_preview_fp8_scaled.safetensors` | FP32 | `()` | 1139 | 1.1K |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `all_in_one/mochi_preview_fp8_scaled.safetensors` | FP8 (E4M3FN) | `(16384, 3072)` | 48 | 2.42B |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `all_in_one/mochi_preview_fp8_scaled.safetensors` | FP8 (E4M3FN) | `(10240, 4096)` | 48 | 2.01B |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `all_in_one/mochi_preview_fp8_scaled.safetensors` | FP8 (E4M3FN) | `(12288, 3072)` | 48 | 1.81B |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `all_in_one/mochi_preview_fp8_scaled.safetensors` | FP8 (E4M3FN) | `(4096, 4096)` | 97 | 1.63B |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `all_in_one/mochi_preview_fp8_scaled.safetensors` | FP8 (E4M3FN) | `(9216, 3072)` | 48 | 1.36B |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `all_in_one/mochi_preview_fp8_scaled.safetensors` | FP8 (E4M3FN) | `(3072, 8192)` | 48 | 1.21B |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `all_in_one/mochi_preview_fp8_scaled.safetensors` | FP8 (E4M3FN) | `(4096, 10240)` | 24 | 1.01B |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `all_in_one/mochi_preview_fp8_scaled.safetensors` | FP8 (E4M3FN) | `(6144, 3072)` | 48 | 906.0M |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `all_in_one/mochi_preview_fp8_scaled.safetensors` | FP8 (E4M3FN) | `(9216, 1536)` | 48 | 679.5M |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `all_in_one/mochi_preview_fp8_scaled.safetensors` | FP8 (E4M3FN) | `(8192, 1536)` | 47 | 591.4M |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `all_in_one/mochi_preview_fp8_scaled.safetensors` | FP8 (E4M3FN) | `(3072, 3072)` | 49 | 462.4M |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `all_in_one/mochi_preview_fp8_scaled.safetensors` | FP8 (E4M3FN) | `(1536, 4096)` | 48 | 302.0M |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `all_in_one/mochi_preview_fp8_scaled.safetensors` | FP8 (E4M3FN) | `(1536, 3072)` | 48 | 226.5M |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `all_in_one/mochi_preview_fp8_scaled.safetensors` | FP8 (E4M3FN) | `(8192, 4096)` | 1 | 33.6M |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `all_in_one/mochi_preview_fp8_scaled.safetensors` | FP8 (E4M3FN) | `(3072, 4096)` | 1 | 12.6M |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `all_in_one/mochi_preview_fp8_scaled.safetensors` | FP8 (E4M3FN) | `(3072, 256)` | 1 | 786.4K |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `all_in_one/mochi_preview_fp8_scaled.safetensors` | FP8 (E4M3FN) | `(12288)` | 48 | 589.8K |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `all_in_one/mochi_preview_fp8_scaled.safetensors` | FP8 (E4M3FN) | `(6144)` | 48 | 294.9K |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `all_in_one/mochi_preview_fp8_scaled.safetensors` | FP8 (E4M3FN) | `(3072)` | 51 | 156.7K |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `all_in_one/mochi_preview_fp8_scaled.safetensors` | FP8 (E4M3FN) | `(48, 3072)` | 1 | 147.5K |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `all_in_one/mochi_preview_fp8_scaled.safetensors` | FP8 (E4M3FN) | `(1536)` | 49 | 75.3K |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `all_in_one/mochi_preview_fp8_scaled.safetensors` | FP8 (E4M3FN) | `(8192)` | 1 | 8.2K |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `all_in_one/mochi_preview_fp8_scaled.safetensors` | FP8 (E4M3FN) | `(4096)` | 1 | 4.1K |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `all_in_one/mochi_preview_fp8_scaled.safetensors` | FP8 (E4M3FN) | `(48)` | 1 | 48 |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | `all_in_one/mochi_preview_fp8_scaled.safetensors` | FP8 (E4M3FN) | `(0)` | 2 | 0 |
| [Comfy-Org/sigclip_vision_384](https://huggingface.co/Comfy-Org/sigclip_vision_384) | `sigclip_vision_patch14_384.safetensors` | FP16 | `(1152, 1152)` | 109 | 144.7M |
| [Comfy-Org/sigclip_vision_384](https://huggingface.co/Comfy-Org/sigclip_vision_384) | `sigclip_vision_patch14_384.safetensors` | FP16 | `(1152, 4304)` | 28 | 138.8M |
| [Comfy-Org/sigclip_vision_384](https://huggingface.co/Comfy-Org/sigclip_vision_384) | `sigclip_vision_patch14_384.safetensors` | FP16 | `(4304, 1152)` | 28 | 138.8M |
| [Comfy-Org/sigclip_vision_384](https://huggingface.co/Comfy-Org/sigclip_vision_384) | `sigclip_vision_patch14_384.safetensors` | FP16 | `(3456, 1152)` | 1 | 4.0M |
| [Comfy-Org/sigclip_vision_384](https://huggingface.co/Comfy-Org/sigclip_vision_384) | `sigclip_vision_patch14_384.safetensors` | FP16 | `(729, 1152)` | 1 | 839.8K |
| [Comfy-Org/sigclip_vision_384](https://huggingface.co/Comfy-Org/sigclip_vision_384) | `sigclip_vision_patch14_384.safetensors` | FP16 | `(1152, 3, 14, 14)` | 1 | 677.4K |
| [Comfy-Org/sigclip_vision_384](https://huggingface.co/Comfy-Org/sigclip_vision_384) | `sigclip_vision_patch14_384.safetensors` | FP16 | `(1152)` | 250 | 288.0K |
| [Comfy-Org/sigclip_vision_384](https://huggingface.co/Comfy-Org/sigclip_vision_384) | `sigclip_vision_patch14_384.safetensors` | FP16 | `(4304)` | 28 | 120.5K |
| [Comfy-Org/sigclip_vision_384](https://huggingface.co/Comfy-Org/sigclip_vision_384) | `sigclip_vision_patch14_384.safetensors` | FP16 | `(3456)` | 1 | 3.5K |
| [Comfy-Org/sigclip_vision_384](https://huggingface.co/Comfy-Org/sigclip_vision_384) | `sigclip_vision_patch14_384.safetensors` | FP16 | `(1, 1, 1152)` | 1 | 1.2K |
| [Comfy-Org/stable-diffusion-3.5-fp8](https://huggingface.co/Comfy-Org/stable-diffusion-3.5-fp8) | `text_encoders/t5xxl_fp16.safetensors` | FP16 | `(10240, 4096)` | 48 | 2.01B |
| [Comfy-Org/stable-diffusion-3.5-fp8](https://huggingface.co/Comfy-Org/stable-diffusion-3.5-fp8) | `text_encoders/t5xxl_fp16.safetensors` | FP16 | `(4096, 4096)` | 96 | 1.61B |
| [Comfy-Org/stable-diffusion-3.5-fp8](https://huggingface.co/Comfy-Org/stable-diffusion-3.5-fp8) | `text_encoders/t5xxl_fp16.safetensors` | FP16 | `(4096, 10240)` | 24 | 1.01B |
| [Comfy-Org/stable-diffusion-3.5-fp8](https://huggingface.co/Comfy-Org/stable-diffusion-3.5-fp8) | `text_encoders/t5xxl_fp16.safetensors` | FP16 | `(32128, 4096)` | 2 | 263.2M |
| [Comfy-Org/stable-diffusion-3.5-fp8](https://huggingface.co/Comfy-Org/stable-diffusion-3.5-fp8) | `text_encoders/clip_l.safetensors` | FP16 | `(49408, 768)` | 1 | 37.9M |
| [Comfy-Org/stable-diffusion-3.5-fp8](https://huggingface.co/Comfy-Org/stable-diffusion-3.5-fp8) | `text_encoders/clip_l.safetensors` | FP16 | `(3072, 768)` | 12 | 28.3M |
| [Comfy-Org/stable-diffusion-3.5-fp8](https://huggingface.co/Comfy-Org/stable-diffusion-3.5-fp8) | `text_encoders/clip_l.safetensors` | FP16 | `(768, 3072)` | 12 | 28.3M |
| [Comfy-Org/stable-diffusion-3.5-fp8](https://huggingface.co/Comfy-Org/stable-diffusion-3.5-fp8) | `text_encoders/clip_l.safetensors` | FP16 | `(768, 768)` | 48 | 28.3M |
| [Comfy-Org/stable-diffusion-3.5-fp8](https://huggingface.co/Comfy-Org/stable-diffusion-3.5-fp8) | `text_encoders/t5xxl_fp16.safetensors` | FP16 | `(4096)` | 49 | 200.7K |
| [Comfy-Org/stable-diffusion-3.5-fp8](https://huggingface.co/Comfy-Org/stable-diffusion-3.5-fp8) | `text_encoders/clip_l.safetensors` | FP16 | `(768)` | 110 | 84.5K |
| [Comfy-Org/stable-diffusion-3.5-fp8](https://huggingface.co/Comfy-Org/stable-diffusion-3.5-fp8) | `text_encoders/clip_l.safetensors` | FP16 | `(77, 768)` | 1 | 59.1K |
| [Comfy-Org/stable-diffusion-3.5-fp8](https://huggingface.co/Comfy-Org/stable-diffusion-3.5-fp8) | `text_encoders/clip_l.safetensors` | FP16 | `(3072)` | 12 | 36.9K |
| [Comfy-Org/stable-diffusion-3.5-fp8](https://huggingface.co/Comfy-Org/stable-diffusion-3.5-fp8) | `text_encoders/t5xxl_fp16.safetensors` | FP16 | `(32, 64)` | 1 | 2.0K |
| [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged) | `split_files/diffusion_models/wan2.1_i2v_480p_14B_bf16.safetensors` | BF16 | `(5120, 5120)` | 402 | 10.54B |
| [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged) | `split_files/diffusion_models/wan2.1_i2v_720p_14B_bf16.safetensors` | BF16 | `(5120, 5120)` | 402 | 10.54B |
| [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged) | `split_files/diffusion_models/wan2.1_i2v_480p_14B_bf16.safetensors` | BF16 | `(13824, 5120)` | 40 | 2.83B |
| [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged) | `split_files/diffusion_models/wan2.1_i2v_720p_14B_bf16.safetensors` | BF16 | `(13824, 5120)` | 40 | 2.83B |
| [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged) | `split_files/diffusion_models/wan2.1_i2v_480p_14B_bf16.safetensors` | BF16 | `(5120, 13824)` | 40 | 2.83B |
| [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged) | `split_files/diffusion_models/wan2.1_i2v_720p_14B_bf16.safetensors` | BF16 | `(5120, 13824)` | 40 | 2.83B |
| [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged) | `split_files/diffusion_models/wan2.1_i2v_480p_14B_bf16.safetensors` | BF16 | `(30720, 5120)` | 1 | 157.3M |
| [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged) | `split_files/diffusion_models/wan2.1_i2v_720p_14B_bf16.safetensors` | BF16 | `(30720, 5120)` | 1 | 157.3M |
| [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged) | `split_files/diffusion_models/wan2.1_i2v_480p_14B_bf16.safetensors` | BF16 | `(5120, 4096)` | 1 | 21.0M |
| [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged) | `split_files/diffusion_models/wan2.1_i2v_720p_14B_bf16.safetensors` | BF16 | `(5120, 4096)` | 1 | 21.0M |
| [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged) | `split_files/diffusion_models/wan2.1_i2v_480p_14B_bf16.safetensors` | BF16 | `(5120, 1280)` | 1 | 6.6M |
| [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged) | `split_files/diffusion_models/wan2.1_i2v_720p_14B_bf16.safetensors` | BF16 | `(5120, 1280)` | 1 | 6.6M |
| [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged) | `split_files/diffusion_models/wan2.1_i2v_480p_14B_bf16.safetensors` | BF16 | `(5120)` | 728 | 3.7M |
| [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged) | `split_files/diffusion_models/wan2.1_i2v_720p_14B_bf16.safetensors` | BF16 | `(5120)` | 728 | 3.7M |
| [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged) | `split_files/diffusion_models/wan2.1_i2v_480p_14B_bf16.safetensors` | BF16 | `(1280, 1280)` | 1 | 1.6M |
| [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged) | `split_files/diffusion_models/wan2.1_i2v_720p_14B_bf16.safetensors` | BF16 | `(1280, 1280)` | 1 | 1.6M |
| [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged) | `split_files/diffusion_models/wan2.1_i2v_480p_14B_bf16.safetensors` | BF16 | `(5120, 256)` | 1 | 1.3M |
| [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged) | `split_files/diffusion_models/wan2.1_i2v_720p_14B_bf16.safetensors` | BF16 | `(5120, 256)` | 1 | 1.3M |
| [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged) | `split_files/diffusion_models/wan2.1_i2v_480p_14B_bf16.safetensors` | BF16 | `(1, 6, 5120)` | 40 | 1.2M |
| [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged) | `split_files/diffusion_models/wan2.1_i2v_720p_14B_bf16.safetensors` | BF16 | `(1, 6, 5120)` | 40 | 1.2M |
| [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged) | `split_files/diffusion_models/wan2.1_i2v_480p_14B_bf16.safetensors` | BF16 | `(5120, 36, 1, 2, 2)` | 1 | 737.3K |
| [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged) | `split_files/diffusion_models/wan2.1_i2v_720p_14B_bf16.safetensors` | BF16 | `(5120, 36, 1, 2, 2)` | 1 | 737.3K |
| [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged) | `split_files/diffusion_models/wan2.1_i2v_480p_14B_bf16.safetensors` | BF16 | `(13824)` | 40 | 553.0K |
| [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged) | `split_files/diffusion_models/wan2.1_i2v_720p_14B_bf16.safetensors` | BF16 | `(13824)` | 40 | 553.0K |
| [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged) | `split_files/diffusion_models/wan2.1_i2v_480p_14B_bf16.safetensors` | BF16 | `(64, 5120)` | 1 | 327.7K |
| [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged) | `split_files/diffusion_models/wan2.1_i2v_720p_14B_bf16.safetensors` | BF16 | `(64, 5120)` | 1 | 327.7K |
| [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged) | `split_files/diffusion_models/wan2.1_i2v_480p_14B_bf16.safetensors` | BF16 | `(30720)` | 1 | 30.7K |
| [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged) | `split_files/diffusion_models/wan2.1_i2v_720p_14B_bf16.safetensors` | BF16 | `(30720)` | 1 | 30.7K |
| [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged) | `split_files/diffusion_models/wan2.1_i2v_480p_14B_bf16.safetensors` | BF16 | `(1, 2, 5120)` | 1 | 10.2K |
| [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged) | `split_files/diffusion_models/wan2.1_i2v_720p_14B_bf16.safetensors` | BF16 | `(1, 2, 5120)` | 1 | 10.2K |
| [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged) | `split_files/diffusion_models/wan2.1_i2v_480p_14B_bf16.safetensors` | BF16 | `(1280)` | 3 | 3.8K |
| [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged) | `split_files/diffusion_models/wan2.1_i2v_720p_14B_bf16.safetensors` | BF16 | `(1280)` | 3 | 3.8K |
| [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged) | `split_files/diffusion_models/wan2.1_i2v_480p_14B_bf16.safetensors` | BF16 | `(64)` | 1 | 64 |
| [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged) | `split_files/diffusion_models/wan2.1_i2v_720p_14B_bf16.safetensors` | BF16 | `(64)` | 1 | 64 |
| [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged) | `split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors` | FP16 | `(256384, 4096)` | 1 | 1.05B |
| [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged) | `split_files/clip_vision/clip_vision_h.safetensors` | FP16 | `(1280, 1280)` | 128 | 209.7M |
| [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged) | `split_files/clip_vision/clip_vision_h.safetensors` | FP16 | `(1280, 5120)` | 32 | 209.7M |
| [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged) | `split_files/clip_vision/clip_vision_h.safetensors` | FP16 | `(5120, 1280)` | 32 | 209.7M |
| [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged) | `split_files/clip_vision/clip_vision_h.safetensors` | FP16 | `(1024, 1280)` | 1 | 1.3M |
| [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged) | `split_files/clip_vision/clip_vision_h.safetensors` | FP16 | `(1280, 3, 14, 14)` | 1 | 752.6K |
| [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged) | `split_files/clip_vision/clip_vision_h.safetensors` | FP16 | `(1280)` | 293 | 375.0K |
| [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged) | `split_files/clip_vision/clip_vision_h.safetensors` | FP16 | `(257, 1280)` | 1 | 329.0K |
| [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged) | `split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors` | FP16 | `(4096)` | 49 | 200.7K |
| [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged) | `split_files/clip_vision/clip_vision_h.safetensors` | FP16 | `(5120)` | 32 | 163.8K |
| [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged) | `split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors` | FP16 | `(32, 64)` | 24 | 49.2K |
| [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged) | `split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors` | FP32 | `()` | 168 | 168 |
| [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged) | `split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors` | FP8 (E4M3FN) | `(10240, 4096)` | 48 | 2.01B |
| [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged) | `split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors` | FP8 (E4M3FN) | `(4096, 4096)` | 96 | 1.61B |
| [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged) | `split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors` | FP8 (E4M3FN) | `(4096, 10240)` | 24 | 1.01B |
| [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged) | `split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors` | FP8 (E4M3FN) | `(0)` | 1 | 0 |
| [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged) | `split_files/clip_vision/clip_vision_h.safetensors` | INT64 | `(1, 257)` | 1 | 257 |
| [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged) | `split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors` | UINT8 | `(4548313)` | 1 | 4.5M |
| [comfyanonymous/flux_text_encoders](https://huggingface.co/comfyanonymous/flux_text_encoders) | `t5xxl_fp16.safetensors` | FP16 | `(10240, 4096)` | 48 | 2.01B |
| [comfyanonymous/flux_text_encoders](https://huggingface.co/comfyanonymous/flux_text_encoders) | `t5xxl_fp16.safetensors` | FP16 | `(4096, 4096)` | 96 | 1.61B |
| [comfyanonymous/flux_text_encoders](https://huggingface.co/comfyanonymous/flux_text_encoders) | `t5xxl_fp16.safetensors` | FP16 | `(4096, 10240)` | 24 | 1.01B |
| [comfyanonymous/flux_text_encoders](https://huggingface.co/comfyanonymous/flux_text_encoders) | `t5xxl_fp16.safetensors` | FP16 | `(32128, 4096)` | 2 | 263.2M |
| [comfyanonymous/flux_text_encoders](https://huggingface.co/comfyanonymous/flux_text_encoders) | `clip_l.safetensors` | FP16 | `(49408, 768)` | 1 | 37.9M |
| [comfyanonymous/flux_text_encoders](https://huggingface.co/comfyanonymous/flux_text_encoders) | `clip_l.safetensors` | FP16 | `(3072, 768)` | 12 | 28.3M |
| [comfyanonymous/flux_text_encoders](https://huggingface.co/comfyanonymous/flux_text_encoders) | `clip_l.safetensors` | FP16 | `(768, 3072)` | 12 | 28.3M |
| [comfyanonymous/flux_text_encoders](https://huggingface.co/comfyanonymous/flux_text_encoders) | `clip_l.safetensors` | FP16 | `(768, 768)` | 48 | 28.3M |
| [comfyanonymous/flux_text_encoders](https://huggingface.co/comfyanonymous/flux_text_encoders) | `t5xxl_fp16.safetensors` | FP16 | `(4096)` | 49 | 200.7K |
| [comfyanonymous/flux_text_encoders](https://huggingface.co/comfyanonymous/flux_text_encoders) | `clip_l.safetensors` | FP16 | `(768)` | 110 | 84.5K |
| [comfyanonymous/flux_text_encoders](https://huggingface.co/comfyanonymous/flux_text_encoders) | `clip_l.safetensors` | FP16 | `(77, 768)` | 1 | 59.1K |
| [comfyanonymous/flux_text_encoders](https://huggingface.co/comfyanonymous/flux_text_encoders) | `clip_l.safetensors` | FP16 | `(3072)` | 12 | 36.9K |
| [comfyanonymous/flux_text_encoders](https://huggingface.co/comfyanonymous/flux_text_encoders) | `t5xxl_fp16.safetensors` | FP16 | `(32, 64)` | 1 | 2.0K |
| [comfyanonymous/flux_text_encoders](https://huggingface.co/comfyanonymous/flux_text_encoders) | `t5xxl_fp8_e4m3fn.safetensors` | FP8 (E4M3FN) | `(10240, 4096)` | 48 | 2.01B |
| [comfyanonymous/flux_text_encoders](https://huggingface.co/comfyanonymous/flux_text_encoders) | `t5xxl_fp8_e4m3fn.safetensors` | FP8 (E4M3FN) | `(4096, 4096)` | 96 | 1.61B |
| [comfyanonymous/flux_text_encoders](https://huggingface.co/comfyanonymous/flux_text_encoders) | `t5xxl_fp8_e4m3fn.safetensors` | FP8 (E4M3FN) | `(4096, 10240)` | 24 | 1.01B |
| [comfyanonymous/flux_text_encoders](https://huggingface.co/comfyanonymous/flux_text_encoders) | `t5xxl_fp8_e4m3fn.safetensors` | FP8 (E4M3FN) | `(32128, 4096)` | 2 | 263.2M |
| [comfyanonymous/flux_text_encoders](https://huggingface.co/comfyanonymous/flux_text_encoders) | `t5xxl_fp8_e4m3fn.safetensors` | FP8 (E4M3FN) | `(4096)` | 49 | 200.7K |
| [comfyanonymous/flux_text_encoders](https://huggingface.co/comfyanonymous/flux_text_encoders) | `t5xxl_fp8_e4m3fn.safetensors` | FP8 (E4M3FN) | `(32, 64)` | 1 | 2.0K |
| [drbaph/FLUX.1-schnell-dev-merged-fp8-4step](https://huggingface.co/drbaph/FLUX.1-schnell-dev-merged-fp8-4step) | `FLUX.1-schnell-dev-merged-fp8-4step.safetensors` | BF16 | `(512, 512, 3, 3)` | 30 | 70.8M |
| [drbaph/FLUX.1-schnell-dev-merged-fp8-4step](https://huggingface.co/drbaph/FLUX.1-schnell-dev-merged-fp8-4step) | `FLUX.1-schnell-dev-merged-fp8-4step.safetensors` | BF16 | `(256, 256, 3, 3)` | 10 | 5.9M |
| [drbaph/FLUX.1-schnell-dev-merged-fp8-4step](https://huggingface.co/drbaph/FLUX.1-schnell-dev-merged-fp8-4step) | `FLUX.1-schnell-dev-merged-fp8-4step.safetensors` | BF16 | `(512, 512, 1, 1)` | 8 | 2.1M |
| [drbaph/FLUX.1-schnell-dev-merged-fp8-4step](https://huggingface.co/drbaph/FLUX.1-schnell-dev-merged-fp8-4step) | `FLUX.1-schnell-dev-merged-fp8-4step.safetensors` | BF16 | `(128, 128, 3, 3)` | 10 | 1.5M |
| [drbaph/FLUX.1-schnell-dev-merged-fp8-4step](https://huggingface.co/drbaph/FLUX.1-schnell-dev-merged-fp8-4step) | `FLUX.1-schnell-dev-merged-fp8-4step.safetensors` | BF16 | `(256, 512, 3, 3)` | 1 | 1.2M |
| [drbaph/FLUX.1-schnell-dev-merged-fp8-4step](https://huggingface.co/drbaph/FLUX.1-schnell-dev-merged-fp8-4step) | `FLUX.1-schnell-dev-merged-fp8-4step.safetensors` | BF16 | `(512, 256, 3, 3)` | 1 | 1.2M |
| [drbaph/FLUX.1-schnell-dev-merged-fp8-4step](https://huggingface.co/drbaph/FLUX.1-schnell-dev-merged-fp8-4step) | `FLUX.1-schnell-dev-merged-fp8-4step.safetensors` | BF16 | `(128, 256, 3, 3)` | 1 | 294.9K |
| [drbaph/FLUX.1-schnell-dev-merged-fp8-4step](https://huggingface.co/drbaph/FLUX.1-schnell-dev-merged-fp8-4step) | `FLUX.1-schnell-dev-merged-fp8-4step.safetensors` | BF16 | `(256, 128, 3, 3)` | 1 | 294.9K |
| [drbaph/FLUX.1-schnell-dev-merged-fp8-4step](https://huggingface.co/drbaph/FLUX.1-schnell-dev-merged-fp8-4step) | `FLUX.1-schnell-dev-merged-fp8-4step.safetensors` | BF16 | `(32, 512, 3, 3)` | 1 | 147.5K |
| [drbaph/FLUX.1-schnell-dev-merged-fp8-4step](https://huggingface.co/drbaph/FLUX.1-schnell-dev-merged-fp8-4step) | `FLUX.1-schnell-dev-merged-fp8-4step.safetensors` | BF16 | `(256, 512, 1, 1)` | 1 | 131.1K |
| [drbaph/FLUX.1-schnell-dev-merged-fp8-4step](https://huggingface.co/drbaph/FLUX.1-schnell-dev-merged-fp8-4step) | `FLUX.1-schnell-dev-merged-fp8-4step.safetensors` | BF16 | `(512, 256, 1, 1)` | 1 | 131.1K |
| [drbaph/FLUX.1-schnell-dev-merged-fp8-4step](https://huggingface.co/drbaph/FLUX.1-schnell-dev-merged-fp8-4step) | `FLUX.1-schnell-dev-merged-fp8-4step.safetensors` | BF16 | `(512, 16, 3, 3)` | 1 | 73.7K |
| [drbaph/FLUX.1-schnell-dev-merged-fp8-4step](https://huggingface.co/drbaph/FLUX.1-schnell-dev-merged-fp8-4step) | `FLUX.1-schnell-dev-merged-fp8-4step.safetensors` | BF16 | `(512)` | 103 | 52.7K |
| [drbaph/FLUX.1-schnell-dev-merged-fp8-4step](https://huggingface.co/drbaph/FLUX.1-schnell-dev-merged-fp8-4step) | `FLUX.1-schnell-dev-merged-fp8-4step.safetensors` | BF16 | `(128, 256, 1, 1)` | 1 | 32.8K |
| [drbaph/FLUX.1-schnell-dev-merged-fp8-4step](https://huggingface.co/drbaph/FLUX.1-schnell-dev-merged-fp8-4step) | `FLUX.1-schnell-dev-merged-fp8-4step.safetensors` | BF16 | `(256, 128, 1, 1)` | 1 | 32.8K |
| [drbaph/FLUX.1-schnell-dev-merged-fp8-4step](https://huggingface.co/drbaph/FLUX.1-schnell-dev-merged-fp8-4step) | `FLUX.1-schnell-dev-merged-fp8-4step.safetensors` | BF16 | `(256)` | 34 | 8.7K |
| [drbaph/FLUX.1-schnell-dev-merged-fp8-4step](https://huggingface.co/drbaph/FLUX.1-schnell-dev-merged-fp8-4step) | `FLUX.1-schnell-dev-merged-fp8-4step.safetensors` | BF16 | `(128)` | 35 | 4.5K |
| [drbaph/FLUX.1-schnell-dev-merged-fp8-4step](https://huggingface.co/drbaph/FLUX.1-schnell-dev-merged-fp8-4step) | `FLUX.1-schnell-dev-merged-fp8-4step.safetensors` | BF16 | `(128, 3, 3, 3)` | 1 | 3.5K |
| [drbaph/FLUX.1-schnell-dev-merged-fp8-4step](https://huggingface.co/drbaph/FLUX.1-schnell-dev-merged-fp8-4step) | `FLUX.1-schnell-dev-merged-fp8-4step.safetensors` | BF16 | `(3, 128, 3, 3)` | 1 | 3.5K |
| [drbaph/FLUX.1-schnell-dev-merged-fp8-4step](https://huggingface.co/drbaph/FLUX.1-schnell-dev-merged-fp8-4step) | `FLUX.1-schnell-dev-merged-fp8-4step.safetensors` | BF16 | `(32)` | 1 | 32 |
| [drbaph/FLUX.1-schnell-dev-merged-fp8-4step](https://huggingface.co/drbaph/FLUX.1-schnell-dev-merged-fp8-4step) | `FLUX.1-schnell-dev-merged-fp8-4step.safetensors` | BF16 | `(3)` | 1 | 3 |
| [drbaph/FLUX.1-schnell-dev-merged-fp8-4step](https://huggingface.co/drbaph/FLUX.1-schnell-dev-merged-fp8-4step) | `FLUX.1-schnell-dev-merged-fp8-4step.safetensors` | FP16 | `(10240, 4096)` | 48 | 2.01B |
| [drbaph/FLUX.1-schnell-dev-merged-fp8-4step](https://huggingface.co/drbaph/FLUX.1-schnell-dev-merged-fp8-4step) | `FLUX.1-schnell-dev-merged-fp8-4step.safetensors` | FP16 | `(4096, 4096)` | 96 | 1.61B |
| [drbaph/FLUX.1-schnell-dev-merged-fp8-4step](https://huggingface.co/drbaph/FLUX.1-schnell-dev-merged-fp8-4step) | `FLUX.1-schnell-dev-merged-fp8-4step.safetensors` | FP16 | `(4096, 10240)` | 24 | 1.01B |
| [drbaph/FLUX.1-schnell-dev-merged-fp8-4step](https://huggingface.co/drbaph/FLUX.1-schnell-dev-merged-fp8-4step) | `FLUX.1-schnell-dev-merged-fp8-4step.safetensors` | FP16 | `(32128, 4096)` | 1 | 131.6M |
| [drbaph/FLUX.1-schnell-dev-merged-fp8-4step](https://huggingface.co/drbaph/FLUX.1-schnell-dev-merged-fp8-4step) | `FLUX.1-schnell-dev-merged-fp8-4step.safetensors` | FP16 | `(49408, 768)` | 1 | 37.9M |
| [drbaph/FLUX.1-schnell-dev-merged-fp8-4step](https://huggingface.co/drbaph/FLUX.1-schnell-dev-merged-fp8-4step) | `FLUX.1-schnell-dev-merged-fp8-4step.safetensors` | FP16 | `(768, 768)` | 49 | 28.9M |
| [drbaph/FLUX.1-schnell-dev-merged-fp8-4step](https://huggingface.co/drbaph/FLUX.1-schnell-dev-merged-fp8-4step) | `FLUX.1-schnell-dev-merged-fp8-4step.safetensors` | FP16 | `(3072, 768)` | 12 | 28.3M |
| [drbaph/FLUX.1-schnell-dev-merged-fp8-4step](https://huggingface.co/drbaph/FLUX.1-schnell-dev-merged-fp8-4step) | `FLUX.1-schnell-dev-merged-fp8-4step.safetensors` | FP16 | `(768, 3072)` | 12 | 28.3M |
| [drbaph/FLUX.1-schnell-dev-merged-fp8-4step](https://huggingface.co/drbaph/FLUX.1-schnell-dev-merged-fp8-4step) | `FLUX.1-schnell-dev-merged-fp8-4step.safetensors` | FP16 | `(4096)` | 49 | 200.7K |
| [drbaph/FLUX.1-schnell-dev-merged-fp8-4step](https://huggingface.co/drbaph/FLUX.1-schnell-dev-merged-fp8-4step) | `FLUX.1-schnell-dev-merged-fp8-4step.safetensors` | FP16 | `(768)` | 110 | 84.5K |
| [drbaph/FLUX.1-schnell-dev-merged-fp8-4step](https://huggingface.co/drbaph/FLUX.1-schnell-dev-merged-fp8-4step) | `FLUX.1-schnell-dev-merged-fp8-4step.safetensors` | FP16 | `(77, 768)` | 1 | 59.1K |
| [drbaph/FLUX.1-schnell-dev-merged-fp8-4step](https://huggingface.co/drbaph/FLUX.1-schnell-dev-merged-fp8-4step) | `FLUX.1-schnell-dev-merged-fp8-4step.safetensors` | FP16 | `(3072)` | 12 | 36.9K |
| [drbaph/FLUX.1-schnell-dev-merged-fp8-4step](https://huggingface.co/drbaph/FLUX.1-schnell-dev-merged-fp8-4step) | `FLUX.1-schnell-dev-merged-fp8-4step.safetensors` | FP16 | `(32, 64)` | 1 | 2.0K |
| [drbaph/FLUX.1-schnell-dev-merged-fp8-4step](https://huggingface.co/drbaph/FLUX.1-schnell-dev-merged-fp8-4step) | `FLUX.1-schnell-dev-merged-fp8-4step.safetensors` | FP32 | `()` | 2 | 2 |
| [drbaph/FLUX.1-schnell-dev-merged-fp8-4step](https://huggingface.co/drbaph/FLUX.1-schnell-dev-merged-fp8-4step) | `FLUX.1-schnell-dev-merged-fp8-4step.safetensors` | FP8 (E4M3FN) | `(21504, 3072)` | 38 | 2.51B |
| [drbaph/FLUX.1-schnell-dev-merged-fp8-4step](https://huggingface.co/drbaph/FLUX.1-schnell-dev-merged-fp8-4step) | `FLUX.1-schnell-dev-merged-fp8-4step.safetensors` | FP8 (E4M3FN) | `(18432, 3072)` | 38 | 2.15B |
| [drbaph/FLUX.1-schnell-dev-merged-fp8-4step](https://huggingface.co/drbaph/FLUX.1-schnell-dev-merged-fp8-4step) | `FLUX.1-schnell-dev-merged-fp8-4step.safetensors` | FP8 (E4M3FN) | `(9216, 3072)` | 76 | 2.15B |
| [drbaph/FLUX.1-schnell-dev-merged-fp8-4step](https://huggingface.co/drbaph/FLUX.1-schnell-dev-merged-fp8-4step) | `FLUX.1-schnell-dev-merged-fp8-4step.safetensors` | FP8 (E4M3FN) | `(3072, 15360)` | 38 | 1.79B |
| [drbaph/FLUX.1-schnell-dev-merged-fp8-4step](https://huggingface.co/drbaph/FLUX.1-schnell-dev-merged-fp8-4step) | `FLUX.1-schnell-dev-merged-fp8-4step.safetensors` | FP8 (E4M3FN) | `(12288, 3072)` | 38 | 1.43B |
| [drbaph/FLUX.1-schnell-dev-merged-fp8-4step](https://huggingface.co/drbaph/FLUX.1-schnell-dev-merged-fp8-4step) | `FLUX.1-schnell-dev-merged-fp8-4step.safetensors` | FP8 (E4M3FN) | `(3072, 12288)` | 38 | 1.43B |
| [drbaph/FLUX.1-schnell-dev-merged-fp8-4step](https://huggingface.co/drbaph/FLUX.1-schnell-dev-merged-fp8-4step) | `FLUX.1-schnell-dev-merged-fp8-4step.safetensors` | FP8 (E4M3FN) | `(3072, 3072)` | 40 | 377.5M |
| [drbaph/FLUX.1-schnell-dev-merged-fp8-4step](https://huggingface.co/drbaph/FLUX.1-schnell-dev-merged-fp8-4step) | `FLUX.1-schnell-dev-merged-fp8-4step.safetensors` | FP8 (E4M3FN) | `(6144, 3072)` | 1 | 18.9M |
| [drbaph/FLUX.1-schnell-dev-merged-fp8-4step](https://huggingface.co/drbaph/FLUX.1-schnell-dev-merged-fp8-4step) | `FLUX.1-schnell-dev-merged-fp8-4step.safetensors` | FP8 (E4M3FN) | `(3072, 4096)` | 1 | 12.6M |
| [drbaph/FLUX.1-schnell-dev-merged-fp8-4step](https://huggingface.co/drbaph/FLUX.1-schnell-dev-merged-fp8-4step) | `FLUX.1-schnell-dev-merged-fp8-4step.safetensors` | FP8 (E4M3FN) | `(3072, 768)` | 1 | 2.4M |
| [drbaph/FLUX.1-schnell-dev-merged-fp8-4step](https://huggingface.co/drbaph/FLUX.1-schnell-dev-merged-fp8-4step) | `FLUX.1-schnell-dev-merged-fp8-4step.safetensors` | FP8 (E4M3FN) | `(21504)` | 38 | 817.2K |
| [drbaph/FLUX.1-schnell-dev-merged-fp8-4step](https://huggingface.co/drbaph/FLUX.1-schnell-dev-merged-fp8-4step) | `FLUX.1-schnell-dev-merged-fp8-4step.safetensors` | FP8 (E4M3FN) | `(3072, 256)` | 1 | 786.4K |
| [drbaph/FLUX.1-schnell-dev-merged-fp8-4step](https://huggingface.co/drbaph/FLUX.1-schnell-dev-merged-fp8-4step) | `FLUX.1-schnell-dev-merged-fp8-4step.safetensors` | FP8 (E4M3FN) | `(18432)` | 38 | 700.4K |
| [drbaph/FLUX.1-schnell-dev-merged-fp8-4step](https://huggingface.co/drbaph/FLUX.1-schnell-dev-merged-fp8-4step) | `FLUX.1-schnell-dev-merged-fp8-4step.safetensors` | FP8 (E4M3FN) | `(9216)` | 76 | 700.4K |
| [drbaph/FLUX.1-schnell-dev-merged-fp8-4step](https://huggingface.co/drbaph/FLUX.1-schnell-dev-merged-fp8-4step) | `FLUX.1-schnell-dev-merged-fp8-4step.safetensors` | FP8 (E4M3FN) | `(12288)` | 38 | 466.9K |
| [drbaph/FLUX.1-schnell-dev-merged-fp8-4step](https://huggingface.co/drbaph/FLUX.1-schnell-dev-merged-fp8-4step) | `FLUX.1-schnell-dev-merged-fp8-4step.safetensors` | FP8 (E4M3FN) | `(3072)` | 120 | 368.6K |
| [drbaph/FLUX.1-schnell-dev-merged-fp8-4step](https://huggingface.co/drbaph/FLUX.1-schnell-dev-merged-fp8-4step) | `FLUX.1-schnell-dev-merged-fp8-4step.safetensors` | FP8 (E4M3FN) | `(3072, 64)` | 1 | 196.6K |
| [drbaph/FLUX.1-schnell-dev-merged-fp8-4step](https://huggingface.co/drbaph/FLUX.1-schnell-dev-merged-fp8-4step) | `FLUX.1-schnell-dev-merged-fp8-4step.safetensors` | FP8 (E4M3FN) | `(64, 3072)` | 1 | 196.6K |
| [drbaph/FLUX.1-schnell-dev-merged-fp8-4step](https://huggingface.co/drbaph/FLUX.1-schnell-dev-merged-fp8-4step) | `FLUX.1-schnell-dev-merged-fp8-4step.safetensors` | FP8 (E4M3FN) | `(128)` | 152 | 19.5K |
| [drbaph/FLUX.1-schnell-dev-merged-fp8-4step](https://huggingface.co/drbaph/FLUX.1-schnell-dev-merged-fp8-4step) | `FLUX.1-schnell-dev-merged-fp8-4step.safetensors` | FP8 (E4M3FN) | `(6144)` | 1 | 6.1K |
| [drbaph/FLUX.1-schnell-dev-merged-fp8-4step](https://huggingface.co/drbaph/FLUX.1-schnell-dev-merged-fp8-4step) | `FLUX.1-schnell-dev-merged-fp8-4step.safetensors` | FP8 (E4M3FN) | `(64)` | 1 | 64 |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | `stable-diffusion-v1-5/unet/diffusion_pytorch_model.safetensors` | FP32 | `(1280, 1280, 3, 3)` | 20 | 294.9M |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | `stable-diffusion-v1-5/unet/diffusion_pytorch_model.safetensors` | FP32 | `(1280, 2560, 3, 3)` | 5 | 147.5M |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | `stable-diffusion-v1-5/unet/diffusion_pytorch_model.safetensors` | FP32 | `(1280, 1280)` | 49 | 80.3M |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | `stable-diffusion-v1-5/unet/diffusion_pytorch_model.safetensors` | FP32 | `(10240, 1280)` | 6 | 78.6M |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | `sd-vae-ft-mse/diffusion_pytorch_model.safetensors` | FP32 | `(512, 512, 3, 3)` | 30 | 70.8M |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | `stable-diffusion-v1-5/unet/diffusion_pytorch_model.safetensors` | FP32 | `(1280, 5120)` | 6 | 39.3M |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | `stable-diffusion-v1-5/unet/diffusion_pytorch_model.safetensors` | FP32 | `(640, 640, 3, 3)` | 8 | 29.5M |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | `wav2vec/wav2vec2-base-960h/model.safetensors` | FP32 | `(3072, 768)` | 12 | 28.3M |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | `wav2vec/wav2vec2-base-960h/model.safetensors` | FP32 | `(768, 3072)` | 12 | 28.3M |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | `wav2vec/wav2vec2-base-960h/model.safetensors` | FP32 | `(768, 768)` | 48 | 28.3M |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | `stable-diffusion-v1-5/unet/diffusion_pytorch_model.safetensors` | FP32 | `(1280, 1920, 3, 3)` | 1 | 22.1M |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | `stable-diffusion-v1-5/unet/diffusion_pytorch_model.safetensors` | FP32 | `(1280, 1280, 1, 1)` | 12 | 19.7M |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | `stable-diffusion-v1-5/unet/diffusion_pytorch_model.safetensors` | FP32 | `(1280, 2560, 1, 1)` | 5 | 16.4M |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | `stable-diffusion-v1-5/unet/diffusion_pytorch_model.safetensors` | FP32 | `(5120, 640)` | 5 | 16.4M |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | `stable-diffusion-v1-5/unet/diffusion_pytorch_model.safetensors` | FP32 | `(640, 640)` | 30 | 12.3M |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | `stable-diffusion-v1-5/unet/diffusion_pytorch_model.safetensors` | FP32 | `(1280, 768)` | 12 | 11.8M |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | `stable-diffusion-v1-5/unet/diffusion_pytorch_model.safetensors` | FP32 | `(640, 1920, 3, 3)` | 1 | 11.1M |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | `stable-diffusion-v1-5/unet/diffusion_pytorch_model.safetensors` | FP32 | `(640, 2560)` | 5 | 8.2M |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | `stable-diffusion-v1-5/unet/diffusion_pytorch_model.safetensors` | FP32 | `(1280, 640, 3, 3)` | 1 | 7.4M |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | `stable-diffusion-v1-5/unet/diffusion_pytorch_model.safetensors` | FP32 | `(320, 320, 3, 3)` | 8 | 7.4M |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | `stable-diffusion-v1-5/unet/diffusion_pytorch_model.safetensors` | FP32 | `(640, 1280, 3, 3)` | 1 | 7.4M |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | `sd-vae-ft-mse/diffusion_pytorch_model.safetensors` | FP32 | `(256, 256, 3, 3)` | 10 | 5.9M |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | `stable-diffusion-v1-5/unet/diffusion_pytorch_model.safetensors` | FP32 | `(640, 960, 3, 3)` | 1 | 5.5M |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | `stable-diffusion-v1-5/unet/diffusion_pytorch_model.safetensors` | FP32 | `(640, 768)` | 10 | 4.9M |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | `wav2vec/wav2vec2-base-960h/model.safetensors` | FP32 | `(768, 48, 128)` | 1 | 4.7M |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | `stable-diffusion-v1-5/unet/diffusion_pytorch_model.safetensors` | FP32 | `(2560, 320)` | 5 | 4.1M |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | `stable-diffusion-v1-5/unet/diffusion_pytorch_model.safetensors` | FP32 | `(320, 1280)` | 10 | 4.1M |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | `stable-diffusion-v1-5/unet/diffusion_pytorch_model.safetensors` | FP32 | `(640, 1280)` | 5 | 4.1M |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | `stable-diffusion-v1-5/unet/diffusion_pytorch_model.safetensors` | FP32 | `(640, 640, 1, 1)` | 10 | 4.1M |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | `stable-diffusion-v1-5/unet/diffusion_pytorch_model.safetensors` | FP32 | `(320, 640, 3, 3)` | 2 | 3.7M |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | `wav2vec/wav2vec2-base-960h/model.safetensors` | FP32 | `(512, 512, 3)` | 4 | 3.1M |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | `stable-diffusion-v1-5/unet/diffusion_pytorch_model.safetensors` | FP32 | `(320, 320)` | 30 | 3.1M |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | `stable-diffusion-v1-5/unet/diffusion_pytorch_model.safetensors` | FP32 | `(320, 960, 3, 3)` | 1 | 2.8M |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | `stable-diffusion-v1-5/unet/diffusion_pytorch_model.safetensors` | FP32 | `(1280, 1920, 1, 1)` | 1 | 2.5M |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | `stable-diffusion-v1-5/unet/diffusion_pytorch_model.safetensors` | FP32 | `(320, 768)` | 10 | 2.5M |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | `sd-vae-ft-mse/diffusion_pytorch_model.safetensors` | FP32 | `(512, 512)` | 8 | 2.1M |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | `stable-diffusion-v1-5/unet/diffusion_pytorch_model.safetensors` | FP32 | `(640, 320, 3, 3)` | 1 | 1.8M |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | `sd-vae-ft-mse/diffusion_pytorch_model.safetensors` | FP32 | `(128, 128, 3, 3)` | 10 | 1.5M |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | `stable-diffusion-v1-5/unet/diffusion_pytorch_model.safetensors` | FP32 | `(640, 1920, 1, 1)` | 1 | 1.2M |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | `sd-vae-ft-mse/diffusion_pytorch_model.safetensors` | FP32 | `(256, 512, 3, 3)` | 1 | 1.2M |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | `sd-vae-ft-mse/diffusion_pytorch_model.safetensors` | FP32 | `(512, 256, 3, 3)` | 1 | 1.2M |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | `wav2vec/wav2vec2-base-960h/model.safetensors` | FP32 | `(512, 512, 2)` | 2 | 1.0M |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | `stable-diffusion-v1-5/unet/diffusion_pytorch_model.safetensors` | FP32 | `(320, 320, 1, 1)` | 10 | 1.0M |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | `stable-diffusion-v1-5/unet/diffusion_pytorch_model.safetensors` | FP32 | `(1280, 640, 1, 1)` | 1 | 819.2K |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | `stable-diffusion-v1-5/unet/diffusion_pytorch_model.safetensors` | FP32 | `(640, 1280, 1, 1)` | 1 | 819.2K |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | `stable-diffusion-v1-5/unet/diffusion_pytorch_model.safetensors` | FP32 | `(640, 960, 1, 1)` | 1 | 614.4K |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | `stable-diffusion-v1-5/unet/diffusion_pytorch_model.safetensors` | FP32 | `(1280, 320)` | 1 | 409.6K |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | `stable-diffusion-v1-5/unet/diffusion_pytorch_model.safetensors` | FP32 | `(320, 640, 1, 1)` | 2 | 409.6K |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | `wav2vec/wav2vec2-base-960h/model.safetensors` | FP32 | `(768, 512)` | 1 | 393.2K |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | `stable-diffusion-v1-5/unet/diffusion_pytorch_model.safetensors` | FP32 | `(320, 960, 1, 1)` | 1 | 307.2K |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | `sd-vae-ft-mse/diffusion_pytorch_model.safetensors` | FP32 | `(128, 256, 3, 3)` | 1 | 294.9K |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | `sd-vae-ft-mse/diffusion_pytorch_model.safetensors` | FP32 | `(256, 128, 3, 3)` | 1 | 294.9K |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | `stable-diffusion-v1-5/unet/diffusion_pytorch_model.safetensors` | FP32 | `(1280)` | 162 | 207.4K |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | `stable-diffusion-v1-5/unet/diffusion_pytorch_model.safetensors` | FP32 | `(640, 320, 1, 1)` | 1 | 204.8K |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | `sd-vae-ft-mse/diffusion_pytorch_model.safetensors` | FP32 | `(256, 512, 1, 1)` | 1 | 131.1K |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | `sd-vae-ft-mse/diffusion_pytorch_model.safetensors` | FP32 | `(512, 256, 1, 1)` | 1 | 131.1K |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | `wav2vec/wav2vec2-base-960h/model.safetensors` | FP32 | `(768)` | 112 | 86.0K |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | `stable-diffusion-v1-5/unet/diffusion_pytorch_model.safetensors` | FP32 | `(640)` | 104 | 66.6K |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | `stable-diffusion-v1-5/unet/diffusion_pytorch_model.safetensors` | FP32 | `(10240)` | 6 | 61.4K |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | `sd-vae-ft-mse/diffusion_pytorch_model.safetensors` | FP32 | `(512)` | 103 | 52.7K |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | `stable-diffusion-v1-5/unet/diffusion_pytorch_model.safetensors` | FP32 | `(2560)` | 15 | 38.4K |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | `wav2vec/wav2vec2-base-960h/model.safetensors` | FP32 | `(3072)` | 12 | 36.9K |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | `sd-vae-ft-mse/diffusion_pytorch_model.safetensors` | FP32 | `(8, 512, 3, 3)` | 1 | 36.9K |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | `stable-diffusion-v1-5/unet/diffusion_pytorch_model.safetensors` | FP32 | `(320)` | 103 | 33.0K |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | `sd-vae-ft-mse/diffusion_pytorch_model.safetensors` | FP32 | `(128, 256, 1, 1)` | 1 | 32.8K |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | `sd-vae-ft-mse/diffusion_pytorch_model.safetensors` | FP32 | `(256, 128, 1, 1)` | 1 | 32.8K |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | `stable-diffusion-v1-5/unet/diffusion_pytorch_model.safetensors` | FP32 | `(5120)` | 5 | 25.6K |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | `wav2vec/wav2vec2-base-960h/model.safetensors` | FP32 | `(32, 768)` | 1 | 24.6K |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | `sd-vae-ft-mse/diffusion_pytorch_model.safetensors` | FP32 | `(512, 4, 3, 3)` | 1 | 18.4K |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | `stable-diffusion-v1-5/unet/diffusion_pytorch_model.safetensors` | FP32 | `(320, 4, 3, 3)` | 1 | 11.5K |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | `stable-diffusion-v1-5/unet/diffusion_pytorch_model.safetensors` | FP32 | `(4, 320, 3, 3)` | 1 | 11.5K |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | `sd-vae-ft-mse/diffusion_pytorch_model.safetensors` | FP32 | `(256)` | 34 | 8.7K |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | `stable-diffusion-v1-5/unet/diffusion_pytorch_model.safetensors` | FP32 | `(1920)` | 4 | 7.7K |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | `wav2vec/wav2vec2-base-960h/model.safetensors` | FP32 | `(512, 1, 10)` | 1 | 5.1K |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | `sd-vae-ft-mse/diffusion_pytorch_model.safetensors` | FP32 | `(128)` | 35 | 4.5K |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | `stable-diffusion-v1-5/unet/diffusion_pytorch_model.safetensors` | FP32 | `(960)` | 4 | 3.8K |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | `sd-vae-ft-mse/diffusion_pytorch_model.safetensors` | FP32 | `(128, 3, 3, 3)` | 1 | 3.5K |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | `sd-vae-ft-mse/diffusion_pytorch_model.safetensors` | FP32 | `(3, 128, 3, 3)` | 1 | 3.5K |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | `wav2vec/wav2vec2-base-960h/model.safetensors` | FP32 | `(512)` | 4 | 2.0K |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | `wav2vec/wav2vec2-base-960h/model.safetensors` | FP32 | `(1, 1, 128)` | 1 | 128 |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | `sd-vae-ft-mse/diffusion_pytorch_model.safetensors` | FP32 | `(8, 8, 1, 1)` | 1 | 64 |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | `wav2vec/wav2vec2-base-960h/model.safetensors` | FP32 | `(32)` | 1 | 32 |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | `sd-vae-ft-mse/diffusion_pytorch_model.safetensors` | FP32 | `(4, 4, 1, 1)` | 1 | 16 |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | `sd-vae-ft-mse/diffusion_pytorch_model.safetensors` | FP32 | `(8)` | 2 | 16 |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | `sd-vae-ft-mse/diffusion_pytorch_model.safetensors` | FP32 | `(4)` | 1 | 4 |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | `stable-diffusion-v1-5/unet/diffusion_pytorch_model.safetensors` | FP32 | `(4)` | 1 | 4 |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | `sd-vae-ft-mse/diffusion_pytorch_model.safetensors` | FP32 | `(3)` | 1 | 3 |
| [genmo/mochi-1-preview](https://huggingface.co/genmo/mochi-1-preview) | `dit.safetensors` | FP32 | `(16384, 3072)` | 48 | 2.42B |
| [genmo/mochi-1-preview](https://huggingface.co/genmo/mochi-1-preview) | `dit.safetensors` | FP32 | `(12288, 3072)` | 48 | 1.81B |
| [genmo/mochi-1-preview](https://huggingface.co/genmo/mochi-1-preview) | `dit.safetensors` | FP32 | `(9216, 3072)` | 48 | 1.36B |
| [genmo/mochi-1-preview](https://huggingface.co/genmo/mochi-1-preview) | `dit.safetensors` | FP32 | `(3072, 8192)` | 48 | 1.21B |
| [genmo/mochi-1-preview](https://huggingface.co/genmo/mochi-1-preview) | `dit.safetensors` | FP32 | `(6144, 3072)` | 48 | 906.0M |
| [genmo/mochi-1-preview](https://huggingface.co/genmo/mochi-1-preview) | `dit.safetensors` | FP32 | `(9216, 1536)` | 48 | 679.5M |
| [genmo/mochi-1-preview](https://huggingface.co/genmo/mochi-1-preview) | `dit.safetensors` | FP32 | `(8192, 1536)` | 47 | 591.4M |
| [genmo/mochi-1-preview](https://huggingface.co/genmo/mochi-1-preview) | `dit.safetensors` | FP32 | `(3072, 3072)` | 49 | 462.4M |
| [genmo/mochi-1-preview](https://huggingface.co/genmo/mochi-1-preview) | `dit.safetensors` | FP32 | `(1536, 4096)` | 48 | 302.0M |
| [genmo/mochi-1-preview](https://huggingface.co/genmo/mochi-1-preview) | `decoder.safetensors` | FP32 | `(768, 768, 3, 3, 3)` | 18 | 286.7M |
| [genmo/mochi-1-preview](https://huggingface.co/genmo/mochi-1-preview) | `dit.safetensors` | FP32 | `(1536, 3072)` | 48 | 226.5M |
| [genmo/mochi-1-preview](https://huggingface.co/genmo/mochi-1-preview) | `encoder.safetensors` | FP32 | `(384, 384, 3, 3, 3)` | 18 | 71.7M |
| [genmo/mochi-1-preview](https://huggingface.co/genmo/mochi-1-preview) | `decoder.safetensors` | FP32 | `(512, 512, 3, 3, 3)` | 8 | 56.6M |
| [genmo/mochi-1-preview](https://huggingface.co/genmo/mochi-1-preview) | `dit.safetensors` | FP32 | `(8192, 4096)` | 1 | 33.6M |
| [genmo/mochi-1-preview](https://huggingface.co/genmo/mochi-1-preview) | `dit.safetensors` | FP32 | `(4096, 4096)` | 1 | 16.8M |
| [genmo/mochi-1-preview](https://huggingface.co/genmo/mochi-1-preview) | `encoder.safetensors` | FP32 | `(256, 256, 3, 3, 3)` | 8 | 14.2M |
| [genmo/mochi-1-preview](https://huggingface.co/genmo/mochi-1-preview) | `dit.safetensors` | FP32 | `(3072, 4096)` | 1 | 12.6M |
| [genmo/mochi-1-preview](https://huggingface.co/genmo/mochi-1-preview) | `decoder.safetensors` | FP32 | `(256, 256, 3, 3, 3)` | 6 | 10.6M |
| [genmo/mochi-1-preview](https://huggingface.co/genmo/mochi-1-preview) | `decoder.safetensors` | FP32 | `(6144, 768)` | 1 | 4.7M |
| [genmo/mochi-1-preview](https://huggingface.co/genmo/mochi-1-preview) | `encoder.safetensors` | FP32 | `(1152, 384)` | 9 | 4.0M |
| [genmo/mochi-1-preview](https://huggingface.co/genmo/mochi-1-preview) | `decoder.safetensors` | FP32 | `(128, 128, 3, 3, 3)` | 6 | 2.7M |
| [genmo/mochi-1-preview](https://huggingface.co/genmo/mochi-1-preview) | `encoder.safetensors` | FP32 | `(128, 128, 3, 3, 3)` | 6 | 2.7M |
| [genmo/mochi-1-preview](https://huggingface.co/genmo/mochi-1-preview) | `encoder.safetensors` | FP32 | `(384, 384)` | 9 | 1.3M |
| [genmo/mochi-1-preview](https://huggingface.co/genmo/mochi-1-preview) | `encoder.safetensors` | FP32 | `(384, 256, 3, 2, 2)` | 1 | 1.2M |
| [genmo/mochi-1-preview](https://huggingface.co/genmo/mochi-1-preview) | `decoder.safetensors` | FP32 | `(2048, 512)` | 1 | 1.0M |
| [genmo/mochi-1-preview](https://huggingface.co/genmo/mochi-1-preview) | `dit.safetensors` | FP32 | `(3072, 256)` | 1 | 786.4K |
| [genmo/mochi-1-preview](https://huggingface.co/genmo/mochi-1-preview) | `encoder.safetensors` | FP32 | `(768, 256)` | 4 | 786.4K |
| [genmo/mochi-1-preview](https://huggingface.co/genmo/mochi-1-preview) | `encoder.safetensors` | FP32 | `(64, 64, 3, 3, 3)` | 6 | 663.6K |
| [genmo/mochi-1-preview](https://huggingface.co/genmo/mochi-1-preview) | `dit.safetensors` | FP32 | `(12288)` | 48 | 589.8K |
| [genmo/mochi-1-preview](https://huggingface.co/genmo/mochi-1-preview) | `dit.safetensors` | FP32 | `(6144)` | 48 | 294.9K |
| [genmo/mochi-1-preview](https://huggingface.co/genmo/mochi-1-preview) | `encoder.safetensors` | FP32 | `(256, 128, 2, 2, 2)` | 1 | 262.1K |
| [genmo/mochi-1-preview](https://huggingface.co/genmo/mochi-1-preview) | `encoder.safetensors` | FP32 | `(256, 256)` | 4 | 262.1K |
| [genmo/mochi-1-preview](https://huggingface.co/genmo/mochi-1-preview) | `dit.safetensors` | FP32 | `(3072)` | 52 | 159.7K |
| [genmo/mochi-1-preview](https://huggingface.co/genmo/mochi-1-preview) | `dit.safetensors` | FP32 | `(3072, 12, 2, 2)` | 1 | 147.5K |
| [genmo/mochi-1-preview](https://huggingface.co/genmo/mochi-1-preview) | `encoder.safetensors` | FP32 | `(384, 128)` | 3 | 147.5K |
| [genmo/mochi-1-preview](https://huggingface.co/genmo/mochi-1-preview) | `dit.safetensors` | FP32 | `(48, 3072)` | 1 | 147.5K |
| [genmo/mochi-1-preview](https://huggingface.co/genmo/mochi-1-preview) | `decoder.safetensors` | FP32 | `(512, 256)` | 1 | 131.1K |
| [genmo/mochi-1-preview](https://huggingface.co/genmo/mochi-1-preview) | `dit.safetensors` | FP32 | `(1536)` | 49 | 75.3K |
| [genmo/mochi-1-preview](https://huggingface.co/genmo/mochi-1-preview) | `encoder.safetensors` | FP32 | `(128, 128)` | 3 | 49.2K |
| [genmo/mochi-1-preview](https://huggingface.co/genmo/mochi-1-preview) | `decoder.safetensors` | FP32 | `(768)` | 55 | 42.2K |
| [genmo/mochi-1-preview](https://huggingface.co/genmo/mochi-1-preview) | `encoder.safetensors` | FP32 | `(128, 64, 1, 2, 2)` | 1 | 32.8K |
| [genmo/mochi-1-preview](https://huggingface.co/genmo/mochi-1-preview) | `encoder.safetensors` | FP32 | `(384)` | 84 | 32.3K |
| [genmo/mochi-1-preview](https://huggingface.co/genmo/mochi-1-preview) | `dit.safetensors` | FP32 | `(128)` | 192 | 24.6K |
| [genmo/mochi-1-preview](https://huggingface.co/genmo/mochi-1-preview) | `decoder.safetensors` | FP32 | `(512)` | 25 | 12.8K |
| [genmo/mochi-1-preview](https://huggingface.co/genmo/mochi-1-preview) | `encoder.safetensors` | FP32 | `(256)` | 37 | 9.5K |
| [genmo/mochi-1-preview](https://huggingface.co/genmo/mochi-1-preview) | `encoder.safetensors` | FP32 | `(24, 384)` | 1 | 9.2K |
| [genmo/mochi-1-preview](https://huggingface.co/genmo/mochi-1-preview) | `decoder.safetensors` | FP32 | `(768, 12, 1, 1, 1)` | 1 | 9.2K |
| [genmo/mochi-1-preview](https://huggingface.co/genmo/mochi-1-preview) | `dit.safetensors` | FP32 | `(8192)` | 1 | 8.2K |
| [genmo/mochi-1-preview](https://huggingface.co/genmo/mochi-1-preview) | `decoder.safetensors` | FP32 | `(6144)` | 1 | 6.1K |
| [genmo/mochi-1-preview](https://huggingface.co/genmo/mochi-1-preview) | `decoder.safetensors` | FP32 | `(256)` | 18 | 4.6K |
| [genmo/mochi-1-preview](https://huggingface.co/genmo/mochi-1-preview) | `dit.safetensors` | FP32 | `(3, 24, 64)` | 1 | 4.6K |
| [genmo/mochi-1-preview](https://huggingface.co/genmo/mochi-1-preview) | `dit.safetensors` | FP32 | `(4096)` | 1 | 4.1K |
| [genmo/mochi-1-preview](https://huggingface.co/genmo/mochi-1-preview) | `encoder.safetensors` | FP32 | `(128)` | 28 | 3.6K |
| [genmo/mochi-1-preview](https://huggingface.co/genmo/mochi-1-preview) | `decoder.safetensors` | FP32 | `(128)` | 18 | 2.3K |
| [genmo/mochi-1-preview](https://huggingface.co/genmo/mochi-1-preview) | `decoder.safetensors` | FP32 | `(2048)` | 1 | 2.0K |
| [genmo/mochi-1-preview](https://huggingface.co/genmo/mochi-1-preview) | `encoder.safetensors` | FP32 | `(64)` | 19 | 1.2K |
| [genmo/mochi-1-preview](https://huggingface.co/genmo/mochi-1-preview) | `encoder.safetensors` | FP32 | `(64, 15)` | 1 | 960 |
| [genmo/mochi-1-preview](https://huggingface.co/genmo/mochi-1-preview) | `decoder.safetensors` | FP32 | `(3, 128)` | 1 | 384 |
| [genmo/mochi-1-preview](https://huggingface.co/genmo/mochi-1-preview) | `dit.safetensors` | FP32 | `(48)` | 1 | 48 |
| [genmo/mochi-1-preview](https://huggingface.co/genmo/mochi-1-preview) | `decoder.safetensors` | FP32 | `(3)` | 1 | 3 |
| [hunyuanvideo-community/HunyuanVideo](https://huggingface.co/hunyuanvideo-community/HunyuanVideo) | `text_encoder/model-00002-of-00004.safetensors` | FP16 | `(14336, 4096)` | 23 | 1.35B |
| [hunyuanvideo-community/HunyuanVideo](https://huggingface.co/hunyuanvideo-community/HunyuanVideo) | `text_encoder/model-00003-of-00004.safetensors` | FP16 | `(14336, 4096)` | 23 | 1.35B |
| [hunyuanvideo-community/HunyuanVideo](https://huggingface.co/hunyuanvideo-community/HunyuanVideo) | `text_encoder/model-00001-of-00004.safetensors` | FP16 | `(14336, 4096)` | 18 | 1.06B |
| [hunyuanvideo-community/HunyuanVideo](https://huggingface.co/hunyuanvideo-community/HunyuanVideo) | `text_encoder/model-00002-of-00004.safetensors` | FP16 | `(4096, 14336)` | 11 | 645.9M |
| [hunyuanvideo-community/HunyuanVideo](https://huggingface.co/hunyuanvideo-community/HunyuanVideo) | `text_encoder/model-00003-of-00004.safetensors` | FP16 | `(4096, 14336)` | 11 | 645.9M |
| [hunyuanvideo-community/HunyuanVideo](https://huggingface.co/hunyuanvideo-community/HunyuanVideo) | `text_encoder/model-00001-of-00004.safetensors` | FP16 | `(4096, 14336)` | 9 | 528.5M |
| [hunyuanvideo-community/HunyuanVideo](https://huggingface.co/hunyuanvideo-community/HunyuanVideo) | `text_encoder/model-00001-of-00004.safetensors` | FP16 | `(128320, 4096)` | 1 | 525.6M |
| [hunyuanvideo-community/HunyuanVideo](https://huggingface.co/hunyuanvideo-community/HunyuanVideo) | `text_encoder/model-00002-of-00004.safetensors` | FP16 | `(4096, 4096)` | 24 | 402.7M |
| [hunyuanvideo-community/HunyuanVideo](https://huggingface.co/hunyuanvideo-community/HunyuanVideo) | `text_encoder/model-00003-of-00004.safetensors` | FP16 | `(4096, 4096)` | 22 | 369.1M |
| [hunyuanvideo-community/HunyuanVideo](https://huggingface.co/hunyuanvideo-community/HunyuanVideo) | `text_encoder/model-00001-of-00004.safetensors` | FP16 | `(4096, 4096)` | 18 | 302.0M |
| [hunyuanvideo-community/HunyuanVideo](https://huggingface.co/hunyuanvideo-community/HunyuanVideo) | `text_encoder/model-00002-of-00004.safetensors` | FP16 | `(1024, 4096)` | 24 | 100.7M |
| [hunyuanvideo-community/HunyuanVideo](https://huggingface.co/hunyuanvideo-community/HunyuanVideo) | `text_encoder/model-00003-of-00004.safetensors` | FP16 | `(1024, 4096)` | 22 | 92.3M |
| [hunyuanvideo-community/HunyuanVideo](https://huggingface.co/hunyuanvideo-community/HunyuanVideo) | `text_encoder/model-00001-of-00004.safetensors` | FP16 | `(1024, 4096)` | 18 | 75.5M |
| [hunyuanvideo-community/HunyuanVideo](https://huggingface.co/hunyuanvideo-community/HunyuanVideo) | `text_encoder/model-00002-of-00004.safetensors` | FP16 | `(4096)` | 22 | 90.1K |
| [hunyuanvideo-community/HunyuanVideo](https://huggingface.co/hunyuanvideo-community/HunyuanVideo) | `text_encoder/model-00003-of-00004.safetensors` | FP16 | `(4096)` | 22 | 90.1K |
| [hunyuanvideo-community/HunyuanVideo](https://huggingface.co/hunyuanvideo-community/HunyuanVideo) | `text_encoder/model-00001-of-00004.safetensors` | FP16 | `(4096)` | 18 | 73.7K |
| [KBlueLeaf/kohaku-v2.1](https://huggingface.co/KBlueLeaf/kohaku-v2.1) | `kohaku-v2.1.safetensors` | FP16 | `(1280, 1280, 3, 3)` | 20 | 294.9M |
| [KBlueLeaf/kohaku-v2.1](https://huggingface.co/KBlueLeaf/kohaku-v2.1) | `kohaku-v2.1.safetensors` | FP16 | `(1280, 2560, 3, 3)` | 5 | 147.5M |
| [KBlueLeaf/kohaku-v2.1](https://huggingface.co/KBlueLeaf/kohaku-v2.1) | `kohaku-v2.1.safetensors` | FP16 | `(1280, 1280)` | 49 | 80.3M |
| [KBlueLeaf/kohaku-v2.1](https://huggingface.co/KBlueLeaf/kohaku-v2.1) | `kohaku-v2.1.safetensors` | FP16 | `(10240, 1280)` | 6 | 78.6M |
| [KBlueLeaf/kohaku-v2.1](https://huggingface.co/KBlueLeaf/kohaku-v2.1) | `kohaku-v2.1.safetensors` | FP16 | `(512, 512, 3, 3)` | 30 | 70.8M |
| [KBlueLeaf/kohaku-v2.1](https://huggingface.co/KBlueLeaf/kohaku-v2.1) | `kohaku-v2.1.safetensors` | FP16 | `(1280, 5120)` | 6 | 39.3M |
| [KBlueLeaf/kohaku-v2.1](https://huggingface.co/KBlueLeaf/kohaku-v2.1) | `kohaku-v2.1.safetensors` | FP16 | `(49408, 768)` | 1 | 37.9M |
| [KBlueLeaf/kohaku-v2.1](https://huggingface.co/KBlueLeaf/kohaku-v2.1) | `kohaku-v2.1.safetensors` | FP16 | `(640, 640, 3, 3)` | 8 | 29.5M |
| [KBlueLeaf/kohaku-v2.1](https://huggingface.co/KBlueLeaf/kohaku-v2.1) | `kohaku-v2.1.safetensors` | FP16 | `(3072, 768)` | 12 | 28.3M |
| [KBlueLeaf/kohaku-v2.1](https://huggingface.co/KBlueLeaf/kohaku-v2.1) | `kohaku-v2.1.safetensors` | FP16 | `(768, 3072)` | 12 | 28.3M |
| [KBlueLeaf/kohaku-v2.1](https://huggingface.co/KBlueLeaf/kohaku-v2.1) | `kohaku-v2.1.safetensors` | FP16 | `(768, 768)` | 48 | 28.3M |
| [KBlueLeaf/kohaku-v2.1](https://huggingface.co/KBlueLeaf/kohaku-v2.1) | `kohaku-v2.1.safetensors` | FP16 | `(1280, 1920, 3, 3)` | 1 | 22.1M |
| [KBlueLeaf/kohaku-v2.1](https://huggingface.co/KBlueLeaf/kohaku-v2.1) | `kohaku-v2.1.safetensors` | FP16 | `(1280, 1280, 1, 1)` | 12 | 19.7M |
| [KBlueLeaf/kohaku-v2.1](https://huggingface.co/KBlueLeaf/kohaku-v2.1) | `kohaku-v2.1.safetensors` | FP16 | `(1280, 2560, 1, 1)` | 5 | 16.4M |
| [KBlueLeaf/kohaku-v2.1](https://huggingface.co/KBlueLeaf/kohaku-v2.1) | `kohaku-v2.1.safetensors` | FP16 | `(5120, 640)` | 5 | 16.4M |
| [KBlueLeaf/kohaku-v2.1](https://huggingface.co/KBlueLeaf/kohaku-v2.1) | `kohaku-v2.1.safetensors` | FP16 | `(640, 640)` | 30 | 12.3M |
| [KBlueLeaf/kohaku-v2.1](https://huggingface.co/KBlueLeaf/kohaku-v2.1) | `kohaku-v2.1.safetensors` | FP16 | `(1280, 768)` | 12 | 11.8M |
| [KBlueLeaf/kohaku-v2.1](https://huggingface.co/KBlueLeaf/kohaku-v2.1) | `kohaku-v2.1.safetensors` | FP16 | `(640, 1920, 3, 3)` | 1 | 11.1M |
| [KBlueLeaf/kohaku-v2.1](https://huggingface.co/KBlueLeaf/kohaku-v2.1) | `kohaku-v2.1.safetensors` | FP16 | `(640, 2560)` | 5 | 8.2M |
| [KBlueLeaf/kohaku-v2.1](https://huggingface.co/KBlueLeaf/kohaku-v2.1) | `kohaku-v2.1.safetensors` | FP16 | `(1280, 640, 3, 3)` | 1 | 7.4M |
| [KBlueLeaf/kohaku-v2.1](https://huggingface.co/KBlueLeaf/kohaku-v2.1) | `kohaku-v2.1.safetensors` | FP16 | `(320, 320, 3, 3)` | 8 | 7.4M |
| [KBlueLeaf/kohaku-v2.1](https://huggingface.co/KBlueLeaf/kohaku-v2.1) | `kohaku-v2.1.safetensors` | FP16 | `(640, 1280, 3, 3)` | 1 | 7.4M |
| [KBlueLeaf/kohaku-v2.1](https://huggingface.co/KBlueLeaf/kohaku-v2.1) | `kohaku-v2.1.safetensors` | FP16 | `(256, 256, 3, 3)` | 10 | 5.9M |
| [KBlueLeaf/kohaku-v2.1](https://huggingface.co/KBlueLeaf/kohaku-v2.1) | `kohaku-v2.1.safetensors` | FP16 | `(640, 960, 3, 3)` | 1 | 5.5M |
| [KBlueLeaf/kohaku-v2.1](https://huggingface.co/KBlueLeaf/kohaku-v2.1) | `kohaku-v2.1.safetensors` | FP16 | `(640, 768)` | 10 | 4.9M |
| [KBlueLeaf/kohaku-v2.1](https://huggingface.co/KBlueLeaf/kohaku-v2.1) | `kohaku-v2.1.safetensors` | FP16 | `(2560, 320)` | 5 | 4.1M |
| [KBlueLeaf/kohaku-v2.1](https://huggingface.co/KBlueLeaf/kohaku-v2.1) | `kohaku-v2.1.safetensors` | FP16 | `(320, 1280)` | 10 | 4.1M |
| [KBlueLeaf/kohaku-v2.1](https://huggingface.co/KBlueLeaf/kohaku-v2.1) | `kohaku-v2.1.safetensors` | FP16 | `(640, 1280)` | 5 | 4.1M |
| [KBlueLeaf/kohaku-v2.1](https://huggingface.co/KBlueLeaf/kohaku-v2.1) | `kohaku-v2.1.safetensors` | FP16 | `(640, 640, 1, 1)` | 10 | 4.1M |
| [KBlueLeaf/kohaku-v2.1](https://huggingface.co/KBlueLeaf/kohaku-v2.1) | `kohaku-v2.1.safetensors` | FP16 | `(320, 640, 3, 3)` | 2 | 3.7M |
| [KBlueLeaf/kohaku-v2.1](https://huggingface.co/KBlueLeaf/kohaku-v2.1) | `kohaku-v2.1.safetensors` | FP16 | `(320, 320)` | 30 | 3.1M |
| [KBlueLeaf/kohaku-v2.1](https://huggingface.co/KBlueLeaf/kohaku-v2.1) | `kohaku-v2.1.safetensors` | FP16 | `(320, 960, 3, 3)` | 1 | 2.8M |
| [KBlueLeaf/kohaku-v2.1](https://huggingface.co/KBlueLeaf/kohaku-v2.1) | `kohaku-v2.1.safetensors` | FP16 | `(1280, 1920, 1, 1)` | 1 | 2.5M |
| [KBlueLeaf/kohaku-v2.1](https://huggingface.co/KBlueLeaf/kohaku-v2.1) | `kohaku-v2.1.safetensors` | FP16 | `(320, 768)` | 10 | 2.5M |
| [KBlueLeaf/kohaku-v2.1](https://huggingface.co/KBlueLeaf/kohaku-v2.1) | `kohaku-v2.1.safetensors` | FP16 | `(512, 512, 1, 1)` | 8 | 2.1M |
| [KBlueLeaf/kohaku-v2.1](https://huggingface.co/KBlueLeaf/kohaku-v2.1) | `kohaku-v2.1.safetensors` | FP16 | `(640, 320, 3, 3)` | 1 | 1.8M |
| [KBlueLeaf/kohaku-v2.1](https://huggingface.co/KBlueLeaf/kohaku-v2.1) | `kohaku-v2.1.safetensors` | FP16 | `(128, 128, 3, 3)` | 10 | 1.5M |
| [KBlueLeaf/kohaku-v2.1](https://huggingface.co/KBlueLeaf/kohaku-v2.1) | `kohaku-v2.1.safetensors` | FP16 | `(640, 1920, 1, 1)` | 1 | 1.2M |
| [KBlueLeaf/kohaku-v2.1](https://huggingface.co/KBlueLeaf/kohaku-v2.1) | `kohaku-v2.1.safetensors` | FP16 | `(256, 512, 3, 3)` | 1 | 1.2M |
| [KBlueLeaf/kohaku-v2.1](https://huggingface.co/KBlueLeaf/kohaku-v2.1) | `kohaku-v2.1.safetensors` | FP16 | `(512, 256, 3, 3)` | 1 | 1.2M |
| [KBlueLeaf/kohaku-v2.1](https://huggingface.co/KBlueLeaf/kohaku-v2.1) | `kohaku-v2.1.safetensors` | FP16 | `(320, 320, 1, 1)` | 10 | 1.0M |
| [KBlueLeaf/kohaku-v2.1](https://huggingface.co/KBlueLeaf/kohaku-v2.1) | `kohaku-v2.1.safetensors` | FP16 | `(1280, 640, 1, 1)` | 1 | 819.2K |
| [KBlueLeaf/kohaku-v2.1](https://huggingface.co/KBlueLeaf/kohaku-v2.1) | `kohaku-v2.1.safetensors` | FP16 | `(640, 1280, 1, 1)` | 1 | 819.2K |
| [KBlueLeaf/kohaku-v2.1](https://huggingface.co/KBlueLeaf/kohaku-v2.1) | `kohaku-v2.1.safetensors` | FP16 | `(640, 960, 1, 1)` | 1 | 614.4K |
| [KBlueLeaf/kohaku-v2.1](https://huggingface.co/KBlueLeaf/kohaku-v2.1) | `kohaku-v2.1.safetensors` | FP16 | `(1280, 320)` | 1 | 409.6K |
| [KBlueLeaf/kohaku-v2.1](https://huggingface.co/KBlueLeaf/kohaku-v2.1) | `kohaku-v2.1.safetensors` | FP16 | `(320, 640, 1, 1)` | 2 | 409.6K |
| [KBlueLeaf/kohaku-v2.1](https://huggingface.co/KBlueLeaf/kohaku-v2.1) | `kohaku-v2.1.safetensors` | FP16 | `(320, 960, 1, 1)` | 1 | 307.2K |
| [KBlueLeaf/kohaku-v2.1](https://huggingface.co/KBlueLeaf/kohaku-v2.1) | `kohaku-v2.1.safetensors` | FP16 | `(128, 256, 3, 3)` | 1 | 294.9K |
| [KBlueLeaf/kohaku-v2.1](https://huggingface.co/KBlueLeaf/kohaku-v2.1) | `kohaku-v2.1.safetensors` | FP16 | `(256, 128, 3, 3)` | 1 | 294.9K |
| [KBlueLeaf/kohaku-v2.1](https://huggingface.co/KBlueLeaf/kohaku-v2.1) | `kohaku-v2.1.safetensors` | FP16 | `(1280)` | 162 | 207.4K |
| [KBlueLeaf/kohaku-v2.1](https://huggingface.co/KBlueLeaf/kohaku-v2.1) | `kohaku-v2.1.safetensors` | FP16 | `(640, 320, 1, 1)` | 1 | 204.8K |
| [KBlueLeaf/kohaku-v2.1](https://huggingface.co/KBlueLeaf/kohaku-v2.1) | `kohaku-v2.1.safetensors` | FP16 | `(256, 512, 1, 1)` | 1 | 131.1K |
| [KBlueLeaf/kohaku-v2.1](https://huggingface.co/KBlueLeaf/kohaku-v2.1) | `kohaku-v2.1.safetensors` | FP16 | `(512, 256, 1, 1)` | 1 | 131.1K |
| [KBlueLeaf/kohaku-v2.1](https://huggingface.co/KBlueLeaf/kohaku-v2.1) | `kohaku-v2.1.safetensors` | FP16 | `(768)` | 110 | 84.5K |
| [KBlueLeaf/kohaku-v2.1](https://huggingface.co/KBlueLeaf/kohaku-v2.1) | `kohaku-v2.1.safetensors` | FP16 | `(640)` | 104 | 66.6K |
| [KBlueLeaf/kohaku-v2.1](https://huggingface.co/KBlueLeaf/kohaku-v2.1) | `kohaku-v2.1.safetensors` | FP16 | `(10240)` | 6 | 61.4K |
| [KBlueLeaf/kohaku-v2.1](https://huggingface.co/KBlueLeaf/kohaku-v2.1) | `kohaku-v2.1.safetensors` | FP16 | `(77, 768)` | 1 | 59.1K |
| [KBlueLeaf/kohaku-v2.1](https://huggingface.co/KBlueLeaf/kohaku-v2.1) | `kohaku-v2.1.safetensors` | FP16 | `(512)` | 103 | 52.7K |
| [KBlueLeaf/kohaku-v2.1](https://huggingface.co/KBlueLeaf/kohaku-v2.1) | `kohaku-v2.1.safetensors` | FP16 | `(2560)` | 15 | 38.4K |
| [KBlueLeaf/kohaku-v2.1](https://huggingface.co/KBlueLeaf/kohaku-v2.1) | `kohaku-v2.1.safetensors` | FP16 | `(3072)` | 12 | 36.9K |
| [KBlueLeaf/kohaku-v2.1](https://huggingface.co/KBlueLeaf/kohaku-v2.1) | `kohaku-v2.1.safetensors` | FP16 | `(8, 512, 3, 3)` | 1 | 36.9K |
| [KBlueLeaf/kohaku-v2.1](https://huggingface.co/KBlueLeaf/kohaku-v2.1) | `kohaku-v2.1.safetensors` | FP16 | `(320)` | 103 | 33.0K |
| [KBlueLeaf/kohaku-v2.1](https://huggingface.co/KBlueLeaf/kohaku-v2.1) | `kohaku-v2.1.safetensors` | FP16 | `(128, 256, 1, 1)` | 1 | 32.8K |
| [KBlueLeaf/kohaku-v2.1](https://huggingface.co/KBlueLeaf/kohaku-v2.1) | `kohaku-v2.1.safetensors` | FP16 | `(256, 128, 1, 1)` | 1 | 32.8K |
| [KBlueLeaf/kohaku-v2.1](https://huggingface.co/KBlueLeaf/kohaku-v2.1) | `kohaku-v2.1.safetensors` | FP16 | `(5120)` | 5 | 25.6K |
| [KBlueLeaf/kohaku-v2.1](https://huggingface.co/KBlueLeaf/kohaku-v2.1) | `kohaku-v2.1.safetensors` | FP16 | `(512, 4, 3, 3)` | 1 | 18.4K |
| [KBlueLeaf/kohaku-v2.1](https://huggingface.co/KBlueLeaf/kohaku-v2.1) | `kohaku-v2.1.safetensors` | FP16 | `(320, 4, 3, 3)` | 1 | 11.5K |
| [KBlueLeaf/kohaku-v2.1](https://huggingface.co/KBlueLeaf/kohaku-v2.1) | `kohaku-v2.1.safetensors` | FP16 | `(4, 320, 3, 3)` | 1 | 11.5K |
| [KBlueLeaf/kohaku-v2.1](https://huggingface.co/KBlueLeaf/kohaku-v2.1) | `kohaku-v2.1.safetensors` | FP16 | `(256)` | 34 | 8.7K |
| [KBlueLeaf/kohaku-v2.1](https://huggingface.co/KBlueLeaf/kohaku-v2.1) | `kohaku-v2.1.safetensors` | FP16 | `(1920)` | 4 | 7.7K |
| [KBlueLeaf/kohaku-v2.1](https://huggingface.co/KBlueLeaf/kohaku-v2.1) | `kohaku-v2.1.safetensors` | FP16 | `(128)` | 35 | 4.5K |
| [KBlueLeaf/kohaku-v2.1](https://huggingface.co/KBlueLeaf/kohaku-v2.1) | `kohaku-v2.1.safetensors` | FP16 | `(960)` | 4 | 3.8K |
| [KBlueLeaf/kohaku-v2.1](https://huggingface.co/KBlueLeaf/kohaku-v2.1) | `kohaku-v2.1.safetensors` | FP16 | `(128, 3, 3, 3)` | 1 | 3.5K |
| [KBlueLeaf/kohaku-v2.1](https://huggingface.co/KBlueLeaf/kohaku-v2.1) | `kohaku-v2.1.safetensors` | FP16 | `(3, 128, 3, 3)` | 1 | 3.5K |
| [KBlueLeaf/kohaku-v2.1](https://huggingface.co/KBlueLeaf/kohaku-v2.1) | `kohaku-v2.1.safetensors` | FP16 | `(8, 8, 1, 1)` | 1 | 64 |
| [KBlueLeaf/kohaku-v2.1](https://huggingface.co/KBlueLeaf/kohaku-v2.1) | `kohaku-v2.1.safetensors` | FP16 | `(4, 4, 1, 1)` | 1 | 16 |
| [KBlueLeaf/kohaku-v2.1](https://huggingface.co/KBlueLeaf/kohaku-v2.1) | `kohaku-v2.1.safetensors` | FP16 | `(8)` | 2 | 16 |
| [KBlueLeaf/kohaku-v2.1](https://huggingface.co/KBlueLeaf/kohaku-v2.1) | `kohaku-v2.1.safetensors` | FP16 | `(4)` | 2 | 8 |
| [KBlueLeaf/kohaku-v2.1](https://huggingface.co/KBlueLeaf/kohaku-v2.1) | `kohaku-v2.1.safetensors` | FP16 | `(3)` | 1 | 3 |
| [KBlueLeaf/kohaku-v2.1](https://huggingface.co/KBlueLeaf/kohaku-v2.1) | `kohaku-v2.1.safetensors` | INT64 | `(1, 77)` | 1 | 77 |
| [Kijai/HunyuanVideo_comfy](https://huggingface.co/Kijai/HunyuanVideo_comfy) | `hunyuan_video_vae_bf16.safetensors` | BF16 | `(512, 512, 3, 3, 3)` | 30 | 212.3M |
| [Kijai/HunyuanVideo_comfy](https://huggingface.co/Kijai/HunyuanVideo_comfy) | `hunyuan_video_720_cfgdistill_fp8_e4m3fn.safetensors` | BF16 | `(12288, 3072)` | 2 | 75.5M |
| [Kijai/HunyuanVideo_comfy](https://huggingface.co/Kijai/HunyuanVideo_comfy) | `hunyuan_video_720_cfgdistill_fp8_e4m3fn.safetensors` | BF16 | `(3072, 12288)` | 2 | 75.5M |
| [Kijai/HunyuanVideo_comfy](https://huggingface.co/Kijai/HunyuanVideo_comfy) | `hunyuan_video_720_cfgdistill_fp8_e4m3fn.safetensors` | BF16 | `(3072, 3072)` | 7 | 66.1M |
| [Kijai/HunyuanVideo_comfy](https://huggingface.co/Kijai/HunyuanVideo_comfy) | `hunyuan_video_720_cfgdistill_fp8_e4m3fn.safetensors` | BF16 | `(6144, 3072)` | 3 | 56.6M |
| [Kijai/HunyuanVideo_comfy](https://huggingface.co/Kijai/HunyuanVideo_comfy) | `hunyuan_video_720_cfgdistill_fp8_e4m3fn.safetensors` | BF16 | `(9216, 3072)` | 2 | 56.6M |
| [Kijai/HunyuanVideo_comfy](https://huggingface.co/Kijai/HunyuanVideo_comfy) | `hunyuan_video_720_cfgdistill_fp8_e4m3fn.safetensors` | BF16 | `(3072, 4096)` | 2 | 25.2M |
| [Kijai/HunyuanVideo_comfy](https://huggingface.co/Kijai/HunyuanVideo_comfy) | `hunyuan_video_vae_bf16.safetensors` | BF16 | `(256, 256, 3, 3, 3)` | 10 | 17.7M |
| [Kijai/HunyuanVideo_comfy](https://huggingface.co/Kijai/HunyuanVideo_comfy) | `hunyuan_video_vae_bf16.safetensors` | BF16 | `(128, 128, 3, 3, 3)` | 10 | 4.4M |
| [Kijai/HunyuanVideo_comfy](https://huggingface.co/Kijai/HunyuanVideo_comfy) | `hunyuan_video_vae_bf16.safetensors` | BF16 | `(256, 512, 3, 3, 3)` | 1 | 3.5M |
| [Kijai/HunyuanVideo_comfy](https://huggingface.co/Kijai/HunyuanVideo_comfy) | `hunyuan_video_vae_bf16.safetensors` | BF16 | `(512, 256, 3, 3, 3)` | 1 | 3.5M |
| [Kijai/HunyuanVideo_comfy](https://huggingface.co/Kijai/HunyuanVideo_comfy) | `hunyuan_video_720_cfgdistill_fp8_e4m3fn.safetensors` | BF16 | `(3072, 256)` | 3 | 2.4M |
| [Kijai/HunyuanVideo_comfy](https://huggingface.co/Kijai/HunyuanVideo_comfy) | `hunyuan_video_720_cfgdistill_fp8_e4m3fn.safetensors` | BF16 | `(3072, 768)` | 1 | 2.4M |
| [Kijai/HunyuanVideo_comfy](https://huggingface.co/Kijai/HunyuanVideo_comfy) | `hunyuan_video_vae_bf16.safetensors` | BF16 | `(512, 512)` | 8 | 2.1M |
| [Kijai/HunyuanVideo_comfy](https://huggingface.co/Kijai/HunyuanVideo_comfy) | `hunyuan_video_vae_bf16.safetensors` | BF16 | `(128, 256, 3, 3, 3)` | 1 | 884.7K |
| [Kijai/HunyuanVideo_comfy](https://huggingface.co/Kijai/HunyuanVideo_comfy) | `hunyuan_video_vae_bf16.safetensors` | BF16 | `(256, 128, 3, 3, 3)` | 1 | 884.7K |
| [Kijai/HunyuanVideo_comfy](https://huggingface.co/Kijai/HunyuanVideo_comfy) | `hunyuan_video_720_cfgdistill_fp8_e4m3fn.safetensors` | BF16 | `(21504)` | 40 | 860.2K |
| [Kijai/HunyuanVideo_comfy](https://huggingface.co/Kijai/HunyuanVideo_comfy) | `hunyuan_video_720_cfgdistill_fp8_e4m3fn.safetensors` | BF16 | `(9216)` | 82 | 755.7K |
| [Kijai/HunyuanVideo_comfy](https://huggingface.co/Kijai/HunyuanVideo_comfy) | `hunyuan_video_720_cfgdistill_fp8_e4m3fn.safetensors` | BF16 | `(18432)` | 40 | 737.3K |
| [Kijai/HunyuanVideo_comfy](https://huggingface.co/Kijai/HunyuanVideo_comfy) | `hunyuan_video_720_cfgdistill_fp8_e4m3fn.safetensors` | BF16 | `(12288)` | 42 | 516.1K |
| [Kijai/HunyuanVideo_comfy](https://huggingface.co/Kijai/HunyuanVideo_comfy) | `hunyuan_video_720_cfgdistill_fp8_e4m3fn.safetensors` | BF16 | `(3072)` | 144 | 442.4K |
| [Kijai/HunyuanVideo_comfy](https://huggingface.co/Kijai/HunyuanVideo_comfy) | `hunyuan_video_vae_bf16.safetensors` | BF16 | `(32, 512, 3, 3, 3)` | 1 | 442.4K |
| [Kijai/HunyuanVideo_comfy](https://huggingface.co/Kijai/HunyuanVideo_comfy) | `hunyuan_video_vae_bf16.safetensors` | BF16 | `(512, 16, 3, 3, 3)` | 1 | 221.2K |
| [Kijai/HunyuanVideo_comfy](https://huggingface.co/Kijai/HunyuanVideo_comfy) | `hunyuan_video_720_cfgdistill_fp8_e4m3fn.safetensors` | BF16 | `(3072, 16, 1, 2, 2)` | 1 | 196.6K |
| [Kijai/HunyuanVideo_comfy](https://huggingface.co/Kijai/HunyuanVideo_comfy) | `hunyuan_video_720_cfgdistill_fp8_e4m3fn.safetensors` | BF16 | `(64, 3072)` | 1 | 196.6K |
| [Kijai/HunyuanVideo_comfy](https://huggingface.co/Kijai/HunyuanVideo_comfy) | `hunyuan_video_vae_bf16.safetensors` | BF16 | `(256, 512, 1, 1, 1)` | 1 | 131.1K |
| [Kijai/HunyuanVideo_comfy](https://huggingface.co/Kijai/HunyuanVideo_comfy) | `hunyuan_video_vae_bf16.safetensors` | BF16 | `(512, 256, 1, 1, 1)` | 1 | 131.1K |
| [Kijai/HunyuanVideo_comfy](https://huggingface.co/Kijai/HunyuanVideo_comfy) | `hunyuan_video_vae_bf16.safetensors` | BF16 | `(512)` | 103 | 52.7K |
| [Kijai/HunyuanVideo_comfy](https://huggingface.co/Kijai/HunyuanVideo_comfy) | `hunyuan_video_vae_bf16.safetensors` | BF16 | `(128, 256, 1, 1, 1)` | 1 | 32.8K |
| [Kijai/HunyuanVideo_comfy](https://huggingface.co/Kijai/HunyuanVideo_comfy) | `hunyuan_video_vae_bf16.safetensors` | BF16 | `(256, 128, 1, 1, 1)` | 1 | 32.8K |
| [Kijai/HunyuanVideo_comfy](https://huggingface.co/Kijai/HunyuanVideo_comfy) | `hunyuan_video_720_cfgdistill_fp8_e4m3fn.safetensors` | BF16 | `(128)` | 160 | 20.5K |
| [Kijai/HunyuanVideo_comfy](https://huggingface.co/Kijai/HunyuanVideo_comfy) | `hunyuan_video_720_cfgdistill_fp8_e4m3fn.safetensors` | BF16 | `(6144)` | 3 | 18.4K |
| [Kijai/HunyuanVideo_comfy](https://huggingface.co/Kijai/HunyuanVideo_comfy) | `hunyuan_video_vae_bf16.safetensors` | BF16 | `(128, 3, 3, 3, 3)` | 1 | 10.4K |
| [Kijai/HunyuanVideo_comfy](https://huggingface.co/Kijai/HunyuanVideo_comfy) | `hunyuan_video_vae_bf16.safetensors` | BF16 | `(3, 128, 3, 3, 3)` | 1 | 10.4K |
| [Kijai/HunyuanVideo_comfy](https://huggingface.co/Kijai/HunyuanVideo_comfy) | `hunyuan_video_vae_bf16.safetensors` | BF16 | `(256)` | 34 | 8.7K |
| [Kijai/HunyuanVideo_comfy](https://huggingface.co/Kijai/HunyuanVideo_comfy) | `hunyuan_video_vae_bf16.safetensors` | BF16 | `(128)` | 35 | 4.5K |
| [Kijai/HunyuanVideo_comfy](https://huggingface.co/Kijai/HunyuanVideo_comfy) | `hunyuan_video_vae_bf16.safetensors` | BF16 | `(32, 32, 1, 1, 1)` | 1 | 1.0K |
| [Kijai/HunyuanVideo_comfy](https://huggingface.co/Kijai/HunyuanVideo_comfy) | `hunyuan_video_vae_bf16.safetensors` | BF16 | `(16, 16, 1, 1, 1)` | 1 | 256 |
| [Kijai/HunyuanVideo_comfy](https://huggingface.co/Kijai/HunyuanVideo_comfy) | `hunyuan_video_vae_bf16.safetensors` | BF16 | `(32)` | 2 | 64 |
| [Kijai/HunyuanVideo_comfy](https://huggingface.co/Kijai/HunyuanVideo_comfy) | `hunyuan_video_720_cfgdistill_fp8_e4m3fn.safetensors` | BF16 | `(64)` | 1 | 64 |
| [Kijai/HunyuanVideo_comfy](https://huggingface.co/Kijai/HunyuanVideo_comfy) | `hunyuan_video_vae_bf16.safetensors` | BF16 | `(16)` | 1 | 16 |
| [Kijai/HunyuanVideo_comfy](https://huggingface.co/Kijai/HunyuanVideo_comfy) | `hunyuan_video_vae_bf16.safetensors` | BF16 | `(3)` | 1 | 3 |
| [Kijai/HunyuanVideo_comfy](https://huggingface.co/Kijai/HunyuanVideo_comfy) | `hunyuan_video_720_cfgdistill_fp8_e4m3fn.safetensors` | FP8 (E4M3FN) | `(21504, 3072)` | 40 | 2.64B |
| [Kijai/HunyuanVideo_comfy](https://huggingface.co/Kijai/HunyuanVideo_comfy) | `hunyuan_video_720_cfgdistill_fp8_e4m3fn.safetensors` | FP8 (E4M3FN) | `(18432, 3072)` | 40 | 2.26B |
| [Kijai/HunyuanVideo_comfy](https://huggingface.co/Kijai/HunyuanVideo_comfy) | `hunyuan_video_720_cfgdistill_fp8_e4m3fn.safetensors` | FP8 (E4M3FN) | `(9216, 3072)` | 80 | 2.26B |
| [Kijai/HunyuanVideo_comfy](https://huggingface.co/Kijai/HunyuanVideo_comfy) | `hunyuan_video_720_cfgdistill_fp8_e4m3fn.safetensors` | FP8 (E4M3FN) | `(3072, 15360)` | 40 | 1.89B |
| [Kijai/HunyuanVideo_comfy](https://huggingface.co/Kijai/HunyuanVideo_comfy) | `hunyuan_video_720_cfgdistill_fp8_e4m3fn.safetensors` | FP8 (E4M3FN) | `(12288, 3072)` | 40 | 1.51B |
| [Kijai/HunyuanVideo_comfy](https://huggingface.co/Kijai/HunyuanVideo_comfy) | `hunyuan_video_720_cfgdistill_fp8_e4m3fn.safetensors` | FP8 (E4M3FN) | `(3072, 12288)` | 40 | 1.51B |
| [Kijai/HunyuanVideo_comfy](https://huggingface.co/Kijai/HunyuanVideo_comfy) | `hunyuan_video_720_cfgdistill_fp8_e4m3fn.safetensors` | FP8 (E4M3FN) | `(3072, 3072)` | 40 | 377.5M |
| [Kijai/llava-llama-3-8b-text-encoder-tokenizer](https://huggingface.co/Kijai/llava-llama-3-8b-text-encoder-tokenizer) | `model-00002-of-00004.safetensors` | FP16 | `(14336, 4096)` | 23 | 1.35B |
| [Kijai/llava-llama-3-8b-text-encoder-tokenizer](https://huggingface.co/Kijai/llava-llama-3-8b-text-encoder-tokenizer) | `model-00003-of-00004.safetensors` | FP16 | `(14336, 4096)` | 23 | 1.35B |
| [Kijai/llava-llama-3-8b-text-encoder-tokenizer](https://huggingface.co/Kijai/llava-llama-3-8b-text-encoder-tokenizer) | `model-00001-of-00004.safetensors` | FP16 | `(14336, 4096)` | 18 | 1.06B |
| [Kijai/llava-llama-3-8b-text-encoder-tokenizer](https://huggingface.co/Kijai/llava-llama-3-8b-text-encoder-tokenizer) | `model-00002-of-00004.safetensors` | FP16 | `(4096, 14336)` | 11 | 645.9M |
| [Kijai/llava-llama-3-8b-text-encoder-tokenizer](https://huggingface.co/Kijai/llava-llama-3-8b-text-encoder-tokenizer) | `model-00003-of-00004.safetensors` | FP16 | `(4096, 14336)` | 11 | 645.9M |
| [Kijai/llava-llama-3-8b-text-encoder-tokenizer](https://huggingface.co/Kijai/llava-llama-3-8b-text-encoder-tokenizer) | `model-00001-of-00004.safetensors` | FP16 | `(4096, 14336)` | 9 | 528.5M |
| [Kijai/llava-llama-3-8b-text-encoder-tokenizer](https://huggingface.co/Kijai/llava-llama-3-8b-text-encoder-tokenizer) | `model-00001-of-00004.safetensors` | FP16 | `(128320, 4096)` | 1 | 525.6M |
| [Kijai/llava-llama-3-8b-text-encoder-tokenizer](https://huggingface.co/Kijai/llava-llama-3-8b-text-encoder-tokenizer) | `model-00002-of-00004.safetensors` | FP16 | `(4096, 4096)` | 24 | 402.7M |
| [Kijai/llava-llama-3-8b-text-encoder-tokenizer](https://huggingface.co/Kijai/llava-llama-3-8b-text-encoder-tokenizer) | `model-00003-of-00004.safetensors` | FP16 | `(4096, 4096)` | 22 | 369.1M |
| [Kijai/llava-llama-3-8b-text-encoder-tokenizer](https://huggingface.co/Kijai/llava-llama-3-8b-text-encoder-tokenizer) | `model-00001-of-00004.safetensors` | FP16 | `(4096, 4096)` | 18 | 302.0M |
| [Kijai/llava-llama-3-8b-text-encoder-tokenizer](https://huggingface.co/Kijai/llava-llama-3-8b-text-encoder-tokenizer) | `model-00002-of-00004.safetensors` | FP16 | `(1024, 4096)` | 24 | 100.7M |
| [Kijai/llava-llama-3-8b-text-encoder-tokenizer](https://huggingface.co/Kijai/llava-llama-3-8b-text-encoder-tokenizer) | `model-00003-of-00004.safetensors` | FP16 | `(1024, 4096)` | 22 | 92.3M |
| [Kijai/llava-llama-3-8b-text-encoder-tokenizer](https://huggingface.co/Kijai/llava-llama-3-8b-text-encoder-tokenizer) | `model-00001-of-00004.safetensors` | FP16 | `(1024, 4096)` | 18 | 75.5M |
| [Kijai/llava-llama-3-8b-text-encoder-tokenizer](https://huggingface.co/Kijai/llava-llama-3-8b-text-encoder-tokenizer) | `model-00002-of-00004.safetensors` | FP16 | `(4096)` | 22 | 90.1K |
| [Kijai/llava-llama-3-8b-text-encoder-tokenizer](https://huggingface.co/Kijai/llava-llama-3-8b-text-encoder-tokenizer) | `model-00003-of-00004.safetensors` | FP16 | `(4096)` | 22 | 90.1K |
| [Kijai/llava-llama-3-8b-text-encoder-tokenizer](https://huggingface.co/Kijai/llava-llama-3-8b-text-encoder-tokenizer) | `model-00001-of-00004.safetensors` | FP16 | `(4096)` | 18 | 73.7K |
| [latent-consistency/lcm-lora-sdv1-5](https://huggingface.co/latent-consistency/lcm-lora-sdv1-5) | `pytorch_lora_weights.safetensors` | FP16 | `(64, 1280, 3, 3)` | 21 | 15.5M |
| [latent-consistency/lcm-lora-sdv1-5](https://huggingface.co/latent-consistency/lcm-lora-sdv1-5) | `pytorch_lora_weights.safetensors` | FP16 | `(64, 2560, 3, 3)` | 5 | 7.4M |
| [latent-consistency/lcm-lora-sdv1-5](https://huggingface.co/latent-consistency/lcm-lora-sdv1-5) | `pytorch_lora_weights.safetensors` | FP16 | `(64, 1280)` | 69 | 5.7M |
| [latent-consistency/lcm-lora-sdv1-5](https://huggingface.co/latent-consistency/lcm-lora-sdv1-5) | `pytorch_lora_weights.safetensors` | FP16 | `(1280, 64)` | 66 | 5.4M |
| [latent-consistency/lcm-lora-sdv1-5](https://huggingface.co/latent-consistency/lcm-lora-sdv1-5) | `pytorch_lora_weights.safetensors` | FP16 | `(64, 640, 3, 3)` | 11 | 4.1M |
| [latent-consistency/lcm-lora-sdv1-5](https://huggingface.co/latent-consistency/lcm-lora-sdv1-5) | `pytorch_lora_weights.safetensors` | FP16 | `(10240, 64)` | 6 | 3.9M |
| [latent-consistency/lcm-lora-sdv1-5](https://huggingface.co/latent-consistency/lcm-lora-sdv1-5) | `pytorch_lora_weights.safetensors` | FP16 | `(1280, 64, 1, 1)` | 46 | 3.8M |
| [latent-consistency/lcm-lora-sdv1-5](https://huggingface.co/latent-consistency/lcm-lora-sdv1-5) | `pytorch_lora_weights.safetensors` | FP16 | `(64, 1920, 3, 3)` | 2 | 2.2M |
| [latent-consistency/lcm-lora-sdv1-5](https://huggingface.co/latent-consistency/lcm-lora-sdv1-5) | `pytorch_lora_weights.safetensors` | FP16 | `(640, 64)` | 50 | 2.0M |
| [latent-consistency/lcm-lora-sdv1-5](https://huggingface.co/latent-consistency/lcm-lora-sdv1-5) | `pytorch_lora_weights.safetensors` | FP16 | `(64, 5120)` | 6 | 2.0M |
| [latent-consistency/lcm-lora-sdv1-5](https://huggingface.co/latent-consistency/lcm-lora-sdv1-5) | `pytorch_lora_weights.safetensors` | FP16 | `(64, 320, 3, 3)` | 9 | 1.7M |
| [latent-consistency/lcm-lora-sdv1-5](https://huggingface.co/latent-consistency/lcm-lora-sdv1-5) | `pytorch_lora_weights.safetensors` | FP16 | `(5120, 64)` | 5 | 1.6M |
| [latent-consistency/lcm-lora-sdv1-5](https://huggingface.co/latent-consistency/lcm-lora-sdv1-5) | `pytorch_lora_weights.safetensors` | FP16 | `(64, 768)` | 32 | 1.6M |
| [latent-consistency/lcm-lora-sdv1-5](https://huggingface.co/latent-consistency/lcm-lora-sdv1-5) | `pytorch_lora_weights.safetensors` | FP16 | `(64, 640)` | 35 | 1.4M |
| [latent-consistency/lcm-lora-sdv1-5](https://huggingface.co/latent-consistency/lcm-lora-sdv1-5) | `pytorch_lora_weights.safetensors` | FP16 | `(64, 960, 3, 3)` | 2 | 1.1M |
| [latent-consistency/lcm-lora-sdv1-5](https://huggingface.co/latent-consistency/lcm-lora-sdv1-5) | `pytorch_lora_weights.safetensors` | FP16 | `(64, 1280, 1, 1)` | 13 | 1.1M |
| [latent-consistency/lcm-lora-sdv1-5](https://huggingface.co/latent-consistency/lcm-lora-sdv1-5) | `pytorch_lora_weights.safetensors` | FP16 | `(640, 64, 1, 1)` | 26 | 1.1M |
| [latent-consistency/lcm-lora-sdv1-5](https://huggingface.co/latent-consistency/lcm-lora-sdv1-5) | `pytorch_lora_weights.safetensors` | FP16 | `(320, 64)` | 50 | 1.0M |
| [latent-consistency/lcm-lora-sdv1-5](https://huggingface.co/latent-consistency/lcm-lora-sdv1-5) | `pytorch_lora_weights.safetensors` | FP16 | `(2560, 64)` | 5 | 819.2K |
| [latent-consistency/lcm-lora-sdv1-5](https://huggingface.co/latent-consistency/lcm-lora-sdv1-5) | `pytorch_lora_weights.safetensors` | FP16 | `(64, 2560)` | 5 | 819.2K |
| [latent-consistency/lcm-lora-sdv1-5](https://huggingface.co/latent-consistency/lcm-lora-sdv1-5) | `pytorch_lora_weights.safetensors` | FP16 | `(64, 2560, 1, 1)` | 5 | 819.2K |
| [latent-consistency/lcm-lora-sdv1-5](https://huggingface.co/latent-consistency/lcm-lora-sdv1-5) | `pytorch_lora_weights.safetensors` | FP16 | `(64, 320)` | 35 | 716.8K |
| [latent-consistency/lcm-lora-sdv1-5](https://huggingface.co/latent-consistency/lcm-lora-sdv1-5) | `pytorch_lora_weights.safetensors` | FP16 | `(64, 640, 1, 1)` | 13 | 532.5K |
| [latent-consistency/lcm-lora-sdv1-5](https://huggingface.co/latent-consistency/lcm-lora-sdv1-5) | `pytorch_lora_weights.safetensors` | FP16 | `(320, 64, 1, 1)` | 24 | 491.5K |
| [latent-consistency/lcm-lora-sdv1-5](https://huggingface.co/latent-consistency/lcm-lora-sdv1-5) | `pytorch_lora_weights.safetensors` | FP16 | `(64, 1920, 1, 1)` | 2 | 245.8K |
| [latent-consistency/lcm-lora-sdv1-5](https://huggingface.co/latent-consistency/lcm-lora-sdv1-5) | `pytorch_lora_weights.safetensors` | FP16 | `(64, 320, 1, 1)` | 11 | 225.3K |
| [latent-consistency/lcm-lora-sdv1-5](https://huggingface.co/latent-consistency/lcm-lora-sdv1-5) | `pytorch_lora_weights.safetensors` | FP16 | `(64, 960, 1, 1)` | 2 | 122.9K |
| [latent-consistency/lcm-lora-sdv1-5](https://huggingface.co/latent-consistency/lcm-lora-sdv1-5) | `pytorch_lora_weights.safetensors` | FP16 | `()` | 278 | 278 |
| [latent-consistency/lcm-lora-sdxl](https://huggingface.co/latent-consistency/lcm-lora-sdxl) | `pytorch_lora_weights.safetensors` | FP16 | `(1280, 64)` | 559 | 45.8M |
| [latent-consistency/lcm-lora-sdxl](https://huggingface.co/latent-consistency/lcm-lora-sdxl) | `pytorch_lora_weights.safetensors` | FP16 | `(10240, 64)` | 60 | 39.3M |
| [latent-consistency/lcm-lora-sdxl](https://huggingface.co/latent-consistency/lcm-lora-sdxl) | `pytorch_lora_weights.safetensors` | FP16 | `(64, 1280)` | 449 | 36.8M |
| [latent-consistency/lcm-lora-sdxl](https://huggingface.co/latent-consistency/lcm-lora-sdxl) | `pytorch_lora_weights.safetensors` | FP16 | `(64, 5120)` | 60 | 19.7M |
| [latent-consistency/lcm-lora-sdxl](https://huggingface.co/latent-consistency/lcm-lora-sdxl) | `pytorch_lora_weights.safetensors` | FP16 | `(64, 2048)` | 140 | 18.4M |
| [latent-consistency/lcm-lora-sdxl](https://huggingface.co/latent-consistency/lcm-lora-sdxl) | `pytorch_lora_weights.safetensors` | FP16 | `(64, 1280, 3, 3)` | 12 | 8.8M |
| [latent-consistency/lcm-lora-sdxl](https://huggingface.co/latent-consistency/lcm-lora-sdxl) | `pytorch_lora_weights.safetensors` | FP16 | `(640, 64)` | 105 | 4.3M |
| [latent-consistency/lcm-lora-sdxl](https://huggingface.co/latent-consistency/lcm-lora-sdxl) | `pytorch_lora_weights.safetensors` | FP16 | `(64, 640, 3, 3)` | 11 | 4.1M |
| [latent-consistency/lcm-lora-sdxl](https://huggingface.co/latent-consistency/lcm-lora-sdxl) | `pytorch_lora_weights.safetensors` | FP16 | `(5120, 64)` | 10 | 3.3M |
| [latent-consistency/lcm-lora-sdxl](https://huggingface.co/latent-consistency/lcm-lora-sdxl) | `pytorch_lora_weights.safetensors` | FP16 | `(64, 640)` | 80 | 3.3M |
| [latent-consistency/lcm-lora-sdxl](https://huggingface.co/latent-consistency/lcm-lora-sdxl) | `pytorch_lora_weights.safetensors` | FP16 | `(64, 2560, 3, 3)` | 2 | 2.9M |
| [latent-consistency/lcm-lora-sdxl](https://huggingface.co/latent-consistency/lcm-lora-sdxl) | `pytorch_lora_weights.safetensors` | FP16 | `(64, 1920, 3, 3)` | 2 | 2.2M |
| [latent-consistency/lcm-lora-sdxl](https://huggingface.co/latent-consistency/lcm-lora-sdxl) | `pytorch_lora_weights.safetensors` | FP16 | `(64, 320, 3, 3)` | 9 | 1.7M |
| [latent-consistency/lcm-lora-sdxl](https://huggingface.co/latent-consistency/lcm-lora-sdxl) | `pytorch_lora_weights.safetensors` | FP16 | `(64, 2560)` | 10 | 1.6M |
| [latent-consistency/lcm-lora-sdxl](https://huggingface.co/latent-consistency/lcm-lora-sdxl) | `pytorch_lora_weights.safetensors` | FP16 | `(1280, 64, 1, 1)` | 19 | 1.6M |
| [latent-consistency/lcm-lora-sdxl](https://huggingface.co/latent-consistency/lcm-lora-sdxl) | `pytorch_lora_weights.safetensors` | FP16 | `(64, 960, 3, 3)` | 2 | 1.1M |
| [latent-consistency/lcm-lora-sdxl](https://huggingface.co/latent-consistency/lcm-lora-sdxl) | `pytorch_lora_weights.safetensors` | FP16 | `(640, 64, 1, 1)` | 16 | 655.4K |
| [latent-consistency/lcm-lora-sdxl](https://huggingface.co/latent-consistency/lcm-lora-sdxl) | `pytorch_lora_weights.safetensors` | FP16 | `(64, 2560, 1, 1)` | 2 | 327.7K |
| [latent-consistency/lcm-lora-sdxl](https://huggingface.co/latent-consistency/lcm-lora-sdxl) | `pytorch_lora_weights.safetensors` | FP16 | `(320, 64, 1, 1)` | 14 | 286.7K |
| [latent-consistency/lcm-lora-sdxl](https://huggingface.co/latent-consistency/lcm-lora-sdxl) | `pytorch_lora_weights.safetensors` | FP16 | `(64, 1920, 1, 1)` | 2 | 245.8K |
| [latent-consistency/lcm-lora-sdxl](https://huggingface.co/latent-consistency/lcm-lora-sdxl) | `pytorch_lora_weights.safetensors` | FP16 | `(64, 640, 1, 1)` | 3 | 122.9K |
| [latent-consistency/lcm-lora-sdxl](https://huggingface.co/latent-consistency/lcm-lora-sdxl) | `pytorch_lora_weights.safetensors` | FP16 | `(64, 960, 1, 1)` | 2 | 122.9K |
| [latent-consistency/lcm-lora-sdxl](https://huggingface.co/latent-consistency/lcm-lora-sdxl) | `pytorch_lora_weights.safetensors` | FP16 | `(320, 64)` | 5 | 102.4K |
| [latent-consistency/lcm-lora-sdxl](https://huggingface.co/latent-consistency/lcm-lora-sdxl) | `pytorch_lora_weights.safetensors` | FP16 | `(64, 1280, 1, 1)` | 1 | 81.9K |
| [latent-consistency/lcm-lora-sdxl](https://huggingface.co/latent-consistency/lcm-lora-sdxl) | `pytorch_lora_weights.safetensors` | FP16 | `(64, 320, 1, 1)` | 1 | 20.5K |
| [latent-consistency/lcm-lora-sdxl](https://huggingface.co/latent-consistency/lcm-lora-sdxl) | `pytorch_lora_weights.safetensors` | FP16 | `()` | 788 | 788 |
| [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video) | `ltx-video-2b-v0.9.5.safetensors` | BF16 | `(2048, 2048)` | 227 | 952.1M |
| [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video) | `ltx-video-2b-v0.9.5.safetensors` | BF16 | `(2048, 8192)` | 28 | 469.8M |
| [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video) | `ltx-video-2b-v0.9.5.safetensors` | BF16 | `(8192, 2048)` | 28 | 469.8M |
| [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video) | `ltx-video-2b-v0.9.5.safetensors` | BF16 | `(2048, 2048, 3, 3, 3)` | 4 | 453.0M |
| [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video) | `ltx-video-2b-v0.9.5.safetensors` | BF16 | `(1024, 1024, 3, 3, 3)` | 14 | 396.4M |
| [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video) | `ltx-video-2b-v0.9.5.safetensors` | BF16 | `(512, 512, 3, 3, 3)` | 22 | 155.7M |
| [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video) | `ltx-video-2b-v0.9.5.safetensors` | BF16 | `(4096, 1024, 3, 3, 3)` | 1 | 113.2M |
| [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video) | `ltx-video-2b-v0.9.5.safetensors` | BF16 | `(256, 256, 3, 3, 3)` | 23 | 40.7M |
| [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video) | `ltx-video-2b-v0.9.5.safetensors` | BF16 | `(2048, 512, 3, 3, 3)` | 1 | 28.3M |
| [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video) | `ltx-video-2b-v0.9.5.safetensors` | BF16 | `(12288, 2048)` | 1 | 25.2M |
| [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video) | `ltx-video-2b-v0.9.5.safetensors` | BF16 | `(4096, 4096)` | 1 | 16.8M |
| [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video) | `ltx-video-2b-v0.9.5.safetensors` | BF16 | `(2048, 4096)` | 1 | 8.4M |
| [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video) | `ltx-video-2b-v0.9.5.safetensors` | BF16 | `(128, 128, 3, 3, 3)` | 18 | 8.0M |
| [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video) | `ltx-video-2b-v0.9.5.safetensors` | BF16 | `(129, 2048, 3, 3, 3)` | 1 | 7.1M |
| [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video) | `ltx-video-2b-v0.9.5.safetensors` | BF16 | `(1024, 256, 3, 3, 3)` | 1 | 7.1M |
| [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video) | `ltx-video-2b-v0.9.5.safetensors` | BF16 | `(256, 1024, 3, 3, 3)` | 1 | 7.1M |
| [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video) | `ltx-video-2b-v0.9.5.safetensors` | BF16 | `(1024, 128, 3, 3, 3)` | 1 | 3.5M |
| [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video) | `ltx-video-2b-v0.9.5.safetensors` | BF16 | `(128, 512, 3, 3, 3)` | 1 | 1.8M |
| [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video) | `ltx-video-2b-v0.9.5.safetensors` | BF16 | `(1024, 1024)` | 1 | 1.0M |
| [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video) | `ltx-video-2b-v0.9.5.safetensors` | BF16 | `(2048, 256)` | 2 | 1.0M |
| [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video) | `ltx-video-2b-v0.9.5.safetensors` | BF16 | `(4096, 256)` | 1 | 1.0M |
| [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video) | `ltx-video-2b-v0.9.5.safetensors` | BF16 | `(2048)` | 376 | 770.0K |
| [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video) | `ltx-video-2b-v0.9.5.safetensors` | BF16 | `(6, 2048)` | 28 | 344.1K |
| [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video) | `ltx-video-2b-v0.9.5.safetensors` | BF16 | `(1024, 256)` | 1 | 262.1K |
| [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video) | `ltx-video-2b-v0.9.5.safetensors` | BF16 | `(128, 2048)` | 1 | 262.1K |
| [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video) | `ltx-video-2b-v0.9.5.safetensors` | BF16 | `(2048, 128)` | 1 | 262.1K |
| [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video) | `ltx-video-2b-v0.9.5.safetensors` | BF16 | `(512, 512)` | 1 | 262.1K |
| [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video) | `ltx-video-2b-v0.9.5.safetensors` | BF16 | `(8192)` | 28 | 229.4K |
| [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video) | `ltx-video-2b-v0.9.5.safetensors` | BF16 | `(64, 128, 3, 3, 3)` | 1 | 221.2K |
| [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video) | `ltx-video-2b-v0.9.5.safetensors` | BF16 | `(128, 48, 3, 3, 3)` | 1 | 165.9K |
| [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video) | `ltx-video-2b-v0.9.5.safetensors` | BF16 | `(48, 128, 3, 3, 3)` | 1 | 165.9K |
| [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video) | `ltx-video-2b-v0.9.5.safetensors` | BF16 | `(256, 256)` | 2 | 131.1K |
| [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video) | `ltx-video-2b-v0.9.5.safetensors` | BF16 | `(512, 256)` | 1 | 131.1K |
| [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video) | `ltx-video-2b-v0.9.5.safetensors` | BF16 | `(4, 1024)` | 5 | 20.5K |
| [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video) | `ltx-video-2b-v0.9.5.safetensors` | BF16 | `(1024)` | 18 | 18.4K |
| [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video) | `ltx-video-2b-v0.9.5.safetensors` | BF16 | `(12288)` | 1 | 12.3K |
| [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video) | `ltx-video-2b-v0.9.5.safetensors` | BF16 | `(4096)` | 3 | 12.3K |
| [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video) | `ltx-video-2b-v0.9.5.safetensors` | BF16 | `(512)` | 24 | 12.3K |
| [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video) | `ltx-video-2b-v0.9.5.safetensors` | BF16 | `(4, 512)` | 5 | 10.2K |
| [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video) | `ltx-video-2b-v0.9.5.safetensors` | BF16 | `(256)` | 26 | 6.7K |
| [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video) | `ltx-video-2b-v0.9.5.safetensors` | BF16 | `(4, 256)` | 5 | 5.1K |
| [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video) | `ltx-video-2b-v0.9.5.safetensors` | BF16 | `(2, 2048)` | 1 | 4.1K |
| [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video) | `ltx-video-2b-v0.9.5.safetensors` | BF16 | `(128)` | 26 | 3.3K |
| [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video) | `ltx-video-2b-v0.9.5.safetensors` | BF16 | `(4, 128)` | 5 | 2.6K |
| [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video) | `ltx-video-2b-v0.9.5.safetensors` | BF16 | `(2, 128)` | 1 | 256 |
| [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video) | `ltx-video-2b-v0.9.5.safetensors` | BF16 | `(129)` | 1 | 129 |
| [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video) | `ltx-video-2b-v0.9.5.safetensors` | BF16 | `(64)` | 1 | 64 |
| [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video) | `ltx-video-2b-v0.9.5.safetensors` | BF16 | `(48)` | 1 | 48 |
| [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video) | `ltx-video-2b-v0.9.5.safetensors` | BF16 | `()` | 1 | 1 |
| [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video) | `ltx-video-2b-v0.9.safetensors` | FP32 | `(2048, 2048)` | 226 | 947.9M |
| [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video) | `ltx-video-2b-v0.9.safetensors` | FP32 | `(2048, 8192)` | 28 | 469.8M |
| [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video) | `ltx-video-2b-v0.9.safetensors` | FP32 | `(8192, 2048)` | 28 | 469.8M |
| [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video) | `ltx-video-2b-v0.9.safetensors` | FP32 | `(512, 512, 3, 3, 3)` | 42 | 297.3M |
| [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video) | `ltx-video-2b-v0.9.safetensors` | FP32 | `(4096, 512, 3, 3, 3)` | 1 | 56.6M |
| [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video) | `ltx-video-2b-v0.9.safetensors` | FP32 | `(256, 256, 3, 3, 3)` | 15 | 26.5M |
| [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video) | `ltx-video-2b-v0.9.safetensors` | FP32 | `(12288, 2048)` | 1 | 25.2M |
| [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video) | `ltx-video-2b-v0.9.safetensors` | FP32 | `(2048, 256, 3, 3, 3)` | 1 | 14.2M |
| [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video) | `ltx-video-2b-v0.9.safetensors` | FP32 | `(2048, 4096)` | 1 | 8.4M |
| [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video) | `ltx-video-2b-v0.9.safetensors` | FP32 | `(128, 128, 3, 3, 3)` | 18 | 8.0M |
| [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video) | `ltx-video-2b-v0.9.safetensors` | FP32 | `(1024, 128, 3, 3, 3)` | 1 | 3.5M |
| [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video) | `ltx-video-2b-v0.9.safetensors` | FP32 | `(256, 512, 3, 3, 3)` | 1 | 3.5M |
| [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video) | `ltx-video-2b-v0.9.safetensors` | FP32 | `(512, 256, 3, 3, 3)` | 1 | 3.5M |
| [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video) | `ltx-video-2b-v0.9.safetensors` | FP32 | `(129, 512, 3, 3, 3)` | 1 | 1.8M |
| [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video) | `ltx-video-2b-v0.9.safetensors` | FP32 | `(512, 128, 3, 3, 3)` | 1 | 1.8M |
| [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video) | `ltx-video-2b-v0.9.safetensors` | FP32 | `(128, 256, 3, 3, 3)` | 1 | 884.7K |
| [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video) | `ltx-video-2b-v0.9.safetensors` | FP32 | `(256, 128, 3, 3, 3)` | 1 | 884.7K |
| [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video) | `ltx-video-2b-v0.9.safetensors` | FP32 | `(2048)` | 370 | 757.8K |
| [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video) | `ltx-video-2b-v0.9.safetensors` | FP32 | `(2048, 256)` | 1 | 524.3K |
| [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video) | `ltx-video-2b-v0.9.safetensors` | FP32 | `(6, 2048)` | 28 | 344.1K |
| [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video) | `ltx-video-2b-v0.9.safetensors` | FP32 | `(128, 2048)` | 1 | 262.1K |
| [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video) | `ltx-video-2b-v0.9.safetensors` | FP32 | `(2048, 128)` | 1 | 262.1K |
| [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video) | `ltx-video-2b-v0.9.safetensors` | FP32 | `(8192)` | 28 | 229.4K |
| [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video) | `ltx-video-2b-v0.9.safetensors` | FP32 | `(128, 48, 3, 3, 3)` | 1 | 165.9K |
| [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video) | `ltx-video-2b-v0.9.safetensors` | FP32 | `(48, 128, 3, 3, 3)` | 1 | 165.9K |
| [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video) | `ltx-video-2b-v0.9.safetensors` | FP32 | `(256, 512, 1, 1, 1)` | 1 | 131.1K |
| [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video) | `ltx-video-2b-v0.9.safetensors` | FP32 | `(512, 256, 1, 1, 1)` | 1 | 131.1K |
| [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video) | `ltx-video-2b-v0.9.safetensors` | FP32 | `(128, 256, 1, 1, 1)` | 1 | 32.8K |
| [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video) | `ltx-video-2b-v0.9.safetensors` | FP32 | `(256, 128, 1, 1, 1)` | 1 | 32.8K |
| [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video) | `ltx-video-2b-v0.9.safetensors` | FP32 | `(512)` | 47 | 24.1K |
| [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video) | `ltx-video-2b-v0.9.safetensors` | FP32 | `(12288)` | 1 | 12.3K |
| [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video) | `ltx-video-2b-v0.9.safetensors` | FP32 | `(256)` | 23 | 5.9K |
| [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video) | `ltx-video-2b-v0.9.safetensors` | FP32 | `(2, 2048)` | 1 | 4.1K |
| [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video) | `ltx-video-2b-v0.9.safetensors` | FP32 | `(4096)` | 1 | 4.1K |
| [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video) | `ltx-video-2b-v0.9.safetensors` | FP32 | `(128)` | 29 | 3.7K |
| [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video) | `ltx-video-2b-v0.9.safetensors` | FP32 | `(1024)` | 1 | 1.0K |
| [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video) | `ltx-video-2b-v0.9.safetensors` | FP32 | `(129)` | 1 | 129 |
| [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video) | `ltx-video-2b-v0.9.safetensors` | FP32 | `(48)` | 1 | 48 |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/DreamShaper.safetensors` | FP16 | `(1280, 1280, 3, 3)` | 20 | 294.9M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/MeinaMix.safetensors` | FP16 | `(1280, 1280, 3, 3)` | 20 | 294.9M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/ghostmix_v20Bakedvae.safetensors` | FP16 | `(1280, 1280, 3, 3)` | 20 | 294.9M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/DreamShaper.safetensors` | FP16 | `(1280, 2560, 3, 3)` | 5 | 147.5M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/MeinaMix.safetensors` | FP16 | `(1280, 2560, 3, 3)` | 5 | 147.5M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/ghostmix_v20Bakedvae.safetensors` | FP16 | `(1280, 2560, 3, 3)` | 5 | 147.5M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/DreamShaper.safetensors` | FP16 | `(1280, 1280)` | 49 | 80.3M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/MeinaMix.safetensors` | FP16 | `(1280, 1280)` | 49 | 80.3M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/ghostmix_v20Bakedvae.safetensors` | FP16 | `(1280, 1280)` | 49 | 80.3M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/DreamShaper.safetensors` | FP16 | `(10240, 1280)` | 6 | 78.6M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/MeinaMix.safetensors` | FP16 | `(10240, 1280)` | 6 | 78.6M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/ghostmix_v20Bakedvae.safetensors` | FP16 | `(10240, 1280)` | 6 | 78.6M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/ghostmix_v20Bakedvae.safetensors` | FP16 | `(49408, 768)` | 2 | 75.9M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/DreamShaper.safetensors` | FP16 | `(512, 512, 3, 3)` | 30 | 70.8M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/MeinaMix.safetensors` | FP16 | `(512, 512, 3, 3)` | 30 | 70.8M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/ghostmix_v20Bakedvae.safetensors` | FP16 | `(512, 512, 3, 3)` | 30 | 70.8M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/ghostmix_v20Bakedvae.safetensors` | FP16 | `(3072, 768)` | 24 | 56.6M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/ghostmix_v20Bakedvae.safetensors` | FP16 | `(768, 3072)` | 24 | 56.6M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/ghostmix_v20Bakedvae.safetensors` | FP16 | `(768, 768)` | 96 | 56.6M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/DreamShaper.safetensors` | FP16 | `(1280, 5120)` | 6 | 39.3M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/MeinaMix.safetensors` | FP16 | `(1280, 5120)` | 6 | 39.3M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/ghostmix_v20Bakedvae.safetensors` | FP16 | `(1280, 5120)` | 6 | 39.3M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/DreamShaper.safetensors` | FP16 | `(49408, 768)` | 1 | 37.9M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/MeinaMix.safetensors` | FP16 | `(49408, 768)` | 1 | 37.9M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/DreamShaper.safetensors` | FP16 | `(640, 640, 3, 3)` | 8 | 29.5M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/MeinaMix.safetensors` | FP16 | `(640, 640, 3, 3)` | 8 | 29.5M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/ghostmix_v20Bakedvae.safetensors` | FP16 | `(640, 640, 3, 3)` | 8 | 29.5M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/DreamShaper.safetensors` | FP16 | `(3072, 768)` | 12 | 28.3M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/MeinaMix.safetensors` | FP16 | `(3072, 768)` | 12 | 28.3M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/DreamShaper.safetensors` | FP16 | `(768, 3072)` | 12 | 28.3M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/MeinaMix.safetensors` | FP16 | `(768, 3072)` | 12 | 28.3M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/DreamShaper.safetensors` | FP16 | `(768, 768)` | 48 | 28.3M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/MeinaMix.safetensors` | FP16 | `(768, 768)` | 48 | 28.3M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/DreamShaper.safetensors` | FP16 | `(1280, 1920, 3, 3)` | 1 | 22.1M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/MeinaMix.safetensors` | FP16 | `(1280, 1920, 3, 3)` | 1 | 22.1M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/ghostmix_v20Bakedvae.safetensors` | FP16 | `(1280, 1920, 3, 3)` | 1 | 22.1M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/DreamShaper.safetensors` | FP16 | `(1280, 1280, 1, 1)` | 12 | 19.7M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/MeinaMix.safetensors` | FP16 | `(1280, 1280, 1, 1)` | 12 | 19.7M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/ghostmix_v20Bakedvae.safetensors` | FP16 | `(1280, 1280, 1, 1)` | 12 | 19.7M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/DreamShaper.safetensors` | FP16 | `(1280, 2560, 1, 1)` | 5 | 16.4M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/MeinaMix.safetensors` | FP16 | `(1280, 2560, 1, 1)` | 5 | 16.4M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/ghostmix_v20Bakedvae.safetensors` | FP16 | `(1280, 2560, 1, 1)` | 5 | 16.4M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/DreamShaper.safetensors` | FP16 | `(5120, 640)` | 5 | 16.4M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/MeinaMix.safetensors` | FP16 | `(5120, 640)` | 5 | 16.4M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/ghostmix_v20Bakedvae.safetensors` | FP16 | `(5120, 640)` | 5 | 16.4M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/DreamShaper.safetensors` | FP16 | `(640, 640)` | 30 | 12.3M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/MeinaMix.safetensors` | FP16 | `(640, 640)` | 30 | 12.3M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/ghostmix_v20Bakedvae.safetensors` | FP16 | `(640, 640)` | 30 | 12.3M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/DreamShaper.safetensors` | FP16 | `(1280, 768)` | 12 | 11.8M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/MeinaMix.safetensors` | FP16 | `(1280, 768)` | 12 | 11.8M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/ghostmix_v20Bakedvae.safetensors` | FP16 | `(1280, 768)` | 12 | 11.8M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/DreamShaper.safetensors` | FP16 | `(640, 1920, 3, 3)` | 1 | 11.1M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/MeinaMix.safetensors` | FP16 | `(640, 1920, 3, 3)` | 1 | 11.1M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/ghostmix_v20Bakedvae.safetensors` | FP16 | `(640, 1920, 3, 3)` | 1 | 11.1M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/DreamShaper.safetensors` | FP16 | `(640, 2560)` | 5 | 8.2M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/MeinaMix.safetensors` | FP16 | `(640, 2560)` | 5 | 8.2M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/ghostmix_v20Bakedvae.safetensors` | FP16 | `(640, 2560)` | 5 | 8.2M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/DreamShaper.safetensors` | FP16 | `(1280, 640, 3, 3)` | 1 | 7.4M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/MeinaMix.safetensors` | FP16 | `(1280, 640, 3, 3)` | 1 | 7.4M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/ghostmix_v20Bakedvae.safetensors` | FP16 | `(1280, 640, 3, 3)` | 1 | 7.4M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/DreamShaper.safetensors` | FP16 | `(320, 320, 3, 3)` | 8 | 7.4M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/MeinaMix.safetensors` | FP16 | `(320, 320, 3, 3)` | 8 | 7.4M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/ghostmix_v20Bakedvae.safetensors` | FP16 | `(320, 320, 3, 3)` | 8 | 7.4M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/DreamShaper.safetensors` | FP16 | `(640, 1280, 3, 3)` | 1 | 7.4M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/MeinaMix.safetensors` | FP16 | `(640, 1280, 3, 3)` | 1 | 7.4M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/ghostmix_v20Bakedvae.safetensors` | FP16 | `(640, 1280, 3, 3)` | 1 | 7.4M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/DreamShaper.safetensors` | FP16 | `(256, 256, 3, 3)` | 10 | 5.9M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/MeinaMix.safetensors` | FP16 | `(256, 256, 3, 3)` | 10 | 5.9M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/ghostmix_v20Bakedvae.safetensors` | FP16 | `(256, 256, 3, 3)` | 10 | 5.9M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/DreamShaper.safetensors` | FP16 | `(640, 960, 3, 3)` | 1 | 5.5M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/MeinaMix.safetensors` | FP16 | `(640, 960, 3, 3)` | 1 | 5.5M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/ghostmix_v20Bakedvae.safetensors` | FP16 | `(640, 960, 3, 3)` | 1 | 5.5M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/DreamShaper.safetensors` | FP16 | `(640, 768)` | 10 | 4.9M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/MeinaMix.safetensors` | FP16 | `(640, 768)` | 10 | 4.9M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/ghostmix_v20Bakedvae.safetensors` | FP16 | `(640, 768)` | 10 | 4.9M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/DreamShaper.safetensors` | FP16 | `(2560, 320)` | 5 | 4.1M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/MeinaMix.safetensors` | FP16 | `(2560, 320)` | 5 | 4.1M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/ghostmix_v20Bakedvae.safetensors` | FP16 | `(2560, 320)` | 5 | 4.1M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/DreamShaper.safetensors` | FP16 | `(320, 1280)` | 10 | 4.1M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/MeinaMix.safetensors` | FP16 | `(320, 1280)` | 10 | 4.1M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/ghostmix_v20Bakedvae.safetensors` | FP16 | `(320, 1280)` | 10 | 4.1M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/DreamShaper.safetensors` | FP16 | `(640, 1280)` | 5 | 4.1M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/MeinaMix.safetensors` | FP16 | `(640, 1280)` | 5 | 4.1M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/ghostmix_v20Bakedvae.safetensors` | FP16 | `(640, 1280)` | 5 | 4.1M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/DreamShaper.safetensors` | FP16 | `(640, 640, 1, 1)` | 10 | 4.1M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/MeinaMix.safetensors` | FP16 | `(640, 640, 1, 1)` | 10 | 4.1M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/ghostmix_v20Bakedvae.safetensors` | FP16 | `(640, 640, 1, 1)` | 10 | 4.1M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/DreamShaper.safetensors` | FP16 | `(320, 640, 3, 3)` | 2 | 3.7M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/MeinaMix.safetensors` | FP16 | `(320, 640, 3, 3)` | 2 | 3.7M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/ghostmix_v20Bakedvae.safetensors` | FP16 | `(320, 640, 3, 3)` | 2 | 3.7M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/DreamShaper.safetensors` | FP16 | `(320, 320)` | 30 | 3.1M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/MeinaMix.safetensors` | FP16 | `(320, 320)` | 30 | 3.1M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/ghostmix_v20Bakedvae.safetensors` | FP16 | `(320, 320)` | 30 | 3.1M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/ghostmix_v20Bakedvae.safetensors` | FP16 | `(64, 768)` | 60 | 2.9M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/ghostmix_v20Bakedvae.safetensors` | FP16 | `(768, 64)` | 60 | 2.9M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/DreamShaper.safetensors` | FP16 | `(320, 960, 3, 3)` | 1 | 2.8M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/MeinaMix.safetensors` | FP16 | `(320, 960, 3, 3)` | 1 | 2.8M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/ghostmix_v20Bakedvae.safetensors` | FP16 | `(320, 960, 3, 3)` | 1 | 2.8M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/DreamShaper.safetensors` | FP16 | `(1280, 1920, 1, 1)` | 1 | 2.5M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/MeinaMix.safetensors` | FP16 | `(1280, 1920, 1, 1)` | 1 | 2.5M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/ghostmix_v20Bakedvae.safetensors` | FP16 | `(1280, 1920, 1, 1)` | 1 | 2.5M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/DreamShaper.safetensors` | FP16 | `(320, 768)` | 10 | 2.5M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/MeinaMix.safetensors` | FP16 | `(320, 768)` | 10 | 2.5M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/ghostmix_v20Bakedvae.safetensors` | FP16 | `(320, 768)` | 10 | 2.5M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/ghostmix_v20Bakedvae.safetensors` | FP16 | `(3072, 64)` | 12 | 2.4M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/ghostmix_v20Bakedvae.safetensors` | FP16 | `(64, 3072)` | 12 | 2.4M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/DreamShaper.safetensors` | FP16 | `(512, 512, 1, 1)` | 8 | 2.1M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/MeinaMix.safetensors` | FP16 | `(512, 512, 1, 1)` | 8 | 2.1M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/ghostmix_v20Bakedvae.safetensors` | FP16 | `(512, 512, 1, 1)` | 8 | 2.1M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/DreamShaper.safetensors` | FP16 | `(640, 320, 3, 3)` | 1 | 1.8M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/MeinaMix.safetensors` | FP16 | `(640, 320, 3, 3)` | 1 | 1.8M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/ghostmix_v20Bakedvae.safetensors` | FP16 | `(640, 320, 3, 3)` | 1 | 1.8M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/DreamShaper.safetensors` | FP16 | `(128, 128, 3, 3)` | 10 | 1.5M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/MeinaMix.safetensors` | FP16 | `(128, 128, 3, 3)` | 10 | 1.5M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/ghostmix_v20Bakedvae.safetensors` | FP16 | `(128, 128, 3, 3)` | 10 | 1.5M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/DreamShaper.safetensors` | FP16 | `(640, 1920, 1, 1)` | 1 | 1.2M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/MeinaMix.safetensors` | FP16 | `(640, 1920, 1, 1)` | 1 | 1.2M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/ghostmix_v20Bakedvae.safetensors` | FP16 | `(640, 1920, 1, 1)` | 1 | 1.2M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/DreamShaper.safetensors` | FP16 | `(256, 512, 3, 3)` | 1 | 1.2M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/MeinaMix.safetensors` | FP16 | `(256, 512, 3, 3)` | 1 | 1.2M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/ghostmix_v20Bakedvae.safetensors` | FP16 | `(256, 512, 3, 3)` | 1 | 1.2M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/DreamShaper.safetensors` | FP16 | `(512, 256, 3, 3)` | 1 | 1.2M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/MeinaMix.safetensors` | FP16 | `(512, 256, 3, 3)` | 1 | 1.2M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/ghostmix_v20Bakedvae.safetensors` | FP16 | `(512, 256, 3, 3)` | 1 | 1.2M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/DreamShaper.safetensors` | FP16 | `(320, 320, 1, 1)` | 10 | 1.0M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/MeinaMix.safetensors` | FP16 | `(320, 320, 1, 1)` | 10 | 1.0M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/ghostmix_v20Bakedvae.safetensors` | FP16 | `(320, 320, 1, 1)` | 10 | 1.0M |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/DreamShaper.safetensors` | FP16 | `(1280, 640, 1, 1)` | 1 | 819.2K |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/MeinaMix.safetensors` | FP16 | `(1280, 640, 1, 1)` | 1 | 819.2K |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/ghostmix_v20Bakedvae.safetensors` | FP16 | `(1280, 640, 1, 1)` | 1 | 819.2K |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/DreamShaper.safetensors` | FP16 | `(640, 1280, 1, 1)` | 1 | 819.2K |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/MeinaMix.safetensors` | FP16 | `(640, 1280, 1, 1)` | 1 | 819.2K |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/ghostmix_v20Bakedvae.safetensors` | FP16 | `(640, 1280, 1, 1)` | 1 | 819.2K |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/DreamShaper.safetensors` | FP16 | `(640, 960, 1, 1)` | 1 | 614.4K |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/MeinaMix.safetensors` | FP16 | `(640, 960, 1, 1)` | 1 | 614.4K |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/ghostmix_v20Bakedvae.safetensors` | FP16 | `(640, 960, 1, 1)` | 1 | 614.4K |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/DreamShaper.safetensors` | FP16 | `(1280, 320)` | 1 | 409.6K |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/MeinaMix.safetensors` | FP16 | `(1280, 320)` | 1 | 409.6K |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/ghostmix_v20Bakedvae.safetensors` | FP16 | `(1280, 320)` | 1 | 409.6K |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/DreamShaper.safetensors` | FP16 | `(320, 640, 1, 1)` | 2 | 409.6K |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/MeinaMix.safetensors` | FP16 | `(320, 640, 1, 1)` | 2 | 409.6K |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/ghostmix_v20Bakedvae.safetensors` | FP16 | `(320, 640, 1, 1)` | 2 | 409.6K |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/DreamShaper.safetensors` | FP16 | `(320, 960, 1, 1)` | 1 | 307.2K |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/MeinaMix.safetensors` | FP16 | `(320, 960, 1, 1)` | 1 | 307.2K |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/ghostmix_v20Bakedvae.safetensors` | FP16 | `(320, 960, 1, 1)` | 1 | 307.2K |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/DreamShaper.safetensors` | FP16 | `(128, 256, 3, 3)` | 1 | 294.9K |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/MeinaMix.safetensors` | FP16 | `(128, 256, 3, 3)` | 1 | 294.9K |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/ghostmix_v20Bakedvae.safetensors` | FP16 | `(128, 256, 3, 3)` | 1 | 294.9K |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/DreamShaper.safetensors` | FP16 | `(256, 128, 3, 3)` | 1 | 294.9K |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/MeinaMix.safetensors` | FP16 | `(256, 128, 3, 3)` | 1 | 294.9K |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/ghostmix_v20Bakedvae.safetensors` | FP16 | `(256, 128, 3, 3)` | 1 | 294.9K |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/DreamShaper.safetensors` | FP16 | `(1280)` | 162 | 207.4K |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/MeinaMix.safetensors` | FP16 | `(1280)` | 162 | 207.4K |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/ghostmix_v20Bakedvae.safetensors` | FP16 | `(1280)` | 162 | 207.4K |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/DreamShaper.safetensors` | FP16 | `(640, 320, 1, 1)` | 1 | 204.8K |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/MeinaMix.safetensors` | FP16 | `(640, 320, 1, 1)` | 1 | 204.8K |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/ghostmix_v20Bakedvae.safetensors` | FP16 | `(640, 320, 1, 1)` | 1 | 204.8K |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/ghostmix_v20Bakedvae.safetensors` | FP16 | `(768)` | 220 | 169.0K |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/DreamShaper.safetensors` | FP16 | `(256, 512, 1, 1)` | 1 | 131.1K |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/MeinaMix.safetensors` | FP16 | `(256, 512, 1, 1)` | 1 | 131.1K |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/ghostmix_v20Bakedvae.safetensors` | FP16 | `(256, 512, 1, 1)` | 1 | 131.1K |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/DreamShaper.safetensors` | FP16 | `(512, 256, 1, 1)` | 1 | 131.1K |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/MeinaMix.safetensors` | FP16 | `(512, 256, 1, 1)` | 1 | 131.1K |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/ghostmix_v20Bakedvae.safetensors` | FP16 | `(512, 256, 1, 1)` | 1 | 131.1K |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/ghostmix_v20Bakedvae.safetensors` | FP16 | `(77, 768)` | 2 | 118.3K |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/DreamShaper.safetensors` | FP16 | `(768)` | 110 | 84.5K |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/MeinaMix.safetensors` | FP16 | `(768)` | 110 | 84.5K |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/ghostmix_v20Bakedvae.safetensors` | FP16 | `(3072)` | 24 | 73.7K |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/DreamShaper.safetensors` | FP16 | `(640)` | 104 | 66.6K |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/MeinaMix.safetensors` | FP16 | `(640)` | 104 | 66.6K |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/ghostmix_v20Bakedvae.safetensors` | FP16 | `(640)` | 104 | 66.6K |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/DreamShaper.safetensors` | FP16 | `(10240)` | 6 | 61.4K |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/MeinaMix.safetensors` | FP16 | `(10240)` | 6 | 61.4K |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/ghostmix_v20Bakedvae.safetensors` | FP16 | `(10240)` | 6 | 61.4K |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/DreamShaper.safetensors` | FP16 | `(77, 768)` | 1 | 59.1K |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/MeinaMix.safetensors` | FP16 | `(77, 768)` | 1 | 59.1K |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/DreamShaper.safetensors` | FP16 | `(512)` | 103 | 52.7K |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/MeinaMix.safetensors` | FP16 | `(512)` | 103 | 52.7K |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/ghostmix_v20Bakedvae.safetensors` | FP16 | `(512)` | 103 | 52.7K |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/DreamShaper.safetensors` | FP16 | `(2560)` | 15 | 38.4K |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/MeinaMix.safetensors` | FP16 | `(2560)` | 15 | 38.4K |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/ghostmix_v20Bakedvae.safetensors` | FP16 | `(2560)` | 15 | 38.4K |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/DreamShaper.safetensors` | FP16 | `(3072)` | 12 | 36.9K |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/MeinaMix.safetensors` | FP16 | `(3072)` | 12 | 36.9K |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/DreamShaper.safetensors` | FP16 | `(8, 512, 3, 3)` | 1 | 36.9K |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/MeinaMix.safetensors` | FP16 | `(8, 512, 3, 3)` | 1 | 36.9K |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/ghostmix_v20Bakedvae.safetensors` | FP16 | `(8, 512, 3, 3)` | 1 | 36.9K |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/DreamShaper.safetensors` | FP16 | `(320)` | 103 | 33.0K |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/MeinaMix.safetensors` | FP16 | `(320)` | 103 | 33.0K |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/ghostmix_v20Bakedvae.safetensors` | FP16 | `(320)` | 103 | 33.0K |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/DreamShaper.safetensors` | FP16 | `(128, 256, 1, 1)` | 1 | 32.8K |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/MeinaMix.safetensors` | FP16 | `(128, 256, 1, 1)` | 1 | 32.8K |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/ghostmix_v20Bakedvae.safetensors` | FP16 | `(128, 256, 1, 1)` | 1 | 32.8K |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/DreamShaper.safetensors` | FP16 | `(256, 128, 1, 1)` | 1 | 32.8K |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/MeinaMix.safetensors` | FP16 | `(256, 128, 1, 1)` | 1 | 32.8K |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/ghostmix_v20Bakedvae.safetensors` | FP16 | `(256, 128, 1, 1)` | 1 | 32.8K |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/DreamShaper.safetensors` | FP16 | `(5120)` | 5 | 25.6K |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/MeinaMix.safetensors` | FP16 | `(5120)` | 5 | 25.6K |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/ghostmix_v20Bakedvae.safetensors` | FP16 | `(5120)` | 5 | 25.6K |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/DreamShaper.safetensors` | FP16 | `(512, 4, 3, 3)` | 1 | 18.4K |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/MeinaMix.safetensors` | FP16 | `(512, 4, 3, 3)` | 1 | 18.4K |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/ghostmix_v20Bakedvae.safetensors` | FP16 | `(512, 4, 3, 3)` | 1 | 18.4K |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/MeinaMix.safetensors` | FP16 | `(1000)` | 12 | 12.0K |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/ghostmix_v20Bakedvae.safetensors` | FP16 | `(1000)` | 12 | 12.0K |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/DreamShaper.safetensors` | FP16 | `(320, 4, 3, 3)` | 1 | 11.5K |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/MeinaMix.safetensors` | FP16 | `(320, 4, 3, 3)` | 1 | 11.5K |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/ghostmix_v20Bakedvae.safetensors` | FP16 | `(320, 4, 3, 3)` | 1 | 11.5K |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/DreamShaper.safetensors` | FP16 | `(4, 320, 3, 3)` | 1 | 11.5K |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/MeinaMix.safetensors` | FP16 | `(4, 320, 3, 3)` | 1 | 11.5K |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/ghostmix_v20Bakedvae.safetensors` | FP16 | `(4, 320, 3, 3)` | 1 | 11.5K |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/DreamShaper.safetensors` | FP16 | `(256)` | 34 | 8.7K |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/MeinaMix.safetensors` | FP16 | `(256)` | 34 | 8.7K |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/ghostmix_v20Bakedvae.safetensors` | FP16 | `(256)` | 34 | 8.7K |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/DreamShaper.safetensors` | FP16 | `(1920)` | 4 | 7.7K |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/MeinaMix.safetensors` | FP16 | `(1920)` | 4 | 7.7K |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/ghostmix_v20Bakedvae.safetensors` | FP16 | `(1920)` | 4 | 7.7K |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/DreamShaper.safetensors` | FP16 | `(128)` | 35 | 4.5K |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/MeinaMix.safetensors` | FP16 | `(128)` | 35 | 4.5K |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/ghostmix_v20Bakedvae.safetensors` | FP16 | `(128)` | 35 | 4.5K |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/DreamShaper.safetensors` | FP16 | `(960)` | 4 | 3.8K |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/MeinaMix.safetensors` | FP16 | `(960)` | 4 | 3.8K |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/ghostmix_v20Bakedvae.safetensors` | FP16 | `(960)` | 4 | 3.8K |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/DreamShaper.safetensors` | FP16 | `(128, 3, 3, 3)` | 1 | 3.5K |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/MeinaMix.safetensors` | FP16 | `(128, 3, 3, 3)` | 1 | 3.5K |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/ghostmix_v20Bakedvae.safetensors` | FP16 | `(128, 3, 3, 3)` | 1 | 3.5K |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/DreamShaper.safetensors` | FP16 | `(3, 128, 3, 3)` | 1 | 3.5K |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/MeinaMix.safetensors` | FP16 | `(3, 128, 3, 3)` | 1 | 3.5K |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/ghostmix_v20Bakedvae.safetensors` | FP16 | `(3, 128, 3, 3)` | 1 | 3.5K |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/ghostmix_v20Bakedvae.safetensors` | FP16 | `(1, 77)` | 2 | 154 |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/ghostmix_v20Bakedvae.safetensors` | FP16 | `()` | 72 | 72 |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/DreamShaper.safetensors` | FP16 | `(8, 8, 1, 1)` | 1 | 64 |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/MeinaMix.safetensors` | FP16 | `(8, 8, 1, 1)` | 1 | 64 |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/ghostmix_v20Bakedvae.safetensors` | FP16 | `(8, 8, 1, 1)` | 1 | 64 |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/DreamShaper.safetensors` | FP16 | `(4, 4, 1, 1)` | 1 | 16 |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/MeinaMix.safetensors` | FP16 | `(4, 4, 1, 1)` | 1 | 16 |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/ghostmix_v20Bakedvae.safetensors` | FP16 | `(4, 4, 1, 1)` | 1 | 16 |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/DreamShaper.safetensors` | FP16 | `(8)` | 2 | 16 |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/MeinaMix.safetensors` | FP16 | `(8)` | 2 | 16 |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/ghostmix_v20Bakedvae.safetensors` | FP16 | `(8)` | 2 | 16 |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/DreamShaper.safetensors` | FP16 | `(4)` | 2 | 8 |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/MeinaMix.safetensors` | FP16 | `(4)` | 2 | 8 |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/ghostmix_v20Bakedvae.safetensors` | FP16 | `(4)` | 2 | 8 |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/DreamShaper.safetensors` | FP16 | `(3)` | 1 | 3 |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/MeinaMix.safetensors` | FP16 | `(3)` | 1 | 3 |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/ghostmix_v20Bakedvae.safetensors` | FP16 | `(3)` | 1 | 3 |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/MeinaMix.safetensors` | FP16 | `()` | 2 | 2 |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/DreamShaper.safetensors` | INT64 | `(1, 77)` | 1 | 77 |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | `checkpoints/SD1.5/MeinaMix.safetensors` | INT64 | `(1, 77)` | 1 | 77 |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4-v2.safetensors` | BF16 | `(21504)` | 38 | 817.2K |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4.safetensors` | BF16 | `(21504)` | 38 | 817.2K |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4-v2.safetensors` | BF16 | `(18432)` | 38 | 700.4K |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4.safetensors` | BF16 | `(18432)` | 38 | 700.4K |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4-v2.safetensors` | BF16 | `(9216)` | 76 | 700.4K |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4.safetensors` | BF16 | `(9216)` | 76 | 700.4K |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4-v2.safetensors` | BF16 | `(12288)` | 38 | 466.9K |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4.safetensors` | BF16 | `(12288)` | 38 | 466.9K |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4-v2.safetensors` | BF16 | `(3072)` | 122 | 374.8K |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4.safetensors` | BF16 | `(3072)` | 122 | 374.8K |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4-v2.safetensors` | BF16 | `(6144)` | 1 | 6.1K |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4.safetensors` | BF16 | `(6144)` | 1 | 6.1K |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4-v2.safetensors` | BF16 | `(64)` | 1 | 64 |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4.safetensors` | BF16 | `(64)` | 1 | 64 |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4-v2.safetensors` | FP16 | `(49408, 768)` | 1 | 37.9M |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4.safetensors` | FP16 | `(49408, 768)` | 1 | 37.9M |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4-v2.safetensors` | FP16 | `(768, 768)` | 49 | 28.9M |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4.safetensors` | FP16 | `(768, 768)` | 49 | 28.9M |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4-v2.safetensors` | FP16 | `(3072, 768)` | 12 | 28.3M |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4.safetensors` | FP16 | `(3072, 768)` | 12 | 28.3M |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4-v2.safetensors` | FP16 | `(768, 3072)` | 12 | 28.3M |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4.safetensors` | FP16 | `(768, 3072)` | 12 | 28.3M |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4-v2.safetensors` | FP16 | `(768)` | 110 | 84.5K |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4.safetensors` | FP16 | `(768)` | 110 | 84.5K |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4-v2.safetensors` | FP16 | `(77, 768)` | 1 | 59.1K |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4.safetensors` | FP16 | `(77, 768)` | 1 | 59.1K |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4-v2.safetensors` | FP16 | `(3072)` | 12 | 36.9K |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4.safetensors` | FP16 | `(3072)` | 12 | 36.9K |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4-v2.safetensors` | FP32 | `(512, 512, 3, 3)` | 30 | 70.8M |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4.safetensors` | FP32 | `(512, 512, 3, 3)` | 30 | 70.8M |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4-v2.safetensors` | FP32 | `(589824)` | 76 | 44.8M |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4-v2.safetensors` | FP32 | `(1032192)` | 38 | 39.2M |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4-v2.safetensors` | FP32 | `(442368)` | 76 | 33.6M |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4-v2.safetensors` | FP32 | `(884736)` | 38 | 33.6M |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4-v2.safetensors` | FP32 | `(737280)` | 38 | 28.0M |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4-v2.safetensors` | FP32 | `(147456)` | 41 | 6.0M |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4-v2.safetensors` | FP32 | `(256, 256, 3, 3)` | 10 | 5.9M |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4.safetensors` | FP32 | `(256, 256, 3, 3)` | 10 | 5.9M |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4-v2.safetensors` | FP32 | `(512, 512, 1, 1)` | 8 | 2.1M |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4.safetensors` | FP32 | `(512, 512, 1, 1)` | 8 | 2.1M |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4-v2.safetensors` | FP32 | `(128, 128, 3, 3)` | 10 | 1.5M |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4.safetensors` | FP32 | `(128, 128, 3, 3)` | 10 | 1.5M |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4-v2.safetensors` | FP32 | `(256, 512, 3, 3)` | 1 | 1.2M |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4.safetensors` | FP32 | `(256, 512, 3, 3)` | 1 | 1.2M |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4-v2.safetensors` | FP32 | `(512, 256, 3, 3)` | 1 | 1.2M |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4.safetensors` | FP32 | `(512, 256, 3, 3)` | 1 | 1.2M |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4-v2.safetensors` | FP32 | `(128, 256, 3, 3)` | 1 | 294.9K |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4.safetensors` | FP32 | `(128, 256, 3, 3)` | 1 | 294.9K |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4-v2.safetensors` | FP32 | `(256, 128, 3, 3)` | 1 | 294.9K |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4.safetensors` | FP32 | `(256, 128, 3, 3)` | 1 | 294.9K |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4-v2.safetensors` | FP32 | `(294912)` | 1 | 294.9K |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4-v2.safetensors` | FP32 | `(196608)` | 1 | 196.6K |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4.safetensors` | FP32 | `(2304)` | 76 | 175.1K |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4.safetensors` | FP32 | `(4032)` | 38 | 153.2K |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4-v2.safetensors` | FP32 | `(32, 512, 3, 3)` | 1 | 147.5K |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4.safetensors` | FP32 | `(32, 512, 3, 3)` | 1 | 147.5K |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4.safetensors` | FP32 | `(1728)` | 76 | 131.3K |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4.safetensors` | FP32 | `(3456)` | 38 | 131.3K |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4-v2.safetensors` | FP32 | `(256, 512, 1, 1)` | 1 | 131.1K |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4.safetensors` | FP32 | `(256, 512, 1, 1)` | 1 | 131.1K |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4-v2.safetensors` | FP32 | `(512, 256, 1, 1)` | 1 | 131.1K |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4.safetensors` | FP32 | `(512, 256, 1, 1)` | 1 | 131.1K |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4.safetensors` | FP32 | `(2880)` | 38 | 109.4K |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4.safetensors` | FP32 | `(256)` | 348 | 89.1K |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4-v2.safetensors` | FP32 | `(512, 16, 3, 3)` | 1 | 73.7K |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4.safetensors` | FP32 | `(512, 16, 3, 3)` | 1 | 73.7K |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4-v2.safetensors` | FP32 | `(512)` | 103 | 52.7K |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4.safetensors` | FP32 | `(512)` | 103 | 52.7K |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4-v2.safetensors` | FP32 | `(36864)` | 1 | 36.9K |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4-v2.safetensors` | FP32 | `(128, 256, 1, 1)` | 1 | 32.8K |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4.safetensors` | FP32 | `(128, 256, 1, 1)` | 1 | 32.8K |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4-v2.safetensors` | FP32 | `(256, 128, 1, 1)` | 1 | 32.8K |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4.safetensors` | FP32 | `(256, 128, 1, 1)` | 1 | 32.8K |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4-v2.safetensors` | FP32 | `(12288)` | 2 | 24.6K |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4-v2.safetensors` | FP32 | `(128)` | 187 | 23.9K |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4.safetensors` | FP32 | `(128)` | 187 | 23.9K |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4.safetensors` | FP32 | `(576)` | 41 | 23.6K |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4-v2.safetensors` | FP32 | `(256)` | 34 | 8.7K |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4-v2.safetensors` | FP32 | `(3072)` | 2 | 6.1K |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4-v2.safetensors` | FP32 | `(16)` | 314 | 5.0K |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4.safetensors` | FP32 | `(16)` | 314 | 5.0K |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4-v2.safetensors` | FP32 | `(128, 3, 3, 3)` | 1 | 3.5K |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4.safetensors` | FP32 | `(128, 3, 3, 3)` | 1 | 3.5K |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4-v2.safetensors` | FP32 | `(3, 128, 3, 3)` | 1 | 3.5K |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4.safetensors` | FP32 | `(3, 128, 3, 3)` | 1 | 3.5K |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4.safetensors` | FP32 | `(1152)` | 1 | 1.2K |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4.safetensors` | FP32 | `(768)` | 1 | 768 |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4.safetensors` | FP32 | `(144)` | 1 | 144 |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4.safetensors` | FP32 | `(48)` | 2 | 96 |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4-v2.safetensors` | FP32 | `(32)` | 1 | 32 |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4.safetensors` | FP32 | `(32)` | 1 | 32 |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4.safetensors` | FP32 | `(12)` | 2 | 24 |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4-v2.safetensors` | FP32 | `(3)` | 1 | 3 |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4.safetensors` | FP32 | `(3)` | 1 | 3 |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4-v2.safetensors` | FP32 | `()` | 2 | 2 |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4.safetensors` | FP32 | `()` | 2 | 2 |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4-v2.safetensors` | FP8 (E4M3FN) | `(10240, 4096)` | 48 | 2.01B |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4.safetensors` | FP8 (E4M3FN) | `(10240, 4096)` | 48 | 2.01B |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4-v2.safetensors` | FP8 (E4M3FN) | `(4096, 4096)` | 96 | 1.61B |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4.safetensors` | FP8 (E4M3FN) | `(4096, 4096)` | 96 | 1.61B |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4-v2.safetensors` | FP8 (E4M3FN) | `(4096, 10240)` | 24 | 1.01B |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4.safetensors` | FP8 (E4M3FN) | `(4096, 10240)` | 24 | 1.01B |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4-v2.safetensors` | FP8 (E4M3FN) | `(32128, 4096)` | 1 | 131.6M |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4.safetensors` | FP8 (E4M3FN) | `(32128, 4096)` | 1 | 131.6M |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4-v2.safetensors` | FP8 (E4M3FN) | `(4096)` | 49 | 200.7K |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4.safetensors` | FP8 (E4M3FN) | `(4096)` | 49 | 200.7K |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4-v2.safetensors` | FP8 (E4M3FN) | `(32, 64)` | 1 | 2.0K |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4.safetensors` | FP8 (E4M3FN) | `(32, 64)` | 1 | 2.0K |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4-v2.safetensors` | NF4 (packed U8) | `(18874368, 1)` | 76 | 1.43B |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4.safetensors` | NF4 (packed U8) | `(18874368, 1)` | 76 | 1.43B |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4-v2.safetensors` | NF4 (packed U8) | `(33030144, 1)` | 38 | 1.26B |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4.safetensors` | NF4 (packed U8) | `(33030144, 1)` | 38 | 1.26B |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4-v2.safetensors` | NF4 (packed U8) | `(14155776, 1)` | 76 | 1.08B |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4.safetensors` | NF4 (packed U8) | `(14155776, 1)` | 76 | 1.08B |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4-v2.safetensors` | NF4 (packed U8) | `(28311552, 1)` | 38 | 1.08B |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4.safetensors` | NF4 (packed U8) | `(28311552, 1)` | 38 | 1.08B |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4-v2.safetensors` | NF4 (packed U8) | `(23592960, 1)` | 38 | 896.5M |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4.safetensors` | NF4 (packed U8) | `(23592960, 1)` | 38 | 896.5M |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4-v2.safetensors` | NF4 (packed U8) | `(4718592, 1)` | 41 | 193.5M |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4.safetensors` | NF4 (packed U8) | `(4718592, 1)` | 41 | 193.5M |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4.safetensors` | NF4 (packed U8) | `(589824)` | 76 | 44.8M |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4.safetensors` | NF4 (packed U8) | `(1032192)` | 38 | 39.2M |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4.safetensors` | NF4 (packed U8) | `(442368)` | 76 | 33.6M |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4.safetensors` | NF4 (packed U8) | `(884736)` | 38 | 33.6M |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4.safetensors` | NF4 (packed U8) | `(737280)` | 38 | 28.0M |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4-v2.safetensors` | NF4 (packed U8) | `(9437184, 1)` | 1 | 9.4M |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4.safetensors` | NF4 (packed U8) | `(9437184, 1)` | 1 | 9.4M |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4-v2.safetensors` | NF4 (packed U8) | `(6291456, 1)` | 1 | 6.3M |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4.safetensors` | NF4 (packed U8) | `(6291456, 1)` | 1 | 6.3M |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4.safetensors` | NF4 (packed U8) | `(147456)` | 41 | 6.0M |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4-v2.safetensors` | NF4 (packed U8) | `(1179648, 1)` | 1 | 1.2M |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4.safetensors` | NF4 (packed U8) | `(1179648, 1)` | 1 | 1.2M |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4-v2.safetensors` | NF4 (packed U8) | `(393216, 1)` | 2 | 786.4K |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4.safetensors` | NF4 (packed U8) | `(393216, 1)` | 2 | 786.4K |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4.safetensors` | NF4 (packed U8) | `(294912)` | 1 | 294.9K |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4.safetensors` | NF4 (packed U8) | `(196608)` | 1 | 196.6K |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4-v2.safetensors` | NF4 (packed U8) | `(98304, 1)` | 2 | 196.6K |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4.safetensors` | NF4 (packed U8) | `(98304, 1)` | 2 | 196.6K |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4.safetensors` | NF4 (packed U8) | `(36864)` | 1 | 36.9K |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4.safetensors` | NF4 (packed U8) | `(173)` | 152 | 26.3K |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4.safetensors` | NF4 (packed U8) | `(12288)` | 2 | 24.6K |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4.safetensors` | NF4 (packed U8) | `(172)` | 132 | 22.7K |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4-v2.safetensors` | NF4 (packed U8) | `(83)` | 190 | 15.8K |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4-v2.safetensors` | NF4 (packed U8) | `(82)` | 119 | 9.8K |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4.safetensors` | NF4 (packed U8) | `(3072)` | 2 | 6.1K |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4.safetensors` | NF4 (packed U8) | `(171)` | 25 | 4.3K |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4.safetensors` | NF4 (packed U8) | `(170)` | 3 | 510 |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4.safetensors` | NF4 (packed U8) | `(174)` | 2 | 348 |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4-v2.safetensors` | NF4 (packed U8) | `(81)` | 3 | 243 |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | `flux1-dev-bnb-nf4-v2.safetensors` | NF4 (packed U8) | `(80)` | 2 | 160 |
| [lllyasviel/flux1_dev](https://huggingface.co/lllyasviel/flux1_dev) | `flux1-dev-fp8.safetensors` | FP16 | `(49408, 768)` | 1 | 37.9M |
| [lllyasviel/flux1_dev](https://huggingface.co/lllyasviel/flux1_dev) | `flux1-dev-fp8.safetensors` | FP16 | `(768, 768)` | 49 | 28.9M |
| [lllyasviel/flux1_dev](https://huggingface.co/lllyasviel/flux1_dev) | `flux1-dev-fp8.safetensors` | FP16 | `(3072, 768)` | 12 | 28.3M |
| [lllyasviel/flux1_dev](https://huggingface.co/lllyasviel/flux1_dev) | `flux1-dev-fp8.safetensors` | FP16 | `(768, 3072)` | 12 | 28.3M |
| [lllyasviel/flux1_dev](https://huggingface.co/lllyasviel/flux1_dev) | `flux1-dev-fp8.safetensors` | FP16 | `(768)` | 110 | 84.5K |
| [lllyasviel/flux1_dev](https://huggingface.co/lllyasviel/flux1_dev) | `flux1-dev-fp8.safetensors` | FP16 | `(77, 768)` | 1 | 59.1K |
| [lllyasviel/flux1_dev](https://huggingface.co/lllyasviel/flux1_dev) | `flux1-dev-fp8.safetensors` | FP16 | `(3072)` | 12 | 36.9K |
| [lllyasviel/flux1_dev](https://huggingface.co/lllyasviel/flux1_dev) | `flux1-dev-fp8.safetensors` | FP32 | `(512, 512, 3, 3)` | 30 | 70.8M |
| [lllyasviel/flux1_dev](https://huggingface.co/lllyasviel/flux1_dev) | `flux1-dev-fp8.safetensors` | FP32 | `(256, 256, 3, 3)` | 10 | 5.9M |
| [lllyasviel/flux1_dev](https://huggingface.co/lllyasviel/flux1_dev) | `flux1-dev-fp8.safetensors` | FP32 | `(512, 512, 1, 1)` | 8 | 2.1M |
| [lllyasviel/flux1_dev](https://huggingface.co/lllyasviel/flux1_dev) | `flux1-dev-fp8.safetensors` | FP32 | `(128, 128, 3, 3)` | 10 | 1.5M |
| [lllyasviel/flux1_dev](https://huggingface.co/lllyasviel/flux1_dev) | `flux1-dev-fp8.safetensors` | FP32 | `(256, 512, 3, 3)` | 1 | 1.2M |
| [lllyasviel/flux1_dev](https://huggingface.co/lllyasviel/flux1_dev) | `flux1-dev-fp8.safetensors` | FP32 | `(512, 256, 3, 3)` | 1 | 1.2M |
| [lllyasviel/flux1_dev](https://huggingface.co/lllyasviel/flux1_dev) | `flux1-dev-fp8.safetensors` | FP32 | `(128, 256, 3, 3)` | 1 | 294.9K |
| [lllyasviel/flux1_dev](https://huggingface.co/lllyasviel/flux1_dev) | `flux1-dev-fp8.safetensors` | FP32 | `(256, 128, 3, 3)` | 1 | 294.9K |
| [lllyasviel/flux1_dev](https://huggingface.co/lllyasviel/flux1_dev) | `flux1-dev-fp8.safetensors` | FP32 | `(32, 512, 3, 3)` | 1 | 147.5K |
| [lllyasviel/flux1_dev](https://huggingface.co/lllyasviel/flux1_dev) | `flux1-dev-fp8.safetensors` | FP32 | `(256, 512, 1, 1)` | 1 | 131.1K |
| [lllyasviel/flux1_dev](https://huggingface.co/lllyasviel/flux1_dev) | `flux1-dev-fp8.safetensors` | FP32 | `(512, 256, 1, 1)` | 1 | 131.1K |
| [lllyasviel/flux1_dev](https://huggingface.co/lllyasviel/flux1_dev) | `flux1-dev-fp8.safetensors` | FP32 | `(512, 16, 3, 3)` | 1 | 73.7K |
| [lllyasviel/flux1_dev](https://huggingface.co/lllyasviel/flux1_dev) | `flux1-dev-fp8.safetensors` | FP32 | `(512)` | 103 | 52.7K |
| [lllyasviel/flux1_dev](https://huggingface.co/lllyasviel/flux1_dev) | `flux1-dev-fp8.safetensors` | FP32 | `(128, 256, 1, 1)` | 1 | 32.8K |
| [lllyasviel/flux1_dev](https://huggingface.co/lllyasviel/flux1_dev) | `flux1-dev-fp8.safetensors` | FP32 | `(256, 128, 1, 1)` | 1 | 32.8K |
| [lllyasviel/flux1_dev](https://huggingface.co/lllyasviel/flux1_dev) | `flux1-dev-fp8.safetensors` | FP32 | `(256)` | 34 | 8.7K |
| [lllyasviel/flux1_dev](https://huggingface.co/lllyasviel/flux1_dev) | `flux1-dev-fp8.safetensors` | FP32 | `(128)` | 35 | 4.5K |
| [lllyasviel/flux1_dev](https://huggingface.co/lllyasviel/flux1_dev) | `flux1-dev-fp8.safetensors` | FP32 | `(128, 3, 3, 3)` | 1 | 3.5K |
| [lllyasviel/flux1_dev](https://huggingface.co/lllyasviel/flux1_dev) | `flux1-dev-fp8.safetensors` | FP32 | `(3, 128, 3, 3)` | 1 | 3.5K |
| [lllyasviel/flux1_dev](https://huggingface.co/lllyasviel/flux1_dev) | `flux1-dev-fp8.safetensors` | FP32 | `(32)` | 1 | 32 |
| [lllyasviel/flux1_dev](https://huggingface.co/lllyasviel/flux1_dev) | `flux1-dev-fp8.safetensors` | FP32 | `(3)` | 1 | 3 |
| [lllyasviel/flux1_dev](https://huggingface.co/lllyasviel/flux1_dev) | `flux1-dev-fp8.safetensors` | FP32 | `()` | 2 | 2 |
| [lllyasviel/flux1_dev](https://huggingface.co/lllyasviel/flux1_dev) | `flux1-dev-fp8.safetensors` | FP8 (E4M3FN) | `(21504, 3072)` | 38 | 2.51B |
| [lllyasviel/flux1_dev](https://huggingface.co/lllyasviel/flux1_dev) | `flux1-dev-fp8.safetensors` | FP8 (E4M3FN) | `(18432, 3072)` | 38 | 2.15B |
| [lllyasviel/flux1_dev](https://huggingface.co/lllyasviel/flux1_dev) | `flux1-dev-fp8.safetensors` | FP8 (E4M3FN) | `(9216, 3072)` | 76 | 2.15B |
| [lllyasviel/flux1_dev](https://huggingface.co/lllyasviel/flux1_dev) | `flux1-dev-fp8.safetensors` | FP8 (E4M3FN) | `(10240, 4096)` | 48 | 2.01B |
| [lllyasviel/flux1_dev](https://huggingface.co/lllyasviel/flux1_dev) | `flux1-dev-fp8.safetensors` | FP8 (E4M3FN) | `(3072, 15360)` | 38 | 1.79B |
| [lllyasviel/flux1_dev](https://huggingface.co/lllyasviel/flux1_dev) | `flux1-dev-fp8.safetensors` | FP8 (E4M3FN) | `(4096, 4096)` | 96 | 1.61B |
| [lllyasviel/flux1_dev](https://huggingface.co/lllyasviel/flux1_dev) | `flux1-dev-fp8.safetensors` | FP8 (E4M3FN) | `(12288, 3072)` | 38 | 1.43B |
| [lllyasviel/flux1_dev](https://huggingface.co/lllyasviel/flux1_dev) | `flux1-dev-fp8.safetensors` | FP8 (E4M3FN) | `(3072, 12288)` | 38 | 1.43B |
| [lllyasviel/flux1_dev](https://huggingface.co/lllyasviel/flux1_dev) | `flux1-dev-fp8.safetensors` | FP8 (E4M3FN) | `(4096, 10240)` | 24 | 1.01B |
| [lllyasviel/flux1_dev](https://huggingface.co/lllyasviel/flux1_dev) | `flux1-dev-fp8.safetensors` | FP8 (E4M3FN) | `(3072, 3072)` | 41 | 386.9M |
| [lllyasviel/flux1_dev](https://huggingface.co/lllyasviel/flux1_dev) | `flux1-dev-fp8.safetensors` | FP8 (E4M3FN) | `(32128, 4096)` | 1 | 131.6M |
| [lllyasviel/flux1_dev](https://huggingface.co/lllyasviel/flux1_dev) | `flux1-dev-fp8.safetensors` | FP8 (E4M3FN) | `(6144, 3072)` | 1 | 18.9M |
| [lllyasviel/flux1_dev](https://huggingface.co/lllyasviel/flux1_dev) | `flux1-dev-fp8.safetensors` | FP8 (E4M3FN) | `(3072, 4096)` | 1 | 12.6M |
| [lllyasviel/flux1_dev](https://huggingface.co/lllyasviel/flux1_dev) | `flux1-dev-fp8.safetensors` | FP8 (E4M3FN) | `(3072, 768)` | 1 | 2.4M |
| [lllyasviel/flux1_dev](https://huggingface.co/lllyasviel/flux1_dev) | `flux1-dev-fp8.safetensors` | FP8 (E4M3FN) | `(3072, 256)` | 2 | 1.6M |
| [lllyasviel/flux1_dev](https://huggingface.co/lllyasviel/flux1_dev) | `flux1-dev-fp8.safetensors` | FP8 (E4M3FN) | `(21504)` | 38 | 817.2K |
| [lllyasviel/flux1_dev](https://huggingface.co/lllyasviel/flux1_dev) | `flux1-dev-fp8.safetensors` | FP8 (E4M3FN) | `(18432)` | 38 | 700.4K |
| [lllyasviel/flux1_dev](https://huggingface.co/lllyasviel/flux1_dev) | `flux1-dev-fp8.safetensors` | FP8 (E4M3FN) | `(9216)` | 76 | 700.4K |
| [lllyasviel/flux1_dev](https://huggingface.co/lllyasviel/flux1_dev) | `flux1-dev-fp8.safetensors` | FP8 (E4M3FN) | `(12288)` | 38 | 466.9K |
| [lllyasviel/flux1_dev](https://huggingface.co/lllyasviel/flux1_dev) | `flux1-dev-fp8.safetensors` | FP8 (E4M3FN) | `(3072)` | 122 | 374.8K |
| [lllyasviel/flux1_dev](https://huggingface.co/lllyasviel/flux1_dev) | `flux1-dev-fp8.safetensors` | FP8 (E4M3FN) | `(4096)` | 49 | 200.7K |
| [lllyasviel/flux1_dev](https://huggingface.co/lllyasviel/flux1_dev) | `flux1-dev-fp8.safetensors` | FP8 (E4M3FN) | `(3072, 64)` | 1 | 196.6K |
| [lllyasviel/flux1_dev](https://huggingface.co/lllyasviel/flux1_dev) | `flux1-dev-fp8.safetensors` | FP8 (E4M3FN) | `(64, 3072)` | 1 | 196.6K |
| [lllyasviel/flux1_dev](https://huggingface.co/lllyasviel/flux1_dev) | `flux1-dev-fp8.safetensors` | FP8 (E4M3FN) | `(128)` | 152 | 19.5K |
| [lllyasviel/flux1_dev](https://huggingface.co/lllyasviel/flux1_dev) | `flux1-dev-fp8.safetensors` | FP8 (E4M3FN) | `(6144)` | 1 | 6.1K |
| [lllyasviel/flux1_dev](https://huggingface.co/lllyasviel/flux1_dev) | `flux1-dev-fp8.safetensors` | FP8 (E4M3FN) | `(32, 64)` | 1 | 2.0K |
| [lllyasviel/flux1_dev](https://huggingface.co/lllyasviel/flux1_dev) | `flux1-dev-fp8.safetensors` | FP8 (E4M3FN) | `(64)` | 1 | 64 |
| [lllyasviel/flux_redux_bfl](https://huggingface.co/lllyasviel/flux_redux_bfl) | `image_encoder/model.safetensors` | BF16 | `(1152, 1152)` | 109 | 144.7M |
| [lllyasviel/flux_redux_bfl](https://huggingface.co/lllyasviel/flux_redux_bfl) | `image_encoder/model.safetensors` | BF16 | `(1152, 4304)` | 28 | 138.8M |
| [lllyasviel/flux_redux_bfl](https://huggingface.co/lllyasviel/flux_redux_bfl) | `image_encoder/model.safetensors` | BF16 | `(4304, 1152)` | 28 | 138.8M |
| [lllyasviel/flux_redux_bfl](https://huggingface.co/lllyasviel/flux_redux_bfl) | `image_embedder/diffusion_pytorch_model.safetensors` | BF16 | `(4096, 12288)` | 1 | 50.3M |
| [lllyasviel/flux_redux_bfl](https://huggingface.co/lllyasviel/flux_redux_bfl) | `image_embedder/diffusion_pytorch_model.safetensors` | BF16 | `(12288, 1152)` | 1 | 14.2M |
| [lllyasviel/flux_redux_bfl](https://huggingface.co/lllyasviel/flux_redux_bfl) | `image_encoder/model.safetensors` | BF16 | `(3456, 1152)` | 1 | 4.0M |
| [lllyasviel/flux_redux_bfl](https://huggingface.co/lllyasviel/flux_redux_bfl) | `image_encoder/model.safetensors` | BF16 | `(729, 1152)` | 1 | 839.8K |
| [lllyasviel/flux_redux_bfl](https://huggingface.co/lllyasviel/flux_redux_bfl) | `image_encoder/model.safetensors` | BF16 | `(1152, 3, 14, 14)` | 1 | 677.4K |
| [lllyasviel/flux_redux_bfl](https://huggingface.co/lllyasviel/flux_redux_bfl) | `image_encoder/model.safetensors` | BF16 | `(1152)` | 250 | 288.0K |
| [lllyasviel/flux_redux_bfl](https://huggingface.co/lllyasviel/flux_redux_bfl) | `image_encoder/model.safetensors` | BF16 | `(4304)` | 28 | 120.5K |
| [lllyasviel/flux_redux_bfl](https://huggingface.co/lllyasviel/flux_redux_bfl) | `image_embedder/diffusion_pytorch_model.safetensors` | BF16 | `(12288)` | 1 | 12.3K |
| [lllyasviel/flux_redux_bfl](https://huggingface.co/lllyasviel/flux_redux_bfl) | `image_embedder/diffusion_pytorch_model.safetensors` | BF16 | `(4096)` | 1 | 4.1K |
| [lllyasviel/flux_redux_bfl](https://huggingface.co/lllyasviel/flux_redux_bfl) | `image_encoder/model.safetensors` | BF16 | `(3456)` | 1 | 3.5K |
| [lllyasviel/flux_redux_bfl](https://huggingface.co/lllyasviel/flux_redux_bfl) | `image_encoder/model.safetensors` | BF16 | `(1, 1, 1152)` | 1 | 1.2K |
| [lllyasviel/FramePack_F1_I2V_HY_20250503](https://huggingface.co/lllyasviel/FramePack_F1_I2V_HY_20250503) | `diffusion_pytorch_model-00001-of-00003.safetensors` | BF16 | `(18432, 3072)` | 28 | 1.59B |
| [lllyasviel/FramePack_F1_I2V_HY_20250503](https://huggingface.co/lllyasviel/FramePack_F1_I2V_HY_20250503) | `diffusion_pytorch_model-00002-of-00003.safetensors` | BF16 | `(12288, 3072)` | 33 | 1.25B |
| [lllyasviel/FramePack_F1_I2V_HY_20250503](https://huggingface.co/lllyasviel/FramePack_F1_I2V_HY_20250503) | `diffusion_pytorch_model-00001-of-00003.safetensors` | BF16 | `(3072, 3072)` | 125 | 1.18B |
| [lllyasviel/FramePack_F1_I2V_HY_20250503](https://huggingface.co/lllyasviel/FramePack_F1_I2V_HY_20250503) | `diffusion_pytorch_model-00001-of-00003.safetensors` | BF16 | `(12288, 3072)` | 29 | 1.09B |
| [lllyasviel/FramePack_F1_I2V_HY_20250503](https://huggingface.co/lllyasviel/FramePack_F1_I2V_HY_20250503) | `diffusion_pytorch_model-00001-of-00003.safetensors` | BF16 | `(3072, 12288)` | 28 | 1.06B |
| [lllyasviel/FramePack_F1_I2V_HY_20250503](https://huggingface.co/lllyasviel/FramePack_F1_I2V_HY_20250503) | `diffusion_pytorch_model-00002-of-00003.safetensors` | BF16 | `(3072, 3072)` | 109 | 1.03B |
| [lllyasviel/FramePack_F1_I2V_HY_20250503](https://huggingface.co/lllyasviel/FramePack_F1_I2V_HY_20250503) | `diffusion_pytorch_model-00002-of-00003.safetensors` | BF16 | `(3072, 15360)` | 20 | 943.7M |
| [lllyasviel/FramePack_F1_I2V_HY_20250503](https://huggingface.co/lllyasviel/FramePack_F1_I2V_HY_20250503) | `diffusion_pytorch_model-00003-of-00003.safetensors` | BF16 | `(3072, 15360)` | 20 | 943.7M |
| [lllyasviel/FramePack_F1_I2V_HY_20250503](https://huggingface.co/lllyasviel/FramePack_F1_I2V_HY_20250503) | `diffusion_pytorch_model-00003-of-00003.safetensors` | BF16 | `(12288, 3072)` | 20 | 755.0M |
| [lllyasviel/FramePack_F1_I2V_HY_20250503](https://huggingface.co/lllyasviel/FramePack_F1_I2V_HY_20250503) | `diffusion_pytorch_model-00002-of-00003.safetensors` | BF16 | `(18432, 3072)` | 12 | 679.5M |
| [lllyasviel/FramePack_F1_I2V_HY_20250503](https://huggingface.co/lllyasviel/FramePack_F1_I2V_HY_20250503) | `diffusion_pytorch_model-00002-of-00003.safetensors` | BF16 | `(9216, 3072)` | 20 | 566.2M |
| [lllyasviel/FramePack_F1_I2V_HY_20250503](https://huggingface.co/lllyasviel/FramePack_F1_I2V_HY_20250503) | `diffusion_pytorch_model-00003-of-00003.safetensors` | BF16 | `(9216, 3072)` | 20 | 566.2M |
| [lllyasviel/FramePack_F1_I2V_HY_20250503](https://huggingface.co/lllyasviel/FramePack_F1_I2V_HY_20250503) | `diffusion_pytorch_model-00003-of-00003.safetensors` | BF16 | `(3072, 3072)` | 59 | 556.8M |
| [lllyasviel/FramePack_F1_I2V_HY_20250503](https://huggingface.co/lllyasviel/FramePack_F1_I2V_HY_20250503) | `diffusion_pytorch_model-00002-of-00003.safetensors` | BF16 | `(3072, 12288)` | 14 | 528.5M |
| [lllyasviel/FramePack_F1_I2V_HY_20250503](https://huggingface.co/lllyasviel/FramePack_F1_I2V_HY_20250503) | `diffusion_pytorch_model-00001-of-00003.safetensors` | BF16 | `(6144, 3072)` | 2 | 37.7M |
| [lllyasviel/FramePack_F1_I2V_HY_20250503](https://huggingface.co/lllyasviel/FramePack_F1_I2V_HY_20250503) | `diffusion_pytorch_model-00003-of-00003.safetensors` | BF16 | `(3072, 9216)` | 1 | 28.3M |
| [lllyasviel/FramePack_F1_I2V_HY_20250503](https://huggingface.co/lllyasviel/FramePack_F1_I2V_HY_20250503) | `diffusion_pytorch_model-00001-of-00003.safetensors` | BF16 | `(3072, 4096)` | 2 | 25.2M |
| [lllyasviel/FramePack_F1_I2V_HY_20250503](https://huggingface.co/lllyasviel/FramePack_F1_I2V_HY_20250503) | `diffusion_pytorch_model-00003-of-00003.safetensors` | BF16 | `(6144, 3072)` | 1 | 18.9M |
| [lllyasviel/FramePack_F1_I2V_HY_20250503](https://huggingface.co/lllyasviel/FramePack_F1_I2V_HY_20250503) | `diffusion_pytorch_model-00003-of-00003.safetensors` | BF16 | `(3072, 16, 4, 8, 8)` | 1 | 12.6M |
| [lllyasviel/FramePack_F1_I2V_HY_20250503](https://huggingface.co/lllyasviel/FramePack_F1_I2V_HY_20250503) | `diffusion_pytorch_model-00003-of-00003.safetensors` | BF16 | `(9216, 1152)` | 1 | 10.6M |
| [lllyasviel/FramePack_F1_I2V_HY_20250503](https://huggingface.co/lllyasviel/FramePack_F1_I2V_HY_20250503) | `diffusion_pytorch_model-00001-of-00003.safetensors` | BF16 | `(3072, 256)` | 3 | 2.4M |
| [lllyasviel/FramePack_F1_I2V_HY_20250503](https://huggingface.co/lllyasviel/FramePack_F1_I2V_HY_20250503) | `diffusion_pytorch_model-00001-of-00003.safetensors` | BF16 | `(3072, 768)` | 1 | 2.4M |
| [lllyasviel/FramePack_F1_I2V_HY_20250503](https://huggingface.co/lllyasviel/FramePack_F1_I2V_HY_20250503) | `diffusion_pytorch_model-00003-of-00003.safetensors` | BF16 | `(3072, 16, 2, 4, 4)` | 1 | 1.6M |
| [lllyasviel/FramePack_F1_I2V_HY_20250503](https://huggingface.co/lllyasviel/FramePack_F1_I2V_HY_20250503) | `diffusion_pytorch_model-00001-of-00003.safetensors` | BF16 | `(18432)` | 28 | 516.1K |
| [lllyasviel/FramePack_F1_I2V_HY_20250503](https://huggingface.co/lllyasviel/FramePack_F1_I2V_HY_20250503) | `diffusion_pytorch_model-00001-of-00003.safetensors` | BF16 | `(3072)` | 168 | 516.1K |
| [lllyasviel/FramePack_F1_I2V_HY_20250503](https://huggingface.co/lllyasviel/FramePack_F1_I2V_HY_20250503) | `diffusion_pytorch_model-00002-of-00003.safetensors` | BF16 | `(3072)` | 143 | 439.3K |
| [lllyasviel/FramePack_F1_I2V_HY_20250503](https://huggingface.co/lllyasviel/FramePack_F1_I2V_HY_20250503) | `diffusion_pytorch_model-00002-of-00003.safetensors` | BF16 | `(12288)` | 33 | 405.5K |
| [lllyasviel/FramePack_F1_I2V_HY_20250503](https://huggingface.co/lllyasviel/FramePack_F1_I2V_HY_20250503) | `diffusion_pytorch_model-00001-of-00003.safetensors` | BF16 | `(12288)` | 29 | 356.4K |
| [lllyasviel/FramePack_F1_I2V_HY_20250503](https://huggingface.co/lllyasviel/FramePack_F1_I2V_HY_20250503) | `diffusion_pytorch_model-00003-of-00003.safetensors` | BF16 | `(3072)` | 83 | 255.0K |
| [lllyasviel/FramePack_F1_I2V_HY_20250503](https://huggingface.co/lllyasviel/FramePack_F1_I2V_HY_20250503) | `diffusion_pytorch_model-00003-of-00003.safetensors` | BF16 | `(12288)` | 20 | 245.8K |
| [lllyasviel/FramePack_F1_I2V_HY_20250503](https://huggingface.co/lllyasviel/FramePack_F1_I2V_HY_20250503) | `diffusion_pytorch_model-00002-of-00003.safetensors` | BF16 | `(18432)` | 12 | 221.2K |
| [lllyasviel/FramePack_F1_I2V_HY_20250503](https://huggingface.co/lllyasviel/FramePack_F1_I2V_HY_20250503) | `diffusion_pytorch_model-00001-of-00003.safetensors` | BF16 | `(3072, 16, 1, 2, 2)` | 1 | 196.6K |
| [lllyasviel/FramePack_F1_I2V_HY_20250503](https://huggingface.co/lllyasviel/FramePack_F1_I2V_HY_20250503) | `diffusion_pytorch_model-00003-of-00003.safetensors` | BF16 | `(3072, 16, 1, 2, 2)` | 1 | 196.6K |
| [lllyasviel/FramePack_F1_I2V_HY_20250503](https://huggingface.co/lllyasviel/FramePack_F1_I2V_HY_20250503) | `diffusion_pytorch_model-00003-of-00003.safetensors` | BF16 | `(64, 3072)` | 1 | 196.6K |
| [lllyasviel/FramePack_F1_I2V_HY_20250503](https://huggingface.co/lllyasviel/FramePack_F1_I2V_HY_20250503) | `diffusion_pytorch_model-00003-of-00003.safetensors` | BF16 | `(9216)` | 21 | 193.5K |
| [lllyasviel/FramePack_F1_I2V_HY_20250503](https://huggingface.co/lllyasviel/FramePack_F1_I2V_HY_20250503) | `diffusion_pytorch_model-00002-of-00003.safetensors` | BF16 | `(9216)` | 20 | 184.3K |
| [lllyasviel/FramePack_F1_I2V_HY_20250503](https://huggingface.co/lllyasviel/FramePack_F1_I2V_HY_20250503) | `diffusion_pytorch_model-00001-of-00003.safetensors` | BF16 | `(6144)` | 2 | 12.3K |
| [lllyasviel/FramePack_F1_I2V_HY_20250503](https://huggingface.co/lllyasviel/FramePack_F1_I2V_HY_20250503) | `diffusion_pytorch_model-00002-of-00003.safetensors` | BF16 | `(128)` | 66 | 8.4K |
| [lllyasviel/FramePack_F1_I2V_HY_20250503](https://huggingface.co/lllyasviel/FramePack_F1_I2V_HY_20250503) | `diffusion_pytorch_model-00001-of-00003.safetensors` | BF16 | `(128)` | 56 | 7.2K |
| [lllyasviel/FramePack_F1_I2V_HY_20250503](https://huggingface.co/lllyasviel/FramePack_F1_I2V_HY_20250503) | `diffusion_pytorch_model-00003-of-00003.safetensors` | BF16 | `(6144)` | 1 | 6.1K |
| [lllyasviel/FramePack_F1_I2V_HY_20250503](https://huggingface.co/lllyasviel/FramePack_F1_I2V_HY_20250503) | `diffusion_pytorch_model-00003-of-00003.safetensors` | BF16 | `(128)` | 38 | 4.9K |
| [lllyasviel/FramePack_F1_I2V_HY_20250503](https://huggingface.co/lllyasviel/FramePack_F1_I2V_HY_20250503) | `diffusion_pytorch_model-00003-of-00003.safetensors` | BF16 | `(64)` | 1 | 64 |
| [lllyasviel/FramePackI2V_HY](https://huggingface.co/lllyasviel/FramePackI2V_HY) | `diffusion_pytorch_model-00001-of-00003.safetensors` | BF16 | `(18432, 3072)` | 28 | 1.59B |
| [lllyasviel/FramePackI2V_HY](https://huggingface.co/lllyasviel/FramePackI2V_HY) | `diffusion_pytorch_model-00002-of-00003.safetensors` | BF16 | `(12288, 3072)` | 33 | 1.25B |
| [lllyasviel/FramePackI2V_HY](https://huggingface.co/lllyasviel/FramePackI2V_HY) | `diffusion_pytorch_model-00001-of-00003.safetensors` | BF16 | `(3072, 3072)` | 125 | 1.18B |
| [lllyasviel/FramePackI2V_HY](https://huggingface.co/lllyasviel/FramePackI2V_HY) | `diffusion_pytorch_model-00001-of-00003.safetensors` | BF16 | `(12288, 3072)` | 29 | 1.09B |
| [lllyasviel/FramePackI2V_HY](https://huggingface.co/lllyasviel/FramePackI2V_HY) | `diffusion_pytorch_model-00001-of-00003.safetensors` | BF16 | `(3072, 12288)` | 28 | 1.06B |
| [lllyasviel/FramePackI2V_HY](https://huggingface.co/lllyasviel/FramePackI2V_HY) | `diffusion_pytorch_model-00002-of-00003.safetensors` | BF16 | `(3072, 3072)` | 109 | 1.03B |
| [lllyasviel/FramePackI2V_HY](https://huggingface.co/lllyasviel/FramePackI2V_HY) | `diffusion_pytorch_model-00002-of-00003.safetensors` | BF16 | `(3072, 15360)` | 20 | 943.7M |
| [lllyasviel/FramePackI2V_HY](https://huggingface.co/lllyasviel/FramePackI2V_HY) | `diffusion_pytorch_model-00003-of-00003.safetensors` | BF16 | `(3072, 15360)` | 20 | 943.7M |
| [lllyasviel/FramePackI2V_HY](https://huggingface.co/lllyasviel/FramePackI2V_HY) | `diffusion_pytorch_model-00003-of-00003.safetensors` | BF16 | `(12288, 3072)` | 20 | 755.0M |
| [lllyasviel/FramePackI2V_HY](https://huggingface.co/lllyasviel/FramePackI2V_HY) | `diffusion_pytorch_model-00002-of-00003.safetensors` | BF16 | `(18432, 3072)` | 12 | 679.5M |
| [lllyasviel/FramePackI2V_HY](https://huggingface.co/lllyasviel/FramePackI2V_HY) | `diffusion_pytorch_model-00002-of-00003.safetensors` | BF16 | `(9216, 3072)` | 20 | 566.2M |
| [lllyasviel/FramePackI2V_HY](https://huggingface.co/lllyasviel/FramePackI2V_HY) | `diffusion_pytorch_model-00003-of-00003.safetensors` | BF16 | `(9216, 3072)` | 20 | 566.2M |
| [lllyasviel/FramePackI2V_HY](https://huggingface.co/lllyasviel/FramePackI2V_HY) | `diffusion_pytorch_model-00003-of-00003.safetensors` | BF16 | `(3072, 3072)` | 59 | 556.8M |
| [lllyasviel/FramePackI2V_HY](https://huggingface.co/lllyasviel/FramePackI2V_HY) | `diffusion_pytorch_model-00002-of-00003.safetensors` | BF16 | `(3072, 12288)` | 14 | 528.5M |
| [lllyasviel/FramePackI2V_HY](https://huggingface.co/lllyasviel/FramePackI2V_HY) | `diffusion_pytorch_model-00001-of-00003.safetensors` | BF16 | `(6144, 3072)` | 2 | 37.7M |
| [lllyasviel/FramePackI2V_HY](https://huggingface.co/lllyasviel/FramePackI2V_HY) | `diffusion_pytorch_model-00003-of-00003.safetensors` | BF16 | `(3072, 9216)` | 1 | 28.3M |
| [lllyasviel/FramePackI2V_HY](https://huggingface.co/lllyasviel/FramePackI2V_HY) | `diffusion_pytorch_model-00001-of-00003.safetensors` | BF16 | `(3072, 4096)` | 2 | 25.2M |
| [lllyasviel/FramePackI2V_HY](https://huggingface.co/lllyasviel/FramePackI2V_HY) | `diffusion_pytorch_model-00003-of-00003.safetensors` | BF16 | `(6144, 3072)` | 1 | 18.9M |
| [lllyasviel/FramePackI2V_HY](https://huggingface.co/lllyasviel/FramePackI2V_HY) | `diffusion_pytorch_model-00003-of-00003.safetensors` | BF16 | `(3072, 16, 4, 8, 8)` | 1 | 12.6M |
| [lllyasviel/FramePackI2V_HY](https://huggingface.co/lllyasviel/FramePackI2V_HY) | `diffusion_pytorch_model-00003-of-00003.safetensors` | BF16 | `(9216, 1152)` | 1 | 10.6M |
| [lllyasviel/FramePackI2V_HY](https://huggingface.co/lllyasviel/FramePackI2V_HY) | `diffusion_pytorch_model-00001-of-00003.safetensors` | BF16 | `(3072, 256)` | 3 | 2.4M |
| [lllyasviel/FramePackI2V_HY](https://huggingface.co/lllyasviel/FramePackI2V_HY) | `diffusion_pytorch_model-00001-of-00003.safetensors` | BF16 | `(3072, 768)` | 1 | 2.4M |
| [lllyasviel/FramePackI2V_HY](https://huggingface.co/lllyasviel/FramePackI2V_HY) | `diffusion_pytorch_model-00003-of-00003.safetensors` | BF16 | `(3072, 16, 2, 4, 4)` | 1 | 1.6M |
| [lllyasviel/FramePackI2V_HY](https://huggingface.co/lllyasviel/FramePackI2V_HY) | `diffusion_pytorch_model-00001-of-00003.safetensors` | BF16 | `(18432)` | 28 | 516.1K |
| [lllyasviel/FramePackI2V_HY](https://huggingface.co/lllyasviel/FramePackI2V_HY) | `diffusion_pytorch_model-00001-of-00003.safetensors` | BF16 | `(3072)` | 168 | 516.1K |
| [lllyasviel/FramePackI2V_HY](https://huggingface.co/lllyasviel/FramePackI2V_HY) | `diffusion_pytorch_model-00002-of-00003.safetensors` | BF16 | `(3072)` | 143 | 439.3K |
| [lllyasviel/FramePackI2V_HY](https://huggingface.co/lllyasviel/FramePackI2V_HY) | `diffusion_pytorch_model-00002-of-00003.safetensors` | BF16 | `(12288)` | 33 | 405.5K |
| [lllyasviel/FramePackI2V_HY](https://huggingface.co/lllyasviel/FramePackI2V_HY) | `diffusion_pytorch_model-00001-of-00003.safetensors` | BF16 | `(12288)` | 29 | 356.4K |
| [lllyasviel/FramePackI2V_HY](https://huggingface.co/lllyasviel/FramePackI2V_HY) | `diffusion_pytorch_model-00003-of-00003.safetensors` | BF16 | `(3072)` | 83 | 255.0K |
| [lllyasviel/FramePackI2V_HY](https://huggingface.co/lllyasviel/FramePackI2V_HY) | `diffusion_pytorch_model-00003-of-00003.safetensors` | BF16 | `(12288)` | 20 | 245.8K |
| [lllyasviel/FramePackI2V_HY](https://huggingface.co/lllyasviel/FramePackI2V_HY) | `diffusion_pytorch_model-00002-of-00003.safetensors` | BF16 | `(18432)` | 12 | 221.2K |
| [lllyasviel/FramePackI2V_HY](https://huggingface.co/lllyasviel/FramePackI2V_HY) | `diffusion_pytorch_model-00001-of-00003.safetensors` | BF16 | `(3072, 16, 1, 2, 2)` | 1 | 196.6K |
| [lllyasviel/FramePackI2V_HY](https://huggingface.co/lllyasviel/FramePackI2V_HY) | `diffusion_pytorch_model-00003-of-00003.safetensors` | BF16 | `(3072, 16, 1, 2, 2)` | 1 | 196.6K |
| [lllyasviel/FramePackI2V_HY](https://huggingface.co/lllyasviel/FramePackI2V_HY) | `diffusion_pytorch_model-00003-of-00003.safetensors` | BF16 | `(64, 3072)` | 1 | 196.6K |
| [lllyasviel/FramePackI2V_HY](https://huggingface.co/lllyasviel/FramePackI2V_HY) | `diffusion_pytorch_model-00003-of-00003.safetensors` | BF16 | `(9216)` | 21 | 193.5K |
| [lllyasviel/FramePackI2V_HY](https://huggingface.co/lllyasviel/FramePackI2V_HY) | `diffusion_pytorch_model-00002-of-00003.safetensors` | BF16 | `(9216)` | 20 | 184.3K |
| [lllyasviel/FramePackI2V_HY](https://huggingface.co/lllyasviel/FramePackI2V_HY) | `diffusion_pytorch_model-00001-of-00003.safetensors` | BF16 | `(6144)` | 2 | 12.3K |
| [lllyasviel/FramePackI2V_HY](https://huggingface.co/lllyasviel/FramePackI2V_HY) | `diffusion_pytorch_model-00002-of-00003.safetensors` | BF16 | `(128)` | 66 | 8.4K |
| [lllyasviel/FramePackI2V_HY](https://huggingface.co/lllyasviel/FramePackI2V_HY) | `diffusion_pytorch_model-00001-of-00003.safetensors` | BF16 | `(128)` | 56 | 7.2K |
| [lllyasviel/FramePackI2V_HY](https://huggingface.co/lllyasviel/FramePackI2V_HY) | `diffusion_pytorch_model-00003-of-00003.safetensors` | BF16 | `(6144)` | 1 | 6.1K |
| [lllyasviel/FramePackI2V_HY](https://huggingface.co/lllyasviel/FramePackI2V_HY) | `diffusion_pytorch_model-00003-of-00003.safetensors` | BF16 | `(128)` | 38 | 4.9K |
| [lllyasviel/FramePackI2V_HY](https://huggingface.co/lllyasviel/FramePackI2V_HY) | `diffusion_pytorch_model-00003-of-00003.safetensors` | BF16 | `(64)` | 1 | 64 |
| [madebyollin/taesd](https://huggingface.co/madebyollin/taesd) | `diffusion_pytorch_model.safetensors` | FP32 | `(64, 64, 3, 3)` | 66 | 2.4M |
| [madebyollin/taesd](https://huggingface.co/madebyollin/taesd) | `taesd_decoder.safetensors` | FP32 | `(64, 64, 3, 3)` | 33 | 1.2M |
| [madebyollin/taesd](https://huggingface.co/madebyollin/taesd) | `taesd_encoder.safetensors` | FP32 | `(64, 64, 3, 3)` | 33 | 1.2M |
| [madebyollin/taesd](https://huggingface.co/madebyollin/taesd) | `diffusion_pytorch_model.safetensors` | FP32 | `(64)` | 62 | 4.0K |
| [madebyollin/taesd](https://huggingface.co/madebyollin/taesd) | `diffusion_pytorch_model.safetensors` | FP32 | `(4, 64, 3, 3)` | 1 | 2.3K |
| [madebyollin/taesd](https://huggingface.co/madebyollin/taesd) | `taesd_encoder.safetensors` | FP32 | `(4, 64, 3, 3)` | 1 | 2.3K |
| [madebyollin/taesd](https://huggingface.co/madebyollin/taesd) | `diffusion_pytorch_model.safetensors` | FP32 | `(64, 4, 3, 3)` | 1 | 2.3K |
| [madebyollin/taesd](https://huggingface.co/madebyollin/taesd) | `taesd_decoder.safetensors` | FP32 | `(64, 4, 3, 3)` | 1 | 2.3K |
| [madebyollin/taesd](https://huggingface.co/madebyollin/taesd) | `taesd_decoder.safetensors` | FP32 | `(64)` | 31 | 2.0K |
| [madebyollin/taesd](https://huggingface.co/madebyollin/taesd) | `taesd_encoder.safetensors` | FP32 | `(64)` | 31 | 2.0K |
| [madebyollin/taesd](https://huggingface.co/madebyollin/taesd) | `diffusion_pytorch_model.safetensors` | FP32 | `(3, 64, 3, 3)` | 1 | 1.7K |
| [madebyollin/taesd](https://huggingface.co/madebyollin/taesd) | `taesd_decoder.safetensors` | FP32 | `(3, 64, 3, 3)` | 1 | 1.7K |
| [madebyollin/taesd](https://huggingface.co/madebyollin/taesd) | `diffusion_pytorch_model.safetensors` | FP32 | `(64, 3, 3, 3)` | 1 | 1.7K |
| [madebyollin/taesd](https://huggingface.co/madebyollin/taesd) | `taesd_encoder.safetensors` | FP32 | `(64, 3, 3, 3)` | 1 | 1.7K |
| [madebyollin/taesd](https://huggingface.co/madebyollin/taesd) | `diffusion_pytorch_model.safetensors` | FP32 | `(4)` | 1 | 4 |
| [madebyollin/taesd](https://huggingface.co/madebyollin/taesd) | `taesd_encoder.safetensors` | FP32 | `(4)` | 1 | 4 |
| [madebyollin/taesd](https://huggingface.co/madebyollin/taesd) | `diffusion_pytorch_model.safetensors` | FP32 | `(3)` | 1 | 3 |
| [madebyollin/taesd](https://huggingface.co/madebyollin/taesd) | `taesd_decoder.safetensors` | FP32 | `(3)` | 1 | 3 |
| [microsoft/OmniParser](https://huggingface.co/microsoft/OmniParser) | `icon_detect/model.safetensors` | FP16 | `(128, 128, 3, 3)` | 5 | 737.3K |
| [microsoft/OmniParser](https://huggingface.co/microsoft/OmniParser) | `icon_detect/model.safetensors` | FP16 | `(64, 64, 3, 3)` | 17 | 626.7K |
| [microsoft/OmniParser](https://huggingface.co/microsoft/OmniParser) | `icon_detect/model.safetensors` | FP16 | `(256, 128, 3, 3)` | 1 | 294.9K |
| [microsoft/OmniParser](https://huggingface.co/microsoft/OmniParser) | `icon_detect/model.safetensors` | FP16 | `(256, 384, 1, 1)` | 3 | 294.9K |
| [microsoft/OmniParser](https://huggingface.co/microsoft/OmniParser) | `icon_detect/model.safetensors` | FP16 | `(64, 256, 3, 3)` | 2 | 294.9K |
| [microsoft/OmniParser](https://huggingface.co/microsoft/OmniParser) | `icon_detect/model.safetensors` | FP16 | `(64, 128, 3, 3)` | 2 | 147.5K |
| [microsoft/OmniParser](https://huggingface.co/microsoft/OmniParser) | `icon_detect/model.safetensors` | FP16 | `(256, 512, 1, 1)` | 1 | 131.1K |
| [microsoft/OmniParser](https://huggingface.co/microsoft/OmniParser) | `icon_detect/model.safetensors` | FP16 | `(128, 192, 1, 1)` | 3 | 73.7K |
| [microsoft/OmniParser](https://huggingface.co/microsoft/OmniParser) | `icon_detect/model.safetensors` | FP16 | `(128, 64, 3, 3)` | 1 | 73.7K |
| [microsoft/OmniParser](https://huggingface.co/microsoft/OmniParser) | `icon_detect/model.safetensors` | FP16 | `(128, 256, 1, 1)` | 2 | 65.5K |
| [microsoft/OmniParser](https://huggingface.co/microsoft/OmniParser) | `icon_detect/model.safetensors` | FP16 | `(256, 256, 1, 1)` | 1 | 65.5K |
| [microsoft/OmniParser](https://huggingface.co/microsoft/OmniParser) | `icon_detect/model.safetensors` | FP16 | `(32, 32, 3, 3)` | 6 | 55.3K |
| [microsoft/OmniParser](https://huggingface.co/microsoft/OmniParser) | `icon_detect/model.safetensors` | FP16 | `(128, 384, 1, 1)` | 1 | 49.2K |
| [microsoft/OmniParser](https://huggingface.co/microsoft/OmniParser) | `icon_detect/model.safetensors` | FP16 | `(64, 32, 3, 3)` | 1 | 18.4K |
| [microsoft/OmniParser](https://huggingface.co/microsoft/OmniParser) | `icon_detect/model.safetensors` | FP16 | `(128, 128, 1, 1)` | 1 | 16.4K |
| [microsoft/OmniParser](https://huggingface.co/microsoft/OmniParser) | `icon_detect/model.safetensors` | FP16 | `(64, 64, 1, 1)` | 4 | 16.4K |
| [microsoft/OmniParser](https://huggingface.co/microsoft/OmniParser) | `icon_detect/model.safetensors` | FP16 | `(64, 192, 1, 1)` | 1 | 12.3K |
| [microsoft/OmniParser](https://huggingface.co/microsoft/OmniParser) | `icon_detect/model.safetensors` | FP16 | `(64, 128, 1, 1)` | 1 | 8.2K |
| [microsoft/OmniParser](https://huggingface.co/microsoft/OmniParser) | `icon_detect/model.safetensors` | FP16 | `(64)` | 107 | 6.8K |
| [microsoft/OmniParser](https://huggingface.co/microsoft/OmniParser) | `icon_detect/model.safetensors` | FP16 | `(128)` | 52 | 6.7K |
| [microsoft/OmniParser](https://huggingface.co/microsoft/OmniParser) | `icon_detect/model.safetensors` | FP16 | `(256)` | 24 | 6.1K |
| [microsoft/OmniParser](https://huggingface.co/microsoft/OmniParser) | `icon_detect/model.safetensors` | FP16 | `(64, 96, 1, 1)` | 1 | 6.1K |
| [microsoft/OmniParser](https://huggingface.co/microsoft/OmniParser) | `icon_detect/model.safetensors` | FP16 | `(16, 16, 3, 3)` | 2 | 4.6K |
| [microsoft/OmniParser](https://huggingface.co/microsoft/OmniParser) | `icon_detect/model.safetensors` | FP16 | `(32, 16, 3, 3)` | 1 | 4.6K |
| [microsoft/OmniParser](https://huggingface.co/microsoft/OmniParser) | `icon_detect/model.safetensors` | FP16 | `(32, 48, 1, 1)` | 1 | 1.5K |
| [microsoft/OmniParser](https://huggingface.co/microsoft/OmniParser) | `icon_detect/model.safetensors` | FP16 | `(32)` | 36 | 1.2K |
| [microsoft/OmniParser](https://huggingface.co/microsoft/OmniParser) | `icon_detect/model.safetensors` | FP16 | `(32, 32, 1, 1)` | 1 | 1.0K |
| [microsoft/OmniParser](https://huggingface.co/microsoft/OmniParser) | `icon_detect/model.safetensors` | FP16 | `(16, 3, 3, 3)` | 1 | 432 |
| [microsoft/OmniParser](https://huggingface.co/microsoft/OmniParser) | `icon_detect/model.safetensors` | FP16 | `(1, 64, 1, 1)` | 3 | 192 |
| [microsoft/OmniParser](https://huggingface.co/microsoft/OmniParser) | `icon_detect/model.safetensors` | FP16 | `(16)` | 12 | 192 |
| [microsoft/OmniParser](https://huggingface.co/microsoft/OmniParser) | `icon_detect/model.safetensors` | FP16 | `(1, 16, 1, 1)` | 1 | 16 |
| [microsoft/OmniParser](https://huggingface.co/microsoft/OmniParser) | `icon_detect/model.safetensors` | FP16 | `(1)` | 3 | 3 |
| [microsoft/OmniParser](https://huggingface.co/microsoft/OmniParser) | `icon_caption_florence/model.safetensors` | FP32 | `(51289, 768)` | 2 | 78.8M |
| [microsoft/OmniParser](https://huggingface.co/microsoft/OmniParser) | `icon_caption_florence/model.safetensors` | FP32 | `(768, 768)` | 72 | 42.5M |
| [microsoft/OmniParser](https://huggingface.co/microsoft/OmniParser) | `icon_caption_florence/model.safetensors` | FP32 | `(3072, 768)` | 12 | 28.3M |
| [microsoft/OmniParser](https://huggingface.co/microsoft/OmniParser) | `icon_caption_florence/model.safetensors` | FP32 | `(768, 3072)` | 12 | 28.3M |
| [microsoft/OmniParser](https://huggingface.co/microsoft/OmniParser) | `icon_caption_florence/model.safetensors` | FP32 | `(2048, 512)` | 18 | 18.9M |
| [microsoft/OmniParser](https://huggingface.co/microsoft/OmniParser) | `icon_caption_florence/model.safetensors` | FP32 | `(512, 2048)` | 18 | 18.9M |
| [microsoft/OmniParser](https://huggingface.co/microsoft/OmniParser) | `icon_caption_florence/model.safetensors` | FP32 | `(1536, 512)` | 18 | 14.2M |
| [microsoft/OmniParser](https://huggingface.co/microsoft/OmniParser) | `icon_caption_florence/model.safetensors` | FP32 | `(1024, 4096)` | 2 | 8.4M |
| [microsoft/OmniParser](https://huggingface.co/microsoft/OmniParser) | `icon_caption_florence/model.safetensors` | FP32 | `(4096, 1024)` | 2 | 8.4M |
| [microsoft/OmniParser](https://huggingface.co/microsoft/OmniParser) | `icon_caption_florence/model.safetensors` | FP32 | `(3072, 1024)` | 2 | 6.3M |
| [microsoft/OmniParser](https://huggingface.co/microsoft/OmniParser) | `icon_caption_florence/model.safetensors` | FP32 | `(1024, 512, 3, 3)` | 1 | 4.7M |
| [microsoft/OmniParser](https://huggingface.co/microsoft/OmniParser) | `icon_caption_florence/model.safetensors` | FP32 | `(512, 512)` | 18 | 4.7M |
| [microsoft/OmniParser](https://huggingface.co/microsoft/OmniParser) | `icon_caption_florence/model.safetensors` | FP32 | `(1024, 1024)` | 2 | 2.1M |
| [microsoft/OmniParser](https://huggingface.co/microsoft/OmniParser) | `icon_caption_florence/model.safetensors` | FP32 | `(1026, 768)` | 2 | 1.6M |
| [microsoft/OmniParser](https://huggingface.co/microsoft/OmniParser) | `icon_caption_florence/model.safetensors` | FP32 | `(512, 256, 3, 3)` | 1 | 1.2M |
| [microsoft/OmniParser](https://huggingface.co/microsoft/OmniParser) | `icon_caption_florence/model.safetensors` | FP32 | `(1024, 768)` | 1 | 786.4K |
| [microsoft/OmniParser](https://huggingface.co/microsoft/OmniParser) | `icon_caption_florence/model.safetensors` | FP32 | `(1024, 256)` | 2 | 524.3K |
| [microsoft/OmniParser](https://huggingface.co/microsoft/OmniParser) | `icon_caption_florence/model.safetensors` | FP32 | `(256, 1024)` | 2 | 524.3K |
| [microsoft/OmniParser](https://huggingface.co/microsoft/OmniParser) | `icon_caption_florence/model.safetensors` | FP32 | `(768, 256)` | 2 | 393.2K |
| [microsoft/OmniParser](https://huggingface.co/microsoft/OmniParser) | `icon_caption_florence/model.safetensors` | FP32 | `(256, 128, 3, 3)` | 1 | 294.9K |
| [microsoft/OmniParser](https://huggingface.co/microsoft/OmniParser) | `icon_caption_florence/model.safetensors` | FP32 | `(512, 1, 3, 3)` | 36 | 165.9K |
| [microsoft/OmniParser](https://huggingface.co/microsoft/OmniParser) | `icon_caption_florence/model.safetensors` | FP32 | `(128, 512)` | 2 | 131.1K |
| [microsoft/OmniParser](https://huggingface.co/microsoft/OmniParser) | `icon_caption_florence/model.safetensors` | FP32 | `(256, 256)` | 2 | 131.1K |
| [microsoft/OmniParser](https://huggingface.co/microsoft/OmniParser) | `icon_caption_florence/model.safetensors` | FP32 | `(512, 128)` | 2 | 131.1K |
| [microsoft/OmniParser](https://huggingface.co/microsoft/OmniParser) | `icon_caption_florence/model.safetensors` | FP32 | `(768)` | 152 | 116.7K |
| [microsoft/OmniParser](https://huggingface.co/microsoft/OmniParser) | `icon_caption_florence/model.safetensors` | FP32 | `(100, 1024)` | 1 | 102.4K |
| [microsoft/OmniParser](https://huggingface.co/microsoft/OmniParser) | `icon_caption_florence/model.safetensors` | FP32 | `(384, 128)` | 2 | 98.3K |
| [microsoft/OmniParser](https://huggingface.co/microsoft/OmniParser) | `icon_caption_florence/model.safetensors` | FP32 | `(512)` | 149 | 76.3K |
| [microsoft/OmniParser](https://huggingface.co/microsoft/OmniParser) | `icon_caption_florence/model.safetensors` | FP32 | `(1, 51289)` | 1 | 51.3K |
| [microsoft/OmniParser](https://huggingface.co/microsoft/OmniParser) | `icon_caption_florence/model.safetensors` | FP32 | `(50, 512)` | 2 | 51.2K |
| [microsoft/OmniParser](https://huggingface.co/microsoft/OmniParser) | `icon_caption_florence/model.safetensors` | FP32 | `(3072)` | 14 | 43.0K |
| [microsoft/OmniParser](https://huggingface.co/microsoft/OmniParser) | `icon_caption_florence/model.safetensors` | FP32 | `(1024, 1, 3, 3)` | 4 | 36.9K |
| [microsoft/OmniParser](https://huggingface.co/microsoft/OmniParser) | `icon_caption_florence/model.safetensors` | FP32 | `(2048)` | 18 | 36.9K |
| [microsoft/OmniParser](https://huggingface.co/microsoft/OmniParser) | `icon_caption_florence/model.safetensors` | FP32 | `(128, 128)` | 2 | 32.8K |
| [microsoft/OmniParser](https://huggingface.co/microsoft/OmniParser) | `icon_caption_florence/model.safetensors` | FP32 | `(1536)` | 18 | 27.6K |
| [microsoft/OmniParser](https://huggingface.co/microsoft/OmniParser) | `icon_caption_florence/model.safetensors` | FP32 | `(1024)` | 19 | 19.5K |
| [microsoft/OmniParser](https://huggingface.co/microsoft/OmniParser) | `icon_caption_florence/model.safetensors` | FP32 | `(128, 3, 7, 7)` | 1 | 18.8K |
| [microsoft/OmniParser](https://huggingface.co/microsoft/OmniParser) | `icon_caption_florence/model.safetensors` | FP32 | `(256, 1, 3, 3)` | 4 | 9.2K |
| [microsoft/OmniParser](https://huggingface.co/microsoft/OmniParser) | `icon_caption_florence/model.safetensors` | FP32 | `(4096)` | 2 | 8.2K |
| [microsoft/OmniParser](https://huggingface.co/microsoft/OmniParser) | `icon_caption_florence/model.safetensors` | FP32 | `(256)` | 19 | 4.9K |
| [microsoft/OmniParser](https://huggingface.co/microsoft/OmniParser) | `icon_caption_florence/model.safetensors` | FP32 | `(128, 1, 3, 3)` | 4 | 4.6K |
| [microsoft/OmniParser](https://huggingface.co/microsoft/OmniParser) | `icon_caption_florence/model.safetensors` | FP32 | `(128)` | 21 | 2.7K |
| [microsoft/OmniParser](https://huggingface.co/microsoft/OmniParser) | `icon_caption_florence/model.safetensors` | FP32 | `(384)` | 2 | 768 |
| [microsoft/OmniParser](https://huggingface.co/microsoft/OmniParser) | `icon_detect/model.safetensors` | INT64 | `()` | 57 | 57 |
| [microsoft/VibeVoice-Realtime-0.5B](https://huggingface.co/microsoft/VibeVoice-Realtime-0.5B) | `model.safetensors` | BF16 | `(151936, 896)` | 2 | 272.3M |
| [microsoft/VibeVoice-Realtime-0.5B](https://huggingface.co/microsoft/VibeVoice-Realtime-0.5B) | `model.safetensors` | BF16 | `(4864, 896)` | 48 | 209.2M |
| [microsoft/VibeVoice-Realtime-0.5B](https://huggingface.co/microsoft/VibeVoice-Realtime-0.5B) | `model.safetensors` | BF16 | `(2048, 8192)` | 8 | 134.2M |
| [microsoft/VibeVoice-Realtime-0.5B](https://huggingface.co/microsoft/VibeVoice-Realtime-0.5B) | `model.safetensors` | BF16 | `(8192, 2048)` | 8 | 134.2M |
| [microsoft/VibeVoice-Realtime-0.5B](https://huggingface.co/microsoft/VibeVoice-Realtime-0.5B) | `model.safetensors` | BF16 | `(896, 4864)` | 24 | 104.6M |
| [microsoft/VibeVoice-Realtime-0.5B](https://huggingface.co/microsoft/VibeVoice-Realtime-0.5B) | `model.safetensors` | BF16 | `(896, 896)` | 52 | 41.7M |
| [microsoft/VibeVoice-Realtime-0.5B](https://huggingface.co/microsoft/VibeVoice-Realtime-0.5B) | `model.safetensors` | BF16 | `(2048, 1024, 16)` | 1 | 33.6M |
| [microsoft/VibeVoice-Realtime-0.5B](https://huggingface.co/microsoft/VibeVoice-Realtime-0.5B) | `model.safetensors` | BF16 | `(2688, 896)` | 12 | 28.9M |
| [microsoft/VibeVoice-Realtime-0.5B](https://huggingface.co/microsoft/VibeVoice-Realtime-0.5B) | `model.safetensors` | BF16 | `(1024, 4096)` | 3 | 12.6M |
| [microsoft/VibeVoice-Realtime-0.5B](https://huggingface.co/microsoft/VibeVoice-Realtime-0.5B) | `model.safetensors` | BF16 | `(4096, 1024)` | 3 | 12.6M |
| [microsoft/VibeVoice-Realtime-0.5B](https://huggingface.co/microsoft/VibeVoice-Realtime-0.5B) | `model.safetensors` | BF16 | `(896, 2688)` | 4 | 9.6M |
| [microsoft/VibeVoice-Realtime-0.5B](https://huggingface.co/microsoft/VibeVoice-Realtime-0.5B) | `model.safetensors` | BF16 | `(128, 896)` | 48 | 5.5M |
| [microsoft/VibeVoice-Realtime-0.5B](https://huggingface.co/microsoft/VibeVoice-Realtime-0.5B) | `model.safetensors` | BF16 | `(1024, 512, 10)` | 1 | 5.2M |
| [microsoft/VibeVoice-Realtime-0.5B](https://huggingface.co/microsoft/VibeVoice-Realtime-0.5B) | `model.safetensors` | BF16 | `(2048, 512)` | 3 | 3.1M |
| [microsoft/VibeVoice-Realtime-0.5B](https://huggingface.co/microsoft/VibeVoice-Realtime-0.5B) | `model.safetensors` | BF16 | `(512, 2048)` | 3 | 3.1M |
| [microsoft/VibeVoice-Realtime-0.5B](https://huggingface.co/microsoft/VibeVoice-Realtime-0.5B) | `model.safetensors` | BF16 | `(1792, 896)` | 1 | 1.6M |
| [microsoft/VibeVoice-Realtime-0.5B](https://huggingface.co/microsoft/VibeVoice-Realtime-0.5B) | `model.safetensors` | BF16 | `(512, 256, 10)` | 1 | 1.3M |
| [microsoft/VibeVoice-Realtime-0.5B](https://huggingface.co/microsoft/VibeVoice-Realtime-0.5B) | `model.safetensors` | BF16 | `(2048, 64, 7)` | 1 | 917.5K |
| [microsoft/VibeVoice-Realtime-0.5B](https://huggingface.co/microsoft/VibeVoice-Realtime-0.5B) | `model.safetensors` | BF16 | `(1024, 256)` | 3 | 786.4K |
| [microsoft/VibeVoice-Realtime-0.5B](https://huggingface.co/microsoft/VibeVoice-Realtime-0.5B) | `model.safetensors` | BF16 | `(256, 1024)` | 3 | 786.4K |
| [microsoft/VibeVoice-Realtime-0.5B](https://huggingface.co/microsoft/VibeVoice-Realtime-0.5B) | `model.safetensors` | BF16 | `(256, 128, 8)` | 1 | 262.1K |
| [microsoft/VibeVoice-Realtime-0.5B](https://huggingface.co/microsoft/VibeVoice-Realtime-0.5B) | `model.safetensors` | BF16 | `(896, 256)` | 1 | 229.4K |
| [microsoft/VibeVoice-Realtime-0.5B](https://huggingface.co/microsoft/VibeVoice-Realtime-0.5B) | `model.safetensors` | BF16 | `(128, 512)` | 3 | 196.6K |
| [microsoft/VibeVoice-Realtime-0.5B](https://huggingface.co/microsoft/VibeVoice-Realtime-0.5B) | `model.safetensors` | BF16 | `(512, 128)` | 3 | 196.6K |
| [microsoft/VibeVoice-Realtime-0.5B](https://huggingface.co/microsoft/VibeVoice-Realtime-0.5B) | `model.safetensors` | BF16 | `(2048, 1, 7)` | 8 | 114.7K |
| [microsoft/VibeVoice-Realtime-0.5B](https://huggingface.co/microsoft/VibeVoice-Realtime-0.5B) | `model.safetensors` | BF16 | `(896, 64)` | 2 | 114.7K |
| [microsoft/VibeVoice-Realtime-0.5B](https://huggingface.co/microsoft/VibeVoice-Realtime-0.5B) | `model.safetensors` | BF16 | `(2048)` | 52 | 106.5K |
| [microsoft/VibeVoice-Realtime-0.5B](https://huggingface.co/microsoft/VibeVoice-Realtime-0.5B) | `model.safetensors` | BF16 | `(896)` | 81 | 72.6K |
| [microsoft/VibeVoice-Realtime-0.5B](https://huggingface.co/microsoft/VibeVoice-Realtime-0.5B) | `model.safetensors` | BF16 | `(8192)` | 8 | 65.5K |
| [microsoft/VibeVoice-Realtime-0.5B](https://huggingface.co/microsoft/VibeVoice-Realtime-0.5B) | `model.safetensors` | BF16 | `(64, 896)` | 1 | 57.3K |
| [microsoft/VibeVoice-Realtime-0.5B](https://huggingface.co/microsoft/VibeVoice-Realtime-0.5B) | `model.safetensors` | BF16 | `(256, 64)` | 3 | 49.2K |
| [microsoft/VibeVoice-Realtime-0.5B](https://huggingface.co/microsoft/VibeVoice-Realtime-0.5B) | `model.safetensors` | BF16 | `(64, 256)` | 3 | 49.2K |
| [microsoft/VibeVoice-Realtime-0.5B](https://huggingface.co/microsoft/VibeVoice-Realtime-0.5B) | `model.safetensors` | BF16 | `(128, 64, 4)` | 1 | 32.8K |
| [microsoft/VibeVoice-Realtime-0.5B](https://huggingface.co/microsoft/VibeVoice-Realtime-0.5B) | `model.safetensors` | BF16 | `(1024)` | 22 | 22.5K |
| [microsoft/VibeVoice-Realtime-0.5B](https://huggingface.co/microsoft/VibeVoice-Realtime-0.5B) | `model.safetensors` | BF16 | `(1024, 1, 7)` | 3 | 21.5K |
| [microsoft/VibeVoice-Realtime-0.5B](https://huggingface.co/microsoft/VibeVoice-Realtime-0.5B) | `model.safetensors` | BF16 | `(128, 32)` | 3 | 12.3K |
| [microsoft/VibeVoice-Realtime-0.5B](https://huggingface.co/microsoft/VibeVoice-Realtime-0.5B) | `model.safetensors` | BF16 | `(32, 128)` | 3 | 12.3K |
| [microsoft/VibeVoice-Realtime-0.5B](https://huggingface.co/microsoft/VibeVoice-Realtime-0.5B) | `model.safetensors` | BF16 | `(4096)` | 3 | 12.3K |
| [microsoft/VibeVoice-Realtime-0.5B](https://huggingface.co/microsoft/VibeVoice-Realtime-0.5B) | `model.safetensors` | BF16 | `(512)` | 22 | 11.3K |
| [microsoft/VibeVoice-Realtime-0.5B](https://huggingface.co/microsoft/VibeVoice-Realtime-0.5B) | `model.safetensors` | BF16 | `(512, 1, 7)` | 3 | 10.8K |
| [microsoft/VibeVoice-Realtime-0.5B](https://huggingface.co/microsoft/VibeVoice-Realtime-0.5B) | `model.safetensors` | BF16 | `(128)` | 70 | 9.0K |
| [microsoft/VibeVoice-Realtime-0.5B](https://huggingface.co/microsoft/VibeVoice-Realtime-0.5B) | `model.safetensors` | BF16 | `(64, 32, 4)` | 1 | 8.2K |
| [microsoft/VibeVoice-Realtime-0.5B](https://huggingface.co/microsoft/VibeVoice-Realtime-0.5B) | `model.safetensors` | BF16 | `(256)` | 22 | 5.6K |
| [microsoft/VibeVoice-Realtime-0.5B](https://huggingface.co/microsoft/VibeVoice-Realtime-0.5B) | `model.safetensors` | BF16 | `(256, 1, 7)` | 3 | 5.4K |
| [microsoft/VibeVoice-Realtime-0.5B](https://huggingface.co/microsoft/VibeVoice-Realtime-0.5B) | `model.safetensors` | BF16 | `(128, 1, 7)` | 3 | 2.7K |
| [microsoft/VibeVoice-Realtime-0.5B](https://huggingface.co/microsoft/VibeVoice-Realtime-0.5B) | `model.safetensors` | BF16 | `(2, 896)` | 1 | 1.8K |
| [microsoft/VibeVoice-Realtime-0.5B](https://huggingface.co/microsoft/VibeVoice-Realtime-0.5B) | `model.safetensors` | BF16 | `(64, 1, 7)` | 3 | 1.3K |
| [microsoft/VibeVoice-Realtime-0.5B](https://huggingface.co/microsoft/VibeVoice-Realtime-0.5B) | `model.safetensors` | BF16 | `(64)` | 19 | 1.2K |
| [microsoft/VibeVoice-Realtime-0.5B](https://huggingface.co/microsoft/VibeVoice-Realtime-0.5B) | `model.safetensors` | BF16 | `(1, 896)` | 1 | 896 |
| [microsoft/VibeVoice-Realtime-0.5B](https://huggingface.co/microsoft/VibeVoice-Realtime-0.5B) | `model.safetensors` | BF16 | `(32, 1, 7)` | 3 | 672 |
| [microsoft/VibeVoice-Realtime-0.5B](https://huggingface.co/microsoft/VibeVoice-Realtime-0.5B) | `model.safetensors` | BF16 | `(32)` | 19 | 608 |
| [microsoft/VibeVoice-Realtime-0.5B](https://huggingface.co/microsoft/VibeVoice-Realtime-0.5B) | `model.safetensors` | BF16 | `(1, 32, 7)` | 1 | 224 |
| [microsoft/VibeVoice-Realtime-0.5B](https://huggingface.co/microsoft/VibeVoice-Realtime-0.5B) | `model.safetensors` | BF16 | `()` | 2 | 2 |
| [microsoft/VibeVoice-Realtime-0.5B](https://huggingface.co/microsoft/VibeVoice-Realtime-0.5B) | `model.safetensors` | BF16 | `(1)` | 2 | 2 |
| [nari-labs/Dia-1.6B](https://huggingface.co/nari-labs/Dia-1.6B) | `model.safetensors` | FP32 | `(2048, 2, 8192)` | 18 | 604.0M |
| [nari-labs/Dia-1.6B](https://huggingface.co/nari-labs/Dia-1.6B) | `model.safetensors` | FP32 | `(8192, 2048)` | 18 | 302.0M |
| [nari-labs/Dia-1.6B](https://huggingface.co/nari-labs/Dia-1.6B) | `model.safetensors` | FP32 | `(1024, 16, 128)` | 72 | 151.0M |
| [nari-labs/Dia-1.6B](https://huggingface.co/nari-labs/Dia-1.6B) | `model.safetensors` | FP32 | `(16, 128, 2048)` | 36 | 151.0M |
| [nari-labs/Dia-1.6B](https://huggingface.co/nari-labs/Dia-1.6B) | `model.safetensors` | FP32 | `(2048, 16, 128)` | 36 | 151.0M |
| [nari-labs/Dia-1.6B](https://huggingface.co/nari-labs/Dia-1.6B) | `model.safetensors` | FP32 | `(1024, 2, 4096)` | 12 | 100.7M |
| [nari-labs/Dia-1.6B](https://huggingface.co/nari-labs/Dia-1.6B) | `model.safetensors` | FP32 | `(4096, 1024)` | 12 | 50.3M |
| [nari-labs/Dia-1.6B](https://huggingface.co/nari-labs/Dia-1.6B) | `model.safetensors` | FP32 | `(2048, 4, 128)` | 36 | 37.7M |
| [nari-labs/Dia-1.6B](https://huggingface.co/nari-labs/Dia-1.6B) | `model.safetensors` | FP32 | `(16, 128, 1024)` | 12 | 25.2M |
| [nari-labs/Dia-1.6B](https://huggingface.co/nari-labs/Dia-1.6B) | `model.safetensors` | FP32 | `(1028, 2048)` | 9 | 18.9M |
| [nari-labs/Dia-1.6B](https://huggingface.co/nari-labs/Dia-1.6B) | `model.safetensors` | FP32 | `(2048, 9, 1028)` | 1 | 18.9M |
| [nari-labs/Dia-1.6B](https://huggingface.co/nari-labs/Dia-1.6B) | `model.safetensors` | FP32 | `(256, 1024)` | 1 | 262.1K |
| [nari-labs/Dia-1.6B](https://huggingface.co/nari-labs/Dia-1.6B) | `model.safetensors` | FP32 | `(2048)` | 55 | 112.6K |
| [nari-labs/Dia-1.6B](https://huggingface.co/nari-labs/Dia-1.6B) | `model.safetensors` | FP32 | `(1024)` | 25 | 25.6K |
| [openai/clip-vit-large-patch14](https://huggingface.co/openai/clip-vit-large-patch14) | `model.safetensors` | FP32 | `(1024, 1024)` | 96 | 100.7M |
| [openai/clip-vit-large-patch14](https://huggingface.co/openai/clip-vit-large-patch14) | `model.safetensors` | FP32 | `(1024, 4096)` | 24 | 100.7M |
| [openai/clip-vit-large-patch14](https://huggingface.co/openai/clip-vit-large-patch14) | `model.safetensors` | FP32 | `(4096, 1024)` | 24 | 100.7M |
| [openai/clip-vit-large-patch14](https://huggingface.co/openai/clip-vit-large-patch14) | `model.safetensors` | FP32 | `(49408, 768)` | 1 | 37.9M |
| [openai/clip-vit-large-patch14](https://huggingface.co/openai/clip-vit-large-patch14) | `model.safetensors` | FP32 | `(768, 768)` | 49 | 28.9M |
| [openai/clip-vit-large-patch14](https://huggingface.co/openai/clip-vit-large-patch14) | `model.safetensors` | FP32 | `(3072, 768)` | 12 | 28.3M |
| [openai/clip-vit-large-patch14](https://huggingface.co/openai/clip-vit-large-patch14) | `model.safetensors` | FP32 | `(768, 3072)` | 12 | 28.3M |
| [openai/clip-vit-large-patch14](https://huggingface.co/openai/clip-vit-large-patch14) | `model.safetensors` | FP32 | `(768, 1024)` | 1 | 786.4K |
| [openai/clip-vit-large-patch14](https://huggingface.co/openai/clip-vit-large-patch14) | `model.safetensors` | FP32 | `(1024, 3, 14, 14)` | 1 | 602.1K |
| [openai/clip-vit-large-patch14](https://huggingface.co/openai/clip-vit-large-patch14) | `model.safetensors` | FP32 | `(257, 1024)` | 1 | 263.2K |
| [openai/clip-vit-large-patch14](https://huggingface.co/openai/clip-vit-large-patch14) | `model.safetensors` | FP32 | `(1024)` | 221 | 226.3K |
| [openai/clip-vit-large-patch14](https://huggingface.co/openai/clip-vit-large-patch14) | `model.safetensors` | FP32 | `(4096)` | 24 | 98.3K |
| [openai/clip-vit-large-patch14](https://huggingface.co/openai/clip-vit-large-patch14) | `model.safetensors` | FP32 | `(768)` | 110 | 84.5K |
| [openai/clip-vit-large-patch14](https://huggingface.co/openai/clip-vit-large-patch14) | `model.safetensors` | FP32 | `(77, 768)` | 1 | 59.1K |
| [openai/clip-vit-large-patch14](https://huggingface.co/openai/clip-vit-large-patch14) | `model.safetensors` | FP32 | `(3072)` | 12 | 36.9K |
| [openai/clip-vit-large-patch14](https://huggingface.co/openai/clip-vit-large-patch14) | `model.safetensors` | FP32 | `()` | 1 | 1 |
| [openai/clip-vit-large-patch14](https://huggingface.co/openai/clip-vit-large-patch14) | `model.safetensors` | INT64 | `(1, 257)` | 1 | 257 |
| [openai/clip-vit-large-patch14](https://huggingface.co/openai/clip-vit-large-patch14) | `model.safetensors` | INT64 | `(1, 77)` | 1 | 77 |
| [philz1337x/loras](https://huggingface.co/philz1337x/loras) | `FilmVelvia3.safetensors` | FP16 | `(128, 768)` | 92 | 9.0M |
| [philz1337x/loras](https://huggingface.co/philz1337x/loras) | `FilmVelvia3.safetensors` | FP16 | `(1280, 128)` | 54 | 8.8M |
| [philz1337x/loras](https://huggingface.co/philz1337x/loras) | `FilmVelvia3.safetensors` | FP16 | `(10240, 128)` | 6 | 7.9M |
| [philz1337x/loras](https://huggingface.co/philz1337x/loras) | `FilmVelvia3.safetensors` | FP16 | `(128, 1280)` | 47 | 7.7M |
| [philz1337x/loras](https://huggingface.co/philz1337x/loras) | `FilmVelvia3.safetensors` | FP16 | `(768, 128)` | 60 | 5.9M |
| [philz1337x/loras](https://huggingface.co/philz1337x/loras) | `FilmVelvia3.safetensors` | FP16 | `(128, 3072)` | 12 | 4.7M |
| [philz1337x/loras](https://huggingface.co/philz1337x/loras) | `FilmVelvia3.safetensors` | FP16 | `(3072, 128)` | 12 | 4.7M |
| [philz1337x/loras](https://huggingface.co/philz1337x/loras) | `FilmVelvia3.safetensors` | FP16 | `(128, 5120)` | 6 | 3.9M |
| [philz1337x/loras](https://huggingface.co/philz1337x/loras) | `FilmVelvia3.safetensors` | FP16 | `(640, 128)` | 45 | 3.7M |
| [philz1337x/loras](https://huggingface.co/philz1337x/loras) | `FilmVelvia3.safetensors` | FP16 | `(5120, 128)` | 5 | 3.3M |
| [philz1337x/loras](https://huggingface.co/philz1337x/loras) | `FilmVelvia3.safetensors` | FP16 | `(128, 640)` | 35 | 2.9M |
| [philz1337x/loras](https://huggingface.co/philz1337x/loras) | `103423215.safetensors` | FP16 | `(1280, 32)` | 54 | 2.2M |
| [philz1337x/loras](https://huggingface.co/philz1337x/loras) | `103423215.safetensors` | FP16 | `(10240, 32)` | 6 | 2.0M |
| [philz1337x/loras](https://huggingface.co/philz1337x/loras) | `FilmVelvia3.safetensors` | FP16 | `(128, 1280, 1, 1)` | 12 | 2.0M |
| [philz1337x/loras](https://huggingface.co/philz1337x/loras) | `FilmVelvia3.safetensors` | FP16 | `(1280, 128, 1, 1)` | 12 | 2.0M |
| [philz1337x/loras](https://huggingface.co/philz1337x/loras) | `103423215.safetensors` | FP16 | `(32, 1280)` | 47 | 1.9M |
| [philz1337x/loras](https://huggingface.co/philz1337x/loras) | `FilmVelvia3.safetensors` | FP16 | `(320, 128)` | 45 | 1.8M |
| [philz1337x/loras](https://huggingface.co/philz1337x/loras) | `FilmVelvia3.safetensors` | FP16 | `(128, 2560)` | 5 | 1.6M |
| [philz1337x/loras](https://huggingface.co/philz1337x/loras) | `FilmVelvia3.safetensors` | FP16 | `(2560, 128)` | 5 | 1.6M |
| [philz1337x/loras](https://huggingface.co/philz1337x/loras) | `FilmVelvia3.safetensors` | FP16 | `(128, 320)` | 35 | 1.4M |
| [philz1337x/loras](https://huggingface.co/philz1337x/loras) | `103423215.safetensors` | FP16 | `(32, 5120)` | 6 | 983.0K |
| [philz1337x/loras](https://huggingface.co/philz1337x/loras) | `103423215.safetensors` | FP16 | `(640, 32)` | 45 | 921.6K |
| [philz1337x/loras](https://huggingface.co/philz1337x/loras) | `FilmVelvia3.safetensors` | FP16 | `(128, 640, 1, 1)` | 10 | 819.2K |
| [philz1337x/loras](https://huggingface.co/philz1337x/loras) | `103423215.safetensors` | FP16 | `(5120, 32)` | 5 | 819.2K |
| [philz1337x/loras](https://huggingface.co/philz1337x/loras) | `FilmVelvia3.safetensors` | FP16 | `(640, 128, 1, 1)` | 10 | 819.2K |
| [philz1337x/loras](https://huggingface.co/philz1337x/loras) | `103423215.safetensors` | FP16 | `(32, 768)` | 32 | 786.4K |
| [philz1337x/loras](https://huggingface.co/philz1337x/loras) | `103423215.safetensors` | FP16 | `(32, 640)` | 35 | 716.8K |
| [philz1337x/loras](https://huggingface.co/philz1337x/loras) | `103423215.safetensors` | FP16 | `(1280, 32, 1, 1)` | 12 | 491.5K |
| [philz1337x/loras](https://huggingface.co/philz1337x/loras) | `103423215.safetensors` | FP16 | `(32, 1280, 1, 1)` | 12 | 491.5K |
| [philz1337x/loras](https://huggingface.co/philz1337x/loras) | `103423215.safetensors` | FP16 | `(320, 32)` | 45 | 460.8K |
| [philz1337x/loras](https://huggingface.co/philz1337x/loras) | `FilmVelvia3.safetensors` | FP16 | `(128, 320, 1, 1)` | 10 | 409.6K |
| [philz1337x/loras](https://huggingface.co/philz1337x/loras) | `103423215.safetensors` | FP16 | `(2560, 32)` | 5 | 409.6K |
| [philz1337x/loras](https://huggingface.co/philz1337x/loras) | `103423215.safetensors` | FP16 | `(32, 2560)` | 5 | 409.6K |
| [philz1337x/loras](https://huggingface.co/philz1337x/loras) | `FilmVelvia3.safetensors` | FP16 | `(320, 128, 1, 1)` | 10 | 409.6K |
| [philz1337x/loras](https://huggingface.co/philz1337x/loras) | `103423215.safetensors` | FP16 | `(32, 320)` | 35 | 358.4K |
| [philz1337x/loras](https://huggingface.co/philz1337x/loras) | `103423215.safetensors` | FP16 | `(32, 640, 1, 1)` | 10 | 204.8K |
| [philz1337x/loras](https://huggingface.co/philz1337x/loras) | `103423215.safetensors` | FP16 | `(640, 32, 1, 1)` | 10 | 204.8K |
| [philz1337x/loras](https://huggingface.co/philz1337x/loras) | `103423215.safetensors` | FP16 | `(32, 320, 1, 1)` | 10 | 102.4K |
| [philz1337x/loras](https://huggingface.co/philz1337x/loras) | `103423215.safetensors` | FP16 | `(320, 32, 1, 1)` | 10 | 102.4K |
| [philz1337x/loras](https://huggingface.co/philz1337x/loras) | `FilmVelvia3.safetensors` | FP16 | `()` | 264 | 264 |
| [philz1337x/loras](https://huggingface.co/philz1337x/loras) | `103423215.safetensors` | FP16 | `()` | 192 | 192 |
| [philz1337x/loras](https://huggingface.co/philz1337x/loras) | `Elixir.safetensors` | FP32 | `(4, 768)` | 92 | 282.6K |
| [philz1337x/loras](https://huggingface.co/philz1337x/loras) | `Elixir.safetensors` | FP32 | `(1280, 4)` | 54 | 276.5K |
| [philz1337x/loras](https://huggingface.co/philz1337x/loras) | `Elixir.safetensors` | FP32 | `(10240, 4)` | 6 | 245.8K |
| [philz1337x/loras](https://huggingface.co/philz1337x/loras) | `Elixir.safetensors` | FP32 | `(4, 1280)` | 47 | 240.6K |
| [philz1337x/loras](https://huggingface.co/philz1337x/loras) | `Elixir.safetensors` | FP32 | `(768, 4)` | 60 | 184.3K |
| [philz1337x/loras](https://huggingface.co/philz1337x/loras) | `Elixir.safetensors` | FP32 | `(3072, 4)` | 12 | 147.5K |
| [philz1337x/loras](https://huggingface.co/philz1337x/loras) | `Elixir.safetensors` | FP32 | `(4, 3072)` | 12 | 147.5K |
| [philz1337x/loras](https://huggingface.co/philz1337x/loras) | `Elixir.safetensors` | FP32 | `(4, 5120)` | 6 | 122.9K |
| [philz1337x/loras](https://huggingface.co/philz1337x/loras) | `Elixir.safetensors` | FP32 | `(640, 4)` | 45 | 115.2K |
| [philz1337x/loras](https://huggingface.co/philz1337x/loras) | `Elixir.safetensors` | FP32 | `(5120, 4)` | 5 | 102.4K |
| [philz1337x/loras](https://huggingface.co/philz1337x/loras) | `Elixir.safetensors` | FP32 | `(4, 640)` | 35 | 89.6K |
| [philz1337x/loras](https://huggingface.co/philz1337x/loras) | `Elixir.safetensors` | FP32 | `(1280, 4, 1, 1)` | 12 | 61.4K |
| [philz1337x/loras](https://huggingface.co/philz1337x/loras) | `Elixir.safetensors` | FP32 | `(4, 1280, 1, 1)` | 12 | 61.4K |
| [philz1337x/loras](https://huggingface.co/philz1337x/loras) | `Elixir.safetensors` | FP32 | `(320, 4)` | 45 | 57.6K |
| [philz1337x/loras](https://huggingface.co/philz1337x/loras) | `Elixir.safetensors` | FP32 | `(2560, 4)` | 5 | 51.2K |
| [philz1337x/loras](https://huggingface.co/philz1337x/loras) | `Elixir.safetensors` | FP32 | `(4, 2560)` | 5 | 51.2K |
| [philz1337x/loras](https://huggingface.co/philz1337x/loras) | `Elixir.safetensors` | FP32 | `(4, 320)` | 35 | 44.8K |
| [philz1337x/loras](https://huggingface.co/philz1337x/loras) | `Elixir.safetensors` | FP32 | `(4, 640, 1, 1)` | 10 | 25.6K |
| [philz1337x/loras](https://huggingface.co/philz1337x/loras) | `Elixir.safetensors` | FP32 | `(640, 4, 1, 1)` | 10 | 25.6K |
| [philz1337x/loras](https://huggingface.co/philz1337x/loras) | `Elixir.safetensors` | FP32 | `(320, 4, 1, 1)` | 10 | 12.8K |
| [philz1337x/loras](https://huggingface.co/philz1337x/loras) | `Elixir.safetensors` | FP32 | `(4, 320, 1, 1)` | 10 | 12.8K |
| [philz1337x/loras](https://huggingface.co/philz1337x/loras) | `Elixir.safetensors` | FP32 | `()` | 264 | 264 |
| [refiners/controlnet.sd1_5.tile](https://huggingface.co/refiners/controlnet.sd1_5.tile) | `model.safetensors` | FP16 | `(1280, 1280, 3, 3)` | 12 | 176.9M |
| [refiners/controlnet.sd1_5.tile](https://huggingface.co/refiners/controlnet.sd1_5.tile) | `model.safetensors` | FP16 | `(1280, 1280)` | 25 | 41.0M |
| [refiners/controlnet.sd1_5.tile](https://huggingface.co/refiners/controlnet.sd1_5.tile) | `model.safetensors` | FP16 | `(10240, 1280)` | 3 | 39.3M |
| [refiners/controlnet.sd1_5.tile](https://huggingface.co/refiners/controlnet.sd1_5.tile) | `model.safetensors` | FP16 | `(1280, 1280, 1, 1)` | 12 | 19.7M |
| [refiners/controlnet.sd1_5.tile](https://huggingface.co/refiners/controlnet.sd1_5.tile) | `model.safetensors` | FP16 | `(1280, 5120)` | 3 | 19.7M |
| [refiners/controlnet.sd1_5.tile](https://huggingface.co/refiners/controlnet.sd1_5.tile) | `model.safetensors` | FP16 | `(640, 640, 3, 3)` | 4 | 14.7M |
| [refiners/controlnet.sd1_5.tile](https://huggingface.co/refiners/controlnet.sd1_5.tile) | `model.safetensors` | FP16 | `(1280, 640, 3, 3)` | 1 | 7.4M |
| [refiners/controlnet.sd1_5.tile](https://huggingface.co/refiners/controlnet.sd1_5.tile) | `model.safetensors` | FP16 | `(5120, 640)` | 2 | 6.6M |
| [refiners/controlnet.sd1_5.tile](https://huggingface.co/refiners/controlnet.sd1_5.tile) | `model.safetensors` | FP16 | `(1280, 768)` | 6 | 5.9M |
| [refiners/controlnet.sd1_5.tile](https://huggingface.co/refiners/controlnet.sd1_5.tile) | `model.safetensors` | FP16 | `(640, 640)` | 12 | 4.9M |
| [refiners/controlnet.sd1_5.tile](https://huggingface.co/refiners/controlnet.sd1_5.tile) | `model.safetensors` | FP16 | `(320, 320, 3, 3)` | 5 | 4.6M |
| [refiners/controlnet.sd1_5.tile](https://huggingface.co/refiners/controlnet.sd1_5.tile) | `model.safetensors` | FP16 | `(640, 2560)` | 2 | 3.3M |
| [refiners/controlnet.sd1_5.tile](https://huggingface.co/refiners/controlnet.sd1_5.tile) | `model.safetensors` | FP16 | `(640, 640, 1, 1)` | 7 | 2.9M |
| [refiners/controlnet.sd1_5.tile](https://huggingface.co/refiners/controlnet.sd1_5.tile) | `model.safetensors` | FP16 | `(640, 768)` | 4 | 2.0M |
| [refiners/controlnet.sd1_5.tile](https://huggingface.co/refiners/controlnet.sd1_5.tile) | `model.safetensors` | FP16 | `(640, 320, 3, 3)` | 1 | 1.8M |
| [refiners/controlnet.sd1_5.tile](https://huggingface.co/refiners/controlnet.sd1_5.tile) | `model.safetensors` | FP16 | `(2560, 320)` | 2 | 1.6M |
| [refiners/controlnet.sd1_5.tile](https://huggingface.co/refiners/controlnet.sd1_5.tile) | `model.safetensors` | FP16 | `(320, 1280)` | 4 | 1.6M |
| [refiners/controlnet.sd1_5.tile](https://huggingface.co/refiners/controlnet.sd1_5.tile) | `model.safetensors` | FP16 | `(640, 1280)` | 2 | 1.6M |
| [refiners/controlnet.sd1_5.tile](https://huggingface.co/refiners/controlnet.sd1_5.tile) | `model.safetensors` | FP16 | `(320, 320)` | 12 | 1.2M |
| [refiners/controlnet.sd1_5.tile](https://huggingface.co/refiners/controlnet.sd1_5.tile) | `model.safetensors` | FP16 | `(320, 768)` | 4 | 983.0K |
| [refiners/controlnet.sd1_5.tile](https://huggingface.co/refiners/controlnet.sd1_5.tile) | `model.safetensors` | FP16 | `(1280, 640, 1, 1)` | 1 | 819.2K |
| [refiners/controlnet.sd1_5.tile](https://huggingface.co/refiners/controlnet.sd1_5.tile) | `model.safetensors` | FP16 | `(320, 320, 1, 1)` | 8 | 819.2K |
| [refiners/controlnet.sd1_5.tile](https://huggingface.co/refiners/controlnet.sd1_5.tile) | `model.safetensors` | FP16 | `(320, 256, 3, 3)` | 1 | 737.3K |
| [refiners/controlnet.sd1_5.tile](https://huggingface.co/refiners/controlnet.sd1_5.tile) | `model.safetensors` | FP16 | `(1280, 320)` | 1 | 409.6K |
| [refiners/controlnet.sd1_5.tile](https://huggingface.co/refiners/controlnet.sd1_5.tile) | `model.safetensors` | FP16 | `(256, 96, 3, 3)` | 1 | 221.2K |
| [refiners/controlnet.sd1_5.tile](https://huggingface.co/refiners/controlnet.sd1_5.tile) | `model.safetensors` | FP16 | `(640, 320, 1, 1)` | 1 | 204.8K |
| [refiners/controlnet.sd1_5.tile](https://huggingface.co/refiners/controlnet.sd1_5.tile) | `model.safetensors` | FP16 | `(1280)` | 89 | 113.9K |
| [refiners/controlnet.sd1_5.tile](https://huggingface.co/refiners/controlnet.sd1_5.tile) | `model.safetensors` | FP16 | `(96, 96, 3, 3)` | 1 | 82.9K |
| [refiners/controlnet.sd1_5.tile](https://huggingface.co/refiners/controlnet.sd1_5.tile) | `model.safetensors` | FP16 | `(10240)` | 3 | 30.7K |
| [refiners/controlnet.sd1_5.tile](https://huggingface.co/refiners/controlnet.sd1_5.tile) | `model.safetensors` | FP16 | `(640)` | 45 | 28.8K |
| [refiners/controlnet.sd1_5.tile](https://huggingface.co/refiners/controlnet.sd1_5.tile) | `model.safetensors` | FP16 | `(96, 32, 3, 3)` | 1 | 27.6K |
| [refiners/controlnet.sd1_5.tile](https://huggingface.co/refiners/controlnet.sd1_5.tile) | `model.safetensors` | FP16 | `(320)` | 49 | 15.7K |
| [refiners/controlnet.sd1_5.tile](https://huggingface.co/refiners/controlnet.sd1_5.tile) | `model.safetensors` | FP16 | `(320, 4, 3, 3)` | 1 | 11.5K |
| [refiners/controlnet.sd1_5.tile](https://huggingface.co/refiners/controlnet.sd1_5.tile) | `model.safetensors` | FP16 | `(5120)` | 2 | 10.2K |
| [refiners/controlnet.sd1_5.tile](https://huggingface.co/refiners/controlnet.sd1_5.tile) | `model.safetensors` | FP16 | `(32, 32, 3, 3)` | 1 | 9.2K |
| [refiners/controlnet.sd1_5.tile](https://huggingface.co/refiners/controlnet.sd1_5.tile) | `model.safetensors` | FP16 | `(2560)` | 2 | 5.1K |
| [refiners/controlnet.sd1_5.tile](https://huggingface.co/refiners/controlnet.sd1_5.tile) | `model.safetensors` | FP16 | `(32, 16, 3, 3)` | 1 | 4.6K |
| [refiners/controlnet.sd1_5.tile](https://huggingface.co/refiners/controlnet.sd1_5.tile) | `model.safetensors` | FP16 | `(16, 16, 3, 3)` | 1 | 2.3K |
| [refiners/controlnet.sd1_5.tile](https://huggingface.co/refiners/controlnet.sd1_5.tile) | `model.safetensors` | FP16 | `(16, 3, 3, 3)` | 1 | 432 |
| [refiners/controlnet.sd1_5.tile](https://huggingface.co/refiners/controlnet.sd1_5.tile) | `model.safetensors` | FP16 | `(256)` | 1 | 256 |
| [refiners/controlnet.sd1_5.tile](https://huggingface.co/refiners/controlnet.sd1_5.tile) | `model.safetensors` | FP16 | `(96)` | 2 | 192 |
| [refiners/controlnet.sd1_5.tile](https://huggingface.co/refiners/controlnet.sd1_5.tile) | `model.safetensors` | FP16 | `(32)` | 2 | 64 |
| [refiners/controlnet.sd1_5.tile](https://huggingface.co/refiners/controlnet.sd1_5.tile) | `model.safetensors` | FP16 | `(16)` | 2 | 32 |
| [refiners/juggernaut.reborn.sd1_5.autoencoder](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.autoencoder) | `model.safetensors` | FP16 | `(512, 512, 3, 3)` | 30 | 70.8M |
| [refiners/juggernaut.reborn.sd1_5.autoencoder](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.autoencoder) | `model.safetensors` | FP16 | `(256, 256, 3, 3)` | 10 | 5.9M |
| [refiners/juggernaut.reborn.sd1_5.autoencoder](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.autoencoder) | `model.safetensors` | FP16 | `(512, 512)` | 8 | 2.1M |
| [refiners/juggernaut.reborn.sd1_5.autoencoder](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.autoencoder) | `model.safetensors` | FP16 | `(128, 128, 3, 3)` | 10 | 1.5M |
| [refiners/juggernaut.reborn.sd1_5.autoencoder](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.autoencoder) | `model.safetensors` | FP16 | `(256, 512, 3, 3)` | 1 | 1.2M |
| [refiners/juggernaut.reborn.sd1_5.autoencoder](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.autoencoder) | `model.safetensors` | FP16 | `(512, 256, 3, 3)` | 1 | 1.2M |
| [refiners/juggernaut.reborn.sd1_5.autoencoder](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.autoencoder) | `model.safetensors` | FP16 | `(128, 256, 3, 3)` | 1 | 294.9K |
| [refiners/juggernaut.reborn.sd1_5.autoencoder](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.autoencoder) | `model.safetensors` | FP16 | `(256, 128, 3, 3)` | 1 | 294.9K |
| [refiners/juggernaut.reborn.sd1_5.autoencoder](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.autoencoder) | `model.safetensors` | FP16 | `(256, 512, 1, 1)` | 1 | 131.1K |
| [refiners/juggernaut.reborn.sd1_5.autoencoder](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.autoencoder) | `model.safetensors` | FP16 | `(512, 256, 1, 1)` | 1 | 131.1K |
| [refiners/juggernaut.reborn.sd1_5.autoencoder](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.autoencoder) | `model.safetensors` | FP16 | `(512)` | 103 | 52.7K |
| [refiners/juggernaut.reborn.sd1_5.autoencoder](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.autoencoder) | `model.safetensors` | FP16 | `(8, 512, 3, 3)` | 1 | 36.9K |
| [refiners/juggernaut.reborn.sd1_5.autoencoder](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.autoencoder) | `model.safetensors` | FP16 | `(128, 256, 1, 1)` | 1 | 32.8K |
| [refiners/juggernaut.reborn.sd1_5.autoencoder](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.autoencoder) | `model.safetensors` | FP16 | `(256, 128, 1, 1)` | 1 | 32.8K |
| [refiners/juggernaut.reborn.sd1_5.autoencoder](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.autoencoder) | `model.safetensors` | FP16 | `(512, 4, 3, 3)` | 1 | 18.4K |
| [refiners/juggernaut.reborn.sd1_5.autoencoder](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.autoencoder) | `model.safetensors` | FP16 | `(256)` | 34 | 8.7K |
| [refiners/juggernaut.reborn.sd1_5.autoencoder](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.autoencoder) | `model.safetensors` | FP16 | `(128)` | 35 | 4.5K |
| [refiners/juggernaut.reborn.sd1_5.autoencoder](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.autoencoder) | `model.safetensors` | FP16 | `(128, 3, 3, 3)` | 1 | 3.5K |
| [refiners/juggernaut.reborn.sd1_5.autoencoder](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.autoencoder) | `model.safetensors` | FP16 | `(3, 128, 3, 3)` | 1 | 3.5K |
| [refiners/juggernaut.reborn.sd1_5.autoencoder](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.autoencoder) | `model.safetensors` | FP16 | `(8, 8, 1, 1)` | 1 | 64 |
| [refiners/juggernaut.reborn.sd1_5.autoencoder](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.autoencoder) | `model.safetensors` | FP16 | `(4, 4, 1, 1)` | 1 | 16 |
| [refiners/juggernaut.reborn.sd1_5.autoencoder](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.autoencoder) | `model.safetensors` | FP16 | `(8)` | 2 | 16 |
| [refiners/juggernaut.reborn.sd1_5.autoencoder](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.autoencoder) | `model.safetensors` | FP16 | `(4)` | 1 | 4 |
| [refiners/juggernaut.reborn.sd1_5.autoencoder](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.autoencoder) | `model.safetensors` | FP16 | `(3)` | 1 | 3 |
| [refiners/juggernaut.reborn.sd1_5.text_encoder](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.text_encoder) | `model.safetensors` | FP16 | `(49408, 768)` | 1 | 37.9M |
| [refiners/juggernaut.reborn.sd1_5.text_encoder](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.text_encoder) | `model.safetensors` | FP16 | `(3072, 768)` | 12 | 28.3M |
| [refiners/juggernaut.reborn.sd1_5.text_encoder](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.text_encoder) | `model.safetensors` | FP16 | `(768, 3072)` | 12 | 28.3M |
| [refiners/juggernaut.reborn.sd1_5.text_encoder](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.text_encoder) | `model.safetensors` | FP16 | `(768, 768)` | 48 | 28.3M |
| [refiners/juggernaut.reborn.sd1_5.text_encoder](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.text_encoder) | `model.safetensors` | FP16 | `(768)` | 110 | 84.5K |
| [refiners/juggernaut.reborn.sd1_5.text_encoder](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.text_encoder) | `model.safetensors` | FP16 | `(77, 768)` | 1 | 59.1K |
| [refiners/juggernaut.reborn.sd1_5.text_encoder](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.text_encoder) | `model.safetensors` | FP16 | `(3072)` | 12 | 36.9K |
| [refiners/juggernaut.reborn.sd1_5.unet](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.unet) | `model.safetensors` | FP16 | `(1280, 1280, 3, 3)` | 20 | 294.9M |
| [refiners/juggernaut.reborn.sd1_5.unet](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.unet) | `model.safetensors` | FP16 | `(1280, 2560, 3, 3)` | 5 | 147.5M |
| [refiners/juggernaut.reborn.sd1_5.unet](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.unet) | `model.safetensors` | FP16 | `(1280, 1280)` | 49 | 80.3M |
| [refiners/juggernaut.reborn.sd1_5.unet](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.unet) | `model.safetensors` | FP16 | `(10240, 1280)` | 6 | 78.6M |
| [refiners/juggernaut.reborn.sd1_5.unet](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.unet) | `model.safetensors` | FP16 | `(1280, 5120)` | 6 | 39.3M |
| [refiners/juggernaut.reborn.sd1_5.unet](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.unet) | `model.safetensors` | FP16 | `(640, 640, 3, 3)` | 8 | 29.5M |
| [refiners/juggernaut.reborn.sd1_5.unet](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.unet) | `model.safetensors` | FP16 | `(1280, 1920, 3, 3)` | 1 | 22.1M |
| [refiners/juggernaut.reborn.sd1_5.unet](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.unet) | `model.safetensors` | FP16 | `(1280, 1280, 1, 1)` | 12 | 19.7M |
| [refiners/juggernaut.reborn.sd1_5.unet](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.unet) | `model.safetensors` | FP16 | `(1280, 2560, 1, 1)` | 5 | 16.4M |
| [refiners/juggernaut.reborn.sd1_5.unet](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.unet) | `model.safetensors` | FP16 | `(5120, 640)` | 5 | 16.4M |
| [refiners/juggernaut.reborn.sd1_5.unet](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.unet) | `model.safetensors` | FP16 | `(640, 640)` | 30 | 12.3M |
| [refiners/juggernaut.reborn.sd1_5.unet](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.unet) | `model.safetensors` | FP16 | `(1280, 768)` | 12 | 11.8M |
| [refiners/juggernaut.reborn.sd1_5.unet](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.unet) | `model.safetensors` | FP16 | `(640, 1920, 3, 3)` | 1 | 11.1M |
| [refiners/juggernaut.reborn.sd1_5.unet](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.unet) | `model.safetensors` | FP16 | `(640, 2560)` | 5 | 8.2M |
| [refiners/juggernaut.reborn.sd1_5.unet](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.unet) | `model.safetensors` | FP16 | `(1280, 640, 3, 3)` | 1 | 7.4M |
| [refiners/juggernaut.reborn.sd1_5.unet](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.unet) | `model.safetensors` | FP16 | `(320, 320, 3, 3)` | 8 | 7.4M |
| [refiners/juggernaut.reborn.sd1_5.unet](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.unet) | `model.safetensors` | FP16 | `(640, 1280, 3, 3)` | 1 | 7.4M |
| [refiners/juggernaut.reborn.sd1_5.unet](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.unet) | `model.safetensors` | FP16 | `(640, 960, 3, 3)` | 1 | 5.5M |
| [refiners/juggernaut.reborn.sd1_5.unet](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.unet) | `model.safetensors` | FP16 | `(640, 768)` | 10 | 4.9M |
| [refiners/juggernaut.reborn.sd1_5.unet](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.unet) | `model.safetensors` | FP16 | `(2560, 320)` | 5 | 4.1M |
| [refiners/juggernaut.reborn.sd1_5.unet](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.unet) | `model.safetensors` | FP16 | `(320, 1280)` | 10 | 4.1M |
| [refiners/juggernaut.reborn.sd1_5.unet](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.unet) | `model.safetensors` | FP16 | `(640, 1280)` | 5 | 4.1M |
| [refiners/juggernaut.reborn.sd1_5.unet](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.unet) | `model.safetensors` | FP16 | `(640, 640, 1, 1)` | 10 | 4.1M |
| [refiners/juggernaut.reborn.sd1_5.unet](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.unet) | `model.safetensors` | FP16 | `(320, 640, 3, 3)` | 2 | 3.7M |
| [refiners/juggernaut.reborn.sd1_5.unet](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.unet) | `model.safetensors` | FP16 | `(320, 320)` | 30 | 3.1M |
| [refiners/juggernaut.reborn.sd1_5.unet](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.unet) | `model.safetensors` | FP16 | `(320, 960, 3, 3)` | 1 | 2.8M |
| [refiners/juggernaut.reborn.sd1_5.unet](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.unet) | `model.safetensors` | FP16 | `(1280, 1920, 1, 1)` | 1 | 2.5M |
| [refiners/juggernaut.reborn.sd1_5.unet](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.unet) | `model.safetensors` | FP16 | `(320, 768)` | 10 | 2.5M |
| [refiners/juggernaut.reborn.sd1_5.unet](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.unet) | `model.safetensors` | FP16 | `(640, 320, 3, 3)` | 1 | 1.8M |
| [refiners/juggernaut.reborn.sd1_5.unet](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.unet) | `model.safetensors` | FP16 | `(640, 1920, 1, 1)` | 1 | 1.2M |
| [refiners/juggernaut.reborn.sd1_5.unet](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.unet) | `model.safetensors` | FP16 | `(320, 320, 1, 1)` | 10 | 1.0M |
| [refiners/juggernaut.reborn.sd1_5.unet](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.unet) | `model.safetensors` | FP16 | `(1280, 640, 1, 1)` | 1 | 819.2K |
| [refiners/juggernaut.reborn.sd1_5.unet](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.unet) | `model.safetensors` | FP16 | `(640, 1280, 1, 1)` | 1 | 819.2K |
| [refiners/juggernaut.reborn.sd1_5.unet](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.unet) | `model.safetensors` | FP16 | `(640, 960, 1, 1)` | 1 | 614.4K |
| [refiners/juggernaut.reborn.sd1_5.unet](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.unet) | `model.safetensors` | FP16 | `(1280, 320)` | 1 | 409.6K |
| [refiners/juggernaut.reborn.sd1_5.unet](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.unet) | `model.safetensors` | FP16 | `(320, 640, 1, 1)` | 2 | 409.6K |
| [refiners/juggernaut.reborn.sd1_5.unet](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.unet) | `model.safetensors` | FP16 | `(320, 960, 1, 1)` | 1 | 307.2K |
| [refiners/juggernaut.reborn.sd1_5.unet](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.unet) | `model.safetensors` | FP16 | `(1280)` | 162 | 207.4K |
| [refiners/juggernaut.reborn.sd1_5.unet](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.unet) | `model.safetensors` | FP16 | `(640, 320, 1, 1)` | 1 | 204.8K |
| [refiners/juggernaut.reborn.sd1_5.unet](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.unet) | `model.safetensors` | FP16 | `(640)` | 104 | 66.6K |
| [refiners/juggernaut.reborn.sd1_5.unet](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.unet) | `model.safetensors` | FP16 | `(10240)` | 6 | 61.4K |
| [refiners/juggernaut.reborn.sd1_5.unet](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.unet) | `model.safetensors` | FP16 | `(2560)` | 15 | 38.4K |
| [refiners/juggernaut.reborn.sd1_5.unet](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.unet) | `model.safetensors` | FP16 | `(320)` | 103 | 33.0K |
| [refiners/juggernaut.reborn.sd1_5.unet](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.unet) | `model.safetensors` | FP16 | `(5120)` | 5 | 25.6K |
| [refiners/juggernaut.reborn.sd1_5.unet](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.unet) | `model.safetensors` | FP16 | `(320, 4, 3, 3)` | 1 | 11.5K |
| [refiners/juggernaut.reborn.sd1_5.unet](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.unet) | `model.safetensors` | FP16 | `(4, 320, 3, 3)` | 1 | 11.5K |
| [refiners/juggernaut.reborn.sd1_5.unet](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.unet) | `model.safetensors` | FP16 | `(1920)` | 4 | 7.7K |
| [refiners/juggernaut.reborn.sd1_5.unet](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.unet) | `model.safetensors` | FP16 | `(960)` | 4 | 3.8K |
| [refiners/juggernaut.reborn.sd1_5.unet](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.unet) | `model.safetensors` | FP16 | `(4)` | 1 | 4 |
| [rhymes-ai/Allegro](https://huggingface.co/rhymes-ai/Allegro) | `text_encoder/model-00003-of-00004.safetensors` | FP32 | `(10240, 4096)` | 13 | 545.3M |
| [rhymes-ai/Allegro](https://huggingface.co/rhymes-ai/Allegro) | `text_encoder/model-00001-of-00004.safetensors` | FP32 | `(10240, 4096)` | 12 | 503.3M |
| [rhymes-ai/Allegro](https://huggingface.co/rhymes-ai/Allegro) | `text_encoder/model-00002-of-00004.safetensors` | FP32 | `(10240, 4096)` | 12 | 503.3M |
| [rhymes-ai/Allegro](https://huggingface.co/rhymes-ai/Allegro) | `text_encoder/model-00002-of-00004.safetensors` | FP32 | `(4096, 4096)` | 27 | 453.0M |
| [rhymes-ai/Allegro](https://huggingface.co/rhymes-ai/Allegro) | `text_encoder/model-00003-of-00004.safetensors` | FP32 | `(4096, 4096)` | 25 | 419.4M |
| [rhymes-ai/Allegro](https://huggingface.co/rhymes-ai/Allegro) | `text_encoder/model-00001-of-00004.safetensors` | FP32 | `(4096, 4096)` | 24 | 402.7M |
| [rhymes-ai/Allegro](https://huggingface.co/rhymes-ai/Allegro) | `text_encoder/model-00002-of-00004.safetensors` | FP32 | `(4096, 10240)` | 7 | 293.6M |
| [rhymes-ai/Allegro](https://huggingface.co/rhymes-ai/Allegro) | `text_encoder/model-00003-of-00004.safetensors` | FP32 | `(4096, 10240)` | 6 | 251.7M |
| [rhymes-ai/Allegro](https://huggingface.co/rhymes-ai/Allegro) | `text_encoder/model-00001-of-00004.safetensors` | FP32 | `(4096, 10240)` | 5 | 209.7M |
| [rhymes-ai/Allegro](https://huggingface.co/rhymes-ai/Allegro) | `text_encoder/model-00001-of-00004.safetensors` | FP32 | `(32128, 4096)` | 1 | 131.6M |
| [rhymes-ai/Allegro](https://huggingface.co/rhymes-ai/Allegro) | `text_encoder/model-00002-of-00004.safetensors` | FP32 | `(4096)` | 13 | 53.2K |
| [rhymes-ai/Allegro](https://huggingface.co/rhymes-ai/Allegro) | `text_encoder/model-00003-of-00004.safetensors` | FP32 | `(4096)` | 13 | 53.2K |
| [rhymes-ai/Allegro](https://huggingface.co/rhymes-ai/Allegro) | `text_encoder/model-00001-of-00004.safetensors` | FP32 | `(4096)` | 11 | 45.1K |
| [rhymes-ai/Allegro](https://huggingface.co/rhymes-ai/Allegro) | `text_encoder/model-00001-of-00004.safetensors` | FP32 | `(32, 64)` | 1 | 2.0K |
| [Roblox/cube3d-v0.1](https://huggingface.co/Roblox/cube3d-v0.1) | `shape_gpt.safetensors` | FP32 | `(6144, 1536)` | 92 | 868.2M |
| [Roblox/cube3d-v0.1](https://huggingface.co/Roblox/cube3d-v0.1) | `shape_gpt.safetensors` | FP32 | `(1536, 6144)` | 46 | 434.1M |
| [Roblox/cube3d-v0.1](https://huggingface.co/Roblox/cube3d-v0.1) | `shape_gpt.safetensors` | FP32 | `(1536, 1536)` | 94 | 221.8M |
| [Roblox/cube3d-v0.1](https://huggingface.co/Roblox/cube3d-v0.1) | `shape_gpt.safetensors` | FP32 | `(3072, 1536)` | 46 | 217.1M |
| [Roblox/cube3d-v0.1](https://huggingface.co/Roblox/cube3d-v0.1) | `shape_tokenizer.safetensors` | FP32 | `(3072, 768)` | 38 | 89.7M |
| [Roblox/cube3d-v0.1](https://huggingface.co/Roblox/cube3d-v0.1) | `shape_tokenizer.safetensors` | FP32 | `(768, 3072)` | 38 | 89.7M |
| [Roblox/cube3d-v0.1](https://huggingface.co/Roblox/cube3d-v0.1) | `shape_tokenizer.safetensors` | FP32 | `(768, 768)` | 88 | 51.9M |
| [Roblox/cube3d-v0.1](https://huggingface.co/Roblox/cube3d-v0.1) | `shape_gpt.safetensors` | FP32 | `(16387, 1536)` | 2 | 50.3M |
| [Roblox/cube3d-v0.1](https://huggingface.co/Roblox/cube3d-v0.1) | `shape_tokenizer.safetensors` | FP32 | `(1536, 768)` | 33 | 38.9M |
| [Roblox/cube3d-v0.1](https://huggingface.co/Roblox/cube3d-v0.1) | `shape_gpt.safetensors` | FP32 | `(1536, 768)` | 1 | 1.2M |
| [Roblox/cube3d-v0.1](https://huggingface.co/Roblox/cube3d-v0.1) | `shape_tokenizer.safetensors` | FP32 | `(768, 774)` | 1 | 594.4K |
| [Roblox/cube3d-v0.1](https://huggingface.co/Roblox/cube3d-v0.1) | `shape_tokenizer.safetensors` | FP32 | `(768, 771)` | 1 | 592.1K |
| [Roblox/cube3d-v0.1](https://huggingface.co/Roblox/cube3d-v0.1) | `shape_gpt.safetensors` | FP32 | `(6144)` | 92 | 565.2K |
| [Roblox/cube3d-v0.1](https://huggingface.co/Roblox/cube3d-v0.1) | `shape_tokenizer.safetensors` | FP32 | `(16384, 32)` | 1 | 524.3K |
| [Roblox/cube3d-v0.1](https://huggingface.co/Roblox/cube3d-v0.1) | `shape_tokenizer.safetensors` | FP32 | `(513, 768)` | 1 | 394.0K |
| [Roblox/cube3d-v0.1](https://huggingface.co/Roblox/cube3d-v0.1) | `shape_tokenizer.safetensors` | FP32 | `(512, 768)` | 1 | 393.2K |
| [Roblox/cube3d-v0.1](https://huggingface.co/Roblox/cube3d-v0.1) | `shape_gpt.safetensors` | FP32 | `(1536)` | 142 | 218.1K |
| [Roblox/cube3d-v0.1](https://huggingface.co/Roblox/cube3d-v0.1) | `shape_tokenizer.safetensors` | FP32 | `(3072)` | 38 | 116.7K |
| [Roblox/cube3d-v0.1](https://huggingface.co/Roblox/cube3d-v0.1) | `shape_tokenizer.safetensors` | FP32 | `(768)` | 133 | 102.1K |
| [Roblox/cube3d-v0.1](https://huggingface.co/Roblox/cube3d-v0.1) | `shape_tokenizer.safetensors` | FP32 | `(1536)` | 33 | 50.7K |
| [Roblox/cube3d-v0.1](https://huggingface.co/Roblox/cube3d-v0.1) | `shape_gpt.safetensors` | FP32 | `(1536, 32)` | 1 | 49.2K |
| [Roblox/cube3d-v0.1](https://huggingface.co/Roblox/cube3d-v0.1) | `shape_tokenizer.safetensors` | FP32 | `(32, 768)` | 2 | 49.2K |
| [Roblox/cube3d-v0.1](https://huggingface.co/Roblox/cube3d-v0.1) | `shape_tokenizer.safetensors` | FP32 | `(768, 32)` | 1 | 24.6K |
| [Roblox/cube3d-v0.1](https://huggingface.co/Roblox/cube3d-v0.1) | `shape_gpt.safetensors` | FP32 | `(128)` | 93 | 11.9K |
| [Roblox/cube3d-v0.1](https://huggingface.co/Roblox/cube3d-v0.1) | `shape_tokenizer.safetensors` | FP32 | `(64)` | 66 | 4.2K |
| [Roblox/cube3d-v0.1](https://huggingface.co/Roblox/cube3d-v0.1) | `shape_tokenizer.safetensors` | FP32 | `(1, 768)` | 1 | 768 |
| [Roblox/cube3d-v0.1](https://huggingface.co/Roblox/cube3d-v0.1) | `shape_tokenizer.safetensors` | FP32 | `(3, 128)` | 1 | 384 |
| [Roblox/cube3d-v0.1](https://huggingface.co/Roblox/cube3d-v0.1) | `shape_tokenizer.safetensors` | FP32 | `(32)` | 5 | 160 |
| [Roblox/cube3d-v0.1](https://huggingface.co/Roblox/cube3d-v0.1) | `shape_tokenizer.safetensors` | FP32 | `(1)` | 1 | 1 |
| [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | `v1-5-pruned.safetensors` | FP32 | `(1280, 1280, 3, 3)` | 40 | 589.8M |
| [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | `v1-5-pruned.safetensors` | FP32 | `(1280, 2560, 3, 3)` | 10 | 294.9M |
| [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | `v1-5-pruned.safetensors` | FP32 | `(1280, 1280)` | 98 | 160.6M |
| [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | `v1-5-pruned.safetensors` | FP32 | `(10240, 1280)` | 12 | 157.3M |
| [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | `v1-5-pruned.safetensors` | FP32 | `(1280, 5120)` | 12 | 78.6M |
| [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | `v1-5-pruned.safetensors` | FP32 | `(512, 512, 3, 3)` | 30 | 70.8M |
| [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | `v1-5-pruned.safetensors` | FP32 | `(640, 640, 3, 3)` | 16 | 59.0M |
| [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | `v1-5-pruned.safetensors` | FP32 | `(1280, 1920, 3, 3)` | 2 | 44.2M |
| [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | `v1-5-pruned.safetensors` | FP32 | `(1280, 1280, 1, 1)` | 24 | 39.3M |
| [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | `v1-5-pruned.safetensors` | FP32 | `(49408, 768)` | 1 | 37.9M |
| [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | `v1-5-pruned.safetensors` | FP32 | `(1280, 2560, 1, 1)` | 10 | 32.8M |
| [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | `v1-5-pruned.safetensors` | FP32 | `(5120, 640)` | 10 | 32.8M |
| [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | `v1-5-pruned.safetensors` | FP32 | `(3072, 768)` | 12 | 28.3M |
| [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | `v1-5-pruned.safetensors` | FP32 | `(768, 3072)` | 12 | 28.3M |
| [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | `v1-5-pruned.safetensors` | FP32 | `(768, 768)` | 48 | 28.3M |
| [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | `v1-5-pruned.safetensors` | FP32 | `(640, 640)` | 60 | 24.6M |
| [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | `v1-5-pruned.safetensors` | FP32 | `(1280, 768)` | 24 | 23.6M |
| [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | `v1-5-pruned.safetensors` | FP32 | `(640, 1920, 3, 3)` | 2 | 22.1M |
| [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | `v1-5-pruned.safetensors` | FP32 | `(640, 2560)` | 10 | 16.4M |
| [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | `v1-5-pruned.safetensors` | FP32 | `(1280, 640, 3, 3)` | 2 | 14.7M |
| [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | `v1-5-pruned.safetensors` | FP32 | `(320, 320, 3, 3)` | 16 | 14.7M |
| [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | `v1-5-pruned.safetensors` | FP32 | `(640, 1280, 3, 3)` | 2 | 14.7M |
| [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | `v1-5-pruned.safetensors` | FP32 | `(640, 960, 3, 3)` | 2 | 11.1M |
| [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | `v1-5-pruned.safetensors` | FP32 | `(640, 768)` | 20 | 9.8M |
| [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | `v1-5-pruned.safetensors` | FP32 | `(2560, 320)` | 10 | 8.2M |
| [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | `v1-5-pruned.safetensors` | FP32 | `(320, 1280)` | 20 | 8.2M |
| [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | `v1-5-pruned.safetensors` | FP32 | `(640, 1280)` | 10 | 8.2M |
| [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | `v1-5-pruned.safetensors` | FP32 | `(640, 640, 1, 1)` | 20 | 8.2M |
| [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | `v1-5-pruned.safetensors` | FP32 | `(320, 640, 3, 3)` | 4 | 7.4M |
| [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | `v1-5-pruned.safetensors` | FP32 | `(320, 320)` | 60 | 6.1M |
| [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | `v1-5-pruned.safetensors` | FP32 | `(256, 256, 3, 3)` | 10 | 5.9M |
| [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | `v1-5-pruned.safetensors` | FP32 | `(320, 960, 3, 3)` | 2 | 5.5M |
| [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | `v1-5-pruned.safetensors` | FP32 | `(1280, 1920, 1, 1)` | 2 | 4.9M |
| [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | `v1-5-pruned.safetensors` | FP32 | `(320, 768)` | 20 | 4.9M |
| [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | `v1-5-pruned.safetensors` | FP32 | `(640, 320, 3, 3)` | 2 | 3.7M |
| [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | `v1-5-pruned.safetensors` | FP32 | `(640, 1920, 1, 1)` | 2 | 2.5M |
| [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | `v1-5-pruned.safetensors` | FP32 | `(512, 512, 1, 1)` | 8 | 2.1M |
| [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | `v1-5-pruned.safetensors` | FP32 | `(320, 320, 1, 1)` | 20 | 2.0M |
| [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | `v1-5-pruned.safetensors` | FP32 | `(1280, 640, 1, 1)` | 2 | 1.6M |
| [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | `v1-5-pruned.safetensors` | FP32 | `(640, 1280, 1, 1)` | 2 | 1.6M |
| [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | `v1-5-pruned.safetensors` | FP32 | `(128, 128, 3, 3)` | 10 | 1.5M |
| [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | `v1-5-pruned.safetensors` | FP32 | `(640, 960, 1, 1)` | 2 | 1.2M |
| [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | `v1-5-pruned.safetensors` | FP32 | `(256, 512, 3, 3)` | 1 | 1.2M |
| [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | `v1-5-pruned.safetensors` | FP32 | `(512, 256, 3, 3)` | 1 | 1.2M |
| [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | `v1-5-pruned.safetensors` | FP32 | `(1280, 320)` | 2 | 819.2K |
| [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | `v1-5-pruned.safetensors` | FP32 | `(320, 640, 1, 1)` | 4 | 819.2K |
| [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | `v1-5-pruned.safetensors` | FP32 | `(320, 960, 1, 1)` | 2 | 614.4K |
| [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | `v1-5-pruned.safetensors` | FP32 | `(1280)` | 324 | 414.7K |
| [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | `v1-5-pruned.safetensors` | FP32 | `(640, 320, 1, 1)` | 2 | 409.6K |
| [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | `v1-5-pruned.safetensors` | FP32 | `(128, 256, 3, 3)` | 1 | 294.9K |
| [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | `v1-5-pruned.safetensors` | FP32 | `(256, 128, 3, 3)` | 1 | 294.9K |
| [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | `v1-5-pruned.safetensors` | FP32 | `(640)` | 208 | 133.1K |
| [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | `v1-5-pruned.safetensors` | FP32 | `(256, 512, 1, 1)` | 1 | 131.1K |
| [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | `v1-5-pruned.safetensors` | FP32 | `(512, 256, 1, 1)` | 1 | 131.1K |
| [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | `v1-5-pruned.safetensors` | FP32 | `(10240)` | 12 | 122.9K |
| [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | `v1-5-pruned.safetensors` | FP32 | `(768)` | 110 | 84.5K |
| [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | `v1-5-pruned.safetensors` | FP32 | `(2560)` | 30 | 76.8K |
| [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | `v1-5-pruned.safetensors` | FP32 | `(320)` | 206 | 65.9K |
| [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | `v1-5-pruned.safetensors` | FP32 | `(77, 768)` | 1 | 59.1K |
| [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | `v1-5-pruned.safetensors` | FP32 | `(512)` | 103 | 52.7K |
| [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | `v1-5-pruned.safetensors` | FP32 | `(5120)` | 10 | 51.2K |
| [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | `v1-5-pruned.safetensors` | FP32 | `(3072)` | 12 | 36.9K |
| [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | `v1-5-pruned.safetensors` | FP32 | `(8, 512, 3, 3)` | 1 | 36.9K |
| [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | `v1-5-pruned.safetensors` | FP32 | `(128, 256, 1, 1)` | 1 | 32.8K |
| [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | `v1-5-pruned.safetensors` | FP32 | `(256, 128, 1, 1)` | 1 | 32.8K |
| [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | `v1-5-pruned.safetensors` | FP32 | `(320, 4, 3, 3)` | 2 | 23.0K |
| [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | `v1-5-pruned.safetensors` | FP32 | `(4, 320, 3, 3)` | 2 | 23.0K |
| [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | `v1-5-pruned.safetensors` | FP32 | `(512, 4, 3, 3)` | 1 | 18.4K |
| [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | `v1-5-pruned.safetensors` | FP32 | `(1920)` | 8 | 15.4K |
| [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | `v1-5-pruned.safetensors` | FP32 | `(1000)` | 12 | 12.0K |
| [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | `v1-5-pruned.safetensors` | FP32 | `(256)` | 34 | 8.7K |
| [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | `v1-5-pruned.safetensors` | FP32 | `(960)` | 8 | 7.7K |
| [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | `v1-5-pruned.safetensors` | FP32 | `(128)` | 35 | 4.5K |
| [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | `v1-5-pruned.safetensors` | FP32 | `(128, 3, 3, 3)` | 1 | 3.5K |
| [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | `v1-5-pruned.safetensors` | FP32 | `(3, 128, 3, 3)` | 1 | 3.5K |
| [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | `v1-5-pruned.safetensors` | FP32 | `(8, 8, 1, 1)` | 1 | 64 |
| [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | `v1-5-pruned.safetensors` | FP32 | `(4, 4, 1, 1)` | 1 | 16 |
| [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | `v1-5-pruned.safetensors` | FP32 | `(8)` | 2 | 16 |
| [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | `v1-5-pruned.safetensors` | FP32 | `(4)` | 3 | 12 |
| [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | `v1-5-pruned.safetensors` | FP32 | `(3)` | 1 | 3 |
| [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | `v1-5-pruned.safetensors` | FP32 | `()` | 1 | 1 |
| [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | `v1-5-pruned.safetensors` | INT32 | `()` | 1 | 1 |
| [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | `v1-5-pruned.safetensors` | INT64 | `(1, 77)` | 1 | 77 |
| [sayakpaul/FLUX.1-merged](https://huggingface.co/sayakpaul/FLUX.1-merged) | `text_encoder_2/model-00001-of-00002.safetensors` | BF16 | `(10240, 4096)` | 24 | 1.01B |
| [sayakpaul/FLUX.1-merged](https://huggingface.co/sayakpaul/FLUX.1-merged) | `text_encoder_2/model-00002-of-00002.safetensors` | BF16 | `(10240, 4096)` | 24 | 1.01B |
| [sayakpaul/FLUX.1-merged](https://huggingface.co/sayakpaul/FLUX.1-merged) | `text_encoder_2/model-00001-of-00002.safetensors` | BF16 | `(4096, 4096)` | 51 | 855.6M |
| [sayakpaul/FLUX.1-merged](https://huggingface.co/sayakpaul/FLUX.1-merged) | `text_encoder_2/model-00002-of-00002.safetensors` | BF16 | `(4096, 4096)` | 45 | 755.0M |
| [sayakpaul/FLUX.1-merged](https://huggingface.co/sayakpaul/FLUX.1-merged) | `text_encoder_2/model-00001-of-00002.safetensors` | BF16 | `(4096, 10240)` | 12 | 503.3M |
| [sayakpaul/FLUX.1-merged](https://huggingface.co/sayakpaul/FLUX.1-merged) | `text_encoder_2/model-00002-of-00002.safetensors` | BF16 | `(4096, 10240)` | 12 | 503.3M |
| [sayakpaul/FLUX.1-merged](https://huggingface.co/sayakpaul/FLUX.1-merged) | `text_encoder_2/model-00001-of-00002.safetensors` | BF16 | `(32128, 4096)` | 1 | 131.6M |
| [sayakpaul/FLUX.1-merged](https://huggingface.co/sayakpaul/FLUX.1-merged) | `text_encoder/model.safetensors` | BF16 | `(49408, 768)` | 1 | 37.9M |
| [sayakpaul/FLUX.1-merged](https://huggingface.co/sayakpaul/FLUX.1-merged) | `text_encoder/model.safetensors` | BF16 | `(3072, 768)` | 12 | 28.3M |
| [sayakpaul/FLUX.1-merged](https://huggingface.co/sayakpaul/FLUX.1-merged) | `text_encoder/model.safetensors` | BF16 | `(768, 3072)` | 12 | 28.3M |
| [sayakpaul/FLUX.1-merged](https://huggingface.co/sayakpaul/FLUX.1-merged) | `text_encoder/model.safetensors` | BF16 | `(768, 768)` | 48 | 28.3M |
| [sayakpaul/FLUX.1-merged](https://huggingface.co/sayakpaul/FLUX.1-merged) | `text_encoder_2/model-00002-of-00002.safetensors` | BF16 | `(4096)` | 25 | 102.4K |
| [sayakpaul/FLUX.1-merged](https://huggingface.co/sayakpaul/FLUX.1-merged) | `text_encoder_2/model-00001-of-00002.safetensors` | BF16 | `(4096)` | 24 | 98.3K |
| [sayakpaul/FLUX.1-merged](https://huggingface.co/sayakpaul/FLUX.1-merged) | `text_encoder/model.safetensors` | BF16 | `(768)` | 110 | 84.5K |
| [sayakpaul/FLUX.1-merged](https://huggingface.co/sayakpaul/FLUX.1-merged) | `text_encoder/model.safetensors` | BF16 | `(77, 768)` | 1 | 59.1K |
| [sayakpaul/FLUX.1-merged](https://huggingface.co/sayakpaul/FLUX.1-merged) | `text_encoder/model.safetensors` | BF16 | `(3072)` | 12 | 36.9K |
| [sayakpaul/FLUX.1-merged](https://huggingface.co/sayakpaul/FLUX.1-merged) | `text_encoder_2/model-00001-of-00002.safetensors` | BF16 | `(32, 64)` | 1 | 2.0K |
| [stabilityai/sd-turbo](https://huggingface.co/stabilityai/sd-turbo) | `sd_turbo.safetensors` | FP32 | `(1280, 1280, 3, 3)` | 20 | 294.9M |
| [stabilityai/sd-turbo](https://huggingface.co/stabilityai/sd-turbo) | `sd_turbo.safetensors` | FP32 | `(1280, 2560, 3, 3)` | 5 | 147.5M |
| [stabilityai/sd-turbo](https://huggingface.co/stabilityai/sd-turbo) | `sd_turbo.safetensors` | FP32 | `(1024, 4096)` | 24 | 100.7M |
| [stabilityai/sd-turbo](https://huggingface.co/stabilityai/sd-turbo) | `sd_turbo.safetensors` | FP32 | `(4096, 1024)` | 24 | 100.7M |
| [stabilityai/sd-turbo](https://huggingface.co/stabilityai/sd-turbo) | `sd_turbo.safetensors` | FP32 | `(1280, 1280)` | 61 | 99.9M |
| [stabilityai/sd-turbo](https://huggingface.co/stabilityai/sd-turbo) | `sd_turbo.safetensors` | FP32 | `(10240, 1280)` | 6 | 78.6M |
| [stabilityai/sd-turbo](https://huggingface.co/stabilityai/sd-turbo) | `sd_turbo.safetensors` | FP32 | `(3072, 1024)` | 24 | 75.5M |
| [stabilityai/sd-turbo](https://huggingface.co/stabilityai/sd-turbo) | `sd_turbo.safetensors` | FP32 | `(512, 512, 3, 3)` | 30 | 70.8M |
| [stabilityai/sd-turbo](https://huggingface.co/stabilityai/sd-turbo) | `sd_turbo.safetensors` | FP32 | `(49408, 1024)` | 1 | 50.6M |
| [stabilityai/sd-turbo](https://huggingface.co/stabilityai/sd-turbo) | `sd_turbo.safetensors` | FP32 | `(1280, 5120)` | 6 | 39.3M |
| [stabilityai/sd-turbo](https://huggingface.co/stabilityai/sd-turbo) | `sd_turbo.safetensors` | FP32 | `(640, 640, 3, 3)` | 8 | 29.5M |
| [stabilityai/sd-turbo](https://huggingface.co/stabilityai/sd-turbo) | `sd_turbo.safetensors` | FP32 | `(1024, 1024)` | 25 | 26.2M |
| [stabilityai/sd-turbo](https://huggingface.co/stabilityai/sd-turbo) | `sd_turbo.safetensors` | FP32 | `(1280, 1920, 3, 3)` | 1 | 22.1M |
| [stabilityai/sd-turbo](https://huggingface.co/stabilityai/sd-turbo) | `sd_turbo.safetensors` | FP32 | `(1280, 2560, 1, 1)` | 5 | 16.4M |
| [stabilityai/sd-turbo](https://huggingface.co/stabilityai/sd-turbo) | `sd_turbo.safetensors` | FP32 | `(5120, 640)` | 5 | 16.4M |
| [stabilityai/sd-turbo](https://huggingface.co/stabilityai/sd-turbo) | `sd_turbo.safetensors` | FP32 | `(640, 640)` | 40 | 16.4M |
| [stabilityai/sd-turbo](https://huggingface.co/stabilityai/sd-turbo) | `sd_turbo.safetensors` | FP32 | `(1280, 1024)` | 12 | 15.7M |
| [stabilityai/sd-turbo](https://huggingface.co/stabilityai/sd-turbo) | `sd_turbo.safetensors` | FP32 | `(640, 1920, 3, 3)` | 1 | 11.1M |
| [stabilityai/sd-turbo](https://huggingface.co/stabilityai/sd-turbo) | `sd_turbo.safetensors` | FP32 | `(640, 2560)` | 5 | 8.2M |
| [stabilityai/sd-turbo](https://huggingface.co/stabilityai/sd-turbo) | `sd_turbo.safetensors` | FP32 | `(1280, 640, 3, 3)` | 1 | 7.4M |
| [stabilityai/sd-turbo](https://huggingface.co/stabilityai/sd-turbo) | `sd_turbo.safetensors` | FP32 | `(320, 320, 3, 3)` | 8 | 7.4M |
| [stabilityai/sd-turbo](https://huggingface.co/stabilityai/sd-turbo) | `sd_turbo.safetensors` | FP32 | `(640, 1280, 3, 3)` | 1 | 7.4M |
| [stabilityai/sd-turbo](https://huggingface.co/stabilityai/sd-turbo) | `sd_turbo.safetensors` | FP32 | `(640, 1024)` | 10 | 6.6M |
| [stabilityai/sd-turbo](https://huggingface.co/stabilityai/sd-turbo) | `sd_turbo.safetensors` | FP32 | `(256, 256, 3, 3)` | 10 | 5.9M |
| [stabilityai/sd-turbo](https://huggingface.co/stabilityai/sd-turbo) | `sd_turbo.safetensors` | FP32 | `(640, 960, 3, 3)` | 1 | 5.5M |
| [stabilityai/sd-turbo](https://huggingface.co/stabilityai/sd-turbo) | `sd_turbo.safetensors` | FP32 | `(2560, 320)` | 5 | 4.1M |
| [stabilityai/sd-turbo](https://huggingface.co/stabilityai/sd-turbo) | `sd_turbo.safetensors` | FP32 | `(320, 1280)` | 10 | 4.1M |
| [stabilityai/sd-turbo](https://huggingface.co/stabilityai/sd-turbo) | `sd_turbo.safetensors` | FP32 | `(320, 320)` | 40 | 4.1M |
| [stabilityai/sd-turbo](https://huggingface.co/stabilityai/sd-turbo) | `sd_turbo.safetensors` | FP32 | `(640, 1280)` | 5 | 4.1M |
| [stabilityai/sd-turbo](https://huggingface.co/stabilityai/sd-turbo) | `sd_turbo.safetensors` | FP32 | `(320, 640, 3, 3)` | 2 | 3.7M |
| [stabilityai/sd-turbo](https://huggingface.co/stabilityai/sd-turbo) | `sd_turbo.safetensors` | FP32 | `(320, 1024)` | 10 | 3.3M |
| [stabilityai/sd-turbo](https://huggingface.co/stabilityai/sd-turbo) | `sd_turbo.safetensors` | FP32 | `(320, 960, 3, 3)` | 1 | 2.8M |
| [stabilityai/sd-turbo](https://huggingface.co/stabilityai/sd-turbo) | `sd_turbo.safetensors` | FP32 | `(1280, 1920, 1, 1)` | 1 | 2.5M |
| [stabilityai/sd-turbo](https://huggingface.co/stabilityai/sd-turbo) | `sd_turbo.safetensors` | FP32 | `(512, 512, 1, 1)` | 8 | 2.1M |
| [stabilityai/sd-turbo](https://huggingface.co/stabilityai/sd-turbo) | `sd_turbo.safetensors` | FP32 | `(640, 320, 3, 3)` | 1 | 1.8M |
| [stabilityai/sd-turbo](https://huggingface.co/stabilityai/sd-turbo) | `sd_turbo.safetensors` | FP32 | `(128, 128, 3, 3)` | 10 | 1.5M |
| [stabilityai/sd-turbo](https://huggingface.co/stabilityai/sd-turbo) | `sd_turbo.safetensors` | FP32 | `(640, 1920, 1, 1)` | 1 | 1.2M |
| [stabilityai/sd-turbo](https://huggingface.co/stabilityai/sd-turbo) | `sd_turbo.safetensors` | FP32 | `(256, 512, 3, 3)` | 1 | 1.2M |
| [stabilityai/sd-turbo](https://huggingface.co/stabilityai/sd-turbo) | `sd_turbo.safetensors` | FP32 | `(512, 256, 3, 3)` | 1 | 1.2M |
| [stabilityai/sd-turbo](https://huggingface.co/stabilityai/sd-turbo) | `sd_turbo.safetensors` | FP32 | `(1280, 640, 1, 1)` | 1 | 819.2K |
| [stabilityai/sd-turbo](https://huggingface.co/stabilityai/sd-turbo) | `sd_turbo.safetensors` | FP32 | `(640, 1280, 1, 1)` | 1 | 819.2K |
| [stabilityai/sd-turbo](https://huggingface.co/stabilityai/sd-turbo) | `sd_turbo.safetensors` | FP32 | `(640, 960, 1, 1)` | 1 | 614.4K |
| [stabilityai/sd-turbo](https://huggingface.co/stabilityai/sd-turbo) | `sd_turbo.safetensors` | FP32 | `(1280, 320)` | 1 | 409.6K |
| [stabilityai/sd-turbo](https://huggingface.co/stabilityai/sd-turbo) | `sd_turbo.safetensors` | FP32 | `(320, 640, 1, 1)` | 2 | 409.6K |
| [stabilityai/sd-turbo](https://huggingface.co/stabilityai/sd-turbo) | `sd_turbo.safetensors` | FP32 | `(320, 960, 1, 1)` | 1 | 307.2K |
| [stabilityai/sd-turbo](https://huggingface.co/stabilityai/sd-turbo) | `sd_turbo.safetensors` | FP32 | `(128, 256, 3, 3)` | 1 | 294.9K |
| [stabilityai/sd-turbo](https://huggingface.co/stabilityai/sd-turbo) | `sd_turbo.safetensors` | FP32 | `(256, 128, 3, 3)` | 1 | 294.9K |
| [stabilityai/sd-turbo](https://huggingface.co/stabilityai/sd-turbo) | `sd_turbo.safetensors` | FP32 | `(1280)` | 162 | 207.4K |
| [stabilityai/sd-turbo](https://huggingface.co/stabilityai/sd-turbo) | `sd_turbo.safetensors` | FP32 | `(640, 320, 1, 1)` | 1 | 204.8K |
| [stabilityai/sd-turbo](https://huggingface.co/stabilityai/sd-turbo) | `sd_turbo.safetensors` | FP32 | `(1024)` | 146 | 149.5K |
| [stabilityai/sd-turbo](https://huggingface.co/stabilityai/sd-turbo) | `sd_turbo.safetensors` | FP32 | `(256, 512, 1, 1)` | 1 | 131.1K |
| [stabilityai/sd-turbo](https://huggingface.co/stabilityai/sd-turbo) | `sd_turbo.safetensors` | FP32 | `(512, 256, 1, 1)` | 1 | 131.1K |
| [stabilityai/sd-turbo](https://huggingface.co/stabilityai/sd-turbo) | `sd_turbo.safetensors` | FP32 | `(4096)` | 24 | 98.3K |
| [stabilityai/sd-turbo](https://huggingface.co/stabilityai/sd-turbo) | `sd_turbo.safetensors` | FP32 | `(77, 1024)` | 1 | 78.8K |
| [stabilityai/sd-turbo](https://huggingface.co/stabilityai/sd-turbo) | `sd_turbo.safetensors` | FP32 | `(3072)` | 24 | 73.7K |
| [stabilityai/sd-turbo](https://huggingface.co/stabilityai/sd-turbo) | `sd_turbo.safetensors` | FP32 | `(640)` | 104 | 66.6K |
| [stabilityai/sd-turbo](https://huggingface.co/stabilityai/sd-turbo) | `sd_turbo.safetensors` | FP32 | `(10240)` | 6 | 61.4K |
| [stabilityai/sd-turbo](https://huggingface.co/stabilityai/sd-turbo) | `sd_turbo.safetensors` | FP32 | `(512)` | 103 | 52.7K |
| [stabilityai/sd-turbo](https://huggingface.co/stabilityai/sd-turbo) | `sd_turbo.safetensors` | FP32 | `(2560)` | 15 | 38.4K |
| [stabilityai/sd-turbo](https://huggingface.co/stabilityai/sd-turbo) | `sd_turbo.safetensors` | FP32 | `(8, 512, 3, 3)` | 1 | 36.9K |
| [stabilityai/sd-turbo](https://huggingface.co/stabilityai/sd-turbo) | `sd_turbo.safetensors` | FP32 | `(320)` | 103 | 33.0K |
| [stabilityai/sd-turbo](https://huggingface.co/stabilityai/sd-turbo) | `sd_turbo.safetensors` | FP32 | `(128, 256, 1, 1)` | 1 | 32.8K |
| [stabilityai/sd-turbo](https://huggingface.co/stabilityai/sd-turbo) | `sd_turbo.safetensors` | FP32 | `(256, 128, 1, 1)` | 1 | 32.8K |
| [stabilityai/sd-turbo](https://huggingface.co/stabilityai/sd-turbo) | `sd_turbo.safetensors` | FP32 | `(5120)` | 5 | 25.6K |
| [stabilityai/sd-turbo](https://huggingface.co/stabilityai/sd-turbo) | `sd_turbo.safetensors` | FP32 | `(512, 4, 3, 3)` | 1 | 18.4K |
| [stabilityai/sd-turbo](https://huggingface.co/stabilityai/sd-turbo) | `sd_turbo.safetensors` | FP32 | `(320, 4, 3, 3)` | 1 | 11.5K |
| [stabilityai/sd-turbo](https://huggingface.co/stabilityai/sd-turbo) | `sd_turbo.safetensors` | FP32 | `(4, 320, 3, 3)` | 1 | 11.5K |
| [stabilityai/sd-turbo](https://huggingface.co/stabilityai/sd-turbo) | `sd_turbo.safetensors` | FP32 | `(256)` | 34 | 8.7K |
| [stabilityai/sd-turbo](https://huggingface.co/stabilityai/sd-turbo) | `sd_turbo.safetensors` | FP32 | `(1920)` | 4 | 7.7K |
| [stabilityai/sd-turbo](https://huggingface.co/stabilityai/sd-turbo) | `sd_turbo.safetensors` | FP32 | `(128)` | 35 | 4.5K |
| [stabilityai/sd-turbo](https://huggingface.co/stabilityai/sd-turbo) | `sd_turbo.safetensors` | FP32 | `(960)` | 4 | 3.8K |
| [stabilityai/sd-turbo](https://huggingface.co/stabilityai/sd-turbo) | `sd_turbo.safetensors` | FP32 | `(128, 3, 3, 3)` | 1 | 3.5K |
| [stabilityai/sd-turbo](https://huggingface.co/stabilityai/sd-turbo) | `sd_turbo.safetensors` | FP32 | `(3, 128, 3, 3)` | 1 | 3.5K |
| [stabilityai/sd-turbo](https://huggingface.co/stabilityai/sd-turbo) | `sd_turbo.safetensors` | FP32 | `(1000)` | 1 | 1.0K |
| [stabilityai/sd-turbo](https://huggingface.co/stabilityai/sd-turbo) | `sd_turbo.safetensors` | FP32 | `(8, 8, 1, 1)` | 1 | 64 |
| [stabilityai/sd-turbo](https://huggingface.co/stabilityai/sd-turbo) | `sd_turbo.safetensors` | FP32 | `(4, 4, 1, 1)` | 1 | 16 |
| [stabilityai/sd-turbo](https://huggingface.co/stabilityai/sd-turbo) | `sd_turbo.safetensors` | FP32 | `(8)` | 2 | 16 |
| [stabilityai/sd-turbo](https://huggingface.co/stabilityai/sd-turbo) | `sd_turbo.safetensors` | FP32 | `(4)` | 2 | 8 |
| [stabilityai/sd-turbo](https://huggingface.co/stabilityai/sd-turbo) | `sd_turbo.safetensors` | FP32 | `(3)` | 1 | 3 |
| [stabilityai/sd-turbo](https://huggingface.co/stabilityai/sd-turbo) | `sd_turbo.safetensors` | FP32 | `()` | 1 | 1 |
| [stabilityai/sd-vae-ft-mse](https://huggingface.co/stabilityai/sd-vae-ft-mse) | `diffusion_pytorch_model.safetensors` | FP32 | `(512, 512, 3, 3)` | 30 | 70.8M |
| [stabilityai/sd-vae-ft-mse](https://huggingface.co/stabilityai/sd-vae-ft-mse) | `diffusion_pytorch_model.safetensors` | FP32 | `(256, 256, 3, 3)` | 10 | 5.9M |
| [stabilityai/sd-vae-ft-mse](https://huggingface.co/stabilityai/sd-vae-ft-mse) | `diffusion_pytorch_model.safetensors` | FP32 | `(512, 512)` | 8 | 2.1M |
| [stabilityai/sd-vae-ft-mse](https://huggingface.co/stabilityai/sd-vae-ft-mse) | `diffusion_pytorch_model.safetensors` | FP32 | `(128, 128, 3, 3)` | 10 | 1.5M |
| [stabilityai/sd-vae-ft-mse](https://huggingface.co/stabilityai/sd-vae-ft-mse) | `diffusion_pytorch_model.safetensors` | FP32 | `(256, 512, 3, 3)` | 1 | 1.2M |
| [stabilityai/sd-vae-ft-mse](https://huggingface.co/stabilityai/sd-vae-ft-mse) | `diffusion_pytorch_model.safetensors` | FP32 | `(512, 256, 3, 3)` | 1 | 1.2M |
| [stabilityai/sd-vae-ft-mse](https://huggingface.co/stabilityai/sd-vae-ft-mse) | `diffusion_pytorch_model.safetensors` | FP32 | `(128, 256, 3, 3)` | 1 | 294.9K |
| [stabilityai/sd-vae-ft-mse](https://huggingface.co/stabilityai/sd-vae-ft-mse) | `diffusion_pytorch_model.safetensors` | FP32 | `(256, 128, 3, 3)` | 1 | 294.9K |
| [stabilityai/sd-vae-ft-mse](https://huggingface.co/stabilityai/sd-vae-ft-mse) | `diffusion_pytorch_model.safetensors` | FP32 | `(256, 512, 1, 1)` | 1 | 131.1K |
| [stabilityai/sd-vae-ft-mse](https://huggingface.co/stabilityai/sd-vae-ft-mse) | `diffusion_pytorch_model.safetensors` | FP32 | `(512, 256, 1, 1)` | 1 | 131.1K |
| [stabilityai/sd-vae-ft-mse](https://huggingface.co/stabilityai/sd-vae-ft-mse) | `diffusion_pytorch_model.safetensors` | FP32 | `(512)` | 103 | 52.7K |
| [stabilityai/sd-vae-ft-mse](https://huggingface.co/stabilityai/sd-vae-ft-mse) | `diffusion_pytorch_model.safetensors` | FP32 | `(8, 512, 3, 3)` | 1 | 36.9K |
| [stabilityai/sd-vae-ft-mse](https://huggingface.co/stabilityai/sd-vae-ft-mse) | `diffusion_pytorch_model.safetensors` | FP32 | `(128, 256, 1, 1)` | 1 | 32.8K |
| [stabilityai/sd-vae-ft-mse](https://huggingface.co/stabilityai/sd-vae-ft-mse) | `diffusion_pytorch_model.safetensors` | FP32 | `(256, 128, 1, 1)` | 1 | 32.8K |
| [stabilityai/sd-vae-ft-mse](https://huggingface.co/stabilityai/sd-vae-ft-mse) | `diffusion_pytorch_model.safetensors` | FP32 | `(512, 4, 3, 3)` | 1 | 18.4K |
| [stabilityai/sd-vae-ft-mse](https://huggingface.co/stabilityai/sd-vae-ft-mse) | `diffusion_pytorch_model.safetensors` | FP32 | `(256)` | 34 | 8.7K |
| [stabilityai/sd-vae-ft-mse](https://huggingface.co/stabilityai/sd-vae-ft-mse) | `diffusion_pytorch_model.safetensors` | FP32 | `(128)` | 35 | 4.5K |
| [stabilityai/sd-vae-ft-mse](https://huggingface.co/stabilityai/sd-vae-ft-mse) | `diffusion_pytorch_model.safetensors` | FP32 | `(128, 3, 3, 3)` | 1 | 3.5K |
| [stabilityai/sd-vae-ft-mse](https://huggingface.co/stabilityai/sd-vae-ft-mse) | `diffusion_pytorch_model.safetensors` | FP32 | `(3, 128, 3, 3)` | 1 | 3.5K |
| [stabilityai/sd-vae-ft-mse](https://huggingface.co/stabilityai/sd-vae-ft-mse) | `diffusion_pytorch_model.safetensors` | FP32 | `(8, 8, 1, 1)` | 1 | 64 |
| [stabilityai/sd-vae-ft-mse](https://huggingface.co/stabilityai/sd-vae-ft-mse) | `diffusion_pytorch_model.safetensors` | FP32 | `(4, 4, 1, 1)` | 1 | 16 |
| [stabilityai/sd-vae-ft-mse](https://huggingface.co/stabilityai/sd-vae-ft-mse) | `diffusion_pytorch_model.safetensors` | FP32 | `(8)` | 2 | 16 |
| [stabilityai/sd-vae-ft-mse](https://huggingface.co/stabilityai/sd-vae-ft-mse) | `diffusion_pytorch_model.safetensors` | FP32 | `(4)` | 1 | 4 |
| [stabilityai/sd-vae-ft-mse](https://huggingface.co/stabilityai/sd-vae-ft-mse) | `diffusion_pytorch_model.safetensors` | FP32 | `(3)` | 1 | 3 |
| [stabilityai/sd-vae-ft-mse-original](https://huggingface.co/stabilityai/sd-vae-ft-mse-original) | `vae-ft-mse-840000-ema-pruned.safetensors` | FP32 | `(512, 512, 3, 3)` | 30 | 70.8M |
| [stabilityai/sd-vae-ft-mse-original](https://huggingface.co/stabilityai/sd-vae-ft-mse-original) | `vae-ft-mse-840000-ema-pruned.safetensors` | FP32 | `(256, 256, 3, 3)` | 10 | 5.9M |
| [stabilityai/sd-vae-ft-mse-original](https://huggingface.co/stabilityai/sd-vae-ft-mse-original) | `vae-ft-mse-840000-ema-pruned.safetensors` | FP32 | `(512, 512, 1, 1)` | 8 | 2.1M |
| [stabilityai/sd-vae-ft-mse-original](https://huggingface.co/stabilityai/sd-vae-ft-mse-original) | `vae-ft-mse-840000-ema-pruned.safetensors` | FP32 | `(128, 128, 3, 3)` | 10 | 1.5M |
| [stabilityai/sd-vae-ft-mse-original](https://huggingface.co/stabilityai/sd-vae-ft-mse-original) | `vae-ft-mse-840000-ema-pruned.safetensors` | FP32 | `(256, 512, 3, 3)` | 1 | 1.2M |
| [stabilityai/sd-vae-ft-mse-original](https://huggingface.co/stabilityai/sd-vae-ft-mse-original) | `vae-ft-mse-840000-ema-pruned.safetensors` | FP32 | `(512, 256, 3, 3)` | 1 | 1.2M |
| [stabilityai/sd-vae-ft-mse-original](https://huggingface.co/stabilityai/sd-vae-ft-mse-original) | `vae-ft-mse-840000-ema-pruned.safetensors` | FP32 | `(128, 256, 3, 3)` | 1 | 294.9K |
| [stabilityai/sd-vae-ft-mse-original](https://huggingface.co/stabilityai/sd-vae-ft-mse-original) | `vae-ft-mse-840000-ema-pruned.safetensors` | FP32 | `(256, 128, 3, 3)` | 1 | 294.9K |
| [stabilityai/sd-vae-ft-mse-original](https://huggingface.co/stabilityai/sd-vae-ft-mse-original) | `vae-ft-mse-840000-ema-pruned.safetensors` | FP32 | `(256, 512, 1, 1)` | 1 | 131.1K |
| [stabilityai/sd-vae-ft-mse-original](https://huggingface.co/stabilityai/sd-vae-ft-mse-original) | `vae-ft-mse-840000-ema-pruned.safetensors` | FP32 | `(512, 256, 1, 1)` | 1 | 131.1K |
| [stabilityai/sd-vae-ft-mse-original](https://huggingface.co/stabilityai/sd-vae-ft-mse-original) | `vae-ft-mse-840000-ema-pruned.safetensors` | FP32 | `(512)` | 103 | 52.7K |
| [stabilityai/sd-vae-ft-mse-original](https://huggingface.co/stabilityai/sd-vae-ft-mse-original) | `vae-ft-mse-840000-ema-pruned.safetensors` | FP32 | `(8, 512, 3, 3)` | 1 | 36.9K |
| [stabilityai/sd-vae-ft-mse-original](https://huggingface.co/stabilityai/sd-vae-ft-mse-original) | `vae-ft-mse-840000-ema-pruned.safetensors` | FP32 | `(128, 256, 1, 1)` | 1 | 32.8K |
| [stabilityai/sd-vae-ft-mse-original](https://huggingface.co/stabilityai/sd-vae-ft-mse-original) | `vae-ft-mse-840000-ema-pruned.safetensors` | FP32 | `(256, 128, 1, 1)` | 1 | 32.8K |
| [stabilityai/sd-vae-ft-mse-original](https://huggingface.co/stabilityai/sd-vae-ft-mse-original) | `vae-ft-mse-840000-ema-pruned.safetensors` | FP32 | `(512, 4, 3, 3)` | 1 | 18.4K |
| [stabilityai/sd-vae-ft-mse-original](https://huggingface.co/stabilityai/sd-vae-ft-mse-original) | `vae-ft-mse-840000-ema-pruned.safetensors` | FP32 | `(256)` | 34 | 8.7K |
| [stabilityai/sd-vae-ft-mse-original](https://huggingface.co/stabilityai/sd-vae-ft-mse-original) | `vae-ft-mse-840000-ema-pruned.safetensors` | FP32 | `(128)` | 35 | 4.5K |
| [stabilityai/sd-vae-ft-mse-original](https://huggingface.co/stabilityai/sd-vae-ft-mse-original) | `vae-ft-mse-840000-ema-pruned.safetensors` | FP32 | `(128, 3, 3, 3)` | 1 | 3.5K |
| [stabilityai/sd-vae-ft-mse-original](https://huggingface.co/stabilityai/sd-vae-ft-mse-original) | `vae-ft-mse-840000-ema-pruned.safetensors` | FP32 | `(3, 128, 3, 3)` | 1 | 3.5K |
| [stabilityai/sd-vae-ft-mse-original](https://huggingface.co/stabilityai/sd-vae-ft-mse-original) | `vae-ft-mse-840000-ema-pruned.safetensors` | FP32 | `(8, 8, 1, 1)` | 1 | 64 |
| [stabilityai/sd-vae-ft-mse-original](https://huggingface.co/stabilityai/sd-vae-ft-mse-original) | `vae-ft-mse-840000-ema-pruned.safetensors` | FP32 | `(4, 4, 1, 1)` | 1 | 16 |
| [stabilityai/sd-vae-ft-mse-original](https://huggingface.co/stabilityai/sd-vae-ft-mse-original) | `vae-ft-mse-840000-ema-pruned.safetensors` | FP32 | `(8)` | 2 | 16 |
| [stabilityai/sd-vae-ft-mse-original](https://huggingface.co/stabilityai/sd-vae-ft-mse-original) | `vae-ft-mse-840000-ema-pruned.safetensors` | FP32 | `(4)` | 1 | 4 |
| [stabilityai/sd-vae-ft-mse-original](https://huggingface.co/stabilityai/sd-vae-ft-mse-original) | `vae-ft-mse-840000-ema-pruned.safetensors` | FP32 | `(3)` | 1 | 3 |
| [stabilityai/sd-vae-ft-mse-original](https://huggingface.co/stabilityai/sd-vae-ft-mse-original) | `vae-ft-mse-840000-ema-pruned.safetensors` | FP32 | `()` | 1 | 1 |
| [stabilityai/sd-vae-ft-mse-original](https://huggingface.co/stabilityai/sd-vae-ft-mse-original) | `vae-ft-mse-840000-ema-pruned.safetensors` | INT32 | `()` | 1 | 1 |
| [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) | `sd_xl_turbo_1.0_fp16.safetensors` | FP16 | `(10240, 1280)` | 60 | 786.4M |
| [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) | `sd_xl_turbo_1.0_fp16.safetensors` | FP16 | `(1280, 1280)` | 414 | 678.3M |
| [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) | `sd_xl_turbo_1.0_fp16.safetensors` | FP16 | `(1280, 5120)` | 92 | 602.9M |
| [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) | `sd_xl_turbo_1.0_fp16.safetensors` | FP16 | `(1280, 2048)` | 120 | 314.6M |
| [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) | `sd_xl_turbo_1.0_fp16.safetensors` | FP16 | `(5120, 1280)` | 32 | 209.7M |
| [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) | `sd_xl_turbo_1.0_fp16.safetensors` | FP16 | `(1280, 1280, 3, 3)` | 11 | 162.2M |
| [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) | `sd_xl_turbo_1.0_fp16.safetensors` | FP16 | `(3840, 1280)` | 32 | 157.3M |
| [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) | `sd_xl_turbo_1.0_fp16.safetensors` | FP16 | `(512, 512, 3, 3)` | 30 | 70.8M |
| [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) | `sd_xl_turbo_1.0_fp16.safetensors` | FP16 | `(49408, 1280)` | 1 | 63.2M |
| [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) | `sd_xl_turbo_1.0_fp16.safetensors` | FP16 | `(1280, 2560, 3, 3)` | 2 | 59.0M |
| [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) | `sd_xl_turbo_1.0_fp16.safetensors` | FP16 | `(49408, 768)` | 1 | 37.9M |
| [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) | `sd_xl_turbo_1.0_fp16.safetensors` | FP16 | `(5120, 640)` | 10 | 32.8M |
| [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) | `sd_xl_turbo_1.0_fp16.safetensors` | FP16 | `(640, 640, 3, 3)` | 8 | 29.5M |
| [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) | `sd_xl_turbo_1.0_fp16.safetensors` | FP16 | `(640, 640)` | 70 | 28.7M |
| [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) | `sd_xl_turbo_1.0_fp16.safetensors` | FP16 | `(3072, 768)` | 12 | 28.3M |
| [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) | `sd_xl_turbo_1.0_fp16.safetensors` | FP16 | `(768, 3072)` | 12 | 28.3M |
| [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) | `sd_xl_turbo_1.0_fp16.safetensors` | FP16 | `(768, 768)` | 48 | 28.3M |
| [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) | `sd_xl_turbo_1.0_fp16.safetensors` | FP16 | `(640, 2048)` | 20 | 26.2M |
| [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) | `sd_xl_turbo_1.0_fp16.safetensors` | FP16 | `(1280, 1920, 3, 3)` | 1 | 22.1M |
| [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) | `sd_xl_turbo_1.0_fp16.safetensors` | FP16 | `(640, 2560)` | 10 | 16.4M |
| [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) | `sd_xl_turbo_1.0_fp16.safetensors` | FP16 | `(640, 1920, 3, 3)` | 1 | 11.1M |
| [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) | `sd_xl_turbo_1.0_fp16.safetensors` | FP16 | `(1280, 640, 3, 3)` | 1 | 7.4M |
| [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) | `sd_xl_turbo_1.0_fp16.safetensors` | FP16 | `(320, 320, 3, 3)` | 8 | 7.4M |
| [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) | `sd_xl_turbo_1.0_fp16.safetensors` | FP16 | `(640, 1280, 3, 3)` | 1 | 7.4M |
| [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) | `sd_xl_turbo_1.0_fp16.safetensors` | FP16 | `(1280, 2560, 1, 1)` | 2 | 6.6M |
| [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) | `sd_xl_turbo_1.0_fp16.safetensors` | FP16 | `(256, 256, 3, 3)` | 10 | 5.9M |
| [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) | `sd_xl_turbo_1.0_fp16.safetensors` | FP16 | `(640, 960, 3, 3)` | 1 | 5.5M |
| [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) | `sd_xl_turbo_1.0_fp16.safetensors` | FP16 | `(640, 1280)` | 5 | 4.1M |
| [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) | `sd_xl_turbo_1.0_fp16.safetensors` | FP16 | `(320, 640, 3, 3)` | 2 | 3.7M |
| [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) | `sd_xl_turbo_1.0_fp16.safetensors` | FP16 | `(1280, 2816)` | 1 | 3.6M |
| [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) | `sd_xl_turbo_1.0_fp16.safetensors` | FP16 | `(320, 960, 3, 3)` | 1 | 2.8M |
| [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) | `sd_xl_turbo_1.0_fp16.safetensors` | FP16 | `(1280, 1920, 1, 1)` | 1 | 2.5M |
| [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) | `sd_xl_turbo_1.0_fp16.safetensors` | FP16 | `(512, 512, 1, 1)` | 8 | 2.1M |
| [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) | `sd_xl_turbo_1.0_fp16.safetensors` | FP16 | `(320, 1280)` | 5 | 2.0M |
| [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) | `sd_xl_turbo_1.0_fp16.safetensors` | FP16 | `(640, 320, 3, 3)` | 1 | 1.8M |
| [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) | `sd_xl_turbo_1.0_fp16.safetensors` | FP16 | `(128, 128, 3, 3)` | 10 | 1.5M |
| [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) | `sd_xl_turbo_1.0_fp16.safetensors` | FP16 | `(640, 1920, 1, 1)` | 1 | 1.2M |
| [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) | `sd_xl_turbo_1.0_fp16.safetensors` | FP16 | `(256, 512, 3, 3)` | 1 | 1.2M |
| [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) | `sd_xl_turbo_1.0_fp16.safetensors` | FP16 | `(512, 256, 3, 3)` | 1 | 1.2M |
| [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) | `sd_xl_turbo_1.0_fp16.safetensors` | FP16 | `(1280)` | 810 | 1.0M |
| [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) | `sd_xl_turbo_1.0_fp16.safetensors` | FP16 | `(1280, 640, 1, 1)` | 1 | 819.2K |
| [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) | `sd_xl_turbo_1.0_fp16.safetensors` | FP16 | `(640, 1280, 1, 1)` | 1 | 819.2K |
| [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) | `sd_xl_turbo_1.0_fp16.safetensors` | FP16 | `(10240)` | 60 | 614.4K |
| [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) | `sd_xl_turbo_1.0_fp16.safetensors` | FP16 | `(640, 960, 1, 1)` | 1 | 614.4K |
| [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) | `sd_xl_turbo_1.0_fp16.safetensors` | FP16 | `(1280, 320)` | 1 | 409.6K |
| [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) | `sd_xl_turbo_1.0_fp16.safetensors` | FP16 | `(320, 640, 1, 1)` | 2 | 409.6K |
| [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) | `sd_xl_turbo_1.0_fp16.safetensors` | FP16 | `(320, 960, 1, 1)` | 1 | 307.2K |
| [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) | `sd_xl_turbo_1.0_fp16.safetensors` | FP16 | `(128, 256, 3, 3)` | 1 | 294.9K |
| [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) | `sd_xl_turbo_1.0_fp16.safetensors` | FP16 | `(256, 128, 3, 3)` | 1 | 294.9K |
| [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) | `sd_xl_turbo_1.0_fp16.safetensors` | FP16 | `(5120)` | 42 | 215.0K |
| [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) | `sd_xl_turbo_1.0_fp16.safetensors` | FP16 | `(640, 320, 1, 1)` | 1 | 204.8K |
| [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) | `sd_xl_turbo_1.0_fp16.safetensors` | FP16 | `(256, 512, 1, 1)` | 1 | 131.1K |
| [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) | `sd_xl_turbo_1.0_fp16.safetensors` | FP16 | `(512, 256, 1, 1)` | 1 | 131.1K |
| [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) | `sd_xl_turbo_1.0_fp16.safetensors` | FP16 | `(3840)` | 32 | 122.9K |
| [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) | `sd_xl_turbo_1.0_fp16.safetensors` | FP16 | `(77, 1280)` | 1 | 98.6K |
| [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) | `sd_xl_turbo_1.0_fp16.safetensors` | FP16 | `(640)` | 149 | 95.4K |
| [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) | `sd_xl_turbo_1.0_fp16.safetensors` | FP16 | `(768)` | 110 | 84.5K |
| [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) | `sd_xl_turbo_1.0_fp16.safetensors` | FP16 | `(77, 768)` | 1 | 59.1K |
| [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) | `sd_xl_turbo_1.0_fp16.safetensors` | FP16 | `(512)` | 103 | 52.7K |
| [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) | `sd_xl_turbo_1.0_fp16.safetensors` | FP16 | `(3072)` | 12 | 36.9K |
| [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) | `sd_xl_turbo_1.0_fp16.safetensors` | FP16 | `(8, 512, 3, 3)` | 1 | 36.9K |
| [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) | `sd_xl_turbo_1.0_fp16.safetensors` | FP16 | `(128, 256, 1, 1)` | 1 | 32.8K |
| [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) | `sd_xl_turbo_1.0_fp16.safetensors` | FP16 | `(256, 128, 1, 1)` | 1 | 32.8K |
| [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) | `sd_xl_turbo_1.0_fp16.safetensors` | FP16 | `(512, 4, 3, 3)` | 1 | 18.4K |
| [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) | `sd_xl_turbo_1.0_fp16.safetensors` | FP16 | `(320)` | 38 | 12.2K |
| [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) | `sd_xl_turbo_1.0_fp16.safetensors` | FP16 | `(320, 4, 3, 3)` | 1 | 11.5K |
| [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) | `sd_xl_turbo_1.0_fp16.safetensors` | FP16 | `(4, 320, 3, 3)` | 1 | 11.5K |
| [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) | `sd_xl_turbo_1.0_fp16.safetensors` | FP16 | `(2560)` | 4 | 10.2K |
| [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) | `sd_xl_turbo_1.0_fp16.safetensors` | FP16 | `(256)` | 34 | 8.7K |
| [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) | `sd_xl_turbo_1.0_fp16.safetensors` | FP16 | `(1920)` | 4 | 7.7K |
| [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) | `sd_xl_turbo_1.0_fp16.safetensors` | FP16 | `(128)` | 35 | 4.5K |
| [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) | `sd_xl_turbo_1.0_fp16.safetensors` | FP16 | `(960)` | 4 | 3.8K |
| [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) | `sd_xl_turbo_1.0_fp16.safetensors` | FP16 | `(128, 3, 3, 3)` | 1 | 3.5K |
| [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) | `sd_xl_turbo_1.0_fp16.safetensors` | FP16 | `(3, 128, 3, 3)` | 1 | 3.5K |
| [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) | `sd_xl_turbo_1.0_fp16.safetensors` | FP16 | `(1000)` | 1 | 1.0K |
| [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) | `sd_xl_turbo_1.0_fp16.safetensors` | FP16 | `(8, 8, 1, 1)` | 1 | 64 |
| [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) | `sd_xl_turbo_1.0_fp16.safetensors` | FP16 | `(4, 4, 1, 1)` | 1 | 16 |
| [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) | `sd_xl_turbo_1.0_fp16.safetensors` | FP16 | `(8)` | 2 | 16 |
| [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) | `sd_xl_turbo_1.0_fp16.safetensors` | FP16 | `(4)` | 2 | 8 |
| [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) | `sd_xl_turbo_1.0_fp16.safetensors` | FP16 | `(3)` | 1 | 3 |
| [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) | `sd_xl_turbo_1.0_fp16.safetensors` | FP16 | `()` | 1 | 1 |
| [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | `sd_xl_base_1.0.safetensors` | FP16 | `(10240, 1280)` | 60 | 786.4M |
| [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | `sd_xl_base_1.0.safetensors` | FP16 | `(1280, 1280)` | 414 | 678.3M |
| [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | `sd_xl_base_1.0.safetensors` | FP16 | `(1280, 5120)` | 92 | 602.9M |
| [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | `sd_xl_base_1.0.safetensors` | FP16 | `(1280, 2048)` | 120 | 314.6M |
| [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | `sd_xl_base_1.0.safetensors` | FP16 | `(5120, 1280)` | 32 | 209.7M |
| [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | `sd_xl_base_1.0.safetensors` | FP16 | `(1280, 1280, 3, 3)` | 11 | 162.2M |
| [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | `sd_xl_base_1.0.safetensors` | FP16 | `(3840, 1280)` | 32 | 157.3M |
| [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | `sd_xl_base_1.0.safetensors` | FP16 | `(512, 512, 3, 3)` | 30 | 70.8M |
| [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | `sd_xl_base_1.0.safetensors` | FP16 | `(49408, 1280)` | 1 | 63.2M |
| [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | `sd_xl_base_1.0.safetensors` | FP16 | `(1280, 2560, 3, 3)` | 2 | 59.0M |
| [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | `sd_xl_base_1.0.safetensors` | FP16 | `(49408, 768)` | 1 | 37.9M |
| [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | `sd_xl_base_1.0.safetensors` | FP16 | `(5120, 640)` | 10 | 32.8M |
| [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | `sd_xl_base_1.0.safetensors` | FP16 | `(640, 640, 3, 3)` | 8 | 29.5M |
| [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | `sd_xl_base_1.0.safetensors` | FP16 | `(640, 640)` | 70 | 28.7M |
| [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | `sd_xl_base_1.0.safetensors` | FP16 | `(3072, 768)` | 12 | 28.3M |
| [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | `sd_xl_base_1.0.safetensors` | FP16 | `(768, 3072)` | 12 | 28.3M |
| [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | `sd_xl_base_1.0.safetensors` | FP16 | `(768, 768)` | 48 | 28.3M |
| [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | `sd_xl_base_1.0.safetensors` | FP16 | `(640, 2048)` | 20 | 26.2M |
| [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | `sd_xl_base_1.0.safetensors` | FP16 | `(1280, 1920, 3, 3)` | 1 | 22.1M |
| [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | `sd_xl_base_1.0.safetensors` | FP16 | `(640, 2560)` | 10 | 16.4M |
| [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | `sd_xl_base_1.0.safetensors` | FP16 | `(640, 1920, 3, 3)` | 1 | 11.1M |
| [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | `sd_xl_base_1.0.safetensors` | FP16 | `(1280, 640, 3, 3)` | 1 | 7.4M |
| [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | `sd_xl_base_1.0.safetensors` | FP16 | `(320, 320, 3, 3)` | 8 | 7.4M |
| [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | `sd_xl_base_1.0.safetensors` | FP16 | `(640, 1280, 3, 3)` | 1 | 7.4M |
| [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | `sd_xl_base_1.0.safetensors` | FP16 | `(1280, 2560, 1, 1)` | 2 | 6.6M |
| [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | `sd_xl_base_1.0.safetensors` | FP16 | `(256, 256, 3, 3)` | 10 | 5.9M |
| [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | `sd_xl_base_1.0.safetensors` | FP16 | `(640, 960, 3, 3)` | 1 | 5.5M |
| [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | `sd_xl_base_1.0.safetensors` | FP16 | `(640, 1280)` | 5 | 4.1M |
| [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | `sd_xl_base_1.0.safetensors` | FP16 | `(320, 640, 3, 3)` | 2 | 3.7M |
| [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | `sd_xl_base_1.0.safetensors` | FP16 | `(1280, 2816)` | 1 | 3.6M |
| [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | `sd_xl_base_1.0.safetensors` | FP16 | `(320, 960, 3, 3)` | 1 | 2.8M |
| [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | `sd_xl_base_1.0.safetensors` | FP16 | `(1280, 1920, 1, 1)` | 1 | 2.5M |
| [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | `sd_xl_base_1.0.safetensors` | FP16 | `(512, 512, 1, 1)` | 8 | 2.1M |
| [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | `sd_xl_base_1.0.safetensors` | FP16 | `(320, 1280)` | 5 | 2.0M |
| [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | `sd_xl_base_1.0.safetensors` | FP16 | `(640, 320, 3, 3)` | 1 | 1.8M |
| [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | `sd_xl_base_1.0.safetensors` | FP16 | `(128, 128, 3, 3)` | 10 | 1.5M |
| [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | `sd_xl_base_1.0.safetensors` | FP16 | `(640, 1920, 1, 1)` | 1 | 1.2M |
| [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | `sd_xl_base_1.0.safetensors` | FP16 | `(256, 512, 3, 3)` | 1 | 1.2M |
| [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | `sd_xl_base_1.0.safetensors` | FP16 | `(512, 256, 3, 3)` | 1 | 1.2M |
| [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | `sd_xl_base_1.0.safetensors` | FP16 | `(1280)` | 810 | 1.0M |
| [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | `sd_xl_base_1.0.safetensors` | FP16 | `(1280, 640, 1, 1)` | 1 | 819.2K |
| [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | `sd_xl_base_1.0.safetensors` | FP16 | `(640, 1280, 1, 1)` | 1 | 819.2K |
| [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | `sd_xl_base_1.0.safetensors` | FP16 | `(10240)` | 60 | 614.4K |
| [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | `sd_xl_base_1.0.safetensors` | FP16 | `(640, 960, 1, 1)` | 1 | 614.4K |
| [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | `sd_xl_base_1.0.safetensors` | FP16 | `(1280, 320)` | 1 | 409.6K |
| [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | `sd_xl_base_1.0.safetensors` | FP16 | `(320, 640, 1, 1)` | 2 | 409.6K |
| [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | `sd_xl_base_1.0.safetensors` | FP16 | `(320, 960, 1, 1)` | 1 | 307.2K |
| [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | `sd_xl_base_1.0.safetensors` | FP16 | `(128, 256, 3, 3)` | 1 | 294.9K |
| [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | `sd_xl_base_1.0.safetensors` | FP16 | `(256, 128, 3, 3)` | 1 | 294.9K |
| [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | `sd_xl_base_1.0.safetensors` | FP16 | `(5120)` | 42 | 215.0K |
| [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | `sd_xl_base_1.0.safetensors` | FP16 | `(640, 320, 1, 1)` | 1 | 204.8K |
| [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | `sd_xl_base_1.0.safetensors` | FP16 | `(256, 512, 1, 1)` | 1 | 131.1K |
| [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | `sd_xl_base_1.0.safetensors` | FP16 | `(512, 256, 1, 1)` | 1 | 131.1K |
| [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | `sd_xl_base_1.0.safetensors` | FP16 | `(3840)` | 32 | 122.9K |
| [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | `sd_xl_base_1.0.safetensors` | FP16 | `(77, 1280)` | 1 | 98.6K |
| [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | `sd_xl_base_1.0.safetensors` | FP16 | `(640)` | 149 | 95.4K |
| [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | `sd_xl_base_1.0.safetensors` | FP16 | `(768)` | 110 | 84.5K |
| [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | `sd_xl_base_1.0.safetensors` | FP16 | `(77, 768)` | 1 | 59.1K |
| [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | `sd_xl_base_1.0.safetensors` | FP16 | `(512)` | 103 | 52.7K |
| [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | `sd_xl_base_1.0.safetensors` | FP16 | `(3072)` | 12 | 36.9K |
| [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | `sd_xl_base_1.0.safetensors` | FP16 | `(8, 512, 3, 3)` | 1 | 36.9K |
| [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | `sd_xl_base_1.0.safetensors` | FP16 | `(128, 256, 1, 1)` | 1 | 32.8K |
| [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | `sd_xl_base_1.0.safetensors` | FP16 | `(256, 128, 1, 1)` | 1 | 32.8K |
| [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | `sd_xl_base_1.0.safetensors` | FP16 | `(512, 4, 3, 3)` | 1 | 18.4K |
| [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | `sd_xl_base_1.0.safetensors` | FP16 | `(320)` | 38 | 12.2K |
| [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | `sd_xl_base_1.0.safetensors` | FP16 | `(320, 4, 3, 3)` | 1 | 11.5K |
| [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | `sd_xl_base_1.0.safetensors` | FP16 | `(4, 320, 3, 3)` | 1 | 11.5K |
| [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | `sd_xl_base_1.0.safetensors` | FP16 | `(2560)` | 4 | 10.2K |
| [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | `sd_xl_base_1.0.safetensors` | FP16 | `(256)` | 34 | 8.7K |
| [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | `sd_xl_base_1.0.safetensors` | FP16 | `(1920)` | 4 | 7.7K |
| [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | `sd_xl_base_1.0.safetensors` | FP16 | `(128)` | 35 | 4.5K |
| [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | `sd_xl_base_1.0.safetensors` | FP16 | `(960)` | 4 | 3.8K |
| [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | `sd_xl_base_1.0.safetensors` | FP16 | `(128, 3, 3, 3)` | 1 | 3.5K |
| [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | `sd_xl_base_1.0.safetensors` | FP16 | `(3, 128, 3, 3)` | 1 | 3.5K |
| [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | `sd_xl_base_1.0.safetensors` | FP16 | `(1, 77)` | 1 | 77 |
| [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | `sd_xl_base_1.0.safetensors` | FP16 | `(8, 8, 1, 1)` | 1 | 64 |
| [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | `sd_xl_base_1.0.safetensors` | FP16 | `(4, 4, 1, 1)` | 1 | 16 |
| [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | `sd_xl_base_1.0.safetensors` | FP16 | `(8)` | 2 | 16 |
| [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | `sd_xl_base_1.0.safetensors` | FP16 | `(4)` | 2 | 8 |
| [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | `sd_xl_base_1.0.safetensors` | FP16 | `(3)` | 1 | 3 |
| [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | `sd_xl_base_1.0.safetensors` | FP16 | `()` | 1 | 1 |
| [stabilityai/stable-diffusion-xl-refiner-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0) | `sd_xl_refiner_1.0.safetensors` | FP16 | `(12288, 1536)` | 24 | 453.0M |
| [stabilityai/stable-diffusion-xl-refiner-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0) | `sd_xl_refiner_1.0.safetensors` | FP16 | `(1536, 1536, 3, 3)` | 20 | 424.7M |
| [stabilityai/stable-diffusion-xl-refiner-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0) | `sd_xl_refiner_1.0.safetensors` | FP16 | `(1536, 1536)` | 170 | 401.1M |
| [stabilityai/stable-diffusion-xl-refiner-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0) | `sd_xl_refiner_1.0.safetensors` | FP16 | `(1536, 6144)` | 24 | 226.5M |
| [stabilityai/stable-diffusion-xl-refiner-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0) | `sd_xl_refiner_1.0.safetensors` | FP16 | `(1536, 3072, 3, 3)` | 5 | 212.3M |
| [stabilityai/stable-diffusion-xl-refiner-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0) | `sd_xl_refiner_1.0.safetensors` | FP16 | `(1280, 5120)` | 32 | 209.7M |
| [stabilityai/stable-diffusion-xl-refiner-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0) | `sd_xl_refiner_1.0.safetensors` | FP16 | `(5120, 1280)` | 32 | 209.7M |
| [stabilityai/stable-diffusion-xl-refiner-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0) | `sd_xl_refiner_1.0.safetensors` | FP16 | `(3840, 1280)` | 32 | 157.3M |
| [stabilityai/stable-diffusion-xl-refiner-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0) | `sd_xl_refiner_1.0.safetensors` | FP16 | `(1536, 1280)` | 48 | 94.4M |
| [stabilityai/stable-diffusion-xl-refiner-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0) | `sd_xl_refiner_1.0.safetensors` | FP16 | `(6144, 768)` | 20 | 94.4M |
| [stabilityai/stable-diffusion-xl-refiner-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0) | `sd_xl_refiner_1.0.safetensors` | FP16 | `(768, 768)` | 130 | 76.7M |
| [stabilityai/stable-diffusion-xl-refiner-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0) | `sd_xl_refiner_1.0.safetensors` | FP16 | `(512, 512, 3, 3)` | 30 | 70.8M |
| [stabilityai/stable-diffusion-xl-refiner-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0) | `sd_xl_refiner_1.0.safetensors` | FP16 | `(49408, 1280)` | 1 | 63.2M |
| [stabilityai/stable-diffusion-xl-refiner-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0) | `sd_xl_refiner_1.0.safetensors` | FP16 | `(1280, 1280)` | 33 | 54.1M |
| [stabilityai/stable-diffusion-xl-refiner-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0) | `sd_xl_refiner_1.0.safetensors` | FP16 | `(768, 3072)` | 20 | 47.2M |
| [stabilityai/stable-diffusion-xl-refiner-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0) | `sd_xl_refiner_1.0.safetensors` | FP16 | `(768, 768, 3, 3)` | 8 | 42.5M |
| [stabilityai/stable-diffusion-xl-refiner-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0) | `sd_xl_refiner_1.0.safetensors` | FP16 | `(768, 1280)` | 40 | 39.3M |
| [stabilityai/stable-diffusion-xl-refiner-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0) | `sd_xl_refiner_1.0.safetensors` | FP16 | `(1536, 2304, 3, 3)` | 1 | 31.9M |
| [stabilityai/stable-diffusion-xl-refiner-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0) | `sd_xl_refiner_1.0.safetensors` | FP16 | `(1536, 3072, 1, 1)` | 5 | 23.6M |
| [stabilityai/stable-diffusion-xl-refiner-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0) | `sd_xl_refiner_1.0.safetensors` | FP16 | `(768, 2304, 3, 3)` | 1 | 15.9M |
| [stabilityai/stable-diffusion-xl-refiner-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0) | `sd_xl_refiner_1.0.safetensors` | FP16 | `(1536, 768, 3, 3)` | 1 | 10.6M |
| [stabilityai/stable-diffusion-xl-refiner-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0) | `sd_xl_refiner_1.0.safetensors` | FP16 | `(384, 384, 3, 3)` | 8 | 10.6M |
| [stabilityai/stable-diffusion-xl-refiner-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0) | `sd_xl_refiner_1.0.safetensors` | FP16 | `(768, 1536, 3, 3)` | 1 | 10.6M |
| [stabilityai/stable-diffusion-xl-refiner-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0) | `sd_xl_refiner_1.0.safetensors` | FP16 | `(768, 1152, 3, 3)` | 1 | 8.0M |
| [stabilityai/stable-diffusion-xl-refiner-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0) | `sd_xl_refiner_1.0.safetensors` | FP16 | `(256, 256, 3, 3)` | 10 | 5.9M |
| [stabilityai/stable-diffusion-xl-refiner-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0) | `sd_xl_refiner_1.0.safetensors` | FP16 | `(768, 1536)` | 5 | 5.9M |
| [stabilityai/stable-diffusion-xl-refiner-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0) | `sd_xl_refiner_1.0.safetensors` | FP16 | `(384, 768, 3, 3)` | 2 | 5.3M |
| [stabilityai/stable-diffusion-xl-refiner-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0) | `sd_xl_refiner_1.0.safetensors` | FP16 | `(384, 1152, 3, 3)` | 1 | 4.0M |
| [stabilityai/stable-diffusion-xl-refiner-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0) | `sd_xl_refiner_1.0.safetensors` | FP16 | `(1536, 2560)` | 1 | 3.9M |
| [stabilityai/stable-diffusion-xl-refiner-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0) | `sd_xl_refiner_1.0.safetensors` | FP16 | `(1536, 2304, 1, 1)` | 1 | 3.5M |
| [stabilityai/stable-diffusion-xl-refiner-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0) | `sd_xl_refiner_1.0.safetensors` | FP16 | `(384, 1536)` | 5 | 2.9M |
| [stabilityai/stable-diffusion-xl-refiner-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0) | `sd_xl_refiner_1.0.safetensors` | FP16 | `(768, 384, 3, 3)` | 1 | 2.7M |
| [stabilityai/stable-diffusion-xl-refiner-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0) | `sd_xl_refiner_1.0.safetensors` | FP16 | `(512, 512, 1, 1)` | 8 | 2.1M |
| [stabilityai/stable-diffusion-xl-refiner-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0) | `sd_xl_refiner_1.0.safetensors` | FP16 | `(768, 2304, 1, 1)` | 1 | 1.8M |
| [stabilityai/stable-diffusion-xl-refiner-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0) | `sd_xl_refiner_1.0.safetensors` | FP16 | `(128, 128, 3, 3)` | 10 | 1.5M |
| [stabilityai/stable-diffusion-xl-refiner-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0) | `sd_xl_refiner_1.0.safetensors` | FP16 | `(1536, 768, 1, 1)` | 1 | 1.2M |
| [stabilityai/stable-diffusion-xl-refiner-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0) | `sd_xl_refiner_1.0.safetensors` | FP16 | `(256, 512, 3, 3)` | 1 | 1.2M |
| [stabilityai/stable-diffusion-xl-refiner-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0) | `sd_xl_refiner_1.0.safetensors` | FP16 | `(512, 256, 3, 3)` | 1 | 1.2M |
| [stabilityai/stable-diffusion-xl-refiner-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0) | `sd_xl_refiner_1.0.safetensors` | FP16 | `(768, 1536, 1, 1)` | 1 | 1.2M |
| [stabilityai/stable-diffusion-xl-refiner-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0) | `sd_xl_refiner_1.0.safetensors` | FP16 | `(768, 1152, 1, 1)` | 1 | 884.7K |
| [stabilityai/stable-diffusion-xl-refiner-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0) | `sd_xl_refiner_1.0.safetensors` | FP16 | `(1536, 384)` | 1 | 589.8K |
| [stabilityai/stable-diffusion-xl-refiner-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0) | `sd_xl_refiner_1.0.safetensors` | FP16 | `(384, 768, 1, 1)` | 2 | 589.8K |
| [stabilityai/stable-diffusion-xl-refiner-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0) | `sd_xl_refiner_1.0.safetensors` | FP16 | `(1536)` | 326 | 500.7K |
| [stabilityai/stable-diffusion-xl-refiner-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0) | `sd_xl_refiner_1.0.safetensors` | FP16 | `(384, 1152, 1, 1)` | 1 | 442.4K |
| [stabilityai/stable-diffusion-xl-refiner-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0) | `sd_xl_refiner_1.0.safetensors` | FP16 | `(12288)` | 24 | 294.9K |
| [stabilityai/stable-diffusion-xl-refiner-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0) | `sd_xl_refiner_1.0.safetensors` | FP16 | `(128, 256, 3, 3)` | 1 | 294.9K |
| [stabilityai/stable-diffusion-xl-refiner-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0) | `sd_xl_refiner_1.0.safetensors` | FP16 | `(256, 128, 3, 3)` | 1 | 294.9K |
| [stabilityai/stable-diffusion-xl-refiner-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0) | `sd_xl_refiner_1.0.safetensors` | FP16 | `(768, 384, 1, 1)` | 1 | 294.9K |
| [stabilityai/stable-diffusion-xl-refiner-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0) | `sd_xl_refiner_1.0.safetensors` | FP16 | `(1280)` | 194 | 248.3K |
| [stabilityai/stable-diffusion-xl-refiner-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0) | `sd_xl_refiner_1.0.safetensors` | FP16 | `(768)` | 239 | 183.6K |
| [stabilityai/stable-diffusion-xl-refiner-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0) | `sd_xl_refiner_1.0.safetensors` | FP16 | `(5120)` | 32 | 163.8K |
| [stabilityai/stable-diffusion-xl-refiner-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0) | `sd_xl_refiner_1.0.safetensors` | FP16 | `(256, 512, 1, 1)` | 1 | 131.1K |
| [stabilityai/stable-diffusion-xl-refiner-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0) | `sd_xl_refiner_1.0.safetensors` | FP16 | `(512, 256, 1, 1)` | 1 | 131.1K |
| [stabilityai/stable-diffusion-xl-refiner-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0) | `sd_xl_refiner_1.0.safetensors` | FP16 | `(3840)` | 32 | 122.9K |
| [stabilityai/stable-diffusion-xl-refiner-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0) | `sd_xl_refiner_1.0.safetensors` | FP16 | `(6144)` | 20 | 122.9K |
| [stabilityai/stable-diffusion-xl-refiner-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0) | `sd_xl_refiner_1.0.safetensors` | FP16 | `(77, 1280)` | 1 | 98.6K |
| [stabilityai/stable-diffusion-xl-refiner-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0) | `sd_xl_refiner_1.0.safetensors` | FP16 | `(512)` | 103 | 52.7K |
| [stabilityai/stable-diffusion-xl-refiner-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0) | `sd_xl_refiner_1.0.safetensors` | FP16 | `(8, 512, 3, 3)` | 1 | 36.9K |
| [stabilityai/stable-diffusion-xl-refiner-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0) | `sd_xl_refiner_1.0.safetensors` | FP16 | `(128, 256, 1, 1)` | 1 | 32.8K |
| [stabilityai/stable-diffusion-xl-refiner-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0) | `sd_xl_refiner_1.0.safetensors` | FP16 | `(256, 128, 1, 1)` | 1 | 32.8K |
| [stabilityai/stable-diffusion-xl-refiner-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0) | `sd_xl_refiner_1.0.safetensors` | FP16 | `(3072)` | 10 | 30.7K |
| [stabilityai/stable-diffusion-xl-refiner-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0) | `sd_xl_refiner_1.0.safetensors` | FP16 | `(512, 4, 3, 3)` | 1 | 18.4K |
| [stabilityai/stable-diffusion-xl-refiner-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0) | `sd_xl_refiner_1.0.safetensors` | FP16 | `(384)` | 38 | 14.6K |
| [stabilityai/stable-diffusion-xl-refiner-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0) | `sd_xl_refiner_1.0.safetensors` | FP16 | `(384, 4, 3, 3)` | 1 | 13.8K |
| [stabilityai/stable-diffusion-xl-refiner-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0) | `sd_xl_refiner_1.0.safetensors` | FP16 | `(4, 384, 3, 3)` | 1 | 13.8K |
| [stabilityai/stable-diffusion-xl-refiner-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0) | `sd_xl_refiner_1.0.safetensors` | FP16 | `(2304)` | 4 | 9.2K |
| [stabilityai/stable-diffusion-xl-refiner-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0) | `sd_xl_refiner_1.0.safetensors` | FP16 | `(256)` | 34 | 8.7K |
| [stabilityai/stable-diffusion-xl-refiner-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0) | `sd_xl_refiner_1.0.safetensors` | FP16 | `(1152)` | 4 | 4.6K |
| [stabilityai/stable-diffusion-xl-refiner-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0) | `sd_xl_refiner_1.0.safetensors` | FP16 | `(128)` | 35 | 4.5K |
| [stabilityai/stable-diffusion-xl-refiner-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0) | `sd_xl_refiner_1.0.safetensors` | FP16 | `(128, 3, 3, 3)` | 1 | 3.5K |
| [stabilityai/stable-diffusion-xl-refiner-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0) | `sd_xl_refiner_1.0.safetensors` | FP16 | `(3, 128, 3, 3)` | 1 | 3.5K |
| [stabilityai/stable-diffusion-xl-refiner-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0) | `sd_xl_refiner_1.0.safetensors` | FP16 | `(8, 8, 1, 1)` | 1 | 64 |
| [stabilityai/stable-diffusion-xl-refiner-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0) | `sd_xl_refiner_1.0.safetensors` | FP16 | `(4, 4, 1, 1)` | 1 | 16 |
| [stabilityai/stable-diffusion-xl-refiner-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0) | `sd_xl_refiner_1.0.safetensors` | FP16 | `(8)` | 2 | 16 |
| [stabilityai/stable-diffusion-xl-refiner-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0) | `sd_xl_refiner_1.0.safetensors` | FP16 | `(4)` | 2 | 8 |
| [stabilityai/stable-diffusion-xl-refiner-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0) | `sd_xl_refiner_1.0.safetensors` | FP16 | `(3)` | 1 | 3 |
| [stabilityai/stable-diffusion-xl-refiner-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0) | `sd_xl_refiner_1.0.safetensors` | FP16 | `()` | 1 | 1 |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | `svd.safetensors` | FP32 | `(1280, 5120)` | 56 | 367.0M |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | `svd.safetensors` | FP32 | `(1280, 1280, 3, 3)` | 20 | 294.9M |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | `svd.safetensors` | FP32 | `(5120, 1280)` | 38 | 249.0M |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | `svd.safetensors` | FP32 | `(10240, 1280)` | 18 | 235.9M |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | `svd.safetensors` | FP32 | `(1280, 1280)` | 142 | 232.7M |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | `svd.safetensors` | FP32 | `(3840, 1280)` | 32 | 157.3M |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | `svd.safetensors` | FP32 | `(1280, 2560, 3, 3)` | 5 | 147.5M |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | `svd.safetensors` | FP32 | `(512, 512, 3, 3)` | 60 | 141.6M |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | `svd.safetensors` | FP32 | `(1280, 1280, 3, 1, 1)` | 24 | 118.0M |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | `svd.safetensors` | FP32 | `(49408, 1024)` | 1 | 50.6M |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | `svd.safetensors` | FP32 | `(5120, 640)` | 15 | 49.2M |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | `svd.safetensors` | FP32 | `(1280, 1024)` | 25 | 32.8M |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | `svd.safetensors` | FP32 | `(640, 2560)` | 20 | 32.8M |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | `svd.safetensors` | FP32 | `(640, 640, 3, 3)` | 8 | 29.5M |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | `svd.safetensors` | FP32 | `(640, 640)` | 70 | 28.7M |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | `svd.safetensors` | FP32 | `(1280, 1920, 3, 3)` | 1 | 22.1M |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | `svd.safetensors` | FP32 | `(1280, 2560, 1, 1)` | 5 | 16.4M |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | `svd.safetensors` | FP32 | `(640, 1024)` | 20 | 13.1M |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | `svd.safetensors` | FP32 | `(512, 512, 3, 1, 1)` | 16 | 12.6M |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | `svd.safetensors` | FP32 | `(2560, 320)` | 15 | 12.3M |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | `svd.safetensors` | FP32 | `(320, 1280)` | 30 | 12.3M |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | `svd.safetensors` | FP32 | `(640, 640, 3, 1, 1)` | 10 | 12.3M |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | `svd.safetensors` | FP32 | `(256, 256, 3, 3)` | 20 | 11.8M |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | `svd.safetensors` | FP32 | `(640, 1920, 3, 3)` | 1 | 11.1M |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | `svd.safetensors` | FP32 | `(2560, 640)` | 5 | 8.2M |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | `svd.safetensors` | FP32 | `(640, 1280)` | 10 | 8.2M |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | `svd.safetensors` | FP32 | `(1280, 640, 3, 3)` | 1 | 7.4M |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | `svd.safetensors` | FP32 | `(320, 320, 3, 3)` | 8 | 7.4M |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | `svd.safetensors` | FP32 | `(640, 1280, 3, 3)` | 1 | 7.4M |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | `svd.safetensors` | FP32 | `(320, 320)` | 70 | 7.2M |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | `svd.safetensors` | FP32 | `(320, 1024)` | 20 | 6.6M |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | `svd.safetensors` | FP32 | `(640, 960, 3, 3)` | 1 | 5.5M |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | `svd.safetensors` | FP32 | `(512, 512, 1, 1)` | 16 | 4.2M |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | `svd.safetensors` | FP32 | `(320, 640, 3, 3)` | 2 | 3.7M |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | `svd.safetensors` | FP32 | `(320, 320, 3, 1, 1)` | 10 | 3.1M |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | `svd.safetensors` | FP32 | `(128, 128, 3, 3)` | 20 | 2.9M |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | `svd.safetensors` | FP32 | `(320, 960, 3, 3)` | 1 | 2.8M |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | `svd.safetensors` | FP32 | `(1280, 1920, 1, 1)` | 1 | 2.5M |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | `svd.safetensors` | FP32 | `(1280, 320)` | 6 | 2.5M |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | `svd.safetensors` | FP32 | `(256, 512, 3, 3)` | 2 | 2.4M |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | `svd.safetensors` | FP32 | `(512, 256, 3, 3)` | 2 | 2.4M |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | `svd.safetensors` | FP32 | `(640, 320, 3, 3)` | 1 | 1.8M |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | `svd.safetensors` | FP32 | `(640, 1920, 1, 1)` | 1 | 1.2M |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | `svd.safetensors` | FP32 | `(256, 256, 3, 1, 1)` | 6 | 1.2M |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | `svd.safetensors` | FP32 | `(1024, 1024)` | 1 | 1.0M |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | `svd.safetensors` | FP32 | `(1280, 768)` | 1 | 983.0K |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | `svd.safetensors` | FP32 | `(1280, 640, 1, 1)` | 1 | 819.2K |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | `svd.safetensors` | FP32 | `(640, 1280, 1, 1)` | 1 | 819.2K |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | `svd.safetensors` | FP32 | `(1280, 3, 14, 14)` | 1 | 752.6K |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | `svd.safetensors` | FP32 | `(1280)` | 528 | 675.8K |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | `svd.safetensors` | FP32 | `(640, 960, 1, 1)` | 1 | 614.4K |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | `svd.safetensors` | FP32 | `(128, 256, 3, 3)` | 2 | 589.8K |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | `svd.safetensors` | FP32 | `(256, 128, 3, 3)` | 2 | 589.8K |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | `svd.safetensors` | FP32 | `(320, 640, 1, 1)` | 2 | 409.6K |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | `svd.safetensors` | FP32 | `(257, 1280)` | 1 | 329.0K |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | `svd.safetensors` | FP32 | `(320, 960, 1, 1)` | 1 | 307.2K |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | `svd.safetensors` | FP32 | `(128, 128, 3, 1, 1)` | 6 | 294.9K |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | `svd.safetensors` | FP32 | `(5120)` | 53 | 271.4K |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | `svd.safetensors` | FP32 | `(256, 512, 1, 1)` | 2 | 262.1K |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | `svd.safetensors` | FP32 | `(512, 256, 1, 1)` | 2 | 262.1K |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | `svd.safetensors` | FP32 | `(640, 320, 1, 1)` | 1 | 204.8K |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | `svd.safetensors` | FP32 | `(10240)` | 18 | 184.3K |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | `svd.safetensors` | FP32 | `(640)` | 204 | 130.6K |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | `svd.safetensors` | FP32 | `(512)` | 254 | 130.0K |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | `svd.safetensors` | FP32 | `(3840)` | 32 | 122.9K |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | `svd.safetensors` | FP32 | `(77, 1024)` | 1 | 78.8K |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | `svd.safetensors` | FP32 | `(2560)` | 30 | 76.8K |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | `svd.safetensors` | FP32 | `(8, 512, 3, 3)` | 2 | 73.7K |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | `svd.safetensors` | FP32 | `(128, 256, 1, 1)` | 2 | 65.5K |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | `svd.safetensors` | FP32 | `(256, 128, 1, 1)` | 2 | 65.5K |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | `svd.safetensors` | FP32 | `(320)` | 203 | 65.0K |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | `svd.safetensors` | FP32 | `(512, 4, 3, 3)` | 2 | 36.9K |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | `svd.safetensors` | FP32 | `(320, 8, 3, 3)` | 1 | 23.0K |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | `svd.safetensors` | FP32 | `(256)` | 86 | 22.0K |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | `svd.safetensors` | FP32 | `(4, 320, 3, 3)` | 1 | 11.5K |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | `svd.safetensors` | FP32 | `(128)` | 88 | 11.3K |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | `svd.safetensors` | FP32 | `(1920)` | 4 | 7.7K |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | `svd.safetensors` | FP32 | `(128, 3, 3, 3)` | 2 | 6.9K |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | `svd.safetensors` | FP32 | `(3, 128, 3, 3)` | 2 | 6.9K |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | `svd.safetensors` | FP32 | `(960)` | 4 | 3.8K |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | `svd.safetensors` | FP32 | `(1024)` | 2 | 2.0K |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | `svd.safetensors` | FP32 | `(8, 8, 1, 1)` | 1 | 64 |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | `svd.safetensors` | FP32 | `(1)` | 52 | 52 |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | `svd.safetensors` | FP32 | `(3, 3, 3, 1, 1)` | 1 | 27 |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | `svd.safetensors` | FP32 | `(8)` | 3 | 24 |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | `svd.safetensors` | FP32 | `(4, 4, 1, 1)` | 1 | 16 |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | `svd.safetensors` | FP32 | `(3)` | 3 | 9 |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | `svd.safetensors` | FP32 | `(4)` | 2 | 8 |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | `svd.safetensors` | FP32 | `()` | 1 | 1 |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | `svd_xt.safetensors` | FP32 | `(1280, 5120)` | 56 | 367.0M |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | `svd_xt.safetensors` | FP32 | `(1280, 1280, 3, 3)` | 20 | 294.9M |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | `svd_xt.safetensors` | FP32 | `(5120, 1280)` | 38 | 249.0M |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | `svd_xt.safetensors` | FP32 | `(10240, 1280)` | 18 | 235.9M |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | `svd_xt.safetensors` | FP32 | `(1280, 1280)` | 142 | 232.7M |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | `svd_xt.safetensors` | FP32 | `(3840, 1280)` | 32 | 157.3M |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | `svd_xt.safetensors` | FP32 | `(1280, 2560, 3, 3)` | 5 | 147.5M |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | `svd_xt.safetensors` | FP32 | `(512, 512, 3, 3)` | 60 | 141.6M |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | `svd_xt.safetensors` | FP32 | `(1280, 1280, 3, 1, 1)` | 24 | 118.0M |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | `svd_xt.safetensors` | FP32 | `(49408, 1024)` | 1 | 50.6M |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | `svd_xt.safetensors` | FP32 | `(5120, 640)` | 15 | 49.2M |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | `svd_xt.safetensors` | FP32 | `(1280, 1024)` | 25 | 32.8M |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | `svd_xt.safetensors` | FP32 | `(640, 2560)` | 20 | 32.8M |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | `svd_xt.safetensors` | FP32 | `(640, 640, 3, 3)` | 8 | 29.5M |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | `svd_xt.safetensors` | FP32 | `(640, 640)` | 70 | 28.7M |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | `svd_xt.safetensors` | FP32 | `(1280, 1920, 3, 3)` | 1 | 22.1M |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | `svd_xt.safetensors` | FP32 | `(1280, 2560, 1, 1)` | 5 | 16.4M |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | `svd_xt.safetensors` | FP32 | `(640, 1024)` | 20 | 13.1M |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | `svd_xt.safetensors` | FP32 | `(512, 512, 3, 1, 1)` | 16 | 12.6M |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | `svd_xt.safetensors` | FP32 | `(2560, 320)` | 15 | 12.3M |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | `svd_xt.safetensors` | FP32 | `(320, 1280)` | 30 | 12.3M |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | `svd_xt.safetensors` | FP32 | `(640, 640, 3, 1, 1)` | 10 | 12.3M |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | `svd_xt.safetensors` | FP32 | `(256, 256, 3, 3)` | 20 | 11.8M |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | `svd_xt.safetensors` | FP32 | `(640, 1920, 3, 3)` | 1 | 11.1M |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | `svd_xt.safetensors` | FP32 | `(2560, 640)` | 5 | 8.2M |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | `svd_xt.safetensors` | FP32 | `(640, 1280)` | 10 | 8.2M |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | `svd_xt.safetensors` | FP32 | `(1280, 640, 3, 3)` | 1 | 7.4M |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | `svd_xt.safetensors` | FP32 | `(320, 320, 3, 3)` | 8 | 7.4M |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | `svd_xt.safetensors` | FP32 | `(640, 1280, 3, 3)` | 1 | 7.4M |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | `svd_xt.safetensors` | FP32 | `(320, 320)` | 70 | 7.2M |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | `svd_xt.safetensors` | FP32 | `(320, 1024)` | 20 | 6.6M |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | `svd_xt.safetensors` | FP32 | `(640, 960, 3, 3)` | 1 | 5.5M |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | `svd_xt.safetensors` | FP32 | `(512, 512, 1, 1)` | 16 | 4.2M |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | `svd_xt.safetensors` | FP32 | `(320, 640, 3, 3)` | 2 | 3.7M |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | `svd_xt.safetensors` | FP32 | `(320, 320, 3, 1, 1)` | 10 | 3.1M |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | `svd_xt.safetensors` | FP32 | `(128, 128, 3, 3)` | 20 | 2.9M |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | `svd_xt.safetensors` | FP32 | `(320, 960, 3, 3)` | 1 | 2.8M |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | `svd_xt.safetensors` | FP32 | `(1280, 1920, 1, 1)` | 1 | 2.5M |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | `svd_xt.safetensors` | FP32 | `(1280, 320)` | 6 | 2.5M |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | `svd_xt.safetensors` | FP32 | `(256, 512, 3, 3)` | 2 | 2.4M |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | `svd_xt.safetensors` | FP32 | `(512, 256, 3, 3)` | 2 | 2.4M |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | `svd_xt.safetensors` | FP32 | `(640, 320, 3, 3)` | 1 | 1.8M |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | `svd_xt.safetensors` | FP32 | `(640, 1920, 1, 1)` | 1 | 1.2M |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | `svd_xt.safetensors` | FP32 | `(256, 256, 3, 1, 1)` | 6 | 1.2M |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | `svd_xt.safetensors` | FP32 | `(1024, 1024)` | 1 | 1.0M |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | `svd_xt.safetensors` | FP32 | `(1280, 768)` | 1 | 983.0K |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | `svd_xt.safetensors` | FP32 | `(1280, 640, 1, 1)` | 1 | 819.2K |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | `svd_xt.safetensors` | FP32 | `(640, 1280, 1, 1)` | 1 | 819.2K |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | `svd_xt.safetensors` | FP32 | `(1280, 3, 14, 14)` | 1 | 752.6K |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | `svd_xt.safetensors` | FP32 | `(1280)` | 528 | 675.8K |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | `svd_xt.safetensors` | FP32 | `(640, 960, 1, 1)` | 1 | 614.4K |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | `svd_xt.safetensors` | FP32 | `(128, 256, 3, 3)` | 2 | 589.8K |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | `svd_xt.safetensors` | FP32 | `(256, 128, 3, 3)` | 2 | 589.8K |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | `svd_xt.safetensors` | FP32 | `(320, 640, 1, 1)` | 2 | 409.6K |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | `svd_xt.safetensors` | FP32 | `(257, 1280)` | 1 | 329.0K |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | `svd_xt.safetensors` | FP32 | `(320, 960, 1, 1)` | 1 | 307.2K |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | `svd_xt.safetensors` | FP32 | `(128, 128, 3, 1, 1)` | 6 | 294.9K |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | `svd_xt.safetensors` | FP32 | `(5120)` | 53 | 271.4K |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | `svd_xt.safetensors` | FP32 | `(256, 512, 1, 1)` | 2 | 262.1K |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | `svd_xt.safetensors` | FP32 | `(512, 256, 1, 1)` | 2 | 262.1K |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | `svd_xt.safetensors` | FP32 | `(640, 320, 1, 1)` | 1 | 204.8K |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | `svd_xt.safetensors` | FP32 | `(10240)` | 18 | 184.3K |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | `svd_xt.safetensors` | FP32 | `(640)` | 204 | 130.6K |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | `svd_xt.safetensors` | FP32 | `(512)` | 254 | 130.0K |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | `svd_xt.safetensors` | FP32 | `(3840)` | 32 | 122.9K |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | `svd_xt.safetensors` | FP32 | `(77, 1024)` | 1 | 78.8K |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | `svd_xt.safetensors` | FP32 | `(2560)` | 30 | 76.8K |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | `svd_xt.safetensors` | FP32 | `(8, 512, 3, 3)` | 2 | 73.7K |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | `svd_xt.safetensors` | FP32 | `(128, 256, 1, 1)` | 2 | 65.5K |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | `svd_xt.safetensors` | FP32 | `(256, 128, 1, 1)` | 2 | 65.5K |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | `svd_xt.safetensors` | FP32 | `(320)` | 203 | 65.0K |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | `svd_xt.safetensors` | FP32 | `(512, 4, 3, 3)` | 2 | 36.9K |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | `svd_xt.safetensors` | FP32 | `(320, 8, 3, 3)` | 1 | 23.0K |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | `svd_xt.safetensors` | FP32 | `(256)` | 86 | 22.0K |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | `svd_xt.safetensors` | FP32 | `(4, 320, 3, 3)` | 1 | 11.5K |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | `svd_xt.safetensors` | FP32 | `(128)` | 88 | 11.3K |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | `svd_xt.safetensors` | FP32 | `(1920)` | 4 | 7.7K |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | `svd_xt.safetensors` | FP32 | `(128, 3, 3, 3)` | 2 | 6.9K |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | `svd_xt.safetensors` | FP32 | `(3, 128, 3, 3)` | 2 | 6.9K |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | `svd_xt.safetensors` | FP32 | `(960)` | 4 | 3.8K |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | `svd_xt.safetensors` | FP32 | `(1024)` | 2 | 2.0K |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | `svd_xt.safetensors` | FP32 | `(8, 8, 1, 1)` | 1 | 64 |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | `svd_xt.safetensors` | FP32 | `(1)` | 52 | 52 |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | `svd_xt.safetensors` | FP32 | `(3, 3, 3, 1, 1)` | 1 | 27 |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | `svd_xt.safetensors` | FP32 | `(8)` | 3 | 24 |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | `svd_xt.safetensors` | FP32 | `(4, 4, 1, 1)` | 1 | 16 |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | `svd_xt.safetensors` | FP32 | `(3)` | 3 | 9 |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | `svd_xt.safetensors` | FP32 | `(4)` | 2 | 8 |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | `svd_xt.safetensors` | FP32 | `()` | 1 | 1 |
| [THUDM/CogVideoX-2B](https://huggingface.co/THUDM/CogVideoX-2B) | `text_encoder/model-00001-of-00002.safetensors` | FP16 | `(10240, 4096)` | 24 | 1.01B |
| [THUDM/CogVideoX-2B](https://huggingface.co/THUDM/CogVideoX-2B) | `text_encoder/model-00002-of-00002.safetensors` | FP16 | `(10240, 4096)` | 24 | 1.01B |
| [THUDM/CogVideoX-2B](https://huggingface.co/THUDM/CogVideoX-2B) | `text_encoder/model-00001-of-00002.safetensors` | FP16 | `(4096, 4096)` | 51 | 855.6M |
| [THUDM/CogVideoX-2B](https://huggingface.co/THUDM/CogVideoX-2B) | `text_encoder/model-00002-of-00002.safetensors` | FP16 | `(4096, 4096)` | 45 | 755.0M |
| [THUDM/CogVideoX-2B](https://huggingface.co/THUDM/CogVideoX-2B) | `text_encoder/model-00001-of-00002.safetensors` | FP16 | `(4096, 10240)` | 12 | 503.3M |
| [THUDM/CogVideoX-2B](https://huggingface.co/THUDM/CogVideoX-2B) | `text_encoder/model-00002-of-00002.safetensors` | FP16 | `(4096, 10240)` | 12 | 503.3M |
| [THUDM/CogVideoX-2B](https://huggingface.co/THUDM/CogVideoX-2B) | `transformer/diffusion_pytorch_model.safetensors` | FP16 | `(1920, 1920)` | 120 | 442.4M |
| [THUDM/CogVideoX-2B](https://huggingface.co/THUDM/CogVideoX-2B) | `transformer/diffusion_pytorch_model.safetensors` | FP16 | `(1920, 7680)` | 30 | 442.4M |
| [THUDM/CogVideoX-2B](https://huggingface.co/THUDM/CogVideoX-2B) | `transformer/diffusion_pytorch_model.safetensors` | FP16 | `(7680, 1920)` | 30 | 442.4M |
| [THUDM/CogVideoX-2B](https://huggingface.co/THUDM/CogVideoX-2B) | `transformer/diffusion_pytorch_model.safetensors` | FP16 | `(11520, 512)` | 60 | 353.9M |
| [THUDM/CogVideoX-2B](https://huggingface.co/THUDM/CogVideoX-2B) | `text_encoder/model-00001-of-00002.safetensors` | FP16 | `(32128, 4096)` | 1 | 131.6M |
| [THUDM/CogVideoX-2B](https://huggingface.co/THUDM/CogVideoX-2B) | `transformer/diffusion_pytorch_model.safetensors` | FP16 | `(1920, 4096)` | 1 | 7.9M |
| [THUDM/CogVideoX-2B](https://huggingface.co/THUDM/CogVideoX-2B) | `transformer/diffusion_pytorch_model.safetensors` | FP16 | `(3840, 512)` | 1 | 2.0M |
| [THUDM/CogVideoX-2B](https://huggingface.co/THUDM/CogVideoX-2B) | `transformer/diffusion_pytorch_model.safetensors` | FP16 | `(512, 1920)` | 1 | 983.0K |
| [THUDM/CogVideoX-2B](https://huggingface.co/THUDM/CogVideoX-2B) | `transformer/diffusion_pytorch_model.safetensors` | FP16 | `(11520)` | 60 | 691.2K |
| [THUDM/CogVideoX-2B](https://huggingface.co/THUDM/CogVideoX-2B) | `transformer/diffusion_pytorch_model.safetensors` | FP16 | `(1920)` | 276 | 529.9K |
| [THUDM/CogVideoX-2B](https://huggingface.co/THUDM/CogVideoX-2B) | `transformer/diffusion_pytorch_model.safetensors` | FP16 | `(512, 512)` | 1 | 262.1K |
| [THUDM/CogVideoX-2B](https://huggingface.co/THUDM/CogVideoX-2B) | `transformer/diffusion_pytorch_model.safetensors` | FP16 | `(7680)` | 30 | 230.4K |
| [THUDM/CogVideoX-2B](https://huggingface.co/THUDM/CogVideoX-2B) | `transformer/diffusion_pytorch_model.safetensors` | FP16 | `(1920, 16, 2, 2)` | 1 | 122.9K |
| [THUDM/CogVideoX-2B](https://huggingface.co/THUDM/CogVideoX-2B) | `transformer/diffusion_pytorch_model.safetensors` | FP16 | `(64, 1920)` | 1 | 122.9K |
| [THUDM/CogVideoX-2B](https://huggingface.co/THUDM/CogVideoX-2B) | `text_encoder/model-00002-of-00002.safetensors` | FP16 | `(4096)` | 25 | 102.4K |
| [THUDM/CogVideoX-2B](https://huggingface.co/THUDM/CogVideoX-2B) | `text_encoder/model-00001-of-00002.safetensors` | FP16 | `(4096)` | 24 | 98.3K |
| [THUDM/CogVideoX-2B](https://huggingface.co/THUDM/CogVideoX-2B) | `transformer/diffusion_pytorch_model.safetensors` | FP16 | `(64)` | 121 | 7.7K |
| [THUDM/CogVideoX-2B](https://huggingface.co/THUDM/CogVideoX-2B) | `transformer/diffusion_pytorch_model.safetensors` | FP16 | `(3840)` | 1 | 3.8K |
| [THUDM/CogVideoX-2B](https://huggingface.co/THUDM/CogVideoX-2B) | `text_encoder/model-00001-of-00002.safetensors` | FP16 | `(32, 64)` | 1 | 2.0K |
| [THUDM/CogVideoX-2B](https://huggingface.co/THUDM/CogVideoX-2B) | `transformer/diffusion_pytorch_model.safetensors` | FP16 | `(512)` | 2 | 1.0K |
| [THUDM/CogVideoX-5b-I2V](https://huggingface.co/THUDM/CogVideoX-5b-I2V) | `text_encoder/model-00001-of-00002.safetensors` | BF16 | `(10240, 4096)` | 24 | 1.01B |
| [THUDM/CogVideoX-5b-I2V](https://huggingface.co/THUDM/CogVideoX-5b-I2V) | `text_encoder/model-00002-of-00002.safetensors` | BF16 | `(10240, 4096)` | 24 | 1.01B |
| [THUDM/CogVideoX-5b-I2V](https://huggingface.co/THUDM/CogVideoX-5b-I2V) | `text_encoder/model-00001-of-00002.safetensors` | BF16 | `(4096, 4096)` | 51 | 855.6M |
| [THUDM/CogVideoX-5b-I2V](https://huggingface.co/THUDM/CogVideoX-5b-I2V) | `text_encoder/model-00002-of-00002.safetensors` | BF16 | `(4096, 4096)` | 45 | 755.0M |
| [THUDM/CogVideoX-5b-I2V](https://huggingface.co/THUDM/CogVideoX-5b-I2V) | `transformer/diffusion_pytorch_model-00001-of-00003.safetensors` | BF16 | `(3072, 3072)` | 76 | 717.2M |
| [THUDM/CogVideoX-5b-I2V](https://huggingface.co/THUDM/CogVideoX-5b-I2V) | `transformer/diffusion_pytorch_model-00001-of-00003.safetensors` | BF16 | `(12288, 3072)` | 18 | 679.5M |
| [THUDM/CogVideoX-5b-I2V](https://huggingface.co/THUDM/CogVideoX-5b-I2V) | `transformer/diffusion_pytorch_model-00001-of-00003.safetensors` | BF16 | `(3072, 12288)` | 18 | 679.5M |
| [THUDM/CogVideoX-5b-I2V](https://huggingface.co/THUDM/CogVideoX-5b-I2V) | `text_encoder/model-00001-of-00002.safetensors` | BF16 | `(4096, 10240)` | 12 | 503.3M |
| [THUDM/CogVideoX-5b-I2V](https://huggingface.co/THUDM/CogVideoX-5b-I2V) | `text_encoder/model-00002-of-00002.safetensors` | BF16 | `(4096, 10240)` | 12 | 503.3M |
| [THUDM/CogVideoX-5b-I2V](https://huggingface.co/THUDM/CogVideoX-5b-I2V) | `transformer/diffusion_pytorch_model-00001-of-00003.safetensors` | BF16 | `(18432, 512)` | 37 | 349.2M |
| [THUDM/CogVideoX-5b-I2V](https://huggingface.co/THUDM/CogVideoX-5b-I2V) | `text_encoder/model-00001-of-00002.safetensors` | BF16 | `(32128, 4096)` | 1 | 131.6M |
| [THUDM/CogVideoX-5b-I2V](https://huggingface.co/THUDM/CogVideoX-5b-I2V) | `transformer/diffusion_pytorch_model-00001-of-00003.safetensors` | BF16 | `(1, 17776, 3072)` | 1 | 54.6M |
| [THUDM/CogVideoX-5b-I2V](https://huggingface.co/THUDM/CogVideoX-5b-I2V) | `transformer/diffusion_pytorch_model-00001-of-00003.safetensors` | BF16 | `(3072, 4096)` | 1 | 12.6M |
| [THUDM/CogVideoX-5b-I2V](https://huggingface.co/THUDM/CogVideoX-5b-I2V) | `transformer/diffusion_pytorch_model-00001-of-00003.safetensors` | BF16 | `(512, 3072)` | 1 | 1.6M |
| [THUDM/CogVideoX-5b-I2V](https://huggingface.co/THUDM/CogVideoX-5b-I2V) | `transformer/diffusion_pytorch_model-00001-of-00003.safetensors` | BF16 | `(18432)` | 37 | 682.0K |
| [THUDM/CogVideoX-5b-I2V](https://huggingface.co/THUDM/CogVideoX-5b-I2V) | `transformer/diffusion_pytorch_model-00001-of-00003.safetensors` | BF16 | `(3072)` | 170 | 522.2K |
| [THUDM/CogVideoX-5b-I2V](https://huggingface.co/THUDM/CogVideoX-5b-I2V) | `transformer/diffusion_pytorch_model-00001-of-00003.safetensors` | BF16 | `(3072, 32, 2, 2)` | 1 | 393.2K |
| [THUDM/CogVideoX-5b-I2V](https://huggingface.co/THUDM/CogVideoX-5b-I2V) | `transformer/diffusion_pytorch_model-00001-of-00003.safetensors` | BF16 | `(512, 512)` | 1 | 262.1K |
| [THUDM/CogVideoX-5b-I2V](https://huggingface.co/THUDM/CogVideoX-5b-I2V) | `transformer/diffusion_pytorch_model-00001-of-00003.safetensors` | BF16 | `(12288)` | 18 | 221.2K |
| [THUDM/CogVideoX-5b-I2V](https://huggingface.co/THUDM/CogVideoX-5b-I2V) | `text_encoder/model-00002-of-00002.safetensors` | BF16 | `(4096)` | 25 | 102.4K |
| [THUDM/CogVideoX-5b-I2V](https://huggingface.co/THUDM/CogVideoX-5b-I2V) | `text_encoder/model-00001-of-00002.safetensors` | BF16 | `(4096)` | 24 | 98.3K |
| [THUDM/CogVideoX-5b-I2V](https://huggingface.co/THUDM/CogVideoX-5b-I2V) | `transformer/diffusion_pytorch_model-00001-of-00003.safetensors` | BF16 | `(64)` | 76 | 4.9K |
| [THUDM/CogVideoX-5b-I2V](https://huggingface.co/THUDM/CogVideoX-5b-I2V) | `text_encoder/model-00001-of-00002.safetensors` | BF16 | `(32, 64)` | 1 | 2.0K |
| [THUDM/CogVideoX-5b-I2V](https://huggingface.co/THUDM/CogVideoX-5b-I2V) | `transformer/diffusion_pytorch_model-00001-of-00003.safetensors` | BF16 | `(512)` | 2 | 1.0K |
| [Tongyi-MAI/Z-Image-Turbo](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo) | `text_encoder/model-00002-of-00003.safetensors` | BF16 | `(9728, 2560)` | 39 | 971.2M |
| [Tongyi-MAI/Z-Image-Turbo](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo) | `text_encoder/model-00001-of-00003.safetensors` | BF16 | `(9728, 2560)` | 32 | 796.9M |
| [Tongyi-MAI/Z-Image-Turbo](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo) | `text_encoder/model-00002-of-00003.safetensors` | BF16 | `(2560, 9728)` | 20 | 498.1M |
| [Tongyi-MAI/Z-Image-Turbo](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo) | `text_encoder/model-00001-of-00003.safetensors` | BF16 | `(151936, 2560)` | 1 | 389.0M |
| [Tongyi-MAI/Z-Image-Turbo](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo) | `text_encoder/model-00001-of-00003.safetensors` | BF16 | `(2560, 9728)` | 15 | 373.6M |
| [Tongyi-MAI/Z-Image-Turbo](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo) | `text_encoder/model-00002-of-00003.safetensors` | BF16 | `(2560, 4096)` | 20 | 209.7M |
| [Tongyi-MAI/Z-Image-Turbo](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo) | `text_encoder/model-00002-of-00003.safetensors` | BF16 | `(4096, 2560)` | 20 | 209.7M |
| [Tongyi-MAI/Z-Image-Turbo](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo) | `text_encoder/model-00001-of-00003.safetensors` | BF16 | `(2560, 4096)` | 16 | 167.8M |
| [Tongyi-MAI/Z-Image-Turbo](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo) | `text_encoder/model-00001-of-00003.safetensors` | BF16 | `(4096, 2560)` | 16 | 167.8M |
| [Tongyi-MAI/Z-Image-Turbo](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo) | `text_encoder/model-00002-of-00003.safetensors` | BF16 | `(1024, 2560)` | 40 | 104.9M |
| [Tongyi-MAI/Z-Image-Turbo](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo) | `text_encoder/model-00001-of-00003.safetensors` | BF16 | `(1024, 2560)` | 32 | 83.9M |
| [Tongyi-MAI/Z-Image-Turbo](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo) | `text_encoder/model-00003-of-00003.safetensors` | BF16 | `(2560, 9728)` | 1 | 24.9M |
| [Tongyi-MAI/Z-Image-Turbo](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo) | `text_encoder/model-00003-of-00003.safetensors` | BF16 | `(9728, 2560)` | 1 | 24.9M |
| [Tongyi-MAI/Z-Image-Turbo](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo) | `text_encoder/model-00002-of-00003.safetensors` | BF16 | `(2560)` | 40 | 102.4K |
| [Tongyi-MAI/Z-Image-Turbo](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo) | `text_encoder/model-00001-of-00003.safetensors` | BF16 | `(2560)` | 30 | 76.8K |
| [Tongyi-MAI/Z-Image-Turbo](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo) | `text_encoder/model-00003-of-00003.safetensors` | BF16 | `(2560)` | 3 | 7.7K |
| [Tongyi-MAI/Z-Image-Turbo](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo) | `text_encoder/model-00002-of-00003.safetensors` | BF16 | `(128)` | 40 | 5.1K |
| [Tongyi-MAI/Z-Image-Turbo](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo) | `text_encoder/model-00001-of-00003.safetensors` | BF16 | `(128)` | 32 | 4.1K |
| [XLabs-AI/flux-lora-collection](https://huggingface.co/XLabs-AI/flux-lora-collection) | `art_lora_comfy_converted.safetensors` | BF16 | `(9216, 256)` | 38 | 89.7M |
| [XLabs-AI/flux-lora-collection](https://huggingface.co/XLabs-AI/flux-lora-collection) | `art_lora_comfy_converted.safetensors` | BF16 | `(256, 3072)` | 76 | 59.8M |
| [XLabs-AI/flux-lora-collection](https://huggingface.co/XLabs-AI/flux-lora-collection) | `art_lora_comfy_converted.safetensors` | BF16 | `(3072, 256)` | 38 | 29.9M |
| [XLabs-AI/flux-lora-collection](https://huggingface.co/XLabs-AI/flux-lora-collection) | `anime_lora_comfy_converted.safetensors` | BF16 | `(9216, 32)` | 38 | 11.2M |
| [XLabs-AI/flux-lora-collection](https://huggingface.co/XLabs-AI/flux-lora-collection) | `disney_lora_comfy_converted.safetensors` | BF16 | `(9216, 32)` | 38 | 11.2M |
| [XLabs-AI/flux-lora-collection](https://huggingface.co/XLabs-AI/flux-lora-collection) | `mjv6_lora_comfy_converted.safetensors` | BF16 | `(9216, 32)` | 38 | 11.2M |
| [XLabs-AI/flux-lora-collection](https://huggingface.co/XLabs-AI/flux-lora-collection) | `anime_lora_comfy_converted.safetensors` | BF16 | `(32, 3072)` | 76 | 7.5M |
| [XLabs-AI/flux-lora-collection](https://huggingface.co/XLabs-AI/flux-lora-collection) | `disney_lora_comfy_converted.safetensors` | BF16 | `(32, 3072)` | 76 | 7.5M |
| [XLabs-AI/flux-lora-collection](https://huggingface.co/XLabs-AI/flux-lora-collection) | `mjv6_lora_comfy_converted.safetensors` | BF16 | `(32, 3072)` | 76 | 7.5M |
| [XLabs-AI/flux-lora-collection](https://huggingface.co/XLabs-AI/flux-lora-collection) | `anime_lora_comfy_converted.safetensors` | BF16 | `(3072, 32)` | 38 | 3.7M |
| [XLabs-AI/flux-lora-collection](https://huggingface.co/XLabs-AI/flux-lora-collection) | `disney_lora_comfy_converted.safetensors` | BF16 | `(3072, 32)` | 38 | 3.7M |
| [XLabs-AI/flux-lora-collection](https://huggingface.co/XLabs-AI/flux-lora-collection) | `mjv6_lora_comfy_converted.safetensors` | BF16 | `(3072, 32)` | 38 | 3.7M |

## Notes on interpretation

- **GGUF** entries are K-quantized llama.cpp checkpoints (`Q4_0`, `Q8_0`); they are portable at the file level but their launcher may still install a CUDA-only loader. Safetensors headers do not apply to them, so precision comes from the filename.
- **PyTorch** here means `.safetensors`, `.bin`, `.pt`, `.pth` or `.ckpt` checkpoints requested by the launcher. Many such repos also contain config/tokenizer files that are not listed.
- **Multi-precision checkpoints** are common: diffusion pipelines keep most weights in FP8/FP16/BF16 but retain text encoders, embeddings or normalization tensors in another dtype. The dominant dtype is reported first; the others are listed after it.
- **unspecified** means neither a parseable safetensors header nor HF aggregate metadata was available (typically a gated repo or a non-safetensors format), and the launcher gave no precision-bearing filename.
