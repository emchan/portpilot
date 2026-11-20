# Kernel libraries and accelerator APIs across Pinokio apps

Companion to [`results/pinokio-apps.md`](../results/pinokio-apps.md). This note records which of the 101 Pinokio Factory repositories actually reference CUDA Graphs, Triton, Vulkan, Metal Performance Shaders (MPS), and attention kernels (FlashAttention, SageAttention, xformers, PyTorch SDPA). Evidence comes from a case-insensitive scan of text files in a full snapshot of each repository; matches are cited as `file:line`. These are launcher repositories, so a symbol found in `torch.js`/`install.js` means the launcher installs or enables the library, while a symbol in `.py` code means the wrapper itself calls it. Absence of a match does **not** mean the upstream app lacks the kernel — it means the wrapper does not declare or call it directly. All snapshots were taken from the default branch `main` on 2026-11-20; the exact commit SHA analyzed for each repository is recorded in its `../results/<repo>.md` report.

## At a glance

| Signal | Repos | Examples |
| --- | --- | --- |
| CUDA Graphs | 1 | StreamDiffusion |
| Triton | 29 | ACE-Step, ai-toolkit, Allegro-txt2vid-install, audiocraft_plus, AudioX, aura-sr-upscaler … |
| Vulkan | 0 | none |
| Apple MPS | 11 | Allegro-txt2vid, diffusers-image-fill, flux-webui, Hunyuan3d-2-lowvram, MatAnyone, Nari-Dia-TTS … |
| Metal API (explicit) | 0 | none |
| MLX (Metal-based, not MPS) | 5 | MFLUX-WEBUI, mlx, mlx-video-transcription, mlx-video-ui, SongGeneration-Studio-MLX |
| FlashAttention | 19 | AudioX, aura-sr-upscaler, clarity-refiners-ui, cogvideo, comfy, florence2 … |
| SageAttention | 17 | ACE-Step, AudioX, aura-sr-upscaler, cogvideo, comfy, dia … |
| xformers | 75 | accdiffusion, ACE-Step, Allegro-txt2vid, Allegro-txt2vid-install, AllTalk-TTS, applio … |
| PyTorch SDPA | 2 | diffusers-image-fill, Nari-Dia-TTS |
| FlashInfer / vLLM | 0 | none |

## CUDA Graphs

Only **StreamDiffusion** contains CUDA Graph code, and it is confined to its TensorRT/Stable-Fast acceleration paths — not the Pinokio launcher itself. No other wrapper uses `CUDAGraph`, `torch.cuda.graph()`, `make_graphed_callables()`, `cudaGraphLaunch`, `cudaGraphInstantiate`, or stream-capture APIs.

| File | Line | Evidence |
| --- | --- | --- |
| src/streamdiffusion/acceleration/tensorrt/utilities.py | 270 | CUASSERT(cudart.cudaGraphLaunch(self.cuda_graph_instance, stream.ptr)) |
| src/streamdiffusion/acceleration/tensorrt/utilities.py | 273 | # do inference before CUDA graph capture |
| src/streamdiffusion/acceleration/tensorrt/utilities.py | 277 | # capture cuda graph |
| src/streamdiffusion/acceleration/tensorrt/utilities.py | 283 | self.cuda_graph_instance = CUASSERT(cudart.cudaGraphInstantiate(self.graph, 0)) |
| utils/wrapper.py | 608 | unet_path, cuda_stream, use_cuda_graph=False |
| utils/wrapper.py | 615 | use_cuda_graph=False, |
| src/streamdiffusion/acceleration/sfast/__init__.py | 27 | # CUDA Graph is suggested for small batch sizes and small resolutions to reduce CPU overhead. |
| src/streamdiffusion/acceleration/sfast/__init__.py | 28 | config.enable_cuda_graph = True |
| src/streamdiffusion/acceleration/tensorrt/engine.py | 13 | def __init__(self, filepath: str, stream: cuda.Stream, use_cuda_graph: bool = False): |
| src/streamdiffusion/acceleration/tensorrt/engine.py | 16 | self.use_cuda_graph = use_cuda_graph |
| src/streamdiffusion/acceleration/tensorrt/engine.py | 48 | use_cuda_graph=self.use_cuda_graph, |
| src/streamdiffusion/acceleration/tensorrt/engine.py | 66 | use_cuda_graph: bool = False, |

**Porting note:** CUDA Graph capture is NVIDIA-specific. On ROCm, HIP graphs exist but require rewriting capture/stream handling; on Apple MPS there is no equivalent capture API, so this path must be replaced by ordinary eager execution or a vendor-specific graph mechanism. StreamDiffusion is therefore the single hardest app in this collection for a non-NVIDIA port.

## Triton

29 repositories mention Triton. Only **[StreamDiffusion](https://github.com/pinokiofactory/StreamDiffusion), [zonos](https://github.com/pinokiofactory/zonos)** contain direct Python code; the rest only declare a `triton` / `triton-windows` wheel in `torch.js`, `install.js` or requirements, frequently behind an `args.triton` optional flag. No launcher defines a `@triton.jit` kernel.

| Project | How used | Files | Evidence |
| --- | --- | --- | --- |
| [ACE-Step](https://github.com/pinokiofactory/ACE-Step) | launcher install | install.js, torch.js | `torch.js:14` — "uv pip install triton-windows==3.3.1.post19" |
| [ai-toolkit](https://github.com/pinokiofactory/ai-toolkit) | launcher install | torch.js | `torch.js:12` — "uv pip install triton-windows==3.5.1.post22 --reinstall --no-deps" |
| [Allegro-txt2vid-install](https://github.com/pinokiofactory/Allegro-txt2vid-install) | launcher install | torch.js | `torch.js:12` — "uv pip install triton-windows==3.3.1.post19" |
| [audiocraft_plus](https://github.com/pinokiofactory/audiocraft_plus) | launcher install | torch.js | `torch.js:12` — "uv pip install triton-windows==3.3.1.post19" |
| [AudioX](https://github.com/pinokiofactory/AudioX) | optional flag + launcher install | install.js, torch.js | `torch.js:12` — "{{args && args.triton ? 'uv pip install -U --pre triton-windows' : ''}}", |
| [aura-sr-upscaler](https://github.com/pinokiofactory/aura-sr-upscaler) | optional flag + launcher install | torch.js | `torch.js:12` — "{{args && args.triton ? 'uv pip install triton-windows==3.3.1.post19' : ''}}", |
| [cogvideo](https://github.com/pinokiofactory/cogvideo) | optional flag + launcher install | torch.js | `torch.js:12` — "{{args && args.triton ? 'uv pip install triton-windows==3.3.1.post19' : ''}}", |
| [comfy](https://github.com/pinokiofactory/comfy) | optional flag + launcher install | h.js, torch.js | `h.js:63` — //          "{{platform === 'win32' ? 'pip install https://github.com/woct0rdho/triton-windows/releases/download/v3.0.0-windows.post3/triton-3.0.0-cp310-cp310-win... |
| [dia](https://github.com/pinokiofactory/dia) | optional flag + launcher install | install.js, torch.js | `torch.js:12` — "{{args && args.triton ? 'uv pip install triton-windows==3.3.1.post19' : ''}}", |
| [diffrhythm](https://github.com/pinokiofactory/diffrhythm) | optional flag + launcher install | install.js, torch.js | `torch.js:12` — "{{args && args.triton ? 'uv pip install triton-windows==3.3.1.post19' : ''}}" |
| [echomimic2](https://github.com/pinokiofactory/echomimic2) | optional flag + launcher install | install.js, torch.js | `torch.js:12` — "{{args && args.triton ? 'uv pip install triton-windows==3.3.1.post19' : ''}}", |
| [errortest](https://github.com/pinokiofactory/errortest) | mention/hint | test.js | `test.js:15` — //          "event": "/error:.*triton/i", |
| [flux-webui](https://github.com/pinokiofactory/flux-webui) | optional flag + launcher install | install.js, torch.js | `torch.js:12` — "{{args && args.triton ? 'uv pip install triton-windows==3.3.1.post19' : ''}}", |
| [Frame-Pack](https://github.com/pinokiofactory/Frame-Pack) | launcher install | install.js, torch.js | `torch.js:12` — "uv pip install triton-windows==3.3.1.post19", |
| [hunyuanvideo](https://github.com/pinokiofactory/hunyuanvideo) | optional flag + launcher install | install.js, torch.js | `torch.js:12` — "{{args && args.triton ? 'uv pip install triton-windows==3.3.1.post19' : ''}}", |
| [Nari-Dia-TTS](https://github.com/pinokiofactory/Nari-Dia-TTS) | optional flag + launcher install | install.js, torch.js | `torch.js:12` — "{{args && args.triton ? 'uv pip install -U --pre triton-windows' : ''}}", |
| [omnigen](https://github.com/pinokiofactory/omnigen) | optional flag + launcher install | install.js, torch.js | `torch.js:12` — "{{args && args.triton ? 'uv pip install triton-windows==3.3.1.post19' : ''}}", |
| [openaudio](https://github.com/pinokiofactory/openaudio) | optional flag + launcher install | torch.js | `torch.js:12` — "{{args && args.triton ? 'uv pip install triton-windows==3.3.1.post19' : ''}}", |
| [pyramidflow](https://github.com/pinokiofactory/pyramidflow) | optional flag + launcher install | torch.js | `torch.js:12` — "{{args && args.triton ? 'uv pip install triton-windows==3.3.1.post19' : ''}}" |
| [rc-stableaudio](https://github.com/pinokiofactory/rc-stableaudio) | optional flag + launcher install | torch.js | `torch.js:12` — "{{args && args.triton ? 'uv pip install triton-windows==3.3.1.post19' : ''}}", |
| [RuinedFooocus](https://github.com/pinokiofactory/RuinedFooocus) | optional flag + launcher install | install.js, torch.js | `torch.js:13` — "{{args && args.triton ? 'uv pip install -U --pre triton-windows' : ''}}", |
| [StreamDiffusion](https://github.com/pinokiofactory/StreamDiffusion) | direct code | src/streamdiffusion/acceleration/sfast/__init__.py | `src/streamdiffusion/acceleration/sfast/__init__.py:14` — # xformers and Triton are suggested for achieving best performance. |
| [TRELLIS](https://github.com/pinokiofactory/TRELLIS) | requirements | requirements-uv.txt, requirements.txt | `requirements-uv.txt:90` — #   triton |
| [Ultimate-TTS-Studio](https://github.com/pinokiofactory/Ultimate-TTS-Studio) | optional flag + launcher install | install.js, torch.js | `torch.js:13` — "{{args && args.triton ? 'uv pip install triton-windows==3.3.1.post19' : ''}}", |
| [uno](https://github.com/pinokiofactory/uno) | optional flag + launcher install | install.js, torch.js | `torch.js:12` — "{{args && args.triton ? 'uv pip install -U --pre triton-windows' : ''}}", |
| [wan](https://github.com/pinokiofactory/wan) | launcher install | torch.js | `torch.js:27` — 'uv pip install "triton-windows>=3.2,<3.3"', |
| [yue](https://github.com/pinokiofactory/yue) | optional flag + launcher install | install.js, torch.js | `torch.js:13` — "{{args && args.triton ? 'uv pip install triton-windows==3.3.1.post19' : ''}}", |
| [z-image-turbo](https://github.com/pinokiofactory/z-image-turbo) | optional flag + launcher install | torch.js | `torch.js:12` — "{{args && args.triton ? 'uv pip install triton-windows==3.3.1.post19' : ''}}", |
| [zonos](https://github.com/pinokiofactory/zonos) | direct code + launcher install | clear_cache.js, cpp.py, cpp_builder.py | `clear_cache.js:9` — const triton_cache_dir = path.resolve(homedir, ".triton/cache"); |

## Vulkan

**No Vulkan references were found in any of the 101 repositories.** The scan looked for `vulkan`, `VK_*` constants, `vk*` entry points (`vkCreateInstance`, `vkQueueSubmit`, …), and `vulkan-runtime`/`vulkan-headers`/`vulkan-loader` packages. AMD support in this collection is delivered through ROCm/HIP wheels or DirectML, not through Vulkan compute. Consequently there is no ready Vulkan compute path here to reuse for cross-vendor porting.

## Apple MPS and Metal

Eleven repositories reference MPS explicitly. Most use PyTorch's MPS device (`torch.backends.mps.is_available()`, `device="mps"`); Allegro and diffusers-image-fill include explicit MPS workarounds for attention masking. No repository calls `MetalPerformanceShaders`/`MPSGraph` directly, and no `.metal` shader or `MTL*` object was found.

| Project | How used | Evidence |
| --- | --- | --- |
| [Allegro-txt2vid](https://github.com/pinokiofactory/Allegro-txt2vid) | direct code | `allegro/pipelines/pipeline_allegro.py:257` — # duplicate text embeddings and attention mask for each generation per prompt, using mps friendly method<br>`allegro/pipelines/pipeline_allegro.py:287` — # duplicate unconditional embeddings for each generation per prompt, using mps friendly method |
| [diffusers-image-fill](https://github.com/pinokiofactory/diffusers-image-fill) | direct code | `controlnet_union.py:899` — is_mps = sample.device.type == "mps"<br>`pipeline_fill_sd_xl.py:236` — # duplicate text embeddings for each generation per prompt, using mps friendly method |
| [flux-webui](https://github.com/pinokiofactory/flux-webui) | direct code | `app.py:74` — if device == "mps":<br>`app.py:82` — if device == "mps": |
| [Hunyuan3d-2-lowvram](https://github.com/pinokiofactory/Hunyuan3d-2-lowvram) | direct code + optional flag | `start.js:5` — cmd = `python gradio_app.py {{args.model_path ? '--model_path ' + args.model_path : ''}} {{ args.subfolder ? '--subfolder ' + args.subfolder : ''}} --enable_t23d ... |
| [MatAnyone](https://github.com/pinokiofactory/MatAnyone) | direct code + optional flag | `app.py:53` — if hasattr(torch.backends, 'mps') and torch.backends.mps.is_available():<br>`app.py:54` — args.device = "mps" + gpu_str |
| [Nari-Dia-TTS](https://github.com/pinokiofactory/Nari-Dia-TTS) | direct code | `app.py:23` — "--device", type=str, default=None, help="Force device (e.g., 'cuda', 'mps', 'cpu')"<br>`app.py:35` — # Simplified MPS check for broader compatibility |
| [openaudio](https://github.com/pinokiofactory/openaudio) | optional flag | `start.js:14` — "python run_webui.py --device {{(platform === 'darwin' ? 'mps' : (gpu === 'nvidia' ? 'cuda' : 'cpu'))}}", |
| [ovis](https://github.com/pinokiofactory/ovis) | direct code | `README.md:11` — - Works on NVIDIA CUDA (fastest), Apple MPS, and CPU. CPU/MPS will be extremely slow and may OOM on modest hardware; the app auto-detects (prefers MPS on macOS, o...<br>`README.md:25` — - `Device` (`auto`, `cuda`, `mps`, `cpu`) |
| [sd35](https://github.com/pinokiofactory/sd35) | direct code | `app.py:14` — elif torch.backends.mps.is_available(): |
| [vibevoice-realtime](https://github.com/pinokiofactory/vibevoice-realtime) | optional flag + env/config flag | `start.js:10` — MODEL_DEVICE: "{{gpu === 'apple' ? 'mps' : (gpu === 'nvidia' ? 'cuda' : 'cpu')}}" |
| [z-image-turbo](https://github.com/pinokiofactory/z-image-turbo) | direct code | `app/app.py:28` — if hasattr(torch.backends, "mps") and torch.backends.mps.is_available():<br>`app/app.py:29` — return "mps" |

Separately, five launchers are MLX-based ([MFLUX-WEBUI](https://github.com/pinokiofactory/MFLUX-WEBUI), [mlx](https://github.com/pinokiofactory/mlx), [mlx-video-transcription](https://github.com/pinokiofactory/mlx-video-transcription), [mlx-video-ui](https://github.com/pinokiofactory/mlx-video-ui), [SongGeneration-Studio-MLX](https://github.com/pinokiofactory/SongGeneration-Studio-MLX)). MLX runs on Apple's Metal backend but does **not** use Metal Performance Shaders APIs; it is an Apple-silicon-only alternative to the CUDA/MPS PyTorch paths above.

## Attention kernels

### FlashAttention

Nineteen repositories contain FlashAttention signals. The dominant pattern is a prebuilt CUDA wheel installed from `cu12x`/`cu128`/`cu130` URLs inside `torch.js`. A few are only optional (`args.flashattention`), build flags, or model names (`no-flash-attn`) rather than real usage; those are labelled below.

| Project | How used | Evidence |
| --- | --- | --- |
| [AudioX](https://github.com/pinokiofactory/AudioX) | optional flag + launcher install | `torch.js:14` — "{{args && args.flashattention ? 'uv pip install https://huggingface.co/lldacing/flash-attention-windows-wheel/resolve/main/flash_attn-2.7.4.post1%2Bcu128torch2.8...<br>`torch.js:30` — "{{args && args.flashattention ? 'uv pip install https://huggingface.co/lldacing/flash-attention-windows-wheel/resolve/main/flash_attn-2.7.4.post1%2Bcu128torch2.7... |
| [aura-sr-upscaler](https://github.com/pinokiofactory/aura-sr-upscaler) | optional flag + launcher install | `torch.js:14` — "{{args && args.flashattention ? 'uv pip install https://huggingface.co/cocktailpeanut/wheels/resolve/main/flash_attn-2.8.2%2Bcu128torch2.7-cp310-cp310-win_amd64....<br>`torch.js:31` — "{{args && args.flashattention ? 'uv pip install https://huggingface.co/cocktailpeanut/wheels/resolve/main/flash_attn-2.8.3%2Bcu128torch2.7-cp310-cp310-linux_x86_... |
| [clarity-refiners-ui](https://github.com/pinokiofactory/clarity-refiners-ui) | reference | `README.md:42` — - https://huggingface.co/multimodalart/Florence-2-large-no-flash-attn<br>`app/app.py:134` — "multimodalart/Florence-2-large-no-flash-attn", |
| [cogvideo](https://github.com/pinokiofactory/cogvideo) | optional flag + launcher install | `torch.js:14` — "{{args && args.flashattention ? 'uv pip install https://huggingface.co/cocktailpeanut/wheels/resolve/main/flash_attn-2.8.2%2Bcu128torch2.7-cp310-cp310-win_amd64....<br>`torch.js:31` — "{{args && args.flashattention ? 'uv pip install https://huggingface.co/cocktailpeanut/wheels/resolve/main/flash_attn-2.8.3%2Bcu128torch2.7-cp310-cp310-linux_x86_... |
| [comfy](https://github.com/pinokiofactory/comfy) | launcher install | `torch.js:14` — "uv pip install https://huggingface.co/cocktailpeanut/wheels/resolve/main/flash_attn-2.8.2%2Bcu128torch2.7-cp310-cp310-win_amd64.whl"<br>`torch.js:60` — "uv pip install https://huggingface.co/MonsterMMORPG/SECourses_Premium_Flash_Attention/resolve/main/sageattention-2.1.1-cp310-cp310-linux_x86_64.whl", |
| [florence2](https://github.com/pinokiofactory/florence2) | env/config flag | `install.js:28` — "FLASH_ATTENTION_SKIP_CUDA_BUILD": "TRUE" |
| [flux-webui](https://github.com/pinokiofactory/flux-webui) | optional flag + launcher install | `torch.js:14` — "{{args && args.flashattention ? 'uv pip install https://huggingface.co/cocktailpeanut/wheels/resolve/main/flash_attn-2.8.2%2Bcu128torch2.7-cp310-cp310-win_amd64....<br>`torch.js:31` — "{{args && args.flashattention ? 'uv pip install https://huggingface.co/cocktailpeanut/wheels/resolve/main/flash_attn-2.8.3%2Bcu128torch2.7-cp310-cp310-linux_x86_... |
| [hertz](https://github.com/pinokiofactory/hertz) | env/config flag | `start.js:9` — //          USE_FLASH_ATTENTION: 1,<br>`server.js:9` — USE_FLASH_ATTENTION: 1, |
| [hunyuanvideo](https://github.com/pinokiofactory/hunyuanvideo) | optional flag + launcher install | `torch.js:14` — "uv pip install https://github.com/kingbri1/flash-attention/releases/download/v2.7.4.post1/flash_attn-2.7.4.post1+cu128torch2.7.0cxx11abiFALSE-cp310-cp310-win_amd...<br>`torch.js:29` — "{{args && args.sageattention ? 'uv pip install https://huggingface.co/MonsterMMORPG/SECourses_Premium_Flash_Attention/resolve/main/sageattention-2.1.1-cp310-cp31... |
| [llamafactory](https://github.com/pinokiofactory/llamafactory) | launcher install | `torch.js:13` — "uv pip install https://github.com/mjun0812/flash-attention-prebuild-wheels/releases/download/v0.4.10/flash_attn-2.7.4+cu128torch2.7-cp311-cp311-win_amd64.whl"<br>`torch.js:73` — "uv pip install https://github.com/mjun0812/flash-attention-prebuild-wheels/releases/download/v0.7.2/flash_attn-2.7.4+cu128torch2.7-cp311-cp311-linux_x86_64.whl" |
| [mochi](https://github.com/pinokiofactory/mochi) | mention/hint | `install.js:19` — //        message: "pip install https://github.com/oobabooga/flash-attention/releases/download/v2.6.3/flash_attn-2.6.3+cu122torch2.4.1cxx11abiFALSE-cp310-cp310-wi...<br>`install.js:28` — //        message: "pip install https://github.com/Dao-AILab/flash-attention/releases/download/v2.6.3/flash_attn-2.6.3+cu123torch2.4cxx11abiFALSE-cp310-cp310-linu... |
| [openaudio](https://github.com/pinokiofactory/openaudio) | optional flag + launcher install | `torch.js:14` — "{{args && args.flashattention ? 'uv pip install https://huggingface.co/cocktailpeanut/wheels/resolve/main/flash_attn-2.8.2%2Bcu128torch2.7-cp310-cp310-win_amd64....<br>`torch.js:31` — "{{args && args.flashattention ? 'uv pip install https://huggingface.co/cocktailpeanut/wheels/resolve/main/flash_attn-2.8.3%2Bcu128torch2.7-cp310-cp310-linux_x86_... |
| [rc-stableaudio](https://github.com/pinokiofactory/rc-stableaudio) | optional flag + launcher install | `torch.js:14` — "{{args && args.flashattention ? 'uv pip install https://huggingface.co/cocktailpeanut/wheels/resolve/main/flash_attn-2.8.2%2Bcu128torch2.7-cp310-cp310-win_amd64....<br>`torch.js:31` — "{{args && args.flashattention ? 'uv pip install https://huggingface.co/cocktailpeanut/wheels/resolve/main/flash_attn-2.8.3%2Bcu128torch2.7-cp310-cp310-linux_x86_... |
| [TRELLIS](https://github.com/pinokiofactory/TRELLIS) | requirements | `requirements-uv.txt:72` — # via flash-attn<br>`requirements-uv.txt:96` — flash-attn @ https://github.com/bdashore3/flash-attention/releases/download/v2.7.1.post1/flash_attn-2.7.1.post1+cu124torch2.5.1cxx11abiFALSE-cp310-cp310-win_amd64... |
| [Ultimate-TTS-Studio](https://github.com/pinokiofactory/Ultimate-TTS-Studio) | launcher install | `torch.js:12` — "uv pip install https://github.com/mjun0812/flash-attention-prebuild-wheels/releases/download/v0.4.10/flash_attn-2.8.2+cu128torch2.7-cp310-cp310-win_amd64.whl",<br>`torch.js:61` — "uv pip install https://github.com/mjun0812/flash-attention-prebuild-wheels/releases/download/v0.4.11/flash_attn-2.8.3+cu128torch2.7-cp310-cp310-linux_x86_64.whl", |
| [wan](https://github.com/pinokiofactory/wan) | launcher install | `torch.js:49` — "uv pip install https://github.com/mjun0812/flash-attention-prebuild-wheels/releases/download/v0.7.13/flash_attn-2.8.3+cu130torch2.10-cp311-cp311-win_amd64.whl",<br>`torch.js:72` — "uv pip install https://github.com/mjun0812/flash-attention-prebuild-wheels/releases/download/v0.7.13/flash_attn-2.8.3+cu130torch2.10-cp311-cp311-win_amd64.whl", |
| [yue](https://github.com/pinokiofactory/yue) | launcher install | `torch.js:14` — "uv pip install https://huggingface.co/lldacing/flash-attention-windows-wheel/resolve/main/flash_attn-2.7.4.post1%2Bcu128torch2.7.0cxx11abiFALSE-cp311-cp311-win_a...<br>`torch.js:30` — "uv pip install https://huggingface.co/lldacing/flash-attention-windows-wheel/resolve/main/flash_attn-2.7.0.post2%2Bcu124torch2.5.1cxx11abiFALSE-cp311-cp311-win_a... |
| [z-image-turbo](https://github.com/pinokiofactory/z-image-turbo) | optional flag + launcher install | `torch.js:14` — "{{args && args.flashattention ? 'uv pip install https://huggingface.co/cocktailpeanut/wheels/resolve/main/flash_attn-2.8.2%2Bcu128torch2.7-cp310-cp310-win_amd64....<br>`torch.js:30` — "{{args && args.flashattention ? 'uv pip install https://huggingface.co/cocktailpeanut/wheels/resolve/main/flash_attn-2.8.3%2Bcu128torch2.7-cp310-cp310-linux_x86_... |
| [zonos](https://github.com/pinokiofactory/zonos) | launcher install | `torch.js:13` — "uv pip install https://huggingface.co/lldacing/flash-attention-windows-wheel/resolve/main/flash_attn-2.7.4.post1%2Bcu128torch2.7.0cxx11abiFALSE-cp310-cp310-win_a...<br>`torch.js:60` — "uv pip install https://github.com/kingbri1/flash-attention/releases/download/v2.7.4.post1/flash_attn-2.7.4.post1+cu128torch2.7.0cxx11abiFALSE-cp310-cp310-linux_x... |

### SageAttention

Seventeen repositories reference SageAttention, almost always as a CUDA wheel (`+cu128torch…`, `+cu130torch…`) in `torch.js`. Some are commented-out hints in `install.js` rather than active installs; those are marked as such.

| Project | How used | Evidence |
| --- | --- | --- |
| [ACE-Step](https://github.com/pinokiofactory/ACE-Step) | mention/hint | `install.js:35` — // sageattention: true   // uncomment this line if your project requires sageattention |
| [AudioX](https://github.com/pinokiofactory/AudioX) | optional flag + launcher install | `torch.js:13` — "{{args && args.sageattention ? 'uv pip install https://github.com/woct0rdho/SageAttention/releases/download/v2.1.1-windows/sageattention-2.1.1+cu128torch2.7.0-cp...<br>`torch.js:29` — "{{args && args.sageattention ? 'uv pip install https://github.com/deepbeepmeep/SageAttention/raw/refs/heads/main/releases/sageattention-2.1.0-cp310-cp310-win_amd... |
| [aura-sr-upscaler](https://github.com/pinokiofactory/aura-sr-upscaler) | optional flag + launcher install | `torch.js:13` — "{{args && args.sageattention ? 'uv pip install https://huggingface.co/cocktailpeanut/wheels/resolve/main/sageattention-2.1.1%2Bcu128torch2.7.1-cp310-cp310-win_am...<br>`torch.js:30` — "{{args && args.sageattention ? 'uv pip install https://huggingface.co/cocktailpeanut/wheels/resolve/main/sageattention-2.1.1%2Bcu128torch2.7.1-cp310-cp310-linux_... |
| [cogvideo](https://github.com/pinokiofactory/cogvideo) | optional flag + launcher install | `torch.js:13` — "{{args && args.sageattention ? 'uv pip install https://huggingface.co/cocktailpeanut/wheels/resolve/main/sageattention-2.1.1%2Bcu128torch2.7.1-cp310-cp310-win_am...<br>`torch.js:30` — "{{args && args.sageattention ? 'uv pip install https://huggingface.co/cocktailpeanut/wheels/resolve/main/sageattention-2.1.1%2Bcu128torch2.7.1-cp310-cp310-linux_... |
| [comfy](https://github.com/pinokiofactory/comfy) | launcher install | `h.js:62` — //          "pip install sageattention",<br>`torch.js:13` — "uv pip install https://github.com/woct0rdho/SageAttention/releases/download/v2.1.1-windows/sageattention-2.1.1+cu128torch2.7.0-cp310-cp310-win_amd64.whl", |
| [dia](https://github.com/pinokiofactory/dia) | optional flag + launcher install | `torch.js:13` — "{{args && args.sageattention ? 'uv pip install https://github.com/woct0rdho/SageAttention/releases/download/v2.1.1-windows/sageattention-2.1.1+cu128torch2.7.0-cp...<br>`torch.js:63` — "{{args && args.sageattention ? 'uv pip install git+https://github.com/thu-ml/SageAttention.git' : ''}}" |
| [flux-webui](https://github.com/pinokiofactory/flux-webui) | optional flag + launcher install | `torch.js:13` — "{{args && args.sageattention ? 'uv pip install https://huggingface.co/cocktailpeanut/wheels/resolve/main/sageattention-2.1.1%2Bcu128torch2.7.1-cp310-cp310-win_am...<br>`torch.js:30` — "{{args && args.sageattention ? 'uv pip install https://huggingface.co/cocktailpeanut/wheels/resolve/main/sageattention-2.1.1%2Bcu128torch2.7.1-cp310-cp310-linux_... |
| [Frame-Pack](https://github.com/pinokiofactory/Frame-Pack) | launcher install | `torch.js:13` — "uv pip install https://github.com/woct0rdho/SageAttention/releases/download/v2.1.1-windows/sageattention-2.1.1+cu128torch2.7.0-cp310-cp310-win_amd64.whl",<br>`torch.js:59` — "uv pip install https://huggingface.co/cocktailpeanut/wheels/resolve/main/sageattention-2.1.1%2Bcu128torch2.7.1-cp310-cp310-linux_x86_64.whl", |
| [hunyuanvideo](https://github.com/pinokiofactory/hunyuanvideo) | optional flag + launcher install | `torch.js:13` — "{{args && args.sageattention ? 'uv pip install https://github.com/woct0rdho/SageAttention/releases/download/v2.1.1-windows/sageattention-2.1.1+cu128torch2.7.0-cp...<br>`torch.js:29` — "{{args && args.sageattention ? 'uv pip install https://huggingface.co/MonsterMMORPG/SECourses_Premium_Flash_Attention/resolve/main/sageattention-2.1.1-cp310-cp31... |
| [Nari-Dia-TTS](https://github.com/pinokiofactory/Nari-Dia-TTS) | optional flag + launcher install | `torch.js:13` — "{{args && args.sageattention ? 'uv pip install https://github.com/woct0rdho/SageAttention/releases/download/v2.1.1-windows/sageattention-2.1.1+cu128torch2.7.0-cp...<br>`torch.js:28` — "{{args && args.sageattention ? 'uv pip install https://github.com/deepbeepmeep/SageAttention/raw/refs/heads/main/releases/sageattention-2.1.0-cp310-cp310-win_amd... |
| [openaudio](https://github.com/pinokiofactory/openaudio) | optional flag + launcher install | `torch.js:13` — "{{args && args.sageattention ? 'uv pip install https://huggingface.co/cocktailpeanut/wheels/resolve/main/sageattention-2.1.1%2Bcu128torch2.7.1-cp310-cp310-win_am...<br>`torch.js:30` — "{{args && args.sageattention ? 'uv pip install https://huggingface.co/cocktailpeanut/wheels/resolve/main/sageattention-2.1.1%2Bcu128torch2.7.1-cp310-cp310-linux_... |
| [rc-stableaudio](https://github.com/pinokiofactory/rc-stableaudio) | optional flag + launcher install | `torch.js:13` — "{{args && args.sageattention ? 'uv pip install https://huggingface.co/cocktailpeanut/wheels/resolve/main/sageattention-2.1.1%2Bcu128torch2.7.1-cp310-cp310-win_am...<br>`torch.js:30` — "{{args && args.sageattention ? 'uv pip install https://huggingface.co/cocktailpeanut/wheels/resolve/main/sageattention-2.1.1%2Bcu128torch2.7.1-cp310-cp310-linux_... |
| [RuinedFooocus](https://github.com/pinokiofactory/RuinedFooocus) | optional flag + launcher install | `torch.js:14` — "{{args && args.sageattention ? 'uv pip install https://github.com/woct0rdho/SageAttention/releases/download/v2.1.1-windows/sageattention-2.1.1+cu128torch2.7.0-cp...<br>`torch.js:29` — "{{args && args.sageattention ? 'uv pip install git+https://github.com/thu-ml/SageAttention.git' : ''}}", |
| [Ultimate-TTS-Studio](https://github.com/pinokiofactory/Ultimate-TTS-Studio) | optional flag + launcher install | `torch.js:14` — "{{args && args.sageattention ? 'uv pip install https://github.com/woct0rdho/SageAttention/releases/download/v2.1.1-windows/sageattention-2.1.1+cu128torch2.7.0-cp...<br>`torch.js:64` — "{{args && args.sageattention ? 'uv pip install git+https://github.com/thu-ml/SageAttention.git' : ''}}" |
| [uno](https://github.com/pinokiofactory/uno) | optional flag + launcher install | `torch.js:13` — "{{args && args.sageattention ? 'uv pip install https://github.com/woct0rdho/SageAttention/releases/download/v2.1.1-windows/sageattention-2.1.1+cu128torch2.7.0-cp...<br>`torch.js:28` — "{{args && args.sageattention ? 'uv pip install https://github.com/deepbeepmeep/SageAttention/raw/refs/heads/main/releases/sageattention-2.1.0-cp310-cp310-win_amd... |
| [wan](https://github.com/pinokiofactory/wan) | launcher install | `torch.js:28` — "uv pip install sageattention==1.0.6",<br>`torch.js:48` — "uv pip install https://github.com/woct0rdho/SageAttention/releases/download/v2.2.0-windows.post4/sageattention-2.2.0+cu130torch2.9.0andhigher.post4-cp39-abi3-win... |
| [z-image-turbo](https://github.com/pinokiofactory/z-image-turbo) | optional flag + launcher install | `torch.js:13` — "{{args && args.sageattention ? 'uv pip install https://huggingface.co/cocktailpeanut/wheels/resolve/main/sageattention-2.1.1%2Bcu128torch2.7.1-cp310-cp310-win_am...<br>`torch.js:29` — "{{args && args.sageattention ? 'uv pip install https://huggingface.co/cocktailpeanut/wheels/resolve/main/sageattention-2.1.1%2Bcu128torch2.7.1-cp310-cp310-linux_... |

### xformers, SDPA and other attention paths

- **xformers:** 75 repositories reference it. In most cases it is an optional `args.xformers` wheel installed only for NVIDIA runs (72 repos carry the optional flag). It has no AMD/Apple wheel, so enabling it blocks a port.
- **PyTorch SDPA:** direct `F.scaled_dot_product_attention` calls were found in **Nari-Dia-TTS** (`dia/layers.py:392`) and **diffusers-image-fill** (`pipeline_fill_sd_xl.py:308`). SDPA is the most portable attention path: it dispatches to FlashAttention on CUDA, AOTriton on ROCm, and MPS/CPU kernels on Apple.
- **FlashInfer / vLLM / PagedAttention:** no references found. Attention for LLM apps in this collection comes from upstream libraries, not the wrappers.

## Porting implications

- CUDA Graph capture (StreamDiffusion) and CUDA-pinned attention wheels (SageAttention, most FlashAttention installs, xformers) are the two hardest obstacles; both need vendor-specific replacements or a fallback to SDPA.
- Triton is widely declared but mostly optional and NVIDIA/Windows-oriented. ROCm Triton can run many kernels, but MPS has no Triton backend at all.
- FlashAttention has partial ROCm support (e.g. via AOTriton) and no MPS wheel; SageAttention is CUDA-only. A port normally swaps both for SDPA or a ROCm attention library and accepts a speed change.
- MPS support exists at the PyTorch device level in 11 wrappers, so the Apple path does not need a new kernel API — but it must avoid CUDA-only attention flags. MLX apps take a separate Apple-only route.
- Vulkan is absent everywhere; it would be a new backend rather than an existing one to preserve.
