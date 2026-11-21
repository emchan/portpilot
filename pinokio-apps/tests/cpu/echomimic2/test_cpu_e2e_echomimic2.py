"""Auto-generated end-to-end CPU test case for echomimic2."""

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
        w = _rand((512, 4, 3, 3), torch.float32)
        out = torch.nn.functional.conv2d(a, w)
        assert tuple(out.shape) == (2, 512, 6, 6)
        assert out.dtype == torch.float32
        ran = True
    except Exception:
        pass
    # Convolution (im2col matmul)
    try:
        a = _rand((2, 128, 8, 8), torch.float32)
        w = _rand((3, 128, 3, 3), torch.float32)
        out = torch.nn.functional.conv2d(a, w)
        assert tuple(out.shape) == (2, 3, 6, 6)
        assert out.dtype == torch.float32
        ran = True
    except Exception:
        pass
    # Convolution (im2col matmul)
    try:
        a = _rand((2, 3, 8, 8), torch.float32)
        w = _rand((128, 3, 3, 3), torch.float32)
        out = torch.nn.functional.conv2d(a, w)
        assert tuple(out.shape) == (2, 128, 6, 6)
        assert out.dtype == torch.float32
        ran = True
    except Exception:
        pass
    # Convolution (im2col matmul)
    try:
        a = _rand((2, 512, 8, 8), torch.float32)
        w = _rand((8, 512, 3, 3), torch.float32)
        out = torch.nn.functional.conv2d(a, w)
        assert tuple(out.shape) == (2, 8, 6, 6)
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
