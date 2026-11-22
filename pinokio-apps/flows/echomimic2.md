# Matrix-multiply flow — echomimic2

Companion to [`results/pinokio-apps.md`](../results/pinokio-apps.md) and [`analysis/flows.md`](../analysis/flows.md). Interactive viewer: [`echomimic2.html`](echomimic2.html).

**Models whose checkpoints were analysed:** [BadToBest/EchoMimicV2](https://huggingface.co/BadToBest/EchoMimicV2), [cocktailpeanut/audio_processor](https://huggingface.co/cocktailpeanut/audio_processor), [lambdalabs/sd-image-variations-diffusers](https://huggingface.co/lambdalabs/sd-image-variations-diffusers), [stabilityai/sd-vae-ft-mse](https://huggingface.co/stabilityai/sd-vae-ft-mse)

Reconstructed **74 matmul operations** from 1 checkpoint(s) (1 safetensors files).

## How the flow was inferred

The launcher snapshots are wrappers, so the graph is reconstructed from the safetensors header of each checkpoint the launcher downloads. Tensor **names** encode the layer role (Q/K/V, attention out, MLP gate/up/down, conv, head), **shapes** encode the matrix dimensions (PyTorch stores linear weights as `[out_features, in_features]`), and **dtypes** give weight precision. Activation precision is inferred from the weight dtype (quantized weights imply BF16/FP16 compute). `B` is the weight matrix; `A` is the activation `[B, S, in]` and `C` the output `[B, S, out]`. Two extra ops per attention block (Q×Kᵀ and softmax×V) are derived from the Q/K/V triple. This is an inferred dataflow, not a traced execution.

## Flow summary

| Component | Matmul ops | Weight dtypes | Activation dtypes |
| --- | --- | --- | --- |
| vae | 74 | F32 (72), — (2) | FP32 (74) |

## Representative block sequence — [stabilityai/sd-vae-ft-mse](https://huggingface.co/stabilityai/sd-vae-ft-mse), `vae`, block 0

This is one coherent pass through a repeated transformer/UNet block; the aggregated roles across every block follow in the next section.

| # | Role | Operation | A (activation) | B (weight) | C (output) | Precision |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Q projection | Matmul (linear) | [B, S, 512] FP32 | [512, 512] F32 | [B, S, 512] FP32 | F32 weights / FP32 activations |
| 2 | K projection | Matmul (linear) | [B, S, 512] FP32 | [512, 512] F32 | [B, S, 512] FP32 | F32 weights / FP32 activations |
| 3 | V projection | Matmul (linear) | [B, S, 512] FP32 | [512, 512] F32 | [B, S, 512] FP32 | F32 weights / FP32 activations |
| 4 | Attention scores (Q×Kᵀ) | Attention scores (Q x K^T) | [B, H, S, D] FP32 | [B, H, D, S] (K^T) FP32 | [B, H, S, S] FP32, FP32 accumulate | — weights / FP32 activations |
| 5 | Attention context (softmax×V) | Attention context (softmax x V) | [B, H, S, S] FP32 | [B, H, S, D] (V) FP32 | [B, H, S, D] FP32 | — weights / FP32 activations |
| 6 | Projection / FFN | Matmul (linear) | [B, S, 512] FP32 | [512, 512] F32 | [B, S, 512] FP32 | F32 weights / FP32 activations |
| 7 | Convolution (im2col matmul) | Conv [3, 3] (im2col matmul) | [B, 512, spatial] FP32 | [512, 512, 3, 3] F32 | [B, 512, spatial'] FP32 | F32 weights / FP32 activations |

## Aggregated matrix-multiply roles

For every model and component, each role is listed with the number of matching weight tensors, the most common weight shapes, and the weight/activation dtypes.

| Model | Component | Role | Ops | Blocks | Common B shapes | Weight dtypes | Activation dtypes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [stabilityai/sd-vae-ft-mse](https://huggingface.co/stabilityai/sd-vae-ft-mse) | vae | Q projection | 2 | 0 | `[512, 512]` ×2 | F32×2 | FP32×2 |
| [stabilityai/sd-vae-ft-mse](https://huggingface.co/stabilityai/sd-vae-ft-mse) | vae | K projection | 2 | 0 | `[512, 512]` ×2 | F32×2 | FP32×2 |
| [stabilityai/sd-vae-ft-mse](https://huggingface.co/stabilityai/sd-vae-ft-mse) | vae | V projection | 2 | 0 | `[512, 512]` ×2 | F32×2 | FP32×2 |
| [stabilityai/sd-vae-ft-mse](https://huggingface.co/stabilityai/sd-vae-ft-mse) | vae | Attention scores (Q×Kᵀ) | 1 | 0 | `[B, H, D, S] (K^T)` ×1 | —×1 | FP32×1 |
| [stabilityai/sd-vae-ft-mse](https://huggingface.co/stabilityai/sd-vae-ft-mse) | vae | Attention context (softmax×V) | 1 | 0 | `[B, H, S, D] (V)` ×1 | —×1 | FP32×1 |
| [stabilityai/sd-vae-ft-mse](https://huggingface.co/stabilityai/sd-vae-ft-mse) | vae | Projection / FFN | 2 | 0 | `[512, 512]` ×2 | F32×2 | FP32×2 |
| [stabilityai/sd-vae-ft-mse](https://huggingface.co/stabilityai/sd-vae-ft-mse) | vae | Convolution (im2col matmul) | 58 | 0–3 | `[512, 512, 3, 3]` ×30; `[128, 128, 3, 3]` ×10; `[256, 256, 3, 3]` ×10 | F32×58 | FP32×58 |
| [stabilityai/sd-vae-ft-mse](https://huggingface.co/stabilityai/sd-vae-ft-mse) | vae | 1×1 conv matmul | 6 | 1–3 | `[4, 4, 1, 1]` ×1; `[8, 8, 1, 1]` ×1; `[256, 128, 1, 1]` ×1 | F32×6 | FP32×6 |

## Snapdragon note
- Deep scan: torch=11, triton=2, xformers=3, onnxruntime-gpu=1. Contains CUDA/Triton/TensorRT signals; Snapdragon path requires replacement or ONNX conversion.
