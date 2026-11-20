# Reproduce the Pinokio Factory Apps Study (single-shot prompt)

Use this prompt to reproduce the full study in one pass.

---

**Prompt:**

Consider all repositories in the GitHub organization https://github.com/pinokiofactory. Analyze the `main` branch tip of each repository (source snapshots fetched from `https://codeload.github.com/pinokiofactory/<repo>/tar.gz/refs/heads/main` on 2026-11-20); **no git tag was analyzed**. For each repository:

1. Fetch the repository tree and any `requirements*.txt` files (root or nested). Record their full dependency lists.
2. Fetch README.md, install.js, and torch.js (if present) and scan them for platform/GPU support signals (NVIDIA-only markers, AMD/ROCm, macOS/Apple Silicon/MPS, CUDA).
3. Clone each repository locally when needed and inspect Python imports for repos that lack a requirements file. Record the default-branch (`main`) commit SHA of every snapshot that is analyzed.
4. Build a Markdown table named `results/pinokio-apps.md` with columns:
   - Repository (linked to its GitHub URL)
   - Platform support (NVIDIA only / NVIDIA / AMD / Mac / Cross-platform / Mac (Apple Silicon) only)
   - Dependencies (combined, version numbers stripped, no install-command noise; merge requirements.txt + install.js packages; drop superfluous `req:` / `editable:` / `install.js:` labels)
   - CUDA-only packages (not supported on AMD/Apple)
   - Porting difficulty (estimate per app)
5. Add a summary section listing NVIDIA/CUDA-only dependencies with: short description, porting difficulty (AMD/Apple), and which repos rely on each.
6. Produce a detailed report for each app in the `results/` folder (one analysis per package/repository, saved as `results/<repo>.md`). Each report must state:
   - Package name
   - Description
   - Original git URL
   - Dependencies (from `requirements.txt` or `install.js`)
   - Platforms supported
   - Number of CUDA kernels
   - Lines of CUDA code
   - Lines of non-CUDA code
   - CUDA-related functions used
7. Save everything to `results/pinokio-apps.md` (create the `results/` directory if needed).
8. Create an `analysis/` folder and write `analysis/kernels.md` covering:
   - Which projects use CUDA Graphs (`cudaGraphLaunch`, `cudaGraphInstantiate`, `torch.cuda.graph`, stream capture, etc.) and where.
   - Which projects use Triton, distinguishing direct Python code from optional `triton` / `triton-windows` wheel installs, and noting whether any `@triton.jit` kernels exist.
   - Whether Vulkan, explicit Metal APIs, Apple MPS, or MLX are used.
   - Attention kernels: FlashAttention, SageAttention, xformers, PyTorch SDPA, FlashInfer/vLLM/PagedAttention.
   - For every signal, cite `file:line` evidence from the repository snapshot and state the porting implication for AMD/ROCm and Apple/MPS.
   - Add a **Commit** column to every per-project table in `analysis/kernels.md` (not the at-a-glance summary), showing the short analyzed SHA and linking it to `https://github.com/pinokiofactory/<repo>/commit/<sha>`.
   - Make every `file:line` reference a direct link to `https://github.com/pinokiofactory/<repo>/blob/<sha>/<path>#L<line>`; use a dedicated **Line** column where one exists and a **Line / evidence** column elsewhere.
9. In the same folder, write `analysis/quantization.md` covering:
   - Quantized weights and runtime quantization settings; call out false positives such as dtype tables or audio codec quantizers.
   - GGUF / llama.cpp usage, including CUDA-only loaders.
   - Quantization libraries: bitsandbytes, torchao, optimum-quanto; note the absence of GPTQ, AWQ, ExLlama, HQQ, ONNX Runtime quantization, TensorRT INT8/FP8, and vLLM quantization flags.
   - For every signal, cite `file:line` evidence and state the porting implication for AMD/ROCm and Apple/MPS.
   - Put an **executive summary** at the top counting instances of each explicit datatype (`float`/FP32, `float16`/FP16, `bfloat16`/BF16, `float8`/FP8, NVFP4/FP4, int8, uint8, int4, NF4, int16/32/64, float64, bool, complex) plus cast/quantization API signals, with matching-line counts and affected-repo counts; state the counting convention and include zero-match datatypes.
   - Add a detailed table of every cast and precision-manipulation line with **Project**, **Commit** (short SHA linked to the commit), **Line** (direct blob link with `#L<line>`), **Datatype(s)**, **Kind** (`explicit cast`, `mixed precision`, `quantization API`, `dtype declaration`, `checkpoint / config`) and the matching evidence snippet.
10. Scan every snapshot for Hugging Face model pulls (manifest `repo`/`uri` fields, `hf download`, `snapshot_download`, `from_pretrained`, and `huggingface.co` URLs) and write `analysis/models.md`. Deduplicate by model repository, exclude obvious non-model repos (wheel hosts / attention-wheel downloads), and for each model give a direct link, the projects that use it (linked), inferred format (GGUF / PyTorch / ONNX / Other) and precision. Derive precision from the model's own safetensors header JSON where possible: fetch the launcher-requested `.safetensors` file with an HTTP Range request, parse its header, and compute parameter counts per tensor dtype; report the dominant dtype as the default and list every dtype holding ≥0.1% of parameters when a checkpoint is mixed-precision (note that NF4/INT4 weights appear as packed `UINT8` tensors). Fall back to Hugging Face's aggregated `safetensors` metadata (mark as *repo aggregate*) and then filename/config inference, marking unknown values unspecified. Include summary tables of format, precision source, and default precision counts plus a tensor-dtype detail table with params, tensor counts and shares. Also record **all tensor shapes** from those safetensors headers in a dedicated table with Model, File, Dtype, Shape, Tensors and Params columns (shape product × tensor count), covering every distinct shape observed. Cite evidence with direct blob links carrying `#L<line>` anchors at the analyzed commit.
11. Use the exact final paths `results/pinokio-apps.md`, `analysis/models.md`, `results/<repo>.md`, `analysis/kernels.md`, and `analysis/quantization.md`. Link all three analysis notes (`analysis/kernels.md`, `analysis/quantization.md`, `analysis/models.md`) to `../results/pinokio-apps.md`, and link `analysis/quantization.md` to `kernels.md`.
12. State the analyzed commit SHA in every `results/<repo>.md` report (N/A for empty repositories) and note the snapshot date and commit-recording convention in the summary and both analysis notes.

Output the complete table, summary, and analysis notes.
