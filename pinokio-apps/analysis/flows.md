# Common matrix-multiply flows across Pinokio apps

Companion to [`results/pinokio-apps.md`](../results/pinokio-apps.md) and [`models.md`](models.md). Per-project graphs and interactive viewers are in [`../flows/`](../flows/).

Across the 101 projects, **43,886 matmul operations** were reconstructed from the safetensors headers of 61 model checkpoints. Only 22 projects pull a checkpoint with a weight-level graph; the rest are launchers around externally managed models.

## How to read A, B and C

`B` is the stored weight matrix `[out_features, in_features]`; `A` is the activation `[B, S, in_features]` flowing in; `C` is the output `[B, S, out_features]`. Activation precision is inferred from the weight dtype — FP8/INT8/NF4 checkpoints compute in BF16/FP16 with FP32 accumulation for attention scores. Shapes are taken from the exact checkpoint tensor headers; `B`/`S`/`H`/`D` denote batch, sequence, heads and head dimension where the checkpoint alone cannot fix them.

## Most common role sequences

| Component | Role sequence | Blocks observed |
| --- | --- | --- |
| single_blocks | Projection / FFN → Other linear | 217 |
| transformer | Projection / FFN → Other linear | 195 |
| conditioner | Attention output → Projection / FFN | 180 |
| vae | Q projection → K projection → V projection → Attention output → MLP gate → MLP up → MLP down | 164 |
| conditioner | Q projection → K projection → V projection → Attention output → MLP gate → MLP up → MLP down | 139 |
| transformer | Q projection → K projection → V projection → Attention output → Projection / FFN → Other linear | 114 |
| transformer | Q projection → K projection → V projection → Attention output → MLP up → MLP down | 107 |
| double_blocks | Projection / FFN → Other linear | 95 |
| transformer | Q projection → K projection → V projection → Attention output → Projection / FFN → Convolution (im2col matmul) → 1×1 conv matmul → Other linear | 84 |
| transformer | Q projection → K projection → V projection → MLP gate → MLP up → MLP down → Projection / FFN | 75 |
| transformer | MLP up → MLP down → Projection / FFN → Other linear | 68 |
| conditioner | Q projection → K projection → V projection → Attention output → MLP up → MLP down | 66 |

## Representative A / B / C by pattern

Counts and the most frequent concrete matrix dimensions are taken from all reconstructed ops of that role.

| Pattern | Ops | A shape & precision | B shape & precision | C shape & precision |
| --- | --- | --- | --- | --- |
| Transformer self-attention Q projection | 3,310 | `[B, S, 1280]` (1028); `[B, S, 4096]` (494) · `FP16` (1861); `FP32` (659) | `[1280, 1280]` (1028); `[4096, 4096]` (494) · `F16` (1861); `F32` (659) | `[B, S, 1280]` (1028); `[B, S, 4096]` (530) · `FP16` (1861); `FP32` (659) |
| Transformer self-attention K projection | 3,279 | `[B, S, 1280]` (618); `[B, S, 2048]` (532) · `FP16` (1861); `FP32` (628) | `[1280, 1280]` (530); `[4096, 4096]` (427) · `F16` (1861); `F32` (628) | `[B, S, 1280]` (1028); `[B, S, 768]` (427) · `FP16` (1861); `FP32` (628) |
| Transformer self-attention V projection | 3,355 | `[B, S, 1280]` (618); `[B, S, 768]` (548) · `FP16` (1861); `FP32` (706) | `[1280, 1280]` (530); `[4096, 4096]` (427) · `F16` (1861); `F32` (706) | `[B, S, 1280]` (1028); `[B, S, 768]` (460) · `FP16` (1861); `FP32` (706) |
| Attention scores Q×Kᵀ | 84 | `[B, H, S, D]` (84) · `FP16` (39); `FP32` (21) | `[B, H, D, S] (K^T)` (84) · `—` (84) | `[B, H, S, S]` (84) · `FP16` (39); `FP32` (21) |
| Attention context softmax×V | 84 | `[B, H, S, S]` (84) · `FP16` (39); `FP32` (21) | `[B, H, S, D] (V)` (84) · `—` (84) | `[B, H, S, D]` (84) · `FP16` (39); `FP32` (21) |
| Attention output projection | 3,868 | `[B, S, 1280]` (1592); `[B, S, 768]` (446) · `FP16` (2287); `FP32` (887) | `[1280, 1280]` (1592); `[768, 768]` (445) · `F16` (2287); `F32` (887) | `[B, S, 1280]` (1592); `[B, S, 768]` (446) · `FP16` (2287); `FP32` (887) |
| MLP gate / up projection | 1,339 | `[B, S, 4096]` (490); `[B, S, 768]` (349) · `FP16` (646); `BF16 (FP8 weights)` (280) | `[10240, 4096]` (426); `[3072, 768]` (349) · `F16` (646); `F8_E4M3` (280) | `[B, S, 10240]` (426); `[B, S, 3072]` (349) · `FP16` (646); `BF16 (FP8 weights)` (280) |
| MLP down projection | 1,367 | `[B, S, 10240]` (426); `[B, S, 3072]` (349) · `FP16` (644); `FP32` (289) | `[4096, 10240]` (426); `[768, 3072]` (349) · `F16` (644); `F32` (289) | `[B, S, 4096]` (500); `[B, S, 768]` (349) · `FP16` (644); `FP32` (289) |
| UNet / VAE convolution (im2col matmul) | 5,503 | `[B, 512, spatial]` (1750); `[B, 128, spatial]` (758) · `FP32` (2813); `FP16` (2318) | `[512, 512, 3, 3]` (1411); `[128, 128, 3, 3]` (475) · `F32` (2813); `F16` (2318) | `[B, 512, spatial']` (1788); `[B, 1280, spatial']` (738) · `FP32` (2813); `FP16` (2318) |
| Output head / classifier | 9 | `[B, S, 3072]` (3); `[B, S, 768]` (3) · `FP32` (5); `BF16` (3) | `[6144, 3072]` (3); `[64, 5120]` (2) · `F32` (5); `BF16` (3) | `[B, S, 6144]` (3); `[B, S, 64]` (2) · `FP32` (5); `BF16` (3) |

## Precision of weight matrices and activations

| Weight dtype | Matmul ops | Inferred activation dtype |
| --- | --- | --- |
| F16 | 22,240 | FP16 (22240) |
| F32 | 10,007 | FP32 (10007) |
| BF16 | 6,486 | BF16 (6486) |
| F8_E4M3 | 3,733 | BF16 (FP8 weights) (3733) |
| U8 | 1,252 | BF16 (packed 4-bit weights) (1252) |
| — | 168 | FP16 (78), FP32 (42), BF16 (42) |

## Porting implications

- FP16/BF16 linear and attention matmuls map cleanly to ROCm and to MPS via PyTorch SDPA; these dominate the reconstructed graphs.
- FP8 (`F8_E4M3`, `F8_E5M2`) and INT8/NF4 weight matrices require a matching quantized GEMM kernel — CUDA-first today, with limited ROCm support and no MPS equivalent. Their activations are typically BF16, so the precision boundary is at the weight only.
- Convolution im2col matmuls in VAE/UNet blocks are backend-agnostic but expensive; the vendor convolution library, not the matmul itself, is what must be ported.
- The two derived attention ops (Q×Kᵀ, softmax×V) are exactly what PyTorch SDPA, FlashAttention and xformers replace with fused kernels — see [`kernels.md`](kernels.md).

## Per-project graphs

| Project | Models | Matmul ops | Flow report | Viewer |
| --- | --- | --- | --- | --- |
| [accdiffusion](https://github.com/pinokiofactory/accdiffusion) | 0 | 0 | [`accdiffusion.md`](../flows/accdiffusion.md) | [`accdiffusion.html`](../flows/accdiffusion.html) |
| [ACE-Step](https://github.com/pinokiofactory/ACE-Step) | 0 | 0 | [`ACE-Step.md`](../flows/ACE-Step.md) | [`ACE-Step.html`](../flows/ACE-Step.html) |
| [ai-toolkit](https://github.com/pinokiofactory/ai-toolkit) | 0 | 0 | [`ai-toolkit.md`](../flows/ai-toolkit.md) | [`ai-toolkit.html`](../flows/ai-toolkit.html) |
| [ai-video-composer](https://github.com/pinokiofactory/ai-video-composer) | 0 | 0 | [`ai-video-composer.md`](../flows/ai-video-composer.md) | [`ai-video-composer.html`](../flows/ai-video-composer.html) |
| [Allegro-txt2vid](https://github.com/pinokiofactory/Allegro-txt2vid) | 4 | 209 | [`Allegro-txt2vid.md`](../flows/Allegro-txt2vid.md) | [`Allegro-txt2vid.html`](../flows/Allegro-txt2vid.html) |
| [Allegro-txt2vid-install](https://github.com/pinokiofactory/Allegro-txt2vid-install) | 1 | 0 | [`Allegro-txt2vid-install.md`](../flows/Allegro-txt2vid-install.md) | [`Allegro-txt2vid-install.html`](../flows/Allegro-txt2vid-install.html) |
| [AllTalk-TTS](https://github.com/pinokiofactory/AllTalk-TTS) | 0 | 0 | [`AllTalk-TTS.md`](../flows/AllTalk-TTS.md) | [`AllTalk-TTS.html`](../flows/AllTalk-TTS.html) |
| [applio](https://github.com/pinokiofactory/applio) | 0 | 0 | [`applio.md`](../flows/applio.md) | [`applio.html`](../flows/applio.html) |
| [applio-old](https://github.com/pinokiofactory/applio-old) | 1 | 0 | [`applio-old.md`](../flows/applio-old.md) | [`applio-old.html`](../flows/applio-old.html) |
| [artist](https://github.com/pinokiofactory/artist) | 0 | 0 | [`artist.md`](../flows/artist.md) | [`artist.html`](../flows/artist.html) |
| [audiocraft_plus](https://github.com/pinokiofactory/audiocraft_plus) | 0 | 0 | [`audiocraft_plus.md`](../flows/audiocraft_plus.md) | [`audiocraft_plus.html`](../flows/audiocraft_plus.html) |
| [AudioX](https://github.com/pinokiofactory/AudioX) | 1 | 0 | [`AudioX.md`](../flows/AudioX.md) | [`AudioX.html`](../flows/AudioX.html) |
| [augmentoolkit](https://github.com/pinokiofactory/augmentoolkit) | 0 | 0 | [`augmentoolkit.md`](../flows/augmentoolkit.md) | [`augmentoolkit.html`](../flows/augmentoolkit.html) |
| [aura-sr-upscaler](https://github.com/pinokiofactory/aura-sr-upscaler) | 0 | 0 | [`aura-sr-upscaler.md`](../flows/aura-sr-upscaler.md) | [`aura-sr-upscaler.html`](../flows/aura-sr-upscaler.html) |
| [autogpt](https://github.com/pinokiofactory/autogpt) | 0 | 0 | [`autogpt.md`](../flows/autogpt.md) | [`autogpt.html`](../flows/autogpt.html) |
| [bolt](https://github.com/pinokiofactory/bolt) | 0 | 0 | [`bolt.md`](../flows/bolt.md) | [`bolt.html`](../flows/bolt.html) |
| [browser-use](https://github.com/pinokiofactory/browser-use) | 0 | 0 | [`browser-use.md`](../flows/browser-use.md) | [`browser-use.html`](../flows/browser-use.html) |
| [clarity-refiners-ui](https://github.com/pinokiofactory/clarity-refiners-ui) | 8 | 2,011 | [`clarity-refiners-ui.md`](../flows/clarity-refiners-ui.md) | [`clarity-refiners-ui.html`](../flows/clarity-refiners-ui.html) |
| [cogstudio](https://github.com/pinokiofactory/cogstudio) | 4 | 649 | [`cogstudio.md`](../flows/cogstudio.md) | [`cogstudio.html`](../flows/cogstudio.html) |
| [cogvideo](https://github.com/pinokiofactory/cogvideo) | 0 | 0 | [`cogvideo.md`](../flows/cogvideo.md) | [`cogvideo.html`](../flows/cogvideo.html) |
| [comfy](https://github.com/pinokiofactory/comfy) | 28 | 15,071 | [`comfy.md`](../flows/comfy.md) | [`comfy.html`](../flows/comfy.html) |
| [controlyourself](https://github.com/pinokiofactory/controlyourself) | 0 | 0 | [`controlyourself.md`](../flows/controlyourself.md) | [`controlyourself.html`](../flows/controlyourself.html) |
| [cube](https://github.com/pinokiofactory/cube) | 1 | 488 | [`cube.md`](../flows/cube.md) | [`cube.html`](../flows/cube.html) |
| [dia](https://github.com/pinokiofactory/dia) | 0 | 0 | [`dia.md`](../flows/dia.md) | [`dia.html`](../flows/dia.html) |
| [diamond](https://github.com/pinokiofactory/diamond) | 0 | 0 | [`diamond.md`](../flows/diamond.md) | [`diamond.html`](../flows/diamond.html) |
| [diffrhythm](https://github.com/pinokiofactory/diffrhythm) | 0 | 0 | [`diffrhythm.md`](../flows/diffrhythm.md) | [`diffrhythm.html`](../flows/diffrhythm.html) |
| [diffusers-image-fill](https://github.com/pinokiofactory/diffusers-image-fill) | 0 | 0 | [`diffusers-image-fill.md`](../flows/diffusers-image-fill.md) | [`diffusers-image-fill.html`](../flows/diffusers-image-fill.html) |
| [ditto](https://github.com/pinokiofactory/ditto) | 0 | 0 | [`ditto.md`](../flows/ditto.md) | [`ditto.html`](../flows/ditto.html) |
| [dough](https://github.com/pinokiofactory/dough) | 0 | 0 | [`dough.md`](../flows/dough.md) | [`dough.html`](../flows/dough.html) |
| [e2-f5-tts](https://github.com/pinokiofactory/e2-f5-tts) | 0 | 0 | [`e2-f5-tts.md`](../flows/e2-f5-tts.md) | [`e2-f5-tts.html`](../flows/e2-f5-tts.html) |
| [echomimic2](https://github.com/pinokiofactory/echomimic2) | 4 | 74 | [`echomimic2.md`](../flows/echomimic2.md) | [`echomimic2.html`](../flows/echomimic2.html) |
| [errortest](https://github.com/pinokiofactory/errortest) | 0 | 0 | [`errortest.md`](../flows/errortest.md) | [`errortest.html`](../flows/errortest.html) |
| [facepoke](https://github.com/pinokiofactory/facepoke) | 0 | 0 | [`facepoke.md`](../flows/facepoke.md) | [`facepoke.html`](../flows/facepoke.html) |
| [factory](https://github.com/pinokiofactory/factory) | 0 | 0 | [`factory.md`](../flows/factory.md) | [`factory.html`](../flows/factory.html) |
| [flashdiffusion](https://github.com/pinokiofactory/flashdiffusion) | 0 | 0 | [`flashdiffusion.md`](../flows/flashdiffusion.md) | [`flashdiffusion.html`](../flows/flashdiffusion.html) |
| [florence-sam](https://github.com/pinokiofactory/florence-sam) | 0 | 0 | [`florence-sam.md`](../flows/florence-sam.md) | [`florence-sam.html`](../flows/florence-sam.html) |
| [florence2](https://github.com/pinokiofactory/florence2) | 0 | 0 | [`florence2.md`](../flows/florence2.md) | [`florence2.html`](../flows/florence2.html) |
| [flux-webui](https://github.com/pinokiofactory/flux-webui) | 6 | 246 | [`flux-webui.md`](../flows/flux-webui.md) | [`flux-webui.html`](../flows/flux-webui.html) |
| [forge](https://github.com/pinokiofactory/forge) | 9 | 7,236 | [`forge.md`](../flows/forge.md) | [`forge.html`](../flows/forge.html) |
| [Frame-Pack](https://github.com/pinokiofactory/Frame-Pack) | 4 | 1,351 | [`Frame-Pack.md`](../flows/Frame-Pack.md) | [`Frame-Pack.html`](../flows/Frame-Pack.html) |
| [hallo](https://github.com/pinokiofactory/hallo) | 1 | 441 | [`hallo.md`](../flows/hallo.md) | [`hallo.html`](../flows/hallo.html) |
| [hertz](https://github.com/pinokiofactory/hertz) | 0 | 0 | [`hertz.md`](../flows/hertz.md) | [`hertz.html`](../flows/hertz.html) |
| [Hunyuan3D-2](https://github.com/pinokiofactory/Hunyuan3D-2) | 0 | 0 | [`Hunyuan3D-2.md`](../flows/Hunyuan3D-2.md) | [`Hunyuan3D-2.html`](../flows/Hunyuan3D-2.html) |
| [Hunyuan3d-2-lowvram](https://github.com/pinokiofactory/Hunyuan3d-2-lowvram) | 0 | 0 | [`Hunyuan3d-2-lowvram.md`](../flows/Hunyuan3d-2-lowvram.md) | [`Hunyuan3d-2-lowvram.html`](../flows/Hunyuan3d-2-lowvram.html) |
| [Hunyuan3D-2-mini](https://github.com/pinokiofactory/Hunyuan3D-2-mini) | 0 | 0 | [`Hunyuan3D-2-mini.md`](../flows/Hunyuan3D-2-mini.md) | [`Hunyuan3D-2-mini.html`](../flows/Hunyuan3D-2-mini.html) |
| [hunyuanvideo](https://github.com/pinokiofactory/hunyuanvideo) | 0 | 0 | [`hunyuanvideo.md`](../flows/hunyuanvideo.md) | [`hunyuanvideo.html`](../flows/hunyuanvideo.html) |
| [Ilaria-RVC](https://github.com/pinokiofactory/Ilaria-RVC) | 0 | 0 | [`Ilaria-RVC.md`](../flows/Ilaria-RVC.md) | [`Ilaria-RVC.html`](../flows/Ilaria-RVC.html) |
| [instantir](https://github.com/pinokiofactory/instantir) | 0 | 0 | [`instantir.md`](../flows/instantir.md) | [`instantir.html`](../flows/instantir.html) |
| [invoke](https://github.com/pinokiofactory/invoke) | 0 | 0 | [`invoke.md`](../flows/invoke.md) | [`invoke.html`](../flows/invoke.html) |
| [janus](https://github.com/pinokiofactory/janus) | 0 | 0 | [`janus.md`](../flows/janus.md) | [`janus.html`](../flows/janus.html) |
| [Kokoro-TTS](https://github.com/pinokiofactory/Kokoro-TTS) | 1 | 0 | [`Kokoro-TTS.md`](../flows/Kokoro-TTS.md) | [`Kokoro-TTS.html`](../flows/Kokoro-TTS.html) |
| [liveportrait](https://github.com/pinokiofactory/liveportrait) | 2 | 0 | [`liveportrait.md`](../flows/liveportrait.md) | [`liveportrait.html`](../flows/liveportrait.html) |
| [llamafactory](https://github.com/pinokiofactory/llamafactory) | 0 | 0 | [`llamafactory.md`](../flows/llamafactory.md) | [`llamafactory.html`](../flows/llamafactory.html) |
| [LTX-Desktop-WanGP](https://github.com/pinokiofactory/LTX-Desktop-WanGP) | 0 | 0 | [`LTX-Desktop-WanGP.md`](../flows/LTX-Desktop-WanGP.md) | [`LTX-Desktop-WanGP.html`](../flows/LTX-Desktop-WanGP.html) |
| [macOS-use](https://github.com/pinokiofactory/macOS-use) | 0 | 0 | [`macOS-use.md`](../flows/macOS-use.md) | [`macOS-use.html`](../flows/macOS-use.html) |
| [MagicQuill](https://github.com/pinokiofactory/MagicQuill) | 1 | 1,500 | [`MagicQuill.md`](../flows/MagicQuill.md) | [`MagicQuill.html`](../flows/MagicQuill.html) |
| [MatAnyone](https://github.com/pinokiofactory/MatAnyone) | 0 | 0 | [`MatAnyone.md`](../flows/MatAnyone.md) | [`MatAnyone.html`](../flows/MatAnyone.html) |
| [mcp](https://github.com/pinokiofactory/mcp) | 0 | 0 | [`mcp.md`](../flows/mcp.md) | [`mcp.html`](../flows/mcp.html) |
| [MFLUX-WEBUI](https://github.com/pinokiofactory/MFLUX-WEBUI) | 0 | 0 | [`MFLUX-WEBUI.md`](../flows/MFLUX-WEBUI.md) | [`MFLUX-WEBUI.html`](../flows/MFLUX-WEBUI.html) |
| [mlx](https://github.com/pinokiofactory/mlx) | 0 | 0 | [`mlx.md`](../flows/mlx.md) | [`mlx.html`](../flows/mlx.html) |
| [mlx-video-transcription](https://github.com/pinokiofactory/mlx-video-transcription) | 0 | 0 | [`mlx-video-transcription.md`](../flows/mlx-video-transcription.md) | [`mlx-video-transcription.html`](../flows/mlx-video-transcription.html) |
| [mlx-video-ui](https://github.com/pinokiofactory/mlx-video-ui) | 0 | 0 | [`mlx-video-ui.md`](../flows/mlx-video-ui.md) | [`mlx-video-ui.html`](../flows/mlx-video-ui.html) |
| [MMAudio](https://github.com/pinokiofactory/MMAudio) | 0 | 0 | [`MMAudio.md`](../flows/MMAudio.md) | [`MMAudio.html`](../flows/MMAudio.html) |
| [mochi](https://github.com/pinokiofactory/mochi) | 1 | 606 | [`mochi.md`](../flows/mochi.md) | [`mochi.html`](../flows/mochi.html) |
| [moshi](https://github.com/pinokiofactory/moshi) | 0 | 0 | [`moshi.md`](../flows/moshi.md) | [`moshi.html`](../flows/moshi.html) |
| [Nari-Dia-TTS](https://github.com/pinokiofactory/Nari-Dia-TTS) | 1 | 263 | [`Nari-Dia-TTS.md`](../flows/Nari-Dia-TTS.md) | [`Nari-Dia-TTS.html`](../flows/Nari-Dia-TTS.html) |
| [oasis](https://github.com/pinokiofactory/oasis) | 1 | 209 | [`oasis.md`](../flows/oasis.md) | [`oasis.html`](../flows/oasis.html) |
| [ominicontrol](https://github.com/pinokiofactory/ominicontrol) | 0 | 0 | [`ominicontrol.md`](../flows/ominicontrol.md) | [`ominicontrol.html`](../flows/ominicontrol.html) |
| [omnigen](https://github.com/pinokiofactory/omnigen) | 0 | 0 | [`omnigen.md`](../flows/omnigen.md) | [`omnigen.html`](../flows/omnigen.html) |
| [omniparser](https://github.com/pinokiofactory/omniparser) | 1 | 313 | [`omniparser.md`](../flows/omniparser.md) | [`omniparser.html`](../flows/omniparser.html) |
| [open-webui](https://github.com/pinokiofactory/open-webui) | 0 | 0 | [`open-webui.md`](../flows/open-webui.md) | [`open-webui.html`](../flows/open-webui.html) |
| [openaudio](https://github.com/pinokiofactory/openaudio) | 0 | 0 | [`openaudio.md`](../flows/openaudio.md) | [`openaudio.html`](../flows/openaudio.html) |
| [openui](https://github.com/pinokiofactory/openui) | 0 | 0 | [`openui.md`](../flows/openui.md) | [`openui.html`](../flows/openui.html) |
| [Orpheus-TTS-FastAPI](https://github.com/pinokiofactory/Orpheus-TTS-FastAPI) | 1 | 0 | [`Orpheus-TTS-FastAPI.md`](../flows/Orpheus-TTS-FastAPI.md) | [`Orpheus-TTS-FastAPI.html`](../flows/Orpheus-TTS-FastAPI.html) |
| [ovis](https://github.com/pinokiofactory/ovis) | 1 | 228 | [`ovis.md`](../flows/ovis.md) | [`ovis.html`](../flows/ovis.html) |
| [pcm](https://github.com/pinokiofactory/pcm) | 0 | 0 | [`pcm.md`](../flows/pcm.md) | [`pcm.html`](../flows/pcm.html) |
| [photomaker2](https://github.com/pinokiofactory/photomaker2) | 0 | 0 | [`photomaker2.md`](../flows/photomaker2.md) | [`photomaker2.html`](../flows/photomaker2.html) |
| [pyramidflow](https://github.com/pinokiofactory/pyramidflow) | 0 | 0 | [`pyramidflow.md`](../flows/pyramidflow.md) | [`pyramidflow.html`](../flows/pyramidflow.html) |
| [rc-stableaudio](https://github.com/pinokiofactory/rc-stableaudio) | 0 | 0 | [`rc-stableaudio.md`](../flows/rc-stableaudio.md) | [`rc-stableaudio.html`](../flows/rc-stableaudio.html) |
| [RMBG-2-Studio](https://github.com/pinokiofactory/RMBG-2-Studio) | 1 | 0 | [`RMBG-2-Studio.md`](../flows/RMBG-2-Studio.md) | [`RMBG-2-Studio.html`](../flows/RMBG-2-Studio.html) |
| [RuinedFooocus](https://github.com/pinokiofactory/RuinedFooocus) | 0 | 0 | [`RuinedFooocus.md`](../flows/RuinedFooocus.md) | [`RuinedFooocus.html`](../flows/RuinedFooocus.html) |
| [sd35](https://github.com/pinokiofactory/sd35) | 2 | 756 | [`sd35.md`](../flows/sd35.md) | [`sd35.html`](../flows/sd35.html) |
| [sillytavern](https://github.com/pinokiofactory/sillytavern) | 0 | 0 | [`sillytavern.md`](../flows/sillytavern.md) | [`sillytavern.html`](../flows/sillytavern.html) |
| [SongGeneration-Studio-MLX](https://github.com/pinokiofactory/SongGeneration-Studio-MLX) | 1 | 0 | [`SongGeneration-Studio-MLX.md`](../flows/SongGeneration-Studio-MLX.md) | [`SongGeneration-Studio-MLX.html`](../flows/SongGeneration-Studio-MLX.html) |
| [stable-diffusion-webui-forge](https://github.com/pinokiofactory/stable-diffusion-webui-forge) | 13 | 9,722 | [`stable-diffusion-webui-forge.md`](../flows/stable-diffusion-webui-forge.md) | [`stable-diffusion-webui-forge.html`](../flows/stable-diffusion-webui-forge.html) |
| [stable-fast-3d](https://github.com/pinokiofactory/stable-fast-3d) | 1 | 427 | [`stable-fast-3d.md`](../flows/stable-fast-3d.md) | [`stable-fast-3d.html`](../flows/stable-fast-3d.html) |
| [stableaudio](https://github.com/pinokiofactory/stableaudio) | 0 | 0 | [`stableaudio.md`](../flows/stableaudio.md) | [`stableaudio.html`](../flows/stableaudio.html) |
| [StreamDiffusion](https://github.com/pinokiofactory/StreamDiffusion) | 4 | 1,552 | [`StreamDiffusion.md`](../flows/StreamDiffusion.md) | [`StreamDiffusion.html`](../flows/StreamDiffusion.html) |
| [StyleTTS2_Studio](https://github.com/pinokiofactory/StyleTTS2_Studio) | 0 | 0 | [`StyleTTS2_Studio.md`](../flows/StyleTTS2_Studio.md) | [`StyleTTS2_Studio.html`](../flows/StyleTTS2_Studio.html) |
| [text2midi](https://github.com/pinokiofactory/text2midi) | 1 | 0 | [`text2midi.md`](../flows/text2midi.md) | [`text2midi.html`](../flows/text2midi.html) |
| [TRELLIS](https://github.com/pinokiofactory/TRELLIS) | 0 | 0 | [`TRELLIS.md`](../flows/TRELLIS.md) | [`TRELLIS.html`](../flows/TRELLIS.html) |
| [Ultimate-TTS-Studio](https://github.com/pinokiofactory/Ultimate-TTS-Studio) | 1 | 0 | [`Ultimate-TTS-Studio.md`](../flows/Ultimate-TTS-Studio.md) | [`Ultimate-TTS-Studio.html`](../flows/Ultimate-TTS-Studio.html) |
| [uno](https://github.com/pinokiofactory/uno) | 0 | 0 | [`uno.md`](../flows/uno.md) | [`uno.html`](../flows/uno.html) |
| [vibevoice-realtime](https://github.com/pinokiofactory/vibevoice-realtime) | 1 | 278 | [`vibevoice-realtime.md`](../flows/vibevoice-realtime.md) | [`vibevoice-realtime.html`](../flows/vibevoice-realtime.html) |
| [video-background-removal](https://github.com/pinokiofactory/video-background-removal) | 0 | 0 | [`video-background-removal.md`](../flows/video-background-removal.md) | [`video-background-removal.html`](../flows/video-background-removal.html) |
| [wan](https://github.com/pinokiofactory/wan) | 0 | 0 | [`wan.md`](../flows/wan.md) | [`wan.html`](../flows/wan.html) |
| [whisper-webui](https://github.com/pinokiofactory/whisper-webui) | 0 | 0 | [`whisper-webui.md`](../flows/whisper-webui.md) | [`whisper-webui.html`](../flows/whisper-webui.html) |
| [y](https://github.com/pinokiofactory/y) | 0 | 0 | [`y.md`](../flows/y.md) | [`y.html`](../flows/y.html) |
| [yue](https://github.com/pinokiofactory/yue) | 1 | 0 | [`yue.md`](../flows/yue.md) | [`yue.html`](../flows/yue.html) |
| [z-image-turbo](https://github.com/pinokiofactory/z-image-turbo) | 1 | 256 | [`z-image-turbo.md`](../flows/z-image-turbo.md) | [`z-image-turbo.html`](../flows/z-image-turbo.html) |
| [zonos](https://github.com/pinokiofactory/zonos) | 0 | 0 | [`zonos.md`](../flows/zonos.md) | [`zonos.html`](../flows/zonos.html) |
