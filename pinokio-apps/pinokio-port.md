# Reproduce the Pinokio Factory Apps Study (single-shot prompt)

Use this prompt to reproduce the full study in one pass.

---

**Prompt:**

Consider all repositories in the GitHub organization https://github.com/pinokiofactory. For each repository:

1. Fetch the repository tree and any `requirements*.txt` files (root or nested). Record their full dependency lists.
2. Fetch README.md, install.js, and torch.js (if present) and scan them for platform/GPU support signals (NVIDIA-only markers, AMD/ROCm, macOS/Apple Silicon/MPS, CUDA).
3. Clone each repository locally when needed and inspect Python imports for repos that lack a requirements file.
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

Output the complete table and summary.