---
name: Porting with AI agents
description: Run an agent-driven hardware port effectively — keep the loop tight and evidence-based, escalate models deliberately, challenge assumptions against installed libraries, and convert silent failures into regression checks.
---

# Porting with AI agents

Agent-driven porting works best when the loop is tight and evidence-based.

## Working rules

- Start with fast/free models, then escalate to stronger models when progress stalls.
- Ask for the smallest reproducible failure, not a full rewrite.
- Prefer patches at existing extension points (`modules/patch.py`) over model surgery.
- Require commands, logs, and diffs to be captured in the repo.
- Re-check assumptions against the installed library. Agents often assume return arity, property names, or API shapes.
- Watch for late-binding bugs in monkeypatches; bind the original function explicitly.
- Make the agent explain the root cause before accepting a fix.
- Add a regression check for every silent failure it finds.
- Run the bug-driven test set from `porting-verification` and record the command, output, and expected result for each test.
- Keep a human in the loop for vendor support decisions, credentials, and destructive changes.

## Model escalation

1. Try a fast/free model on the smallest failing case.
2. If it loops or guesses, capture the command, log, and diff, then escalate.
3. Give the stronger model the evidence, not the whole history.
4. Record which model solved which class of problem for future ports.

## Handoff checklist

- [ ] Repro command and expected result are recorded.
- [ ] Hardware, driver, Python, and package versions are recorded.
- [ ] The failure is reduced to the smallest case that still fails.
- [ ] The root cause is stated, not just the patch.
- [ ] A regression check covers the failure.
- [ ] The suggested test set has been run, with commands and saved output.
- [ ] Commands, logs, and diffs are in the repo.

For the full porting workflow, load `porting` first.
