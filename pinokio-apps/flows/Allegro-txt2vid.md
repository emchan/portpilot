# Matrix-multiply flow — Allegro-txt2vid

Companion to [`results/pinokio-apps.md`](../results/pinokio-apps.md) and [`analysis/flows.md`](../analysis/flows.md). Interactive viewer: [`Allegro-txt2vid.html`](Allegro-txt2vid.html).

**Models whose checkpoints were analysed:** [AlexWortega/RIFE](https://huggingface.co/AlexWortega/RIFE), [PixArt-alpha/PixArt-alpha](https://huggingface.co/PixArt-alpha/PixArt-alpha), [rhymes-ai/Allegro](https://huggingface.co/rhymes-ai/Allegro), [stabilityai/sd-vae-ft-mse-original](https://huggingface.co/stabilityai/sd-vae-ft-mse-original)

Reconstructed **209 matmul operations** from 2 checkpoint(s) (4 safetensors files).

## How the flow was inferred

The launcher snapshots are wrappers, so the graph is reconstructed from the safetensors header of each checkpoint the launcher downloads. Tensor **names** encode the layer role (Q/K/V, attention out, MLP gate/up/down, conv, head), **shapes** encode the matrix dimensions (PyTorch stores linear weights as `[out_features, in_features]`), and **dtypes** give weight precision. Activation precision is inferred from the weight dtype (quantized weights imply BF16/FP16 compute). `B` is the weight matrix; `A` is the activation `[B, S, in]` and `C` the output `[B, S, out]`. Two extra ops per attention block (Q×Kᵀ and softmax×V) are derived from the Q/K/V triple. This is an inferred dataflow, not a traced execution.

## Flow summary

| Component | Matmul ops | Weight dtypes | Activation dtypes |
| --- | --- | --- | --- |
| vae | 209 | F32 (203), — (6) | FP32 (209) |

## Representative block sequence — [rhymes-ai/Allegro](https://huggingface.co/rhymes-ai/Allegro), `vae`, block 0

This is one coherent pass through a repeated transformer/UNet block; the aggregated roles across every block follow in the next section.

| # | Role | Operation | A (activation) | B (weight) | C (output) | Precision |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Q projection | Matmul (linear) | [B, S, 4096] FP32 | [4096, 4096] F32 | [B, S, 4096] FP32 | F32 weights / FP32 activations |
| 2 | K projection | Matmul (linear) | [B, S, 4096] FP32 | [4096, 4096] F32 | [B, S, 4096] FP32 | F32 weights / FP32 activations |
| 3 | V projection | Matmul (linear) | [B, S, 4096] FP32 | [4096, 4096] F32 | [B, S, 4096] FP32 | F32 weights / FP32 activations |
| 4 | Attention scores (Q×Kᵀ) | Attention scores (Q x K^T) | [B, H, S, D] FP32 | [B, H, D, S] (K^T) FP32 | [B, H, S, S] FP32, FP32 accumulate | — weights / FP32 activations |
| 5 | Attention context (softmax×V) | Attention context (softmax x V) | [B, H, S, S] FP32 | [B, H, S, D] (V) FP32 | [B, H, S, D] FP32 | — weights / FP32 activations |
| 6 | Attention output | Matmul (linear) | [B, S, 4096] FP32 | [4096, 4096] F32 | [B, S, 4096] FP32 | F32 weights / FP32 activations |
| 7 | MLP gate | Matmul (linear) | [B, S, 4096] FP32 | [10240, 4096] F32 | [B, S, 10240] FP32 | F32 weights / FP32 activations |
| 8 | MLP up | Matmul (linear) | [B, S, 4096] FP32 | [10240, 4096] F32 | [B, S, 10240] FP32 | F32 weights / FP32 activations |
| 9 | MLP down | Matmul (linear) | [B, S, 10240] FP32 | [4096, 10240] F32 | [B, S, 4096] FP32 | F32 weights / FP32 activations |

## Aggregated matrix-multiply roles

For every model and component, each role is listed with the number of matching weight tensors, the most common weight shapes, and the weight/activation dtypes.

| Model | Component | Role | Ops | Blocks | Common B shapes | Weight dtypes | Activation dtypes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [rhymes-ai/Allegro](https://huggingface.co/rhymes-ai/Allegro) | vae | Q projection | 19 | 0–18 | `[4096, 4096]` ×19 | F32×19 | FP32×19 |
| [rhymes-ai/Allegro](https://huggingface.co/rhymes-ai/Allegro) | vae | K projection | 19 | 0–18 | `[4096, 4096]` ×19 | F32×19 | FP32×19 |
| [rhymes-ai/Allegro](https://huggingface.co/rhymes-ai/Allegro) | vae | V projection | 19 | 0–18 | `[4096, 4096]` ×19 | F32×19 | FP32×19 |
| [rhymes-ai/Allegro](https://huggingface.co/rhymes-ai/Allegro) | vae | Attention scores (Q×Kᵀ) | 3 | 0–13 | `[B, H, D, S] (K^T)` ×3 | —×3 | FP32×3 |
| [rhymes-ai/Allegro](https://huggingface.co/rhymes-ai/Allegro) | vae | Attention context (softmax×V) | 3 | 0–13 | `[B, H, S, D] (V)` ×3 | —×3 | FP32×3 |
| [rhymes-ai/Allegro](https://huggingface.co/rhymes-ai/Allegro) | vae | Attention output | 19 | 0–18 | `[4096, 4096]` ×19 | F32×19 | FP32×19 |
| [rhymes-ai/Allegro](https://huggingface.co/rhymes-ai/Allegro) | vae | MLP gate | 19 | 0–18 | `[10240, 4096]` ×19 | F32×19 | FP32×19 |
| [rhymes-ai/Allegro](https://huggingface.co/rhymes-ai/Allegro) | vae | MLP up | 18 | 0–17 | `[10240, 4096]` ×18 | F32×18 | FP32×18 |
| [rhymes-ai/Allegro](https://huggingface.co/rhymes-ai/Allegro) | vae | MLP down | 18 | 0–17 | `[4096, 10240]` ×18 | F32×18 | FP32×18 |
| [stabilityai/sd-vae-ft-mse-original](https://huggingface.co/stabilityai/sd-vae-ft-mse-original) | vae | Convolution (im2col matmul) | 58 | 0–3 | `[512, 512, 3, 3]` ×30; `[128, 128, 3, 3]` ×10; `[256, 256, 3, 3]` ×10 | F32×58 | FP32×58 |
| [stabilityai/sd-vae-ft-mse-original](https://huggingface.co/stabilityai/sd-vae-ft-mse-original) | vae | 1×1 conv matmul | 14 | 0 | `[512, 512, 1, 1]` ×8; `[4, 4, 1, 1]` ×1; `[8, 8, 1, 1]` ×1 | F32×14 | FP32×14 |

## Local source evidence

| File | Line | Evidence |
| --- | --- | --- |
| allegro/models/transformers/transformer_3d_allegro.py | [allegro/models/transformers/transformer_3d_allegro.py:201](https://github.com/pinokiofactory/Allegro-txt2vid/blob/f8327e3172834ee8d932d7284641a5e9a0065cbc/allegro/models/transformers/transformer_3d_allegro.py#L201) | self.proj_out_1 = nn.Linear(inner_dim, 2 * inner_dim) |
| allegro/models/transformers/transformer_3d_allegro.py | [allegro/models/transformers/transformer_3d_allegro.py:202](https://github.com/pinokiofactory/Allegro-txt2vid/blob/f8327e3172834ee8d932d7284641a5e9a0065cbc/allegro/models/transformers/transformer_3d_allegro.py#L202) | self.proj_out_2 = nn.Linear(inner_dim, patch_size * patch_size * self.out_channels) |
| allegro/models/transformers/transformer_3d_allegro.py | [allegro/models/transformers/transformer_3d_allegro.py:206](https://github.com/pinokiofactory/Allegro-txt2vid/blob/f8327e3172834ee8d932d7284641a5e9a0065cbc/allegro/models/transformers/transformer_3d_allegro.py#L206) | self.proj_out = nn.Linear(inner_dim, patch_size * patch_size * self.out_channels) |
| allegro/models/transformers/transformer_3d_allegro.py | [allegro/models/transformers/transformer_3d_allegro.py:412](https://github.com/pinokiofactory/Allegro-txt2vid/blob/f8327e3172834ee8d932d7284641a5e9a0065cbc/allegro/models/transformers/transformer_3d_allegro.py#L412) | hidden_states = torch.einsum("nthwopqc->nctohpwq", hidden_states) |
| allegro/models/transformers/rope.py | [allegro/models/transformers/rope.py:49](https://github.com/pinokiofactory/Allegro-txt2vid/blob/f8327e3172834ee8d932d7284641a5e9a0065cbc/allegro/models/transformers/rope.py#L49) | freqs = torch.einsum("i,j->ij", t, inv_freq).to(dtype) |
| allegro/models/transformers/block.py | [allegro/models/transformers/block.py:824](https://github.com/pinokiofactory/Allegro-txt2vid/blob/f8327e3172834ee8d932d7284641a5e9a0065cbc/allegro/models/transformers/block.py#L824) | # hidden_states = F.scaled_dot_product_attention( |
| allegro/models/transformers/block.py | [allegro/models/transformers/block.py:829](https://github.com/pinokiofactory/Allegro-txt2vid/blob/f8327e3172834ee8d932d7284641a5e9a0065cbc/allegro/models/transformers/block.py#L829) | # hidden_states = F.scaled_dot_product_attention( |
| allegro/models/transformers/block.py | [allegro/models/transformers/block.py:835](https://github.com/pinokiofactory/Allegro-txt2vid/blob/f8327e3172834ee8d932d7284641a5e9a0065cbc/allegro/models/transformers/block.py#L835) | hidden_states = F.scaled_dot_product_attention( |
| allegro/models/transformers/block.py | [allegro/models/transformers/block.py:1187](https://github.com/pinokiofactory/Allegro-txt2vid/blob/f8327e3172834ee8d932d7284641a5e9a0065cbc/allegro/models/transformers/block.py#L1187) | self.linear = nn.Linear(embedding_dim, 6 * embedding_dim, bias=True) |

## Snapdragon note
- Deep scan: cuda=19, torch=297, xformers=42, mps=8. Contains CUDA/Triton/TensorRT signals; Snapdragon path requires replacement or ONNX conversion.
