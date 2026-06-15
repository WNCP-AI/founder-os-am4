---
name: util_get_company_info
description: >
  The single read/write path for what the company is — ground truth every skill reads before
  it runs. Triggers when the founder says "update my company info", "what do you know about
  my company", "update the product description", "add our traction", "we pivoted — update
  the overview", "log this week's insight", or any correction to company facts. Also invoked
  by pipeline skills (5-user-persona, 6-jtbd, 8-draft-prd, 9-metrics, and others) to read
  company ground truth before running and to fold distilled essence back in after producing
  output. This compounding — each skill reading the latest ground truth, then writing its
  essence back — is what makes the pipeline chain without re-explaining context each session.
  All reads and writes go through this skill — no other skill touches 0_Company/ directly.
---

# util_get_company_info — Company Ground Truth

You are the sole gatekeeper for `0_Company/`. Every skill reads company ground truth through
you before it runs, and writes its distilled essence back through you after. Essence only —
full work products go to `2_Outputs/.agents/<session>/`, not here.

## Why this matters

Each pipeline skill reads `0_Company/` before it runs, so it starts with full context, not
just the last message. After producing output, each skill folds a short distilled essence
back in via `set()`. The next skill picks up richer ground truth than the one before it.
This compounding is what turns a chain of individual exercises into a coherent week of work.

## The folder contract

`0_Company/` holds company facts only — what the company is, for whom, and how it's doing.
Personal facts about the founder never go here; those belong in `0_User/` via
`util_get_user_info`.

```
0_Company/
├── 01_Overview.md      # one-liner, identity, stage
├── 02_Product.md       # what it is, what it does, the core mechanism
├── 03_Users.md         # who you serve, segments, early adopters
├── 04_Market.md        # market, competition, positioning
├── 05_Traction.md      # stage, metrics, OKRs
├── 06_Team.md          # founders, roles
├── 07_PW_Insights.md   # running takeaways across Product Week
└── Z_Library.md        # deeper detail; referenced by file name + section header
```

The folder starts empty. Bootstrap seeds it from the onboarding interview via `set()`.
Pipeline skills fold distilled essence back in via `set()` after each exercise.

## Seeded-by and pipeline essence map

| File | Seeded by | Pipeline essence folds in |
|---|---|---|
| `01_Overview.md` | bootstrap (A.1) | value-prop one-liner |
| `02_Product.md` | bootstrap | `8-draft-prd` (short product summary) |
| `03_Users.md` | bootstrap | `5-user-persona`, `6-jtbd` (segment + top JTBD) |
| `04_Market.md` | bootstrap | — |
| `05_Traction.md` | bootstrap | `9-metrics` (OKR snapshot) |
| `06_Team.md` | bootstrap | — |
| `07_PW_Insights.md` | — | running takeaways from any pipeline skill |
| `Z_Library.md` | — | deep detail routed from any topic file |

## Interface

These are the only two entry points. No skill reads or writes `0_Company/` any other way.

### get()

Read and return the whole folder in one pass — read each file (`01_Overview.md` through
`07_PW_Insights.md` and `Z_Library.md`) and return their combined contents. If a file
doesn't exist yet, skip it silently.

### get(file)

Read and return the named topic file (e.g. `get(03_Users)`). If the file doesn't exist
yet, return empty and note it hasn't been created.

### set(file, essence)

Write distilled essence into a specific topic file or section. **Never write full work
products here.** Full outputs — `Value-Proposition.md`, `PRD-v1.md`, `Metrics-OKR.md`,
persona documents — live in `2_Outputs/.agents/<session>/` with Title-Case filenames.
Write only the short distilled version here.

1. If the file doesn't exist, create it with `essence` as the full body.
2. If the file already exists, read it first. Locate the section matching `essence`'s
   top-level `##` or `###` header. Replace that section in place, leaving all other
   sections intact. If no matching section header exists, append as a new section.
3. If the incoming content is long (more than ~40 lines) or too detailed for a concise
   topic file, route the detail into `Z_Library.md` under a `##` section header named for
   the topic (e.g. `## Value-Proposition Detail`). Write only a short summary in the primary
   topic file with a note: `→ see Z_Library.md § <section>`.
4. After writing, read the file back and confirm the result looks correct before returning.

## Step-by-step: reading company ground truth

When a pipeline skill or the founder asks what you know about the company:

1. Read each topic file that exists in `0_Company/`.
2. Return the contents cleanly, grouped by file heading. Do not editorialize.
3. If a topic file is missing or empty, note the gap so the calling skill knows which
   context is absent.

## Step-by-step: folding essence back in

When a pipeline skill has produced output and wants to update the ground truth:

1. Identify which topic file(s) the essence belongs to (use the seeded-by/folds-in table).
2. Distill the output to its core facts — one to three short paragraphs. Full documents
   stay in `2_Outputs/.agents/<session>/`.
3. Call `set(file, essence)` as described above.
4. Read the file back immediately. Confirm the update in one short sentence before returning.

## Topic guide

| File | What goes here |
|---|---|
| `01_Overview.md` | Company name, one-liner, value-prop summary, current stage |
| `02_Product.md` | What it is, core mechanism, state today (idea / prototype / live / revenue) |
| `03_Users.md` | Target segments, early adopters, top jobs-to-be-done (short) |
| `04_Market.md` | Market definition, key competitors, positioning statement |
| `05_Traction.md` | Stage, key metrics, OKR snapshot |
| `06_Team.md` | Founders, roles, key hires |
| `07_PW_Insights.md` | Running weekly takeaways — one bullet per insight, dated |
| `Z_Library.md` | Extended company background, deep market detail, anything too long for a topic file |

## Guardrails

- Company facts only — never write personal facts about the founder into `0_Company/`.
  Those belong in `0_User/` via `util_get_user_info`.
- Never write full work products here. Full outputs go to `2_Outputs/.agents/<session>/`
  with Title-Case filenames. Write only distilled essence.
- Keep each topic file short and skimmable. Push length into `Z_Library.md`.
- Always read the file back after writing and confirm before returning.
- Never send the founder's data to external services — all reads and writes are local,
  in this conversation.
