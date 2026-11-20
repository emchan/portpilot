# Matrix-multiply flow — vibevoice-realtime

Companion to [`results/pinokio-apps.md`](../results/pinokio-apps.md) and [`analysis/flows.md`](../analysis/flows.md). Interactive viewer: [`vibevoice-realtime.html`](vibevoice-realtime.html).

**Models whose checkpoints were analysed:** [microsoft/VibeVoice-Realtime-0.5B](https://huggingface.co/microsoft/VibeVoice-Realtime-0.5B)

Reconstructed **278 matmul operations** from 1 checkpoint(s) (1 safetensors files).

## How the flow was inferred

The launcher snapshots are wrappers, so the graph is reconstructed from the safetensors header of each checkpoint the launcher downloads. Tensor **names** encode the layer role (Q/K/V, attention out, MLP gate/up/down, conv, head), **shapes** encode the matrix dimensions (PyTorch stores linear weights as `[out_features, in_features]`), and **dtypes** give weight precision. Activation precision is inferred from the weight dtype (quantized weights imply BF16/FP16 compute). `B` is the weight matrix; `A` is the activation `[B, S, in]` and `C` the output `[B, S, out]`. Two extra ops per attention block (Q×Kᵀ and softmax×V) are derived from the Q/K/V triple. This is an inferred dataflow, not a traced execution.

## Flow summary

| Component | Matmul ops | Weight dtypes | Activation dtypes |
| --- | --- | --- | --- |
| transformer | 276 | BF16 (274), — (2) | BF16 (276) |
| tts_eos_classifier | 2 | BF16 (2) | BF16 (2) |

## Representative block sequence — [microsoft/VibeVoice-Realtime-0.5B](https://huggingface.co/microsoft/VibeVoice-Realtime-0.5B), `transformer`, block 0

This is one coherent pass through a repeated transformer/UNet block; the aggregated roles across every block follow in the next section.

| # | Role | Operation | A (activation) | B (weight) | C (output) | Precision |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Q projection | Matmul (linear) | [B, S, 896] BF16 | [896, 896] BF16 | [B, S, 896] BF16 | BF16 weights / BF16 activations |
| 2 | K projection | Matmul (linear) | [B, S, 896] BF16 | [128, 896] BF16 | [B, S, 128] BF16 | BF16 weights / BF16 activations |
| 3 | V projection | Matmul (linear) | [B, S, 896] BF16 | [128, 896] BF16 | [B, S, 128] BF16 | BF16 weights / BF16 activations |
| 4 | Attention scores (Q×Kᵀ) | Attention scores (Q x K^T) | [B, H, S, D] BF16 | [B, H, D, S] (K^T) BF16 | [B, H, S, S] BF16, FP32 accumulate | — weights / BF16 activations |
| 5 | Attention context (softmax×V) | Attention context (softmax x V) | [B, H, S, S] BF16 | [B, H, S, D] (V) BF16 | [B, H, S, D] BF16 | — weights / BF16 activations |
| 6 | MLP gate | Matmul (linear) | [B, S, 896] BF16 | [4864, 896] BF16 | [B, S, 4864] BF16 | BF16 weights / BF16 activations |
| 7 | MLP up | Matmul (linear) | [B, S, 896] BF16 | [4864, 896] BF16 | [B, S, 4864] BF16 | BF16 weights / BF16 activations |
| 8 | MLP down | Matmul (linear) | [B, S, 4864] BF16 | [896, 4864] BF16 | [B, S, 896] BF16 | BF16 weights / BF16 activations |
| 9 | Projection / FFN | Matmul (linear) | [B, S, 2048] BF16 | [8192, 2048] BF16 | [B, S, 8192] BF16 | BF16 weights / BF16 activations |
| 10 | Convolution (im2col matmul) | Conv [7] (im2col matmul) | [B, 1, spatial] BF16 | [2048, 1, 7] BF16 | [B, 2048, spatial'] BF16 | BF16 weights / BF16 activations |

## Aggregated matrix-multiply roles

For every model and component, each role is listed with the number of matching weight tensors, the most common weight shapes, and the weight/activation dtypes.

| Model | Component | Role | Ops | Blocks | Common B shapes | Weight dtypes | Activation dtypes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [microsoft/VibeVoice-Realtime-0.5B](https://huggingface.co/microsoft/VibeVoice-Realtime-0.5B) | transformer | Q projection | 24 | 0–19 | `[896, 896]` ×24 | BF16×24 | BF16×24 |
| [microsoft/VibeVoice-Realtime-0.5B](https://huggingface.co/microsoft/VibeVoice-Realtime-0.5B) | transformer | K projection | 24 | 0–19 | `[128, 896]` ×24 | BF16×24 | BF16×24 |
| [microsoft/VibeVoice-Realtime-0.5B](https://huggingface.co/microsoft/VibeVoice-Realtime-0.5B) | transformer | V projection | 24 | 0–19 | `[128, 896]` ×24 | BF16×24 | BF16×24 |
| [microsoft/VibeVoice-Realtime-0.5B](https://huggingface.co/microsoft/VibeVoice-Realtime-0.5B) | transformer | Attention scores (Q×Kᵀ) | 1 | 0 | `[B, H, D, S] (K^T)` ×1 | —×1 | BF16×1 |
| [microsoft/VibeVoice-Realtime-0.5B](https://huggingface.co/microsoft/VibeVoice-Realtime-0.5B) | transformer | Attention context (softmax×V) | 1 | 0 | `[B, H, S, D] (V)` ×1 | —×1 | BF16×1 |
| [microsoft/VibeVoice-Realtime-0.5B](https://huggingface.co/microsoft/VibeVoice-Realtime-0.5B) | transformer | MLP gate | 28 | 0–19 | `[4864, 896]` ×24; `[2688, 896]` ×4 | BF16×28 | BF16×28 |
| [microsoft/VibeVoice-Realtime-0.5B](https://huggingface.co/microsoft/VibeVoice-Realtime-0.5B) | transformer | MLP up | 28 | 0–19 | `[4864, 896]` ×24; `[2688, 896]` ×4 | BF16×28 | BF16×28 |
| [microsoft/VibeVoice-Realtime-0.5B](https://huggingface.co/microsoft/VibeVoice-Realtime-0.5B) | transformer | MLP down | 28 | 0–19 | `[896, 4864]` ×24; `[896, 2688]` ×4 | BF16×28 | BF16×28 |
| [microsoft/VibeVoice-Realtime-0.5B](https://huggingface.co/microsoft/VibeVoice-Realtime-0.5B) | transformer | Projection / FFN | 83 | 0–19 | `[896, 896]` ×27; `[8192, 2048]` ×8; `[2048, 8192]` ×8 | BF16×83 | BF16×83 |
| [microsoft/VibeVoice-Realtime-0.5B](https://huggingface.co/microsoft/VibeVoice-Realtime-0.5B) | transformer | Convolution (im2col matmul) | 34 | 0–6 | `[2048, 1, 7]` ×8; `[1024, 1, 7]` ×3; `[512, 1, 7]` ×3 | BF16×34 | BF16×34 |
| [microsoft/VibeVoice-Realtime-0.5B](https://huggingface.co/microsoft/VibeVoice-Realtime-0.5B) | transformer | Other linear | 1 | — | `[2, 896]` ×1 | BF16×1 | BF16×1 |
| [microsoft/VibeVoice-Realtime-0.5B](https://huggingface.co/microsoft/VibeVoice-Realtime-0.5B) | tts_eos_classifier | Projection / FFN | 2 | — | `[896, 896]` ×1; `[1, 896]` ×1 | BF16×2 | BF16×2 |
