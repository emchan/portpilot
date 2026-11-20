# Matrix-multiply flow — omniparser

Companion to [`results/pinokio-apps.md`](../results/pinokio-apps.md) and [`analysis/flows.md`](../analysis/flows.md). Interactive viewer: [`omniparser.html`](omniparser.html).

**Models whose checkpoints were analysed:** [microsoft/OmniParser](https://huggingface.co/microsoft/OmniParser)

Reconstructed **313 matmul operations** from 1 checkpoint(s) (2 safetensors files).

## How the flow was inferred

The launcher snapshots are wrappers, so the graph is reconstructed from the safetensors header of each checkpoint the launcher downloads. Tensor **names** encode the layer role (Q/K/V, attention out, MLP gate/up/down, conv, head), **shapes** encode the matrix dimensions (PyTorch stores linear weights as `[out_features, in_features]`), and **dtypes** give weight precision. Activation precision is inferred from the weight dtype (quantized weights imply BF16/FP16 compute). `B` is the weight matrix; `A` is the activation `[B, S, in]` and `C` the output `[B, S, out]`. Two extra ops per attention block (Q×Kᵀ and softmax×V) are derived from the Q/K/V triple. This is an inferred dataflow, not a traced execution.

## Flow summary

| Component | Matmul ops | Weight dtypes | Activation dtypes |
| --- | --- | --- | --- |
| transformer | 165 | F32 (99), F16 (64), — (2) | FP32 (101), FP16 (64) |
| vision_tower | 148 | F32 (148) | FP32 (148) |

## Representative block sequence — [microsoft/OmniParser](https://huggingface.co/microsoft/OmniParser), `transformer`, block 0

This is one coherent pass through a repeated transformer/UNet block; the aggregated roles across every block follow in the next section.

| # | Role | Operation | A (activation) | B (weight) | C (output) | Precision |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Q projection | Matmul (linear) | [B, S, 768] FP32 | [768, 768] F32 | [B, S, 768] FP32 | F32 weights / FP32 activations |
| 2 | K projection | Matmul (linear) | [B, S, 768] FP32 | [768, 768] F32 | [B, S, 768] FP32 | F32 weights / FP32 activations |
| 3 | V projection | Matmul (linear) | [B, S, 768] FP32 | [768, 768] F32 | [B, S, 768] FP32 | F32 weights / FP32 activations |
| 4 | Attention scores (Q×Kᵀ) | Attention scores (Q x K^T) | [B, H, S, D] FP32 | [B, H, D, S] (K^T) FP32 | [B, H, S, S] FP32, FP32 accumulate | — weights / FP32 activations |
| 5 | Attention context (softmax×V) | Attention context (softmax x V) | [B, H, S, S] FP32 | [B, H, S, D] (V) FP32 | [B, H, S, D] FP32 | — weights / FP32 activations |
| 6 | Attention output | Matmul (linear) | [B, S, 768] FP32 | [768, 768] F32 | [B, S, 768] FP32 | F32 weights / FP32 activations |
| 7 | Projection / FFN | Matmul (linear) | [B, S, 768] FP32 | [3072, 768] F32 | [B, S, 3072] FP32 | F32 weights / FP32 activations |
| 8 | Convolution (im2col matmul) | Conv [3, 3] (im2col matmul) | [B, 3, spatial] FP16 | [16, 3, 3, 3] F16 | [B, 16, spatial'] FP16 | F16 weights / FP16 activations |

## Aggregated matrix-multiply roles

For every model and component, each role is listed with the number of matching weight tensors, the most common weight shapes, and the weight/activation dtypes.

| Model | Component | Role | Ops | Blocks | Common B shapes | Weight dtypes | Activation dtypes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [microsoft/OmniParser](https://huggingface.co/microsoft/OmniParser) | transformer | Embedding projection | 2 | — | `[1026, 768]` ×2 | F32×2 | FP32×2 |
| [microsoft/OmniParser](https://huggingface.co/microsoft/OmniParser) | transformer | Q projection | 18 | 0–5 | `[768, 768]` ×18 | F32×18 | FP32×18 |
| [microsoft/OmniParser](https://huggingface.co/microsoft/OmniParser) | transformer | K projection | 18 | 0–5 | `[768, 768]` ×18 | F32×18 | FP32×18 |
| [microsoft/OmniParser](https://huggingface.co/microsoft/OmniParser) | transformer | V projection | 18 | 0–5 | `[768, 768]` ×18 | F32×18 | FP32×18 |
| [microsoft/OmniParser](https://huggingface.co/microsoft/OmniParser) | transformer | Attention scores (Q×Kᵀ) | 1 | 0 | `[B, H, D, S] (K^T)` ×1 | —×1 | FP32×1 |
| [microsoft/OmniParser](https://huggingface.co/microsoft/OmniParser) | transformer | Attention context (softmax×V) | 1 | 0 | `[B, H, S, D] (V)` ×1 | —×1 | FP32×1 |
| [microsoft/OmniParser](https://huggingface.co/microsoft/OmniParser) | transformer | Attention output | 18 | 0–5 | `[768, 768]` ×18 | F32×18 | FP32×18 |
| [microsoft/OmniParser](https://huggingface.co/microsoft/OmniParser) | transformer | Projection / FFN | 24 | 0–5 | `[3072, 768]` ×12; `[768, 3072]` ×12 | F32×24 | FP32×24 |
| [microsoft/OmniParser](https://huggingface.co/microsoft/OmniParser) | transformer | Output head | 1 | — | `[51289, 768]` ×1 | F32×1 | FP32×1 |
| [microsoft/OmniParser](https://huggingface.co/microsoft/OmniParser) | transformer | Convolution (im2col matmul) | 39 | 0–22 | `[64, 64, 3, 3]` ×17; `[32, 32, 3, 3]` ×6; `[128, 128, 3, 3]` ×5 | F16×39 | FP16×39 |
| [microsoft/OmniParser](https://huggingface.co/microsoft/OmniParser) | transformer | 1×1 conv matmul | 25 | 2–22 | `[64, 64, 1, 1]` ×4; `[256, 384, 1, 1]` ×3; `[128, 192, 1, 1]` ×3 | F16×25 | FP16×25 |
| [microsoft/OmniParser](https://huggingface.co/microsoft/OmniParser) | vision_tower | Projection / FFN | 72 | 0–3 | `[512, 512]` ×18; `[2048, 512]` ×18; `[512, 2048]` ×18 | F32×72 | FP32×72 |
| [microsoft/OmniParser](https://huggingface.co/microsoft/OmniParser) | vision_tower | Convolution (im2col matmul) | 52 | 0–3 | `[512, 1, 3, 3]` ×36; `[128, 1, 3, 3]` ×4; `[256, 1, 3, 3]` ×4 | F32×52 | FP32×52 |
| [microsoft/OmniParser](https://huggingface.co/microsoft/OmniParser) | vision_tower | Other linear | 24 | 0–3 | `[1536, 512]` ×18; `[384, 128]` ×2; `[768, 256]` ×2 | F32×24 | FP32×24 |
