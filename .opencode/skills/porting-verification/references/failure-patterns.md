# Common failure patterns

| Symptom | Likely cause | First check |
| --- | --- | --- |
| Black or flat images | Weights not loaded, dtype mismatch, NaN | state-dict keys, finite audit |
| Import-time CUDA crash | Unconditional `torch.cuda.*` | gate CUDA calls behind a probe |
| Wrong device selected | Backend detection too broad | print accelerator and device type |
| Missing kernels on AMD | Unsupported `gfx` target | `rocminfo`, `HSA_OVERRIDE_GFX_VERSION` |
| OOM despite "free" memory | Shared memory / UMA / compile peak | real allocatable memory, low-VRAM mode |
| Very slow attention | xformers unavailable, basic attention selected | force SDPA |
| UI exits before serving | Gradio/web-stack version mismatch | pin FastAPI/Pydantic/Starlette/websockets |
| Websocket closes mid-generation | HTTP queue timeout shorter than first step | disable/raise queue client timeout |
| `pip` breaks the accelerator stack | CUDA-era requirements installed over it | skip `requirements_versions.txt` |
| Plausible output but wrong result | Silent API or layout drift | compare library version behavior, load reports |

## Triage order

Use the cheapest check that can distinguish the likely causes:

1. **Import and device** — does the app load, and does it see the intended accelerator?
2. **Core ops** — do matmul, SDPA, conv, norms, and SiLU run at the target dtype?
3. **Weight loading** — do checkpoint keys match, and how many keys actually loaded?
4. **Finiteness** — are conditioning tensors and the first latent finite?
5. **Image sanity** — is the output non-flat, with plausible mean/std?
6. **UI path** — does the app's own worker complete a generation, not just a helper script?
7. **Performance** — only after correctness, measure cold start and steady state separately.

## Notes

- `strict=False` only reports unexpected/missing keys relative to the model; it does **not** guarantee anything loaded.
- On TPU, uninitialised memory can be NaN, turning a silent load failure into black images.
- On CPU/CUDA, the same load failure may produce garbage output or appear to work, so verify explicitly.
- Prefer a small headless reproducer over debugging through the UI.

## Tests worth writing first

Each row above has a matching test in
[suggested tests](suggested-tests.md), with runnable snippets and the real Fooocus
failure it would have caught. Run that set before declaring a port working.
