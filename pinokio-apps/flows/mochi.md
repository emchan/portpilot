# Matrix-multiply flow — mochi

Companion to [`results/pinokio-apps.md`](../results/pinokio-apps.md) and [`analysis/flows.md`](../analysis/flows.md). Interactive viewer: [`mochi.html`](mochi.html).

**Models whose checkpoints were analysed:** [genmo/mochi-1-preview](https://huggingface.co/genmo/mochi-1-preview)

Reconstructed **606 matmul operations** from 1 checkpoint(s) (3 safetensors files).

## How the flow was inferred

The launcher snapshots are wrappers, so the graph is reconstructed from the safetensors header of each checkpoint the launcher downloads. Tensor **names** encode the layer role (Q/K/V, attention out, MLP gate/up/down, conv, head), **shapes** encode the matrix dimensions (PyTorch stores linear weights as `[out_features, in_features]`), and **dtypes** give weight precision. Activation precision is inferred from the weight dtype (quantized weights imply BF16/FP16 compute). `B` is the weight matrix; `A` is the activation `[B, S, in]` and `C` the output `[B, S, out]`. Two extra ops per attention block (Q×Kᵀ and softmax×V) are derived from the Q/K/V triple. This is an inferred dataflow, not a traced execution.

## Flow summary

| Component | Matmul ops | Weight dtypes | Activation dtypes |
| --- | --- | --- | --- |
| blocks | 519 | F32 (519) | FP32 (519) |
| layers | 74 | F32 (74) | FP32 (74) |
| conditioner | 6 | F32 (4), — (2) | FP32 (6) |
| final_layer | 2 | F32 (2) | FP32 (2) |
| output_proj | 2 | F32 (2) | FP32 (2) |
| t_embedder | 2 | F32 (2) | FP32 (2) |
| x_embedder | 1 | F32 (1) | FP32 (1) |

## Representative block sequence — [genmo/mochi-1-preview](https://huggingface.co/genmo/mochi-1-preview), `blocks`, block -1

This is one coherent pass through a repeated transformer/UNet block; the aggregated roles across every block follow in the next section.

| # | Role | Operation | A (activation) | B (weight) | C (output) | Precision |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 1×1 conv matmul | Matmul (1x1 conv) | [B, 12, spatial] FP32 | [768, 12, 1, 1, 1] F32 | [B, 768, spatial'] FP32 | F32 weights / FP32 activations |
| 2 | Convolution (im2col matmul) | Conv [3, 3, 3] (im2col matmul) | [B, 768, spatial] FP32 | [768, 768, 3, 3, 3] F32 | [B, 768, spatial'] FP32 | F32 weights / FP32 activations |
| 3 | Convolution (im2col matmul) | Conv [3, 3, 3] (im2col matmul) | [B, 768, spatial] FP32 | [768, 768, 3, 3, 3] F32 | [B, 768, spatial'] FP32 | F32 weights / FP32 activations |
| 4 | Convolution (im2col matmul) | Conv [3, 3, 3] (im2col matmul) | [B, 768, spatial] FP32 | [768, 768, 3, 3, 3] F32 | [B, 768, spatial'] FP32 | F32 weights / FP32 activations |
| 5 | Convolution (im2col matmul) | Conv [3, 3, 3] (im2col matmul) | [B, 768, spatial] FP32 | [768, 768, 3, 3, 3] F32 | [B, 768, spatial'] FP32 | F32 weights / FP32 activations |
| 6 | Convolution (im2col matmul) | Conv [3, 3, 3] (im2col matmul) | [B, 768, spatial] FP32 | [768, 768, 3, 3, 3] F32 | [B, 768, spatial'] FP32 | F32 weights / FP32 activations |
| 7 | Convolution (im2col matmul) | Conv [3, 3, 3] (im2col matmul) | [B, 768, spatial] FP32 | [768, 768, 3, 3, 3] F32 | [B, 768, spatial'] FP32 | F32 weights / FP32 activations |
| 8 | Projection / FFN | Matmul (linear) | [B, S, 3072] FP32 | [3072, 3072] F32 | [B, S, 3072] FP32 | F32 weights / FP32 activations |
| 9 | Projection / FFN | Matmul (linear) | [B, S, 3072] FP32 | [1536, 3072] F32 | [B, S, 1536] FP32 | F32 weights / FP32 activations |
| 10 | Other linear | Matmul (linear) | [B, S, 3072] FP32 | [9216, 3072] F32 | [B, S, 9216] FP32 | F32 weights / FP32 activations |

## Aggregated matrix-multiply roles

For every model and component, each role is listed with the number of matching weight tensors, the most common weight shapes, and the weight/activation dtypes.

| Model | Component | Role | Ops | Blocks | Common B shapes | Weight dtypes | Activation dtypes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [genmo/mochi-1-preview](https://huggingface.co/genmo/mochi-1-preview) | blocks | MLP gate | 95 | 0–47 | `[16384, 3072]` ×48; `[8192, 1536]` ×47 | F32×95 | FP32×95 |
| [genmo/mochi-1-preview](https://huggingface.co/genmo/mochi-1-preview) | blocks | Projection / FFN | 193 | 0–47 | `[3072, 3072]` ×48; `[3072, 8192]` ×48; `[1536, 3072]` ×47 | F32×193 | FP32×193 |
| [genmo/mochi-1-preview](https://huggingface.co/genmo/mochi-1-preview) | blocks | Convolution (im2col matmul) | 38 | 0–4 | `[768, 768, 3, 3, 3]` ×18; `[512, 512, 3, 3, 3]` ×8; `[256, 256, 3, 3, 3]` ×6 | F32×38 | FP32×38 |
| [genmo/mochi-1-preview](https://huggingface.co/genmo/mochi-1-preview) | blocks | 1×1 conv matmul | 1 | 0 | `[768, 12, 1, 1, 1]` ×1 | F32×1 | FP32×1 |
| [genmo/mochi-1-preview](https://huggingface.co/genmo/mochi-1-preview) | blocks | Other linear | 192 | 0–47 | `[9216, 3072]` ×48; `[9216, 1536]` ×48; `[12288, 3072]` ×48 | F32×192 | FP32×192 |
| [genmo/mochi-1-preview](https://huggingface.co/genmo/mochi-1-preview) | conditioner | Q projection | 1 | — | `[4096, 4096]` ×1 | F32×1 | FP32×1 |
| [genmo/mochi-1-preview](https://huggingface.co/genmo/mochi-1-preview) | conditioner | K projection | 1 | — | `[8192, 4096]` ×1 | F32×1 | FP32×1 |
| [genmo/mochi-1-preview](https://huggingface.co/genmo/mochi-1-preview) | conditioner | Attention scores (Q×Kᵀ) | 1 | — | `[B, H, D, S] (K^T)` ×1 | —×1 | FP32×1 |
| [genmo/mochi-1-preview](https://huggingface.co/genmo/mochi-1-preview) | conditioner | Attention context (softmax×V) | 1 | — | `[B, H, S, D] (V)` ×1 | —×1 | FP32×1 |
| [genmo/mochi-1-preview](https://huggingface.co/genmo/mochi-1-preview) | conditioner | Attention output | 1 | — | `[3072, 4096]` ×1 | F32×1 | FP32×1 |
| [genmo/mochi-1-preview](https://huggingface.co/genmo/mochi-1-preview) | conditioner | Projection / FFN | 1 | — | `[1536, 4096]` ×1 | F32×1 | FP32×1 |
| [genmo/mochi-1-preview](https://huggingface.co/genmo/mochi-1-preview) | final_layer | Projection / FFN | 1 | — | `[48, 3072]` ×1 | F32×1 | FP32×1 |
| [genmo/mochi-1-preview](https://huggingface.co/genmo/mochi-1-preview) | final_layer | Output head | 1 | — | `[6144, 3072]` ×1 | F32×1 | FP32×1 |
| [genmo/mochi-1-preview](https://huggingface.co/genmo/mochi-1-preview) | layers | Convolution (im2col matmul) | 41 | 1–9 | `[384, 384, 3, 3, 3]` ×18; `[256, 256, 3, 3, 3]` ×8; `[64, 64, 3, 3, 3]` ×6 | F32×41 | FP32×41 |
| [genmo/mochi-1-preview](https://huggingface.co/genmo/mochi-1-preview) | layers | Other linear | 33 | 0–9 | `[384, 384]` ×9; `[1152, 384]` ×9; `[256, 256]` ×4 | F32×33 | FP32×33 |
| [genmo/mochi-1-preview](https://huggingface.co/genmo/mochi-1-preview) | output_proj | Projection / FFN | 2 | — | `[3, 128]` ×1; `[24, 384]` ×1 | F32×2 | FP32×2 |
| [genmo/mochi-1-preview](https://huggingface.co/genmo/mochi-1-preview) | t_embedder | Projection / FFN | 2 | 0–2 | `[3072, 256]` ×1; `[3072, 3072]` ×1 | F32×2 | FP32×2 |
| [genmo/mochi-1-preview](https://huggingface.co/genmo/mochi-1-preview) | x_embedder | Convolution (im2col matmul) | 1 | — | `[3072, 12, 2, 2]` ×1 | F32×1 | FP32×1 |
