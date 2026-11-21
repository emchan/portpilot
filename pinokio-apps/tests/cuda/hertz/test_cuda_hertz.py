"""Auto-generated CUDA GPU port smoke test for hertz."""

import pytest


def test_cuda_gpu_available():
    """CUDA execution requires a CUDA-capable GPU and PyTorch CUDA build."""
    torch = pytest.importorskip("torch")
    if not torch.cuda.is_available():
        pytest.skip("No CUDA GPU or CUDA-enabled PyTorch in this environment")
    assert torch.cuda.device_count() > 0
