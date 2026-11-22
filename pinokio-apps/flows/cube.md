# Matrix-multiply flow — cube

Companion to [`results/pinokio-apps.md`](../results/pinokio-apps.md) and [`analysis/flows.md`](../analysis/flows.md). Interactive viewer: [`cube.html`](cube.html).

**Models whose checkpoints were analysed:** [Roblox/cube3d-v0.1](https://huggingface.co/Roblox/cube3d-v0.1)

Reconstructed **488 matmul operations** from 1 checkpoint(s) (2 safetensors files).

## How the flow was inferred

The launcher snapshots are wrappers, so the graph is reconstructed from the safetensors header of each checkpoint the launcher downloads. Tensor **names** encode the layer role (Q/K/V, attention out, MLP gate/up/down, conv, head), **shapes** encode the matrix dimensions (PyTorch stores linear weights as `[out_features, in_features]`), and **dtypes** give weight precision. Activation precision is inferred from the weight dtype (quantized weights imply BF16/FP16 compute). `B` is the weight matrix; `A` is the activation `[B, S, in]` and `C` the output `[B, S, out]`. Two extra ops per attention block (Q×Kᵀ and softmax×V) are derived from the Q/K/V triple. This is an inferred dataflow, not a traced execution.

## Flow summary

| Component | Matmul ops | Weight dtypes | Activation dtypes |
| --- | --- | --- | --- |
| transformer | 278 | F32 (278) | FP32 (278) |
| vae | 202 | F32 (200), — (2) | FP32 (202) |
| bottleneck | 4 | F32 (4) | FP32 (4) |
| embedder | 1 | F32 (1) | FP32 (1) |
| lm_head | 1 | F32 (1) | FP32 (1) |
| shape_proj | 1 | F32 (1) | FP32 (1) |
| text_proj | 1 | F32 (1) | FP32 (1) |

## Representative block sequence — [Roblox/cube3d-v0.1](https://huggingface.co/Roblox/cube3d-v0.1), `vae`, block 0

This is one coherent pass through a repeated transformer/UNet block; the aggregated roles across every block follow in the next section.

| # | Role | Operation | A (activation) | B (weight) | C (output) | Precision |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Q projection | Matmul (linear) | [B, S, 768] FP32 | [768, 768] F32 | [B, S, 768] FP32 | F32 weights / FP32 activations |
| 2 | K projection | Matmul (linear) | [B, S, 768] FP32 | [768, 768] F32 | [B, S, 768] FP32 | F32 weights / FP32 activations |
| 3 | V projection | Matmul (linear) | [B, S, 768] FP32 | [768, 768] F32 | [B, S, 768] FP32 | F32 weights / FP32 activations |
| 4 | Attention scores (Q×Kᵀ) | Attention scores (Q x K^T) | [B, H, S, D] FP32 | [B, H, D, S] (K^T) FP32 | [B, H, S, S] FP32, FP32 accumulate | — weights / FP32 activations |
| 5 | Attention context (softmax×V) | Attention context (softmax x V) | [B, H, S, S] FP32 | [B, H, S, D] (V) FP32 | [B, H, S, D] FP32 | — weights / FP32 activations |
| 6 | MLP up | Matmul (linear) | [B, S, 768] FP32 | [3072, 768] F32 | [B, S, 3072] FP32 | F32 weights / FP32 activations |
| 7 | MLP down | Matmul (linear) | [B, S, 3072] FP32 | [768, 3072] F32 | [B, S, 768] FP32 | F32 weights / FP32 activations |
| 8 | Projection / FFN | Matmul (linear) | [B, S, 768] FP32 | [768, 768] F32 | [B, S, 768] FP32 | F32 weights / FP32 activations |
| 9 | Other linear | Matmul (linear) | [B, S, 768] FP32 | [1536, 768] F32 | [B, S, 1536] FP32 | F32 weights / FP32 activations |

## Aggregated matrix-multiply roles

For every model and component, each role is listed with the number of matching weight tensors, the most common weight shapes, and the weight/activation dtypes.

| Model | Component | Role | Ops | Blocks | Common B shapes | Weight dtypes | Activation dtypes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Roblox/cube3d-v0.1](https://huggingface.co/Roblox/cube3d-v0.1) | bottleneck | Other linear | 4 | — | `[32, 768]` ×2; `[768, 32]` ×1; `[16384, 32]` ×1 | F32×4 | FP32×4 |
| [Roblox/cube3d-v0.1](https://huggingface.co/Roblox/cube3d-v0.1) | embedder | Embedding projection | 1 | — | `[3, 128]` ×1 | F32×1 | FP32×1 |
| [Roblox/cube3d-v0.1](https://huggingface.co/Roblox/cube3d-v0.1) | lm_head | Output head | 1 | — | `[16387, 1536]` ×1 | F32×1 | FP32×1 |
| [Roblox/cube3d-v0.1](https://huggingface.co/Roblox/cube3d-v0.1) | shape_proj | Projection / FFN | 1 | — | `[1536, 32]` ×1 | F32×1 | FP32×1 |
| [Roblox/cube3d-v0.1](https://huggingface.co/Roblox/cube3d-v0.1) | text_proj | Projection / FFN | 1 | — | `[1536, 768]` ×1 | F32×1 | FP32×1 |
| [Roblox/cube3d-v0.1](https://huggingface.co/Roblox/cube3d-v0.1) | transformer | K projection | 1 | 22 | `[1536, 1536]` ×1 | F32×1 | FP32×1 |
| [Roblox/cube3d-v0.1](https://huggingface.co/Roblox/cube3d-v0.1) | transformer | V projection | 47 | 0–22 | `[1536, 1536]` ×47 | F32×47 | FP32×47 |
| [Roblox/cube3d-v0.1](https://huggingface.co/Roblox/cube3d-v0.1) | transformer | MLP gate | 46 | 0–22 | `[6144, 1536]` ×46 | F32×46 | FP32×46 |
| [Roblox/cube3d-v0.1](https://huggingface.co/Roblox/cube3d-v0.1) | transformer | MLP up | 46 | 0–22 | `[6144, 1536]` ×46 | F32×46 | FP32×46 |
| [Roblox/cube3d-v0.1](https://huggingface.co/Roblox/cube3d-v0.1) | transformer | MLP down | 46 | 0–22 | `[1536, 6144]` ×46 | F32×46 | FP32×46 |
| [Roblox/cube3d-v0.1](https://huggingface.co/Roblox/cube3d-v0.1) | transformer | Projection / FFN | 46 | 0–22 | `[1536, 1536]` ×46 | F32×46 | FP32×46 |
| [Roblox/cube3d-v0.1](https://huggingface.co/Roblox/cube3d-v0.1) | transformer | Other linear | 46 | 0–22 | `[3072, 1536]` ×46 | F32×46 | FP32×46 |
| [Roblox/cube3d-v0.1](https://huggingface.co/Roblox/cube3d-v0.1) | vae | Q projection | 5 | 0–8 | `[768, 768]` ×5 | F32×5 | FP32×5 |
| [Roblox/cube3d-v0.1](https://huggingface.co/Roblox/cube3d-v0.1) | vae | K projection | 5 | 0–8 | `[768, 768]` ×5 | F32×5 | FP32×5 |
| [Roblox/cube3d-v0.1](https://huggingface.co/Roblox/cube3d-v0.1) | vae | V projection | 38 | 0–23 | `[768, 768]` ×38 | F32×38 | FP32×38 |
| [Roblox/cube3d-v0.1](https://huggingface.co/Roblox/cube3d-v0.1) | vae | Attention scores (Q×Kᵀ) | 1 | 0 | `[B, H, D, S] (K^T)` ×1 | —×1 | FP32×1 |
| [Roblox/cube3d-v0.1](https://huggingface.co/Roblox/cube3d-v0.1) | vae | Attention context (softmax×V) | 1 | 0 | `[B, H, S, D] (V)` ×1 | —×1 | FP32×1 |
| [Roblox/cube3d-v0.1](https://huggingface.co/Roblox/cube3d-v0.1) | vae | Attention output | 3 | — | `[768, 768]` ×1; `[768, 3072]` ×1; `[3072, 768]` ×1 | F32×3 | FP32×3 |
| [Roblox/cube3d-v0.1](https://huggingface.co/Roblox/cube3d-v0.1) | vae | MLP up | 37 | 0–23 | `[3072, 768]` ×37 | F32×37 | FP32×37 |
| [Roblox/cube3d-v0.1](https://huggingface.co/Roblox/cube3d-v0.1) | vae | MLP down | 37 | 0–23 | `[768, 3072]` ×37 | F32×37 | FP32×37 |
| [Roblox/cube3d-v0.1](https://huggingface.co/Roblox/cube3d-v0.1) | vae | Projection / FFN | 37 | 0–23 | `[768, 768]` ×37 | F32×37 | FP32×37 |
| [Roblox/cube3d-v0.1](https://huggingface.co/Roblox/cube3d-v0.1) | vae | Output head | 1 | — | `[1, 768]` ×1 | F32×1 | FP32×1 |
| [Roblox/cube3d-v0.1](https://huggingface.co/Roblox/cube3d-v0.1) | vae | Other linear | 37 | 0–23 | `[1536, 768]` ×33; `[768, 768]` ×2; `[768, 774]` ×1 | F32×37 | FP32×37 |

## Snapdragon note
- Deep scan: torch=9, xformers=3, directml=1. No Python GEMM in wrapper; Snapdragon CPU-ready as launcher/wrapper (no model port).
