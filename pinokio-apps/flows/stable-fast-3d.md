# Matrix-multiply flow — stable-fast-3d

Companion to [`results/pinokio-apps.md`](../results/pinokio-apps.md) and [`analysis/flows.md`](../analysis/flows.md). Interactive viewer: [`stable-fast-3d.html`](stable-fast-3d.html).

**Models whose checkpoints were analysed:** [cocktailpeanut/sf3d](https://huggingface.co/cocktailpeanut/sf3d)

Reconstructed **427 matmul operations** from 1 checkpoint(s) (1 safetensors files).

## How the flow was inferred

The launcher snapshots are wrappers, so the graph is reconstructed from the safetensors header of each checkpoint the launcher downloads. Tensor **names** encode the layer role (Q/K/V, attention out, MLP gate/up/down, conv, head), **shapes** encode the matrix dimensions (PyTorch stores linear weights as `[out_features, in_features]`), and **dtypes** give weight precision. Activation precision is inferred from the weight dtype (quantized weights imply BF16/FP16 compute). `B` is the weight matrix; `A` is the activation `[B, S, in]` and `C` the output `[B, S, out]`. Two extra ops per attention block (Q×Kᵀ and softmax×V) are derived from the Q/K/V triple. This is an inferred dataflow, not a traced execution.

## Flow summary

| Component | Matmul ops | Weight dtypes | Activation dtypes |
| --- | --- | --- | --- |
| transformer | 340 | F32 (338), — (2) | FP32 (340) |
| backbone | 52 | F32 (52) | FP32 (52) |
| image_estimator | 14 | F32 (14) | FP32 (14) |
| vae | 10 | F32 (10) | FP32 (10) |
| global_estimator | 6 | F32 (6) | FP32 (6) |
| post_processor | 4 | F32 (4) | FP32 (4) |
| camera_embedder | 1 | F32 (1) | FP32 (1) |

## Representative block sequence — [cocktailpeanut/sf3d](https://huggingface.co/cocktailpeanut/sf3d), `transformer`, block 0

This is one coherent pass through a repeated transformer/UNet block; the aggregated roles across every block follow in the next section.

| # | Role | Operation | A (activation) | B (weight) | C (output) | Precision |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Q projection | Matmul (linear) | [B, S, 1024] FP32 | [1024, 1024] F32 | [B, S, 1024] FP32 | F32 weights / FP32 activations |
| 2 | K projection | Matmul (linear) | [B, S, 1024] FP32 | [1024, 1024] F32 | [B, S, 1024] FP32 | F32 weights / FP32 activations |
| 3 | V projection | Matmul (linear) | [B, S, 1024] FP32 | [1024, 1024] F32 | [B, S, 1024] FP32 | F32 weights / FP32 activations |
| 4 | Attention scores (Q×Kᵀ) | Attention scores (Q x K^T) | [B, H, S, D] FP32 | [B, H, D, S] (K^T) FP32 | [B, H, S, S] FP32, FP32 accumulate | — weights / FP32 activations |
| 5 | Attention context (softmax×V) | Attention context (softmax x V) | [B, H, S, S] FP32 | [B, H, S, D] (V) FP32 | [B, H, S, D] FP32 | — weights / FP32 activations |
| 6 | Attention output | Matmul (linear) | [B, S, 512] FP32 | [512, 512] F32 | [B, S, 512] FP32 | F32 weights / FP32 activations |
| 7 | MLP up | Matmul (linear) | [B, S, 1024] FP32 | [4096, 1024] F32 | [B, S, 4096] FP32 | F32 weights / FP32 activations |
| 8 | MLP down | Matmul (linear) | [B, S, 4096] FP32 | [1024, 4096] F32 | [B, S, 1024] FP32 | F32 weights / FP32 activations |
| 9 | Projection / FFN | Matmul (linear) | [B, S, 1024] FP32 | [1024, 1024] F32 | [B, S, 1024] FP32 | F32 weights / FP32 activations |
| 10 | Other linear | Matmul (linear) | [B, S, 1024] FP32 | [1024, 1024] F32 | [B, S, 1024] FP32 | F32 weights / FP32 activations |

## Aggregated matrix-multiply roles

For every model and component, each role is listed with the number of matching weight tensors, the most common weight shapes, and the weight/activation dtypes.

| Model | Component | Role | Ops | Blocks | Common B shapes | Weight dtypes | Activation dtypes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [cocktailpeanut/sf3d](https://huggingface.co/cocktailpeanut/sf3d) | backbone | Attention output | 1 | — | `[1024, 1024]` ×1 | F32×1 | FP32×1 |
| [cocktailpeanut/sf3d](https://huggingface.co/cocktailpeanut/sf3d) | backbone | Projection / FFN | 19 | 0–3 | `[1024, 1024]` ×11; `[8192, 1024]` ×8 | F32×19 | FP32×19 |
| [cocktailpeanut/sf3d](https://huggingface.co/cocktailpeanut/sf3d) | backbone | Other linear | 32 | 0–3 | `[1024, 1024]` ×24; `[1024, 4096]` ×8 | F32×32 | FP32×32 |
| [cocktailpeanut/sf3d](https://huggingface.co/cocktailpeanut/sf3d) | camera_embedder | Projection / FFN | 1 | — | `[768, 25]` ×1 | F32×1 | FP32×1 |
| [cocktailpeanut/sf3d](https://huggingface.co/cocktailpeanut/sf3d) | global_estimator | Convolution (im2col matmul) | 2 | 0–2 | `[512, 3072, 3, 3]` ×1; `[512, 512, 3, 3]` ×1 | F32×2 | FP32×2 |
| [cocktailpeanut/sf3d](https://huggingface.co/cocktailpeanut/sf3d) | global_estimator | Other linear | 4 | 0–6 | `[512, 512]` ×3; `[24, 512]` ×1 | F32×4 | FP32×4 |
| [cocktailpeanut/sf3d](https://huggingface.co/cocktailpeanut/sf3d) | image_estimator | Other linear | 14 | 0–2 | `[512, 512]` ×10; `[1, 512]` ×4 | F32×14 | FP32×14 |
| [cocktailpeanut/sf3d](https://huggingface.co/cocktailpeanut/sf3d) | post_processor | Convolution (im2col matmul) | 4 | 0–6 | `[1024, 1024, 3, 3]` ×3; `[640, 1024, 3, 3]` ×1 | F32×4 | FP32×4 |
| [cocktailpeanut/sf3d](https://huggingface.co/cocktailpeanut/sf3d) | transformer | Q projection | 24 | 0–23 | `[1024, 1024]` ×24 | F32×24 | FP32×24 |
| [cocktailpeanut/sf3d](https://huggingface.co/cocktailpeanut/sf3d) | transformer | K projection | 24 | 0–23 | `[1024, 1024]` ×24 | F32×24 | FP32×24 |
| [cocktailpeanut/sf3d](https://huggingface.co/cocktailpeanut/sf3d) | transformer | V projection | 24 | 0–23 | `[1024, 1024]` ×24 | F32×24 | FP32×24 |
| [cocktailpeanut/sf3d](https://huggingface.co/cocktailpeanut/sf3d) | transformer | Attention scores (Q×Kᵀ) | 1 | 0 | `[B, H, D, S] (K^T)` ×1 | —×1 | FP32×1 |
| [cocktailpeanut/sf3d](https://huggingface.co/cocktailpeanut/sf3d) | transformer | Attention context (softmax×V) | 1 | 0 | `[B, H, S, D] (V)` ×1 | —×1 | FP32×1 |
| [cocktailpeanut/sf3d](https://huggingface.co/cocktailpeanut/sf3d) | transformer | Attention output | 24 | 0–11 | `[512, 512]` ×12; `[768, 768]` ×12 | F32×24 | FP32×24 |
| [cocktailpeanut/sf3d](https://huggingface.co/cocktailpeanut/sf3d) | transformer | MLP up | 24 | 0–23 | `[4096, 1024]` ×24 | F32×24 | FP32×24 |
| [cocktailpeanut/sf3d](https://huggingface.co/cocktailpeanut/sf3d) | transformer | MLP down | 24 | 0–23 | `[1024, 4096]` ×24 | F32×24 | FP32×24 |
| [cocktailpeanut/sf3d](https://huggingface.co/cocktailpeanut/sf3d) | transformer | Projection / FFN | 108 | 0–23 | `[1024, 1024]` ×48; `[8192, 1024]` ×12; `[2048, 512]` ×12 | F32×108 | FP32×108 |
| [cocktailpeanut/sf3d](https://huggingface.co/cocktailpeanut/sf3d) | transformer | Convolution (im2col matmul) | 2 | — | `[768, 3, 32, 32]` ×1; `[1024, 3, 14, 14]` ×1 | F32×2 | FP32×2 |
| [cocktailpeanut/sf3d](https://huggingface.co/cocktailpeanut/sf3d) | transformer | Other linear | 84 | 0–3 | `[1024, 1024]` ×72; `[1024, 4096]` ×12 | F32×84 | FP32×84 |
| [cocktailpeanut/sf3d](https://huggingface.co/cocktailpeanut/sf3d) | vae | Other linear | 10 | 0–6 | `[64, 64]` ×4; `[64, 120]` ×3; `[3, 64]` ×2 | F32×10 | FP32×10 |

## Snapdragon note
- Deep scan: torch=10, xformers=3, directml=1. No Python GEMM in wrapper; Snapdragon CPU-ready as launcher/wrapper (no model port).
