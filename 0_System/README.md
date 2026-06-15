# 0_System — Repo Engine

The machinery that makes this workspace work. Founders rarely need to open this folder —
the bootstrap and skills drive everything.

## What's here

| Path | Purpose |
|---|---|
| `bootstrap/setup.mjs` | Links `CLAUDE.md → AGENTS.md` (symlink on Mac/Linux; generated copy on Windows) + environment readiness checks (Node, git). Cross-platform, dependency-free Node. Safe to re-run. |
| `scripts/scan-skills.py` | Regenerates `.agents/skills/skills.json` (a slim `{name, path, enabled}` registry) from the SKILL.md files on disk. Run after adding or removing a skill: `python3 0_System/scripts/scan-skills.py` |
| `scripts/parse-sources.py` | Tiered `raw/ → processed/` converter (the `ingest-sources` engine). Auto-uses the best converter installed (Docling → MarkItDown → built-in text/CSV; stubs the rest), mirrors subfolders, and **recommends installs but never runs them**. `--plan` dry-runs the analysis; `--force` reconverts. `python3 0_System/scripts/parse-sources.py` |

## How the pieces fit

- **`AGENTS.md` is the source of truth.** `CLAUDE.md` is a **symlink to `AGENTS.md`** (created
  by `setup.mjs`; Windows falls back to a generated copy), and is gitignored. Edit `AGENTS.md`,
  re-run setup, never hand-edit `CLAUDE.md`.
- **Skills are auto-discovered** from `.agents/skills/` (each `SKILL.md`). The frontmatter is the
  source of truth for what a skill does and when it fires. The manifest (`skills.json`) is a slim
  registry — it records `name`, `path`, and `enabled` state only (no descriptions, so it can't go
  stale); `scan-skills.py` preserves enabled flags when it rescans.
- **No servers, no background processes.** This repo is plain files; everything runs
  inside the agent session.

This engine is a productized fork of the WNCP team OS
(`WNCP-AI/wncp-team-shared-projects`, bootstrap rework branch) — same conventions,
founder content slots instead of WNCP content.
