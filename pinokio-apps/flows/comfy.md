# Matrix-multiply flow — comfy

Companion to [`results/pinokio-apps.md`](../results/pinokio-apps.md) and [`analysis/flows.md`](../analysis/flows.md). Interactive viewer: [`comfy.html`](comfy.html).

**Models whose checkpoints were analysed:** [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged), [Comfy-Org/flux1-dev](https://huggingface.co/Comfy-Org/flux1-dev), [Comfy-Org/flux1-schnell](https://huggingface.co/Comfy-Org/flux1-schnell), [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged), [Comfy-Org/sigclip_vision_384](https://huggingface.co/Comfy-Org/sigclip_vision_384), [Comfy-Org/stable-diffusion-3.5-fp8](https://huggingface.co/Comfy-Org/stable-diffusion-3.5-fp8), [Kijai/HunyuanVideo_comfy](https://huggingface.co/Kijai/HunyuanVideo_comfy), [Kijai/llava-llama-3-8b-text-encoder-tokenizer](https://huggingface.co/Kijai/llava-llama-3-8b-text-encoder-tokenizer), [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video), [city96/FLUX.1-dev-gguf](https://huggingface.co/city96/FLUX.1-dev-gguf), [city96/FLUX.1-schnell-gguf](https://huggingface.co/city96/FLUX.1-schnell-gguf), [cocktailpeanut/fcanny](https://huggingface.co/cocktailpeanut/fcanny), [cocktailpeanut/fdepth](https://huggingface.co/cocktailpeanut/fdepth), [cocktailpeanut/fill](https://huggingface.co/cocktailpeanut/fill), [cocktailpeanut/redux](https://huggingface.co/cocktailpeanut/redux), [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv), [cocktailpeanut/xulf-dev](https://huggingface.co/cocktailpeanut/xulf-dev), [cocktailpeanut/xulf-schnell](https://huggingface.co/cocktailpeanut/xulf-schnell), [comfyanonymous/flux_text_encoders](https://huggingface.co/comfyanonymous/flux_text_encoders), [drbaph/FLUX.1-schnell-dev-merged-fp8-4step](https://huggingface.co/drbaph/FLUX.1-schnell-dev-merged-fp8-4step), [latent-consistency/lcm-lora-sdxl](https://huggingface.co/latent-consistency/lcm-lora-sdxl), [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4), [openai/clip-vit-large-patch14](https://huggingface.co/openai/clip-vit-large-patch14), [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5), [silveroxides/flux1-nf4-weights](https://huggingface.co/silveroxides/flux1-nf4-weights), [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo), [stabilityai/stable-diffusion-2-1](https://huggingface.co/stabilityai/stable-diffusion-2-1), [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0)

Reconstructed **15,071 matmul operations** from 24 checkpoint(s) (39 safetensors files).

## How the flow was inferred

The launcher snapshots are wrappers, so the graph is reconstructed from the safetensors header of each checkpoint the launcher downloads. Tensor **names** encode the layer role (Q/K/V, attention out, MLP gate/up/down, conv, head), **shapes** encode the matrix dimensions (PyTorch stores linear weights as `[out_features, in_features]`), and **dtypes** give weight precision. Activation precision is inferred from the weight dtype (quantized weights imply BF16/FP16 compute). `B` is the weight matrix; `A` is the activation `[B, S, in]` and `C` the output `[B, S, out]`. Two extra ops per attention block (Q×Kᵀ and softmax×V) are derived from the Q/K/V triple. This is an inferred dataflow, not a traced execution.

## Flow summary

| Component | Matmul ops | Weight dtypes | Activation dtypes |
| --- | --- | --- | --- |
| transformer | 7,963 | F16 (4355), F8_E4M3 (1416), F32 (783), BF16 (767) | FP16 (4367), BF16 (FP8 weights) (1416), FP32 (785), BF16 (769) |
| conditioner | 2,200 | F16 (1182), F8_E4M3 (844), F32 (144), — (26) | FP16 (1200), BF16 (FP8 weights) (846), FP32 (148), BF16 (6) |
| vae | 1,839 | F16 (740), F32 (510), F8_E4M3 (336), BF16 (241) | FP16 (746), FP32 (510), BF16 (FP8 weights) (340), BF16 (243) |
| double_blocks | 1,150 | BF16 (950), F8_E4M3 (200) | BF16 (950), BF16 (FP8 weights) (200) |
| blocks | 964 | BF16 (960), — (4) | BF16 (964) |
| single_blocks | 690 | BF16 (570), F8_E4M3 (120) | BF16 (570), BF16 (FP8 weights) (120) |
| unet | 176 | F16 (176) | FP16 (176) |
| txt_in | 18 | BF16 (18) | BF16 (18) |
| time_in | 12 | BF16 (12) | BF16 (12) |
| vector_in | 12 | BF16 (12) | BF16 (12) |
| guidance_in | 10 | BF16 (10) | BF16 (10) |
| final_layer | 6 | BF16 (6) | BF16 (6) |
| img_in | 6 | BF16 (6) | BF16 (6) |
| img_emb | 4 | BF16 (4) | BF16 (4) |
| text_embedding | 4 | BF16 (4) | BF16 (4) |
| time_embedding | 4 | BF16 (4) | BF16 (4) |
| head | 2 | BF16 (2) | BF16 (2) |
| patch_embedding | 2 | BF16 (2) | BF16 (2) |
| time_projection | 2 | BF16 (2) | BF16 (2) |
| visual_projection | 2 | F16 (1), F32 (1) | FP16 (1), FP32 (1) |
| post_quant_conv | 1 | BF16 (1) | BF16 (1) |
| quant_conv | 1 | BF16 (1) | BF16 (1) |
| redux_down | 1 | BF16 (1) | BF16 (1) |
| redux_up | 1 | BF16 (1) | BF16 (1) |
| text_projection | 1 | F32 (1) | FP32 (1) |

## Representative block sequence — [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged), `vae`, block 0

This is one coherent pass through a repeated transformer/UNet block; the aggregated roles across every block follow in the next section.

| # | Role | Operation | A (activation) | B (weight) | C (output) | Precision |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Q projection | Matmul (linear) | [B, S, 4096] FP16 | [4096, 4096] F16 | [B, S, 4096] FP16 | F16 weights / FP16 activations |
| 2 | K projection | Matmul (linear) | [B, S, 4096] FP16 | [4096, 4096] F16 | [B, S, 4096] FP16 | F16 weights / FP16 activations |
| 3 | V projection | Matmul (linear) | [B, S, 4096] FP16 | [4096, 4096] F16 | [B, S, 4096] FP16 | F16 weights / FP16 activations |
| 4 | Attention scores (Q×Kᵀ) | Attention scores (Q x K^T) | [B, H, S, D] FP16 | [B, H, D, S] (K^T) FP16 | [B, H, S, S] FP16, FP32 accumulate | — weights / FP16 activations |
| 5 | Attention context (softmax×V) | Attention context (softmax x V) | [B, H, S, S] FP16 | [B, H, S, D] (V) FP16 | [B, H, S, D] FP16 | — weights / FP16 activations |
| 6 | Attention output | Matmul (linear) | [B, S, 4096] FP16 | [4096, 4096] F16 | [B, S, 4096] FP16 | F16 weights / FP16 activations |
| 7 | MLP gate | Matmul (linear) | [B, S, 4096] FP16 | [10240, 4096] F16 | [B, S, 10240] FP16 | F16 weights / FP16 activations |
| 8 | MLP up | Matmul (linear) | [B, S, 4096] FP16 | [10240, 4096] F16 | [B, S, 10240] FP16 | F16 weights / FP16 activations |
| 9 | MLP down | Matmul (linear) | [B, S, 10240] FP16 | [4096, 10240] F16 | [B, S, 4096] FP16 | F16 weights / FP16 activations |
| 10 | Convolution (im2col matmul) | Conv [3, 3, 3] (im2col matmul) | [B, 768, spatial] FP16 | [768, 768, 3, 3, 3] F16 | [B, 768, spatial'] FP16 | F16 weights / FP16 activations |
| 11 | 1×1 conv matmul | Matmul (1x1 conv) | [B, 12, spatial] FP16 | [768, 12, 1, 1, 1] F16 | [B, 768, spatial'] FP16 | F16 weights / FP16 activations |
| 12 | Other linear | Matmul (linear) | [B, S, 15] FP16 | [64, 15] F16 | [B, S, 64] FP16 | F16 weights / FP16 activations |

## Aggregated matrix-multiply roles

For every model and component, each role is listed with the number of matching weight tensors, the most common weight shapes, and the weight/activation dtypes.

| Model | Component | Role | Ops | Blocks | Common B shapes | Weight dtypes | Activation dtypes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [cocktailpeanut/fcanny](https://huggingface.co/cocktailpeanut/fcanny) | double_blocks | Projection / FFN | 114 | 0–18 | `[3072, 3072]` ×38; `[12288, 3072]` ×38; `[3072, 12288]` ×38 | BF16×114 | BF16×114 |
| [cocktailpeanut/fcanny](https://huggingface.co/cocktailpeanut/fcanny) | double_blocks | Other linear | 76 | 0–18 | `[9216, 3072]` ×38; `[18432, 3072]` ×38 | BF16×76 | BF16×76 |
| [cocktailpeanut/fcanny](https://huggingface.co/cocktailpeanut/fcanny) | final_layer | Projection / FFN | 1 | — | `[64, 3072]` ×1 | BF16×1 | BF16×1 |
| [cocktailpeanut/fcanny](https://huggingface.co/cocktailpeanut/fcanny) | guidance_in | Other linear | 2 | — | `[3072, 256]` ×1; `[3072, 3072]` ×1 | BF16×2 | BF16×2 |
| [cocktailpeanut/fcanny](https://huggingface.co/cocktailpeanut/fcanny) | img_in | Other linear | 1 | — | `[3072, 128]` ×1 | BF16×1 | BF16×1 |
| [cocktailpeanut/fcanny](https://huggingface.co/cocktailpeanut/fcanny) | single_blocks | Projection / FFN | 76 | 0–37 | `[21504, 3072]` ×38; `[3072, 15360]` ×38 | BF16×76 | BF16×76 |
| [cocktailpeanut/fcanny](https://huggingface.co/cocktailpeanut/fcanny) | single_blocks | Other linear | 38 | 0–37 | `[9216, 3072]` ×38 | BF16×38 | BF16×38 |
| [cocktailpeanut/fcanny](https://huggingface.co/cocktailpeanut/fcanny) | time_in | Other linear | 2 | — | `[3072, 256]` ×1; `[3072, 3072]` ×1 | BF16×2 | BF16×2 |
| [cocktailpeanut/fcanny](https://huggingface.co/cocktailpeanut/fcanny) | txt_in | Other linear | 1 | — | `[3072, 4096]` ×1 | BF16×1 | BF16×1 |
| [cocktailpeanut/fcanny](https://huggingface.co/cocktailpeanut/fcanny) | vector_in | Other linear | 2 | — | `[3072, 768]` ×1; `[3072, 3072]` ×1 | BF16×2 | BF16×2 |
| [cocktailpeanut/fdepth](https://huggingface.co/cocktailpeanut/fdepth) | double_blocks | Projection / FFN | 114 | 0–18 | `[3072, 3072]` ×38; `[12288, 3072]` ×38; `[3072, 12288]` ×38 | BF16×114 | BF16×114 |
| [cocktailpeanut/fdepth](https://huggingface.co/cocktailpeanut/fdepth) | double_blocks | Other linear | 76 | 0–18 | `[9216, 3072]` ×38; `[18432, 3072]` ×38 | BF16×76 | BF16×76 |
| [cocktailpeanut/fdepth](https://huggingface.co/cocktailpeanut/fdepth) | final_layer | Projection / FFN | 1 | — | `[64, 3072]` ×1 | BF16×1 | BF16×1 |
| [cocktailpeanut/fdepth](https://huggingface.co/cocktailpeanut/fdepth) | guidance_in | Other linear | 2 | — | `[3072, 256]` ×1; `[3072, 3072]` ×1 | BF16×2 | BF16×2 |
| [cocktailpeanut/fdepth](https://huggingface.co/cocktailpeanut/fdepth) | img_in | Other linear | 1 | — | `[3072, 128]` ×1 | BF16×1 | BF16×1 |
| [cocktailpeanut/fdepth](https://huggingface.co/cocktailpeanut/fdepth) | single_blocks | Projection / FFN | 76 | 0–37 | `[21504, 3072]` ×38; `[3072, 15360]` ×38 | BF16×76 | BF16×76 |
| [cocktailpeanut/fdepth](https://huggingface.co/cocktailpeanut/fdepth) | single_blocks | Other linear | 38 | 0–37 | `[9216, 3072]` ×38 | BF16×38 | BF16×38 |
| [cocktailpeanut/fdepth](https://huggingface.co/cocktailpeanut/fdepth) | time_in | Other linear | 2 | — | `[3072, 256]` ×1; `[3072, 3072]` ×1 | BF16×2 | BF16×2 |
| [cocktailpeanut/fdepth](https://huggingface.co/cocktailpeanut/fdepth) | txt_in | Other linear | 1 | — | `[3072, 4096]` ×1 | BF16×1 | BF16×1 |
| [cocktailpeanut/fdepth](https://huggingface.co/cocktailpeanut/fdepth) | vector_in | Other linear | 2 | — | `[3072, 768]` ×1; `[3072, 3072]` ×1 | BF16×2 | BF16×2 |
| [cocktailpeanut/fill](https://huggingface.co/cocktailpeanut/fill) | double_blocks | Projection / FFN | 114 | 0–18 | `[3072, 3072]` ×38; `[12288, 3072]` ×38; `[3072, 12288]` ×38 | BF16×114 | BF16×114 |
| [cocktailpeanut/fill](https://huggingface.co/cocktailpeanut/fill) | double_blocks | Other linear | 76 | 0–18 | `[9216, 3072]` ×38; `[18432, 3072]` ×38 | BF16×76 | BF16×76 |
| [cocktailpeanut/fill](https://huggingface.co/cocktailpeanut/fill) | final_layer | Projection / FFN | 1 | — | `[64, 3072]` ×1 | BF16×1 | BF16×1 |
| [cocktailpeanut/fill](https://huggingface.co/cocktailpeanut/fill) | guidance_in | Other linear | 2 | — | `[3072, 256]` ×1; `[3072, 3072]` ×1 | BF16×2 | BF16×2 |
| [cocktailpeanut/fill](https://huggingface.co/cocktailpeanut/fill) | img_in | Other linear | 1 | — | `[3072, 384]` ×1 | BF16×1 | BF16×1 |
| [cocktailpeanut/fill](https://huggingface.co/cocktailpeanut/fill) | single_blocks | Projection / FFN | 76 | 0–37 | `[21504, 3072]` ×38; `[3072, 15360]` ×38 | BF16×76 | BF16×76 |
| [cocktailpeanut/fill](https://huggingface.co/cocktailpeanut/fill) | single_blocks | Other linear | 38 | 0–37 | `[9216, 3072]` ×38 | BF16×38 | BF16×38 |
| [cocktailpeanut/fill](https://huggingface.co/cocktailpeanut/fill) | time_in | Other linear | 2 | — | `[3072, 256]` ×1; `[3072, 3072]` ×1 | BF16×2 | BF16×2 |
| [cocktailpeanut/fill](https://huggingface.co/cocktailpeanut/fill) | txt_in | Other linear | 1 | — | `[3072, 4096]` ×1 | BF16×1 | BF16×1 |
| [cocktailpeanut/fill](https://huggingface.co/cocktailpeanut/fill) | vector_in | Other linear | 2 | — | `[3072, 768]` ×1; `[3072, 3072]` ×1 | BF16×2 | BF16×2 |
| [cocktailpeanut/redux](https://huggingface.co/cocktailpeanut/redux) | redux_down | Other linear | 1 | — | `[4096, 12288]` ×1 | BF16×1 | BF16×1 |
| [cocktailpeanut/redux](https://huggingface.co/cocktailpeanut/redux) | redux_up | Other linear | 1 | — | `[12288, 1152]` ×1 | BF16×1 | BF16×1 |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | conditioner | Attention output | 32 | 0–31 | `[1280, 1280]` ×32 | F16×32 | FP16×32 |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | conditioner | Projection / FFN | 64 | 0–31 | `[5120, 1280]` ×32; `[1280, 5120]` ×32 | F16×64 | FP16×64 |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | conditioner | Convolution (im2col matmul) | 59 | 0–3 | `[512, 512, 3, 3]` ×30; `[128, 128, 3, 3]` ×10; `[256, 256, 3, 3]` ×10 | F16×59 | FP16×59 |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | conditioner | 1×1 conv matmul | 14 | 0–3 | `[512, 512, 1, 1]` ×8; `[128, 256, 1, 1]` ×1; `[256, 512, 1, 1]` ×1 | F16×14 | FP16×14 |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | transformer | Embedding projection | 2 | 0–2 | `[1280, 320]` ×1; `[1280, 1280]` ×1 | F16×2 | FP16×2 |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | transformer | Q projection | 64 | 1–11 | `[1280, 1280]` ×24; `[320, 320]` ×20; `[640, 640]` ×20 | F16×64 | FP16×64 |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | transformer | K projection | 64 | 1–11 | `[1280, 1280]` ×12; `[1280, 1024]` ×12; `[320, 320]` ×10 | F16×64 | FP16×64 |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | transformer | V projection | 64 | 1–11 | `[1280, 1280]` ×12; `[1280, 1024]` ×12; `[320, 320]` ×10 | F16×64 | FP16×64 |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | transformer | Attention scores (Q×Kᵀ) | 1 | 1 | `[B, H, D, S] (K^T)` ×1 | —×1 | FP16×1 |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | transformer | Attention context (softmax×V) | 1 | 1 | `[B, H, S, D] (V)` ×1 | —×1 | FP16×1 |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | transformer | Attention output | 80 | 1–11 | `[1280, 1280]` ×30; `[320, 320]` ×25; `[640, 640]` ×25 | F16×80 | FP16×80 |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | transformer | Projection / FFN | 64 | 1–11 | `[10240, 1280]` ×18; `[2560, 320]` ×15; `[5120, 640]` ×15 | F16×64 | FP16×64 |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | transformer | Convolution (im2col matmul) | 183 | 0–11 | `[512, 512, 3, 3]` ×30; `[1280, 1280, 3, 1, 1]` ×24; `[1280, 1280, 3, 3]` ×20 | F16×183 | FP16×183 |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | transformer | 1×1 conv matmul | 26 | 0–11 | `[512, 512, 1, 1]` ×8; `[1280, 2560, 1, 1]` ×5; `[320, 640, 1, 1]` ×2 | F16×26 | FP16×26 |
| [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv) | transformer | Other linear | 94 | 0–11 | `[1280, 1280]` ×25; `[320, 1280]` ×25; `[1280, 5120]` ×18 | F16×94 | FP16×94 |
| [cocktailpeanut/xulf-dev](https://huggingface.co/cocktailpeanut/xulf-dev) | double_blocks | Projection / FFN | 114 | 0–18 | `[3072, 3072]` ×38; `[12288, 3072]` ×38; `[3072, 12288]` ×38 | BF16×114 | BF16×114 |
| [cocktailpeanut/xulf-dev](https://huggingface.co/cocktailpeanut/xulf-dev) | double_blocks | Other linear | 76 | 0–18 | `[9216, 3072]` ×38; `[18432, 3072]` ×38 | BF16×76 | BF16×76 |
| [cocktailpeanut/xulf-dev](https://huggingface.co/cocktailpeanut/xulf-dev) | final_layer | Projection / FFN | 1 | — | `[64, 3072]` ×1 | BF16×1 | BF16×1 |
| [cocktailpeanut/xulf-dev](https://huggingface.co/cocktailpeanut/xulf-dev) | guidance_in | Other linear | 2 | — | `[3072, 256]` ×1; `[3072, 3072]` ×1 | BF16×2 | BF16×2 |
| [cocktailpeanut/xulf-dev](https://huggingface.co/cocktailpeanut/xulf-dev) | img_in | Other linear | 1 | — | `[3072, 64]` ×1 | BF16×1 | BF16×1 |
| [cocktailpeanut/xulf-dev](https://huggingface.co/cocktailpeanut/xulf-dev) | single_blocks | Projection / FFN | 76 | 0–37 | `[21504, 3072]` ×38; `[3072, 15360]` ×38 | BF16×76 | BF16×76 |
| [cocktailpeanut/xulf-dev](https://huggingface.co/cocktailpeanut/xulf-dev) | single_blocks | Other linear | 38 | 0–37 | `[9216, 3072]` ×38 | BF16×38 | BF16×38 |
| [cocktailpeanut/xulf-dev](https://huggingface.co/cocktailpeanut/xulf-dev) | time_in | Other linear | 2 | — | `[3072, 256]` ×1; `[3072, 3072]` ×1 | BF16×2 | BF16×2 |
| [cocktailpeanut/xulf-dev](https://huggingface.co/cocktailpeanut/xulf-dev) | txt_in | Other linear | 1 | — | `[3072, 4096]` ×1 | BF16×1 | BF16×1 |
| [cocktailpeanut/xulf-dev](https://huggingface.co/cocktailpeanut/xulf-dev) | vae | Convolution (im2col matmul) | 58 | 0–3 | `[512, 512, 3, 3]` ×30; `[128, 128, 3, 3]` ×10; `[256, 256, 3, 3]` ×10 | F32×58 | FP32×58 |
| [cocktailpeanut/xulf-dev](https://huggingface.co/cocktailpeanut/xulf-dev) | vae | 1×1 conv matmul | 12 | 0 | `[512, 512, 1, 1]` ×8; `[128, 256, 1, 1]` ×1; `[256, 512, 1, 1]` ×1 | F32×12 | FP32×12 |
| [cocktailpeanut/xulf-dev](https://huggingface.co/cocktailpeanut/xulf-dev) | vector_in | Other linear | 2 | — | `[3072, 768]` ×1; `[3072, 3072]` ×1 | BF16×2 | BF16×2 |
| [cocktailpeanut/xulf-schnell](https://huggingface.co/cocktailpeanut/xulf-schnell) | double_blocks | Projection / FFN | 114 | 0–18 | `[3072, 3072]` ×38; `[12288, 3072]` ×38; `[3072, 12288]` ×38 | BF16×114 | BF16×114 |
| [cocktailpeanut/xulf-schnell](https://huggingface.co/cocktailpeanut/xulf-schnell) | double_blocks | Other linear | 76 | 0–18 | `[9216, 3072]` ×38; `[18432, 3072]` ×38 | BF16×76 | BF16×76 |
| [cocktailpeanut/xulf-schnell](https://huggingface.co/cocktailpeanut/xulf-schnell) | final_layer | Projection / FFN | 1 | — | `[64, 3072]` ×1 | BF16×1 | BF16×1 |
| [cocktailpeanut/xulf-schnell](https://huggingface.co/cocktailpeanut/xulf-schnell) | img_in | Other linear | 1 | — | `[3072, 64]` ×1 | BF16×1 | BF16×1 |
| [cocktailpeanut/xulf-schnell](https://huggingface.co/cocktailpeanut/xulf-schnell) | single_blocks | Projection / FFN | 76 | 0–37 | `[21504, 3072]` ×38; `[3072, 15360]` ×38 | BF16×76 | BF16×76 |
| [cocktailpeanut/xulf-schnell](https://huggingface.co/cocktailpeanut/xulf-schnell) | single_blocks | Other linear | 38 | 0–37 | `[9216, 3072]` ×38 | BF16×38 | BF16×38 |
| [cocktailpeanut/xulf-schnell](https://huggingface.co/cocktailpeanut/xulf-schnell) | time_in | Other linear | 2 | — | `[3072, 256]` ×1; `[3072, 3072]` ×1 | BF16×2 | BF16×2 |
| [cocktailpeanut/xulf-schnell](https://huggingface.co/cocktailpeanut/xulf-schnell) | txt_in | Other linear | 1 | — | `[3072, 4096]` ×1 | BF16×1 | BF16×1 |
| [cocktailpeanut/xulf-schnell](https://huggingface.co/cocktailpeanut/xulf-schnell) | vae | Convolution (im2col matmul) | 58 | 0–3 | `[512, 512, 3, 3]` ×30; `[128, 128, 3, 3]` ×10; `[256, 256, 3, 3]` ×10 | F32×58 | FP32×58 |
| [cocktailpeanut/xulf-schnell](https://huggingface.co/cocktailpeanut/xulf-schnell) | vae | 1×1 conv matmul | 12 | 0 | `[512, 512, 1, 1]` ×8; `[128, 256, 1, 1]` ×1; `[256, 512, 1, 1]` ×1 | F32×12 | FP32×12 |
| [cocktailpeanut/xulf-schnell](https://huggingface.co/cocktailpeanut/xulf-schnell) | vector_in | Other linear | 2 | — | `[3072, 768]` ×1; `[3072, 3072]` ×1 | BF16×2 | BF16×2 |
| [Comfy-Org/flux1-dev](https://huggingface.co/Comfy-Org/flux1-dev) | conditioner | Q projection | 36 | 0–23 | `[4096, 4096]` ×24; `[768, 768]` ×12 | F8_E4M3×24, F16×12 | BF16 (FP8 weights)×24, FP16×12 |
| [Comfy-Org/flux1-dev](https://huggingface.co/Comfy-Org/flux1-dev) | conditioner | K projection | 36 | 0–23 | `[4096, 4096]` ×24; `[768, 768]` ×12 | F8_E4M3×24, F16×12 | BF16 (FP8 weights)×24, FP16×12 |
| [Comfy-Org/flux1-dev](https://huggingface.co/Comfy-Org/flux1-dev) | conditioner | V projection | 36 | 0–23 | `[4096, 4096]` ×24; `[768, 768]` ×12 | F8_E4M3×24, F16×12 | BF16 (FP8 weights)×24, FP16×12 |
| [Comfy-Org/flux1-dev](https://huggingface.co/Comfy-Org/flux1-dev) | conditioner | Attention scores (Q×Kᵀ) | 1 | 0 | `[B, H, D, S] (K^T)` ×1 | —×1 | FP16×1 |
| [Comfy-Org/flux1-dev](https://huggingface.co/Comfy-Org/flux1-dev) | conditioner | Attention context (softmax×V) | 1 | 0 | `[B, H, S, D] (V)` ×1 | —×1 | FP16×1 |
| [Comfy-Org/flux1-dev](https://huggingface.co/Comfy-Org/flux1-dev) | conditioner | Attention output | 36 | 0–23 | `[4096, 4096]` ×24; `[768, 768]` ×12 | F8_E4M3×24, F16×12 | BF16 (FP8 weights)×24, FP16×12 |
| [Comfy-Org/flux1-dev](https://huggingface.co/Comfy-Org/flux1-dev) | conditioner | MLP gate | 24 | 0–23 | `[10240, 4096]` ×24 | F8_E4M3×24 | BF16 (FP8 weights)×24 |
| [Comfy-Org/flux1-dev](https://huggingface.co/Comfy-Org/flux1-dev) | conditioner | MLP up | 36 | 0–23 | `[10240, 4096]` ×24; `[3072, 768]` ×12 | F8_E4M3×24, F16×12 | BF16 (FP8 weights)×24, FP16×12 |
| [Comfy-Org/flux1-dev](https://huggingface.co/Comfy-Org/flux1-dev) | conditioner | MLP down | 36 | 0–23 | `[4096, 10240]` ×24; `[768, 3072]` ×12 | F8_E4M3×24, F16×12 | BF16 (FP8 weights)×24, FP16×12 |
| [Comfy-Org/flux1-dev](https://huggingface.co/Comfy-Org/flux1-dev) | conditioner | Projection / FFN | 1 | — | `[768, 768]` ×1 | F16×1 | FP16×1 |
| [Comfy-Org/flux1-dev](https://huggingface.co/Comfy-Org/flux1-dev) | transformer | Projection / FFN | 191 | 0–37 | `[3072, 3072]` ×38; `[12288, 3072]` ×38; `[3072, 12288]` ×38 | F8_E4M3×191 | BF16 (FP8 weights)×191 |
| [Comfy-Org/flux1-dev](https://huggingface.co/Comfy-Org/flux1-dev) | transformer | Other linear | 122 | 0–37 | `[9216, 3072]` ×76; `[18432, 3072]` ×38; `[3072, 3072]` ×3 | F8_E4M3×122 | BF16 (FP8 weights)×122 |
| [Comfy-Org/flux1-dev](https://huggingface.co/Comfy-Org/flux1-dev) | vae | Convolution (im2col matmul) | 58 | 0–3 | `[512, 512, 3, 3]` ×30; `[128, 128, 3, 3]` ×10; `[256, 256, 3, 3]` ×10 | F32×58 | FP32×58 |
| [Comfy-Org/flux1-dev](https://huggingface.co/Comfy-Org/flux1-dev) | vae | 1×1 conv matmul | 12 | 0 | `[512, 512, 1, 1]` ×8; `[128, 256, 1, 1]` ×1; `[256, 512, 1, 1]` ×1 | F32×12 | FP32×12 |
| [Comfy-Org/flux1-schnell](https://huggingface.co/Comfy-Org/flux1-schnell) | conditioner | Q projection | 36 | 0–23 | `[4096, 4096]` ×24; `[768, 768]` ×12 | F8_E4M3×24, F16×12 | BF16 (FP8 weights)×24, FP16×12 |
| [Comfy-Org/flux1-schnell](https://huggingface.co/Comfy-Org/flux1-schnell) | conditioner | K projection | 36 | 0–23 | `[4096, 4096]` ×24; `[768, 768]` ×12 | F8_E4M3×24, F16×12 | BF16 (FP8 weights)×24, FP16×12 |
| [Comfy-Org/flux1-schnell](https://huggingface.co/Comfy-Org/flux1-schnell) | conditioner | V projection | 36 | 0–23 | `[4096, 4096]` ×24; `[768, 768]` ×12 | F8_E4M3×24, F16×12 | BF16 (FP8 weights)×24, FP16×12 |
| [Comfy-Org/flux1-schnell](https://huggingface.co/Comfy-Org/flux1-schnell) | conditioner | Attention scores (Q×Kᵀ) | 1 | 0 | `[B, H, D, S] (K^T)` ×1 | —×1 | FP16×1 |
| [Comfy-Org/flux1-schnell](https://huggingface.co/Comfy-Org/flux1-schnell) | conditioner | Attention context (softmax×V) | 1 | 0 | `[B, H, S, D] (V)` ×1 | —×1 | FP16×1 |
| [Comfy-Org/flux1-schnell](https://huggingface.co/Comfy-Org/flux1-schnell) | conditioner | Attention output | 36 | 0–23 | `[4096, 4096]` ×24; `[768, 768]` ×12 | F8_E4M3×24, F16×12 | BF16 (FP8 weights)×24, FP16×12 |
| [Comfy-Org/flux1-schnell](https://huggingface.co/Comfy-Org/flux1-schnell) | conditioner | MLP gate | 24 | 0–23 | `[10240, 4096]` ×24 | F8_E4M3×24 | BF16 (FP8 weights)×24 |
| [Comfy-Org/flux1-schnell](https://huggingface.co/Comfy-Org/flux1-schnell) | conditioner | MLP up | 36 | 0–23 | `[10240, 4096]` ×24; `[3072, 768]` ×12 | F8_E4M3×24, F16×12 | BF16 (FP8 weights)×24, FP16×12 |
| [Comfy-Org/flux1-schnell](https://huggingface.co/Comfy-Org/flux1-schnell) | conditioner | MLP down | 36 | 0–23 | `[4096, 10240]` ×24; `[768, 3072]` ×12 | F8_E4M3×24, F16×12 | BF16 (FP8 weights)×24, FP16×12 |
| [Comfy-Org/flux1-schnell](https://huggingface.co/Comfy-Org/flux1-schnell) | conditioner | Projection / FFN | 1 | — | `[768, 768]` ×1 | F16×1 | FP16×1 |
| [Comfy-Org/flux1-schnell](https://huggingface.co/Comfy-Org/flux1-schnell) | transformer | Projection / FFN | 191 | 0–37 | `[3072, 3072]` ×38; `[12288, 3072]` ×38; `[3072, 12288]` ×38 | F8_E4M3×191 | BF16 (FP8 weights)×191 |
| [Comfy-Org/flux1-schnell](https://huggingface.co/Comfy-Org/flux1-schnell) | transformer | Other linear | 120 | 0–37 | `[9216, 3072]` ×76; `[18432, 3072]` ×38; `[3072, 3072]` ×2 | F8_E4M3×120 | BF16 (FP8 weights)×120 |
| [Comfy-Org/flux1-schnell](https://huggingface.co/Comfy-Org/flux1-schnell) | vae | Convolution (im2col matmul) | 58 | 0–3 | `[512, 512, 3, 3]` ×30; `[128, 128, 3, 3]` ×10; `[256, 256, 3, 3]` ×10 | F32×58 | FP32×58 |
| [Comfy-Org/flux1-schnell](https://huggingface.co/Comfy-Org/flux1-schnell) | vae | 1×1 conv matmul | 12 | 0 | `[512, 512, 1, 1]` ×8; `[128, 256, 1, 1]` ×1; `[256, 512, 1, 1]` ×1 | F32×12 | FP32×12 |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | conditioner | Q projection | 26 | 0–23 | `[4096, 4096]` ×26 | F8_E4M3×25, BF16×1 | BF16 (FP8 weights)×25, BF16×1 |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | conditioner | K projection | 26 | 0–23 | `[4096, 4096]` ×24; `[8192, 4096]` ×2 | F8_E4M3×25, BF16×1 | BF16 (FP8 weights)×25, BF16×1 |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | conditioner | V projection | 24 | 0–23 | `[4096, 4096]` ×24 | F8_E4M3×24 | BF16 (FP8 weights)×24 |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | conditioner | Attention scores (Q×Kᵀ) | 2 | — | `[B, H, D, S] (K^T)` ×2 | —×2 | BF16×1, BF16 (FP8 weights)×1 |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | conditioner | Attention context (softmax×V) | 2 | — | `[B, H, S, D] (V)` ×2 | —×2 | BF16×1, BF16 (FP8 weights)×1 |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | conditioner | Attention output | 26 | 0–23 | `[4096, 4096]` ×24; `[3072, 4096]` ×2 | F8_E4M3×25, BF16×1 | BF16 (FP8 weights)×25, BF16×1 |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | conditioner | MLP gate | 24 | 0–23 | `[10240, 4096]` ×24 | F8_E4M3×24 | BF16 (FP8 weights)×24 |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | conditioner | MLP up | 24 | 0–23 | `[10240, 4096]` ×24 | F8_E4M3×24 | BF16 (FP8 weights)×24 |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | conditioner | MLP down | 24 | 0–23 | `[4096, 10240]` ×24 | F8_E4M3×24 | BF16 (FP8 weights)×24 |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | conditioner | Projection / FFN | 2 | — | `[1536, 4096]` ×2 | BF16×1, F8_E4M3×1 | BF16×1, BF16 (FP8 weights)×1 |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | transformer | MLP gate | 190 | 0–47 | `[16384, 3072]` ×96; `[8192, 1536]` ×94 | BF16×95, F8_E4M3×95 | BF16×95, BF16 (FP8 weights)×95 |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | transformer | Projection / FFN | 386 | 0–47 | `[3072, 3072]` ×98; `[3072, 8192]` ×96; `[1536, 3072]` ×94 | BF16×193, F8_E4M3×193 | BF16×193, BF16 (FP8 weights)×193 |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | transformer | Output head | 2 | — | `[6144, 3072]` ×2 | BF16×1, F8_E4M3×1 | BF16×1, BF16 (FP8 weights)×1 |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | transformer | Convolution (im2col matmul) | 2 | — | `[3072, 12, 2, 2]` ×2 | BF16×2 | BF16×2 |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | transformer | Other linear | 384 | 0–47 | `[9216, 3072]` ×96; `[9216, 1536]` ×96; `[12288, 3072]` ×96 | BF16×192, F8_E4M3×192 | BF16×192, BF16 (FP8 weights)×192 |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | vae | Q projection | 24 | 0–23 | `[4096, 4096]` ×24 | F16×24 | FP16×24 |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | vae | K projection | 24 | 0–23 | `[4096, 4096]` ×24 | F16×24 | FP16×24 |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | vae | V projection | 24 | 0–23 | `[4096, 4096]` ×24 | F16×24 | FP16×24 |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | vae | Attention scores (Q×Kᵀ) | 1 | 0 | `[B, H, D, S] (K^T)` ×1 | —×1 | FP16×1 |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | vae | Attention context (softmax×V) | 1 | 0 | `[B, H, S, D] (V)` ×1 | —×1 | FP16×1 |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | vae | Attention output | 24 | 0–23 | `[4096, 4096]` ×24 | F16×24 | FP16×24 |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | vae | MLP gate | 24 | 0–23 | `[10240, 4096]` ×24 | F16×24 | FP16×24 |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | vae | MLP up | 24 | 0–23 | `[10240, 4096]` ×24 | F16×24 | FP16×24 |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | vae | MLP down | 24 | 0–23 | `[4096, 10240]` ×24 | F16×24 | FP16×24 |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | vae | Projection / FFN | 10 | 1–3 | `[3, 128]` ×2; `[24, 384]` ×2; `[6144, 768]` ×2 | F16×10 | FP16×10 |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | vae | Convolution (im2col matmul) | 158 | 0–9 | `[768, 768, 3, 3, 3]` ×36; `[384, 384, 3, 3, 3]` ×36; `[256, 256, 3, 3, 3]` ×28 | F16×158 | FP16×158 |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | vae | 1×1 conv matmul | 2 | 0 | `[768, 12, 1, 1, 1]` ×2 | F16×2 | FP16×2 |
| [Comfy-Org/mochi_preview_repackaged](https://huggingface.co/Comfy-Org/mochi_preview_repackaged) | vae | Other linear | 66 | 0–9 | `[384, 384]` ×18; `[1152, 384]` ×18; `[256, 256]` ×8 | F16×66 | FP16×66 |
| [Comfy-Org/sigclip_vision_384](https://huggingface.co/Comfy-Org/sigclip_vision_384) | transformer | Q projection | 27 | 0–26 | `[1152, 1152]` ×27 | F16×27 | FP16×27 |
| [Comfy-Org/sigclip_vision_384](https://huggingface.co/Comfy-Org/sigclip_vision_384) | transformer | K projection | 27 | 0–26 | `[1152, 1152]` ×27 | F16×27 | FP16×27 |
| [Comfy-Org/sigclip_vision_384](https://huggingface.co/Comfy-Org/sigclip_vision_384) | transformer | V projection | 27 | 0–26 | `[1152, 1152]` ×27 | F16×27 | FP16×27 |
| [Comfy-Org/sigclip_vision_384](https://huggingface.co/Comfy-Org/sigclip_vision_384) | transformer | Attention scores (Q×Kᵀ) | 1 | 0 | `[B, H, D, S] (K^T)` ×1 | —×1 | FP16×1 |
| [Comfy-Org/sigclip_vision_384](https://huggingface.co/Comfy-Org/sigclip_vision_384) | transformer | Attention context (softmax×V) | 1 | 0 | `[B, H, S, D] (V)` ×1 | —×1 | FP16×1 |
| [Comfy-Org/sigclip_vision_384](https://huggingface.co/Comfy-Org/sigclip_vision_384) | transformer | Attention output | 28 | 0–26 | `[1152, 1152]` ×28 | F16×28 | FP16×28 |
| [Comfy-Org/sigclip_vision_384](https://huggingface.co/Comfy-Org/sigclip_vision_384) | transformer | MLP up | 28 | 0–26 | `[4304, 1152]` ×28 | F16×28 | FP16×28 |
| [Comfy-Org/sigclip_vision_384](https://huggingface.co/Comfy-Org/sigclip_vision_384) | transformer | MLP down | 28 | 0–26 | `[1152, 4304]` ×28 | F16×28 | FP16×28 |
| [Comfy-Org/sigclip_vision_384](https://huggingface.co/Comfy-Org/sigclip_vision_384) | transformer | Convolution (im2col matmul) | 1 | — | `[1152, 3, 14, 14]` ×1 | F16×1 | FP16×1 |
| [Comfy-Org/stable-diffusion-3.5-fp8](https://huggingface.co/Comfy-Org/stable-diffusion-3.5-fp8) | conditioner | Q projection | 12 | 0–11 | `[768, 768]` ×12 | F16×12 | FP16×12 |
| [Comfy-Org/stable-diffusion-3.5-fp8](https://huggingface.co/Comfy-Org/stable-diffusion-3.5-fp8) | conditioner | K projection | 12 | 0–11 | `[768, 768]` ×12 | F16×12 | FP16×12 |
| [Comfy-Org/stable-diffusion-3.5-fp8](https://huggingface.co/Comfy-Org/stable-diffusion-3.5-fp8) | conditioner | V projection | 12 | 0–11 | `[768, 768]` ×12 | F16×12 | FP16×12 |
| [Comfy-Org/stable-diffusion-3.5-fp8](https://huggingface.co/Comfy-Org/stable-diffusion-3.5-fp8) | conditioner | Attention scores (Q×Kᵀ) | 1 | 0 | `[B, H, D, S] (K^T)` ×1 | —×1 | FP16×1 |
| [Comfy-Org/stable-diffusion-3.5-fp8](https://huggingface.co/Comfy-Org/stable-diffusion-3.5-fp8) | conditioner | Attention context (softmax×V) | 1 | 0 | `[B, H, S, D] (V)` ×1 | —×1 | FP16×1 |
| [Comfy-Org/stable-diffusion-3.5-fp8](https://huggingface.co/Comfy-Org/stable-diffusion-3.5-fp8) | conditioner | Attention output | 12 | 0–11 | `[768, 768]` ×12 | F16×12 | FP16×12 |
| [Comfy-Org/stable-diffusion-3.5-fp8](https://huggingface.co/Comfy-Org/stable-diffusion-3.5-fp8) | conditioner | MLP up | 12 | 0–11 | `[3072, 768]` ×12 | F16×12 | FP16×12 |
| [Comfy-Org/stable-diffusion-3.5-fp8](https://huggingface.co/Comfy-Org/stable-diffusion-3.5-fp8) | conditioner | MLP down | 12 | 0–11 | `[768, 3072]` ×12 | F16×12 | FP16×12 |
| [Comfy-Org/stable-diffusion-3.5-fp8](https://huggingface.co/Comfy-Org/stable-diffusion-3.5-fp8) | vae | Q projection | 24 | 0–23 | `[4096, 4096]` ×24 | F16×24 | FP16×24 |
| [Comfy-Org/stable-diffusion-3.5-fp8](https://huggingface.co/Comfy-Org/stable-diffusion-3.5-fp8) | vae | K projection | 24 | 0–23 | `[4096, 4096]` ×24 | F16×24 | FP16×24 |
| [Comfy-Org/stable-diffusion-3.5-fp8](https://huggingface.co/Comfy-Org/stable-diffusion-3.5-fp8) | vae | V projection | 24 | 0–23 | `[4096, 4096]` ×24 | F16×24 | FP16×24 |
| [Comfy-Org/stable-diffusion-3.5-fp8](https://huggingface.co/Comfy-Org/stable-diffusion-3.5-fp8) | vae | Attention scores (Q×Kᵀ) | 1 | 0 | `[B, H, D, S] (K^T)` ×1 | —×1 | FP16×1 |
| [Comfy-Org/stable-diffusion-3.5-fp8](https://huggingface.co/Comfy-Org/stable-diffusion-3.5-fp8) | vae | Attention context (softmax×V) | 1 | 0 | `[B, H, S, D] (V)` ×1 | —×1 | FP16×1 |
| [Comfy-Org/stable-diffusion-3.5-fp8](https://huggingface.co/Comfy-Org/stable-diffusion-3.5-fp8) | vae | Attention output | 24 | 0–23 | `[4096, 4096]` ×24 | F16×24 | FP16×24 |
| [Comfy-Org/stable-diffusion-3.5-fp8](https://huggingface.co/Comfy-Org/stable-diffusion-3.5-fp8) | vae | MLP gate | 24 | 0–23 | `[10240, 4096]` ×24 | F16×24 | FP16×24 |
| [Comfy-Org/stable-diffusion-3.5-fp8](https://huggingface.co/Comfy-Org/stable-diffusion-3.5-fp8) | vae | MLP up | 24 | 0–23 | `[10240, 4096]` ×24 | F16×24 | FP16×24 |
| [Comfy-Org/stable-diffusion-3.5-fp8](https://huggingface.co/Comfy-Org/stable-diffusion-3.5-fp8) | vae | MLP down | 24 | 0–23 | `[4096, 10240]` ×24 | F16×24 | FP16×24 |
| [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged) | blocks | Q projection | 160 | 0–39 | `[5120, 5120]` ×160 | BF16×160 | BF16×160 |
| [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged) | blocks | K projection | 160 | 0–39 | `[5120, 5120]` ×160 | BF16×160 | BF16×160 |
| [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged) | blocks | V projection | 160 | 0–39 | `[5120, 5120]` ×160 | BF16×160 | BF16×160 |
| [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged) | blocks | Attention scores (Q×Kᵀ) | 2 | 0 | `[B, H, D, S] (K^T)` ×2 | —×2 | BF16×2 |
| [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged) | blocks | Attention context (softmax×V) | 2 | 0 | `[B, H, S, D] (V)` ×2 | —×2 | BF16×2 |
| [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged) | blocks | Attention output | 160 | 0–39 | `[5120, 5120]` ×160 | BF16×160 | BF16×160 |
| [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged) | blocks | Projection / FFN | 160 | 0–39 | `[13824, 5120]` ×80; `[5120, 13824]` ×80 | BF16×160 | BF16×160 |
| [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged) | blocks | Other linear | 160 | 0–39 | `[5120, 5120]` ×160 | BF16×160 | BF16×160 |
| [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged) | head | Output head | 2 | — | `[64, 5120]` ×2 | BF16×2 | BF16×2 |
| [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged) | img_emb | Projection / FFN | 4 | 1–3 | `[1280, 1280]` ×2; `[5120, 1280]` ×2 | BF16×4 | BF16×4 |
| [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged) | patch_embedding | Convolution (im2col matmul) | 2 | — | `[5120, 36, 1, 2, 2]` ×2 | BF16×2 | BF16×2 |
| [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged) | text_embedding | Embedding projection | 4 | 0–2 | `[5120, 4096]` ×2; `[5120, 5120]` ×2 | BF16×4 | BF16×4 |
| [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged) | time_embedding | Embedding projection | 4 | 0–2 | `[5120, 256]` ×2; `[5120, 5120]` ×2 | BF16×4 | BF16×4 |
| [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged) | time_projection | Projection / FFN | 2 | 1 | `[30720, 5120]` ×2 | BF16×2 | BF16×2 |
| [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged) | transformer | Q projection | 32 | 0–31 | `[1280, 1280]` ×32 | F16×32 | FP16×32 |
| [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged) | transformer | K projection | 32 | 0–31 | `[1280, 1280]` ×32 | F16×32 | FP16×32 |
| [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged) | transformer | V projection | 32 | 0–31 | `[1280, 1280]` ×32 | F16×32 | FP16×32 |
| [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged) | transformer | Attention scores (Q×Kᵀ) | 1 | 0 | `[B, H, D, S] (K^T)` ×1 | —×1 | FP16×1 |
| [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged) | transformer | Attention context (softmax×V) | 1 | 0 | `[B, H, S, D] (V)` ×1 | —×1 | FP16×1 |
| [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged) | transformer | Attention output | 32 | 0–31 | `[1280, 1280]` ×32 | F16×32 | FP16×32 |
| [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged) | transformer | MLP up | 32 | 0–31 | `[5120, 1280]` ×32 | F16×32 | FP16×32 |
| [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged) | transformer | MLP down | 32 | 0–31 | `[1280, 5120]` ×32 | F16×32 | FP16×32 |
| [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged) | transformer | Convolution (im2col matmul) | 1 | — | `[1280, 3, 14, 14]` ×1 | F16×1 | FP16×1 |
| [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged) | vae | Q projection | 24 | 0–23 | `[4096, 4096]` ×24 | F8_E4M3×24 | BF16 (FP8 weights)×24 |
| [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged) | vae | K projection | 24 | 0–23 | `[4096, 4096]` ×24 | F8_E4M3×24 | BF16 (FP8 weights)×24 |
| [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged) | vae | V projection | 24 | 0–23 | `[4096, 4096]` ×24 | F8_E4M3×24 | BF16 (FP8 weights)×24 |
| [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged) | vae | Attention scores (Q×Kᵀ) | 1 | 0 | `[B, H, D, S] (K^T)` ×1 | —×1 | BF16 (FP8 weights)×1 |
| [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged) | vae | Attention context (softmax×V) | 1 | 0 | `[B, H, S, D] (V)` ×1 | —×1 | BF16 (FP8 weights)×1 |
| [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged) | vae | Attention output | 24 | 0–23 | `[4096, 4096]` ×24 | F8_E4M3×24 | BF16 (FP8 weights)×24 |
| [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged) | vae | MLP gate | 24 | 0–23 | `[10240, 4096]` ×24 | F8_E4M3×24 | BF16 (FP8 weights)×24 |
| [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged) | vae | MLP up | 24 | 0–23 | `[10240, 4096]` ×24 | F8_E4M3×24 | BF16 (FP8 weights)×24 |
| [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged) | vae | MLP down | 24 | 0–23 | `[4096, 10240]` ×24 | F8_E4M3×24 | BF16 (FP8 weights)×24 |
| [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged) | visual_projection | Projection / FFN | 1 | — | `[1024, 1280]` ×1 | F16×1 | FP16×1 |
| [comfyanonymous/flux_text_encoders](https://huggingface.co/comfyanonymous/flux_text_encoders) | conditioner | Q projection | 12 | 0–11 | `[768, 768]` ×12 | F16×12 | FP16×12 |
| [comfyanonymous/flux_text_encoders](https://huggingface.co/comfyanonymous/flux_text_encoders) | conditioner | K projection | 12 | 0–11 | `[768, 768]` ×12 | F16×12 | FP16×12 |
| [comfyanonymous/flux_text_encoders](https://huggingface.co/comfyanonymous/flux_text_encoders) | conditioner | V projection | 12 | 0–11 | `[768, 768]` ×12 | F16×12 | FP16×12 |
| [comfyanonymous/flux_text_encoders](https://huggingface.co/comfyanonymous/flux_text_encoders) | conditioner | Attention scores (Q×Kᵀ) | 1 | 0 | `[B, H, D, S] (K^T)` ×1 | —×1 | FP16×1 |
| [comfyanonymous/flux_text_encoders](https://huggingface.co/comfyanonymous/flux_text_encoders) | conditioner | Attention context (softmax×V) | 1 | 0 | `[B, H, S, D] (V)` ×1 | —×1 | FP16×1 |
| [comfyanonymous/flux_text_encoders](https://huggingface.co/comfyanonymous/flux_text_encoders) | conditioner | Attention output | 12 | 0–11 | `[768, 768]` ×12 | F16×12 | FP16×12 |
| [comfyanonymous/flux_text_encoders](https://huggingface.co/comfyanonymous/flux_text_encoders) | conditioner | MLP up | 12 | 0–11 | `[3072, 768]` ×12 | F16×12 | FP16×12 |
| [comfyanonymous/flux_text_encoders](https://huggingface.co/comfyanonymous/flux_text_encoders) | conditioner | MLP down | 12 | 0–11 | `[768, 3072]` ×12 | F16×12 | FP16×12 |
| [comfyanonymous/flux_text_encoders](https://huggingface.co/comfyanonymous/flux_text_encoders) | vae | Q projection | 48 | 0–23 | `[4096, 4096]` ×48 | F16×24, F8_E4M3×24 | FP16×24, BF16 (FP8 weights)×24 |
| [comfyanonymous/flux_text_encoders](https://huggingface.co/comfyanonymous/flux_text_encoders) | vae | K projection | 48 | 0–23 | `[4096, 4096]` ×48 | F16×24, F8_E4M3×24 | FP16×24, BF16 (FP8 weights)×24 |
| [comfyanonymous/flux_text_encoders](https://huggingface.co/comfyanonymous/flux_text_encoders) | vae | V projection | 48 | 0–23 | `[4096, 4096]` ×48 | F16×24, F8_E4M3×24 | FP16×24, BF16 (FP8 weights)×24 |
| [comfyanonymous/flux_text_encoders](https://huggingface.co/comfyanonymous/flux_text_encoders) | vae | Attention scores (Q×Kᵀ) | 2 | 0 | `[B, H, D, S] (K^T)` ×2 | —×2 | FP16×1, BF16 (FP8 weights)×1 |
| [comfyanonymous/flux_text_encoders](https://huggingface.co/comfyanonymous/flux_text_encoders) | vae | Attention context (softmax×V) | 2 | 0 | `[B, H, S, D] (V)` ×2 | —×2 | FP16×1, BF16 (FP8 weights)×1 |
| [comfyanonymous/flux_text_encoders](https://huggingface.co/comfyanonymous/flux_text_encoders) | vae | Attention output | 48 | 0–23 | `[4096, 4096]` ×48 | F16×24, F8_E4M3×24 | FP16×24, BF16 (FP8 weights)×24 |
| [comfyanonymous/flux_text_encoders](https://huggingface.co/comfyanonymous/flux_text_encoders) | vae | MLP gate | 48 | 0–23 | `[10240, 4096]` ×48 | F16×24, F8_E4M3×24 | FP16×24, BF16 (FP8 weights)×24 |
| [comfyanonymous/flux_text_encoders](https://huggingface.co/comfyanonymous/flux_text_encoders) | vae | MLP up | 48 | 0–23 | `[10240, 4096]` ×48 | F16×24, F8_E4M3×24 | FP16×24, BF16 (FP8 weights)×24 |
| [comfyanonymous/flux_text_encoders](https://huggingface.co/comfyanonymous/flux_text_encoders) | vae | MLP down | 48 | 0–23 | `[4096, 10240]` ×48 | F16×24, F8_E4M3×24 | FP16×24, BF16 (FP8 weights)×24 |
| [drbaph/FLUX.1-schnell-dev-merged-fp8-4step](https://huggingface.co/drbaph/FLUX.1-schnell-dev-merged-fp8-4step) | conditioner | Q projection | 36 | 0–23 | `[4096, 4096]` ×24; `[768, 768]` ×12 | F16×36 | FP16×36 |
| [drbaph/FLUX.1-schnell-dev-merged-fp8-4step](https://huggingface.co/drbaph/FLUX.1-schnell-dev-merged-fp8-4step) | conditioner | K projection | 36 | 0–23 | `[4096, 4096]` ×24; `[768, 768]` ×12 | F16×36 | FP16×36 |
| [drbaph/FLUX.1-schnell-dev-merged-fp8-4step](https://huggingface.co/drbaph/FLUX.1-schnell-dev-merged-fp8-4step) | conditioner | V projection | 36 | 0–23 | `[4096, 4096]` ×24; `[768, 768]` ×12 | F16×36 | FP16×36 |
| [drbaph/FLUX.1-schnell-dev-merged-fp8-4step](https://huggingface.co/drbaph/FLUX.1-schnell-dev-merged-fp8-4step) | conditioner | Attention scores (Q×Kᵀ) | 1 | 0 | `[B, H, D, S] (K^T)` ×1 | —×1 | FP16×1 |
| [drbaph/FLUX.1-schnell-dev-merged-fp8-4step](https://huggingface.co/drbaph/FLUX.1-schnell-dev-merged-fp8-4step) | conditioner | Attention context (softmax×V) | 1 | 0 | `[B, H, S, D] (V)` ×1 | —×1 | FP16×1 |
| [drbaph/FLUX.1-schnell-dev-merged-fp8-4step](https://huggingface.co/drbaph/FLUX.1-schnell-dev-merged-fp8-4step) | conditioner | Attention output | 36 | 0–23 | `[4096, 4096]` ×24; `[768, 768]` ×12 | F16×36 | FP16×36 |
| [drbaph/FLUX.1-schnell-dev-merged-fp8-4step](https://huggingface.co/drbaph/FLUX.1-schnell-dev-merged-fp8-4step) | conditioner | MLP gate | 24 | 0–23 | `[10240, 4096]` ×24 | F16×24 | FP16×24 |
| [drbaph/FLUX.1-schnell-dev-merged-fp8-4step](https://huggingface.co/drbaph/FLUX.1-schnell-dev-merged-fp8-4step) | conditioner | MLP up | 36 | 0–23 | `[10240, 4096]` ×24; `[3072, 768]` ×12 | F16×36 | FP16×36 |
| [drbaph/FLUX.1-schnell-dev-merged-fp8-4step](https://huggingface.co/drbaph/FLUX.1-schnell-dev-merged-fp8-4step) | conditioner | MLP down | 36 | 0–23 | `[4096, 10240]` ×24; `[768, 3072]` ×12 | F16×36 | FP16×36 |
| [drbaph/FLUX.1-schnell-dev-merged-fp8-4step](https://huggingface.co/drbaph/FLUX.1-schnell-dev-merged-fp8-4step) | conditioner | Projection / FFN | 1 | — | `[768, 768]` ×1 | F16×1 | FP16×1 |
| [drbaph/FLUX.1-schnell-dev-merged-fp8-4step](https://huggingface.co/drbaph/FLUX.1-schnell-dev-merged-fp8-4step) | transformer | Projection / FFN | 191 | 0–37 | `[3072, 3072]` ×38; `[12288, 3072]` ×38; `[3072, 12288]` ×38 | F8_E4M3×191 | BF16 (FP8 weights)×191 |
| [drbaph/FLUX.1-schnell-dev-merged-fp8-4step](https://huggingface.co/drbaph/FLUX.1-schnell-dev-merged-fp8-4step) | transformer | Other linear | 120 | 0–37 | `[9216, 3072]` ×76; `[18432, 3072]` ×38; `[3072, 3072]` ×2 | F8_E4M3×120 | BF16 (FP8 weights)×120 |
| [drbaph/FLUX.1-schnell-dev-merged-fp8-4step](https://huggingface.co/drbaph/FLUX.1-schnell-dev-merged-fp8-4step) | vae | Convolution (im2col matmul) | 58 | 0–3 | `[512, 512, 3, 3]` ×30; `[128, 128, 3, 3]` ×10; `[256, 256, 3, 3]` ×10 | BF16×58 | BF16×58 |
| [drbaph/FLUX.1-schnell-dev-merged-fp8-4step](https://huggingface.co/drbaph/FLUX.1-schnell-dev-merged-fp8-4step) | vae | 1×1 conv matmul | 12 | 0 | `[512, 512, 1, 1]` ×8; `[128, 256, 1, 1]` ×1; `[256, 512, 1, 1]` ×1 | BF16×12 | BF16×12 |
| [Kijai/HunyuanVideo_comfy](https://huggingface.co/Kijai/HunyuanVideo_comfy) | double_blocks | MLP up | 40 | 0–19 | `[12288, 3072]` ×40 | F8_E4M3×40 | BF16 (FP8 weights)×40 |
| [Kijai/HunyuanVideo_comfy](https://huggingface.co/Kijai/HunyuanVideo_comfy) | double_blocks | MLP down | 40 | 0–19 | `[3072, 12288]` ×40 | F8_E4M3×40 | BF16 (FP8 weights)×40 |
| [Kijai/HunyuanVideo_comfy](https://huggingface.co/Kijai/HunyuanVideo_comfy) | double_blocks | Projection / FFN | 80 | 0–19 | `[3072, 3072]` ×40; `[18432, 3072]` ×40 | F8_E4M3×80 | BF16 (FP8 weights)×80 |
| [Kijai/HunyuanVideo_comfy](https://huggingface.co/Kijai/HunyuanVideo_comfy) | double_blocks | Other linear | 40 | 0–19 | `[9216, 3072]` ×40 | F8_E4M3×40 | BF16 (FP8 weights)×40 |
| [Kijai/HunyuanVideo_comfy](https://huggingface.co/Kijai/HunyuanVideo_comfy) | final_layer | Projection / FFN | 1 | — | `[64, 3072]` ×1 | BF16×1 | BF16×1 |
| [Kijai/HunyuanVideo_comfy](https://huggingface.co/Kijai/HunyuanVideo_comfy) | guidance_in | Projection / FFN | 2 | 0–2 | `[3072, 256]` ×1; `[3072, 3072]` ×1 | BF16×2 | BF16×2 |
| [Kijai/HunyuanVideo_comfy](https://huggingface.co/Kijai/HunyuanVideo_comfy) | img_in | Convolution (im2col matmul) | 1 | — | `[3072, 16, 1, 2, 2]` ×1 | BF16×1 | BF16×1 |
| [Kijai/HunyuanVideo_comfy](https://huggingface.co/Kijai/HunyuanVideo_comfy) | post_quant_conv | 1×1 conv matmul | 1 | — | `[16, 16, 1, 1, 1]` ×1 | BF16×1 | BF16×1 |
| [Kijai/HunyuanVideo_comfy](https://huggingface.co/Kijai/HunyuanVideo_comfy) | quant_conv | 1×1 conv matmul | 1 | — | `[32, 32, 1, 1, 1]` ×1 | BF16×1 | BF16×1 |
| [Kijai/HunyuanVideo_comfy](https://huggingface.co/Kijai/HunyuanVideo_comfy) | single_blocks | Projection / FFN | 120 | 0–39 | `[21504, 3072]` ×40; `[3072, 15360]` ×40; `[9216, 3072]` ×40 | F8_E4M3×120 | BF16 (FP8 weights)×120 |
| [Kijai/HunyuanVideo_comfy](https://huggingface.co/Kijai/HunyuanVideo_comfy) | time_in | Projection / FFN | 2 | 0–2 | `[3072, 256]` ×1; `[3072, 3072]` ×1 | BF16×2 | BF16×2 |
| [Kijai/HunyuanVideo_comfy](https://huggingface.co/Kijai/HunyuanVideo_comfy) | txt_in | Embedding projection | 1 | — | `[3072, 4096]` ×1 | BF16×1 | BF16×1 |
| [Kijai/HunyuanVideo_comfy](https://huggingface.co/Kijai/HunyuanVideo_comfy) | txt_in | MLP up | 2 | 0–1 | `[12288, 3072]` ×2 | BF16×2 | BF16×2 |
| [Kijai/HunyuanVideo_comfy](https://huggingface.co/Kijai/HunyuanVideo_comfy) | txt_in | MLP down | 2 | 0–1 | `[3072, 12288]` ×2 | BF16×2 | BF16×2 |
| [Kijai/HunyuanVideo_comfy](https://huggingface.co/Kijai/HunyuanVideo_comfy) | txt_in | Projection / FFN | 6 | 0–2 | `[3072, 3072]` ×4; `[3072, 4096]` ×1; `[3072, 256]` ×1 | BF16×6 | BF16×6 |
| [Kijai/HunyuanVideo_comfy](https://huggingface.co/Kijai/HunyuanVideo_comfy) | txt_in | Other linear | 2 | 0–1 | `[9216, 3072]` ×2 | BF16×2 | BF16×2 |
| [Kijai/HunyuanVideo_comfy](https://huggingface.co/Kijai/HunyuanVideo_comfy) | vae | Q projection | 2 | 0 | `[512, 512]` ×2 | BF16×2 | BF16×2 |
| [Kijai/HunyuanVideo_comfy](https://huggingface.co/Kijai/HunyuanVideo_comfy) | vae | K projection | 2 | 0 | `[512, 512]` ×2 | BF16×2 | BF16×2 |
| [Kijai/HunyuanVideo_comfy](https://huggingface.co/Kijai/HunyuanVideo_comfy) | vae | V projection | 2 | 0 | `[512, 512]` ×2 | BF16×2 | BF16×2 |
| [Kijai/HunyuanVideo_comfy](https://huggingface.co/Kijai/HunyuanVideo_comfy) | vae | Attention scores (Q×Kᵀ) | 1 | 0 | `[B, H, D, S] (K^T)` ×1 | —×1 | BF16×1 |
| [Kijai/HunyuanVideo_comfy](https://huggingface.co/Kijai/HunyuanVideo_comfy) | vae | Attention context (softmax×V) | 1 | 0 | `[B, H, S, D] (V)` ×1 | —×1 | BF16×1 |
| [Kijai/HunyuanVideo_comfy](https://huggingface.co/Kijai/HunyuanVideo_comfy) | vae | Attention output | 2 | 0 | `[512, 512]` ×2 | BF16×2 | BF16×2 |
| [Kijai/HunyuanVideo_comfy](https://huggingface.co/Kijai/HunyuanVideo_comfy) | vae | Convolution (im2col matmul) | 58 | 0–3 | `[512, 512, 3, 3, 3]` ×30; `[128, 128, 3, 3, 3]` ×10; `[256, 256, 3, 3, 3]` ×10 | BF16×58 | BF16×58 |
| [Kijai/HunyuanVideo_comfy](https://huggingface.co/Kijai/HunyuanVideo_comfy) | vae | 1×1 conv matmul | 4 | 1–3 | `[256, 128, 1, 1, 1]` ×1; `[256, 512, 1, 1, 1]` ×1; `[512, 256, 1, 1, 1]` ×1 | BF16×4 | BF16×4 |
| [Kijai/HunyuanVideo_comfy](https://huggingface.co/Kijai/HunyuanVideo_comfy) | vector_in | Other linear | 2 | — | `[3072, 768]` ×1; `[3072, 3072]` ×1 | BF16×2 | BF16×2 |
| [Kijai/llava-llama-3-8b-text-encoder-tokenizer](https://huggingface.co/Kijai/llava-llama-3-8b-text-encoder-tokenizer) | transformer | Q projection | 32 | 0–31 | `[4096, 4096]` ×32 | F16×32 | FP16×32 |
| [Kijai/llava-llama-3-8b-text-encoder-tokenizer](https://huggingface.co/Kijai/llava-llama-3-8b-text-encoder-tokenizer) | transformer | K projection | 32 | 0–31 | `[1024, 4096]` ×32 | F16×32 | FP16×32 |
| [Kijai/llava-llama-3-8b-text-encoder-tokenizer](https://huggingface.co/Kijai/llava-llama-3-8b-text-encoder-tokenizer) | transformer | V projection | 32 | 0–31 | `[1024, 4096]` ×32 | F16×32 | FP16×32 |
| [Kijai/llava-llama-3-8b-text-encoder-tokenizer](https://huggingface.co/Kijai/llava-llama-3-8b-text-encoder-tokenizer) | transformer | Attention scores (Q×Kᵀ) | 3 | 0–21 | `[B, H, D, S] (K^T)` ×3 | —×3 | FP16×3 |
| [Kijai/llava-llama-3-8b-text-encoder-tokenizer](https://huggingface.co/Kijai/llava-llama-3-8b-text-encoder-tokenizer) | transformer | Attention context (softmax×V) | 3 | 0–21 | `[B, H, S, D] (V)` ×3 | —×3 | FP16×3 |
| [Kijai/llava-llama-3-8b-text-encoder-tokenizer](https://huggingface.co/Kijai/llava-llama-3-8b-text-encoder-tokenizer) | transformer | MLP gate | 32 | 0–31 | `[14336, 4096]` ×32 | F16×32 | FP16×32 |
| [Kijai/llava-llama-3-8b-text-encoder-tokenizer](https://huggingface.co/Kijai/llava-llama-3-8b-text-encoder-tokenizer) | transformer | MLP up | 32 | 0–31 | `[14336, 4096]` ×32 | F16×32 | FP16×32 |
| [Kijai/llava-llama-3-8b-text-encoder-tokenizer](https://huggingface.co/Kijai/llava-llama-3-8b-text-encoder-tokenizer) | transformer | MLP down | 31 | 0–30 | `[4096, 14336]` ×31 | F16×31 | FP16×31 |
| [Kijai/llava-llama-3-8b-text-encoder-tokenizer](https://huggingface.co/Kijai/llava-llama-3-8b-text-encoder-tokenizer) | transformer | Projection / FFN | 32 | 0–31 | `[4096, 4096]` ×32 | F16×32 | FP16×32 |
| [latent-consistency/lcm-lora-sdxl](https://huggingface.co/latent-consistency/lcm-lora-sdxl) | transformer | LoRA down (low-rank) | 700 | 0–9 | `[64, 1280] (rank 64)` ×420; `[64, 2048] (rank 64)` ×140; `[64, 640] (rank 64)` ×70 | F16×700 | FP16×700 |
| [latent-consistency/lcm-lora-sdxl](https://huggingface.co/latent-consistency/lcm-lora-sdxl) | transformer | LoRA up (low-rank) | 700 | 0–9 | `[1280, 64]` ×540; `[640, 64]` ×90; `[10240, 64]` ×60 | F16×700 | FP16×700 |
| [latent-consistency/lcm-lora-sdxl](https://huggingface.co/latent-consistency/lcm-lora-sdxl) | unet | LoRA down (low-rank) | 88 | 0–2 | `[64, 1280] (rank 64)` ×42; `[64, 640] (rank 64)` ×24; `[64, 320] (rank 64)` ×10 | F16×88 | FP16×88 |
| [latent-consistency/lcm-lora-sdxl](https://huggingface.co/latent-consistency/lcm-lora-sdxl) | unet | LoRA up (low-rank) | 88 | 0–2 | `[1280, 64]` ×38; `[640, 64]` ×31; `[320, 64]` ×19 | F16×88 | FP16×88 |
| [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video) | transformer | Q projection | 112 | 0–27 | `[2048, 2048]` ×112 | BF16×56, F32×56 | BF16×56, FP32×56 |
| [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video) | transformer | K projection | 112 | 0–27 | `[2048, 2048]` ×112 | BF16×56, F32×56 | BF16×56, FP32×56 |
| [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video) | transformer | V projection | 112 | 0–27 | `[2048, 2048]` ×112 | BF16×56, F32×56 | BF16×56, FP32×56 |
| [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video) | transformer | Attention scores (Q×Kᵀ) | 2 | 0 | `[B, H, D, S] (K^T)` ×2 | —×2 | BF16×1, FP32×1 |
| [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video) | transformer | Attention context (softmax×V) | 2 | 0 | `[B, H, S, D] (V)` ×2 | —×2 | BF16×1, FP32×1 |
| [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video) | transformer | Attention output | 114 | 0–27 | `[2048, 2048]` ×112; `[128, 2048]` ×2 | BF16×57, F32×57 | BF16×57, FP32×57 |
| [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video) | transformer | Projection / FFN | 62 | 0–27 | `[8192, 2048]` ×56; `[2048, 4096]` ×2; `[2048, 2048]` ×2 | BF16×31, F32×31 | BF16×31, FP32×31 |
| [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video) | transformer | Other linear | 56 | 0–27 | `[2048, 8192]` ×56 | BF16×28, F32×28 | BF16×28, FP32×28 |
| [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video) | vae | Projection / FFN | 10 | 0–6 | `[256, 256]` ×2; `[4096, 256]` ×1; `[4096, 4096]` ×1 | BF16×10 | BF16×10 |
| [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video) | vae | Convolution (im2col matmul) | 177 | 0–9 | `[512, 512, 3, 3, 3]` ×64; `[256, 256, 3, 3, 3]` ×38; `[128, 128, 3, 3, 3]` ×36 | BF16×91, F32×86 | BF16×91, FP32×86 |
| [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video) | vae | 1×1 conv matmul | 4 | 2–7 | `[256, 128, 1, 1, 1]` ×1; `[256, 512, 1, 1, 1]` ×1; `[512, 256, 1, 1, 1]` ×1 | F32×4 | FP32×4 |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | conditioner | Q projection | 72 | 0–23 | `[4096, 4096]` ×48; `[768, 768]` ×24 | F8_E4M3×48, F16×24 | BF16 (FP8 weights)×48, FP16×24 |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | conditioner | K projection | 72 | 0–23 | `[4096, 4096]` ×48; `[768, 768]` ×24 | F8_E4M3×48, F16×24 | BF16 (FP8 weights)×48, FP16×24 |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | conditioner | V projection | 72 | 0–23 | `[4096, 4096]` ×48; `[768, 768]` ×24 | F8_E4M3×48, F16×24 | BF16 (FP8 weights)×48, FP16×24 |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | conditioner | Attention scores (Q×Kᵀ) | 2 | 0 | `[B, H, D, S] (K^T)` ×2 | —×2 | FP16×2 |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | conditioner | Attention context (softmax×V) | 2 | 0 | `[B, H, S, D] (V)` ×2 | —×2 | FP16×2 |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | conditioner | Attention output | 72 | 0–23 | `[4096, 4096]` ×48; `[768, 768]` ×24 | F8_E4M3×48, F16×24 | BF16 (FP8 weights)×48, FP16×24 |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | conditioner | MLP gate | 48 | 0–23 | `[10240, 4096]` ×48 | F8_E4M3×48 | BF16 (FP8 weights)×48 |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | conditioner | MLP up | 72 | 0–23 | `[10240, 4096]` ×48; `[3072, 768]` ×24 | F8_E4M3×48, F16×24 | BF16 (FP8 weights)×48, FP16×24 |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | conditioner | MLP down | 72 | 0–23 | `[4096, 10240]` ×48; `[768, 3072]` ×24 | F8_E4M3×48, F16×24 | BF16 (FP8 weights)×48, FP16×24 |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | conditioner | Projection / FFN | 2 | — | `[768, 768]` ×2 | F16×2 | FP16×2 |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | transformer | Projection / FFN | 382 | 0–37 | `[18874368, 1]` ×152; `[4718592, 1]` ×76; `[33030144, 1]` ×76 | U8×382 | BF16 (packed 4-bit weights)×382 |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | transformer | Other linear | 244 | 0–37 | `[14155776, 1]` ×152; `[28311552, 1]` ×76; `[4718592, 1]` ×6 | U8×244 | BF16 (packed 4-bit weights)×244 |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | vae | Convolution (im2col matmul) | 116 | 0–3 | `[512, 512, 3, 3]` ×60; `[128, 128, 3, 3]` ×20; `[256, 256, 3, 3]` ×20 | F32×116 | FP32×116 |
| [lllyasviel/flux1-dev-bnb-nf4](https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4) | vae | 1×1 conv matmul | 24 | 0 | `[512, 512, 1, 1]` ×16; `[128, 256, 1, 1]` ×2; `[256, 512, 1, 1]` ×2 | F32×24 | FP32×24 |
| [openai/clip-vit-large-patch14](https://huggingface.co/openai/clip-vit-large-patch14) | conditioner | Q projection | 12 | 0–11 | `[768, 768]` ×12 | F32×12 | FP32×12 |
| [openai/clip-vit-large-patch14](https://huggingface.co/openai/clip-vit-large-patch14) | conditioner | K projection | 12 | 0–11 | `[768, 768]` ×12 | F32×12 | FP32×12 |
| [openai/clip-vit-large-patch14](https://huggingface.co/openai/clip-vit-large-patch14) | conditioner | V projection | 12 | 0–11 | `[768, 768]` ×12 | F32×12 | FP32×12 |
| [openai/clip-vit-large-patch14](https://huggingface.co/openai/clip-vit-large-patch14) | conditioner | Attention scores (Q×Kᵀ) | 1 | 0 | `[B, H, D, S] (K^T)` ×1 | —×1 | FP32×1 |
| [openai/clip-vit-large-patch14](https://huggingface.co/openai/clip-vit-large-patch14) | conditioner | Attention context (softmax×V) | 1 | 0 | `[B, H, S, D] (V)` ×1 | —×1 | FP32×1 |
| [openai/clip-vit-large-patch14](https://huggingface.co/openai/clip-vit-large-patch14) | conditioner | Attention output | 12 | 0–11 | `[768, 768]` ×12 | F32×12 | FP32×12 |
| [openai/clip-vit-large-patch14](https://huggingface.co/openai/clip-vit-large-patch14) | conditioner | MLP up | 12 | 0–11 | `[3072, 768]` ×12 | F32×12 | FP32×12 |
| [openai/clip-vit-large-patch14](https://huggingface.co/openai/clip-vit-large-patch14) | conditioner | MLP down | 12 | 0–11 | `[768, 3072]` ×12 | F32×12 | FP32×12 |
| [openai/clip-vit-large-patch14](https://huggingface.co/openai/clip-vit-large-patch14) | text_projection | Projection / FFN | 1 | — | `[768, 768]` ×1 | F32×1 | FP32×1 |
| [openai/clip-vit-large-patch14](https://huggingface.co/openai/clip-vit-large-patch14) | transformer | Q projection | 24 | 0–23 | `[1024, 1024]` ×24 | F32×24 | FP32×24 |
| [openai/clip-vit-large-patch14](https://huggingface.co/openai/clip-vit-large-patch14) | transformer | K projection | 24 | 0–23 | `[1024, 1024]` ×24 | F32×24 | FP32×24 |
| [openai/clip-vit-large-patch14](https://huggingface.co/openai/clip-vit-large-patch14) | transformer | V projection | 24 | 0–23 | `[1024, 1024]` ×24 | F32×24 | FP32×24 |
| [openai/clip-vit-large-patch14](https://huggingface.co/openai/clip-vit-large-patch14) | transformer | Attention output | 24 | 0–23 | `[1024, 1024]` ×24 | F32×24 | FP32×24 |
| [openai/clip-vit-large-patch14](https://huggingface.co/openai/clip-vit-large-patch14) | transformer | MLP up | 24 | 0–23 | `[4096, 1024]` ×24 | F32×24 | FP32×24 |
| [openai/clip-vit-large-patch14](https://huggingface.co/openai/clip-vit-large-patch14) | transformer | MLP down | 24 | 0–23 | `[1024, 4096]` ×24 | F32×24 | FP32×24 |
| [openai/clip-vit-large-patch14](https://huggingface.co/openai/clip-vit-large-patch14) | transformer | Convolution (im2col matmul) | 1 | — | `[1024, 3, 14, 14]` ×1 | F32×1 | FP32×1 |
| [openai/clip-vit-large-patch14](https://huggingface.co/openai/clip-vit-large-patch14) | visual_projection | Projection / FFN | 1 | — | `[768, 1024]` ×1 | F32×1 | FP32×1 |
| [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | conditioner | Q projection | 12 | 0–11 | `[768, 768]` ×12 | F32×12 | FP32×12 |
| [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | conditioner | K projection | 12 | 0–11 | `[768, 768]` ×12 | F32×12 | FP32×12 |
| [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | conditioner | V projection | 12 | 0–11 | `[768, 768]` ×12 | F32×12 | FP32×12 |
| [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | conditioner | Attention scores (Q×Kᵀ) | 1 | 0 | `[B, H, D, S] (K^T)` ×1 | —×1 | FP32×1 |
| [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | conditioner | Attention context (softmax×V) | 1 | 0 | `[B, H, S, D] (V)` ×1 | —×1 | FP32×1 |
| [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | conditioner | Attention output | 12 | 0–11 | `[768, 768]` ×12 | F32×12 | FP32×12 |
| [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | conditioner | MLP up | 12 | 0–11 | `[3072, 768]` ×12 | F32×12 | FP32×12 |
| [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | conditioner | MLP down | 12 | 0–11 | `[768, 3072]` ×12 | F32×12 | FP32×12 |
| [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | transformer | Embedding projection | 2 | 0–2 | `[1280, 320]` ×1; `[1280, 1280]` ×1 | F32×2 | FP32×2 |
| [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | transformer | Q projection | 32 | 1–11 | `[1280, 1280]` ×12; `[320, 320]` ×10; `[640, 640]` ×10 | F32×32 | FP32×32 |
| [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | transformer | K projection | 32 | 1–11 | `[1280, 1280]` ×6; `[1280, 768]` ×6; `[320, 320]` ×5 | F32×32 | FP32×32 |
| [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | transformer | V projection | 32 | 1–11 | `[1280, 1280]` ×6; `[1280, 768]` ×6; `[320, 320]` ×5 | F32×32 | FP32×32 |
| [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | transformer | Attention output | 32 | 1–11 | `[1280, 1280]` ×12; `[320, 320]` ×10; `[640, 640]` ×10 | F32×32 | FP32×32 |
| [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | transformer | Projection / FFN | 16 | 1–11 | `[10240, 1280]` ×6; `[2560, 320]` ×5; `[5120, 640]` ×5 | F32×16 | FP32×16 |
| [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | transformer | Convolution (im2col matmul) | 110 | 0–11 | `[512, 512, 3, 3]` ×30; `[1280, 1280, 3, 3]` ×20; `[128, 128, 3, 3]` ×10 | F32×110 | FP32×110 |
| [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | transformer | 1×1 conv matmul | 60 | 0–11 | `[1280, 1280, 1, 1]` ×12; `[320, 320, 1, 1]` ×10; `[640, 640, 1, 1]` ×10 | F32×60 | FP32×60 |
| [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | transformer | Other linear | 38 | 0–11 | `[1280, 1280]` ×12; `[320, 1280]` ×10; `[1280, 5120]` ×6 | F32×38 | FP32×38 |
| [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) | conditioner | Q projection | 12 | 0–11 | `[768, 768]` ×12 | F16×12 | FP16×12 |
| [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) | conditioner | K projection | 12 | 0–11 | `[768, 768]` ×12 | F16×12 | FP16×12 |
| [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) | conditioner | V projection | 12 | 0–11 | `[768, 768]` ×12 | F16×12 | FP16×12 |
| [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) | conditioner | Attention scores (Q×Kᵀ) | 1 | 0 | `[B, H, D, S] (K^T)` ×1 | —×1 | FP16×1 |
| [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) | conditioner | Attention context (softmax×V) | 1 | 0 | `[B, H, S, D] (V)` ×1 | —×1 | FP16×1 |
| [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) | conditioner | Attention output | 44 | 0–31 | `[1280, 1280]` ×32; `[768, 768]` ×12 | F16×44 | FP16×44 |
| [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) | conditioner | MLP up | 12 | 0–11 | `[3072, 768]` ×12 | F16×12 | FP16×12 |
| [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) | conditioner | MLP down | 12 | 0–11 | `[768, 3072]` ×12 | F16×12 | FP16×12 |
| [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) | conditioner | Projection / FFN | 64 | 0–31 | `[5120, 1280]` ×32; `[1280, 5120]` ×32 | F16×64 | FP16×64 |
| [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) | transformer | Embedding projection | 2 | 0–2 | `[1280, 320]` ×1; `[1280, 1280]` ×1 | F16×2 | FP16×2 |
| [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) | transformer | Q projection | 140 | 0–8 | `[1280, 1280]` ×120; `[640, 640]` ×20 | F16×140 | FP16×140 |
| [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) | transformer | K projection | 140 | 0–8 | `[1280, 1280]` ×60; `[1280, 2048]` ×60; `[640, 640]` ×10 | F16×140 | FP16×140 |
| [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) | transformer | V projection | 140 | 0–8 | `[1280, 1280]` ×60; `[1280, 2048]` ×60; `[640, 640]` ×10 | F16×140 | FP16×140 |
| [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) | transformer | Attention output | 151 | 0–8 | `[1280, 1280]` ×126; `[640, 640]` ×25 | F16×151 | FP16×151 |
| [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) | transformer | Projection / FFN | 81 | 0–8 | `[10240, 1280]` ×60; `[5120, 640]` ×10; `[1280, 1280]` ×6 | F16×81 | FP16×81 |
| [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) | transformer | Convolution (im2col matmul) | 98 | 0–8 | `[512, 512, 3, 3]` ×30; `[1280, 1280, 3, 3]` ×11; `[128, 128, 3, 3]` ×10 | F16×98 | FP16×98 |
| [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) | transformer | 1×1 conv matmul | 25 | 0–8 | `[512, 512, 1, 1]` ×8; `[1280, 2560, 1, 1]` ×2; `[320, 640, 1, 1]` ×2 | F16×25 | FP16×25 |
| [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) | transformer | Other linear | 89 | 0–8 | `[1280, 5120]` ×60; `[640, 2560]` ×10; `[1280, 1280]` ×8 | F16×89 | FP16×89 |
| [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | conditioner | Q projection | 12 | 0–11 | `[768, 768]` ×12 | F16×12 | FP16×12 |
| [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | conditioner | K projection | 12 | 0–11 | `[768, 768]` ×12 | F16×12 | FP16×12 |
| [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | conditioner | V projection | 12 | 0–11 | `[768, 768]` ×12 | F16×12 | FP16×12 |
| [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | conditioner | Attention scores (Q×Kᵀ) | 1 | 0 | `[B, H, D, S] (K^T)` ×1 | —×1 | FP16×1 |
| [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | conditioner | Attention context (softmax×V) | 1 | 0 | `[B, H, S, D] (V)` ×1 | —×1 | FP16×1 |
| [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | conditioner | Attention output | 44 | 0–31 | `[1280, 1280]` ×32; `[768, 768]` ×12 | F16×44 | FP16×44 |
| [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | conditioner | MLP up | 12 | 0–11 | `[3072, 768]` ×12 | F16×12 | FP16×12 |
| [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | conditioner | MLP down | 12 | 0–11 | `[768, 3072]` ×12 | F16×12 | FP16×12 |
| [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | conditioner | Projection / FFN | 64 | 0–31 | `[5120, 1280]` ×32; `[1280, 5120]` ×32 | F16×64 | FP16×64 |
| [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | transformer | Embedding projection | 2 | 0–2 | `[1280, 320]` ×1; `[1280, 1280]` ×1 | F16×2 | FP16×2 |
| [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | transformer | Q projection | 140 | 0–8 | `[1280, 1280]` ×120; `[640, 640]` ×20 | F16×140 | FP16×140 |
| [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | transformer | K projection | 140 | 0–8 | `[1280, 1280]` ×60; `[1280, 2048]` ×60; `[640, 640]` ×10 | F16×140 | FP16×140 |
| [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | transformer | V projection | 140 | 0–8 | `[1280, 1280]` ×60; `[1280, 2048]` ×60; `[640, 640]` ×10 | F16×140 | FP16×140 |
| [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | transformer | Attention output | 151 | 0–8 | `[1280, 1280]` ×126; `[640, 640]` ×25 | F16×151 | FP16×151 |
| [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | transformer | Projection / FFN | 81 | 0–8 | `[10240, 1280]` ×60; `[5120, 640]` ×10; `[1280, 1280]` ×6 | F16×81 | FP16×81 |
| [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | transformer | Convolution (im2col matmul) | 98 | 0–8 | `[512, 512, 3, 3]` ×30; `[1280, 1280, 3, 3]` ×11; `[128, 128, 3, 3]` ×10 | F16×98 | FP16×98 |
| [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | transformer | 1×1 conv matmul | 25 | 0–8 | `[512, 512, 1, 1]` ×8; `[1280, 2560, 1, 1]` ×2; `[320, 640, 1, 1]` ×2 | F16×25 | FP16×25 |
| [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | transformer | Other linear | 89 | 0–8 | `[1280, 5120]` ×60; `[640, 2560]` ×10; `[1280, 1280]` ×8 | F16×89 | FP16×89 |
