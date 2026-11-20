# Matrix-multiply flow — MagicQuill

Companion to [`results/pinokio-apps.md`](../results/pinokio-apps.md) and [`analysis/flows.md`](../analysis/flows.md). Interactive viewer: [`MagicQuill.html`](MagicQuill.html).

**Models whose checkpoints were analysed:** [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models)

Reconstructed **1,500 matmul operations** from 1 checkpoint(s) (3 safetensors files).

## How the flow was inferred

The launcher snapshots are wrappers, so the graph is reconstructed from the safetensors header of each checkpoint the launcher downloads. Tensor **names** encode the layer role (Q/K/V, attention out, MLP gate/up/down, conv, head), **shapes** encode the matrix dimensions (PyTorch stores linear weights as `[out_features, in_features]`), and **dtypes** give weight precision. Activation precision is inferred from the weight dtype (quantized weights imply BF16/FP16 compute). `B` is the weight matrix; `A` is the activation `[B, S, in]` and `C` the output `[B, S, out]`. Two extra ops per attention block (Q×Kᵀ and softmax×V) are derived from the Q/K/V triple. This is an inferred dataflow, not a traced execution.

## Flow summary

| Component | Matmul ops | Weight dtypes | Activation dtypes |
| --- | --- | --- | --- |
| transformer | 1,062 | F16 (1062) | FP16 (1062) |
| conditioner | 438 | F16 (432), — (6) | FP16 (438) |

## Representative block sequence — [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models), `transformer`, block 2

This is one coherent pass through a repeated transformer/UNet block; the aggregated roles across every block follow in the next section.

| # | Role | Operation | A (activation) | B (weight) | C (output) | Precision |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Embedding projection | Matmul (linear) | [B, S, 1280] FP16 | [1280, 1280] F16 | [B, S, 1280] FP16 | F16 weights / FP16 activations |
| 2 | Q projection | Matmul (linear) | [B, S, 320] FP16 | [320, 320] F16 | [B, S, 320] FP16 | F16 weights / FP16 activations |
| 3 | K projection | Matmul (linear) | [B, S, 320] FP16 | [320, 320] F16 | [B, S, 320] FP16 | F16 weights / FP16 activations |
| 4 | V projection | Matmul (linear) | [B, S, 320] FP16 | [320, 320] F16 | [B, S, 320] FP16 | F16 weights / FP16 activations |
| 5 | Attention output | Matmul (linear) | [B, S, 320] FP16 | [320, 320] F16 | [B, S, 320] FP16 | F16 weights / FP16 activations |
| 6 | Projection / FFN | Matmul (linear) | [B, S, 320] FP16 | [2560, 320] F16 | [B, S, 2560] FP16 | F16 weights / FP16 activations |
| 7 | Convolution (im2col matmul) | Conv [3, 3] (im2col matmul) | [B, 512, spatial] FP16 | [512, 512, 3, 3] F16 | [B, 512, spatial'] FP16 | F16 weights / FP16 activations |
| 8 | 1×1 conv matmul | Matmul (1x1 conv) | [B, 320, spatial] FP16 | [320, 320, 1, 1] F16 | [B, 320, spatial'] FP16 | F16 weights / FP16 activations |
| 9 | Other linear | Matmul (linear) | [B, S, 1280] FP16 | [320, 1280] F16 | [B, S, 320] FP16 | F16 weights / FP16 activations |

## Aggregated matrix-multiply roles

For every model and component, each role is listed with the number of matching weight tensors, the most common weight shapes, and the weight/activation dtypes.

| Model | Component | Role | Ops | Blocks | Common B shapes | Weight dtypes | Activation dtypes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | conditioner | LoRA down (low-rank) | 72 | 0–11 | `[64, 768] (rank 64)` ×60; `[64, 3072] (rank 64)` ×12 | F16×72 | FP16×72 |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | conditioner | LoRA up (low-rank) | 72 | 0–11 | `[768, 64]` ×60; `[3072, 64]` ×12 | F16×72 | FP16×72 |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | conditioner | Q projection | 48 | 0–11 | `[768, 768]` ×48 | F16×48 | FP16×48 |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | conditioner | K projection | 48 | 0–11 | `[768, 768]` ×48 | F16×48 | FP16×48 |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | conditioner | V projection | 48 | 0–11 | `[768, 768]` ×48 | F16×48 | FP16×48 |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | conditioner | Attention scores (Q×Kᵀ) | 3 | 0 | `[B, H, D, S] (K^T)` ×3 | —×3 | FP16×3 |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | conditioner | Attention context (softmax×V) | 3 | 0 | `[B, H, S, D] (V)` ×3 | —×3 | FP16×3 |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | conditioner | Attention output | 48 | 0–11 | `[768, 768]` ×48 | F16×48 | FP16×48 |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | conditioner | MLP up | 48 | 0–11 | `[3072, 768]` ×48 | F16×48 | FP16×48 |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | conditioner | MLP down | 48 | 0–11 | `[768, 3072]` ×48 | F16×48 | FP16×48 |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | transformer | Embedding projection | 6 | 0–2 | `[1280, 320]` ×3; `[1280, 1280]` ×3 | F16×6 | FP16×6 |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | transformer | Q projection | 96 | 1–11 | `[1280, 1280]` ×36; `[320, 320]` ×30; `[640, 640]` ×30 | F16×96 | FP16×96 |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | transformer | K projection | 96 | 1–11 | `[1280, 1280]` ×18; `[1280, 768]` ×18; `[320, 320]` ×15 | F16×96 | FP16×96 |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | transformer | V projection | 96 | 1–11 | `[1280, 1280]` ×18; `[1280, 768]` ×18; `[320, 320]` ×15 | F16×96 | FP16×96 |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | transformer | Attention output | 96 | 1–11 | `[1280, 1280]` ×36; `[320, 320]` ×30; `[640, 640]` ×30 | F16×96 | FP16×96 |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | transformer | Projection / FFN | 48 | 1–11 | `[10240, 1280]` ×18; `[2560, 320]` ×15; `[5120, 640]` ×15 | F16×48 | FP16×48 |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | transformer | Convolution (im2col matmul) | 330 | 0–11 | `[512, 512, 3, 3]` ×90; `[1280, 1280, 3, 3]` ×60; `[128, 128, 3, 3]` ×30 | F16×330 | FP16×330 |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | transformer | 1×1 conv matmul | 180 | 0–11 | `[1280, 1280, 1, 1]` ×36; `[320, 320, 1, 1]` ×30; `[640, 640, 1, 1]` ×30 | F16×180 | FP16×180 |
| [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) | transformer | Other linear | 114 | 0–11 | `[1280, 1280]` ×36; `[320, 1280]` ×30; `[1280, 5120]` ×18 | F16×114 | FP16×114 |
