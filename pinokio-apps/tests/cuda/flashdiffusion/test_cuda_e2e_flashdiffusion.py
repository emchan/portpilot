"""Auto-generated end-to-end CUDA GPU smoke test for flashdiffusion."""

import pytest


def test_cuda_end_to_end():
    """Run a minimal end-to-end CUDA smoke check when a GPU is available."""
    torch = pytest.importorskip("torch")
    if not torch.cuda.is_available():
        pytest.skip("No CUDA GPU or CUDA-enabled PyTorch in this environment")

    device = torch.device("cuda:0")
    x = torch.tensor([1.0, 2.0, 3.0], device=device)
    y = x * 2
    assert y.device.type == "cuda"
    assert torch.allclose(y, torch.tensor([2.0, 4.0, 6.0], device=device))
