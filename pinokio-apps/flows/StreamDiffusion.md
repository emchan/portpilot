# Matrix-multiply flow — StreamDiffusion

Companion to [`results/pinokio-apps.md`](../results/pinokio-apps.md) and [`analysis/flows.md`](../analysis/flows.md). Interactive viewer: [`StreamDiffusion.html`](StreamDiffusion.html).

**Models whose checkpoints were analysed:** [KBlueLeaf/kohaku-v2.1](https://huggingface.co/KBlueLeaf/kohaku-v2.1), [latent-consistency/lcm-lora-sdv1-5](https://huggingface.co/latent-consistency/lcm-lora-sdv1-5), [madebyollin/taesd](https://huggingface.co/madebyollin/taesd), [stabilityai/sd-turbo](https://huggingface.co/stabilityai/sd-turbo)

Reconstructed **1,552 matmul operations** from 4 checkpoint(s) (6 safetensors files).

## How the flow was inferred

The launcher snapshots are wrappers, so the graph is reconstructed from the safetensors header of each checkpoint the launcher downloads. Tensor **names** encode the layer role (Q/K/V, attention out, MLP gate/up/down, conv, head), **shapes** encode the matrix dimensions (PyTorch stores linear weights as `[out_features, in_features]`), and **dtypes** give weight precision. Activation precision is inferred from the weight dtype (quantized weights imply BF16/FP16 compute). `B` is the weight matrix; `A` is the activation `[B, S, in]` and `C` the output `[B, S, out]`. Two extra ops per attention block (Q×Kᵀ and softmax×V) are derived from the Q/K/V triple. This is an inferred dataflow, not a traced execution.

## Flow summary

| Component | Matmul ops | Weight dtypes | Activation dtypes |
| --- | --- | --- | --- |
| transformer | 1,030 | F16 (674), F32 (354), — (2) | FP16 (674), FP32 (356) |
| unet | 236 | F16 (236) | FP16 (236) |
| conditioner | 146 | F16 (72), F32 (72), — (2) | FP16 (74), FP32 (72) |
| vae | 140 | F32 (140) | FP32 (140) |

## Representative block sequence — [stabilityai/sd-turbo](https://huggingface.co/stabilityai/sd-turbo), `transformer`, block 1

This is one coherent pass through a repeated transformer/UNet block; the aggregated roles across every block follow in the next section.

| # | Role | Operation | A (activation) | B (weight) | C (output) | Precision |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Q projection | Matmul (linear) | [B, S, 320] FP32 | [320, 320] F32 | [B, S, 320] FP32 | F32 weights / FP32 activations |
| 2 | K projection | Matmul (linear) | [B, S, 320] FP32 | [320, 320] F32 | [B, S, 320] FP32 | F32 weights / FP32 activations |
| 3 | V projection | Matmul (linear) | [B, S, 320] FP32 | [320, 320] F32 | [B, S, 320] FP32 | F32 weights / FP32 activations |
| 4 | Attention scores (Q×Kᵀ) | Attention scores (Q x K^T) | [B, H, S, D] FP32 | [B, H, D, S] (K^T) FP32 | [B, H, S, S] FP32, FP32 accumulate | — weights / FP32 activations |
| 5 | Attention context (softmax×V) | Attention context (softmax x V) | [B, H, S, S] FP32 | [B, H, S, D] (V) FP32 | [B, H, S, D] FP32 | — weights / FP32 activations |
| 6 | Attention output | Matmul (linear) | [B, S, 320] FP32 | [320, 320] F32 | [B, S, 320] FP32 | F32 weights / FP32 activations |
| 7 | Projection / FFN | Matmul (linear) | [B, S, 320] FP32 | [320, 320] F32 | [B, S, 320] FP32 | F32 weights / FP32 activations |
| 8 | Convolution (im2col matmul) | Conv [3, 3] (im2col matmul) | [B, 512, spatial] FP32 | [512, 512, 3, 3] F32 | [B, 512, spatial'] FP32 | F32 weights / FP32 activations |
| 9 | 1×1 conv matmul | Matmul (1x1 conv) | [B, 2560, spatial] FP32 | [1280, 2560, 1, 1] F32 | [B, 1280, spatial'] FP32 | F32 weights / FP32 activations |
| 10 | Other linear | Matmul (linear) | [B, S, 1280] FP32 | [320, 1280] F32 | [B, S, 320] FP32 | F32 weights / FP32 activations |

## Aggregated matrix-multiply roles

For every model and component, each role is listed with the number of matching weight tensors, the most common weight shapes, and the weight/activation dtypes.

| Model | Component | Role | Ops | Blocks | Common B shapes | Weight dtypes | Activation dtypes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [KBlueLeaf/kohaku-v2.1](https://huggingface.co/KBlueLeaf/kohaku-v2.1) | conditioner | Q projection | 12 | 0–11 | `[768, 768]` ×12 | F16×12 | FP16×12 |
| [KBlueLeaf/kohaku-v2.1](https://huggingface.co/KBlueLeaf/kohaku-v2.1) | conditioner | K projection | 12 | 0–11 | `[768, 768]` ×12 | F16×12 | FP16×12 |
| [KBlueLeaf/kohaku-v2.1](https://huggingface.co/KBlueLeaf/kohaku-v2.1) | conditioner | V projection | 12 | 0–11 | `[768, 768]` ×12 | F16×12 | FP16×12 |
| [KBlueLeaf/kohaku-v2.1](https://huggingface.co/KBlueLeaf/kohaku-v2.1) | conditioner | Attention scores (Q×Kᵀ) | 1 | 0 | `[B, H, D, S] (K^T)` ×1 | —×1 | FP16×1 |
| [KBlueLeaf/kohaku-v2.1](https://huggingface.co/KBlueLeaf/kohaku-v2.1) | conditioner | Attention context (softmax×V) | 1 | 0 | `[B, H, S, D] (V)` ×1 | —×1 | FP16×1 |
| [KBlueLeaf/kohaku-v2.1](https://huggingface.co/KBlueLeaf/kohaku-v2.1) | conditioner | Attention output | 12 | 0–11 | `[768, 768]` ×12 | F16×12 | FP16×12 |
| [KBlueLeaf/kohaku-v2.1](https://huggingface.co/KBlueLeaf/kohaku-v2.1) | conditioner | MLP up | 12 | 0–11 | `[3072, 768]` ×12 | F16×12 | FP16×12 |
| [KBlueLeaf/kohaku-v2.1](https://huggingface.co/KBlueLeaf/kohaku-v2.1) | conditioner | MLP down | 12 | 0–11 | `[768, 3072]` ×12 | F16×12 | FP16×12 |
| [KBlueLeaf/kohaku-v2.1](https://huggingface.co/KBlueLeaf/kohaku-v2.1) | transformer | Embedding projection | 2 | 0–2 | `[1280, 320]` ×1; `[1280, 1280]` ×1 | F16×2 | FP16×2 |
| [KBlueLeaf/kohaku-v2.1](https://huggingface.co/KBlueLeaf/kohaku-v2.1) | transformer | Q projection | 32 | 1–11 | `[1280, 1280]` ×12; `[320, 320]` ×10; `[640, 640]` ×10 | F16×32 | FP16×32 |
| [KBlueLeaf/kohaku-v2.1](https://huggingface.co/KBlueLeaf/kohaku-v2.1) | transformer | K projection | 32 | 1–11 | `[1280, 1280]` ×6; `[1280, 768]` ×6; `[320, 320]` ×5 | F16×32 | FP16×32 |
| [KBlueLeaf/kohaku-v2.1](https://huggingface.co/KBlueLeaf/kohaku-v2.1) | transformer | V projection | 32 | 1–11 | `[1280, 1280]` ×6; `[1280, 768]` ×6; `[320, 320]` ×5 | F16×32 | FP16×32 |
| [KBlueLeaf/kohaku-v2.1](https://huggingface.co/KBlueLeaf/kohaku-v2.1) | transformer | Attention output | 32 | 1–11 | `[1280, 1280]` ×12; `[320, 320]` ×10; `[640, 640]` ×10 | F16×32 | FP16×32 |
| [KBlueLeaf/kohaku-v2.1](https://huggingface.co/KBlueLeaf/kohaku-v2.1) | transformer | Projection / FFN | 16 | 1–11 | `[10240, 1280]` ×6; `[2560, 320]` ×5; `[5120, 640]` ×5 | F16×16 | FP16×16 |
| [KBlueLeaf/kohaku-v2.1](https://huggingface.co/KBlueLeaf/kohaku-v2.1) | transformer | Convolution (im2col matmul) | 110 | 0–11 | `[512, 512, 3, 3]` ×30; `[1280, 1280, 3, 3]` ×20; `[128, 128, 3, 3]` ×10 | F16×110 | FP16×110 |
| [KBlueLeaf/kohaku-v2.1](https://huggingface.co/KBlueLeaf/kohaku-v2.1) | transformer | 1×1 conv matmul | 60 | 0–11 | `[1280, 1280, 1, 1]` ×12; `[320, 320, 1, 1]` ×10; `[640, 640, 1, 1]` ×10 | F16×60 | FP16×60 |
| [KBlueLeaf/kohaku-v2.1](https://huggingface.co/KBlueLeaf/kohaku-v2.1) | transformer | Other linear | 38 | 0–11 | `[1280, 1280]` ×12; `[320, 1280]` ×10; `[1280, 5120]` ×6 | F16×38 | FP16×38 |
| [latent-consistency/lcm-lora-sdv1-5](https://huggingface.co/latent-consistency/lcm-lora-sdv1-5) | transformer | LoRA down (low-rank) | 160 | 0–3 | `[64, 1280] (rank 64)` ×47; `[64, 320] (rank 64)` ×35; `[64, 640] (rank 64)` ×35 | F16×160 | FP16×160 |
| [latent-consistency/lcm-lora-sdv1-5](https://huggingface.co/latent-consistency/lcm-lora-sdv1-5) | transformer | LoRA up (low-rank) | 160 | 0–3 | `[1280, 64]` ×54; `[320, 64]` ×45; `[640, 64]` ×45 | F16×160 | FP16×160 |
| [latent-consistency/lcm-lora-sdv1-5](https://huggingface.co/latent-consistency/lcm-lora-sdv1-5) | unet | LoRA down (low-rank) | 118 | 0–3 | `[64, 1280] (rank 64)` ×56; `[64, 640] (rank 64)` ×24; `[64, 320] (rank 64)` ×20 | F16×118 | FP16×118 |
| [latent-consistency/lcm-lora-sdv1-5](https://huggingface.co/latent-consistency/lcm-lora-sdv1-5) | unet | LoRA up (low-rank) | 118 | 0–3 | `[1280, 64]` ×58; `[640, 64]` ×31; `[320, 64]` ×29 | F16×118 | FP16×118 |
| [madebyollin/taesd](https://huggingface.co/madebyollin/taesd) | vae | Convolution (im2col matmul) | 140 | 0–18 | `[64, 64, 3, 3]` ×132; `[64, 3, 3, 3]` ×2; `[64, 4, 3, 3]` ×2 | F32×140 | FP32×140 |
| [stabilityai/sd-turbo](https://huggingface.co/stabilityai/sd-turbo) | conditioner | Attention output | 24 | 0–23 | `[1024, 1024]` ×24 | F32×24 | FP32×24 |
| [stabilityai/sd-turbo](https://huggingface.co/stabilityai/sd-turbo) | conditioner | Projection / FFN | 48 | 0–23 | `[4096, 1024]` ×24; `[1024, 4096]` ×24 | F32×48 | FP32×48 |
| [stabilityai/sd-turbo](https://huggingface.co/stabilityai/sd-turbo) | transformer | Embedding projection | 2 | 0–2 | `[1280, 320]` ×1; `[1280, 1280]` ×1 | F32×2 | FP32×2 |
| [stabilityai/sd-turbo](https://huggingface.co/stabilityai/sd-turbo) | transformer | Q projection | 32 | 1–11 | `[1280, 1280]` ×12; `[320, 320]` ×10; `[640, 640]` ×10 | F32×32 | FP32×32 |
| [stabilityai/sd-turbo](https://huggingface.co/stabilityai/sd-turbo) | transformer | K projection | 32 | 1–11 | `[1280, 1280]` ×6; `[1280, 1024]` ×6; `[320, 320]` ×5 | F32×32 | FP32×32 |
| [stabilityai/sd-turbo](https://huggingface.co/stabilityai/sd-turbo) | transformer | V projection | 32 | 1–11 | `[1280, 1280]` ×6; `[1280, 1024]` ×6; `[320, 320]` ×5 | F32×32 | FP32×32 |
| [stabilityai/sd-turbo](https://huggingface.co/stabilityai/sd-turbo) | transformer | Attention scores (Q×Kᵀ) | 1 | 1 | `[B, H, D, S] (K^T)` ×1 | —×1 | FP32×1 |
| [stabilityai/sd-turbo](https://huggingface.co/stabilityai/sd-turbo) | transformer | Attention context (softmax×V) | 1 | 1 | `[B, H, S, D] (V)` ×1 | —×1 | FP32×1 |
| [stabilityai/sd-turbo](https://huggingface.co/stabilityai/sd-turbo) | transformer | Attention output | 48 | 1–11 | `[1280, 1280]` ×18; `[320, 320]` ×15; `[640, 640]` ×15 | F32×48 | FP32×48 |
| [stabilityai/sd-turbo](https://huggingface.co/stabilityai/sd-turbo) | transformer | Projection / FFN | 32 | 1–11 | `[1280, 1280]` ×6; `[10240, 1280]` ×6; `[320, 320]` ×5 | F32×32 | FP32×32 |
| [stabilityai/sd-turbo](https://huggingface.co/stabilityai/sd-turbo) | transformer | Convolution (im2col matmul) | 110 | 0–11 | `[512, 512, 3, 3]` ×30; `[1280, 1280, 3, 3]` ×20; `[128, 128, 3, 3]` ×10 | F32×110 | FP32×110 |
| [stabilityai/sd-turbo](https://huggingface.co/stabilityai/sd-turbo) | transformer | 1×1 conv matmul | 28 | 0–11 | `[512, 512, 1, 1]` ×8; `[1280, 2560, 1, 1]` ×5; `[320, 640, 1, 1]` ×2 | F32×28 | FP32×28 |
| [stabilityai/sd-turbo](https://huggingface.co/stabilityai/sd-turbo) | transformer | Other linear | 38 | 0–11 | `[1280, 1280]` ×12; `[320, 1280]` ×10; `[1280, 5120]` ×6 | F32×38 | FP32×38 |
