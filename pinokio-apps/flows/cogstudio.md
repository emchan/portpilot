# Matrix-multiply flow — cogstudio

Companion to [`results/pinokio-apps.md`](../results/pinokio-apps.md) and [`analysis/flows.md`](../analysis/flows.md). Interactive viewer: [`cogstudio.html`](cogstudio.html).

**Models whose checkpoints were analysed:** [AlexWortega/RIFE](https://huggingface.co/AlexWortega/RIFE), [THUDM/CogVideoX-2B](https://huggingface.co/THUDM/CogVideoX-2B), [THUDM/CogVideoX-5b-I2V](https://huggingface.co/THUDM/CogVideoX-5b-I2V), [ai-forever/Real-ESRGAN](https://huggingface.co/ai-forever/Real-ESRGAN)

Reconstructed **649 matmul operations** from 2 checkpoint(s) (4 safetensors files).

## How the flow was inferred

The launcher snapshots are wrappers, so the graph is reconstructed from the safetensors header of each checkpoint the launcher downloads. Tensor **names** encode the layer role (Q/K/V, attention out, MLP gate/up/down, conv, head), **shapes** encode the matrix dimensions (PyTorch stores linear weights as `[out_features, in_features]`), and **dtypes** give weight precision. Activation precision is inferred from the weight dtype (quantized weights imply BF16/FP16 compute). `B` is the weight matrix; `A` is the activation `[B, S, in]` and `C` the output `[B, S, out]`. Two extra ops per attention block (Q×Kᵀ and softmax×V) are derived from the Q/K/V triple. This is an inferred dataflow, not a traced execution.

## Flow summary

| Component | Matmul ops | Weight dtypes | Activation dtypes |
| --- | --- | --- | --- |
| vae | 344 | F16 (168), BF16 (168), — (8) | FP16 (172), BF16 (172) |
| transformer | 296 | F16 (180), BF16 (112), — (4) | FP16 (182), BF16 (114) |
| patch_embed | 4 | F16 (2), BF16 (2) | FP16 (2), BF16 (2) |
| time_embedding | 4 | F16 (2), BF16 (2) | FP16 (2), BF16 (2) |
| proj_out | 1 | F16 (1) | FP16 (1) |

## Representative block sequence — [THUDM/CogVideoX-5b-I2V](https://huggingface.co/THUDM/CogVideoX-5b-I2V), `vae`, block 0

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
| [THUDM/CogVideoX-2B](https://huggingface.co/THUDM/CogVideoX-2B) | patch_embed | Projection / FFN | 1 | — | `[1920, 4096]` ×1 | F16×1 | FP16×1 |
| [THUDM/CogVideoX-2B](https://huggingface.co/THUDM/CogVideoX-2B) | patch_embed | Convolution (im2col matmul) | 1 | — | `[1920, 16, 2, 2]` ×1 | F16×1 | FP16×1 |
| [THUDM/CogVideoX-2B](https://huggingface.co/THUDM/CogVideoX-2B) | proj_out | Attention output | 1 | — | `[64, 1920]` ×1 | F16×1 | FP16×1 |
| [THUDM/CogVideoX-2B](https://huggingface.co/THUDM/CogVideoX-2B) | time_embedding | Projection / FFN | 2 | — | `[512, 1920]` ×1; `[512, 512]` ×1 | F16×2 | FP16×2 |
| [THUDM/CogVideoX-2B](https://huggingface.co/THUDM/CogVideoX-2B) | transformer | Q projection | 30 | 0–29 | `[1920, 1920]` ×30 | F16×30 | FP16×30 |
| [THUDM/CogVideoX-2B](https://huggingface.co/THUDM/CogVideoX-2B) | transformer | K projection | 30 | 0–29 | `[1920, 1920]` ×30 | F16×30 | FP16×30 |
| [THUDM/CogVideoX-2B](https://huggingface.co/THUDM/CogVideoX-2B) | transformer | V projection | 30 | 0–29 | `[1920, 1920]` ×30 | F16×30 | FP16×30 |
| [THUDM/CogVideoX-2B](https://huggingface.co/THUDM/CogVideoX-2B) | transformer | Attention scores (Q×Kᵀ) | 1 | 0 | `[B, H, D, S] (K^T)` ×1 | —×1 | FP16×1 |
| [THUDM/CogVideoX-2B](https://huggingface.co/THUDM/CogVideoX-2B) | transformer | Attention context (softmax×V) | 1 | 0 | `[B, H, S, D] (V)` ×1 | —×1 | FP16×1 |
| [THUDM/CogVideoX-2B](https://huggingface.co/THUDM/CogVideoX-2B) | transformer | Attention output | 30 | 0–29 | `[1920, 1920]` ×30 | F16×30 | FP16×30 |
| [THUDM/CogVideoX-2B](https://huggingface.co/THUDM/CogVideoX-2B) | transformer | Projection / FFN | 30 | 0–29 | `[7680, 1920]` ×30 | F16×30 | FP16×30 |
| [THUDM/CogVideoX-2B](https://huggingface.co/THUDM/CogVideoX-2B) | transformer | Other linear | 30 | 0–29 | `[1920, 7680]` ×30 | F16×30 | FP16×30 |
| [THUDM/CogVideoX-2B](https://huggingface.co/THUDM/CogVideoX-2B) | vae | Q projection | 24 | 0–23 | `[4096, 4096]` ×24 | F16×24 | FP16×24 |
| [THUDM/CogVideoX-2B](https://huggingface.co/THUDM/CogVideoX-2B) | vae | K projection | 24 | 0–23 | `[4096, 4096]` ×24 | F16×24 | FP16×24 |
| [THUDM/CogVideoX-2B](https://huggingface.co/THUDM/CogVideoX-2B) | vae | V projection | 24 | 0–23 | `[4096, 4096]` ×24 | F16×24 | FP16×24 |
| [THUDM/CogVideoX-2B](https://huggingface.co/THUDM/CogVideoX-2B) | vae | Attention scores (Q×Kᵀ) | 2 | 0–13 | `[B, H, D, S] (K^T)` ×2 | —×2 | FP16×2 |
| [THUDM/CogVideoX-2B](https://huggingface.co/THUDM/CogVideoX-2B) | vae | Attention context (softmax×V) | 2 | 0–13 | `[B, H, S, D] (V)` ×2 | —×2 | FP16×2 |
| [THUDM/CogVideoX-2B](https://huggingface.co/THUDM/CogVideoX-2B) | vae | Attention output | 24 | 0–23 | `[4096, 4096]` ×24 | F16×24 | FP16×24 |
| [THUDM/CogVideoX-2B](https://huggingface.co/THUDM/CogVideoX-2B) | vae | MLP gate | 24 | 0–23 | `[10240, 4096]` ×24 | F16×24 | FP16×24 |
| [THUDM/CogVideoX-2B](https://huggingface.co/THUDM/CogVideoX-2B) | vae | MLP up | 24 | 0–23 | `[10240, 4096]` ×24 | F16×24 | FP16×24 |
| [THUDM/CogVideoX-2B](https://huggingface.co/THUDM/CogVideoX-2B) | vae | MLP down | 24 | 0–23 | `[4096, 10240]` ×24 | F16×24 | FP16×24 |
| [THUDM/CogVideoX-5b-I2V](https://huggingface.co/THUDM/CogVideoX-5b-I2V) | patch_embed | Projection / FFN | 1 | — | `[3072, 4096]` ×1 | BF16×1 | BF16×1 |
| [THUDM/CogVideoX-5b-I2V](https://huggingface.co/THUDM/CogVideoX-5b-I2V) | patch_embed | Convolution (im2col matmul) | 1 | — | `[3072, 32, 2, 2]` ×1 | BF16×1 | BF16×1 |
| [THUDM/CogVideoX-5b-I2V](https://huggingface.co/THUDM/CogVideoX-5b-I2V) | time_embedding | Projection / FFN | 2 | — | `[512, 3072]` ×1; `[512, 512]` ×1 | BF16×2 | BF16×2 |
| [THUDM/CogVideoX-5b-I2V](https://huggingface.co/THUDM/CogVideoX-5b-I2V) | transformer | Q projection | 19 | 0–18 | `[3072, 3072]` ×19 | BF16×19 | BF16×19 |
| [THUDM/CogVideoX-5b-I2V](https://huggingface.co/THUDM/CogVideoX-5b-I2V) | transformer | K projection | 19 | 0–18 | `[3072, 3072]` ×19 | BF16×19 | BF16×19 |
| [THUDM/CogVideoX-5b-I2V](https://huggingface.co/THUDM/CogVideoX-5b-I2V) | transformer | V projection | 19 | 0–18 | `[3072, 3072]` ×19 | BF16×19 | BF16×19 |
| [THUDM/CogVideoX-5b-I2V](https://huggingface.co/THUDM/CogVideoX-5b-I2V) | transformer | Attention scores (Q×Kᵀ) | 1 | 0 | `[B, H, D, S] (K^T)` ×1 | —×1 | BF16×1 |
| [THUDM/CogVideoX-5b-I2V](https://huggingface.co/THUDM/CogVideoX-5b-I2V) | transformer | Attention context (softmax×V) | 1 | 0 | `[B, H, S, D] (V)` ×1 | —×1 | BF16×1 |
| [THUDM/CogVideoX-5b-I2V](https://huggingface.co/THUDM/CogVideoX-5b-I2V) | transformer | Attention output | 19 | 0–18 | `[3072, 3072]` ×19 | BF16×19 | BF16×19 |
| [THUDM/CogVideoX-5b-I2V](https://huggingface.co/THUDM/CogVideoX-5b-I2V) | transformer | Projection / FFN | 18 | 0–17 | `[12288, 3072]` ×18 | BF16×18 | BF16×18 |
| [THUDM/CogVideoX-5b-I2V](https://huggingface.co/THUDM/CogVideoX-5b-I2V) | transformer | Other linear | 18 | 0–17 | `[3072, 12288]` ×18 | BF16×18 | BF16×18 |
| [THUDM/CogVideoX-5b-I2V](https://huggingface.co/THUDM/CogVideoX-5b-I2V) | vae | Q projection | 24 | 0–23 | `[4096, 4096]` ×24 | BF16×24 | BF16×24 |
| [THUDM/CogVideoX-5b-I2V](https://huggingface.co/THUDM/CogVideoX-5b-I2V) | vae | K projection | 24 | 0–23 | `[4096, 4096]` ×24 | BF16×24 | BF16×24 |
| [THUDM/CogVideoX-5b-I2V](https://huggingface.co/THUDM/CogVideoX-5b-I2V) | vae | V projection | 24 | 0–23 | `[4096, 4096]` ×24 | BF16×24 | BF16×24 |
| [THUDM/CogVideoX-5b-I2V](https://huggingface.co/THUDM/CogVideoX-5b-I2V) | vae | Attention scores (Q×Kᵀ) | 2 | 0–13 | `[B, H, D, S] (K^T)` ×2 | —×2 | BF16×2 |
| [THUDM/CogVideoX-5b-I2V](https://huggingface.co/THUDM/CogVideoX-5b-I2V) | vae | Attention context (softmax×V) | 2 | 0–13 | `[B, H, S, D] (V)` ×2 | —×2 | BF16×2 |
| [THUDM/CogVideoX-5b-I2V](https://huggingface.co/THUDM/CogVideoX-5b-I2V) | vae | Attention output | 24 | 0–23 | `[4096, 4096]` ×24 | BF16×24 | BF16×24 |
| [THUDM/CogVideoX-5b-I2V](https://huggingface.co/THUDM/CogVideoX-5b-I2V) | vae | MLP gate | 24 | 0–23 | `[10240, 4096]` ×24 | BF16×24 | BF16×24 |
| [THUDM/CogVideoX-5b-I2V](https://huggingface.co/THUDM/CogVideoX-5b-I2V) | vae | MLP up | 24 | 0–23 | `[10240, 4096]` ×24 | BF16×24 | BF16×24 |
| [THUDM/CogVideoX-5b-I2V](https://huggingface.co/THUDM/CogVideoX-5b-I2V) | vae | MLP down | 24 | 0–23 | `[4096, 10240]` ×24 | BF16×24 | BF16×24 |

## Snapdragon note
- Deep scan: cuda=7, torch=27, xformers=3, mps=1. Contains CUDA/Triton/TensorRT signals; Snapdragon path requires replacement or ONNX conversion.
