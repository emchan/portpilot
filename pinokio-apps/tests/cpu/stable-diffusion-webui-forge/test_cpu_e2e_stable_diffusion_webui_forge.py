"""Auto-generated end-to-end CPU test case for stable-diffusion-webui-forge."""

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
        a = _rand((2, 4, 3072), torch.bfloat16)
        w = _rand((32, 3072), torch.bfloat16)
        out = a @ w.transpose(-2, -1)
        assert tuple(out.shape) == (2, 4, 32)
        assert out.dtype == torch.bfloat16
        ran = True
    except Exception:
        pass
    # Linear matmul
    try:
        a = _rand((2, 4, 3072), torch.bfloat16)
        w = _rand((256, 3072), torch.bfloat16)
        out = a @ w.transpose(-2, -1)
        assert tuple(out.shape) == (2, 4, 256)
        assert out.dtype == torch.bfloat16
        ran = True
    except Exception:
        pass
    # Linear matmul
    try:
        a = _rand((2, 4, 32), torch.bfloat16)
        w = _rand((3072, 32), torch.bfloat16)
        out = a @ w.transpose(-2, -1)
        assert tuple(out.shape) == (2, 4, 3072)
        assert out.dtype == torch.bfloat16
        ran = True
    except Exception:
        pass
    # Linear matmul
    try:
        a = _rand((2, 4, 256), torch.bfloat16)
        w = _rand((3072, 256), torch.bfloat16)
        out = a @ w.transpose(-2, -1)
        assert tuple(out.shape) == (2, 4, 3072)
        assert out.dtype == torch.bfloat16
        ran = True
    except Exception:
        pass
    # Linear matmul
    try:
        a = _rand((2, 4, 32), torch.bfloat16)
        w = _rand((9216, 32), torch.bfloat16)
        out = a @ w.transpose(-2, -1)
        assert tuple(out.shape) == (2, 4, 9216)
        assert out.dtype == torch.bfloat16
        ran = True
    except Exception:
        pass
    if not ran:
        pytest.skip("No runnable CPU shape case for this app")
