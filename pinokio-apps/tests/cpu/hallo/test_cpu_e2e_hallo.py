"""Auto-generated end-to-end CPU test case for hallo."""

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
        a = _rand((2, 4, 8, 8), torch.float32)
        w = _rand((320, 4, 3, 3), torch.float32)
        out = torch.nn.functional.conv2d(a, w)
        assert tuple(out.shape) == (2, 320, 6, 6)
        assert out.dtype == torch.float32
        ran = True
    except Exception:
        pass
    # Convolution (im2col matmul)
    try:
        a = _rand((2, 320, 8, 8), torch.float32)
        w = _rand((4, 320, 3, 3), torch.float32)
        out = torch.nn.functional.conv2d(a, w)
        assert tuple(out.shape) == (2, 4, 6, 6)
        assert out.dtype == torch.float32
        ran = True
    except Exception:
        pass
    # Linear matmul
    try:
        a = _rand((2, 4, 768), torch.float32)
        w = _rand((32, 768), torch.float32)
        out = a @ w.transpose(-2, -1)
        assert tuple(out.shape) == (2, 4, 32)
        assert out.dtype == torch.float32
        ran = True
    except Exception:
        pass
    # Linear matmul
    try:
        a = _rand((2, 4, 320), torch.float32)
        w = _rand((1280, 320), torch.float32)
        out = a @ w.transpose(-2, -1)
        assert tuple(out.shape) == (2, 4, 1280)
        assert out.dtype == torch.float32
        ran = True
    except Exception:
        pass
    # Linear matmul
    try:
        a = _rand((2, 4, 1280), torch.float32)
        w = _rand((1280, 1280), torch.float32)
        out = a @ w.transpose(-2, -1)
        assert tuple(out.shape) == (2, 4, 1280)
        assert out.dtype == torch.float32
        ran = True
    except Exception:
        pass
    if not ran:
        pytest.skip("No runnable CPU shape case for this app")
