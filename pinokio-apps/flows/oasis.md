# Matrix-multiply flow — oasis

Companion to [`results/pinokio-apps.md`](../results/pinokio-apps.md) and [`analysis/flows.md`](../analysis/flows.md). Interactive viewer: [`oasis.html`](oasis.html).

**Models whose checkpoints were analysed:** [cocktailpeanut/sisao](https://huggingface.co/cocktailpeanut/sisao)

Reconstructed **209 matmul operations** from 1 checkpoint(s) (2 safetensors files).

## How the flow was inferred

The launcher snapshots are wrappers, so the graph is reconstructed from the safetensors header of each checkpoint the launcher downloads. Tensor **names** encode the layer role (Q/K/V, attention out, MLP gate/up/down, conv, head), **shapes** encode the matrix dimensions (PyTorch stores linear weights as `[out_features, in_features]`), and **dtypes** give weight precision. Activation precision is inferred from the weight dtype (quantized weights imply BF16/FP16 compute). `B` is the weight matrix; `A` is the activation `[B, S, in]` and `C` the output `[B, S, out]`. Two extra ops per attention block (Q×Kᵀ and softmax×V) are derived from the Q/K/V triple. This is an inferred dataflow, not a traced execution.

## Flow summary

| Component | Matmul ops | Weight dtypes | Activation dtypes |
| --- | --- | --- | --- |
| blocks | 128 | F32 (128) | FP32 (128) |
| vae | 72 | F32 (72) | FP32 (72) |
| t_embedder | 2 | F32 (2) | FP32 (2) |
| external_cond | 1 | F32 (1) | FP32 (1) |
| final_layer | 1 | F32 (1) | FP32 (1) |
| patch_embed | 1 | F32 (1) | FP32 (1) |
| post_quant_conv | 1 | F32 (1) | FP32 (1) |
| predictor | 1 | F32 (1) | FP32 (1) |
| quant_conv | 1 | F32 (1) | FP32 (1) |
| x_embedder | 1 | F32 (1) | FP32 (1) |

## Representative block sequence — [cocktailpeanut/sisao](https://huggingface.co/cocktailpeanut/sisao), `vae`, block 0

This is one coherent pass through a repeated transformer/UNet block; the aggregated roles across every block follow in the next section.

| # | Role | Operation | A (activation) | B (weight) | C (output) | Precision |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | MLP up | Matmul (linear) | [B, S, 1024] FP32 | [4096, 1024] F32 | [B, S, 4096] FP32 | F32 weights / FP32 activations |
| 2 | MLP down | Matmul (linear) | [B, S, 4096] FP32 | [1024, 4096] F32 | [B, S, 1024] FP32 | F32 weights / FP32 activations |
| 3 | Projection / FFN | Matmul (linear) | [B, S, 1024] FP32 | [1024, 1024] F32 | [B, S, 1024] FP32 | F32 weights / FP32 activations |
| 4 | Other linear | Matmul (linear) | [B, S, 1024] FP32 | [3072, 1024] F32 | [B, S, 3072] FP32 | F32 weights / FP32 activations |

## Aggregated matrix-multiply roles

For every model and component, each role is listed with the number of matching weight tensors, the most common weight shapes, and the weight/activation dtypes.

| Model | Component | Role | Ops | Blocks | Common B shapes | Weight dtypes | Activation dtypes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [cocktailpeanut/sisao](https://huggingface.co/cocktailpeanut/sisao) | blocks | Q projection | 32 | 0–15 | `[3072, 1024]` ×32 | F32×32 | FP32×32 |
| [cocktailpeanut/sisao](https://huggingface.co/cocktailpeanut/sisao) | blocks | Attention output | 32 | 0–15 | `[1024, 1024]` ×32 | F32×32 | FP32×32 |
| [cocktailpeanut/sisao](https://huggingface.co/cocktailpeanut/sisao) | blocks | MLP up | 32 | 0–15 | `[4096, 1024]` ×32 | F32×32 | FP32×32 |
| [cocktailpeanut/sisao](https://huggingface.co/cocktailpeanut/sisao) | blocks | MLP down | 32 | 0–15 | `[1024, 4096]` ×32 | F32×32 | FP32×32 |
| [cocktailpeanut/sisao](https://huggingface.co/cocktailpeanut/sisao) | external_cond | Other linear | 1 | — | `[1024, 25]` ×1 | F32×1 | FP32×1 |
| [cocktailpeanut/sisao](https://huggingface.co/cocktailpeanut/sisao) | final_layer | Projection / FFN | 1 | — | `[64, 1024]` ×1 | F32×1 | FP32×1 |
| [cocktailpeanut/sisao](https://huggingface.co/cocktailpeanut/sisao) | patch_embed | Convolution (im2col matmul) | 1 | — | `[1024, 3, 20, 20]` ×1 | F32×1 | FP32×1 |
| [cocktailpeanut/sisao](https://huggingface.co/cocktailpeanut/sisao) | post_quant_conv | Other linear | 1 | — | `[1024, 16]` ×1 | F32×1 | FP32×1 |
| [cocktailpeanut/sisao](https://huggingface.co/cocktailpeanut/sisao) | predictor | Other linear | 1 | — | `[1200, 1024]` ×1 | F32×1 | FP32×1 |
| [cocktailpeanut/sisao](https://huggingface.co/cocktailpeanut/sisao) | quant_conv | Other linear | 1 | — | `[32, 1024]` ×1 | F32×1 | FP32×1 |
| [cocktailpeanut/sisao](https://huggingface.co/cocktailpeanut/sisao) | t_embedder | Projection / FFN | 2 | 0–2 | `[1024, 256]` ×1; `[1024, 1024]` ×1 | F32×2 | FP32×2 |
| [cocktailpeanut/sisao](https://huggingface.co/cocktailpeanut/sisao) | vae | MLP up | 18 | 0–11 | `[4096, 1024]` ×18 | F32×18 | FP32×18 |
| [cocktailpeanut/sisao](https://huggingface.co/cocktailpeanut/sisao) | vae | MLP down | 18 | 0–11 | `[1024, 4096]` ×18 | F32×18 | FP32×18 |
| [cocktailpeanut/sisao](https://huggingface.co/cocktailpeanut/sisao) | vae | Projection / FFN | 18 | 0–11 | `[1024, 1024]` ×18 | F32×18 | FP32×18 |
| [cocktailpeanut/sisao](https://huggingface.co/cocktailpeanut/sisao) | vae | Other linear | 18 | 0–11 | `[3072, 1024]` ×18 | F32×18 | FP32×18 |
| [cocktailpeanut/sisao](https://huggingface.co/cocktailpeanut/sisao) | x_embedder | Convolution (im2col matmul) | 1 | — | `[1024, 16, 2, 2]` ×1 | F32×1 | FP32×1 |
