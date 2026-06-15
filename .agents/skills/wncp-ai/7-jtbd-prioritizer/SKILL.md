---
name: am4-jtbd-prioritizer
description: >
  AM4 WNCP AI conversational exercise for ranking job-to-be-done statements and making
  explicit keep-or-kill decisions. Reads the JTBD output automatically and ranks jobs across
  five dimensions — pain intensity, existing alternatives, strategic fit, founder edge, evidence
  quality. Use when: "prioritize my jobs", "which job to build for first", "rank my JTBD",
  "pick a job". Make sure to use this skill whenever the user mentions prioritizing jobs,
  keep or kill, or ranking job statements — even if they don't explicitly say am4-jtbd-prioritizer.
---

# JTBD Prioritizer

A guided exercise for founders who have 2–5 job statements and need to decide which one
to build for first. The ranking is earned through conversation — not gut feel, not a spreadsheet
score. Every ranked position gets a rationale. Every non-top job gets an explicit keep-or-kill
decision with a stated reason.

> **Core rule:** Base answers on what you actually know — evidence from customer conversations,
> concrete examples, things you can point to. If an answer is based on assumption, this exercise
> flags it before it drives a decision.

This SKILL is the orchestrator — it loads reference files at each step rather than carrying
every table inline.

## Phase 0 — Resolve and load inputs

Don't hardcode where context comes from. Call **`util_get_inputs`** (`get("jtbd-prioritizer")`)
to get this exercise's input map, then pull each source via the access method it returns.
For this task that is:

- **`A.4-JTBD` output** *(primary)* — the job statements produced by skill 6, at
  `2_Outputs/.agents/A.4-JTBD/JTBD.md`. Extract all job statements with their primary layer
  tag and AI-role tag. These are the jobs being prioritized — do not ask the founder to re-enter
  them.
- **Company ground truth** *(primary)* — via `util_get_company_info` (`get()`). Useful for
  evaluating strategic fit and evidence quality in later dimensions.

**If the `A.4-JTBD` output is missing**, don't stop — recover with the founder (see
`util_get_inputs` → *When a primary input is missing*):

> "I don't have your jobs-to-be-done list from a previous session. Do you have your job statements
> to paste here — 'When [situation], I want to [goal], so I can [outcome],' one per line — or would
> you rather we write them together now, quickly?"

If they paste jobs, use them. If not, pull the job-writing questions from the JTBD skill and walk
them through it inline, then prioritize as normal.

## Opening message

Once jobs are loaded, display them clearly:

> "Let's prioritize your jobs. Here's what we're working with:
>
> **Job 1:** [statement]
> **Job 2:** [statement]
> [continue for all jobs]
>
> We'll go through five questions — one at a time — comparing your jobs against each other.
> At the end, you'll have a ranked list with a rationale for each position, and an explicit
> decision on which jobs to keep and which to kill.
>
> One rule: base your answers on what you actually know — not what you expect or hope."

Then immediately move to Dimension 1. Do not add a "Ready?" prompt.

## The five dimensions

Ask one question per dimension. Each question invites a comparative answer across all jobs —
not a per-job score. Do not move to the next dimension until you have a clear answer, or
have flagged an assumption and the founder has acknowledged it.

**Load and follow `reference/dimensions.md`** for the exact question text, AskUserQuestion
calls, follow-up probes, and answer-type response table for each dimension.

## Synthesis

Once all five dimensions are covered, **load and follow `reference/synthesis.md`** to:

1. Reflect the pattern back — which job led each dimension, grounded in what was said.
2. Propose the ranked list with 2–3 sentence rationale and a "Watch out for" flag per job.
3. Ask: "Does this ranking reflect what you know, or does something feel off?"

If the founder pushes back, probe why before adjusting. Do not reorder without reasoning.

## Kill-or-keep

After the ranking is confirmed, **load and follow `reference/kill-or-keep.md`** to work
through every job that is not in the top position. Each non-top job needs an explicit
keep or kill with a stated reason.

## Closing — hand the founder their conclusions

Once all kill-or-keep decisions are made, show the founder the full ranked block and
next step (see `reference/synthesis.md` for the exact display format).

Then say: "Drop each decision into the matching row of your `A.4-JTBD` template. The
reasoning next to each is so you remember why it landed where it did."

### Quietly record the deliverable

Write the prioritized output silently to `2_Outputs/.agents/A.4-JTBD/JTBD-Prioritized.md`
using the file format in `reference/output-format.md`. Do not announce the path — surface
the conclusions, not the file.

This skill has no essence fold — do not call `util_get_company_info` `set()`.

## Guardrails

- Never accept a ranking based on what the founder wants to build rather than what the customer needs.
- Never accept vague evidence ("I think", "I feel like", "probably") without flagging it as assumption.
- Never skip kill-or-keep — every non-top job needs an explicit decision with a stated reason.
- Never ask more than one question at a time.
- Never reorder the ranking without probing why the founder thinks it is wrong.
- Resolve inputs through `util_get_inputs`; read `0_Company/` only through `util_get_company_info`.
- The founder records their final decisions in their `1_Product_Week/A.4-JTBD/` template by hand.
  The agent guides; it never fills the template for them.

## Quick reference

| Step | Core question | Done when |
|---|---|---|
| Phase 0 | Load JTBD output | Jobs displayed, company context read |
| Dimension 1 — Pain intensity | Which job has the customer hurting most right now? | Named job + evidence cited |
| Dimension 2 — Existing alternatives | Which job has the most broken workaround? | Named job + workaround described |
| Dimension 3 — Strategic fit | Which job unlocks the most if solved first? | Named job + reasoning stated |
| Dimension 4 — Founder edge | Which job plays to your asymmetric advantage? | Named job + specific edge named |
| Dimension 5 — Evidence quality | Which job has the most evidence behind it? | Named job + evidence cited |
| Synthesis | Does the ranking reflect what you know? | Ranking confirmed |
| Kill-or-keep | Keep or kill every non-top job | All decisions made with stated reason |
| Closing | Conclusions shown; file written silently | Founder satisfied with ranking |
