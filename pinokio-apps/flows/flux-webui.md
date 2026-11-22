# Matrix-multiply flow — flux-webui

Companion to [`results/pinokio-apps.md`](../results/pinokio-apps.md) and [`analysis/flows.md`](../analysis/flows.md). Interactive viewer: [`flux-webui.html`](flux-webui.html).

**Models whose checkpoints were analysed:** [black-forest-labs/FLUX.1-schnell](https://huggingface.co/black-forest-labs/FLUX.1-schnell), [cocktailpeanut/flux1-merged-q8](https://huggingface.co/cocktailpeanut/flux1-merged-q8), [cocktailpeanut/flux1-merged-qint8](https://huggingface.co/cocktailpeanut/flux1-merged-qint8), [cocktailpeanut/flux1-schnell-q8](https://huggingface.co/cocktailpeanut/flux1-schnell-q8), [cocktailpeanut/flux1-schnell-qint8](https://huggingface.co/cocktailpeanut/flux1-schnell-qint8), [sayakpaul/FLUX.1-merged](https://huggingface.co/sayakpaul/FLUX.1-merged)

Reconstructed **246 matmul operations** from 1 checkpoint(s) (3 safetensors files).

## How the flow was inferred

The launcher snapshots are wrappers, so the graph is reconstructed from the safetensors header of each checkpoint the launcher downloads. Tensor **names** encode the layer role (Q/K/V, attention out, MLP gate/up/down, conv, head), **shapes** encode the matrix dimensions (PyTorch stores linear weights as `[out_features, in_features]`), and **dtypes** give weight precision. Activation precision is inferred from the weight dtype (quantized weights imply BF16/FP16 compute). `B` is the weight matrix; `A` is the activation `[B, S, in]` and `C` the output `[B, S, out]`. Two extra ops per attention block (Q×Kᵀ and softmax×V) are derived from the Q/K/V triple. This is an inferred dataflow, not a traced execution.

## Flow summary

| Component | Matmul ops | Weight dtypes | Activation dtypes |
| --- | --- | --- | --- |
| vae | 172 | BF16 (168), — (4) | BF16 (172) |
| conditioner | 74 | BF16 (72), — (2) | BF16 (74) |

## Representative block sequence — [sayakpaul/FLUX.1-merged](https://huggingface.co/sayakpaul/FLUX.1-merged), `vae`, block 0

This is one coherent pass through a repeated transformer/UNet block; the aggregated roles across every block follow in the next section.

| # | Role | Operation | A (activation) | B (weight) | C (output) | Precision |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Q projection | Matmul (linear) | [B, S, 4096] BF16 | [4096, 4096] BF16 | [B, S, 4096] BF16 | BF16 weights / BF16 activations |
| 2 | K projection | Matmul (linear) | [B, S, 4096] BF16 | [4096, 4096] BF16 | [B, S, 4096] BF16 | BF16 weights / BF16 activations |
| 3 | V projection | Matmul (linear) | [B, S, 4096] BF16 | [4096, 4096] BF16 | [B, S, 4096] BF16 | BF16 weights / BF16 activations |
| 4 | Attention scores (Q×Kᵀ) | Attention scores (Q x K^T) | [B, H, S, D] BF16 | [B, H, D, S] (K^T) BF16 | [B, H, S, S] BF16, FP32 accumulate | — weights / BF16 activations |
| 5 | Attention context (softmax×V) | Attention context (softmax x V) | [B, H, S, S] BF16 | [B, H, S, D] (V) BF16 | [B, H, S, D] BF16 | — weights / BF16 activations |
| 6 | Attention output | Matmul (linear) | [B, S, 4096] BF16 | [4096, 4096] BF16 | [B, S, 4096] BF16 | BF16 weights / BF16 activations |
| 7 | MLP gate | Matmul (linear) | [B, S, 4096] BF16 | [10240, 4096] BF16 | [B, S, 10240] BF16 | BF16 weights / BF16 activations |
| 8 | MLP up | Matmul (linear) | [B, S, 4096] BF16 | [10240, 4096] BF16 | [B, S, 10240] BF16 | BF16 weights / BF16 activations |
| 9 | MLP down | Matmul (linear) | [B, S, 10240] BF16 | [4096, 10240] BF16 | [B, S, 4096] BF16 | BF16 weights / BF16 activations |

## Aggregated matrix-multiply roles

For every model and component, each role is listed with the number of matching weight tensors, the most common weight shapes, and the weight/activation dtypes.

| Model | Component | Role | Ops | Blocks | Common B shapes | Weight dtypes | Activation dtypes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [sayakpaul/FLUX.1-merged](https://huggingface.co/sayakpaul/FLUX.1-merged) | conditioner | Q projection | 12 | 0–11 | `[768, 768]` ×12 | BF16×12 | BF16×12 |
| [sayakpaul/FLUX.1-merged](https://huggingface.co/sayakpaul/FLUX.1-merged) | conditioner | K projection | 12 | 0–11 | `[768, 768]` ×12 | BF16×12 | BF16×12 |
| [sayakpaul/FLUX.1-merged](https://huggingface.co/sayakpaul/FLUX.1-merged) | conditioner | V projection | 12 | 0–11 | `[768, 768]` ×12 | BF16×12 | BF16×12 |
| [sayakpaul/FLUX.1-merged](https://huggingface.co/sayakpaul/FLUX.1-merged) | conditioner | Attention scores (Q×Kᵀ) | 1 | 0 | `[B, H, D, S] (K^T)` ×1 | —×1 | BF16×1 |
| [sayakpaul/FLUX.1-merged](https://huggingface.co/sayakpaul/FLUX.1-merged) | conditioner | Attention context (softmax×V) | 1 | 0 | `[B, H, S, D] (V)` ×1 | —×1 | BF16×1 |
| [sayakpaul/FLUX.1-merged](https://huggingface.co/sayakpaul/FLUX.1-merged) | conditioner | Attention output | 12 | 0–11 | `[768, 768]` ×12 | BF16×12 | BF16×12 |
| [sayakpaul/FLUX.1-merged](https://huggingface.co/sayakpaul/FLUX.1-merged) | conditioner | MLP up | 12 | 0–11 | `[3072, 768]` ×12 | BF16×12 | BF16×12 |
| [sayakpaul/FLUX.1-merged](https://huggingface.co/sayakpaul/FLUX.1-merged) | conditioner | MLP down | 12 | 0–11 | `[768, 3072]` ×12 | BF16×12 | BF16×12 |
| [sayakpaul/FLUX.1-merged](https://huggingface.co/sayakpaul/FLUX.1-merged) | vae | Q projection | 24 | 0–23 | `[4096, 4096]` ×24 | BF16×24 | BF16×24 |
| [sayakpaul/FLUX.1-merged](https://huggingface.co/sayakpaul/FLUX.1-merged) | vae | K projection | 24 | 0–23 | `[4096, 4096]` ×24 | BF16×24 | BF16×24 |
| [sayakpaul/FLUX.1-merged](https://huggingface.co/sayakpaul/FLUX.1-merged) | vae | V projection | 24 | 0–23 | `[4096, 4096]` ×24 | BF16×24 | BF16×24 |
| [sayakpaul/FLUX.1-merged](https://huggingface.co/sayakpaul/FLUX.1-merged) | vae | Attention scores (Q×Kᵀ) | 2 | 0–13 | `[B, H, D, S] (K^T)` ×2 | —×2 | BF16×2 |
| [sayakpaul/FLUX.1-merged](https://huggingface.co/sayakpaul/FLUX.1-merged) | vae | Attention context (softmax×V) | 2 | 0–13 | `[B, H, S, D] (V)` ×2 | —×2 | BF16×2 |
| [sayakpaul/FLUX.1-merged](https://huggingface.co/sayakpaul/FLUX.1-merged) | vae | Attention output | 24 | 0–23 | `[4096, 4096]` ×24 | BF16×24 | BF16×24 |
| [sayakpaul/FLUX.1-merged](https://huggingface.co/sayakpaul/FLUX.1-merged) | vae | MLP gate | 24 | 0–23 | `[10240, 4096]` ×24 | BF16×24 | BF16×24 |
| [sayakpaul/FLUX.1-merged](https://huggingface.co/sayakpaul/FLUX.1-merged) | vae | MLP up | 24 | 0–23 | `[10240, 4096]` ×24 | BF16×24 | BF16×24 |
| [sayakpaul/FLUX.1-merged](https://huggingface.co/sayakpaul/FLUX.1-merged) | vae | MLP down | 24 | 0–23 | `[4096, 10240]` ×24 | BF16×24 | BF16×24 |

## Snapdragon note
- Deep scan: cuda=2, torch=24, triton=3, xformers=4, flashattention=2, sageattention=2, mps=3, directml=1. Contains CUDA/Triton/TensorRT signals; Snapdragon path requires replacement or ONNX conversion.
