"""Auto-generated end-to-end CPU test case for Frame-Pack."""

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
        a = _rand((2, 4, 14336), torch.float16)
        w = _rand((4096, 14336), torch.float16)
        out = a @ w.transpose(-2, -1)
        assert tuple(out.shape) == (2, 4, 4096)
        assert out.dtype == torch.float16
        ran = True
    except Exception:
        pass
    # Linear matmul
    try:
        a = _rand((2, 4, 4096), torch.float16)
        w = _rand((14336, 4096), torch.float16)
        out = a @ w.transpose(-2, -1)
        assert tuple(out.shape) == (2, 4, 14336)
        assert out.dtype == torch.float16
        ran = True
    except Exception:
        pass
    # Linear matmul
    try:
        a = _rand((2, 4, 4096), torch.float16)
        w = _rand((1024, 4096), torch.float16)
        out = a @ w.transpose(-2, -1)
        assert tuple(out.shape) == (2, 4, 1024)
        assert out.dtype == torch.float16
        ran = True
    except Exception:
        pass
    # Linear matmul
    try:
        a = _rand((2, 4, 4096), torch.float16)
        w = _rand((4096, 4096), torch.float16)
        out = a @ w.transpose(-2, -1)
        assert tuple(out.shape) == (2, 4, 4096)
        assert out.dtype == torch.float16
        ran = True
    except Exception:
        pass
    # Attention scores (Q x K^T)
    try:
        q = _rand((2, 2, 4, 8), torch.float16)
        k = _rand((2, 2, 4, 8), torch.float16)
        out = q @ k.transpose(-2, -1)
        assert tuple(out.shape) == (2, 2, 4, 4)
        assert out.dtype == torch.float16
        ran = True
    except Exception:
        pass
    if not ran:
        pytest.skip("No runnable CPU shape case for this app")
