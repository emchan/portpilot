---
name: Porting AI apps
description: Plan and run an end-to-end port of an AI application to a new accelerator such as Intel AMX, AMD ROCm, or Google TPU. Use when starting a port or deciding which porting skill to load.
---

# Porting AI apps

Port in phases. Load the phase skill by its exact ID when you reach it:

| Phase | Skill ID | Goal |
| --- | --- | --- |
| 1. Bring-up | `porting-bringup` | Reproducible baseline, native access path, conditional backend, dependency changes |
| 2. Verification | `porting-verification` | Weights loaded, tensors finite, real image, UI path works |
| 3. Performance | `porting-performance` | Backend-native kernels, host tuning, honest cold/steady numbers |
| 4. Agent workflow | `porting-agents` | Tight evidence-driven loop and deliberate model escalation |
| 5. Publish | `anonymize`, `polite-language` | Scrub identifiers; check non-disparaging wording |

## Universal rules

1. **Correctness first, speed second.** A fast port that silently loads no weights is worse than a slow one that works.
2. **New hardware rarely breaks compute; device assumptions and dependency changes do.**
3. **Keep the new backend conditional.** Existing CUDA/MPS/XPU/CPU paths should behave exactly as before.
4. **Silent fallbacks are the enemy.** Assert that the intended backend, kernels, and weights were actually used.
5. **Measure cold and steady state separately.** Compilation and first-run caches distort benchmarks.

## Definition of done

A port is done when all of these are true:

- The app imports without CUDA assumptions.
- The intended accelerator is detected and selected.
- Core ops run at the target dtype.
- Checkpoint keys match and the weights actually load.
- Conditioning and latents are finite.
- A full generation produces a real, non-flat image.
- The app's own UI worker completes a generation.
- The intended accelerator and kernels are proven, and reported memory is compared with real allocatable memory.
- Feature coverage is recorded and fallbacks are explicit.
- Cold-start and steady-state timings are recorded.
- The bug-driven test set in `porting-verification` has been run, with commands and output saved.
- Write-ups, diffs, and scripts contain no machine-specific identifiers.
- Write-ups use non-disparaging, status-describing language.

For the consolidated guide, case studies, and Fooocus examples, read
[`skills.md`](../../../skills.md) in the repository root.
