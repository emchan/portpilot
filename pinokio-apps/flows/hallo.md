# Matrix-multiply flow — hallo

Companion to [`results/pinokio-apps.md`](../results/pinokio-apps.md) and [`analysis/flows.md`](../analysis/flows.md). Interactive viewer: [`hallo.html`](hallo.html).

**Models whose checkpoints were analysed:** [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo)

Reconstructed **441 matmul operations** from 1 checkpoint(s) (3 safetensors files).

## How the flow was inferred

The launcher snapshots are wrappers, so the graph is reconstructed from the safetensors header of each checkpoint the launcher downloads. Tensor **names** encode the layer role (Q/K/V, attention out, MLP gate/up/down, conv, head), **shapes** encode the matrix dimensions (PyTorch stores linear weights as `[out_features, in_features]`), and **dtypes** give weight precision. Activation precision is inferred from the weight dtype (quantized weights imply BF16/FP16 compute). `B` is the weight matrix; `A` is the activation `[B, S, in]` and `C` the output `[B, S, out]`. Two extra ops per attention block (Q×Kᵀ and softmax×V) are derived from the Q/K/V triple. This is an inferred dataflow, not a traced execution.

## Flow summary

| Component | Matmul ops | Weight dtypes | Activation dtypes |
| --- | --- | --- | --- |
| transformer | 162 | F32 (160), — (2) | FP32 (162) |
| vae | 146 | F32 (142), — (4) | FP32 (146) |
| unet | 118 | F32 (118) | FP32 (118) |
| wav2vec2 | 8 | F32 (8) | FP32 (8) |
| time_embedding | 2 | F32 (2) | FP32 (2) |
| conv_in | 1 | F32 (1) | FP32 (1) |
| conv_out | 1 | F32 (1) | FP32 (1) |
| lm_head | 1 | F32 (1) | FP32 (1) |
| post_quant_conv | 1 | F32 (1) | FP32 (1) |
| quant_conv | 1 | F32 (1) | FP32 (1) |

## Representative block sequence — [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo), `transformer`, block 0

This is one coherent pass through a repeated transformer/UNet block; the aggregated roles across every block follow in the next section.

| # | Role | Operation | A (activation) | B (weight) | C (output) | Precision |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Q projection | Matmul (linear) | [B, S, 320] FP32 | [320, 320] F32 | [B, S, 320] FP32 | F32 weights / FP32 activations |
| 2 | K projection | Matmul (linear) | [B, S, 320] FP32 | [320, 320] F32 | [B, S, 320] FP32 | F32 weights / FP32 activations |
| 3 | V projection | Matmul (linear) | [B, S, 320] FP32 | [320, 320] F32 | [B, S, 320] FP32 | F32 weights / FP32 activations |
| 4 | Attention scores (Q×Kᵀ) | Attention scores (Q x K^T) | [B, H, S, D] FP32 | [B, H, D, S] (K^T) FP32 | [B, H, S, S] FP32, FP32 accumulate | — weights / FP32 activations |
| 5 | Attention context (softmax×V) | Attention context (softmax x V) | [B, H, S, S] FP32 | [B, H, S, D] (V) FP32 | [B, H, S, D] FP32 | — weights / FP32 activations |
| 6 | Attention output | Matmul (linear) | [B, S, 320] FP32 | [320, 320] F32 | [B, S, 320] FP32 | F32 weights / FP32 activations |
| 7 | Projection / FFN | Matmul (linear) | [B, S, 320] FP32 | [2560, 320] F32 | [B, S, 2560] FP32 | F32 weights / FP32 activations |
| 8 | Other linear | Matmul (linear) | [B, S, 1280] FP32 | [320, 1280] F32 | [B, S, 320] FP32 | F32 weights / FP32 activations |

## Aggregated matrix-multiply roles

For every model and component, each role is listed with the number of matching weight tensors, the most common weight shapes, and the weight/activation dtypes.

| Model | Component | Role | Ops | Blocks | Common B shapes | Weight dtypes | Activation dtypes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | conv_in | Convolution (im2col matmul) | 1 | — | `[320, 4, 3, 3]` ×1 | F32×1 | FP32×1 |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | conv_out | Convolution (im2col matmul) | 1 | — | `[4, 320, 3, 3]` ×1 | F32×1 | FP32×1 |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | lm_head | Output head | 1 | — | `[32, 768]` ×1 | F32×1 | FP32×1 |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | post_quant_conv | 1×1 conv matmul | 1 | — | `[4, 4, 1, 1]` ×1 | F32×1 | FP32×1 |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | quant_conv | 1×1 conv matmul | 1 | — | `[8, 8, 1, 1]` ×1 | F32×1 | FP32×1 |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | time_embedding | Projection / FFN | 2 | — | `[1280, 320]` ×1; `[1280, 1280]` ×1 | F32×2 | FP32×2 |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | transformer | Q projection | 32 | 0–3 | `[1280, 1280]` ×12; `[320, 320]` ×10; `[640, 640]` ×10 | F32×32 | FP32×32 |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | transformer | K projection | 32 | 0–3 | `[1280, 1280]` ×6; `[1280, 768]` ×6; `[320, 320]` ×5 | F32×32 | FP32×32 |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | transformer | V projection | 32 | 0–3 | `[1280, 1280]` ×6; `[1280, 768]` ×6; `[320, 320]` ×5 | F32×32 | FP32×32 |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | transformer | Attention scores (Q×Kᵀ) | 1 | 0 | `[B, H, D, S] (K^T)` ×1 | —×1 | FP32×1 |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | transformer | Attention context (softmax×V) | 1 | 0 | `[B, H, S, D] (V)` ×1 | —×1 | FP32×1 |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | transformer | Attention output | 32 | 0–3 | `[1280, 1280]` ×12; `[320, 320]` ×10; `[640, 640]` ×10 | F32×32 | FP32×32 |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | transformer | Projection / FFN | 16 | 0–3 | `[10240, 1280]` ×6; `[2560, 320]` ×5; `[5120, 640]` ×5 | F32×16 | FP32×16 |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | transformer | Other linear | 16 | 0–3 | `[1280, 5120]` ×6; `[320, 1280]` ×5; `[640, 2560]` ×5 | F32×16 | FP32×16 |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | unet | Projection / FFN | 22 | 0–3 | `[1280, 1280]` ×12; `[320, 1280]` ×5; `[640, 1280]` ×5 | F32×22 | FP32×22 |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | unet | Convolution (im2col matmul) | 50 | 0–3 | `[1280, 1280, 3, 3]` ×20; `[320, 320, 3, 3]` ×8; `[640, 640, 3, 3]` ×8 | F32×50 | FP32×50 |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | unet | 1×1 conv matmul | 46 | 0–3 | `[1280, 1280, 1, 1]` ×12; `[320, 320, 1, 1]` ×10; `[640, 640, 1, 1]` ×10 | F32×46 | FP32×46 |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | vae | Q projection | 14 | 0–11 | `[768, 768]` ×12; `[512, 512]` ×2 | F32×14 | FP32×14 |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | vae | K projection | 14 | 0–11 | `[768, 768]` ×12; `[512, 512]` ×2 | F32×14 | FP32×14 |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | vae | V projection | 14 | 0–11 | `[768, 768]` ×12; `[512, 512]` ×2 | F32×14 | FP32×14 |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | vae | Attention scores (Q×Kᵀ) | 2 | 0 | `[B, H, D, S] (K^T)` ×2 | —×2 | FP32×2 |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | vae | Attention context (softmax×V) | 2 | 0 | `[B, H, S, D] (V)` ×2 | —×2 | FP32×2 |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | vae | Attention output | 12 | 0–11 | `[768, 768]` ×12 | F32×12 | FP32×12 |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | vae | Projection / FFN | 26 | 0–11 | `[3072, 768]` ×12; `[768, 3072]` ×12; `[512, 512]` ×2 | F32×26 | FP32×26 |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | vae | Convolution (im2col matmul) | 58 | 0–3 | `[512, 512, 3, 3]` ×30; `[128, 128, 3, 3]` ×10; `[256, 256, 3, 3]` ×10 | F32×58 | FP32×58 |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | vae | 1×1 conv matmul | 4 | 1–3 | `[256, 128, 1, 1]` ×1; `[256, 512, 1, 1]` ×1; `[512, 256, 1, 1]` ×1 | F32×4 | FP32×4 |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | wav2vec2 | Projection / FFN | 1 | — | `[768, 512]` ×1 | F32×1 | FP32×1 |
| [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) | wav2vec2 | Convolution (im2col matmul) | 7 | 0–6 | `[512, 512, 3]` ×4; `[512, 512, 2]` ×2; `[512, 1, 10]` ×1 | F32×7 | FP32×7 |
