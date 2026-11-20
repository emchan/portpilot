# Matrix-multiply flow — forge

Companion to [`results/pinokio-apps.md`](../results/pinokio-apps.md) and [`analysis/flows.md`](../analysis/flows.md). Interactive viewer: [`forge.html`](forge.html).

**Models whose checkpoints were analysed:** [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv), [latent-consistency/lcm-lora-sdxl](https://huggingface.co/latent-consistency/lcm-lora-sdxl), [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5), [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo), [stabilityai/stable-diffusion-2-1](https://huggingface.co/stabilityai/stable-diffusion-2-1), [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0), [stabilityai/stable-diffusion-xl-refiner-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0), [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid), [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt)

Reconstructed **7,236 matmul operations** from 8 checkpoint(s) (8 safetensors files).

## How the flow was inferred

The launcher snapshots are wrappers, so the graph is reconstructed from the safetensors header of each checkpoint the launcher downloads. Tensor **names** encode the layer role (Q/K/V, attention out, MLP gate/up/down, conv, head), **shapes** encode the matrix dimensions (PyTorch stores linear weights as `[out_features, in_features]`), and **dtypes** give weight precision. Activation precision is inferred from the weight dtype (quantized weights imply BF16/FP16 compute). `B` is the weight matrix; `A` is the activation `[B, S, in]` and `C` the output `[B, S, out]`. Two extra ops per attention block (Q×Kᵀ and softmax×V) are derived from the Q/K/V triple. This is an inferred dataflow, not a traced execution.

## Flow summary

| Component | Matmul ops | Weight dtypes | Activation dtypes |
| --- | --- | --- | --- |
| transformer | 6,043 | F16 (4399), F32 (1636), — (8) | FP16 (4403), FP32 (1640) |
| conditioner | 1,017 | F16 (601), F32 (410), — (6) | FP16 (605), FP32 (412) |
| unet | 176 | F16 (176) | FP16 (176) |

## Representative block sequence — [stabilityai/stable-diffusion-xl-refiner-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0), `transformer`, block 4

This is one coherent pass through a repeated transformer/UNet block; the aggregated roles across every block follow in the next section.

| # | Role | Operation | A (activation) | B (weight) | C (output) | Precision |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Q projection | Matmul (linear) | [B, S, 768] FP16 | [768, 768] F16 | [B, S, 768] FP16 | F16 weights / FP16 activations |
| 2 | K projection | Matmul (linear) | [B, S, 768] FP16 | [768, 768] F16 | [B, S, 768] FP16 | F16 weights / FP16 activations |
| 3 | V projection | Matmul (linear) | [B, S, 768] FP16 | [768, 768] F16 | [B, S, 768] FP16 | F16 weights / FP16 activations |
| 4 | Attention scores (Q×Kᵀ) | Attention scores (Q x K^T) | [B, H, S, D] FP16 | [B, H, D, S] (K^T) FP16 | [B, H, S, S] FP16, FP32 accumulate | — weights / FP16 activations |
| 5 | Attention context (softmax×V) | Attention context (softmax x V) | [B, H, S, S] FP16 | [B, H, S, D] (V) FP16 | [B, H, S, D] FP16 | — weights / FP16 activations |
| 6 | Attention output | Matmul (linear) | [B, S, 768] FP16 | [768, 768] F16 | [B, S, 768] FP16 | F16 weights / FP16 activations |
| 7 | Projection / FFN | Matmul (linear) | [B, S, 768] FP16 | [768, 768] F16 | [B, S, 768] FP16 | F16 weights / FP16 activations |
| 8 | Convolution (im2col matmul) | Conv [3, 3] (im2col matmul) | [B, 384, spatial] FP16 | [768, 384, 3, 3] F16 | [B, 768, spatial'] FP16 | F16 weights / FP16 activations |
| 9 | 1×1 conv matmul | Matmul (1x1 conv) | [B, 384, spatial] FP16 | [768, 384, 1, 1] F16 | [B, 768, spatial'] FP16 | F16 weights / FP16 activations |
| 10 | Other linear | Matmul (linear) | [B, S, 1536] FP16 | [768, 1536] F16 | [B, S, 768] FP16 | F16 weights / FP16 activations |

## Aggregated matrix-multiply roles

For every model and component, each role is listed with the number of matching weight tensors, the most common weight shapes, and the weight/activation dtypes.

| Model | Component | Role | Ops | Blocks | Common B shapes | Weight dtypes | Activation dtypes |
| --- | --- | --- | --- | --- | --- | --- | --- |
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
| [latent-consistency/lcm-lora-sdxl](https://huggingface.co/latent-consistency/lcm-lora-sdxl) | transformer | LoRA down (low-rank) | 700 | 0–9 | `[64, 1280] (rank 64)` ×420; `[64, 2048] (rank 64)` ×140; `[64, 640] (rank 64)` ×70 | F16×700 | FP16×700 |
| [latent-consistency/lcm-lora-sdxl](https://huggingface.co/latent-consistency/lcm-lora-sdxl) | transformer | LoRA up (low-rank) | 700 | 0–9 | `[1280, 64]` ×540; `[640, 64]` ×90; `[10240, 64]` ×60 | F16×700 | FP16×700 |
| [latent-consistency/lcm-lora-sdxl](https://huggingface.co/latent-consistency/lcm-lora-sdxl) | unet | LoRA down (low-rank) | 88 | 0–2 | `[64, 1280] (rank 64)` ×42; `[64, 640] (rank 64)` ×24; `[64, 320] (rank 64)` ×10 | F16×88 | FP16×88 |
| [latent-consistency/lcm-lora-sdxl](https://huggingface.co/latent-consistency/lcm-lora-sdxl) | unet | LoRA up (low-rank) | 88 | 0–2 | `[1280, 64]` ×38; `[640, 64]` ×31; `[320, 64]` ×19 | F16×88 | FP16×88 |
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
| [stabilityai/stable-diffusion-xl-refiner-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0) | conditioner | Attention output | 32 | 0–31 | `[1280, 1280]` ×32 | F16×32 | FP16×32 |
| [stabilityai/stable-diffusion-xl-refiner-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0) | conditioner | Projection / FFN | 64 | 0–31 | `[5120, 1280]` ×32; `[1280, 5120]` ×32 | F16×64 | FP16×64 |
| [stabilityai/stable-diffusion-xl-refiner-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0) | transformer | Embedding projection | 2 | 0–2 | `[1536, 384]` ×1; `[1536, 1536]` ×1 | F16×2 | FP16×2 |
| [stabilityai/stable-diffusion-xl-refiner-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0) | transformer | Q projection | 88 | 1–8 | `[1536, 1536]` ×48; `[768, 768]` ×40 | F16×88 | FP16×88 |
| [stabilityai/stable-diffusion-xl-refiner-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0) | transformer | K projection | 88 | 1–8 | `[1536, 1536]` ×24; `[1536, 1280]` ×24; `[768, 768]` ×20 | F16×88 | FP16×88 |
| [stabilityai/stable-diffusion-xl-refiner-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0) | transformer | V projection | 88 | 1–8 | `[1536, 1536]` ×24; `[1536, 1280]` ×24; `[768, 768]` ×20 | F16×88 | FP16×88 |
| [stabilityai/stable-diffusion-xl-refiner-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0) | transformer | Attention scores (Q×Kᵀ) | 1 | 4 | `[B, H, D, S] (K^T)` ×1 | —×1 | FP16×1 |
| [stabilityai/stable-diffusion-xl-refiner-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0) | transformer | Attention context (softmax×V) | 1 | 4 | `[B, H, S, D] (V)` ×1 | —×1 | FP16×1 |
| [stabilityai/stable-diffusion-xl-refiner-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0) | transformer | Attention output | 99 | 1–8 | `[1536, 1536]` ×54; `[768, 768]` ×45 | F16×99 | FP16×99 |
| [stabilityai/stable-diffusion-xl-refiner-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0) | transformer | Projection / FFN | 55 | 1–8 | `[12288, 1536]` ×24; `[6144, 768]` ×20; `[1536, 1536]` ×6 | F16×55 | FP16×55 |
| [stabilityai/stable-diffusion-xl-refiner-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0) | transformer | Convolution (im2col matmul) | 110 | 0–11 | `[512, 512, 3, 3]` ×30; `[1536, 1536, 3, 3]` ×20; `[128, 128, 3, 3]` ×10 | F16×110 | FP16×110 |
| [stabilityai/stable-diffusion-xl-refiner-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0) | transformer | 1×1 conv matmul | 28 | 0–11 | `[512, 512, 1, 1]` ×8; `[1536, 3072, 1, 1]` ×5; `[384, 768, 1, 1]` ×2 | F16×28 | FP16×28 |
| [stabilityai/stable-diffusion-xl-refiner-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0) | transformer | Other linear | 68 | 0–11 | `[1536, 6144]` ×24; `[768, 3072]` ×20; `[1536, 1536]` ×13 | F16×68 | FP16×68 |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | conditioner | Attention output | 32 | 0–31 | `[1280, 1280]` ×32 | F32×32 | FP32×32 |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | conditioner | Projection / FFN | 64 | 0–31 | `[5120, 1280]` ×32; `[1280, 5120]` ×32 | F32×64 | FP32×64 |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | conditioner | Convolution (im2col matmul) | 59 | 0–3 | `[512, 512, 3, 3]` ×30; `[128, 128, 3, 3]` ×10; `[256, 256, 3, 3]` ×10 | F32×59 | FP32×59 |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | conditioner | 1×1 conv matmul | 14 | 0–3 | `[512, 512, 1, 1]` ×8; `[128, 256, 1, 1]` ×1; `[256, 512, 1, 1]` ×1 | F32×14 | FP32×14 |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | transformer | Embedding projection | 2 | 0–2 | `[1280, 320]` ×1; `[1280, 1280]` ×1 | F32×2 | FP32×2 |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | transformer | Q projection | 64 | 1–11 | `[1280, 1280]` ×24; `[320, 320]` ×20; `[640, 640]` ×20 | F32×64 | FP32×64 |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | transformer | K projection | 64 | 1–11 | `[1280, 1280]` ×12; `[1280, 1024]` ×12; `[320, 320]` ×10 | F32×64 | FP32×64 |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | transformer | V projection | 64 | 1–11 | `[1280, 1280]` ×12; `[1280, 1024]` ×12; `[320, 320]` ×10 | F32×64 | FP32×64 |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | transformer | Attention scores (Q×Kᵀ) | 1 | 1 | `[B, H, D, S] (K^T)` ×1 | —×1 | FP32×1 |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | transformer | Attention context (softmax×V) | 1 | 1 | `[B, H, S, D] (V)` ×1 | —×1 | FP32×1 |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | transformer | Attention output | 80 | 1–11 | `[1280, 1280]` ×30; `[320, 320]` ×25; `[640, 640]` ×25 | F32×80 | FP32×80 |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | transformer | Projection / FFN | 64 | 1–11 | `[10240, 1280]` ×18; `[2560, 320]` ×15; `[5120, 640]` ×15 | F32×64 | FP32×64 |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | transformer | Convolution (im2col matmul) | 183 | 0–11 | `[512, 512, 3, 3]` ×30; `[1280, 1280, 3, 1, 1]` ×24; `[1280, 1280, 3, 3]` ×20 | F32×183 | FP32×183 |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | transformer | 1×1 conv matmul | 26 | 0–11 | `[512, 512, 1, 1]` ×8; `[1280, 2560, 1, 1]` ×5; `[320, 640, 1, 1]` ×2 | F32×26 | FP32×26 |
| [stabilityai/stable-video-diffusion-img2vid](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid) | transformer | Other linear | 94 | 0–11 | `[1280, 1280]` ×25; `[320, 1280]` ×25; `[1280, 5120]` ×18 | F32×94 | FP32×94 |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | conditioner | Attention output | 32 | 0–31 | `[1280, 1280]` ×32 | F32×32 | FP32×32 |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | conditioner | Projection / FFN | 64 | 0–31 | `[5120, 1280]` ×32; `[1280, 5120]` ×32 | F32×64 | FP32×64 |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | conditioner | Convolution (im2col matmul) | 59 | 0–3 | `[512, 512, 3, 3]` ×30; `[128, 128, 3, 3]` ×10; `[256, 256, 3, 3]` ×10 | F32×59 | FP32×59 |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | conditioner | 1×1 conv matmul | 14 | 0–3 | `[512, 512, 1, 1]` ×8; `[128, 256, 1, 1]` ×1; `[256, 512, 1, 1]` ×1 | F32×14 | FP32×14 |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | transformer | Embedding projection | 2 | 0–2 | `[1280, 320]` ×1; `[1280, 1280]` ×1 | F32×2 | FP32×2 |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | transformer | Q projection | 64 | 1–11 | `[1280, 1280]` ×24; `[320, 320]` ×20; `[640, 640]` ×20 | F32×64 | FP32×64 |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | transformer | K projection | 64 | 1–11 | `[1280, 1280]` ×12; `[1280, 1024]` ×12; `[320, 320]` ×10 | F32×64 | FP32×64 |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | transformer | V projection | 64 | 1–11 | `[1280, 1280]` ×12; `[1280, 1024]` ×12; `[320, 320]` ×10 | F32×64 | FP32×64 |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | transformer | Attention scores (Q×Kᵀ) | 1 | 1 | `[B, H, D, S] (K^T)` ×1 | —×1 | FP32×1 |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | transformer | Attention context (softmax×V) | 1 | 1 | `[B, H, S, D] (V)` ×1 | —×1 | FP32×1 |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | transformer | Attention output | 80 | 1–11 | `[1280, 1280]` ×30; `[320, 320]` ×25; `[640, 640]` ×25 | F32×80 | FP32×80 |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | transformer | Projection / FFN | 64 | 1–11 | `[10240, 1280]` ×18; `[2560, 320]` ×15; `[5120, 640]` ×15 | F32×64 | FP32×64 |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | transformer | Convolution (im2col matmul) | 183 | 0–11 | `[512, 512, 3, 3]` ×30; `[1280, 1280, 3, 1, 1]` ×24; `[1280, 1280, 3, 3]` ×20 | F32×183 | FP32×183 |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | transformer | 1×1 conv matmul | 26 | 0–11 | `[512, 512, 1, 1]` ×8; `[1280, 2560, 1, 1]` ×5; `[320, 640, 1, 1]` ×2 | F32×26 | FP32×26 |
| [stabilityai/stable-video-diffusion-img2vid-xt](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt) | transformer | Other linear | 94 | 0–11 | `[1280, 1280]` ×25; `[320, 1280]` ×25; `[1280, 5120]` ×18 | F32×94 | FP32×94 |
