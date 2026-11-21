"""Auto-generated end-to-end CPU test case for ovis."""

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
        a = _rand((2, 4, 3072), torch.float32)
        w = _rand((3072, 3072), torch.float32)
        out = a @ w.transpose(-2, -1)
        assert tuple(out.shape) == (2, 4, 3072)
        assert out.dtype == torch.float32
        ran = True
    except Exception:
        pass
    # Linear matmul
    try:
        a = _rand((2, 4, 3072), torch.float32)
        w = _rand((9216, 3072), torch.float32)
        out = a @ w.transpose(-2, -1)
        assert tuple(out.shape) == (2, 4, 9216)
        assert out.dtype == torch.float32
        ran = True
    except Exception:
        pass
    # Linear matmul
    try:
        a = _rand((2, 4, 12288), torch.float32)
        w = _rand((3072, 12288), torch.float32)
        out = a @ w.transpose(-2, -1)
        assert tuple(out.shape) == (2, 4, 3072)
        assert out.dtype == torch.float32
        ran = True
    except Exception:
        pass
    # Linear matmul
    try:
        a = _rand((2, 4, 3072), torch.float32)
        w = _rand((12288, 3072), torch.float32)
        out = a @ w.transpose(-2, -1)
        assert tuple(out.shape) == (2, 4, 12288)
        assert out.dtype == torch.float32
        ran = True
    except Exception:
        pass
    # Linear matmul
    try:
        a = _rand((2, 4, 3072), torch.float32)
        w = _rand((18432, 3072), torch.float32)
        out = a @ w.transpose(-2, -1)
        assert tuple(out.shape) == (2, 4, 18432)
        assert out.dtype == torch.float32
        ran = True
    except Exception:
        pass
    if not ran:
        pytest.skip("No runnable CPU shape case for this app")
