---
name: find-skills
description: >
  Locates the right skill across all buckets. Trigger when a founder asks:
  "what skills are available", "which skill should I use", "find a skill",
  "what can you do", "show me the skills", "what's in this system", or otherwise
  wants to know what skills exist and which one to reach for next.
---

# find-skills — Skill Finder

The entry point for the Founder OS skill catalog. When a founder asks what's available, or isn't
sure which skill to run next, this skill finds the right one by reading the skills **on disk** —
each `SKILL.md` frontmatter is the source of truth for what that skill does and when it fires.

---

## How to find and route (the procedure)

1. **List what exists.** Glob `.agents/skills/**/SKILL.md` and read each file's frontmatter
   `name` + `description`. The `description` spells out exactly when that skill should fire — match
   the founder's ask against it. Do this every time; do not rely on a list kept inside this file.
2. **Respect enabled state.** Read `.agents/skills/skills.json` — a slim registry of
   `{name, path, enabled}`. Skip any skill marked `enabled: false`. A skill that exists on disk but
   is missing from the registry is treated as **enabled** (the registry just hasn't been
   regenerated yet — it never overrides what's on disk).
3. **Route.** Point the founder to the best-matching skill. If two plausibly fit, name both and ask
   which they want.

> **Why disk-first:** `skills.json` stores only enabled flags — never descriptions — so it cannot go
> stale against the real skills. The directory is always the truth; the registry just says what's
> turned off. If the registry looks out of date (a folder has no entry, or an entry has no file),
> regenerate it: `python3 0_System/scripts/scan-skills.py`.

---

## How skills are organised

Skills live in buckets under `.agents/skills/`:

- **`find-skills/`** — this finder (you are here); always available.
- **`wncp-ai/`** — the WNCP pipeline, numbered in deliverable order (`1-…` → `9-…`). Run them in
  order across the Product Week; each reads the previous one's output. Read the folder names and
  each `SKILL.md` description (step 1) for the current set and what each does.
  - **`wncp-ai/util_/`** — file-access utilities (`util_get_user_info`, `util_get_company_info`,
    `util_get_inputs`) that own the `0_User/` / `0_Company/` file contracts and the central input
    lookup. Mostly invoked BY other skills — but `util_get_user_info` and `util_get_company_info`
    are also the direct path when a founder wants to view or update their own profile or company
    facts.
- **function groups** — general / third-party skills added over time (F8); pull them in with the
  `import-skills` skill (lives in `wncp-ai/`).

That's the stable structure. The specific skills, their order, and their triggers come from the
`SKILL.md` files themselves (step 1) — not from a catalog maintained here, which would drift.
