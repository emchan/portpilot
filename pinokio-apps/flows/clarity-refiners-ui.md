# Matrix-multiply flow — clarity-refiners-ui

Companion to [`results/pinokio-apps.md`](../results/pinokio-apps.md) and [`analysis/flows.md`](../analysis/flows.md). Interactive viewer: [`clarity-refiners-ui.html`](clarity-refiners-ui.html).

**Models whose checkpoints were analysed:** [multimodalart/Florence-2-large-no-flash-attn](https://huggingface.co/multimodalart/Florence-2-large-no-flash-attn), [philz1337x/embeddings](https://huggingface.co/philz1337x/embeddings), [philz1337x/loras](https://huggingface.co/philz1337x/loras), [philz1337x/upscaler](https://huggingface.co/philz1337x/upscaler), [refiners/controlnet.sd1_5.tile](https://huggingface.co/refiners/controlnet.sd1_5.tile), [refiners/juggernaut.reborn.sd1_5.autoencoder](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.autoencoder), [refiners/juggernaut.reborn.sd1_5.text_encoder](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.text_encoder), [refiners/juggernaut.reborn.sd1_5.unet](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.unet)

Reconstructed **2,011 matmul operations** from 5 checkpoint(s) (4 safetensors files).

## How the flow was inferred

The launcher snapshots are wrappers, so the graph is reconstructed from the safetensors header of each checkpoint the launcher downloads. Tensor **names** encode the layer role (Q/K/V, attention out, MLP gate/up/down, conv, head), **shapes** encode the matrix dimensions (PyTorch stores linear weights as `[out_features, in_features]`), and **dtypes** give weight precision. Activation precision is inferred from the weight dtype (quantized weights imply BF16/FP16 compute). `B` is the weight matrix; `A` is the activation `[B, S, in]` and `C` the output `[B, S, out]`. Two extra ops per attention block (Q×Kᵀ and softmax×V) are derived from the Q/K/V triple. This is an inferred dataflow, not a traced execution.

## Flow summary

| Component | Matmul ops | Weight dtypes | Activation dtypes |
| --- | --- | --- | --- |
| transformer | 1,040 | F16 (720), F32 (320) | FP16 (720), FP32 (320) |
| conditioner | 564 | F16 (420), F32 (144) | FP16 (420), FP32 (144) |
| unet | 192 | F16 (128), F32 (64) | FP16 (128), FP32 (64) |
| vae | 78 | F16 (78) | FP16 (78) |
| downblocks | 72 | F16 (72) | FP16 (72) |
| upblocks | 51 | F16 (51) | FP16 (51) |
| middleblock | 7 | F16 (7) | FP16 (7) |
| sum | 6 | F16 (6) | FP16 (6) |
| chain | 1 | F16 (1) | FP16 (1) |

## Representative block sequence — [refiners/juggernaut.reborn.sd1_5.text_encoder](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.text_encoder), `transformer`, block 1

This is one coherent pass through a repeated transformer/UNet block; the aggregated roles across every block follow in the next section.

| # | Role | Operation | A (activation) | B (weight) | C (output) | Precision |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Projection / FFN | Matmul (linear) | [B, S, 768] FP16 | [768, 768] F16 | [B, S, 768] FP16 | F16 weights / FP16 activations |

## Aggregated matrix-multiply roles

For every model and component, each role is listed with the number of matching weight tensors, the most common weight shapes, and the weight/activation dtypes.

| Model | Component | Role | Ops | Blocks | Common B shapes | Weight dtypes | Activation dtypes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [philz1337x/loras](https://huggingface.co/philz1337x/loras) | conditioner | LoRA down (low-rank) | 144 | 0–11 | `[4, 768] (rank 4)` ×60; `[128, 768] (rank 128)` ×60; `[4, 3072] (rank 4)` ×12 | F32×72, F16×72 | FP32×72, FP16×72 |
| [philz1337x/loras](https://huggingface.co/philz1337x/loras) | conditioner | LoRA up (low-rank) | 144 | 0–11 | `[768, 4]` ×60; `[768, 128]` ×60; `[3072, 4]` ×12 | F32×72, F16×72 | FP32×72, FP16×72 |
| [philz1337x/loras](https://huggingface.co/philz1337x/loras) | transformer | LoRA down (low-rank) | 480 | 0–3 | `[32, 1280] (rank 32)` ×47; `[4, 1280] (rank 4)` ×47; `[128, 1280] (rank 128)` ×47 | F16×320, F32×160 | FP16×320, FP32×160 |
| [philz1337x/loras](https://huggingface.co/philz1337x/loras) | transformer | LoRA up (low-rank) | 480 | 0–3 | `[1280, 32]` ×54; `[1280, 4]` ×54; `[1280, 128]` ×54 | F16×320, F32×160 | FP16×320, FP32×160 |
| [philz1337x/loras](https://huggingface.co/philz1337x/loras) | unet | LoRA down (low-rank) | 96 | 0–3 | `[32, 1280] (rank 32)` ×12; `[4, 1280] (rank 4)` ×12; `[128, 1280] (rank 128)` ×12 | F16×64, F32×32 | FP16×64, FP32×32 |
| [philz1337x/loras](https://huggingface.co/philz1337x/loras) | unet | LoRA up (low-rank) | 96 | 0–3 | `[1280, 32]` ×12; `[1280, 4]` ×12; `[1280, 128]` ×12 | F16×64, F32×32 | FP16×64, FP32×32 |
| [refiners/controlnet.sd1_5.tile](https://huggingface.co/refiners/controlnet.sd1_5.tile) | conditioner | Projection / FFN | 70 | — | `[1280, 1280]` ×18; `[320, 320]` ×12; `[640, 640]` ×12 | F16×70 | FP16×70 |
| [refiners/controlnet.sd1_5.tile](https://huggingface.co/refiners/controlnet.sd1_5.tile) | conditioner | 1×1 conv matmul | 14 | — | `[1280, 1280, 1, 1]` ×6; `[320, 320, 1, 1]` ×4; `[640, 640, 1, 1]` ×4 | F16×14 | FP16×14 |
| [refiners/controlnet.sd1_5.tile](https://huggingface.co/refiners/controlnet.sd1_5.tile) | downblocks | Projection / FFN | 8 | — | `[1280, 1280]` ×4; `[320, 1280]` ×2; `[640, 1280]` ×2 | F16×8 | FP16×8 |
| [refiners/controlnet.sd1_5.tile](https://huggingface.co/refiners/controlnet.sd1_5.tile) | downblocks | Convolution (im2col matmul) | 20 | — | `[1280, 1280, 3, 3]` ×8; `[320, 320, 3, 3]` ×5; `[640, 640, 3, 3]` ×4 | F16×20 | FP16×20 |
| [refiners/controlnet.sd1_5.tile](https://huggingface.co/refiners/controlnet.sd1_5.tile) | downblocks | 1×1 conv matmul | 14 | — | `[1280, 1280, 1, 1]` ×5; `[320, 320, 1, 1]` ×4; `[640, 640, 1, 1]` ×3 | F16×14 | FP16×14 |
| [refiners/controlnet.sd1_5.tile](https://huggingface.co/refiners/controlnet.sd1_5.tile) | middleblock | Projection / FFN | 2 | 1–2 | `[1280, 1280]` ×2 | F16×2 | FP16×2 |
| [refiners/controlnet.sd1_5.tile](https://huggingface.co/refiners/controlnet.sd1_5.tile) | middleblock | Convolution (im2col matmul) | 4 | 1–2 | `[1280, 1280, 3, 3]` ×4 | F16×4 | FP16×4 |
| [refiners/controlnet.sd1_5.tile](https://huggingface.co/refiners/controlnet.sd1_5.tile) | middleblock | 1×1 conv matmul | 1 | — | `[1280, 1280, 1, 1]` ×1 | F16×1 | FP16×1 |
| [refiners/controlnet.sd1_5.tile](https://huggingface.co/refiners/controlnet.sd1_5.tile) | transformer | Convolution (im2col matmul) | 8 | — | `[16, 3, 3, 3]` ×1; `[16, 16, 3, 3]` ×1; `[32, 16, 3, 3]` ×1 | F16×8 | FP16×8 |
| [refiners/controlnet.sd1_5.tile](https://huggingface.co/refiners/controlnet.sd1_5.tile) | vae | Projection / FFN | 2 | — | `[1280, 320]` ×1; `[1280, 1280]` ×1 | F16×2 | FP16×2 |
| [refiners/juggernaut.reborn.sd1_5.autoencoder](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.autoencoder) | vae | Projection / FFN | 8 | — | `[512, 512]` ×8 | F16×8 | FP16×8 |
| [refiners/juggernaut.reborn.sd1_5.autoencoder](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.autoencoder) | vae | Convolution (im2col matmul) | 58 | — | `[512, 512, 3, 3]` ×30; `[256, 256, 3, 3]` ×10; `[128, 128, 3, 3]` ×10 | F16×58 | FP16×58 |
| [refiners/juggernaut.reborn.sd1_5.autoencoder](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.autoencoder) | vae | 1×1 conv matmul | 6 | — | `[256, 512, 1, 1]` ×1; `[128, 256, 1, 1]` ×1; `[4, 4, 1, 1]` ×1 | F16×6 | FP16×6 |
| [refiners/juggernaut.reborn.sd1_5.text_encoder](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.text_encoder) | transformer | Projection / FFN | 72 | 1–12 | `[768, 768]` ×48; `[3072, 768]` ×12; `[768, 3072]` ×12 | F16×72 | FP16×72 |
| [refiners/juggernaut.reborn.sd1_5.text_encoder](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.text_encoder) | vae | Embedding projection | 1 | — | `[77, 768]` ×1 | F16×1 | FP16×1 |
| [refiners/juggernaut.reborn.sd1_5.text_encoder](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.text_encoder) | vae | Other linear | 1 | — | `[49408, 768]` ×1 | F16×1 | FP16×1 |
| [refiners/juggernaut.reborn.sd1_5.unet](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.unet) | chain | Convolution (im2col matmul) | 1 | — | `[4, 320, 3, 3]` ×1 | F16×1 | FP16×1 |
| [refiners/juggernaut.reborn.sd1_5.unet](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.unet) | conditioner | Projection / FFN | 160 | — | `[1280, 1280]` ×36; `[320, 320]` ×30; `[640, 640]` ×30 | F16×160 | FP16×160 |
| [refiners/juggernaut.reborn.sd1_5.unet](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.unet) | conditioner | 1×1 conv matmul | 32 | — | `[1280, 1280, 1, 1]` ×12; `[320, 320, 1, 1]` ×10; `[640, 640, 1, 1]` ×10 | F16×32 | FP16×32 |
| [refiners/juggernaut.reborn.sd1_5.unet](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.unet) | downblocks | Projection / FFN | 8 | — | `[1280, 1280]` ×4; `[320, 1280]` ×2; `[640, 1280]` ×2 | F16×8 | FP16×8 |
| [refiners/juggernaut.reborn.sd1_5.unet](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.unet) | downblocks | Convolution (im2col matmul) | 20 | — | `[1280, 1280, 3, 3]` ×8; `[320, 320, 3, 3]` ×5; `[640, 640, 3, 3]` ×4 | F16×20 | FP16×20 |
| [refiners/juggernaut.reborn.sd1_5.unet](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.unet) | downblocks | 1×1 conv matmul | 2 | — | `[640, 320, 1, 1]` ×1; `[1280, 640, 1, 1]` ×1 | F16×2 | FP16×2 |
| [refiners/juggernaut.reborn.sd1_5.unet](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.unet) | sum | Projection / FFN | 2 | 1–2 | `[1280, 1280]` ×2 | F16×2 | FP16×2 |
| [refiners/juggernaut.reborn.sd1_5.unet](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.unet) | sum | Convolution (im2col matmul) | 4 | 1–2 | `[1280, 1280, 3, 3]` ×4 | F16×4 | FP16×4 |
| [refiners/juggernaut.reborn.sd1_5.unet](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.unet) | upblocks | Projection / FFN | 12 | — | `[1280, 1280]` ×6; `[320, 1280]` ×3; `[640, 1280]` ×3 | F16×12 | FP16×12 |
| [refiners/juggernaut.reborn.sd1_5.unet](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.unet) | upblocks | Convolution (im2col matmul) | 27 | — | `[1280, 1280, 3, 3]` ×8; `[1280, 2560, 3, 3]` ×5; `[640, 640, 3, 3]` ×4 | F16×27 | FP16×27 |
| [refiners/juggernaut.reborn.sd1_5.unet](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.unet) | upblocks | 1×1 conv matmul | 12 | — | `[1280, 2560, 1, 1]` ×5; `[320, 640, 1, 1]` ×2; `[320, 960, 1, 1]` ×1 | F16×12 | FP16×12 |
| [refiners/juggernaut.reborn.sd1_5.unet](https://huggingface.co/refiners/juggernaut.reborn.sd1_5.unet) | vae | Projection / FFN | 2 | — | `[1280, 320]` ×1; `[1280, 1280]` ×1 | F16×2 | FP16×2 |

## Snapdragon note
- Deep scan: cuda=5, torch=59, xformers=2, mps=1, directml=1, safetensors=6. Contains CUDA/Triton/TensorRT signals; Snapdragon path requires replacement or ONNX conversion.
