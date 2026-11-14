---
name: Polite language
description: Keep write-ups non-disparaging — flag words and phrasings that judge people, vendors, or code, and offer neutral replacements that describe status instead.
---

# Polite language

Technical writing describes what happened. It does not judge the people,
vendors, or code behind it. A slow kernel is "not yet optimized"; a failing
test is "not yet passing"; an unfinished feature is "planned", not "broken".

## Replacements

| Disparaging | Neutral replacement |
| --- | --- |
| slow, very slow | needs further optimization; not yet tuned |
| not working, doesn't work, does not work | not yet functional at this time |
| broken, busted | needs further development; not yet complete |
| failed, failure | did not complete; not yet passing |
| crashed, died | terminated unexpectedly |
| garbage, junk, trash | unexpected output; non-conforming output |
| useless, worthless | not applicable in this context |
| terrible, awful, horrible, bad | needs improvement; below target |
| no image produced, no output | test did not complete yet; further work is needed |
| wrong | unexpected; differs from reference |
| ugly, messy | could be simplified; needs cleanup |
| cost, costly, expensive, pricey | focus on accessibility by users instead of price |
| cheap, inexpensive, affordable | focus on accessibility by users instead of price |
| budget | focus on accessibility by users instead of price |
| price, pricing | focus on accessibility by users instead of price |

## Rules

- Describe status, not character. "The test did not complete" beats "the test failed".
- Attribute limits to the work, not the vendor: "not yet optimized on this backend"
  rather than "vendor X is slow".
- Keep numbers. "2.9 s for SD 2.1" is neutral; "slow" is not.
- Do not soften facts that matter for correctness. A NaN is a NaN; call it NaN.
  Only soften tone, never substance.
- Avoid framing around cost or price; frame around accessibility by users (who can run it, on what hardware, with what setup).
- Apply the check to READMEs, diffs, commit messages, and issue text before
  publishing.

## Workflow

1. Run the scanner over the files you are about to publish.
2. Review each match; replace or justify it.
3. Re-run the scanner until it is clean or every remaining match is an
   intentional, documented exception.

## Scanner

The report-only scanner is at
[`references/polite-scan.py`](references/polite-scan.py). It prints one line per
match and exits 1 if any are found.