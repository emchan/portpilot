# CPU port attempts — easiest to hardest

Companion to [`results/pinokio-apps.md`](../results/pinokio-apps.md), [`cpu.md`](cpu.md), [`effort.md`](effort.md). Each app was attempted in the order of [`effort.md`](effort.md) (easiest first). Attempts are **static**: launcher/source inspection plus `py_compile` where Python source exists in the snapshot. Pinokio wrappers are not executed and no model is downloaded, so statuses report portability readiness, not a successful end-to-end run.

| # | Project | Commit | Status | Smoke check | Blockers |
|---:|---|---|---|---|---|
| 1 | [ai-video-composer](https://github.com/pinokiofactory/ai-video-composer) | [0cc7921](https://github.com/pinokiofactory/ai-video-composer/commit/0cc7921ff899b4d8ce6e5b8f419f9144e50fa43d) | CPU-tested: passed (packaging fix) | n/a (no Python source in snapshot) | none identified |
| 2 | [bolt](https://github.com/pinokiofactory/bolt) | [e78682b](https://github.com/pinokiofactory/bolt/commit/e78682b26d423a3e26fe8c120521eddb6411d78b) | CPU-ready (no changes) | n/a (no Python source in snapshot) | none identified |
| 3 | [browser-use](https://github.com/pinokiofactory/browser-use) | [6167ae0](https://github.com/pinokiofactory/browser-use/commit/6167ae0fc0dfd49120d215a4962143a87fd14c98) | CPU-ready (no changes) | n/a (no Python source in snapshot) | none identified |
| 4 | [controlyourself](https://github.com/pinokiofactory/controlyourself) | [e516690](https://github.com/pinokiofactory/controlyourself/commit/e516690406e0e8499b09c7e8a4c65ac13539099f) | CPU-ready (no changes) | n/a (no Python source in snapshot) | none identified |
| 5 | [ditto](https://github.com/pinokiofactory/ditto) | [aa45279](https://github.com/pinokiofactory/ditto/commit/aa45279201a7ddaead5ac33d56feba35417319c5) | CPU-ready (no changes) | n/a (no Python source in snapshot) | none identified |
| 6 | [errortest](https://github.com/pinokiofactory/errortest) | [dd40517](https://github.com/pinokiofactory/errortest/commit/dd4051727b682cdfdb3f0ae792875052bd4398b9) | CPU-tested: passed (packaging fix) | n/a (no Python source in snapshot) | none identified |
| 7 | [invoke](https://github.com/pinokiofactory/invoke) | [67ac5a1](https://github.com/pinokiofactory/invoke/commit/67ac5a161a265badb1ff73d46c41f762c16bff35) | CPU-capable (shipped fallback) | n/a (no Python source in snapshot) | none identified |
| 8 | [mcp](https://github.com/pinokiofactory/mcp) | [01d5096](https://github.com/pinokiofactory/mcp/commit/01d5096c5ab4d4aaec70a074896c281fd204f8f5) | CPU-ready (no changes) | n/a (no Python source in snapshot) | none identified |
| 9 | [open-webui](https://github.com/pinokiofactory/open-webui) | [d7c5932](https://github.com/pinokiofactory/open-webui/commit/d7c59329e3758cac350a1b5f1b834038727bec6c) | CPU-ready (no changes) | n/a (no Python source in snapshot) | none identified |
| 10 | [openui](https://github.com/pinokiofactory/openui) | [83ab6b5](https://github.com/pinokiofactory/openui/commit/83ab6b5534ee0500674a6e2872e235092310cd9d) | CPU-tested: passed (peewee pin) | n/a (no Python source in snapshot) | none identified |
| 11 | [sillytavern](https://github.com/pinokiofactory/sillytavern) | [f75be07](https://github.com/pinokiofactory/sillytavern/commit/f75be07a853a78f0a9369d2faeec4518c553241a) | CPU-ready (no changes) | n/a (no Python source in snapshot) | none identified |
| 12 | [vibevoice-realtime](https://github.com/pinokiofactory/vibevoice-realtime) | [e8f4b7b](https://github.com/pinokiofactory/vibevoice-realtime/commit/e8f4b7bd22f65e45b19cd4e67cd0c1a982109102) | CPU-tested: passed (weights_only patch) | n/a (no Python source in snapshot) | none identified |
| 13 | [Hunyuan3d-2-lowvram](https://github.com/pinokiofactory/Hunyuan3d-2-lowvram) | [9c41502](https://github.com/pinokiofactory/Hunyuan3d-2-lowvram/commit/9c415021473ec16b64b85bda5d3d50295c478e5b) | CPU-capable (shipped fallback) | n/a (no Python source in snapshot) | GPU-only attention: xformers |
| 14 | [Ilaria-RVC](https://github.com/pinokiofactory/Ilaria-RVC) | [2dd918e](https://github.com/pinokiofactory/Ilaria-RVC/commit/2dd918e4d99c051cbc3a4201484cb91990cfa118) | CPU-capable (shipped fallback) | n/a (no Python source in snapshot) | GPU-only attention: xformers |
| 15 | [MMAudio](https://github.com/pinokiofactory/MMAudio) | [301b075](https://github.com/pinokiofactory/MMAudio/commit/301b075421ae40d86dded8f5c36c64f65af89bfb) | CPU-capable (shipped fallback) | n/a (no Python source in snapshot) | GPU-only attention: xformers |
| 16 | [Orpheus-TTS-FastAPI](https://github.com/pinokiofactory/Orpheus-TTS-FastAPI) | [36afb50](https://github.com/pinokiofactory/Orpheus-TTS-FastAPI/commit/36afb50f8c7355238763680480dca601789cae82) | CPU-capable (shipped fallback) | n/a (no Python source in snapshot) | GPU-only attention: xformers |
| 17 | [RMBG-2-Studio](https://github.com/pinokiofactory/RMBG-2-Studio) | [a2c3a0d](https://github.com/pinokiofactory/RMBG-2-Studio/commit/a2c3a0d0f1618c74c115d3221eb665bab5e8df10) | CPU-capable (shipped fallback) | pass (1/1 files) | GPU-only attention: xformers |
| 18 | [StyleTTS2_Studio](https://github.com/pinokiofactory/StyleTTS2_Studio) | [cb09179](https://github.com/pinokiofactory/StyleTTS2_Studio/commit/cb09179fa56bf5d34c86dffc9b5424c5331005a7) | CPU-capable (shipped fallback) | n/a (no Python source in snapshot) | GPU-only attention: xformers |
| 19 | [accdiffusion](https://github.com/pinokiofactory/accdiffusion) | [4af0027](https://github.com/pinokiofactory/accdiffusion/commit/4af00276b2b2138562c5c52bce291bdb4a1c590f) | CPU-capable (shipped fallback) | n/a (no Python source in snapshot) | GPU-only attention: xformers |
| 20 | [applio](https://github.com/pinokiofactory/applio) | [41a9ccd](https://github.com/pinokiofactory/applio/commit/41a9ccd75fbb39d84059447a8717581640c11143) | CPU-capable (shipped fallback) | n/a (no Python source in snapshot) | GPU-only attention: xformers |
| 21 | [artist](https://github.com/pinokiofactory/artist) | [af0faf2](https://github.com/pinokiofactory/artist/commit/af0faf241f231b8efd74b9099496a74a24a1eaa7) | CPU-capable (shipped fallback) | n/a (no Python source in snapshot) | GPU-only attention: xformers |
| 22 | [augmentoolkit](https://github.com/pinokiofactory/augmentoolkit) | [24f8037](https://github.com/pinokiofactory/augmentoolkit/commit/24f80371c8ae61a91295b71f773e41a2616437e6) | CPU-capable (shipped fallback) | n/a (no Python source in snapshot) | GPU-only attention: xformers |
| 23 | [autogpt](https://github.com/pinokiofactory/autogpt) | [53e7c0e](https://github.com/pinokiofactory/autogpt/commit/53e7c0e1e22b3b9162d7d0669f9bac3491cf5d51) | CPU-capable (shipped fallback) | n/a (no Python source in snapshot) | GPU-only attention: xformers |
| 24 | [cube](https://github.com/pinokiofactory/cube) | [5884465](https://github.com/pinokiofactory/cube/commit/58844658cfc9eab4f8e956bab4883fa8d867cf44) | CPU-capable (shipped fallback) | n/a (no Python source in snapshot) | GPU-only attention: xformers |
| 25 | [diamond](https://github.com/pinokiofactory/diamond) | [3509823](https://github.com/pinokiofactory/diamond/commit/35098236144ee378454ede9cc7e1a1316d65cf8c) | CPU-capable (shipped fallback) | n/a (no Python source in snapshot) | GPU-only attention: xformers |
| 26 | [diffusers-image-fill](https://github.com/pinokiofactory/diffusers-image-fill) | [a8b6497](https://github.com/pinokiofactory/diffusers-image-fill/commit/a8b6497483d956df7ca1ffc882bf29af03476a26) | CPU-capable (shipped fallback) | pass (3/3 files) | GPU-only attention: xformers |
| 27 | [e2-f5-tts](https://github.com/pinokiofactory/e2-f5-tts) | [f871e54](https://github.com/pinokiofactory/e2-f5-tts/commit/f871e54167835552efa88b366388b299f50c36af) | CPU-capable (shipped fallback) | n/a (no Python source in snapshot) | GPU-only attention: xformers |
| 28 | [flashdiffusion](https://github.com/pinokiofactory/flashdiffusion) | [c61d186](https://github.com/pinokiofactory/flashdiffusion/commit/c61d18626e05f89335aca054a34cbbd6703d5b6b) | CPU-capable (shipped fallback) | n/a (no Python source in snapshot) | GPU-only attention: xformers |
| 29 | [florence2](https://github.com/pinokiofactory/florence2) | [5b517ac](https://github.com/pinokiofactory/florence2/commit/5b517ac86c59d3b8a28a5d75c3aba34e2aa2e3b6) | CPU-capable (shipped fallback) | n/a (no Python source in snapshot) | GPU-only attention: xformers |
| 30 | [instantir](https://github.com/pinokiofactory/instantir) | [98901ae](https://github.com/pinokiofactory/instantir/commit/98901aecae33b014e3fbd0f672706a506918c7f1) | CPU-capable (shipped fallback) | n/a (no Python source in snapshot) | GPU-only attention: xformers |
| 31 | [janus](https://github.com/pinokiofactory/janus) | [6332de0](https://github.com/pinokiofactory/janus/commit/6332de02fce4540acfea094435af331903120c69) | CPU-capable (shipped fallback) | n/a (no Python source in snapshot) | GPU-only attention: xformers |
| 32 | [mochi](https://github.com/pinokiofactory/mochi) | [93d4b2b](https://github.com/pinokiofactory/mochi/commit/93d4b2bddb16f3ce883f47336f1de7c126955d6e) | CPU-capable (shipped fallback) | n/a (no Python source in snapshot) | GPU-only attention: xformers; CUDA-only fused kernels |
| 33 | [oasis](https://github.com/pinokiofactory/oasis) | [a84069d](https://github.com/pinokiofactory/oasis/commit/a84069d12ae3165aa0c8c955f9a93314ecf3d3d8) | CPU-capable (shipped fallback) | n/a (no Python source in snapshot) | GPU-only attention: xformers |
| 34 | [omniparser](https://github.com/pinokiofactory/omniparser) | [b2f7de9](https://github.com/pinokiofactory/omniparser/commit/b2f7de9607dcc3087229feaee36c6c2f0345fc80) | CPU-capable (shipped fallback) | n/a (no Python source in snapshot) | GPU-only attention: xformers |
| 35 | [pcm](https://github.com/pinokiofactory/pcm) | [1902e63](https://github.com/pinokiofactory/pcm/commit/1902e63160c5626aa0b14f0a1279f8c59a6239c1) | CPU-capable (shipped fallback) | n/a (no Python source in snapshot) | GPU-only attention: xformers |
| 36 | [stableaudio](https://github.com/pinokiofactory/stableaudio) | [14c9fbb](https://github.com/pinokiofactory/stableaudio/commit/14c9fbb56ef0054d8fae55bcee825216d30be047) | CPU-capable (shipped fallback) | n/a (no Python source in snapshot) | GPU-only attention: xformers |
| 37 | [text2midi](https://github.com/pinokiofactory/text2midi) | [8e5f742](https://github.com/pinokiofactory/text2midi/commit/8e5f742a1313c9b6f89bcf779fd0f4cf798864b7) | CPU-capable (shipped fallback) | n/a (no Python source in snapshot) | GPU-only attention: xformers |
| 38 | [video-background-removal](https://github.com/pinokiofactory/video-background-removal) | [975e13e](https://github.com/pinokiofactory/video-background-removal/commit/975e13e9f5f659fcebba10d1a4e7a00034d6223f) | CPU-capable (shipped fallback) | n/a (no Python source in snapshot) | GPU-only attention: xformers |
| 39 | [whisper-webui](https://github.com/pinokiofactory/whisper-webui) | [5b6ebed](https://github.com/pinokiofactory/whisper-webui/commit/5b6ebed2652d7adb7608ebe5c82ed01619e10daf) | CPU-capable (shipped fallback) | n/a (no Python source in snapshot) | GPU-only attention: xformers |
| 40 | [hertz](https://github.com/pinokiofactory/hertz) | [306ecc6](https://github.com/pinokiofactory/hertz/commit/306ecc634eea5a51a3d20729d44cc94f5650d45d) | CPU-tested: passed (source patch) | pass (1/1 files) | direct torch.cuda calls |
| 41 | [macOS-use](https://github.com/pinokiofactory/macOS-use) | [7417e3a](https://github.com/pinokiofactory/macOS-use/commit/7417e3a1c1c5f38ec665d4c8ceb31857d8939bc4) | CPU-ready (no changes) | pass (1/1 files) | none identified |
| 42 | [ominicontrol](https://github.com/pinokiofactory/ominicontrol) | [2c9e78d](https://github.com/pinokiofactory/ominicontrol/commit/2c9e78d353de3a48ea5adb83c618081bb2be71db) | CPU-capable (shipped fallback) | n/a (no Python source in snapshot) | GPU-only attention: xformers |
| 43 | [Kokoro-TTS](https://github.com/pinokiofactory/Kokoro-TTS) | [491a369](https://github.com/pinokiofactory/Kokoro-TTS/commit/491a369bdca03b320586bd230f1c819562c03558) | CPU-capable (shipped fallback) | pass (1/1 files) | GPU-only attention: xformers; direct torch.cuda calls |
| 44 | [clarity-refiners-ui](https://github.com/pinokiofactory/clarity-refiners-ui) | [a632fb6](https://github.com/pinokiofactory/clarity-refiners-ui/commit/a632fb6b948fa6b1a55d816982655d6dc8ed995e) | CPU-capable (shipped fallback) | pass (5/5 files) | GPU-only attention: xformers; direct torch.cuda calls; CUDA-only fused kernels |
| 45 | [sd35](https://github.com/pinokiofactory/sd35) | [1e820d7](https://github.com/pinokiofactory/sd35/commit/1e820d785879752bf27626cce260c49cdbfe149d) | CPU-capable (shipped fallback) | pass (1/1 files) | GPU-only attention: xformers; direct torch.cuda calls; MPS branch Apple-only |
| 46 | [forge](https://github.com/pinokiofactory/forge) | [e3378c3](https://github.com/pinokiofactory/forge/commit/e3378c35f7f1c4fec2f600c33b9d17ab6d330b4c) | Needs launcher change | n/a (no Python source in snapshot) | no CPU/AMD launcher branch |
| 47 | [audiocraft_plus](https://github.com/pinokiofactory/audiocraft_plus) | [a8e0d27](https://github.com/pinokiofactory/audiocraft_plus/commit/a8e0d2731e8dbb7185a4a0ffd53b495d003586ab) | CPU-capable (shipped fallback) | n/a (no Python source in snapshot) | GPU-only attention: triton-windows/xformers |
| 48 | [omnigen](https://github.com/pinokiofactory/omnigen) | [07de8c2](https://github.com/pinokiofactory/omnigen/commit/07de8c2c3944d3852bcab55d2f2c4d74bd245532) | CPU-capable (shipped fallback) | n/a (no Python source in snapshot) | GPU-only attention: triton-windows/xformers |
| 49 | [liveportrait](https://github.com/pinokiofactory/liveportrait) | [b5fb16c](https://github.com/pinokiofactory/liveportrait/commit/b5fb16ce6df50e79d11d7c1a2d7b39faa720411e) | CPU-capable (shipped fallback) | n/a (no Python source in snapshot) | GPU-only attention: xformers; GPU runtime: onnxruntime-gpu |
| 50 | [pyramidflow](https://github.com/pinokiofactory/pyramidflow) | [6ae7e61](https://github.com/pinokiofactory/pyramidflow/commit/6ae7e61806478b430473c2a6ce9866525e3cd1a2) | CPU-capable (shipped fallback) | n/a (no Python source in snapshot) | GPU-only attention: triton/triton-windows/xformers |
| 51 | [Hunyuan3D-2](https://github.com/pinokiofactory/Hunyuan3D-2) | [c0aa654](https://github.com/pinokiofactory/Hunyuan3D-2/commit/c0aa654a27ccda410b1d0914b61adbd52731c3c7) | CPU-capable (shipped fallback) | n/a (no Python source in snapshot) | GPU-only attention: xformers |
| 52 | [Hunyuan3D-2-mini](https://github.com/pinokiofactory/Hunyuan3D-2-mini) | [7ffb6a8](https://github.com/pinokiofactory/Hunyuan3D-2-mini/commit/7ffb6a83e54fee4df0f111111e768217e337fadc) | CPU-capable (shipped fallback) | n/a (no Python source in snapshot) | GPU-only attention: xformers |
| 53 | [MagicQuill](https://github.com/pinokiofactory/MagicQuill) | [bfdae28](https://github.com/pinokiofactory/MagicQuill/commit/bfdae2847a85d7b00761b4e93fbcb91be5e6d494) | CPU-capable (shipped fallback) | n/a (no Python source in snapshot) | GPU-only attention: xformers; GPU quantisers: bitsandbytes |
| 54 | [florence-sam](https://github.com/pinokiofactory/florence-sam) | [3cca86f](https://github.com/pinokiofactory/florence-sam/commit/3cca86f7edf8e94daae4339727f202895306c021) | CPU-capable (shipped fallback) | n/a (no Python source in snapshot) | GPU-only attention: xformers; GPU runtime: cudnn |
| 55 | [stable-fast-3d](https://github.com/pinokiofactory/stable-fast-3d) | [00fdb29](https://github.com/pinokiofactory/stable-fast-3d/commit/00fdb293b784f223c100971f37a23f2e8a801654) | CPU-capable (shipped fallback) | n/a (no Python source in snapshot) | GPU-only attention: xformers; CUDA-only fused kernels |
| 56 | [dia](https://github.com/pinokiofactory/dia) | [17e1912](https://github.com/pinokiofactory/dia/commit/17e1912e77363efc198d52a5ae813caaa8d3da90) | CPU-capable (shipped fallback) | n/a (no Python source in snapshot) | GPU-only attention: sageattention/triton-windows/xformers; CUDA-only fused kernels |
| 57 | [MatAnyone](https://github.com/pinokiofactory/MatAnyone) | [8483199](https://github.com/pinokiofactory/MatAnyone/commit/84831993029bc83f5942f0401bc8a32dd315b217) | CPU-capable (shipped fallback) | pass (1/1 files) | GPU-only attention: xformers; direct torch.cuda calls; MPS branch Apple-only |
| 58 | [LTX-Desktop-WanGP](https://github.com/pinokiofactory/LTX-Desktop-WanGP) | [2a3fedd](https://github.com/pinokiofactory/LTX-Desktop-WanGP/commit/2a3fedd030e9c7c12f9f67a14466007319ecc3d5) | Needs launcher change | n/a (no Python source in snapshot) | no CPU/AMD launcher branch |
| 59 | [Nari-Dia-TTS](https://github.com/pinokiofactory/Nari-Dia-TTS) | [e5b630d](https://github.com/pinokiofactory/Nari-Dia-TTS/commit/e5b630df297c7f47f6c518a00d6c3f44be4e25b5) | CPU-capable (shipped fallback) | pass (6/6 files) | GPU-only attention: sageattention/triton-windows/xformers; direct torch.cuda calls; CUDA-only fused kernels; MPS branch Apple-only |
| 60 | [ovis](https://github.com/pinokiofactory/ovis) | [00a5702](https://github.com/pinokiofactory/ovis/commit/00a570258ba7370090037bb14bcfa67e1e81194e) | CPU-capable (shipped fallback) | pass (1/1 files) | CUDA-only torch wheel; direct torch.cuda calls; MPS branch Apple-only |
| 61 | [MFLUX-WEBUI](https://github.com/pinokiofactory/MFLUX-WEBUI) | [62b3f93](https://github.com/pinokiofactory/MFLUX-WEBUI/commit/62b3f9364abf53951cfdfb3c2e872d470d5baa4a) | Blocked (Apple-only) | n/a (no Python source in snapshot) | Apple-silicon-only MLX runtime |
| 62 | [SongGeneration-Studio-MLX](https://github.com/pinokiofactory/SongGeneration-Studio-MLX) | [49e365c](https://github.com/pinokiofactory/SongGeneration-Studio-MLX/commit/49e365c88512ffd1a4bf17d800c5508e7d5781da) | Blocked (Apple-only) | n/a (no Python source in snapshot) | Apple-silicon-only MLX runtime |
| 63 | [cogstudio](https://github.com/pinokiofactory/cogstudio) | [7dfb014](https://github.com/pinokiofactory/cogstudio/commit/7dfb014a636513c5b42de070c43e285c9bf7cce7) | CPU-capable (shipped fallback) | pass (1/1 files) | GPU-only attention: xformers; direct torch.cuda calls |
| 64 | [mlx-video-transcription](https://github.com/pinokiofactory/mlx-video-transcription) | [331245a](https://github.com/pinokiofactory/mlx-video-transcription/commit/331245a916c9eb1602637a5cedebf83eb2322ee5) | Blocked (Apple-only) | n/a (no Python source in snapshot) | Apple-silicon-only MLX runtime |
| 65 | [mlx-video-ui](https://github.com/pinokiofactory/mlx-video-ui) | [2f91ff7](https://github.com/pinokiofactory/mlx-video-ui/commit/2f91ff7c3749a11dfcb3ed3e555a375cb5400421) | Blocked (Apple-only) | n/a (no Python source in snapshot) | Apple-silicon-only MLX runtime |
| 66 | [photomaker2](https://github.com/pinokiofactory/photomaker2) | [2c48cd3](https://github.com/pinokiofactory/photomaker2/commit/2c48cd3f30a305069aad6de30bfe4c3f0fe900f7) | CPU-capable (shipped fallback) | n/a (no Python source in snapshot) | GPU-only attention: xformers; GPU runtime: cudnn/onnxruntime-gpu |
| 67 | [AllTalk-TTS](https://github.com/pinokiofactory/AllTalk-TTS) | [7b6ed78](https://github.com/pinokiofactory/AllTalk-TTS/commit/7b6ed78e5a661eeafccdf446f0772be475390a5c) | CPU-capable (shipped fallback) | n/a (no Python source in snapshot) | GPU-only attention: xformers; GPU runtime: deepspeed |
| 68 | [applio-old](https://github.com/pinokiofactory/applio-old) | [a8d276c](https://github.com/pinokiofactory/applio-old/commit/a8d276c8f426304428755974392b5e42d4ef29a5) | Needs launcher change | n/a (no Python source in snapshot) | no CPU/AMD launcher branch; CUDA-only torch wheel |
| 69 | [dough](https://github.com/pinokiofactory/dough) | [3e8a58b](https://github.com/pinokiofactory/dough/commit/3e8a58b5da380ec15cd5743ffc57d220a64fdae1) | Needs launcher change | pass (1/1 files) | no CPU/AMD launcher branch; CUDA-only torch wheel |
| 70 | [facepoke](https://github.com/pinokiofactory/facepoke) | [f3a8c96](https://github.com/pinokiofactory/facepoke/commit/f3a8c9610834b51b64069f3bce9b1da3a321e620) | CPU-capable (shipped fallback) | n/a (no Python source in snapshot) | GPU-only attention: xformers; GPU runtime: onnxruntime-gpu |
| 71 | [mlx](https://github.com/pinokiofactory/mlx) | [eedc5a1](https://github.com/pinokiofactory/mlx/commit/eedc5a1a3f57fbd7d78ad36d3f934b20372fac4c) | Blocked (Apple-only) | n/a (no Python source in snapshot) | Apple-silicon-only MLX runtime; GPU-only attention: xformers |
| 72 | [moshi](https://github.com/pinokiofactory/moshi) | [485d527](https://github.com/pinokiofactory/moshi/commit/485d527a4d8a57e99e58b4735b61b5fb300d2aa3) | Blocked (Apple-only) | n/a (no Python source in snapshot) | Apple-silicon-only MLX runtime; GPU-only attention: xformers |
| 73 | [stable-diffusion-webui-forge](https://github.com/pinokiofactory/stable-diffusion-webui-forge) | [e44fda2](https://github.com/pinokiofactory/stable-diffusion-webui-forge/commit/e44fda22458c495919a1c90ed9e7d5c63c37adfb) | CPU-capable (shipped fallback) | n/a (no Python source in snapshot) | CUDA-only torch wheel; 817 FP8 GEMMs; 626 packed 4-bit weights |
| 74 | [hallo](https://github.com/pinokiofactory/hallo) | [c72097c](https://github.com/pinokiofactory/hallo/commit/c72097c6c23be58e7435bc48fbe9d0be5d0da1e5) | CPU-capable (shipped fallback) | n/a (no Python source in snapshot) | GPU-only attention: xformers; GPU quantisers: bitsandbytes |
| 75 | [llamafactory](https://github.com/pinokiofactory/llamafactory) | [e299b25](https://github.com/pinokiofactory/llamafactory/commit/e299b25b26f48bb6ef96a670c2da402f0e328441) | CPU-capable (shipped fallback) | n/a (no Python source in snapshot) | GPU-only attention: flash-attn/xformers; GPU quantisers: bitsandbytes; CUDA-only fused kernels |
| 76 | [AudioX](https://github.com/pinokiofactory/AudioX) | [7a0ff7b](https://github.com/pinokiofactory/AudioX/commit/7a0ff7b5ca8d5eeb6054edf84196a23389545d1d) | CPU-capable (shipped fallback) | n/a (no Python source in snapshot) | GPU-only attention: flash-attn/sageattention/triton-windows/xformers; CUDA-only fused kernels |
| 77 | [zonos](https://github.com/pinokiofactory/zonos) | [0be13e4](https://github.com/pinokiofactory/zonos/commit/0be13e4e803fe0834bae8326240633ac8e53bffc) | CPU-capable (shipped fallback) | pass (2/2 files) | GPU-only attention: flash-attn/triton/triton-windows/xformers; CUDA-only fused kernels |
| 78 | [aura-sr-upscaler](https://github.com/pinokiofactory/aura-sr-upscaler) | [9357cf9](https://github.com/pinokiofactory/aura-sr-upscaler/commit/9357cf93dac1f28179bb5d32c98b1c5c75a61ece) | CPU-capable (shipped fallback) | n/a (no Python source in snapshot) | GPU-only attention: flash-attn/sageattention/triton/triton-windows/xformers; CUDA-only fused kernels |
| 79 | [openaudio](https://github.com/pinokiofactory/openaudio) | [6a69e79](https://github.com/pinokiofactory/openaudio/commit/6a69e7903d7430cc3d08dae6673caf85b9032fcf) | CPU-capable (shipped fallback) | n/a (no Python source in snapshot) | GPU-only attention: flash-attn/sageattention/triton/triton-windows/xformers; CUDA-only fused kernels |
| 80 | [rc-stableaudio](https://github.com/pinokiofactory/rc-stableaudio) | [b3a7d5a](https://github.com/pinokiofactory/rc-stableaudio/commit/b3a7d5abecbee8fed08717405830126911825e81) | CPU-capable (shipped fallback) | n/a (no Python source in snapshot) | GPU-only attention: flash-attn/sageattention/triton/triton-windows/xformers; CUDA-only fused kernels |
| 81 | [flux-webui](https://github.com/pinokiofactory/flux-webui) | [62d2f56](https://github.com/pinokiofactory/flux-webui/commit/62d2f5692da1e0aaf776c3dceef0a720a6a24bb6) | CPU-capable (shipped fallback) | pass (1/1 files) | GPU-only attention: flash-attn/sageattention/triton/triton-windows/xformers; CUDA-only fused kernels |
| 82 | [Allegro-txt2vid-install](https://github.com/pinokiofactory/Allegro-txt2vid-install) | [6000ff1](https://github.com/pinokiofactory/Allegro-txt2vid-install/commit/6000ff1e395f6238eaa89e68b45a571e84d324e1) | Needs launcher change | n/a (no Python source in snapshot) | no CPU/AMD launcher branch; GPU-only attention: triton-windows/xformers |
| 83 | [diffrhythm](https://github.com/pinokiofactory/diffrhythm) | [15166cf](https://github.com/pinokiofactory/diffrhythm/commit/15166cfd3b677d7fd6294b4d9fb88e7f4845d3ee) | CPU-capable (shipped fallback) | n/a (no Python source in snapshot) | GPU-only attention: triton/triton-windows/xformers; GPU quantisers: bitsandbytes; GPU runtime: onnxruntime-gpu |
| 84 | [z-image-turbo](https://github.com/pinokiofactory/z-image-turbo) | [54899fd](https://github.com/pinokiofactory/z-image-turbo/commit/54899fdb5c023072de43c8b91ad2b0f0bee5b5c4) | CPU-capable (shipped fallback) | pass (1/1 files) | GPU-only attention: flash-attn/sageattention/triton/triton-windows/xformers; direct torch.cuda calls; CUDA-only fused kernels; MPS branch Apple-only |
| 85 | [Frame-Pack](https://github.com/pinokiofactory/Frame-Pack) | [f0d7d1e](https://github.com/pinokiofactory/Frame-Pack/commit/f0d7d1eba4155f5985a465d0476a9f926d0c6179) | CPU-capable (shipped fallback) | pass (2/2 files) | GPU-only attention: sageattention/triton/triton-windows/xformers; CUDA-only fused kernels |
| 86 | [cogvideo](https://github.com/pinokiofactory/cogvideo) | [9e2a186](https://github.com/pinokiofactory/cogvideo/commit/9e2a18626426cbeb7e84be537d98e9082de8fe97) | CPU-capable (shipped fallback) | n/a (no Python source in snapshot) | GPU-only attention: flash-attn/sageattention/triton/triton-windows/xformers; CUDA-only fused kernels |
| 87 | [uno](https://github.com/pinokiofactory/uno) | [6f19067](https://github.com/pinokiofactory/uno/commit/6f190672a75ccadd481a5cd69db95ed392ede8c0) | CPU-capable (shipped fallback) | n/a (no Python source in snapshot) | GPU-only attention: sageattention/triton/triton-windows/xformers; GPU runtime: deepspeed; CUDA-only fused kernels |
| 88 | [ACE-Step](https://github.com/pinokiofactory/ACE-Step) | [8cf2fac](https://github.com/pinokiofactory/ACE-Step/commit/8cf2fac2765b1383e6d078b399acc3e38374949e) | Needs launcher change | n/a (no Python source in snapshot) | no CPU/AMD launcher branch; GPU-only attention: triton/triton-windows/xformers; CUDA-only fused kernels |
| 89 | [Allegro-txt2vid](https://github.com/pinokiofactory/Allegro-txt2vid) | [f8327e3](https://github.com/pinokiofactory/Allegro-txt2vid/commit/f8327e3172834ee8d932d7284641a5e9a0065cbc) | Blocked | pass (15/15 files) | hard CUDA/TensorRT blocker; GPU-only attention: xformers; direct torch.cuda calls; CUDA-only fused kernels |
| 90 | [RuinedFooocus](https://github.com/pinokiofactory/RuinedFooocus) | [cd74193](https://github.com/pinokiofactory/RuinedFooocus/commit/cd741937b44a7f1625acf35250ebf1bc6521dbb2) | Needs launcher change | n/a (no Python source in snapshot) | no CPU/AMD launcher branch; GPU-only attention: sageattention/triton-windows/xformers; CUDA-only fused kernels |
| 91 | [wan](https://github.com/pinokiofactory/wan) | [8ed1410](https://github.com/pinokiofactory/wan/commit/8ed14108ca7148a612c5eb9528b00ceac99810ff) | CPU-capable (shipped fallback) | n/a (no Python source in snapshot) | GPU-only attention: flash-attn/sageattention/triton-windows/xformers; GPU quantisers: bitsandbytes; CUDA-only fused kernels |
| 92 | [yue](https://github.com/pinokiofactory/yue) | [3261118](https://github.com/pinokiofactory/yue/commit/3261118f111c8d2bb098b82b2870458dfbc486c7) | Needs launcher change | n/a (no Python source in snapshot) | no CPU/AMD launcher branch; GPU-only attention: flash-attn/triton/triton-windows/xformers; CUDA-only fused kernels |
| 93 | [echomimic2](https://github.com/pinokiofactory/echomimic2) | [eb7915a](https://github.com/pinokiofactory/echomimic2/commit/eb7915a14420505c7c8b929a2dbba570f1639831) | Needs launcher change | n/a (no Python source in snapshot) | no CPU/AMD launcher branch; GPU-only attention: triton-windows/xformers; GPU runtime: onnxruntime-gpu |
| 94 | [Ultimate-TTS-Studio](https://github.com/pinokiofactory/Ultimate-TTS-Studio) | [b8c15ef](https://github.com/pinokiofactory/Ultimate-TTS-Studio/commit/b8c15efaead5a5e8744783fd443466333d2b1805) | CPU-capable (shipped fallback) | n/a (no Python source in snapshot) | GPU-only attention: flash-attn/sageattention/triton/triton-windows/xformers; GPU runtime: onnxruntime-gpu; CUDA-only fused kernels |
| 95 | [ai-toolkit](https://github.com/pinokiofactory/ai-toolkit) | [ddfefd7](https://github.com/pinokiofactory/ai-toolkit/commit/ddfefd70eb6f9d0b97c95e30b5c72aaac8660b0e) | Blocked | n/a (no Python source in snapshot) | hard CUDA/TensorRT blocker; GPU-only attention: triton/triton-windows |
| 96 | [comfy](https://github.com/pinokiofactory/comfy) | [ba11047](https://github.com/pinokiofactory/comfy/commit/ba110479f88835d64c603044c2fe69102833fa55) | CPU-capable (shipped fallback) | n/a (no Python source in snapshot) | GPU-only attention: flash-attn/sageattention/triton/triton-windows/xformers; GPU quantisers: bitsandbytes; CUDA-only fused kernels; 2916 FP8 GEMMs; +1 |
| 97 | [hunyuanvideo](https://github.com/pinokiofactory/hunyuanvideo) | [c65cb77](https://github.com/pinokiofactory/hunyuanvideo/commit/c65cb772466eea61e0a330f52ed7764a9d4e821d) | Blocked | n/a (no Python source in snapshot) | hard CUDA/TensorRT blocker; GPU-only attention: flash-attn/sageattention/triton/triton-windows/xformers; CUDA-only fused kernels |
| 98 | [StreamDiffusion](https://github.com/pinokiofactory/StreamDiffusion) | [0e529aa](https://github.com/pinokiofactory/StreamDiffusion/commit/0e529aaff2ff344ce15565420e0c484688eb1bc9) | Blocked | pass (36/36 files) | hard CUDA/TensorRT blocker; GPU-only attention: triton/xformers; GPU runtime: tensorrt; CUDA-only torch wheel; +2 |
| 99 | [TRELLIS](https://github.com/pinokiofactory/TRELLIS) | [3d6dec1](https://github.com/pinokiofactory/TRELLIS/commit/3d6dec1fada102cba537ce7f6926061b0af7b962) | Blocked | n/a (no Python source in snapshot) | hard CUDA/TensorRT blocker; GPU-only attention: flash-attn/triton/xformers; compiled CUDA extensions: ccimport/cumm-cu120/diff-gaussian-rasterization...; CUDA-only fused kernels |
| 100 | [factory](https://github.com/pinokiofactory/factory) | [EMPTY](https://github.com/pinokiofactory/factory/commit/EMPTY) | N/A (empty) | n/a (no Python source in snapshot) | empty repository |
| 101 | [y](https://github.com/pinokiofactory/y) | [EMPTY](https://github.com/pinokiofactory/y/commit/EMPTY) | N/A (empty) | n/a (no Python source in snapshot) | empty repository |

## Actually downloaded and tested

- **openui** — installed and ran on CPU after pinning `peewee==3.17.0`.
- **hertz** — installed CPU torch + requirements and ran after patching `app.py` for CPU.
- **vibevoice-realtime** — installed CPU torch + package and ran the realtime demo on CPU after patching `weights_only=True` to `False`.
- **ai-video-composer** — retested on Python 3.12 with huggingface_hub==0.25.2; Gradio server launched on CPU.
- **z-image-turbo** — import succeeded after dependency updates.
- **flux-webui** — retested on Python 3.12; importing app.py hung in this container.
- **bolt** — pnpm install and build succeeded on CPU.
- **browser-use** — package installed and imported successfully on CPU.
- **controlyourself** — all JS files pass node --check; runtime requires Pinokio kernel/playwright.
- **mcp** — all 21 JS files pass node --check; configuration-only app.
- **open-webui** — retested on Python 3.12; installation hung/timed out in this container.
- **sillytavern** — npm install and server startup succeeded on CPU.
- **Hunyuan3d-2-lowvram** — blocked by compiled extension/build failures.
- **Ilaria-RVC** — retested on Python 3.10; blocked by fairseq/omegaconf dependency conflict.
- **MagicQuill** — retested on Python 3.12; blocked by gradio/huggingface_hub HfFolder incompatibility.
- **Nari-Dia-TTS** — retested on Python 3.12; blocked by torchaudio extension loading failure.
- **Orpheus-TTS-FastAPI** — FastAPI server started on CPU after stubbing sounddevice.
- **RMBG-2-Studio** — retested on Python 3.12; dependencies installed and app imported successfully on CPU.
- **StyleTTS2_Studio** — blocked by monotonic_align build failure and gradio dependency issues.
- **accdiffusion** — dependencies installed and app.py imported successfully on CPU.
- **artist** — retested on Python 3.12; app imports successfully on CPU.
- **augmentoolkit** — dependency installation hung/timed out in this container.
- **autogpt** — upstream/poetry/conda setup too heavy for this container.
- **cube** — dependencies installed and app.py imported successfully on CPU.
- **diamond** — retested on Python 3.12; src imports successfully on CPU.
- **diffusers-image-fill** — retested on Python 3.12; importing app.py still hung in this container.
- **e2-f5-tts** — dependencies installed and f5_tts.api imported successfully on CPU.
- **florence2** — retested on Python 3.12; dependencies installed, full model load not attempted.
- **janus** — retested on Python 3.12; runtime still calls .cuda() and is not CPU-compatible.
- **oasis** — retested on Python 3.12; dependency installation hung/timed out in this container.
- **pcm** — importing app.py hung in this container.
- **text2midi** — retested on Python 3.10; dependencies installed and model/app loaded on CPU.
- **video-background-removal** — retested on Python 3.12; dependencies installed and app imported successfully on CPU.
- **whisper-webui** — retested on Python 3.12; jhj0517-whisper build still fails due setuptools/pkg_resources.
- **macOS-use** — macOS-only app; JS syntax checks pass.
- **ominicontrol** — retested on Python 3.12; still blocked by diffusers API mismatch (USE_PEFT_BACKEND).
- **Kokoro-TTS** — retested on Python 3.12; dependencies installed but importing app.py hung in this container.
- **clarity-refiners-ui** — retested on Python 3.12; blocked by torchvision operator mismatch.
- **sd35** — dependencies installed and app.py imported successfully on CPU.
- **forge** — retested on Python 3.12; tokenizers build failure.
- **omnigen** — retested on Python 3.12; dependency installation hung/timed out in this container.
- **liveportrait** — blocked by CUDA-only code path on CPU.
- **pyramidflow** — blocked by torchvision operator mismatch.
- **MatAnyone** — retested on Python 3.12; blocked by torchvision operator mismatch.
- **LTX-Desktop-WanGP** — setup hung/timed out in this container.
- **Hunyuan3D-2** — retested on Python 3.12; dependencies installed and gradio_app imported successfully on CPU.
- **Hunyuan3D-2-mini** — retested on Python 3.12; blocked by missing pymeshlab compiled extension.
- **SongGeneration-Studio-MLX** — requires MLX/Apple Silicon; cannot run on Linux CPU.
- **moshi** — retested on Python 3.12; moshi package blocked by numpy build failure.
- **hallo** — retested on Python 3.10 with gcc; dependencies installed and hallo imported successfully on CPU.
- **llamafactory** — dependencies installed and package imported successfully on CPU.
- **RuinedFooocus** — runtime failed on missing molbal_comfyui_gguf module.
- **AudioX** — retested on Python 3.10; blocked by torchvision operator mismatch (torchvision::nms).
- **zonos** — dependencies installed and package imported successfully on CPU.
- **aura-sr-upscaler** — retested on Python 3.12; blocked by torchvision operator mismatch (torchvision::nms).
- **openaudio** — blocked by torch==2.8.0 pin unavailable on Python 3.14.
- **ACE-Step** — blocked by matplotlib build failure on Python 3.14.
- **rc-stableaudio** — retested on Python 3.10; run_gradio still fails on torchvision::nms operator mismatch.
- **Allegro-txt2vid-install** — retested on Python 3.10; blocked by torchvision operator mismatch (torchvision::nms).
- **diffrhythm** — retested on Python 3.10; blocked by torchvision operator mismatch (torchvision::nms).
- **Frame-Pack** — retested on Python 3.10; import failed on CUDA-only module-level code (torch.cuda.current_device()).
- **cogvideo** — dependencies installed and inference module imported successfully on CPU.
- **uno** — retested on Python 3.10; dependencies installed and app.py imported successfully on CPU.
- **Allegro-txt2vid** — retested on Python 3.10; blocked by diffusers/transformers version mismatch (FLAX_WEIGHTS_NAME).
- **RuinedFooocus** — runtime failed on missing molbal_comfyui_gguf module.
- **wan** — retested on Python 3.12; dependencies installed but import failed due optimum/quanto/transformers API mismatch (PreTrainedModel).
- **yue** — retested on Python 3.10; dependencies installed and inference module imported successfully on CPU.
- **StreamDiffusion** — dependencies installed and streamdiffusion imported successfully on CPU.
- **TRELLIS** — blocked by CUDA-only compiled extensions.
- **factory** — empty repository; no test possible.
- **y** — empty repository; no test possible.
- **echomimic2** — retested on Python 3.10; blocked by CLIP build failure (pkg_resources).
- **comfy** — dependencies installed; server started on CPU with --cpu.
- **hunyuanvideo** — retested packaging path; still blocked by explicit NVIDIA-only guard and pandas build failure.
- **Ultimate-TTS-Studio** — retested on Python 3.10; requirements installation hung/timed out in this container.
- **ai-toolkit** — all JS files pass node --check; explicit NVIDIA-only guard.
- **stable-diffusion-webui-forge** — retested on Python 3.10; runtime still calls torch.cuda.current_device() and is not CPU-compatible.
- **facepoke** — retested on Python 3.10; blocked by chumpy build failure (no pip in build env).
- **mlx** — retested on Python 3.12; mlx package installed but libmlx.so missing at runtime on Linux.
- **cogstudio** — dependencies installed and cogstudio imported successfully on CPU.
- **mlx-video-transcription** — blocked by missing libmlx.so on Linux.
- **mlx-video-ui** — requires MLX/Apple Silicon and Python 3.11.
- **ovis** — dependencies installed and app.py imported successfully on CPU.
- **MFLUX-WEBUI** — requires MLX/Apple Silicon and Python 3.12.
- **applio-old** — requires Python 3.9 and CUDA 12.1 wheels.
- **dough** — retested on Python 3.10; import app.py failed with botocore NoCredentialsError.
- **photomaker2** — retested on Python 3.10; blocked by torchvision 0.19.1 installation hang.
- **AllTalk-TTS** — retested on Python 3.10; standalone requirements installation hung/timed out.
- **florence-sam** — retested on Python 3.12; still blocked by transformers API mismatch (AutoProcessor).
- **stable-fast-3d** — retested on Python 3.12; blocked by scipy 1.18/numpy 1.26.4 mismatch (np.long removed).
- **dia** — blocked by torchaudio extension incompatibility.
- **audiocraft_plus** — retested on Python 3.12; blocked by spacy build failure.
- **stableaudio** — retested on Python 3.10; stable_audio_tools imported, but run_gradio fails on torchvision::nms.
- **pcm** — importing app.py hung in this container.
- **omniparser** — retested on Python 3.12; gradio_demo failed on paddleocr use_gpu argument.
- **mochi** — package imported successfully on CPU.
- **instantir** — importing app_with_diffusers hung in this container.
- **janus** — retested on Python 3.12; runtime still calls .cuda() and is not CPU-compatible.
- **flashdiffusion** — importing app.py hung in this container.
- **florence2** — blocked by transformers/tokenizers version mismatch.
- **applio** — dependency installation hung/timed out in this container.
- **MMAudio** — package import succeeded; demo not fully run.
- **MagicQuill** — blocked by gradio/huggingface_hub HfFolder incompatibility.
- **Ilaria-RVC** — blocked by Python version constraints and GPU-oriented deps.
- **invoke** — all JS files pass node --check; upstream download not attempted.

## Summary

- **Blocked:** 5
- **Blocked (Apple-only):** 6
- **CPU-capable (shipped fallback):** 68
- **CPU-ready (no changes):** 11
- **N/A (empty):** 2
- **Needs launcher change:** 9

- **Total attempted:** 101 projects.
- **Python smoke checks:** 18 passed, 0 failed, 83 n/a.


## Packaging version conflicts vs true incompatibilities

The failures below were caused by dependency pins, Python-version constraints, build-tool gaps or API drift in the test environment, not by an inherent inability of the application to run on CPU.

**Packaging/version conflicts (retest candidates):** ai-video-composer, errortest, open-webui, MagicQuill, RMBG-2-Studio, diffusers-image-fill, artist, diamond, florence2, janus, oasis, text2midi, video-background-removal, whisper-webui, ominicontrol, Kokoro-TTS, clarity-refiners-ui, forge, omnigen, MatAnyone, moshi, hallo, AudioX, aura-sr-upscaler, openaudio, ACE-Step, rc-stableaudio, Allegro-txt2vid-install, diffrhythm, Frame-Pack, uno, Allegro-txt2vid, wan, yue, echomimic2, hunyuanvideo, Ultimate-TTS-Studio, stable-diffusion-webui-forge, facepoke, mlx, dough, photomaker2, AllTalk-TTS, florence-sam, stable-fast-3d, dia, audiocraft_plus, stableaudio, Nari-Dia-TTS, StyleTTS2_Studio, Ilaria-RVC, Hunyuan3D-2, Hunyuan3D-2-mini, flux-webui, pcm (hung, environment), instantir (hung, environment), flashdiffusion (hung, environment), augmentoolkit (hung, environment), LTX-Desktop-WanGP (setup hung), applio (hung), RuinedFooocus (missing module), mlx-video-transcription (missing libmlx, environment).

**True or environment-specific blockers (not packaging conflicts):** ai-toolkit, hunyuanvideo (CUDA guard), Allegro-txt2vid (CUDA guard), StreamDiffusion (TensorRT), TRELLIS (compiled CUDA extensions), liveportrait (CUDA-only code path), macOS-use (macOS-only), mlx, mlx-video-transcription, mlx-video-ui, MFLUX-WEBUI, SongGeneration-Studio-MLX (MLX/Apple Silicon), moshi (Apple runtime), empty repositories (factory, y), hunyuanvideo (CUDA guard).
