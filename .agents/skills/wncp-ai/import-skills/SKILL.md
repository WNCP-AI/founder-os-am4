---
name: import-skills
description: >
  Finds and imports useful third-party skills from trusted public sources into this repo, then
  makes them discoverable through find-skills. Triggers when the founder says "find skills I could
  add", "import a skill", "are there skills for X", "browse the skill library", "add a community
  skill", "what external skills are useful", or otherwise wants to extend the OS with skills WNCP
  did not author. Reads founder context (0_User/, 0_Company/) to recommend skills that fit, pulls
  the chosen one (npx skills, or a git fallback) into a function bucket under .agents/skills/,
  records its source + license in skills-manifest.json, and re-indexes so find-skills surfaces it.
---

# import-skills — Add Third-Party Skills

This is the gateway to the **general / third-party skill layer** (PRD F8). The founder uses it to
discover skills the wider community has built and pull the useful ones into *their own* copy of the
OS — extending it past the WNCP pipeline.

**How this respects copyright.** Founder OS ships only this skill and a catalog of **pointers**
(`reference/catalog.md`). It never bundles third-party skill source. *You* (the founder, on your
machine) pull a skill from its upstream repo — exactly like `npm install`. WNCP is not in the
redistribution chain. In return, the skill records each import's source + license so attribution
travels with you if you ever share the repo.

Be a calm guide: recommend a few good fits, let the founder choose, pull one cleanly, confirm it
works. Never bulk-import.

---

## Phase 1 — Discover & recommend (agent-guided)

1. **Load founder context** — call `util_get_user_info` and `util_get_company_info` for domain,
   stage, role, what they're building, and where they are in the product week. Recommendations
   must fit *this* founder, not a generic list.
2. **Clarify if the need is fuzzy.** If the ask is broad ("any skills for me?") or context is thin,
   ask 1–2 short follow-up questions first — what they're working on this week, the pain, and
   whether it's build vs. strategy vs. raise — then recommend. Never dump the whole catalog.
3. **Source candidates, recommended-first:**
   - **WNCP AI Recommended** — `reference/catalog.md` §2 (specific vetted picks, each with who
     it's for and when to use it).
   - **Live search** for anything bespoke — `npx skills find "<topic>"` (skills.sh) or the
     indexes in catalog §1.
4. **Judge fit, then present a short ranked list (3–5).** For each: what it does, source repo,
   license, and **one line on why it fits this founder right now** — tie it to their stage or
   current pipeline step. Do not pull anything yet; the founder picks.

## Phase 2 — Import (only on the founder's pick)

For the chosen skill, follow `reference/import-mechanics.md`. In short:

1. **Check the license first** (see License rules below). If it isn't permissive, stop and tell
   the founder; only proceed on an explicit override.
2. **Pull the skill** into a function bucket — `.agents/skills/<function>/<skill>/`
   (e.g. `method/`, `design/`, `documents/`, `founder-biz/`, `durability/`):
   - **Primary:** `npx skills add <owner/repo> --skill <name>` (then move it into the bucket).
   - **Fallback (no Node):** `git sparse-checkout` of the skill subpath, or `curl` the raw files.
3. **Preserve attribution:** copy the upstream `LICENSE` (and `NOTICE` if present) into the
   skill folder.
4. **Record provenance:** add an entry to `.agents/skills/skills-manifest.json` and regenerate
   `.agents/skills/THIRD_PARTY_NOTICES.md` (schema + steps in `reference/import-mechanics.md`).

## Phase 3 — Index & confirm

Run `python3 0_System/scripts/scan-skills.py` to register the new skill (enabled by default), then
tell the founder it's now discoverable via `find-skills` — which reads the skill folders on disk
directly — and how to invoke it.

---

## License rules (enforced)

- **Allowed to catalog/import:** MIT, Apache-2.0, and other clearly permissive licenses — this
  includes the bulk of `anthropics/skills`. For Apache-2.0, preserve the upstream `NOTICE`.
- **Office documents — don't import, they're native.** The `anthropics/skills` `pdf` / `docx` /
  `pptx` / `xlsx` folders are source-available reference only; their LICENSE bars keeping a copy
  outside Anthropic's Services, and the capability is already built into Claude (file creation is
  on for all users). Never vendor them — tell the founder to just ask Claude in-session to make
  the file.
- Anything without a clear permissive license: stop, surface the license, import only on an
  explicit founder override — and still record it in the manifest.

## Provenance — `skills-manifest.json`

One entry per imported skill (create the file on first import):

```json
{ "name": "...", "source_repo": "https://github.com/...", "source_subpath": "...",
  "resolved_commit_sha": "...", "spdx_license_id": "MIT", "license_file_path": "...",
  "copyright_notice": "...", "notice_file_path": null, "author": "...", "import_date": "YYYY-MM-DD",
  "local_path": ".agents/skills/<function>/<skill>" }
```

## Trusted sources

The vetted catalog lives in `reference/catalog.md` — `skills.sh` (Vercel `npx skills`),
`anthropics/skills` (Apache-2.0), `wondelai/skills`, `coreyhaines31/marketingskills`,
`shawnpang/startup-founder-skills`, `tjboudreaux/cc-skills-vc-fundraising`, `obra/superpowers`,
`mattpocock/skills`, `garrytan/gstack`, `nextlevelbuilder/ui-ux-pro-max-skill`, plus the
awesome-* indexes for open-ended discovery.

## Guardrails

- **Pointers, not source.** Never pre-bundle third-party skills; the founder pulls each one.
- **One at a time, on request.** Recommend freely; import only what the founder picks.
- **Always record provenance + license.** No silent imports.
- **Office docs are native, not imports.** Point founders to Claude's built-in file creation for
  PDF/Word/PPT/Excel rather than vendoring those skills.
- The founder owns what they pull — surface the license so they can comply if they redistribute.
