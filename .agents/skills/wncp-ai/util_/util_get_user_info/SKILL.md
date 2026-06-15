---
name: util_get_user_info
description: >
  The single read/write path for who runs this workspace — personal context only, never
  company data. Triggers when the founder says "update my profile", "change my working
  preferences", "what do you know about me", "update my background", "I prefer short answers",
  "add to my goals", or any correction to their name, role, expertise, or working style.
  Also invoked by founder-bootstrap (to seed 0_User/ from the onboarding interview) and by
  pipeline skills that need to read the founder's personal context before adapting their output.
  All reads and writes go through this skill — no other skill touches 0_User/ directly.
---

# util_get_user_info — Founder Personal Profile

You are the sole gatekeeper for `0_User/`. Every skill that needs to know who the founder
is, how they work, or what they want reads through you. Bootstrap seeds the files; the
founder can update any topic at any time.

## The folder contract

`0_User/` holds personal context only — who the founder is and how they work. Company facts
never go here; those belong in `0_Company/` via `util_get_company_info`.

```
0_User/
├── 01_Overview.md      # name, role, identity
├── 02_Expertise.md     # background, domain expertise, strengths, gaps
├── 03_Preferences.md   # working style: tone, depth, pace, decisions, tools
├── 04_Goals.md         # what they want during & after the program
└── Z_Library.md        # fuller background; referenced by file name + section header
```

The folder starts empty. Bootstrap seeds it via `set()` during the onboarding interview.

## Interface

These are the only two entry points. No skill reads or writes `0_User/` any other way.

### get()

Read and return the whole folder in one pass — read each file (`01_Overview.md`,
`02_Expertise.md`, `03_Preferences.md`, `04_Goals.md`, `Z_Library.md`) and return their
combined contents. If a file doesn't exist yet, skip it silently.

### get(file)

Read and return the named topic file (e.g. `get(03_Preferences)`). If the file doesn't
exist yet, return empty and note it hasn't been created.

### set(file, content)

Write a specific topic file or section.

1. If the file doesn't exist, create it with `content` as the full body.
2. If the file already exists, read it first. Locate the section matching `content`'s
   top-level `##` or `###` header. Replace that section in place, leaving all other
   sections intact. If no matching section header exists, append as a new section.
3. If the incoming content is long (more than ~40 lines) or represents deeper background
   that doesn't belong in a concise topic file, route the detail into `Z_Library.md`
   under a `##` section header named for the topic (e.g. `## Extended Background`).
   Write only a short summary in the primary topic file with a note: `→ see Z_Library.md
   § <section>`.
4. After writing, read the file back and confirm the result looks correct before returning.

## Step-by-step: reading the profile

When another skill or the founder asks what you know about the founder:

1. Read each topic file that exists in `0_User/`.
2. Return the contents cleanly, grouped by file heading. Do not editorialize.
3. If a topic file is missing or empty, note the gap so the caller can decide whether to
   prompt the founder for that information.

## Step-by-step: updating the profile

When the founder corrects or adds information, or bootstrap is writing interview answers:

1. Identify which topic file the content belongs to (see the folder contract above).
2. If the content spans multiple topics, split it — write each piece to the correct file.
3. Call `set(file, content)` as described above.
4. Read the file back immediately. Confirm the result to the founder in one short sentence.
5. Never overwrite sections the founder hasn't asked to change.

## Topic guide

| File | What goes here |
|---|---|
| `01_Overview.md` | Name, current role, company name, one-sentence identity |
| `02_Expertise.md` | Professional background, domain depth, self-assessed strengths and gaps |
| `03_Preferences.md` | Tone (direct / explained), depth, pacing, decision style, tools they use daily |
| `04_Goals.md` | What they want to achieve during Product Week; longer-term career or company goals |
| `Z_Library.md` | Extended background, career history, anything too long for a topic file |

## Guardrails

- Personal context only — never write company facts, product details, or market data into
  `0_User/`. Those belong in `0_Company/` via `util_get_company_info`.
- Never overwrite sections the founder hasn't asked to change.
- Keep each topic file short and skimmable. Push length into `Z_Library.md`.
- Always read the file back after writing and confirm before returning.
- Never send the founder's data to external services — all reads and writes are local,
  in this conversation.
