---
name: Model analysis
description: Inspect a neural network before and during a port — operators used, weight matrix shapes, activation shapes, and the precision of weights and activations — so dtype, memory, and kernel decisions are grounded in the actual model.
---

# Model analysis

A port is planned against the model, not the app. Before changing code, know
which operators run, how large the weights are, what shapes flow through the
network, and at what precision. Most "mysterious" port failures are a dtype or
shape assumption that the model does not satisfy.

## 1. Enumerate operators

- Walk the module tree (`model.modules()`) and count operator types.
- For PyTorch, use `torch.fx` tracing or `torch.jit` to capture the op list;
  for ONNX, inspect `graph.node` op types.
- Note which ops are accelerator-sensitive: matmul/conv (GEMM), attention
  (SDPA), normalization (LayerNorm, GroupNorm), activations (SiLU, GELU),
  reductions (softmax, mean), and memory ops (reshape, transpose, concat).
- Flag ops with no native kernel on the target (e.g. `std_mean` on MPS/TPU,
  `cumprod` on older torch).

**Fooocus/SDXL:** the UNet is mostly convolutions and attention; CLIP is
transformer blocks (attention + MLP); the VAE is convolutions. Attention and
normalization are the port-sensitive ops.

## 2. Weight matrix shapes and sizes

- Print `name, tuple(param.shape), param.dtype, param.numel()` for every
  parameter.
- Group by block to see where the parameters live (input/middle/output blocks,
  text encoders, VAE).
- Compute total parameters and bytes per dtype.
- Check for tied/shared weights (same storage) — they affect memory accounting.

**Fooocus/SDXL ballpark (fp16):**

| Component | Parameters | Notes |
| --- | --- | --- |
| UNet (SDXL) | ~2.6 B | 3.8B? actually ~2.6B params; ~5.2 GB fp16 |
| CLIP-L | ~123 M | text encoder |
| CLIP-G | ~694 M | text encoder |
| VAE | ~84 M | encoder + decoder |
| Total | ~3.5 B | ~7 GB fp16, more with refiner |

Use the real numbers from your checkpoint; LoRAs and refiners add to this.

## 3. Activation shapes

- Run a forward pass with a representative input and record intermediate
  shapes (use forward hooks or `torch.fx`).
- Note the latent shape: `B, 4, H/8, W/8` for SDXL.
- Note attention sequence lengths: image tokens (H/8 * W/8) × text tokens (77).
- Static-shape backends (TPU, NPU) need these shapes fixed at compile time.

**Fooocus/SDXL at 1024²:** latent 4×128×128; UNet channels 320/640/1280;
attention at 32², 16², 8² feature maps.

## 4. Precision of weights and activations

- Record the storage dtype of every weight (`param.dtype`) and the compute dtype
  (`autocast` dtype, or the dtype of intermediate activations).
- Check mixed-precision boundaries: which parts stay fp32 (CLIP text
  embeddings in Fooocus) and which run bf16/fp16.
- For quantized ports, record the quantization scheme (NF4 int4, w8a16), block
  size, and scale dtype.
- Verify activations do not overflow the storage dtype during compute.

**Common findings:**

- Fooocus keeps CLIP text embeddings in fp32 while UNet/VAE run in bf16.
- NF4 (Apple) stores weights in 4-bit with fp16 scale; compute is fp16.
- Snapdragon stores the UNet as w8a16 (int8 weights, fp16 activations).
- TPU runs everything in bf16 except CLIP embeddings.

## 5. How to inspect

```python
# weight shapes and dtypes
for name, p in model.named_parameters():
    print(f"{name:60s} {tuple(p.shape)} {p.dtype} {p.numel()}")

# operator census
from collections import Counter
ops = Counter(type(m).__name__ for m in model.modules())
print(ops)

# activation shapes via hooks
shapes = {}
def hook(name):
    def fn(mod, inp, out):
        if isinstance(out, torch.Tensor):
            shapes[name] = tuple(out.shape)
    return fn
for name, m in model.named_modules():
    m.register_forward_hook(hook(name))
model(dummy_input)
print(shapes)
```

For ONNX graphs, enumerate `graph.node` op types and `graph.initializer`
shapes/dtypes. For a quick census without running, use `torchinfo.summary`.

## 6. What to record

- Operator census (which ops, how many).
- Per-component parameter counts and bytes.
- Latent and attention shapes at the default resolution.
- Storage vs compute dtype for every component.
- Quantization scheme and block size, if any.

## 7. Using the results

- **Memory budget:** sum weight bytes + activation bytes at peak; compare to
  allocatable memory from the hardware probe.
- **Kernel selection:** the op census tells you which fused kernels matter
  (attention, conv, norm).
- **Shape stability:** activation shapes determine whether a static-shape
  backend needs recompilation.
- **Numerics:** dtype boundaries tell you where a port can lose precision.

See `hardware-probe` for measuring the device, and `porting-bringup` for using
these findings during a port. The interactive model map is in
`fooocus/architecture/model_details.html`.