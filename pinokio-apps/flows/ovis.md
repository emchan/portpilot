# Matrix-multiply flow — ovis

Companion to [`results/pinokio-apps.md`](../results/pinokio-apps.md) and [`analysis/flows.md`](../analysis/flows.md). Interactive viewer: [`ovis.html`](ovis.html).

**Models whose checkpoints were analysed:** [AIDC-AI/Ovis-Image-7B](https://huggingface.co/AIDC-AI/Ovis-Image-7B)

Reconstructed **228 matmul operations** from 1 checkpoint(s) (2 safetensors files).

## How the flow was inferred

The launcher snapshots are wrappers, so the graph is reconstructed from the safetensors header of each checkpoint the launcher downloads. Tensor **names** encode the layer role (Q/K/V, attention out, MLP gate/up/down, conv, head), **shapes** encode the matrix dimensions (PyTorch stores linear weights as `[out_features, in_features]`), and **dtypes** give weight precision. Activation precision is inferred from the weight dtype (quantized weights imply BF16/FP16 compute). `B` is the weight matrix; `A` is the activation `[B, S, in]` and `C` the output `[B, S, out]`. Two extra ops per attention block (Q×Kᵀ and softmax×V) are derived from the Q/K/V triple. This is an inferred dataflow, not a traced execution.

## Flow summary

| Component | Matmul ops | Weight dtypes | Activation dtypes |
| --- | --- | --- | --- |
| single_blocks | 81 | F32 (81) | FP32 (81) |
| double_blocks | 72 | F32 (72) | FP32 (72) |
| vae | 70 | F32 (70) | FP32 (70) |
| time_in | 2 | F32 (2) | FP32 (2) |
| final_layer | 1 | F32 (1) | FP32 (1) |
| img_in | 1 | F32 (1) | FP32 (1) |
| semantic_txt_in | 1 | F32 (1) | FP32 (1) |

## Representative block sequence — [AIDC-AI/Ovis-Image-7B](https://huggingface.co/AIDC-AI/Ovis-Image-7B), `double_blocks`, block 0

This is one coherent pass through a repeated transformer/UNet block; the aggregated roles across every block follow in the next section.

| # | Role | Operation | A (activation) | B (weight) | C (output) | Precision |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | MLP gate | Matmul (linear) | [B, S, 3072] FP32 | [12288, 3072] F32 | [B, S, 12288] FP32 | F32 weights / FP32 activations |
| 2 | MLP up | Matmul (linear) | [B, S, 3072] FP32 | [12288, 3072] F32 | [B, S, 12288] FP32 | F32 weights / FP32 activations |
| 3 | MLP down | Matmul (linear) | [B, S, 12288] FP32 | [3072, 12288] F32 | [B, S, 3072] FP32 | F32 weights / FP32 activations |
| 4 | Projection / FFN | Matmul (linear) | [B, S, 3072] FP32 | [3072, 3072] F32 | [B, S, 3072] FP32 | F32 weights / FP32 activations |
| 5 | Other linear | Matmul (linear) | [B, S, 3072] FP32 | [9216, 3072] F32 | [B, S, 9216] FP32 | F32 weights / FP32 activations |

## Aggregated matrix-multiply roles

For every model and component, each role is listed with the number of matching weight tensors, the most common weight shapes, and the weight/activation dtypes.

| Model | Component | Role | Ops | Blocks | Common B shapes | Weight dtypes | Activation dtypes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [AIDC-AI/Ovis-Image-7B](https://huggingface.co/AIDC-AI/Ovis-Image-7B) | double_blocks | MLP gate | 12 | 0–5 | `[12288, 3072]` ×12 | F32×12 | FP32×12 |
| [AIDC-AI/Ovis-Image-7B](https://huggingface.co/AIDC-AI/Ovis-Image-7B) | double_blocks | MLP up | 12 | 0–5 | `[12288, 3072]` ×12 | F32×12 | FP32×12 |
| [AIDC-AI/Ovis-Image-7B](https://huggingface.co/AIDC-AI/Ovis-Image-7B) | double_blocks | MLP down | 12 | 0–5 | `[3072, 12288]` ×12 | F32×12 | FP32×12 |
| [AIDC-AI/Ovis-Image-7B](https://huggingface.co/AIDC-AI/Ovis-Image-7B) | double_blocks | Projection / FFN | 12 | 0–5 | `[3072, 3072]` ×12 | F32×12 | FP32×12 |
| [AIDC-AI/Ovis-Image-7B](https://huggingface.co/AIDC-AI/Ovis-Image-7B) | double_blocks | Other linear | 24 | 0–5 | `[9216, 3072]` ×12; `[18432, 3072]` ×12 | F32×24 | FP32×24 |
| [AIDC-AI/Ovis-Image-7B](https://huggingface.co/AIDC-AI/Ovis-Image-7B) | final_layer | Projection / FFN | 1 | — | `[64, 3072]` ×1 | F32×1 | FP32×1 |
| [AIDC-AI/Ovis-Image-7B](https://huggingface.co/AIDC-AI/Ovis-Image-7B) | img_in | Other linear | 1 | — | `[3072, 64]` ×1 | F32×1 | FP32×1 |
| [AIDC-AI/Ovis-Image-7B](https://huggingface.co/AIDC-AI/Ovis-Image-7B) | semantic_txt_in | Other linear | 1 | — | `[3072, 2048]` ×1 | F32×1 | FP32×1 |
| [AIDC-AI/Ovis-Image-7B](https://huggingface.co/AIDC-AI/Ovis-Image-7B) | single_blocks | Projection / FFN | 54 | 0–26 | `[33792, 3072]` ×27; `[3072, 15360]` ×27 | F32×54 | FP32×54 |
| [AIDC-AI/Ovis-Image-7B](https://huggingface.co/AIDC-AI/Ovis-Image-7B) | single_blocks | Other linear | 27 | 0–26 | `[9216, 3072]` ×27 | F32×27 | FP32×27 |
| [AIDC-AI/Ovis-Image-7B](https://huggingface.co/AIDC-AI/Ovis-Image-7B) | time_in | Other linear | 2 | — | `[3072, 256]` ×1; `[3072, 3072]` ×1 | F32×2 | FP32×2 |
| [AIDC-AI/Ovis-Image-7B](https://huggingface.co/AIDC-AI/Ovis-Image-7B) | vae | Convolution (im2col matmul) | 58 | 0–3 | `[512, 512, 3, 3]` ×30; `[128, 128, 3, 3]` ×10; `[256, 256, 3, 3]` ×10 | F32×58 | FP32×58 |
| [AIDC-AI/Ovis-Image-7B](https://huggingface.co/AIDC-AI/Ovis-Image-7B) | vae | 1×1 conv matmul | 12 | 0 | `[512, 512, 1, 1]` ×8; `[128, 256, 1, 1]` ×1; `[256, 512, 1, 1]` ×1 | F32×12 | FP32×12 |
