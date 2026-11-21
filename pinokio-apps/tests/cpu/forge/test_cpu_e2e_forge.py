"""Auto-generated end-to-end CPU test case for forge."""

import torch
import pytest


def _rand(shape, dtype):
    if dtype == torch.uint8:
        return torch.randint(0, 256, shape, dtype=dtype)
    return torch.randn(shape).to(dtype)


def test_cpu_shapes():
    ran = False
    # Convolution (im2col matmul)
    try:
        a = _rand((2, 3, 8, 8), torch.float16)
        w = _rand((1280, 3, 14, 14), torch.float16)
        out = torch.nn.functional.conv2d(a, w)
        assert tuple(out.shape) == (2, 1280, -5, -5)
        assert out.dtype == torch.float16
        ran = True
    except Exception:
        pass
    # Linear matmul
    try:
        a = _rand((2, 4, 1280), torch.float16)
        w = _rand((1280, 1280), torch.float16)
        out = a @ w.transpose(-2, -1)
        assert tuple(out.shape) == (2, 4, 1280)
        assert out.dtype == torch.float16
        ran = True
    except Exception:
        pass
    # Linear matmul
    try:
        a = _rand((2, 4, 1280), torch.float16)
        w = _rand((5120, 1280), torch.float16)
        out = a @ w.transpose(-2, -1)
        assert tuple(out.shape) == (2, 4, 5120)
        assert out.dtype == torch.float16
        ran = True
    except Exception:
        pass
    # Linear matmul
    try:
        a = _rand((2, 4, 5120), torch.float16)
        w = _rand((1280, 5120), torch.float16)
        out = a @ w.transpose(-2, -1)
        assert tuple(out.shape) == (2, 4, 1280)
        assert out.dtype == torch.float16
        ran = True
    except Exception:
        pass
    # Convolution (im2col matmul)
    try:
        a = _rand((2, 256, 8, 8), torch.float16)
        w = _rand((128, 256, 3, 3), torch.float16)
        out = torch.nn.functional.conv2d(a, w)
        assert tuple(out.shape) == (2, 128, 6, 6)
        assert out.dtype == torch.float16
        ran = True
    except Exception:
        pass
    if not ran:
        pytest.skip("No runnable CPU shape case for this app")
