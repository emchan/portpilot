#!/usr/bin/env python3
"""Report disparaging language in text files.

Usage:
    python3 polite-scan.py [PATH ...]

Report-only: prints one line per match and changes nothing. Exits 1 if any
match is found, so it can gate a commit or CI step. Review the output before
editing; some patterns are broad and may flag harmless text, in which case
justify the exception in the write-up.
"""

from __future__ import annotations

import os
import re
import sys

SKIP_DIRS = {
    ".git", ".hg", ".svn", "node_modules", ".venv", "venv", "env",
    "__pycache__", "dist", "build", ".mypy_cache", ".pytest_cache",
}

TEXT_EXTENSIONS = {
    ".md", ".markdown", ".diff", ".patch", ".sh", ".bash", ".zsh",
    ".bat", ".cmd", ".ps1", ".py", ".txt", ".log", ".yaml", ".yml",
    ".toml", ".json", ".cfg", ".ini", ".conf", ".env", ".html",
}

# (pattern, neutral replacement). Patterns are case-insensitive word/phrase matches.
REPLACEMENTS = [
    (r"\bslow\b", "needs further optimization / not yet tuned"),
    (r"\bvery slow\b", "needs further optimization"),
    (r"\bnot working\b", "not yet functional at this time"),
    (r"\bdoesn'?t work\b", "not yet functional at this time"),
    (r"\bdoes not work\b", "not yet functional at this time"),
    (r"\bbroken\b", "needs further development / not yet complete"),
    (r"\bbusted\b", "needs further development"),
    (r"\bfailed\b", "did not complete / not yet passing"),
    (r"\bfailure\b", "did not complete"),
    (r"\bcrashed\b", "terminated unexpectedly"),
    (r"\bdied\b", "terminated unexpectedly"),
    (r"\bgarbage\b", "unexpected output"),
    (r"\bjunk\b", "unexpected output"),
    (r"\btrash\b", "unexpected output"),
    (r"\buseless\b", "not applicable in this context"),
    (r"\bworthless\b", "not applicable in this context"),
    (r"\bterrible\b", "needs improvement / below target"),
    (r"\bawful\b", "needs improvement / below target"),
    (r"\bhorrible\b", "needs improvement / below target"),
    (r"\bno image produced\b", "test did not complete yet; further work is needed"),
    (r"\bno output\b", "test did not complete yet; further work is needed"),
    (r"\bwrong\b", "unexpected / differs from reference"),
    (r"\bugly\b", "could be simplified"),
    (r"\bmessy\b", "needs cleanup"),
    (r"\bcost\b", "focus on accessibility by users instead of price"),
    (r"\bcostly\b", "focus on accessibility by users instead of price"),
    (r"\bexpensive\b", "focus on accessibility by users instead of price"),
    (r"\bpricey\b", "focus on accessibility by users instead of price"),
    (r"\bcheap\b", "focus on accessibility by users instead of price"),
    (r"\binexpensive\b", "focus on accessibility by users instead of price"),
    (r"\baffordable\b", "focus on accessibility by users instead of price"),
    (r"\bbudget\b", "focus on accessibility by users instead of price"),
    (r"\bprice\b", "focus on accessibility by users instead of price"),
    (r"\bpricing\b", "focus on accessibility by users instead of price"),
]


def scan_file(path):
    try:
        with open(path, encoding="utf-8", errors="replace") as f:
            lines = f.readlines()
    except (OSError, UnicodeDecodeError):
        return []
    matches = []
    for i, line in enumerate(lines, 1):
        low = line.lower()
        for pat, repl in REPLACEMENTS:
            for m in re.finditer(pat, low):
                matches.append((i, m.group(0), repl, line.rstrip()))
    return matches


def iter_files(paths):
    if not paths:
        paths = ["."]
    for root in paths:
        if os.path.isfile(root):
            yield root
            continue
        for dirpath, dirnames, filenames in os.walk(root):
            dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
            for fn in filenames:
                ext = os.path.splitext(fn)[1].lower()
                if ext in TEXT_EXTENSIONS:
                    yield os.path.join(dirpath, fn)


def main():
    paths = sys.argv[1:]
    total = 0
    for path in iter_files(paths):
        ms = scan_file(path)
        for line_no, word, repl, line in ms:
            print(f"{path}:{line_no}: {word!r} -> {repl}")
            print(f"    {line}")
            total += 1
    if total:
        print(f"\n{total} match(es).")
        sys.exit(1)
    print("0 match(es). Nothing was changed.")
    sys.exit(0)


if __name__ == "__main__":
    main()
