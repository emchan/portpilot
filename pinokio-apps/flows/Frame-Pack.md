# Matrix-multiply flow — Frame-Pack

Companion to [`results/pinokio-apps.md`](../results/pinokio-apps.md) and [`analysis/flows.md`](../analysis/flows.md). Interactive viewer: [`Frame-Pack.html`](Frame-Pack.html).

**Models whose checkpoints were analysed:** [hunyuanvideo-community/HunyuanVideo](https://huggingface.co/hunyuanvideo-community/HunyuanVideo), [lllyasviel/FramePackI2V_HY](https://huggingface.co/lllyasviel/FramePackI2V_HY), [lllyasviel/FramePack_F1_I2V_HY_20250503](https://huggingface.co/lllyasviel/FramePack_F1_I2V_HY_20250503), [lllyasviel/flux_redux_bfl](https://huggingface.co/lllyasviel/flux_redux_bfl)

Reconstructed **1,351 matmul operations** from 4 checkpoint(s) (8 safetensors files).

## How the flow was inferred

The launcher snapshots are wrappers, so the graph is reconstructed from the safetensors header of each checkpoint the launcher downloads. Tensor **names** encode the layer role (Q/K/V, attention out, MLP gate/up/down, conv, head), **shapes** encode the matrix dimensions (PyTorch stores linear weights as `[out_features, in_features]`), and **dtypes** give weight precision. Activation precision is inferred from the weight dtype (quantized weights imply BF16/FP16 compute). `B` is the weight matrix; `A` is the activation `[B, S, in]` and `C` the output `[B, S, out]`. Two extra ops per attention block (Q×Kᵀ and softmax×V) are derived from the Q/K/V triple. This is an inferred dataflow, not a traced execution.

## Flow summary

| Component | Matmul ops | Weight dtypes | Activation dtypes |
| --- | --- | --- | --- |
| transformer | 1,056 | BF16 (1046), — (10) | BF16 (1056) |
| layers | 229 | F16 (223), — (6) | FP16 (229) |
| context_embedder | 38 | BF16 (34), — (4) | BF16 (38) |
| time_text_embed | 12 | BF16 (12) | BF16 (12) |
| clean_x_embedder | 6 | BF16 (6) | BF16 (6) |
| image_projection | 4 | BF16 (4) | BF16 (4) |
| proj_out | 2 | BF16 (2) | BF16 (2) |
| x_embedder | 2 | BF16 (2) | BF16 (2) |
| redux_down | 1 | BF16 (1) | BF16 (1) |
| redux_up | 1 | BF16 (1) | BF16 (1) |

## Representative block sequence — [lllyasviel/flux_redux_bfl](https://huggingface.co/lllyasviel/flux_redux_bfl), `transformer`, block 0

This is one coherent pass through a repeated transformer/UNet block; the aggregated roles across every block follow in the next section.

| # | Role | Operation | A (activation) | B (weight) | C (output) | Precision |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Q projection | Matmul (linear) | [B, S, 1152] BF16 | [1152, 1152] BF16 | [B, S, 1152] BF16 | BF16 weights / BF16 activations |
| 2 | K projection | Matmul (linear) | [B, S, 1152] BF16 | [1152, 1152] BF16 | [B, S, 1152] BF16 | BF16 weights / BF16 activations |
| 3 | V projection | Matmul (linear) | [B, S, 1152] BF16 | [1152, 1152] BF16 | [B, S, 1152] BF16 | BF16 weights / BF16 activations |
| 4 | Attention scores (Q×Kᵀ) | Attention scores (Q x K^T) | [B, H, S, D] BF16 | [B, H, D, S] (K^T) BF16 | [B, H, S, S] BF16, FP32 accumulate | — weights / BF16 activations |
| 5 | Attention context (softmax×V) | Attention context (softmax x V) | [B, H, S, S] BF16 | [B, H, S, D] (V) BF16 | [B, H, S, D] BF16 | — weights / BF16 activations |
| 6 | Attention output | Matmul (linear) | [B, S, 1152] BF16 | [1152, 1152] BF16 | [B, S, 1152] BF16 | BF16 weights / BF16 activations |
| 7 | MLP up | Matmul (linear) | [B, S, 1152] BF16 | [4304, 1152] BF16 | [B, S, 4304] BF16 | BF16 weights / BF16 activations |
| 8 | MLP down | Matmul (linear) | [B, S, 4304] BF16 | [1152, 4304] BF16 | [B, S, 1152] BF16 | BF16 weights / BF16 activations |

## Aggregated matrix-multiply roles

For every model and component, each role is listed with the number of matching weight tensors, the most common weight shapes, and the weight/activation dtypes.

| Model | Component | Role | Ops | Blocks | Common B shapes | Weight dtypes | Activation dtypes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [hunyuanvideo-community/HunyuanVideo](https://huggingface.co/hunyuanvideo-community/HunyuanVideo) | layers | Q projection | 32 | 0–31 | `[4096, 4096]` ×32 | F16×32 | FP16×32 |
| [hunyuanvideo-community/HunyuanVideo](https://huggingface.co/hunyuanvideo-community/HunyuanVideo) | layers | K projection | 32 | 0–31 | `[1024, 4096]` ×32 | F16×32 | FP16×32 |
| [hunyuanvideo-community/HunyuanVideo](https://huggingface.co/hunyuanvideo-community/HunyuanVideo) | layers | V projection | 32 | 0–31 | `[1024, 4096]` ×32 | F16×32 | FP16×32 |
| [hunyuanvideo-community/HunyuanVideo](https://huggingface.co/hunyuanvideo-community/HunyuanVideo) | layers | Attention scores (Q×Kᵀ) | 3 | 0–21 | `[B, H, D, S] (K^T)` ×3 | —×3 | FP16×3 |
| [hunyuanvideo-community/HunyuanVideo](https://huggingface.co/hunyuanvideo-community/HunyuanVideo) | layers | Attention context (softmax×V) | 3 | 0–21 | `[B, H, S, D] (V)` ×3 | —×3 | FP16×3 |
| [hunyuanvideo-community/HunyuanVideo](https://huggingface.co/hunyuanvideo-community/HunyuanVideo) | layers | MLP gate | 32 | 0–31 | `[14336, 4096]` ×32 | F16×32 | FP16×32 |
| [hunyuanvideo-community/HunyuanVideo](https://huggingface.co/hunyuanvideo-community/HunyuanVideo) | layers | MLP up | 32 | 0–31 | `[14336, 4096]` ×32 | F16×32 | FP16×32 |
| [hunyuanvideo-community/HunyuanVideo](https://huggingface.co/hunyuanvideo-community/HunyuanVideo) | layers | MLP down | 31 | 0–30 | `[4096, 14336]` ×31 | F16×31 | FP16×31 |
| [hunyuanvideo-community/HunyuanVideo](https://huggingface.co/hunyuanvideo-community/HunyuanVideo) | layers | Projection / FFN | 32 | 0–31 | `[4096, 4096]` ×32 | F16×32 | FP16×32 |
| [lllyasviel/flux_redux_bfl](https://huggingface.co/lllyasviel/flux_redux_bfl) | redux_down | Other linear | 1 | — | `[4096, 12288]` ×1 | BF16×1 | BF16×1 |
| [lllyasviel/flux_redux_bfl](https://huggingface.co/lllyasviel/flux_redux_bfl) | redux_up | Other linear | 1 | — | `[12288, 1152]` ×1 | BF16×1 | BF16×1 |
| [lllyasviel/flux_redux_bfl](https://huggingface.co/lllyasviel/flux_redux_bfl) | transformer | Q projection | 27 | 0–26 | `[1152, 1152]` ×27 | BF16×27 | BF16×27 |
| [lllyasviel/flux_redux_bfl](https://huggingface.co/lllyasviel/flux_redux_bfl) | transformer | K projection | 27 | 0–26 | `[1152, 1152]` ×27 | BF16×27 | BF16×27 |
| [lllyasviel/flux_redux_bfl](https://huggingface.co/lllyasviel/flux_redux_bfl) | transformer | V projection | 27 | 0–26 | `[1152, 1152]` ×27 | BF16×27 | BF16×27 |
| [lllyasviel/flux_redux_bfl](https://huggingface.co/lllyasviel/flux_redux_bfl) | transformer | Attention scores (Q×Kᵀ) | 1 | 0 | `[B, H, D, S] (K^T)` ×1 | —×1 | BF16×1 |
| [lllyasviel/flux_redux_bfl](https://huggingface.co/lllyasviel/flux_redux_bfl) | transformer | Attention context (softmax×V) | 1 | 0 | `[B, H, S, D] (V)` ×1 | —×1 | BF16×1 |
| [lllyasviel/flux_redux_bfl](https://huggingface.co/lllyasviel/flux_redux_bfl) | transformer | Attention output | 28 | 0–26 | `[1152, 1152]` ×28 | BF16×28 | BF16×28 |
| [lllyasviel/flux_redux_bfl](https://huggingface.co/lllyasviel/flux_redux_bfl) | transformer | MLP up | 28 | 0–26 | `[4304, 1152]` ×28 | BF16×28 | BF16×28 |
| [lllyasviel/flux_redux_bfl](https://huggingface.co/lllyasviel/flux_redux_bfl) | transformer | MLP down | 28 | 0–26 | `[1152, 4304]` ×28 | BF16×28 | BF16×28 |
| [lllyasviel/flux_redux_bfl](https://huggingface.co/lllyasviel/flux_redux_bfl) | transformer | Convolution (im2col matmul) | 1 | — | `[1152, 3, 14, 14]` ×1 | BF16×1 | BF16×1 |
| [lllyasviel/FramePack_F1_I2V_HY_20250503](https://huggingface.co/lllyasviel/FramePack_F1_I2V_HY_20250503) | clean_x_embedder | Convolution (im2col matmul) | 3 | — | `[3072, 16, 1, 2, 2]` ×1; `[3072, 16, 2, 4, 4]` ×1; `[3072, 16, 4, 8, 8]` ×1 | BF16×3 | BF16×3 |
| [lllyasviel/FramePack_F1_I2V_HY_20250503](https://huggingface.co/lllyasviel/FramePack_F1_I2V_HY_20250503) | context_embedder | Embedding projection | 2 | 0–1 | `[3072, 12288]` ×2 | BF16×2 | BF16×2 |
| [lllyasviel/FramePack_F1_I2V_HY_20250503](https://huggingface.co/lllyasviel/FramePack_F1_I2V_HY_20250503) | context_embedder | Q projection | 2 | 0–1 | `[3072, 3072]` ×2 | BF16×2 | BF16×2 |
| [lllyasviel/FramePack_F1_I2V_HY_20250503](https://huggingface.co/lllyasviel/FramePack_F1_I2V_HY_20250503) | context_embedder | K projection | 2 | 0–1 | `[3072, 3072]` ×2 | BF16×2 | BF16×2 |
| [lllyasviel/FramePack_F1_I2V_HY_20250503](https://huggingface.co/lllyasviel/FramePack_F1_I2V_HY_20250503) | context_embedder | V projection | 2 | 0–1 | `[3072, 3072]` ×2 | BF16×2 | BF16×2 |
| [lllyasviel/FramePack_F1_I2V_HY_20250503](https://huggingface.co/lllyasviel/FramePack_F1_I2V_HY_20250503) | context_embedder | Attention scores (Q×Kᵀ) | 1 | 0 | `[B, H, D, S] (K^T)` ×1 | —×1 | BF16×1 |
| [lllyasviel/FramePack_F1_I2V_HY_20250503](https://huggingface.co/lllyasviel/FramePack_F1_I2V_HY_20250503) | context_embedder | Attention context (softmax×V) | 1 | 0 | `[B, H, S, D] (V)` ×1 | —×1 | BF16×1 |
| [lllyasviel/FramePack_F1_I2V_HY_20250503](https://huggingface.co/lllyasviel/FramePack_F1_I2V_HY_20250503) | context_embedder | Attention output | 2 | 0–1 | `[3072, 3072]` ×2 | BF16×2 | BF16×2 |
| [lllyasviel/FramePack_F1_I2V_HY_20250503](https://huggingface.co/lllyasviel/FramePack_F1_I2V_HY_20250503) | context_embedder | Projection / FFN | 7 | 0–1 | `[3072, 4096]` ×2; `[3072, 3072]` ×2; `[12288, 3072]` ×2 | BF16×7 | BF16×7 |
| [lllyasviel/FramePack_F1_I2V_HY_20250503](https://huggingface.co/lllyasviel/FramePack_F1_I2V_HY_20250503) | image_projection | Projection / FFN | 2 | — | `[3072, 9216]` ×1; `[9216, 1152]` ×1 | BF16×2 | BF16×2 |
| [lllyasviel/FramePack_F1_I2V_HY_20250503](https://huggingface.co/lllyasviel/FramePack_F1_I2V_HY_20250503) | proj_out | Attention output | 1 | — | `[64, 3072]` ×1 | BF16×1 | BF16×1 |
| [lllyasviel/FramePack_F1_I2V_HY_20250503](https://huggingface.co/lllyasviel/FramePack_F1_I2V_HY_20250503) | time_text_embed | Projection / FFN | 6 | — | `[3072, 3072]` ×3; `[3072, 256]` ×2; `[3072, 768]` ×1 | BF16×6 | BF16×6 |
| [lllyasviel/FramePack_F1_I2V_HY_20250503](https://huggingface.co/lllyasviel/FramePack_F1_I2V_HY_20250503) | transformer | Q projection | 80 | 0–39 | `[3072, 3072]` ×80 | BF16×80 | BF16×80 |
| [lllyasviel/FramePack_F1_I2V_HY_20250503](https://huggingface.co/lllyasviel/FramePack_F1_I2V_HY_20250503) | transformer | K projection | 80 | 0–39 | `[3072, 3072]` ×80 | BF16×80 | BF16×80 |
| [lllyasviel/FramePack_F1_I2V_HY_20250503](https://huggingface.co/lllyasviel/FramePack_F1_I2V_HY_20250503) | transformer | V projection | 80 | 0–39 | `[3072, 3072]` ×80 | BF16×80 | BF16×80 |
| [lllyasviel/FramePack_F1_I2V_HY_20250503](https://huggingface.co/lllyasviel/FramePack_F1_I2V_HY_20250503) | transformer | Attention scores (Q×Kᵀ) | 2 | 0–21 | `[B, H, D, S] (K^T)` ×2 | —×2 | BF16×2 |
| [lllyasviel/FramePack_F1_I2V_HY_20250503](https://huggingface.co/lllyasviel/FramePack_F1_I2V_HY_20250503) | transformer | Attention context (softmax×V) | 2 | 0–21 | `[B, H, S, D] (V)` ×2 | —×2 | BF16×2 |
| [lllyasviel/FramePack_F1_I2V_HY_20250503](https://huggingface.co/lllyasviel/FramePack_F1_I2V_HY_20250503) | transformer | Attention output | 60 | 0–39 | `[3072, 15360]` ×40; `[3072, 3072]` ×20 | BF16×60 | BF16×60 |
| [lllyasviel/FramePack_F1_I2V_HY_20250503](https://huggingface.co/lllyasviel/FramePack_F1_I2V_HY_20250503) | transformer | Projection / FFN | 80 | 0–39 | `[12288, 3072]` ×80 | BF16×80 | BF16×80 |
| [lllyasviel/FramePack_F1_I2V_HY_20250503](https://huggingface.co/lllyasviel/FramePack_F1_I2V_HY_20250503) | transformer | Other linear | 60 | 0–19 | `[3072, 12288]` ×40; `[3072, 3072]` ×20 | BF16×60 | BF16×60 |
| [lllyasviel/FramePack_F1_I2V_HY_20250503](https://huggingface.co/lllyasviel/FramePack_F1_I2V_HY_20250503) | x_embedder | Convolution (im2col matmul) | 1 | — | `[3072, 16, 1, 2, 2]` ×1 | BF16×1 | BF16×1 |
| [lllyasviel/FramePackI2V_HY](https://huggingface.co/lllyasviel/FramePackI2V_HY) | clean_x_embedder | Convolution (im2col matmul) | 3 | — | `[3072, 16, 1, 2, 2]` ×1; `[3072, 16, 2, 4, 4]` ×1; `[3072, 16, 4, 8, 8]` ×1 | BF16×3 | BF16×3 |
| [lllyasviel/FramePackI2V_HY](https://huggingface.co/lllyasviel/FramePackI2V_HY) | context_embedder | Embedding projection | 2 | 0–1 | `[3072, 12288]` ×2 | BF16×2 | BF16×2 |
| [lllyasviel/FramePackI2V_HY](https://huggingface.co/lllyasviel/FramePackI2V_HY) | context_embedder | Q projection | 2 | 0–1 | `[3072, 3072]` ×2 | BF16×2 | BF16×2 |
| [lllyasviel/FramePackI2V_HY](https://huggingface.co/lllyasviel/FramePackI2V_HY) | context_embedder | K projection | 2 | 0–1 | `[3072, 3072]` ×2 | BF16×2 | BF16×2 |
| [lllyasviel/FramePackI2V_HY](https://huggingface.co/lllyasviel/FramePackI2V_HY) | context_embedder | V projection | 2 | 0–1 | `[3072, 3072]` ×2 | BF16×2 | BF16×2 |
| [lllyasviel/FramePackI2V_HY](https://huggingface.co/lllyasviel/FramePackI2V_HY) | context_embedder | Attention scores (Q×Kᵀ) | 1 | 0 | `[B, H, D, S] (K^T)` ×1 | —×1 | BF16×1 |
| [lllyasviel/FramePackI2V_HY](https://huggingface.co/lllyasviel/FramePackI2V_HY) | context_embedder | Attention context (softmax×V) | 1 | 0 | `[B, H, S, D] (V)` ×1 | —×1 | BF16×1 |
| [lllyasviel/FramePackI2V_HY](https://huggingface.co/lllyasviel/FramePackI2V_HY) | context_embedder | Attention output | 2 | 0–1 | `[3072, 3072]` ×2 | BF16×2 | BF16×2 |
| [lllyasviel/FramePackI2V_HY](https://huggingface.co/lllyasviel/FramePackI2V_HY) | context_embedder | Projection / FFN | 7 | 0–1 | `[3072, 4096]` ×2; `[3072, 3072]` ×2; `[12288, 3072]` ×2 | BF16×7 | BF16×7 |
| [lllyasviel/FramePackI2V_HY](https://huggingface.co/lllyasviel/FramePackI2V_HY) | image_projection | Projection / FFN | 2 | — | `[3072, 9216]` ×1; `[9216, 1152]` ×1 | BF16×2 | BF16×2 |
| [lllyasviel/FramePackI2V_HY](https://huggingface.co/lllyasviel/FramePackI2V_HY) | proj_out | Attention output | 1 | — | `[64, 3072]` ×1 | BF16×1 | BF16×1 |
| [lllyasviel/FramePackI2V_HY](https://huggingface.co/lllyasviel/FramePackI2V_HY) | time_text_embed | Projection / FFN | 6 | — | `[3072, 3072]` ×3; `[3072, 256]` ×2; `[3072, 768]` ×1 | BF16×6 | BF16×6 |
| [lllyasviel/FramePackI2V_HY](https://huggingface.co/lllyasviel/FramePackI2V_HY) | transformer | Q projection | 80 | 0–39 | `[3072, 3072]` ×80 | BF16×80 | BF16×80 |
| [lllyasviel/FramePackI2V_HY](https://huggingface.co/lllyasviel/FramePackI2V_HY) | transformer | K projection | 80 | 0–39 | `[3072, 3072]` ×80 | BF16×80 | BF16×80 |
| [lllyasviel/FramePackI2V_HY](https://huggingface.co/lllyasviel/FramePackI2V_HY) | transformer | V projection | 80 | 0–39 | `[3072, 3072]` ×80 | BF16×80 | BF16×80 |
| [lllyasviel/FramePackI2V_HY](https://huggingface.co/lllyasviel/FramePackI2V_HY) | transformer | Attention scores (Q×Kᵀ) | 2 | 0–21 | `[B, H, D, S] (K^T)` ×2 | —×2 | BF16×2 |
| [lllyasviel/FramePackI2V_HY](https://huggingface.co/lllyasviel/FramePackI2V_HY) | transformer | Attention context (softmax×V) | 2 | 0–21 | `[B, H, S, D] (V)` ×2 | —×2 | BF16×2 |
| [lllyasviel/FramePackI2V_HY](https://huggingface.co/lllyasviel/FramePackI2V_HY) | transformer | Attention output | 60 | 0–39 | `[3072, 15360]` ×40; `[3072, 3072]` ×20 | BF16×60 | BF16×60 |
| [lllyasviel/FramePackI2V_HY](https://huggingface.co/lllyasviel/FramePackI2V_HY) | transformer | Projection / FFN | 80 | 0–39 | `[12288, 3072]` ×80 | BF16×80 | BF16×80 |
| [lllyasviel/FramePackI2V_HY](https://huggingface.co/lllyasviel/FramePackI2V_HY) | transformer | Other linear | 60 | 0–19 | `[3072, 12288]` ×40; `[3072, 3072]` ×20 | BF16×60 | BF16×60 |
| [lllyasviel/FramePackI2V_HY](https://huggingface.co/lllyasviel/FramePackI2V_HY) | x_embedder | Convolution (im2col matmul) | 1 | — | `[3072, 16, 1, 2, 2]` ×1 | BF16×1 | BF16×1 |

## Snapdragon note
- Deep scan: cuda=4, torch=59, triton=3, xformers=3, sageattention=3, directml=1, safetensors=2. Contains CUDA/Triton/TensorRT signals; Snapdragon path requires replacement or ONNX conversion.
