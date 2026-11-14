# Backend quick reference

Tested stacks and gotchas from the Fooocus ports.

| Target | Working stack | Key gotchas | Verification |
| --- | --- | --- | --- |
| Intel AMX CPU | PyTorch CPU + oneDNN, bf16 autocast | Python 3.13 wheel gaps; IPEX `optimize` may be slower; thread/denormal tuning | `ONEDNN_VERBOSE`, `processwatch` |
| AMD Radeon 780M iGPU | ROCm 7.2.4 + PyTorch ROCm wheels in WSL2 | `gfx1103` needs `HSA_OVERRIDE_GFX_VERSION`; WSL/DXG profiler and allocator quirks; shared-memory illusion | `rocminfo`, PyTorch device props, image test |
| Google TPU | Native `torch_tpu`, bf16 + SDPA | Transformers 5 CLIP layout; Gradio timeouts/NumPy aliases; PJRT compile on new shapes | finite audit, full generation, UI queue test |

## Notes

- Intel AMX: plain bf16 autocast was enough to dispatch `avx10_1_512_amx`; IPEX is optional.
- AMD 780M: the practical memory limit is the 4 GB UMA carve-out plus the WSL RAM cap, not the reported shared GPU memory.
- Google TPU: 1024×1024 is the safer default; 1152×896 leaves under 1 GiB of HBM headroom.
- Always record the exact versions above with the benchmark; results are not portable across driver or wheel changes.
