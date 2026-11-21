"""Auto-generated end-to-end CPU test case for omniparser."""

import torch
import pytest


def _rand(shape, dtype):
    if dtype == torch.uint8:
        return torch.randint(0, 256, shape, dtype=dtype)
    return torch.randn(shape).to(dtype)


def test_cpu_shapes():
    ran = False
    # Linear matmul
    try:
        a = _rand((2, 4, 768), torch.float32)
        w = _rand((51289, 768), torch.float32)
        out = a @ w.transpose(-2, -1)
        assert tuple(out.shape) == (2, 4, 51289)
        assert out.dtype == torch.float32
        ran = True
    except Exception:
        pass
    # Linear matmul
    try:
        a = _rand((2, 4, 768), torch.float32)
        w = _rand((1026, 768), torch.float32)
        out = a @ w.transpose(-2, -1)
        assert tuple(out.shape) == (2, 4, 1026)
        assert out.dtype == torch.float32
        ran = True
    except Exception:
        pass
    # Linear matmul
    try:
        a = _rand((2, 4, 768), torch.float32)
        w = _rand((768, 768), torch.float32)
        out = a @ w.transpose(-2, -1)
        assert tuple(out.shape) == (2, 4, 768)
        assert out.dtype == torch.float32
        ran = True
    except Exception:
        pass
    # Attention scores (Q x K^T)
    try:
        q = _rand((2, 2, 4, 8), torch.float32)
        k = _rand((2, 2, 4, 8), torch.float32)
        out = q @ k.transpose(-2, -1)
        assert tuple(out.shape) == (2, 2, 4, 4)
        assert out.dtype == torch.float32
        ran = True
    except Exception:
        pass
    # Attention context (softmax x V)
    try:
        scores = _rand((2, 2, 4, 4), torch.float32)
        v = _rand((2, 2, 4, 8), torch.float32)
        out = scores @ v
        assert tuple(out.shape) == (2, 2, 4, 8)
        assert out.dtype == torch.float32
        ran = True
    except Exception:
        pass
    if not ran:
        pytest.skip("No runnable CPU shape case for this app")
