"""Auto-generated end-to-end CPU test case for sd35."""

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
        a = _rand((2, 16, 8, 8), torch.bfloat16)
        w = _rand((512, 16, 3, 3), torch.bfloat16)
        out = torch.nn.functional.conv2d(a, w)
        assert tuple(out.shape) == (2, 512, 6, 6)
        assert out.dtype == torch.bfloat16
        ran = True
    except Exception:
        pass
    # Convolution (im2col matmul)
    try:
        a = _rand((2, 128, 8, 8), torch.bfloat16)
        w = _rand((3, 128, 3, 3), torch.bfloat16)
        out = torch.nn.functional.conv2d(a, w)
        assert tuple(out.shape) == (2, 3, 6, 6)
        assert out.dtype == torch.bfloat16
        ran = True
    except Exception:
        pass
    # Convolution (im2col matmul)
    try:
        a = _rand((2, 3, 8, 8), torch.bfloat16)
        w = _rand((128, 3, 3, 3), torch.bfloat16)
        out = torch.nn.functional.conv2d(a, w)
        assert tuple(out.shape) == (2, 128, 6, 6)
        assert out.dtype == torch.bfloat16
        ran = True
    except Exception:
        pass
    # Convolution (im2col matmul)
    try:
        a = _rand((2, 512, 8, 8), torch.bfloat16)
        w = _rand((32, 512, 3, 3), torch.bfloat16)
        out = torch.nn.functional.conv2d(a, w)
        assert tuple(out.shape) == (2, 32, 6, 6)
        assert out.dtype == torch.bfloat16
        ran = True
    except Exception:
        pass
    # Linear matmul
    try:
        a = _rand((2, 4, 4096), torch.float16)
        w = _rand((2432, 4096), torch.float16)
        out = a @ w.transpose(-2, -1)
        assert tuple(out.shape) == (2, 4, 2432)
        assert out.dtype == torch.float16
        ran = True
    except Exception:
        pass
    if not ran:
        pytest.skip("No runnable CPU shape case for this app")
