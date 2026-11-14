"""Experimental int4 (NF4-style) weight quantization for Fooocus.

This module implements block-wise NF4 (Normal Float 4) quantization, the same
scheme used by QLoRA. It is *memory-only*: weights are stored in 4 bits and
dequantized to fp16 on the fly during the forward pass, so it reduces VRAM
usage but does NOT speed up compute (no int4 GEMM kernel is available in the
PyTorch version Fooocus targets).

Usage is opt-in via ``--quantize-int4``. Quality will degrade; treat as a
research/experimental feature.
"""

import torch
import torch.nn as nn

# NF4 quantization levels (from QLoRA / bitsandbytes).
NF4_LEVELS = torch.tensor([
    -1.0, -0.6961928009986877, -0.5250730514526367, -0.39491748809814453,
    -0.28444138169288635, -0.18477343022823334, -0.09105003625154495, 0.0,
    0.07958029955625534, 0.16093020141124725, 0.246112301945689, 0.33791524171829224,
    0.44070982933044495, 0.5626170039176941, 0.7229568362236072, 1.0,
], dtype=torch.float32)

BLOCK_SIZE = 64


def _nf4_quantize_tensor(w: torch.Tensor):
    """Return (packed uint8, per-block fp16 scales, original shape, pad)."""
    orig_shape = tuple(w.shape)
    w_flat = w.detach().reshape(-1).float().cpu()
    n = w_flat.numel()
    pad = (-n) % BLOCK_SIZE
    if pad:
        w_flat = torch.cat([w_flat, torch.zeros(pad, device=w_flat.device)])
    blocks = w_flat.reshape(-1, BLOCK_SIZE)
    amax = blocks.abs().amax(dim=1).clamp(min=1e-8)
    w_norm = (blocks / amax.unsqueeze(1)).clamp(-1.0, 1.0)
    diff = w_norm.unsqueeze(-1) - NF4_LEVELS.view(1, 1, -1)
    idx = diff.abs().argmin(dim=-1).to(torch.uint8).reshape(-1)
    if idx.numel() % 2:
        idx = torch.cat([idx, torch.zeros(1, dtype=torch.uint8)])
    packed = ((idx[0::2] << 4) | idx[1::2]).contiguous()
    return packed, amax.to(torch.float16), orig_shape, pad


def _nf4_dequantize(packed, amax, orig_shape, pad, device, dtype):
    idx = torch.empty(packed.numel() * 2, dtype=torch.uint8, device='cpu')
    idx[0::2] = (packed >> 4) & 0x0F
    idx[1::2] = packed & 0x0F
    levels = NF4_LEVELS
    blocks_n = amax.numel()
    vals = levels[idx.long()].reshape(blocks_n, BLOCK_SIZE) * amax.float().unsqueeze(1)
    vals = vals.reshape(-1)
    if pad:
        vals = vals[:-pad]
    return vals.reshape(orig_shape).to(device=device, dtype=dtype)


class NF4Linear(nn.Module):
    """A Linear layer whose weight is stored in block-wise NF4."""

    def __init__(self, in_features, out_features, bias=True, device=None, dtype=None):
        super().__init__()
        self.in_features = in_features
        self.out_features = out_features
        # placeholder; real data set via from_linear
        self.register_buffer('qweight', torch.empty(0, dtype=torch.uint8))
        self.register_buffer('scale', torch.empty(0, dtype=torch.float16))
        self._shape = (out_features, in_features)
        self._pad = 0
        if bias:
            self.bias = nn.Parameter(torch.zeros(out_features, device=device, dtype=dtype or torch.float16))
        else:
            self.register_parameter('bias', None)

    @classmethod
    def from_linear(cls, linear: nn.Linear):
        out_f, in_f = linear.weight.shape
        mod = cls(in_f, out_f, bias=linear.bias is not None,
                  device=linear.weight.device, dtype=linear.weight.dtype)
        packed, scale, shape, pad = _nf4_quantize_tensor(linear.weight.data)
        mod.qweight = packed
        mod.scale = scale
        mod._shape = shape
        mod._pad = pad
        if linear.bias is not None:
            with torch.no_grad():
                mod.bias.copy_(linear.bias.data.to(mod.bias.dtype))
        return mod

    def forward(self, x):
        target_dtype = x.dtype if x.is_floating_point() else torch.float16
        w = _nf4_dequantize(self.qweight, self.scale, self._shape, self._pad,
                             x.device, target_dtype).to(x.dtype)
        bias = self.bias.to(x.dtype) if self.bias is not None else None
        return torch.nn.functional.linear(x, w, bias)


def quantize_model_int4(model: nn.Module, verbose: bool = False) -> nn.Module:
    """Replace every nn.Linear in *model* with an NF4Linear (in place)."""
    replaced = 0
    for name, module in list(model.named_modules()):
        if isinstance(module, nn.Linear) and not isinstance(module, NF4Linear):
            # find parent
            parts = name.split('.')
            parent = model
            for p in parts[:-1]:
                parent = getattr(parent, p)
            attr = parts[-1]
            new_mod = NF4Linear.from_linear(module)
            setattr(parent, attr, new_mod)
            replaced += 1
    if verbose:
        print(f"[quantize_int4] replaced {replaced} Linear layers")
    return model


def compression_ratio(model: nn.Module) -> float:
    """Rough estimate of weight memory after quantization (not applied)."""
    total = 0
    for m in model.modules():
        if isinstance(m, nn.Linear):
            total += m.weight.numel() * m.weight.element_size()
    return total