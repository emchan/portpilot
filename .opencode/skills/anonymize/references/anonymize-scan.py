#!/usr/bin/env python3
"""Report machine-specific identifiers in text files.

Usage:
    python3 anonymize-scan.py [PATH ...]

Report-only: prints one line per match and changes nothing. Exits 1 if any
match is found, so it can gate a commit or CI step. Review the output before
editing; some patterns are deliberately broad and may flag harmless text.
"""

from __future__ import annotations

import os
import re
import sys

SKIP_DIRS = {
    ".git",
    ".hg",
    ".svn",
    "node_modules",
    ".venv",
    "venv",
    "env",
    "__pycache__",
    "dist",
    "build",
    ".mypy_cache",
    ".pytest_cache",
}

TEXT_EXTENSIONS = {
    ".md", ".markdown", ".diff", ".patch", ".sh", ".bash", ".zsh",
    ".bat", ".cmd", ".ps1", ".py", ".txt", ".log", ".yaml", ".yml",
    ".toml", ".json", ".cfg", ".ini", ".conf", ".env",
}

# Intentional public contacts and upstream identities. Add to this list only
# after confirming the value is meant to be published.
ALLOWED_VALUES = {
    "emchan.aicoding@gmail.com",
    "git@github.com",
    "noreply@github.com",
    "actions@github.com",
}

# Matches containing any of these are already anonymized.
PLACEHOLDERS = (
    "<you>",
    "<user>",
    "<host>",
    "<host-ip>",
    "<name>",
    "<project-id>",
    "<bucket>",
    "<redacted>",
)

# Path-shaped placeholders used by this repo's write-ups.
PLACEHOLDER_PATHS = (
    "/path/to/",
    ":\\path\\to\\",
    "\\server\\share",
    "\\<server>\\",
)

PATTERNS = {
    # /home/alice, /Users/alice, /root/alice (not URL route segments)
    "posix-home": r"(?<![\w.-])/(?:home|Users|root)/[A-Za-z0-9._-]+",
    # /mnt/c/Users/alice on WSL
    "wsl-mount": r"/mnt/[a-z]/[A-Za-z0-9._-]+",
    # C:\Users\alice, D:\Work\proj, C:/Users/alice
    "windows-drive": r"\b[A-Za-z]:[\\/]{1,2}[^\s\"'`]+",
    # Users\alice without a drive letter
    "windows-user": r"(?i)\bUsers\\[A-Za-z0-9._-]+",
    # \\server\share
    "unc": r"\\\\[A-Za-z0-9._-]+\\[A-Za-z0-9$._-]+",
    # alice-laptop.local, gpu-box.lan
    "local-host": r"\b[a-z0-9][a-z0-9-]*\.(?:local|lan|internal|home)\b",
    # user@host for internal hosts
    "user-at-host": r"\b[A-Za-z0-9._-]+@[A-Za-z0-9.-]+\.(?:local|lan|internal|home)\b",
    # RFC 1918 private addresses
    "private-ip": r"\b(?:10(?:\.\d{1,3}){3}|172\.(?:1[6-9]|2\d|3[01])(?:\.\d{1,3}){2}|192\.168(?:\.\d{1,3}){2})\b",
    # Any email address, including personal accounts
    "email": r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b",
    # key = value or token: value
    "secret-assignment": r"(?i)\b(?:api[_-]?key|access[_-]?token|auth[_-]?token|token|secret|password|passwd)\b\s*[:=]\s*\S+",
    # PEM private keys
    "private-key": r"-----BEGIN [A-Z ]*PRIVATE KEY-----",
}


def is_placeholder(text: str) -> bool:
    if any(token in text for token in PLACEHOLDERS):
        return True
    return any(token in text for token in PLACEHOLDER_PATHS)


def scan_file(path: str) -> int:
    hits = 0
    try:
        with open(path, encoding="utf-8", errors="replace") as handle:
            lines = handle.read().splitlines()
    except OSError as exc:
        print(f"{path}: cannot read: {exc}", file=sys.stderr)
        return 0

    for lineno, line in enumerate(lines, 1):
        for label, pattern in PATTERNS.items():
            for match in re.finditer(pattern, line):
                value = match.group(0)
                if value in ALLOWED_VALUES or is_placeholder(value):
                    continue
                hits += 1
                print(f"{path}:{lineno}: [{label}] {value}")
    return hits


def main(argv: list[str]) -> int:
    roots = argv or ["."]
    # Skip the whole skill directory (SKILL.md examples plus references/).
    self_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + os.sep
    total = 0

    def in_skill_dir(path: str) -> bool:
        # This skill's own examples and regexes are intentionally full of
        # identifiers, so do not report them back to the user.
        return os.path.abspath(path).startswith(self_dir)

    for root in roots:
        if os.path.isfile(root):
            if not in_skill_dir(root):
                total += scan_file(root)
            continue
        for dirpath, dirnames, filenames in os.walk(root):
            dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
            for name in filenames:
                if os.path.splitext(name)[1].lower() not in TEXT_EXTENSIONS:
                    continue
                path = os.path.join(dirpath, name)
                if in_skill_dir(path):
                    continue
                total += scan_file(path)

    print(f"\n{total} match(es). Nothing was changed.", file=sys.stderr)
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
