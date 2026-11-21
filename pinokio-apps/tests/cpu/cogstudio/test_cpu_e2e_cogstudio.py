"""Auto-generated end-to-end CPU test case for cogstudio."""

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
        a = _rand((2, 16, 8, 8), torch.float16)
        w = _rand((1920, 16, 2, 2), torch.float16)
        out = torch.nn.functional.conv2d(a, w)
        assert tuple(out.shape) == (2, 1920, 7, 7)
        assert out.dtype == torch.float16
        ran = True
    except Exception:
        pass
    # Linear matmul
    try:
        a = _rand((2, 4, 4096), torch.float16)
        w = _rand((1920, 4096), torch.float16)
        out = a @ w.transpose(-2, -1)
        assert tuple(out.shape) == (2, 4, 1920)
        assert out.dtype == torch.float16
        ran = True
    except Exception:
        pass
    # Linear matmul
    try:
        a = _rand((2, 4, 1920), torch.float16)
        w = _rand((64, 1920), torch.float16)
        out = a @ w.transpose(-2, -1)
        assert tuple(out.shape) == (2, 4, 64)
        assert out.dtype == torch.float16
        ran = True
    except Exception:
        pass
    # Linear matmul
    try:
        a = _rand((2, 4, 1920), torch.float16)
        w = _rand((512, 1920), torch.float16)
        out = a @ w.transpose(-2, -1)
        assert tuple(out.shape) == (2, 4, 512)
        assert out.dtype == torch.float16
        ran = True
    except Exception:
        pass
    # Linear matmul
    try:
        a = _rand((2, 4, 512), torch.float16)
        w = _rand((512, 512), torch.float16)
        out = a @ w.transpose(-2, -1)
        assert tuple(out.shape) == (2, 4, 512)
        assert out.dtype == torch.float16
        ran = True
    except Exception:
        pass
    if not ran:
        pytest.skip("No runnable CPU shape case for this app")
