---
name: founder-bootstrap
description: >
  Onboards a founder into Founder OS — detects OS, creates CLAUDE.md, checks prerequisites,
  optionally ingests any data already in 5_Library/sources/raw/ so the interview is grounded,
  builds the 0_User/ profile and 0_Company/ ground-truth topic files via a short interview, and
  confirms the workspace is ready. Triggers when the user says "get me started", "set me up",
  "I'm new here", or otherwise signals first-time setup. Session A.1 of the Access Mode Product
  Week. Founders bring their own agent — no model key required.
---

# founder-bootstrap — Founder Onboarding

You are setting up a founder's machine to run their own product workspace.
Be a calm, step-by-step guide. Do one step, confirm it worked, then move on.
Assume nothing about technical background — explain what each step does in one plain
sentence before running it.

---

## Step 0 — Link CLAUDE.md + detect OS

Detect the OS (`uname -s` → Darwin/Linux; `$env:OS` → Windows_NT), state it, and confirm. Then
ensure `CLAUDE.md` exists at the repo root — if not, run:

```bash
node 0_System/bootstrap/setup.mjs
```

It detects OS, creates `CLAUDE.md` → `AGENTS.md` (symlink on Mac/Linux, generated copy on Windows),
and confirms the workspace. If Node is unavailable or you're on Windows, see the manual symlink
commands and OS-detection detail in [reference/os-setup.md](reference/os-setup.md).

---

## Step 1 — Confirm agent tool

Confirm the founder is on **Claude Code** (CLI, desktop, or VS Code) — the Day-1 path. Other
AGENTS.md-aware tools (Codex, etc.) work since the repo is plain markdown, but live support is
Claude Code-first; offer it as the fallback rather than debugging an exotic harness. **No model
key required** — founders bring their own agent and model access.

---

## Step 2 — Check prerequisites

Confirm **git** (`git --version`) and **Node 18+** (`node --version`). If either is missing, give
the install command for their OS — see [reference/prerequisites.md](reference/prerequisites.md).
Node is only needed for `setup.mjs`; if it's missing, don't block — continue and note it.

---

## Step 3 — Data first (optional, but it makes the interview better)

The interview (Steps 4–5) is much sharper if you've already read the founder's own data, so
offer ingestion **now** — before the questions — rather than only at the end.

Explain the convention in two sentences: *"Everything you know about your customers goes in
`5_Library/sources/raw/` — any format, organized into subfolders if you like. I can standardize
it into `5_Library/sources/processed/` and use it to ask sharper questions while we build your
profile."* Then **make the determination** yourself:

1. Check `5_Library/sources/raw/`. If it has files, run the dry-run plan to see what's there and
   what the machine can convert (writes nothing):

   ```bash
   python3 0_System/scripts/parse-sources.py --plan
   ```

2. **Decide and offer:**
   - **Files present and worth it** (interviews, research, notes, analytics) → offer to ingest
     now: *"Want me to process these first so the interview uses them?"* If yes, hand to
     `ingest-sources`. If the plan shows files that need a converter the machine doesn't have,
     point them at `ingest-init` for the one-line install recommendation — **never install it
     yourself** — and let them choose: install then ingest, ingest with what's available, or
     defer.
   - **`raw/` is empty** → invite them to drop files now if they have any on this machine; if
     not, that's fine — continue and they can ingest later.
   - **Founder declines** → fine; continue. Ingestion is never required to proceed.

3. Whatever they choose is non-blocking — bootstrap continues either way. If they ingested,
   read the resulting `5_Library/sources/processed/` tree before the interview so you can ask
   informed follow-ups and pre-fill ground truth in Step 5.

Founders can also run `ingest-init` / `ingest-sources` manually any time — this step just makes
the offer at the moment it helps most.

## Step 4 — Founder profile (the interview)

Tell the founder: *"I'm going to ask a few questions to build a profile so every future
session adapts to you."* Then ask, conversationally, one at a time (if you ingested data in
Step 3, lead with what you learned and ask the founder to confirm or correct it):

1. Name, and your role in the company.
2. The company in one sentence — what it does, for whom.
3. Where the product is today (idea / prototype / live / revenue) and what exists already.
4. Your background — product, design, engineering, business? How comfortable are you with
   AI tools day-to-day?
5. How you like to work with an assistant: short and direct, or explained step by step?
   Recommendations first, or options first?

Write the answers into `0_User/` by calling the **`util_get_user_info`** skill — use its
`set(file, content)` interface to create each numbered topic file (`01_Overview`,
`02_Expertise`, `03_Preferences`, `04_Goals`; deep background to `Z_Library`). That skill
owns the numbered topic-file layout described in `0_User/README.md`; bootstrap supplies the
answers, the util skill decides where they land. Read the result back in one short paragraph
and let the founder correct it.

---

## Step 5 — Company ground truth

From the same interview and anything you ingested in Step 3 (ask follow-ups only where thin),
build the `0_Company/` topic files
by calling the **`util_get_company_info`** skill — use its `set(file, essence)` interface
for each topic. The numbered topic-file layout is described in `0_Company/README.md`; that
skill owns where each piece of essence lands. Seed at minimum:

- `01_Overview` — what the company does, for whom; stage
- `02_Product` — what exists today, in what form
- `03_Users` — who they sell to, who they've talked to
- `04_Market` — market, competition, positioning (what they shared)
- `06_Team` — founders and roles

These topic files — not chat memory — are what every later skill reads for company context.
The founder can extend them any time. Each pipeline exercise distills its output back into the
relevant topic file via `util_get_company_info`, so the ground truth stays current as the week
progresses.

---

## Step 6 — Verify and recap

Final checklist — confirm each:

- [ ] `CLAUDE.md` exists at the repo root (symlink to `AGENTS.md`, or generated copy on Windows)
- [ ] `0_User/` topic files exist (`01_Overview` … via `util_get_user_info`) and the founder approved them
- [ ] `0_Company/` topic files exist (via `util_get_company_info`) and the founder approved them
- [ ] `.agents/skills/skills.json` lists the pipeline skills
- [ ] `5_Library/sources/raw/` and `5_Library/sources/processed/` exist
- [ ] Data ingested (Step 3) — or the founder knows to run `ingest-sources` when ready

Recap which steps completed vs. pending. Then set the picture for the week — adapt the opener
to whether they ingested in Step 3:

- **If they ingested:** *"Your data's already standardized in `5_Library/sources/processed/`."*
- **If not:** *"When you're ready, run `ingest-sources` (A.2) to standardize your data — or
  `ingest-init` first if you want a converter recommendation."*

Then: *"From here the chain runs: value proposition → persona → jobs-to-be-done → PRD → OKRs —
each skill reads the last one's output from `2_Outputs/` and company ground truth from
`0_Company/`. By Thursday you'll have a PRD, a prototype, and OKRs — built on your own data."*
