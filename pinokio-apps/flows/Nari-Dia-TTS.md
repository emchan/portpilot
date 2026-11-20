# Matrix-multiply flow — Nari-Dia-TTS

Companion to [`results/pinokio-apps.md`](../results/pinokio-apps.md) and [`analysis/flows.md`](../analysis/flows.md). Interactive viewer: [`Nari-Dia-TTS.html`](Nari-Dia-TTS.html).

**Models whose checkpoints were analysed:** [nari-labs/Dia-1.6B](https://huggingface.co/nari-labs/Dia-1.6B)

Reconstructed **263 matmul operations** from 1 checkpoint(s) (1 safetensors files).

## How the flow was inferred

The launcher snapshots are wrappers, so the graph is reconstructed from the safetensors header of each checkpoint the launcher downloads. Tensor **names** encode the layer role (Q/K/V, attention out, MLP gate/up/down, conv, head), **shapes** encode the matrix dimensions (PyTorch stores linear weights as `[out_features, in_features]`), and **dtypes** give weight precision. Activation precision is inferred from the weight dtype (quantized weights imply BF16/FP16 compute). `B` is the weight matrix; `A` is the activation `[B, S, in]` and `C` the output `[B, S, out]`. Two extra ops per attention block (Q×Kᵀ and softmax×V) are derived from the Q/K/V triple. This is an inferred dataflow, not a traced execution.

## Flow summary

| Component | Matmul ops | Weight dtypes | Activation dtypes |
| --- | --- | --- | --- |
| vae | 263 | F32 (263) | FP32 (263) |

## Representative block sequence — [nari-labs/Dia-1.6B](https://huggingface.co/nari-labs/Dia-1.6B), `vae`, block 0

This is one coherent pass through a repeated transformer/UNet block; the aggregated roles across every block follow in the next section.

| # | Role | Operation | A (activation) | B (weight) | C (output) | Precision |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Embedding projection | Matmul (linear) | [B, S, 2048] FP32 | [1028, 2048] F32 | [B, S, 1028] FP32 | F32 weights / FP32 activations |
| 2 | MLP down | Matmul (linear) | [B, S, 2048] FP32 | [8192, 2048] F32 | [B, S, 8192] FP32 | F32 weights / FP32 activations |
| 3 | Convolution (im2col matmul) | Conv [128] (im2col matmul) | [B, 16, spatial] FP32 | [1024, 16, 128] F32 | [B, 1024, spatial'] FP32 | F32 weights / FP32 activations |

## Aggregated matrix-multiply roles

For every model and component, each role is listed with the number of matching weight tensors, the most common weight shapes, and the weight/activation dtypes.

| Model | Component | Role | Ops | Blocks | Common B shapes | Weight dtypes | Activation dtypes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [nari-labs/Dia-1.6B](https://huggingface.co/nari-labs/Dia-1.6B) | vae | Embedding projection | 10 | 0–8 | `[1028, 2048]` ×9; `[256, 1024]` ×1 | F32×10 | FP32×10 |
| [nari-labs/Dia-1.6B](https://huggingface.co/nari-labs/Dia-1.6B) | vae | MLP down | 30 | 0–17 | `[8192, 2048]` ×18; `[4096, 1024]` ×12 | F32×30 | FP32×30 |
| [nari-labs/Dia-1.6B](https://huggingface.co/nari-labs/Dia-1.6B) | vae | Convolution (im2col matmul) | 223 | 0–17 | `[1024, 16, 128]` ×72; `[16, 128, 2048]` ×36; `[2048, 16, 128]` ×36 | F32×223 | FP32×223 |

## Local source evidence

| File | Line | Evidence |
| --- | --- | --- |
| dia/layers.py | [dia/layers.py:392](https://github.com/pinokiofactory/Nari-Dia-TTS/blob/e5b630df297c7f47f6c518a00d6c3f44be4e25b5/dia/layers.py#L392) | attn_output = F.scaled_dot_product_attention( |
