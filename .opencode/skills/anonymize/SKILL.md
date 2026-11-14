---
name: Anonymizing paths
description: Scrub machine-specific identifiers — usernames, absolute paths, drive letters, hostnames, IPs, emails, and secrets — from READMEs, diffs, logs, and scripts before publishing a port. Use when preparing write-ups, patches, or screenshots for public release, or when asked to check whether paths are anonymized.
---

# Anonymizing paths

Publish a port without leaking the machine it was built on. Treat this as the last
step before committing or sharing write-ups, patches, and logs.

## 1. Decide what must not ship

| Identifier | Examples | Why it leaks |
| --- | --- | --- |
| POSIX home directories | `/home/alice/...`, `/Users/alice/...` | Username, often reused elsewhere |
| Windows paths | `C:\Users\alice\...`, `D:\Work\proj`, `\\nas\share` | Username, internal project names |
| Hostnames | `alice-laptop`, `gpu-box.local` | Network topology |
| Private IPs | `192.168.1.20`, `10.0.0.5` | Internal network layout |
| Accounts | personal email, cloud project IDs, bucket names | Identity and billing |
| Secrets | API keys, tokens, passwords, SSH key paths | Direct compromise |

Upstream project URLs, license text, and an intentionally published author contact
are fine. Record those as explicit exceptions before scanning.

## 2. Choose placeholders and keep them consistent

| Leak | Placeholder |
| --- | --- |
| `/home/alice/opencode/Fooocus` | `/home/<you>/opencode/Fooocus` |
| `/Users/alice/opencode/Fooocus` | `/Users/<you>/opencode/Fooocus` |
| `C:\Users\alice\.wslconfig` | `C:\Users\<you>\.wslconfig` |
| `D:\Work\proj\model.onnx` | `D:\path\to\model.onnx` |
| `\\nas\team\models` | `\\server\share\models` |
| `alice-laptop.local` | `<host>` |
| `192.168.1.20` | `192.0.2.10` (RFC 5737) |
| `alice@corp.example` | `<user>@example.com` |
| `ABCD1234...` key/token | `<redacted>` |

Rules:

- Use angle-bracket placeholders so a later scan can tell them from real values.
- Keep one convention across the whole repository. The Fooocus write-ups here use
  `/home/<you>`, `/Users/<you>`, `C:\Users\<you>`, and `Z:\path\to\...`.
- Replace only the identifying segment and keep the rest of the path, so the
  command still teaches the reader something.
- For IPs use documentation ranges: `192.0.2.0/24`, `198.51.100.0/24`,
  `203.0.113.0/24`, or `2001:db8::/32`.
- For email and hosts use `example.com`.

## 3. Scan before editing

The bundled scanner is report-only and exits non-zero when it finds a hit:

```bash
python3 .opencode/skills/anonymize/references/anonymize-scan.py .
```

Quick equivalent with ripgrep:

```bash
rg -n --hidden -g '!**/.git/**' \
  -e '(?<![\w.-])/(home|Users|root)/[A-Za-z0-9._-]+' \
  -e '\b[A-Za-z]:[\\/]' \
  -e '(?i)\bUsers\\[A-Za-z0-9._-]+' \
  -e '\b(10|172\.(1[6-9]|2\d|3[01])|192\.168)(\.[0-9]{1,3}){2}\b' \
  -e '\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b' \
  -e '(?i)(api[_-]?key|token|secret|password)\s*[:=]'
```

Review every hit. Report first, then fix; an automatic rewrite can corrupt a diff
or rewrite an upstream URL. The scanner skips `.git`, virtualenvs, dependency
folders, binary files, and its own skill directory; it allows the configured
public contacts and the placeholders `/path/to/`, `:\path\to\`, and
`\\server\share`.

## 4. Fix safely

- Prefer exact-text edits over shell `sed` for paths with backslashes. Shell
  escaping turns `\\` into `\\\\` and breaks patch parsing; edit the raw bytes.
- Never change the structure of a patch. Keep `@@` hunk counts, `diff --git`
  headers, and line order unchanged. Replacing text inside a line leaves hunk
  counts intact; adding or removing lines does not.
- If a leaked path appears in a patch's `diff --git a/...`, `---`, or `+++`
  header, replace it in all three places consistently.
- Leave upstream URLs, vendor names, and the intended public author contact alone.
- If the identifier was already committed, cleaning the working tree is not
  enough. Rewrite history with `git filter-repo` (or `filter-branch`) before
  publishing, and rotate any committed secret.

## 5. Verify

- Re-run the scanner until only allowlisted values remain.
- Scan commit metadata separately; the file scanner does not read git objects:
  `git log --all --format='%h %an <%ae>'`.
- Run `git apply --stat <patch>` for every diff to confirm it still parses.
- Re-check Markdown links and anchors.
- If the repo was already public, search history too: `git log -p`, `git grep <term> $(git rev-list --all)`.

## Checklist

- [ ] Scanner is clean except deliberate, documented exceptions.
- [ ] Placeholders follow one convention across the repo.
- [ ] Commit author names/emails are intentional and acceptable to publish.
- [ ] Every diff still parses with `git apply --stat`.
- [ ] Links and anchors still resolve.
- [ ] No secrets remain in the working tree or in git history.
