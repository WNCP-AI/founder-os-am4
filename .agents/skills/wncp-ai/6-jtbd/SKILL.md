---
name: am4-jtbd
description: >
  AM4 WNCP AI guided exercise that walks a founder through writing 3–5 clean,
  solution-agnostic job-to-be-done statements — one at a time, grounded in their
  own value prop, persona, and discovery data. Use when: "write my jobs to be done",
  "JTBD exercise", "what jobs am I solving for", "job statements", "jobs to be done".
  Make sure to use this skill whenever the user mentions jobs to be done, JTBD,
  or writing job statements — even if they don't explicitly say am4-jtbd.
---

# Jobs to Be Done Exercise

A guided exercise. You walk the founder through 3–5 job statements — one at a time,
one question per message. The goal: clean, solution-agnostic statements drawn from
their own data, before any prioritization.

> **Core rule:** A job describes what the customer is trying to accomplish — not what
> your product does. If your solution did not exist, the job statement would still be
> true. That is how you know it is clean.

This SKILL is the orchestrator. Load reference files at the steps indicated below.

## Phase 0 — Resolve and load inputs

Don't hardcode where context comes from. Call **`util_get_inputs`** (`get("jtbd")`) to
get this exercise's input map, then pull each source via the access method it returns.
For this task that is:

- **Value-Prop output** *(primary)* — `2_Outputs/.agents/A.3-Value-Prop/Value-Proposition.md`
- **User-Persona output** *(primary)* — `2_Outputs/.agents/A.3-User-Persona/User-Persona.md`
- **Company ground truth** *(primary)* — via `util_get_company_info` (`get()`)
- **Session template** *(primary)* — read `1_Product_Week/A.4-JTBD/`; build on whatever
  the founder has already filled in
- **Discovery evidence** *(optional)* — files in `5_Library/sources/processed/`; enrich
  but do not block if absent

From the loaded context, synthesize 2–3 partial job stubs before asking any questions:
- The persona's **Situation** seeds the "When…"
- The persona's **High-Value Need** seeds the "I want to…"
- The "so I can…" is intentionally left blank — the founder writes it
- If discovery data contains a distinct job signal beyond the persona, surface one more stub

Stubs are starting points, not finished statements.

**If both value-prop and persona outputs are missing**, don't stop — recover with the founder
(see `util_get_inputs` → *When a primary input is missing*):

> "I don't have your value prop or persona outputs from a previous session. Do you have your
> own notes on the customer you're building for — or would you rather answer a few quick
> questions so we can start writing jobs from what you know now?"

Use what they bring, or ask them to describe the first customer situation they want to write a
job for. Do not generate stubs. The per-job loop is identical.

**If company ground truth is missing:** don't stop — recover with the founder (see
`util_get_inputs` → *When a primary input is missing*): tell them plainly, ask whether they have
company background to share or would rather answer a couple of quick questions, then continue.

## Opening message

One paragraph. No bullet breakdowns. No phase previews.

Say: "Let's write your jobs to be done. Here's how this works: we'll write 3–5 job
statements together — one at a time. Each follows this format: **When [situation],
I want to [goal], so I can [outcome].** One rule: no product, no app, no feature in
the statement. If your solution did not exist, the statement should still be true."

If stubs were generated, add: "I've read your existing work and put together a few
starting points. Each one is partially complete — your job is to finish it."

Then use **AskUserQuestion** to present the stubs as selectable options (one per stub).
Question text: "Which job do you want to start with?" Header: "Job 1 of 3–5".
Option label = partial stub text. The tool provides an "Other" option automatically.

## Per-job loop

Load and follow **`reference/per-job-loop.md`** for the three steps in every job:
Step 1 — Complete and validate the statement; Step 2 — Three-layer tag;
Step 3 — AI-role tag.

Repeat for each job. Target 3–5 total.

**Between jobs:** after each validated job, display the locked confirmation as plain text:

> "Job [N] locked:  
> **[Job statement]**  
> Layer: [tag] | AI: [tag] — [rationale]"

If fewer than 3 done, add "On to Job [N+1] →" and continue the loop.

After job 3, use **AskUserQuestion** to ask:  
Question text: "Want to add a 4th job or stop here?"  
Header: "Shortlist ready"  
Options: "Stop here — 3 jobs is enough" · "Add a 4th job" · "Add a 4th and 5th job"

## Closing — hand the founder their conclusions

When the founder has 3–5 validated jobs, load **`reference/output-format.md`** and:

1. Show the JOBS TO BE DONE block (format §1) — the confirmed statements, tags, and
   rationale — so they can finalize their session template. Say: "Drop each statement
   into the matching section of your `A.4-JTBD` template. The layer and AI tags are
   there to carry into prioritization."
2. Ask: "Does this look good? Is there anything you want to change before I save this?"
   Use **AskUserQuestion**: "Looks good — save it" · "I want to edit something".
   If editing: one change at a time, re-show the block, ask again until confirmed.

### Quietly record the deliverable

Write the output silently to `2_Outputs/.agents/A.4-JTBD/JTBD.md` using the file
template in `reference/output-format.md` §2. Do not announce the path or ask the
founder to manage a file.

Then fold the top 1–2 jobs into company ground truth via `util_get_company_info`
(`set(03_Users, …)`) per `reference/output-format.md` §3 — a short summary under a
`## Jobs to Be Done` header so subsequent runs update in place. Full output stays in
`2_Outputs/.agents/A.4-JTBD/JTBD.md`, not in `0_Company/`.

## Guardrails

- Never write a job statement on behalf of the founder — create the conditions; they write the sentence.
- The founder's `1_Product_Week/A.4-JTBD/` template is human-owned — guide them to fill it; never fill it for them.
- The `2_Outputs/.agents/A.4-JTBD/JTBD.md` file is the chain's reference, written silently — surface conclusions, not the file.
- One question per message. Never bundle two questions.
- Do not push past 5 jobs — 3–5 is the target range.
- The AI-role question is mandatory for every job and cannot be skipped.
- Resolve inputs through `util_get_inputs`; read `0_Company/` only through `util_get_company_info`.
- If the founder conflates "job" with "feature": "A job statement describes what the customer wants to accomplish — not what your product does. Remove the solution."

## Quick reference

| Step | Core question | Done when |
|---|---|---|
| Phase 0 | Load value-prop, persona, company context | Inputs loaded; stubs generated (or recovered with founder) |
| Per job — Statement | When / I want to / so I can | Passes all 3 validation criteria |
| Per job — Layer | Functional, emotional, or social? | One tag committed |
| Per job — AI role | Feature, product core, not yet, or irrelevant? | One tag + one line of rationale |
| Closing | Confirm + save | File written; essence folded into `03_Users` |
