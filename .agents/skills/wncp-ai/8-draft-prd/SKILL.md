---
name: am4-prd
description: >
  AM4 WNCP AI guided PRD exercise — creates PRD v1 (session A.5, Day 1) or extends to PRD v2
  (session C.3, Day 3). Use when: "write my PRD", "fill in my PRD", "draft the PRD", "create PRD
  v2", "Day-3 PRD", "extend my PRD", or "write/extend PRD v2". Make sure to use this skill
  whenever the user mentions PRD, product requirements, or product spec — even if they don't
  explicitly say am4-prd.
---

# Draft PRD Exercise

A guided exercise. You walk the founder through their PRD one section at a time — pre-filling
from their existing outputs so they're never re-explaining themselves, confirming or correcting,
and adding only what's genuinely new. Two modes: PRD v1 (Day 1, §§ 1–5) and PRD v2 (Day 3,
all 9 sections). The founder fills in their working template by hand; you create the conditions
and guide each decision.

This SKILL is the orchestrator — it routes to a reference file for the detailed per-mode logic.

## Phase 0 — Resolve and load inputs

Call **`util_get_inputs`** (`get("draft-prd")`) to get this exercise's input map, then pull
each source via the access method it returns. For this task:

**Always primary (both modes):**
- **A.3-Value-Prop output** *(primary)* — read `2_Outputs/.agents/A.3-Value-Prop/Value-Proposition.md`
- **A.3-User-Persona output** *(primary)* — read `2_Outputs/.agents/A.3-User-Persona/User-Persona.md`
- **A.4-JTBD-Prioritized output** *(primary)* — read `2_Outputs/.agents/A.4-JTBD/JTBD-Prioritized.md`
- **Company ground truth** *(primary)* — via `util_get_company_info`

**v1 mode additionally:**
- **Session template** *(primary)* — read `1_Product_Week/A.5-PRD-v1/`

**v2 mode additionally:**
- **Session template** *(primary)* — read `1_Product_Week/C.3-PRD-v2/`
- **A.5-PRD-v1 output** *(primary)* — read `2_Outputs/.agents/A.5-PRD-v1/PRD-v1.md`
- **C.2-Metrics-OKR output** *(optional)* — read `2_Outputs/.agents/C.2-Metrics-OKR/Metrics-OKR.md`

Never read `0_Company/` directly. Never read `0_User/` directly. Always go through the utilities.
Never use bare `5_Library/sources/processed` as an input source for this skill — these primary
upstream outputs are the wired inputs per the input map.

**If a primary input is missing,** don't stop — recover with the founder (see `util_get_inputs` →
*When a primary input is missing*). Tell them which upstream piece isn't on file, ask whether they
have their own material for it or want to answer a few quick questions, and pull the relevant
questions from the upstream skill (value prop, persona, or JTBD) to fill just that gap. Then
continue — a thinner input makes a lighter PRD, not a blocked one.

Once inputs are loaded, say one sentence: "I can see your [value prop / persona / job list] — I'll
pre-fill from those so you're not re-explaining yourself." Then move to mode routing.

## Mode routing

Before reading any further files, use **AskUserQuestion** with two options:

- **PRD v1 — Day 1** — description: "Company, target user, jobs, features, and prototype (§§ 1–5)"
- **PRD v2 — Day 3** — description: "Adds market context, assumptions, OKRs, and roadmap (all 9 §§)"

Then follow the matching path:

- **PRD v1 selected → v1 mode.** Load and follow **`reference/mode-v1.md`**.
- **PRD v2 selected → v2 mode.** First check: is `2_Outputs/.agents/A.5-PRD-v1/PRD-v1.md` present?
  If present, load and follow **`reference/mode-v2.md`**.
  If not, don't stop — tell the founder "I don't have your PRD v1 on file, and v2 builds on it,"
  then ask whether they have a v1 (or an equivalent product spec) to use, or want to answer the
  PRD v1 questions quickly first. Capture enough of the v1 foundation that way, then continue into
  v2 (see `util_get_inputs` → *When a primary input is missing*).

Both modes end at the Closing below.

## Closing — hand the founder their conclusions

### v1 mode

When all five sections are confirmed, **load `reference/output-format.md`** and:

1. Show the founder a clean summary of the five sections (format §1-v1) so they can finalize their
   `A.5-PRD-v1` template. Say: "Drop each section into the matching part of your `A.5-PRD-v1`
   template. The reasoning next to each is so you remember why it's there."
2. Say:
   > "PRD v1 complete. Sections 1–5 of your PRD are done. You'll add the remaining sections on
   > Day 3 after the Metrics Workshop.
   >
   > **To build the prototype:** open a new Claude session. Paste your Prototype section and say:
   > 'Build a working prototype. Follow the user flow exactly. Hardcoded placeholder data only.
   > No auth, no backend. Build in plain HTML, CSS, and JavaScript.'"

#### Quietly record the v1 deliverable

Write the derived deliverable **silently** to `2_Outputs/.agents/A.5-PRD-v1/PRD-v1.md` using
the file template in `reference/output-format.md` §2-v1. Do not announce the path or ask the
founder to manage a file.

Then fold a short product summary into company ground truth via `util_get_company_info`
(`set(02_Product, …)`) per `reference/output-format.md` §3, under a `## PRD v1 Summary` header
so subsequent runs update that section in place. Full PRD stays in `2_Outputs/.agents/A.5-PRD-v1/`,
not in `0_Company/`.

### v2 mode

When all nine sections are confirmed, **load `reference/output-format.md`** and:

1. Show the founder a clean summary of all nine sections (format §1-v2) so they can finalize their
   `C.3-PRD-v2` template. Say: "Drop each section into the matching part of your `C.3-PRD-v2`
   template."
2. Say:
   > "PRD v2 complete. Your riskiest assumption is [the row with lowest confidence in your
   > Assumptions & Risks] — that's the thing to test first."

#### Quietly record the v2 deliverable

Write the derived deliverable **silently** to `2_Outputs/.agents/C.3-PRD-v2/PRD-v2.md` using
the file template in `reference/output-format.md` §2-v2. v1 is **kept, never overwritten**.

Then fold a distilled product summary into company ground truth via `util_get_company_info`
(`set(02_Product, …)`) per `reference/output-format.md` §3, under a `## PRD v2 Summary` header.

## Guardrails (both modes)

- One section per message — never show two sections at once.
- One question per message — never bundle two questions.
- Push back on weak answers once before accepting. A weak answer sounds plausible but doesn't
  hold up under one follow-up question. One pushback per field, then accept.
- Never re-run value prop, persona, or JTBD exercises — read the outputs, confirm, move on.
- Carry AI role tags forward as-is from the JTBD-Prioritized output — don't re-coach them.
- Never expose file sources, derivation logic, or agent mechanics to the founder. Founders see
  outputs, not process.
- Always use section names, not numbers or symbols — "Features" not "Section 4".
- The founder's template in `1_Product_Week/A.5-PRD-v1/` or `1_Product_Week/C.3-PRD-v2/` is
  human-owned — guide them to fill it; never fill it for them.
- The output files (`2_Outputs/.agents/A.5-PRD-v1/PRD-v1.md` and
  `2_Outputs/.agents/C.3-PRD-v2/PRD-v2.md`) are the chain's reference — written silently,
  never announced.
- Resolve inputs through `util_get_inputs`; read `0_Company/`/`0_User/` only through their utilities.
- v2 mode: never invent OKRs — use the `C.2-Metrics-OKR` output if present; if it isn't, ask the
  founder for their metrics/OKRs (or run the questions) rather than guessing.

## Quick reference

| Mode | Sections | Session template | Output file |
|---|---|---|---|
| v1 | Company + VP · Target User · JTBD · Features · Prototype | `1_Product_Week/A.5-PRD-v1/` | `2_Outputs/.agents/A.5-PRD-v1/PRD-v1.md` |
| v2 | All above + Market Dynamics · Assumptions & Risks · OKRs · Roadmap | `1_Product_Week/C.3-PRD-v2/` | `2_Outputs/.agents/C.3-PRD-v2/PRD-v2.md` |
