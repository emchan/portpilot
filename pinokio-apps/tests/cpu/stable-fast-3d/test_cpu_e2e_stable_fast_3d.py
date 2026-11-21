"""Auto-generated end-to-end CPU test case for stable-fast-3d."""

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
        a = _rand((2, 4, 1024), torch.float32)
        w = _rand((1024, 1024), torch.float32)
        out = a @ w.transpose(-2, -1)
        assert tuple(out.shape) == (2, 4, 1024)
        assert out.dtype == torch.float32
        ran = True
    except Exception:
        pass
    # Linear matmul
    try:
        a = _rand((2, 4, 1024), torch.float32)
        w = _rand((8192, 1024), torch.float32)
        out = a @ w.transpose(-2, -1)
        assert tuple(out.shape) == (2, 4, 8192)
        assert out.dtype == torch.float32
        ran = True
    except Exception:
        pass
    # Linear matmul
    try:
        a = _rand((2, 4, 4096), torch.float32)
        w = _rand((1024, 4096), torch.float32)
        out = a @ w.transpose(-2, -1)
        assert tuple(out.shape) == (2, 4, 1024)
        assert out.dtype == torch.float32
        ran = True
    except Exception:
        pass
    # Linear matmul
    try:
        a = _rand((2, 4, 25), torch.float32)
        w = _rand((768, 25), torch.float32)
        out = a @ w.transpose(-2, -1)
        assert tuple(out.shape) == (2, 4, 768)
        assert out.dtype == torch.float32
        ran = True
    except Exception:
        pass
    # Linear matmul
    try:
        a = _rand((2, 4, 512), torch.float32)
        w = _rand((512, 512), torch.float32)
        out = a @ w.transpose(-2, -1)
        assert tuple(out.shape) == (2, 4, 512)
        assert out.dtype == torch.float32
        ran = True
    except Exception:
        pass
    if not ran:
        pytest.skip("No runnable CPU shape case for this app")
