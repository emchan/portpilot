# Matrix-multiply flow — z-image-turbo

Companion to [`results/pinokio-apps.md`](../results/pinokio-apps.md) and [`analysis/flows.md`](../analysis/flows.md). Interactive viewer: [`z-image-turbo.html`](z-image-turbo.html).

**Models whose checkpoints were analysed:** [Tongyi-MAI/Z-Image-Turbo](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo)

Reconstructed **256 matmul operations** from 1 checkpoint(s) (3 safetensors files).

## How the flow was inferred

The launcher snapshots are wrappers, so the graph is reconstructed from the safetensors header of each checkpoint the launcher downloads. Tensor **names** encode the layer role (Q/K/V, attention out, MLP gate/up/down, conv, head), **shapes** encode the matrix dimensions (PyTorch stores linear weights as `[out_features, in_features]`), and **dtypes** give weight precision. Activation precision is inferred from the weight dtype (quantized weights imply BF16/FP16 compute). `B` is the weight matrix; `A` is the activation `[B, S, in]` and `C` the output `[B, S, out]`. Two extra ops per attention block (Q×Kᵀ and softmax×V) are derived from the Q/K/V triple. This is an inferred dataflow, not a traced execution.

## Flow summary

| Component | Matmul ops | Weight dtypes | Activation dtypes |
| --- | --- | --- | --- |
| transformer | 256 | BF16 (252), — (4) | BF16 (256) |

## Representative block sequence — [Tongyi-MAI/Z-Image-Turbo](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo), `transformer`, block 0

This is one coherent pass through a repeated transformer/UNet block; the aggregated roles across every block follow in the next section.

| # | Role | Operation | A (activation) | B (weight) | C (output) | Precision |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Q projection | Matmul (linear) | [B, S, 2560] BF16 | [4096, 2560] BF16 | [B, S, 4096] BF16 | BF16 weights / BF16 activations |
| 2 | K projection | Matmul (linear) | [B, S, 2560] BF16 | [1024, 2560] BF16 | [B, S, 1024] BF16 | BF16 weights / BF16 activations |
| 3 | V projection | Matmul (linear) | [B, S, 2560] BF16 | [1024, 2560] BF16 | [B, S, 1024] BF16 | BF16 weights / BF16 activations |
| 4 | Attention scores (Q×Kᵀ) | Attention scores (Q x K^T) | [B, H, S, D] BF16 | [B, H, D, S] (K^T) BF16 | [B, H, S, S] BF16, FP32 accumulate | — weights / BF16 activations |
| 5 | Attention context (softmax×V) | Attention context (softmax x V) | [B, H, S, S] BF16 | [B, H, S, D] (V) BF16 | [B, H, S, D] BF16 | — weights / BF16 activations |
| 6 | MLP gate | Matmul (linear) | [B, S, 2560] BF16 | [9728, 2560] BF16 | [B, S, 9728] BF16 | BF16 weights / BF16 activations |
| 7 | MLP up | Matmul (linear) | [B, S, 2560] BF16 | [9728, 2560] BF16 | [B, S, 9728] BF16 | BF16 weights / BF16 activations |
| 8 | MLP down | Matmul (linear) | [B, S, 9728] BF16 | [2560, 9728] BF16 | [B, S, 2560] BF16 | BF16 weights / BF16 activations |
| 9 | Projection / FFN | Matmul (linear) | [B, S, 4096] BF16 | [2560, 4096] BF16 | [B, S, 2560] BF16 | BF16 weights / BF16 activations |

## Aggregated matrix-multiply roles

For every model and component, each role is listed with the number of matching weight tensors, the most common weight shapes, and the weight/activation dtypes.

| Model | Component | Role | Ops | Blocks | Common B shapes | Weight dtypes | Activation dtypes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Tongyi-MAI/Z-Image-Turbo](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo) | transformer | Q projection | 36 | 0–35 | `[4096, 2560]` ×36 | BF16×36 | BF16×36 |
| [Tongyi-MAI/Z-Image-Turbo](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo) | transformer | K projection | 36 | 0–35 | `[1024, 2560]` ×36 | BF16×36 | BF16×36 |
| [Tongyi-MAI/Z-Image-Turbo](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo) | transformer | V projection | 36 | 0–35 | `[1024, 2560]` ×36 | BF16×36 | BF16×36 |
| [Tongyi-MAI/Z-Image-Turbo](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo) | transformer | Attention scores (Q×Kᵀ) | 2 | 0–16 | `[B, H, D, S] (K^T)` ×2 | —×2 | BF16×2 |
| [Tongyi-MAI/Z-Image-Turbo](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo) | transformer | Attention context (softmax×V) | 2 | 0–16 | `[B, H, S, D] (V)` ×2 | —×2 | BF16×2 |
| [Tongyi-MAI/Z-Image-Turbo](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo) | transformer | MLP gate | 36 | 0–35 | `[9728, 2560]` ×36 | BF16×36 | BF16×36 |
| [Tongyi-MAI/Z-Image-Turbo](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo) | transformer | MLP up | 36 | 0–35 | `[9728, 2560]` ×36 | BF16×36 | BF16×36 |
| [Tongyi-MAI/Z-Image-Turbo](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo) | transformer | MLP down | 36 | 0–35 | `[2560, 9728]` ×36 | BF16×36 | BF16×36 |
| [Tongyi-MAI/Z-Image-Turbo](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo) | transformer | Projection / FFN | 36 | 0–35 | `[2560, 4096]` ×36 | BF16×36 | BF16×36 |
