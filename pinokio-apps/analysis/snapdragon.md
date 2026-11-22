# Snapdragon (CPU/GPU/NPU) feasibility across the Pinokio Factory apps


Companion to [`results/pinokio-apps.md`](../results/pinokio-apps.md), [`analysis/cpu.md`](cpu.md), [`analysis/tpu.md`](tpu.md), [`analysis/effort.md`](effort.md), [`analysis/flows.md`](flows.md), [`analysis/kernels.md`](kernels.md), [`analysis/models.md`](models.md). Snapshot: `main` tips recorded on 2026-11-20; every project links to its analysed commit.


## Target hardware (this computer)

| Component | Detail |
|---|---|
| CPU | Qualcomm Snapdragon X 10-core X1P64100 @ 3.40 GHz (ARM64, 10 cores/threads) |
| GPU | Qualcomm Adreno X1-85 GPU (DirectML/QNN-GPU candidate) |
| NPU | Qualcomm Hexagon NPU (QNN HTP backend) |
| OS | Windows 11 Home, ARM64 (build 26300) |
| Python | 3.12.10 (ARM64) installed; 3.10.11 also available |
| ONNX Runtime | 1.32.0 + onnxruntime-qnn 2.8.0 (QNN plugin registered via `ort.register_execution_provider_library`) |
| PyTorch | Not installed on this host; native Windows ARM64 CPU wheels exist for PyTorch 2.7+ (Python 3.12) |

## Snapdragon platform capability summary

- **CPU (Oryon, ARM64):** The realistic primary target. Native Windows ARM64 PyTorch CPU wheels are available (PyTorch 2.7+ for Python 3.12). Most apps classified as CPU-capable in [`analysis/cpu.md`](cpu.md) can run, but must use an ARM64 wheel index and ARM64-native dependencies; WSL2 (Linux aarch64) is the more complete fallback for training/full stacks.
- **GPU (Adreno X1-85):** There is no CUDA on this device. Adreno acceleration is only reachable through ONNX Runtime (DirectML EP or QNN GPU backend) or Windows ML after exporting the model to ONNX; PyTorch `.cuda()` paths do not apply. Treat as a conversion project, not a drop-in backend.
- **NPU (Hexagon):** Reachable through ONNX Runtime QNN EP (`QNNExecutionProvider`, HTP backend) with a QNN-compatible ONNX model (preferably QDQ-quantized or a QAIRT context binary). Requires operator support, quantization, and model export; FP32 models run as FP16 on HTP by default.
- **MLX/Apple-only apps:** Not runnable on this Snapdragon host (MLX is Apple-silicon only).
- **Hard CUDA/TensorRT/compiled-extension apps:** Blocked unless the CUDA-specific component is replaced.

## Summary of findings

| Finding | Apps | Detail |
|---|---:|---|
| CPU-ready (no local GEMM) | 11 | Runs as a normal ARM64 Python app; no model porting needed. |
| CPU-feasible with ARM64 wheels | 68 | Use PyTorch 2.7+ `win_arm64` CPU wheels; verify ARM64 deps; disable CUDA-only attention. |
| CPU possible after launcher change | 9 | Add an ARM64/CPU wheel branch and remove GPU-only flags. |
| Hard-blocked on CUDA/TensorRT/extensions | 5 | Requires replacing TensorRT/compiled CUDA components. |
| Unsuitable MLX/Apple-only runtimes | 6 | MLX is Apple-silicon only. |
| Empty repositories | 2 | No code to analyse. |
| **GPU/NPU conversion candidates** | **77** | Feasible CPU apps whose models can be exported to ONNX for Adreno DirectML/QNN-GPU or Hexagon QNN HTP. |
| **GPU/NPU blocked/unsuitable** | **11** | CUDA-blocked or MLX-only apps. |

## At a glance (Snapdragon)

| Snapdragon route | Apps | Meaning |
|---|---:|---|
| CPU-ready / no GEMM workload | 11 | No local model GEMM; runs as a normal ARM64 Python app. |
| CPU-feasible (adapted) | 68 | Needs ARM64 wheel index + dependency checks; runs on Oryon CPU. |
| CPU possible after launcher change | 9 | Add an ARM64/CPU wheel branch and remove GPU-only flags. |
| Blocked on CUDA/TensorRT/extensions | 5 | Requires replacing TensorRT/compiled CUDA components. |
| Unsuitable (MLX/Apple-only) | 6 | MLX runtime; not available on Windows ARM64. |
| Empty repository | 2 | No code to analyse. |

**Totals:** 101 repositories. GPU/NPU columns below are conversion targets, not drop-in backends.


## Per-app feasibility

| Project | Commit | Snapdragon CPU | Snapdragon GPU (Adreno) | Snapdragon NPU (Hexagon) | Notes |
|---|---|---|---|---|---|
| [ai-video-composer](https://github.com/pinokiofactory/ai-video-composer) | [0cc7921](https://github.com/pinokiofactory/ai-video-composer/commit/0cc7921ff899b4d8ce6e5b8f419f9144e50fa43d) | Ready | N/A (no local GEMM) | N/A (no local GEMM) | No GEMM workload; normal ARM64 app. |
| [bolt](https://github.com/pinokiofactory/bolt) | [e78682b](https://github.com/pinokiofactory/bolt/commit/e78682b26d423a3e26fe8c120521eddb6411d78b) | Ready | N/A (no local GEMM) | N/A (no local GEMM) | No GEMM workload; normal ARM64 app. |
| [browser-use](https://github.com/pinokiofactory/browser-use) | [6167ae0](https://github.com/pinokiofactory/browser-use/commit/6167ae0fc0dfd49120d215a4962143a87fd14c98) | Ready | N/A (no local GEMM) | N/A (no local GEMM) | No GEMM workload; normal ARM64 app. |
| [controlyourself](https://github.com/pinokiofactory/controlyourself) | [e516690](https://github.com/pinokiofactory/controlyourself/commit/e516690406e0e8499b09c7e8a4c65ac13539099f) | Ready | N/A (no local GEMM) | N/A (no local GEMM) | No GEMM workload; normal ARM64 app. |
| [ditto](https://github.com/pinokiofactory/ditto) | [aa45279](https://github.com/pinokiofactory/ditto/commit/aa45279201a7ddaead5ac33d56feba35417319c5) | Ready | N/A (no local GEMM) | N/A (no local GEMM) | No GEMM workload; normal ARM64 app. |
| [errortest](https://github.com/pinokiofactory/errortest) | [dd40517](https://github.com/pinokiofactory/errortest/commit/dd4051727b682cdfdb3f0ae792875052bd4398b9) | Ready | N/A (no local GEMM) | N/A (no local GEMM) | No GEMM workload; normal ARM64 app. |
| [macOS-use](https://github.com/pinokiofactory/macOS-use) | [7417e3a](https://github.com/pinokiofactory/macOS-use/commit/7417e3a1c1c5f38ec665d4c8ceb31857d8939bc4) | Ready | N/A (no local GEMM) | N/A (no local GEMM) | No GEMM workload; normal ARM64 app. |
| [mcp](https://github.com/pinokiofactory/mcp) | [01d5096](https://github.com/pinokiofactory/mcp/commit/01d5096c5ab4d4aaec70a074896c281fd204f8f5) | Ready | N/A (no local GEMM) | N/A (no local GEMM) | No GEMM workload; normal ARM64 app. |
| [open-webui](https://github.com/pinokiofactory/open-webui) | [d7c5932](https://github.com/pinokiofactory/open-webui/commit/d7c59329e3758cac350a1b5f1b834038727bec6c) | Ready | N/A (no local GEMM) | N/A (no local GEMM) | No GEMM workload; normal ARM64 app. |
| [openui](https://github.com/pinokiofactory/openui) | [83ab6b5](https://github.com/pinokiofactory/openui/commit/83ab6b5534ee0500674a6e2872e235092310cd9d) | Ready | N/A (no local GEMM) | N/A (no local GEMM) | No GEMM workload; normal ARM64 app. |
| [sillytavern](https://github.com/pinokiofactory/sillytavern) | [f75be07](https://github.com/pinokiofactory/sillytavern/commit/f75be07a853a78f0a9369d2faeec4518c553241a) | Ready | N/A (no local GEMM) | N/A (no local GEMM) | No GEMM workload; normal ARM64 app. |
| [AllTalk-TTS](https://github.com/pinokiofactory/AllTalk-TTS) | [7b6ed78](https://github.com/pinokiofactory/AllTalk-TTS/commit/7b6ed78e5a661eeafccdf446f0772be475390a5c) | Feasible (ARM64 wheels) | Possible via ONNX export + DirectML/QNN-GPU (conversion required) | Possible via ONNX export + QNN HTP | Use PyTorch 2.7+ win_arm64 wheel; verify ARM64 deps; disable CUDA-only attention. |
| [AudioX](https://github.com/pinokiofactory/AudioX) | [7a0ff7b](https://github.com/pinokiofactory/AudioX/commit/7a0ff7b5ca8d5eeb6054edf84196a23389545d1d) | Feasible (ARM64 wheels) | Possible via ONNX export + DirectML/QNN-GPU (conversion required) | Possible via ONNX export + QNN HTP | Use PyTorch 2.7+ win_arm64 wheel; verify ARM64 deps; disable CUDA-only attention. |
| [Frame-Pack](https://github.com/pinokiofactory/Frame-Pack) | [f0d7d1e](https://github.com/pinokiofactory/Frame-Pack/commit/f0d7d1eba4155f5985a465d0476a9f926d0c6179) | Feasible (ARM64 wheels) | Possible via ONNX export + DirectML/QNN-GPU (conversion required) | Possible via ONNX export + QNN HTP | Use PyTorch 2.7+ win_arm64 wheel; verify ARM64 deps; disable CUDA-only attention. |
| [Hunyuan3D-2](https://github.com/pinokiofactory/Hunyuan3D-2) | [c0aa654](https://github.com/pinokiofactory/Hunyuan3D-2/commit/c0aa654a27ccda410b1d0914b61adbd52731c3c7) | Feasible (ARM64 wheels) | Possible via ONNX export + DirectML/QNN-GPU (conversion required) | Possible via ONNX export + QNN HTP | Use PyTorch 2.7+ win_arm64 wheel; verify ARM64 deps; disable CUDA-only attention. |
| [Hunyuan3D-2-mini](https://github.com/pinokiofactory/Hunyuan3D-2-mini) | [7ffb6a8](https://github.com/pinokiofactory/Hunyuan3D-2-mini/commit/7ffb6a83e54fee4df0f111111e768217e337fadc) | Feasible (ARM64 wheels) | Possible via ONNX export + DirectML/QNN-GPU (conversion required) | Possible via ONNX export + QNN HTP | Use PyTorch 2.7+ win_arm64 wheel; verify ARM64 deps; disable CUDA-only attention. |
| [Hunyuan3d-2-lowvram](https://github.com/pinokiofactory/Hunyuan3d-2-lowvram) | [9c41502](https://github.com/pinokiofactory/Hunyuan3d-2-lowvram/commit/9c415021473ec16b64b85bda5d3d50295c478e5b) | Feasible (ARM64 wheels) | Possible via ONNX export + DirectML/QNN-GPU (conversion required) | Possible via ONNX export + QNN HTP | Use PyTorch 2.7+ win_arm64 wheel; verify ARM64 deps; disable CUDA-only attention. |
| [Ilaria-RVC](https://github.com/pinokiofactory/Ilaria-RVC) | [2dd918e](https://github.com/pinokiofactory/Ilaria-RVC/commit/2dd918e4d99c051cbc3a4201484cb91990cfa118) | Feasible (ARM64 wheels) | Possible via ONNX export + DirectML/QNN-GPU (conversion required) | Possible via ONNX export + QNN HTP | Use PyTorch 2.7+ win_arm64 wheel; verify ARM64 deps; disable CUDA-only attention. |
| [Kokoro-TTS](https://github.com/pinokiofactory/Kokoro-TTS) | [491a369](https://github.com/pinokiofactory/Kokoro-TTS/commit/491a369bdca03b320586bd230f1c819562c03558) | Feasible (ARM64 wheels) | Possible via ONNX export + DirectML/QNN-GPU (conversion required) | Possible via ONNX export + QNN HTP | Use PyTorch 2.7+ win_arm64 wheel; verify ARM64 deps; disable CUDA-only attention. |
| [MMAudio](https://github.com/pinokiofactory/MMAudio) | [301b075](https://github.com/pinokiofactory/MMAudio/commit/301b075421ae40d86dded8f5c36c64f65af89bfb) | Feasible (ARM64 wheels) | Possible via ONNX export + DirectML/QNN-GPU (conversion required) | Possible via ONNX export + QNN HTP | Use PyTorch 2.7+ win_arm64 wheel; verify ARM64 deps; disable CUDA-only attention. |
| [MagicQuill](https://github.com/pinokiofactory/MagicQuill) | [bfdae28](https://github.com/pinokiofactory/MagicQuill/commit/bfdae2847a85d7b00761b4e93fbcb91be5e6d494) | Feasible (ARM64 wheels) | Possible via ONNX export + DirectML/QNN-GPU (conversion required) | Possible via QNN HTP after dequant/upcast (FP8/4-bit) | Use PyTorch 2.7+ win_arm64 wheel; verify ARM64 deps; disable CUDA-only attention. |
| [MatAnyone](https://github.com/pinokiofactory/MatAnyone) | [8483199](https://github.com/pinokiofactory/MatAnyone/commit/84831993029bc83f5942f0401bc8a32dd315b217) | Feasible (ARM64 wheels) | Possible via ONNX export + DirectML/QNN-GPU (conversion required) | Possible via ONNX export + QNN HTP | Use PyTorch 2.7+ win_arm64 wheel; verify ARM64 deps; disable CUDA-only attention. |
| [Nari-Dia-TTS](https://github.com/pinokiofactory/Nari-Dia-TTS) | [e5b630d](https://github.com/pinokiofactory/Nari-Dia-TTS/commit/e5b630df297c7f47f6c518a00d6c3f44be4e25b5) | Feasible (ARM64 wheels) | Possible via ONNX export + DirectML/QNN-GPU (conversion required) | Possible via ONNX export + QNN HTP | Use PyTorch 2.7+ win_arm64 wheel; verify ARM64 deps; disable CUDA-only attention. |
| [Orpheus-TTS-FastAPI](https://github.com/pinokiofactory/Orpheus-TTS-FastAPI) | [36afb50](https://github.com/pinokiofactory/Orpheus-TTS-FastAPI/commit/36afb50f8c7355238763680480dca601789cae82) | Feasible (ARM64 wheels) | Possible via ONNX export + DirectML/QNN-GPU (conversion required) | Possible via ONNX export; GGUF not NPU-native | Use PyTorch 2.7+ win_arm64 wheel; verify ARM64 deps; disable CUDA-only attention. |
| [RMBG-2-Studio](https://github.com/pinokiofactory/RMBG-2-Studio) | [a2c3a0d](https://github.com/pinokiofactory/RMBG-2-Studio/commit/a2c3a0d0f1618c74c115d3221eb665bab5e8df10) | Feasible (ARM64 wheels) | Possible via ONNX export + DirectML/QNN-GPU (conversion required) | Possible via ONNX export + QNN HTP | Use PyTorch 2.7+ win_arm64 wheel; verify ARM64 deps; disable CUDA-only attention. |
| [StyleTTS2_Studio](https://github.com/pinokiofactory/StyleTTS2_Studio) | [cb09179](https://github.com/pinokiofactory/StyleTTS2_Studio/commit/cb09179fa56bf5d34c86dffc9b5424c5331005a7) | Feasible (ARM64 wheels) | Possible via ONNX export + DirectML/QNN-GPU (conversion required) | Possible via ONNX export + QNN HTP | Use PyTorch 2.7+ win_arm64 wheel; verify ARM64 deps; disable CUDA-only attention. |
| [Ultimate-TTS-Studio](https://github.com/pinokiofactory/Ultimate-TTS-Studio) | [b8c15ef](https://github.com/pinokiofactory/Ultimate-TTS-Studio/commit/b8c15efaead5a5e8744783fd443466333d2b1805) | Feasible (ARM64 wheels) | Possible via ONNX export + DirectML/QNN-GPU (conversion required) | Possible via ONNX export + QNN HTP | Use PyTorch 2.7+ win_arm64 wheel; verify ARM64 deps; disable CUDA-only attention. |
| [accdiffusion](https://github.com/pinokiofactory/accdiffusion) | [4af0027](https://github.com/pinokiofactory/accdiffusion/commit/4af00276b2b2138562c5c52bce291bdb4a1c590f) | Feasible (ARM64 wheels) | Possible via ONNX export + DirectML/QNN-GPU (conversion required) | Possible via ONNX export + QNN HTP | Use PyTorch 2.7+ win_arm64 wheel; verify ARM64 deps; disable CUDA-only attention. |
| [applio](https://github.com/pinokiofactory/applio) | [41a9ccd](https://github.com/pinokiofactory/applio/commit/41a9ccd75fbb39d84059447a8717581640c11143) | Feasible (ARM64 wheels) | Possible via ONNX export + DirectML/QNN-GPU (conversion required) | Possible via ONNX export + QNN HTP | Use PyTorch 2.7+ win_arm64 wheel; verify ARM64 deps; disable CUDA-only attention. |
| [artist](https://github.com/pinokiofactory/artist) | [af0faf2](https://github.com/pinokiofactory/artist/commit/af0faf241f231b8efd74b9099496a74a24a1eaa7) | Feasible (ARM64 wheels) | Possible via ONNX export + DirectML/QNN-GPU (conversion required) | Possible via ONNX export + QNN HTP | Use PyTorch 2.7+ win_arm64 wheel; verify ARM64 deps; disable CUDA-only attention. |
| [audiocraft_plus](https://github.com/pinokiofactory/audiocraft_plus) | [a8e0d27](https://github.com/pinokiofactory/audiocraft_plus/commit/a8e0d2731e8dbb7185a4a0ffd53b495d003586ab) | Feasible (ARM64 wheels) | Possible via ONNX export + DirectML/QNN-GPU (conversion required) | Possible via ONNX export + QNN HTP | Use PyTorch 2.7+ win_arm64 wheel; verify ARM64 deps; disable CUDA-only attention. |
| [augmentoolkit](https://github.com/pinokiofactory/augmentoolkit) | [24f8037](https://github.com/pinokiofactory/augmentoolkit/commit/24f80371c8ae61a91295b71f773e41a2616437e6) | Feasible (ARM64 wheels) | Possible via ONNX export + DirectML/QNN-GPU (conversion required) | Possible via ONNX export + QNN HTP | Use PyTorch 2.7+ win_arm64 wheel; verify ARM64 deps; disable CUDA-only attention. |
| [aura-sr-upscaler](https://github.com/pinokiofactory/aura-sr-upscaler) | [9357cf9](https://github.com/pinokiofactory/aura-sr-upscaler/commit/9357cf93dac1f28179bb5d32c98b1c5c75a61ece) | Feasible (ARM64 wheels) | Possible via ONNX export + DirectML/QNN-GPU (conversion required) | Possible via ONNX export + QNN HTP | Use PyTorch 2.7+ win_arm64 wheel; verify ARM64 deps; disable CUDA-only attention. |
| [autogpt](https://github.com/pinokiofactory/autogpt) | [53e7c0e](https://github.com/pinokiofactory/autogpt/commit/53e7c0e1e22b3b9162d7d0669f9bac3491cf5d51) | Feasible (ARM64 wheels) | Possible via ONNX export + DirectML/QNN-GPU (conversion required) | Possible via ONNX export + QNN HTP | Use PyTorch 2.7+ win_arm64 wheel; verify ARM64 deps; disable CUDA-only attention. |
| [clarity-refiners-ui](https://github.com/pinokiofactory/clarity-refiners-ui) | [a632fb6](https://github.com/pinokiofactory/clarity-refiners-ui/commit/a632fb6b948fa6b1a55d816982655d6dc8ed995e) | Feasible (ARM64 wheels) | Possible via ONNX export + DirectML/QNN-GPU (conversion required) | Possible via ONNX export + QNN HTP | Use PyTorch 2.7+ win_arm64 wheel; verify ARM64 deps; disable CUDA-only attention. |
| [cogstudio](https://github.com/pinokiofactory/cogstudio) | [7dfb014](https://github.com/pinokiofactory/cogstudio/commit/7dfb014a636513c5b42de070c43e285c9bf7cce7) | Feasible (ARM64 wheels) | Possible via ONNX export + DirectML/QNN-GPU (conversion required) | Possible via ONNX export + QNN HTP | Use PyTorch 2.7+ win_arm64 wheel; verify ARM64 deps; disable CUDA-only attention. |
| [cogvideo](https://github.com/pinokiofactory/cogvideo) | [9e2a186](https://github.com/pinokiofactory/cogvideo/commit/9e2a18626426cbeb7e84be537d98e9082de8fe97) | Feasible (ARM64 wheels) | Possible via ONNX export + DirectML/QNN-GPU (conversion required) | Possible via ONNX export + QNN HTP | Use PyTorch 2.7+ win_arm64 wheel; verify ARM64 deps; disable CUDA-only attention. |
| [comfy](https://github.com/pinokiofactory/comfy) | [ba11047](https://github.com/pinokiofactory/comfy/commit/ba110479f88835d64c603044c2fe69102833fa55) | Feasible (ARM64 wheels) | Possible via ONNX export + DirectML/QNN-GPU (conversion required) | Possible via ONNX export; GGUF not NPU-native | Use PyTorch 2.7+ win_arm64 wheel; verify ARM64 deps; disable CUDA-only attention. |
| [cube](https://github.com/pinokiofactory/cube) | [5884465](https://github.com/pinokiofactory/cube/commit/58844658cfc9eab4f8e956bab4883fa8d867cf44) | Feasible (ARM64 wheels) | Possible via ONNX export + DirectML/QNN-GPU (conversion required) | Possible via ONNX export + QNN HTP | Use PyTorch 2.7+ win_arm64 wheel; verify ARM64 deps; disable CUDA-only attention. |
| [dia](https://github.com/pinokiofactory/dia) | [17e1912](https://github.com/pinokiofactory/dia/commit/17e1912e77363efc198d52a5ae813caaa8d3da90) | Feasible (ARM64 wheels) | Possible via ONNX export + DirectML/QNN-GPU (conversion required) | Possible via ONNX export + QNN HTP | Use PyTorch 2.7+ win_arm64 wheel; verify ARM64 deps; disable CUDA-only attention. |
| [diamond](https://github.com/pinokiofactory/diamond) | [3509823](https://github.com/pinokiofactory/diamond/commit/35098236144ee378454ede9cc7e1a1316d65cf8c) | Feasible (ARM64 wheels) | Possible via ONNX export + DirectML/QNN-GPU (conversion required) | Possible via ONNX export + QNN HTP | Use PyTorch 2.7+ win_arm64 wheel; verify ARM64 deps; disable CUDA-only attention. |
| [diffrhythm](https://github.com/pinokiofactory/diffrhythm) | [15166cf](https://github.com/pinokiofactory/diffrhythm/commit/15166cfd3b677d7fd6294b4d9fb88e7f4845d3ee) | Feasible (ARM64 wheels) | Possible via ONNX export + DirectML/QNN-GPU (conversion required) | Possible via QNN HTP after dequant/upcast (FP8/4-bit) | Use PyTorch 2.7+ win_arm64 wheel; verify ARM64 deps; disable CUDA-only attention. |
| [diffusers-image-fill](https://github.com/pinokiofactory/diffusers-image-fill) | [a8b6497](https://github.com/pinokiofactory/diffusers-image-fill/commit/a8b6497483d956df7ca1ffc882bf29af03476a26) | Feasible (ARM64 wheels) | Possible via ONNX export + DirectML/QNN-GPU (conversion required) | Possible via ONNX export + QNN HTP | Use PyTorch 2.7+ win_arm64 wheel; verify ARM64 deps; disable CUDA-only attention. |
| [e2-f5-tts](https://github.com/pinokiofactory/e2-f5-tts) | [f871e54](https://github.com/pinokiofactory/e2-f5-tts/commit/f871e54167835552efa88b366388b299f50c36af) | Feasible (ARM64 wheels) | Possible via ONNX export + DirectML/QNN-GPU (conversion required) | Possible via ONNX export + QNN HTP | Use PyTorch 2.7+ win_arm64 wheel; verify ARM64 deps; disable CUDA-only attention. |
| [facepoke](https://github.com/pinokiofactory/facepoke) | [f3a8c96](https://github.com/pinokiofactory/facepoke/commit/f3a8c9610834b51b64069f3bce9b1da3a321e620) | Feasible (ARM64 wheels) | Possible via ONNX export + DirectML/QNN-GPU (conversion required) | Possible via ONNX export + QNN HTP | Use PyTorch 2.7+ win_arm64 wheel; verify ARM64 deps; disable CUDA-only attention. |
| [flashdiffusion](https://github.com/pinokiofactory/flashdiffusion) | [c61d186](https://github.com/pinokiofactory/flashdiffusion/commit/c61d18626e05f89335aca054a34cbbd6703d5b6b) | Feasible (ARM64 wheels) | Possible via ONNX export + DirectML/QNN-GPU (conversion required) | Possible via ONNX export + QNN HTP | Use PyTorch 2.7+ win_arm64 wheel; verify ARM64 deps; disable CUDA-only attention. |
| [florence-sam](https://github.com/pinokiofactory/florence-sam) | [3cca86f](https://github.com/pinokiofactory/florence-sam/commit/3cca86f7edf8e94daae4339727f202895306c021) | Feasible (ARM64 wheels) | Possible via ONNX export + DirectML/QNN-GPU (conversion required) | Possible via ONNX export + QNN HTP | Use PyTorch 2.7+ win_arm64 wheel; verify ARM64 deps; disable CUDA-only attention. |
| [florence2](https://github.com/pinokiofactory/florence2) | [5b517ac](https://github.com/pinokiofactory/florence2/commit/5b517ac86c59d3b8a28a5d75c3aba34e2aa2e3b6) | Feasible (ARM64 wheels) | Possible via ONNX export + DirectML/QNN-GPU (conversion required) | Possible via ONNX export + QNN HTP | Use PyTorch 2.7+ win_arm64 wheel; verify ARM64 deps; disable CUDA-only attention. |
| [flux-webui](https://github.com/pinokiofactory/flux-webui) | [62d2f56](https://github.com/pinokiofactory/flux-webui/commit/62d2f5692da1e0aaf776c3dceef0a720a6a24bb6) | Feasible (ARM64 wheels) | Possible via ONNX export + DirectML/QNN-GPU (conversion required) | Possible via ONNX export + QNN HTP | Use PyTorch 2.7+ win_arm64 wheel; verify ARM64 deps; disable CUDA-only attention. |
| [hallo](https://github.com/pinokiofactory/hallo) | [c72097c](https://github.com/pinokiofactory/hallo/commit/c72097c6c23be58e7435bc48fbe9d0be5d0da1e5) | Feasible (ARM64 wheels) | Possible via ONNX export + DirectML/QNN-GPU (conversion required) | Possible via QNN HTP after dequant/upcast (FP8/4-bit) | Use PyTorch 2.7+ win_arm64 wheel; verify ARM64 deps; disable CUDA-only attention. |
| [hertz](https://github.com/pinokiofactory/hertz) | [306ecc6](https://github.com/pinokiofactory/hertz/commit/306ecc634eea5a51a3d20729d44cc94f5650d45d) | Feasible (ARM64 wheels) | Possible via ONNX export + DirectML/QNN-GPU (conversion required) | Possible via ONNX export + QNN HTP | Use PyTorch 2.7+ win_arm64 wheel; verify ARM64 deps; disable CUDA-only attention. |
| [instantir](https://github.com/pinokiofactory/instantir) | [98901ae](https://github.com/pinokiofactory/instantir/commit/98901aecae33b014e3fbd0f672706a506918c7f1) | Feasible (ARM64 wheels) | Possible via ONNX export + DirectML/QNN-GPU (conversion required) | Possible via ONNX export + QNN HTP | Use PyTorch 2.7+ win_arm64 wheel; verify ARM64 deps; disable CUDA-only attention. |
| [invoke](https://github.com/pinokiofactory/invoke) | [67ac5a1](https://github.com/pinokiofactory/invoke/commit/67ac5a161a265badb1ff73d46c41f762c16bff35) | Feasible (ARM64 wheels) | Possible via ONNX export + DirectML/QNN-GPU (conversion required) | Possible via ONNX export + QNN HTP | Use PyTorch 2.7+ win_arm64 wheel; verify ARM64 deps; disable CUDA-only attention. |
| [janus](https://github.com/pinokiofactory/janus) | [6332de0](https://github.com/pinokiofactory/janus/commit/6332de02fce4540acfea094435af331903120c69) | Feasible (ARM64 wheels) | Possible via ONNX export + DirectML/QNN-GPU (conversion required) | Possible via ONNX export + QNN HTP | Use PyTorch 2.7+ win_arm64 wheel; verify ARM64 deps; disable CUDA-only attention. |
| [liveportrait](https://github.com/pinokiofactory/liveportrait) | [b5fb16c](https://github.com/pinokiofactory/liveportrait/commit/b5fb16ce6df50e79d11d7c1a2d7b39faa720411e) | Feasible (ARM64 wheels) | Possible via ONNX export + DirectML/QNN-GPU (conversion required) | Possible via ONNX export + QNN HTP | Use PyTorch 2.7+ win_arm64 wheel; verify ARM64 deps; disable CUDA-only attention. |
| [llamafactory](https://github.com/pinokiofactory/llamafactory) | [e299b25](https://github.com/pinokiofactory/llamafactory/commit/e299b25b26f48bb6ef96a670c2da402f0e328441) | Feasible (ARM64 wheels) | Possible via ONNX export + DirectML/QNN-GPU (conversion required) | Possible via ONNX export; GGUF not NPU-native | Use PyTorch 2.7+ win_arm64 wheel; verify ARM64 deps; disable CUDA-only attention. |
| [mochi](https://github.com/pinokiofactory/mochi) | [93d4b2b](https://github.com/pinokiofactory/mochi/commit/93d4b2bddb16f3ce883f47336f1de7c126955d6e) | Feasible (ARM64 wheels) | Possible via ONNX export + DirectML/QNN-GPU (conversion required) | Possible via ONNX export + QNN HTP | Use PyTorch 2.7+ win_arm64 wheel; verify ARM64 deps; disable CUDA-only attention. |
| [oasis](https://github.com/pinokiofactory/oasis) | [a84069d](https://github.com/pinokiofactory/oasis/commit/a84069d12ae3165aa0c8c955f9a93314ecf3d3d8) | Feasible (ARM64 wheels) | Possible via ONNX export + DirectML/QNN-GPU (conversion required) | Possible via ONNX export + QNN HTP | Use PyTorch 2.7+ win_arm64 wheel; verify ARM64 deps; disable CUDA-only attention. |
| [ominicontrol](https://github.com/pinokiofactory/ominicontrol) | [2c9e78d](https://github.com/pinokiofactory/ominicontrol/commit/2c9e78d353de3a48ea5adb83c618081bb2be71db) | Feasible (ARM64 wheels) | Possible via ONNX export + DirectML/QNN-GPU (conversion required) | Possible via ONNX export + QNN HTP | Use PyTorch 2.7+ win_arm64 wheel; verify ARM64 deps; disable CUDA-only attention. |
| [omnigen](https://github.com/pinokiofactory/omnigen) | [07de8c2](https://github.com/pinokiofactory/omnigen/commit/07de8c2c3944d3852bcab55d2f2c4d74bd245532) | Feasible (ARM64 wheels) | Possible via ONNX export + DirectML/QNN-GPU (conversion required) | Possible via ONNX export + QNN HTP | Use PyTorch 2.7+ win_arm64 wheel; verify ARM64 deps; disable CUDA-only attention. |
| [omniparser](https://github.com/pinokiofactory/omniparser) | [b2f7de9](https://github.com/pinokiofactory/omniparser/commit/b2f7de9607dcc3087229feaee36c6c2f0345fc80) | Feasible (ARM64 wheels) | Possible via ONNX export + DirectML/QNN-GPU (conversion required) | Possible via ONNX export + QNN HTP | Use PyTorch 2.7+ win_arm64 wheel; verify ARM64 deps; disable CUDA-only attention. |
| [openaudio](https://github.com/pinokiofactory/openaudio) | [6a69e79](https://github.com/pinokiofactory/openaudio/commit/6a69e7903d7430cc3d08dae6673caf85b9032fcf) | Feasible (ARM64 wheels) | Possible via ONNX export + DirectML/QNN-GPU (conversion required) | Possible via ONNX export + QNN HTP | Use PyTorch 2.7+ win_arm64 wheel; verify ARM64 deps; disable CUDA-only attention. |
| [ovis](https://github.com/pinokiofactory/ovis) | [00a5702](https://github.com/pinokiofactory/ovis/commit/00a570258ba7370090037bb14bcfa67e1e81194e) | Feasible (ARM64 wheels) | Possible via ONNX export + DirectML/QNN-GPU (conversion required) | Possible via ONNX export + QNN HTP | Use PyTorch 2.7+ win_arm64 wheel; verify ARM64 deps; disable CUDA-only attention. |
| [pcm](https://github.com/pinokiofactory/pcm) | [1902e63](https://github.com/pinokiofactory/pcm/commit/1902e63160c5626aa0b14f0a1279f8c59a6239c1) | Feasible (ARM64 wheels) | Possible via ONNX export + DirectML/QNN-GPU (conversion required) | Possible via ONNX export + QNN HTP | Use PyTorch 2.7+ win_arm64 wheel; verify ARM64 deps; disable CUDA-only attention. |
| [photomaker2](https://github.com/pinokiofactory/photomaker2) | [2c48cd3](https://github.com/pinokiofactory/photomaker2/commit/2c48cd3f30a305069aad6de30bfe4c3f0fe900f7) | Feasible (ARM64 wheels) | Possible via ONNX export + DirectML/QNN-GPU (conversion required) | Possible via ONNX export + QNN HTP | Use PyTorch 2.7+ win_arm64 wheel; verify ARM64 deps; disable CUDA-only attention. |
| [pyramidflow](https://github.com/pinokiofactory/pyramidflow) | [6ae7e61](https://github.com/pinokiofactory/pyramidflow/commit/6ae7e61806478b430473c2a6ce9866525e3cd1a2) | Feasible (ARM64 wheels) | Possible via ONNX export + DirectML/QNN-GPU (conversion required) | Possible via ONNX export + QNN HTP | Use PyTorch 2.7+ win_arm64 wheel; verify ARM64 deps; disable CUDA-only attention. |
| [rc-stableaudio](https://github.com/pinokiofactory/rc-stableaudio) | [b3a7d5a](https://github.com/pinokiofactory/rc-stableaudio/commit/b3a7d5abecbee8fed08717405830126911825e81) | Feasible (ARM64 wheels) | Possible via ONNX export + DirectML/QNN-GPU (conversion required) | Possible via ONNX export + QNN HTP | Use PyTorch 2.7+ win_arm64 wheel; verify ARM64 deps; disable CUDA-only attention. |
| [sd35](https://github.com/pinokiofactory/sd35) | [1e820d7](https://github.com/pinokiofactory/sd35/commit/1e820d785879752bf27626cce260c49cdbfe149d) | Feasible (ARM64 wheels) | Possible via ONNX export + DirectML/QNN-GPU (conversion required) | Possible via ONNX export + QNN HTP | Use PyTorch 2.7+ win_arm64 wheel; verify ARM64 deps; disable CUDA-only attention. |
| [stable-diffusion-webui-forge](https://github.com/pinokiofactory/stable-diffusion-webui-forge) | [e44fda2](https://github.com/pinokiofactory/stable-diffusion-webui-forge/commit/e44fda22458c495919a1c90ed9e7d5c63c37adfb) | Feasible (ARM64 wheels) | Possible via ONNX export + DirectML/QNN-GPU (conversion required) | Possible via QNN HTP after dequant/upcast (FP8/4-bit) | Use PyTorch 2.7+ win_arm64 wheel; verify ARM64 deps; disable CUDA-only attention. |
| [stable-fast-3d](https://github.com/pinokiofactory/stable-fast-3d) | [00fdb29](https://github.com/pinokiofactory/stable-fast-3d/commit/00fdb293b784f223c100971f37a23f2e8a801654) | Feasible (ARM64 wheels) | Possible via ONNX export + DirectML/QNN-GPU (conversion required) | Possible via ONNX export + QNN HTP | Use PyTorch 2.7+ win_arm64 wheel; verify ARM64 deps; disable CUDA-only attention. |
| [stableaudio](https://github.com/pinokiofactory/stableaudio) | [14c9fbb](https://github.com/pinokiofactory/stableaudio/commit/14c9fbb56ef0054d8fae55bcee825216d30be047) | Feasible (ARM64 wheels) | Possible via ONNX export + DirectML/QNN-GPU (conversion required) | Possible via ONNX export + QNN HTP | Use PyTorch 2.7+ win_arm64 wheel; verify ARM64 deps; disable CUDA-only attention. |
| [text2midi](https://github.com/pinokiofactory/text2midi) | [8e5f742](https://github.com/pinokiofactory/text2midi/commit/8e5f742a1313c9b6f89bcf779fd0f4cf798864b7) | Feasible (ARM64 wheels) | Possible via ONNX export + DirectML/QNN-GPU (conversion required) | Possible via ONNX export + QNN HTP | Use PyTorch 2.7+ win_arm64 wheel; verify ARM64 deps; disable CUDA-only attention. |
| [uno](https://github.com/pinokiofactory/uno) | [6f19067](https://github.com/pinokiofactory/uno/commit/6f190672a75ccadd481a5cd69db95ed392ede8c0) | Feasible (ARM64 wheels) | Possible via ONNX export + DirectML/QNN-GPU (conversion required) | Possible via QNN HTP after dequant/upcast (FP8/4-bit) | Use PyTorch 2.7+ win_arm64 wheel; verify ARM64 deps; disable CUDA-only attention. |
| [vibevoice-realtime](https://github.com/pinokiofactory/vibevoice-realtime) | [e8f4b7b](https://github.com/pinokiofactory/vibevoice-realtime/commit/e8f4b7bd22f65e45b19cd4e67cd0c1a982109102) | Feasible (ARM64 wheels) | Possible via ONNX export + DirectML/QNN-GPU (conversion required) | Possible via ONNX export + QNN HTP | Use PyTorch 2.7+ win_arm64 wheel; verify ARM64 deps; disable CUDA-only attention. |
| [video-background-removal](https://github.com/pinokiofactory/video-background-removal) | [975e13e](https://github.com/pinokiofactory/video-background-removal/commit/975e13e9f5f659fcebba10d1a4e7a00034d6223f) | Feasible (ARM64 wheels) | Possible via ONNX export + DirectML/QNN-GPU (conversion required) | Possible via ONNX export + QNN HTP | Use PyTorch 2.7+ win_arm64 wheel; verify ARM64 deps; disable CUDA-only attention. |
| [wan](https://github.com/pinokiofactory/wan) | [8ed1410](https://github.com/pinokiofactory/wan/commit/8ed14108ca7148a612c5eb9528b00ceac99810ff) | Feasible (ARM64 wheels) | Possible via ONNX export + DirectML/QNN-GPU (conversion required) | Possible via ONNX export; GGUF not NPU-native | Use PyTorch 2.7+ win_arm64 wheel; verify ARM64 deps; disable CUDA-only attention. |
| [whisper-webui](https://github.com/pinokiofactory/whisper-webui) | [5b6ebed](https://github.com/pinokiofactory/whisper-webui/commit/5b6ebed2652d7adb7608ebe5c82ed01619e10daf) | Feasible (ARM64 wheels) | Possible via ONNX export + DirectML/QNN-GPU (conversion required) | Possible via ONNX export + QNN HTP | Use PyTorch 2.7+ win_arm64 wheel; verify ARM64 deps; disable CUDA-only attention. |
| [z-image-turbo](https://github.com/pinokiofactory/z-image-turbo) | [54899fd](https://github.com/pinokiofactory/z-image-turbo/commit/54899fdb5c023072de43c8b91ad2b0f0bee5b5c4) | Feasible (ARM64 wheels) | Possible via ONNX export + DirectML/QNN-GPU (conversion required) | Possible via ONNX export + QNN HTP | Use PyTorch 2.7+ win_arm64 wheel; verify ARM64 deps; disable CUDA-only attention. |
| [zonos](https://github.com/pinokiofactory/zonos) | [0be13e4](https://github.com/pinokiofactory/zonos/commit/0be13e4e803fe0834bae8326240633ac8e53bffc) | Feasible (ARM64 wheels) | Possible via ONNX export + DirectML/QNN-GPU (conversion required) | Possible via QNN HTP after dequant/upcast (FP8/4-bit) | Use PyTorch 2.7+ win_arm64 wheel; verify ARM64 deps; disable CUDA-only attention. |
| [ACE-Step](https://github.com/pinokiofactory/ACE-Step) | [8cf2fac](https://github.com/pinokiofactory/ACE-Step/commit/8cf2fac2765b1383e6d078b399acc3e38374949e) | Needs launcher change | Possible via ONNX export + DirectML/QNN-GPU (conversion required) | Possible via ONNX export + QNN HTP | Add ARM64/CPU wheel branch; remove GPU-only flags. |
| [Allegro-txt2vid-install](https://github.com/pinokiofactory/Allegro-txt2vid-install) | [6000ff1](https://github.com/pinokiofactory/Allegro-txt2vid-install/commit/6000ff1e395f6238eaa89e68b45a571e84d324e1) | Needs launcher change | Possible via ONNX export + DirectML/QNN-GPU (conversion required) | Possible via ONNX export + QNN HTP | Add ARM64/CPU wheel branch; remove GPU-only flags. |
| [LTX-Desktop-WanGP](https://github.com/pinokiofactory/LTX-Desktop-WanGP) | [2a3fedd](https://github.com/pinokiofactory/LTX-Desktop-WanGP/commit/2a3fedd030e9c7c12f9f67a14466007319ecc3d5) | Needs launcher change | Possible via ONNX export + DirectML/QNN-GPU (conversion required) | Possible via ONNX export + QNN HTP | Add ARM64/CPU wheel branch; remove GPU-only flags. |
| [RuinedFooocus](https://github.com/pinokiofactory/RuinedFooocus) | [cd74193](https://github.com/pinokiofactory/RuinedFooocus/commit/cd741937b44a7f1625acf35250ebf1bc6521dbb2) | Needs launcher change | Possible via ONNX export + DirectML/QNN-GPU (conversion required) | Possible via ONNX export; GGUF not NPU-native | Add ARM64/CPU wheel branch; remove GPU-only flags. |
| [applio-old](https://github.com/pinokiofactory/applio-old) | [a8d276c](https://github.com/pinokiofactory/applio-old/commit/a8d276c8f426304428755974392b5e42d4ef29a5) | Needs launcher change | Possible via ONNX export + DirectML/QNN-GPU (conversion required) | Possible via ONNX export + QNN HTP | Add ARM64/CPU wheel branch; remove GPU-only flags. |
| [dough](https://github.com/pinokiofactory/dough) | [3e8a58b](https://github.com/pinokiofactory/dough/commit/3e8a58b5da380ec15cd5743ffc57d220a64fdae1) | Needs launcher change | Possible via ONNX export + DirectML/QNN-GPU (conversion required) | Possible via ONNX export + QNN HTP | Add ARM64/CPU wheel branch; remove GPU-only flags. |
| [echomimic2](https://github.com/pinokiofactory/echomimic2) | [eb7915a](https://github.com/pinokiofactory/echomimic2/commit/eb7915a14420505c7c8b929a2dbba570f1639831) | Needs launcher change | Possible via ONNX export + DirectML/QNN-GPU (conversion required) | Possible via ONNX export + QNN HTP | Add ARM64/CPU wheel branch; remove GPU-only flags. |
| [forge](https://github.com/pinokiofactory/forge) | [e3378c3](https://github.com/pinokiofactory/forge/commit/e3378c35f7f1c4fec2f600c33b9d17ab6d330b4c) | Needs launcher change | Possible via ONNX export + DirectML/QNN-GPU (conversion required) | Possible via ONNX export + QNN HTP | Add ARM64/CPU wheel branch; remove GPU-only flags. |
| [yue](https://github.com/pinokiofactory/yue) | [3261118](https://github.com/pinokiofactory/yue/commit/3261118f111c8d2bb098b82b2870458dfbc486c7) | Needs launcher change | Possible via ONNX export + DirectML/QNN-GPU (conversion required) | Possible via ONNX export + QNN HTP | Add ARM64/CPU wheel branch; remove GPU-only flags. |
| [Allegro-txt2vid](https://github.com/pinokiofactory/Allegro-txt2vid) | [f8327e3](https://github.com/pinokiofactory/Allegro-txt2vid/commit/f8327e3172834ee8d932d7284641a5e9a0065cbc) | Blocked | Blocked (CUDA extension) | Blocked unless CUDA component replaced | TensorRT/compiled CUDA extension or CUDA-required source path. |
| [StreamDiffusion](https://github.com/pinokiofactory/StreamDiffusion) | [0e529aa](https://github.com/pinokiofactory/StreamDiffusion/commit/0e529aaff2ff344ce15565420e0c484688eb1bc9) | Blocked | Blocked (CUDA extension) | Blocked unless CUDA component replaced | TensorRT/compiled CUDA extension or CUDA-required source path. |
| [TRELLIS](https://github.com/pinokiofactory/TRELLIS) | [3d6dec1](https://github.com/pinokiofactory/TRELLIS/commit/3d6dec1fada102cba537ce7f6926061b0af7b962) | Blocked | Blocked (CUDA extension) | Blocked unless CUDA component replaced | TensorRT/compiled CUDA extension or CUDA-required source path. |
| [ai-toolkit](https://github.com/pinokiofactory/ai-toolkit) | [ddfefd7](https://github.com/pinokiofactory/ai-toolkit/commit/ddfefd70eb6f9d0b97c95e30b5c72aaac8660b0e) | Blocked | Blocked (CUDA extension) | Blocked unless CUDA component replaced | TensorRT/compiled CUDA extension or CUDA-required source path. |
| [hunyuanvideo](https://github.com/pinokiofactory/hunyuanvideo) | [c65cb77](https://github.com/pinokiofactory/hunyuanvideo/commit/c65cb772466eea61e0a330f52ed7764a9d4e821d) | Blocked | Blocked (CUDA extension) | Blocked unless CUDA component replaced | TensorRT/compiled CUDA extension or CUDA-required source path. |
| [MFLUX-WEBUI](https://github.com/pinokiofactory/MFLUX-WEBUI) | [62b3f93](https://github.com/pinokiofactory/MFLUX-WEBUI/commit/62b3f9364abf53951cfdfb3c2e872d470d5baa4a) | Unsuitable (MLX) | Unsuitable (MLX) | Unsuitable (MLX/Apple-only) | MLX runtime; not available on Windows ARM64. |
| [SongGeneration-Studio-MLX](https://github.com/pinokiofactory/SongGeneration-Studio-MLX) | [49e365c](https://github.com/pinokiofactory/SongGeneration-Studio-MLX/commit/49e365c88512ffd1a4bf17d800c5508e7d5781da) | Unsuitable (MLX) | Unsuitable (MLX) | Unsuitable (MLX/Apple-only) | MLX runtime; not available on Windows ARM64. |
| [mlx](https://github.com/pinokiofactory/mlx) | [eedc5a1](https://github.com/pinokiofactory/mlx/commit/eedc5a1a3f57fbd7d78ad36d3f934b20372fac4c) | Unsuitable (MLX) | Unsuitable (MLX) | Unsuitable (MLX/Apple-only) | MLX runtime; not available on Windows ARM64. |
| [mlx-video-transcription](https://github.com/pinokiofactory/mlx-video-transcription) | [331245a](https://github.com/pinokiofactory/mlx-video-transcription/commit/331245a916c9eb1602637a5cedebf83eb2322ee5) | Unsuitable (MLX) | Unsuitable (MLX) | Unsuitable (MLX/Apple-only) | MLX runtime; not available on Windows ARM64. |
| [mlx-video-ui](https://github.com/pinokiofactory/mlx-video-ui) | [2f91ff7](https://github.com/pinokiofactory/mlx-video-ui/commit/2f91ff7c3749a11dfcb3ed3e555a375cb5400421) | Unsuitable (MLX) | Unsuitable (MLX) | Unsuitable (MLX/Apple-only) | MLX runtime; not available on Windows ARM64. |
| [moshi](https://github.com/pinokiofactory/moshi) | [485d527](https://github.com/pinokiofactory/moshi/commit/485d527a4d8a57e99e58b4735b61b5fb300d2aa3) | Unsuitable (MLX) | Unsuitable (MLX) | Unsuitable (MLX/Apple-only) | MLX runtime; not available on Windows ARM64. |
| [y](https://github.com/pinokiofactory/y) | N/A | N/A | N/A | N/A (empty repository) | Empty repository. |
| [factory](https://github.com/pinokiofactory/factory) | N/A | N/A | N/A | N/A (empty repository) | Empty repository. |

## Recommended Snapdragon porting paths

1. **CPU-first (Oryon):** Start with CPU-native and CPU-capable apps; install native ARM64 Python 3.12 and PyTorch 2.7+ CPU wheels; use WSL2 for full-stack training.
2. **GPU (Adreno):** Only after an ONNX export exists; validate with DirectML EP or QNN GPU backend; expect operator gaps.
3. **NPU (Hexagon):** Convert to ONNX and quantize (QDQ) for QNN HTP; prefer QAIRT context binaries for large models; validate operator support and FP16 default behaviour.
4. **Avoid:** MLX-only apps and hard CUDA/TensorRT/compiled-extension apps unless a replacement backend is planned.

## Caveats

- This is a source-snapshot feasibility assessment, not a runtime benchmark on the Snapdragon device.
- Native wheel availability is necessary but not sufficient; transitive dependencies may still lack ARM64 wheels.
- Performance of large BF16/FP16 GEMMs on the Oryon CPU may be impractical without AVX512-BF16/FP16 or AMX equivalents; prefer quantized/ONNX paths for heavy models.
- QNN HTP runs FP32 models as FP16 by default and requires QDQ/quantized models for best results.
## Deep clone verification

- All 101 repository snapshots were shallow-cloned from their analyzed `main` commits and scanned for Snapdragon-relevant signals (CUDA, Torch, Triton, xformers, Flash/SageAttention, bitsandbytes, TensorRT, MLX/MPS, DirectML, GGUF, ONNX Runtime GPU, etc.).
- Per-repo clone/scan details and example evidence were appended to each `results/<repo>.md` under `## Snapdragon evaluation (deep clone)` and to `flows/<repo>.md` where present.
- Temporary clone directories were removed after each batch of 3.

## NPU precision and operator risks

| Precision / feature | NPU (QNN HTP) status | Risk / mitigation | Affected repos (examples) |
|---|---|---|---|
| FP32 | Supported (runs as FP16 by default on HTP) | Precision loss vs CPU/GPU FP32; use QDQ for INT8 if accuracy needed | Many (study-wide) |
| FP16 | Native / preferred | Good default for HTP | Most diffusion/LLM checkpoints |
| BF16 | Not consistently native on HTP | Convert/upcast to FP16 or INT8; validate accuracy | comfy, flux, wan, sd35, z-image-turbo |
| FP8 (F8_E4M3) | Not native in QNN HTP | Upcast to FP16/BF16 or use QAIRT context binary; memory grows | comfy, flux-webui, stable-diffusion-webui-forge |
| NF4 / bitsandbytes 4-bit | Packed UINT8 weights | Dequantize to FP16/BF16 before export; no native NF4 EP | comfy, forge, MagicQuill, llamafactory |
| GGUF / llama.cpp | Container format; CUDA loader wheels | Convert to ONNX/QNN context binary; not directly NPU-native | comfy, Orpheus-TTS-FastAPI, wan |
| FlashAttention / SageAttention / xformers | CUDA-only fused kernels | Replace with SDPA/eager attention or QNN-supported ops | 75 repos (xformers signal) |
| Triton / `@triton.jit` | CUDA/GPU kernels | Remove or replace with ONNX ops; no Triton on HTP | 28 repos (triton signal) |
| TensorRT / CUDA Graphs / compiled extensions | Hard blockers | Replace with ONNX Runtime CPU/QNN path | StreamDiffusion, TRELLIS, ai-toolkit, etc. |
| Dynamic shapes / very large context | May fail HTP graph compilation | Fix input shapes, use context binary, enable CPU fallback | LLM/diffusion apps |

**Bottom line:** NPU is realistic for FP16/INT8 ONNX models with standard ops; FP8/NF4/BF16 and fused CUDA attention require conversion and accuracy checks.

## At-risk apps and models (NPU)

| App | Risk tags | Models / notes |
|---|---|---|
| ACE-Step | CUDA/TensorRT/compiled-ext, Fused CUDA attention, Triton | — |
| AllTalk-TTS | Fused CUDA attention | — |
| Allegro-txt2vid-install | CUDA/TensorRT/compiled-ext, Fused CUDA attention, Triton | [AlexWortega/RIFE](https://huggingface.co/AlexWortega/RIFE) |
| Allegro-txt2vid | CUDA/TensorRT/compiled-ext, Fused CUDA attention, Triton | [AlexWortega/RIFE](https://huggingface.co/AlexWortega/RIFE), [PixArt-alpha/PixArt-alpha](https://huggingface.co/PixAr... |
| AudioX | CUDA/TensorRT/compiled-ext, Fused CUDA attention, Triton | [HKUSTAudio/AudioX](https://huggingface.co/HKUSTAudio/AudioX) |
| Frame-Pack | CUDA/TensorRT/compiled-ext, Fused CUDA attention, Triton | [hunyuanvideo-community/HunyuanVideo](https://huggingface.co/hunyuanvideo-community/HunyuanVideo), [lllyasviel/FrameP... |
| Hunyuan3D-2-mini | CUDA/TensorRT/compiled-ext, Fused CUDA attention | — |
| Hunyuan3D-2 | Fused CUDA attention | — |
| Hunyuan3d-2-lowvram | CUDA/TensorRT/compiled-ext, Fused CUDA attention, Triton | — |
| Ilaria-RVC | Fused CUDA attention | — |
| Kokoro-TTS | CUDA/TensorRT/compiled-ext, Fused CUDA attention, Triton | [hexgrad/Kokoro-82M](https://huggingface.co/hexgrad/Kokoro-82M) |
| LTX-Desktop-WanGP | MLX/Apple-only | — |
| MFLUX-WEBUI | MLX/Apple-only | — |
| MMAudio | Fused CUDA attention | — |
| MagicQuill | Fused CUDA attention, NF4/bitsandbytes | [LiuZichen/MagicQuill-models](https://huggingface.co/LiuZichen/MagicQuill-models) |
| MatAnyone | CUDA/TensorRT/compiled-ext, Fused CUDA attention, MLX/Apple-only, Triton | — |
| Nari-Dia-TTS | CUDA/TensorRT/compiled-ext, Fused CUDA attention, MLX/Apple-only, Triton | [nari-labs/Dia-1.6B](https://huggingface.co/nari-labs/Dia-1.6B) |
| Orpheus-TTS-FastAPI | Fused CUDA attention, GGUF | [lex-au/Orpheus-3b-FT-Q8_0.gguf](https://huggingface.co/lex-au/Orpheus-3b-FT-Q8_0.gguf) |
| RMBG-2-Studio | Fused CUDA attention, MLX/Apple-only | [briaai/RMBG-2.0](https://huggingface.co/briaai/RMBG-2.0) |
| RuinedFooocus | CUDA/TensorRT/compiled-ext, Fused CUDA attention, GGUF, Triton | — |
| SongGeneration-Studio-MLX | MLX/Apple-only | [AITRADER/SongGeneration-Large-MLX](https://huggingface.co/AITRADER/SongGeneration-Large-MLX) |
| StreamDiffusion | CUDA/TensorRT/compiled-ext, Fused CUDA attention, Triton | [KBlueLeaf/kohaku-v2.1](https://huggingface.co/KBlueLeaf/kohaku-v2.1), [latent-consistency/lcm-lora-sdv1-5](https://h... |
| StyleTTS2_Studio | Fused CUDA attention, MLX/Apple-only | — |
| TRELLIS | CUDA/TensorRT/compiled-ext, Fused CUDA attention, Triton | — |
| Ultimate-TTS-Studio | CUDA/TensorRT/compiled-ext, Fused CUDA attention, Triton | [cocktailpeanut/oa](https://huggingface.co/cocktailpeanut/oa) |
| accdiffusion | Fused CUDA attention, MLX/Apple-only | — |
| ai-toolkit | CUDA/TensorRT/compiled-ext, Triton | — |
| ai-video-composer | CUDA/TensorRT/compiled-ext, Fused CUDA attention, MLX/Apple-only, NF4/bitsandbytes, Triton | — |
| applio | Fused CUDA attention, MLX/Apple-only | — |
| artist | Fused CUDA attention | — |
| audiocraft_plus | CUDA/TensorRT/compiled-ext, Fused CUDA attention, Triton | — |
| augmentoolkit | Fused CUDA attention | — |
| aura-sr-upscaler | CUDA/TensorRT/compiled-ext, Fused CUDA attention, Triton | — |
| autogpt | Fused CUDA attention | — |
| bolt | CUDA/TensorRT/compiled-ext, Fused CUDA attention, MLX/Apple-only, NF4/bitsandbytes, Triton | — |
| browser-use | CUDA/TensorRT/compiled-ext, Fused CUDA attention, MLX/Apple-only, NF4/bitsandbytes, Triton | — |
| clarity-refiners-ui | CUDA/TensorRT/compiled-ext, Fused CUDA attention, Triton | [multimodalart/Florence-2-large-no-flash-attn](https://huggingface.co/multimodalart/Florence-2-large-no-flash-attn), ... |
| cogstudio | CUDA/TensorRT/compiled-ext, Fused CUDA attention, Triton | [AlexWortega/RIFE](https://huggingface.co/AlexWortega/RIFE), [THUDM/CogVideoX-2B](https://huggingface.co/THUDM/CogVid... |
| cogvideo | CUDA/TensorRT/compiled-ext, Fused CUDA attention, Triton | — |
| comfy | CUDA/TensorRT/compiled-ext, FP8, Fused CUDA attention, GGUF, NF4/bitsandbytes, Triton | [Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged), [Comfy-Org/flux1... |
| controlyourself | MLX/Apple-only | — |
| cube | Fused CUDA attention | [Roblox/cube3d-v0.1](https://huggingface.co/Roblox/cube3d-v0.1) |
| dia | CUDA/TensorRT/compiled-ext, Fused CUDA attention, Triton | — |
| diamond | Fused CUDA attention, MLX/Apple-only | — |
| diffrhythm | CUDA/TensorRT/compiled-ext, Fused CUDA attention, NF4/bitsandbytes, Triton | — |
| diffusers-image-fill | Fused CUDA attention, MLX/Apple-only | — |
| ditto | MLX/Apple-only | — |
| e2-f5-tts | Fused CUDA attention, MLX/Apple-only | — |
| echomimic2 | CUDA/TensorRT/compiled-ext, Fused CUDA attention, Triton | [BadToBest/EchoMimicV2](https://huggingface.co/BadToBest/EchoMimicV2), [cocktailpeanut/audio_processor](https://huggi... |
| errortest | CUDA/TensorRT/compiled-ext, Triton | — |
| facepoke | Fused CUDA attention | — |
| factory | MLX/Apple-only | — |
| flashdiffusion | Fused CUDA attention | — |
| florence-sam | Fused CUDA attention, MLX/Apple-only | — |
| florence2 | CUDA/TensorRT/compiled-ext, Fused CUDA attention, Triton | — |
| flux-webui | CUDA/TensorRT/compiled-ext, Fused CUDA attention, Triton | [black-forest-labs/FLUX.1-schnell](https://huggingface.co/black-forest-labs/FLUX.1-schnell), [cocktailpeanut/flux1-me... |
| forge | MLX/Apple-only | [cocktailpeanut/sv](https://huggingface.co/cocktailpeanut/sv), [latent-consistency/lcm-lora-sdxl](https://huggingface... |
| hallo | Fused CUDA attention, NF4/bitsandbytes | [fudan-generative-ai/hallo](https://huggingface.co/fudan-generative-ai/hallo) |
| hertz | CUDA/TensorRT/compiled-ext, Fused CUDA attention, Triton | — |
| hunyuanvideo | CUDA/TensorRT/compiled-ext, Fused CUDA attention, Triton | — |
| instantir | Fused CUDA attention, MLX/Apple-only | — |
| janus | Fused CUDA attention | — |
| liveportrait | CUDA/TensorRT/compiled-ext, Fused CUDA attention, MLX/Apple-only | [KwaiVGI/LivePortrait](https://huggingface.co/KwaiVGI/LivePortrait), [cleardusk/LivePortrait-Windows](https://hugging... |
| llamafactory | Fused CUDA attention, GGUF, NF4/bitsandbytes | — |
| macOS-use | MLX/Apple-only | — |
| mcp | MLX/Apple-only | — |
| mlx-video-transcription | MLX/Apple-only | — |
| mlx-video-ui | MLX/Apple-only | — |
| mlx | Fused CUDA attention, MLX/Apple-only | — |
| mochi | CUDA/TensorRT/compiled-ext, Fused CUDA attention, Triton | [genmo/mochi-1-preview](https://huggingface.co/genmo/mochi-1-preview) |
| moshi | Fused CUDA attention, MLX/Apple-only | — |
| oasis | Fused CUDA attention | [cocktailpeanut/sisao](https://huggingface.co/cocktailpeanut/sisao) |
| ominicontrol | Fused CUDA attention | — |
| omnigen | CUDA/TensorRT/compiled-ext, Fused CUDA attention, Triton | — |
| omniparser | Fused CUDA attention | [microsoft/OmniParser](https://huggingface.co/microsoft/OmniParser) |
| open-webui | MLX/Apple-only | — |
| openaudio | CUDA/TensorRT/compiled-ext, Fused CUDA attention, Triton | — |
| openui | MLX/Apple-only | — |
| ovis | CUDA/TensorRT/compiled-ext, MLX/Apple-only, Triton | [AIDC-AI/Ovis-Image-7B](https://huggingface.co/AIDC-AI/Ovis-Image-7B) |
| pcm | Fused CUDA attention | — |
| photomaker2 | Fused CUDA attention | — |
| pyramidflow | CUDA/TensorRT/compiled-ext, Fused CUDA attention, Triton | — |
| rc-stableaudio | CUDA/TensorRT/compiled-ext, Fused CUDA attention, Triton | — |
| sd35 | CUDA/TensorRT/compiled-ext, Fused CUDA attention, MLX/Apple-only, Triton | [cocktailpeanut/sd35](https://huggingface.co/cocktailpeanut/sd35), [cocktailpeanut/sd35turbo](https://huggingface.co/... |
| sillytavern | MLX/Apple-only | — |
| stable-diffusion-webui-forge | FP8, NF4/bitsandbytes | [XLabs-AI/flux-lora-collection](https://huggingface.co/XLabs-AI/flux-lora-collection), [cocktailpeanut/sv](https://hu... |
| stable-fast-3d | Fused CUDA attention | [cocktailpeanut/sf3d](https://huggingface.co/cocktailpeanut/sf3d) |
| stableaudio | Fused CUDA attention, MLX/Apple-only | — |
| text2midi | Fused CUDA attention | [amaai-lab/text2midi](https://huggingface.co/amaai-lab/text2midi) |
| uno | CUDA/TensorRT/compiled-ext, FP8, Fused CUDA attention, Triton | — |
| vibevoice-realtime | CUDA/TensorRT/compiled-ext, Triton | [microsoft/VibeVoice-Realtime-0.5B](https://huggingface.co/microsoft/VibeVoice-Realtime-0.5B) |
| video-background-removal | Fused CUDA attention, MLX/Apple-only | — |
| wan | CUDA/TensorRT/compiled-ext, Fused CUDA attention, GGUF, NF4/bitsandbytes, Triton | — |
| whisper-webui | Fused CUDA attention | — |
| y | MLX/Apple-only | — |
| yue | CUDA/TensorRT/compiled-ext, Fused CUDA attention, Triton | [m-a-p/xcodec_mini_infer](https://huggingface.co/m-a-p/xcodec_mini_infer) |
| z-image-turbo | CUDA/TensorRT/compiled-ext, Fused CUDA attention, MLX/Apple-only, Triton | [Tongyi-MAI/Z-Image-Turbo](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo) |
| zonos | CUDA/TensorRT/compiled-ext, Fused CUDA attention, NF4/bitsandbytes, Triton | — |
