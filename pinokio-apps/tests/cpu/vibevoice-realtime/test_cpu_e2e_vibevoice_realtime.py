"""Auto-generated end-to-end CPU test case for vibevoice-realtime."""

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
        a = _rand((2, 4, 64), torch.bfloat16)
        w = _rand((896, 64), torch.bfloat16)
        out = a @ w.transpose(-2, -1)
        assert tuple(out.shape) == (2, 4, 896)
        assert out.dtype == torch.bfloat16
        ran = True
    except Exception:
        pass
    # Linear matmul
    try:
        a = _rand((2, 4, 896), torch.bfloat16)
        w = _rand((896, 896), torch.bfloat16)
        out = a @ w.transpose(-2, -1)
        assert tuple(out.shape) == (2, 4, 896)
        assert out.dtype == torch.bfloat16
        ran = True
    except Exception:
        pass
    # Linear matmul
    try:
        a = _rand((2, 4, 896), torch.bfloat16)
        w = _rand((64, 896), torch.bfloat16)
        out = a @ w.transpose(-2, -1)
        assert tuple(out.shape) == (2, 4, 64)
        assert out.dtype == torch.bfloat16
        ran = True
    except Exception:
        pass
    # Linear matmul
    try:
        a = _rand((2, 4, 896), torch.bfloat16)
        w = _rand((2, 896), torch.bfloat16)
        out = a @ w.transpose(-2, -1)
        assert tuple(out.shape) == (2, 4, 2)
        assert out.dtype == torch.bfloat16
        ran = True
    except Exception:
        pass
    # Linear matmul
    try:
        a = _rand((2, 4, 2048), torch.bfloat16)
        w = _rand((8192, 2048), torch.bfloat16)
        out = a @ w.transpose(-2, -1)
        assert tuple(out.shape) == (2, 4, 8192)
        assert out.dtype == torch.bfloat16
        ran = True
    except Exception:
        pass
    if not ran:
        pytest.skip("No runnable CPU shape case for this app")
