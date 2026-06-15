---
name: am4-user-persona
description: >
  AM4 WNCP AI guided exercise for defining a single Ideal Customer Profile — one person, one
  situation, one high-value need. Use when: "define my user persona", "who is my customer",
  "ICP exercise", "who am I building for", "user persona exercise". Make sure to use this skill
  whenever the user mentions user persona, ICP, ideal customer, or persona exercise — even if
  they don't explicitly say am4-user-persona. Do NOT use for: JTBD exercise, value proposition,
  PRD writing.
---

# User Persona Exercise

A guided exercise. One person at the end.
The goal: name the specific person you are building for, the moment their problem hits them,
and the one thing they need done — before bringing your product in.

> **Core rule:** The persona describes a real person in a real situation with a real need —
> not a market segment, not a buyer profile card, not a demographic description.
> Your product stays out until the output is saved.

This SKILL is the orchestrator — it loads a reference file at each path rather than carrying
every table inline.

## Phase 0 — Resolve and load inputs

Don't hardcode where context comes from. Call **`util_get_inputs`** (`get("user-persona")`)
to get this exercise's input map, then pull each source via the access method it returns.
For this task that is:

- **`A.3-Value-Prop` output** *(primary)* — read `2_Outputs/.agents/A.3-Value-Prop/Value-Proposition.md`.
  This carries the In Scope person from the value prop; the persona narrows from there.
- **Discovery evidence** *(primary)* — the standardized customer data in `5_Library/sources/processed/`.
  Read every file — not just interview files. Each may contain signals.
- **Company ground truth** *(primary)* — via `util_get_company_info` (`get()`).
- **The founder's session template** *(primary)* — read `1_Product_Week/A.3-User-Persona/`;
  build on whatever they've already filled in rather than starting cold.
- **Founder profile** *(optional)* — via `util_get_user_info`, to match their working style.

Hold in context: the In Scope person from the value-prop output, who showed the most acute
pain in the discovery interviews, key quotes, and any workarounds named. These anchor every
question below.

**If the `A.3-Value-Prop` output or discovery evidence is missing**, don't stop — recover with the
founder (see `util_get_inputs` → *When a primary input is missing*):

> "I don't have your value proposition from a previous session. Do you already have one — or notes
> on who your In Scope customer is — that you'd like to use? Or we can answer a couple of quick
> questions to pin down the customer this persona narrows from."

Use what they bring, or pull the In-Scope-customer questions from the value-prop skill and guide
them through just those, then continue.

## Opening message

One paragraph. No bullet breakdowns.

Say: "Your discovery data is loaded. Before we start —" then use the **AskUserQuestion** tool
to present two options:

- "I already have a user persona" — description: "We'll pressure-test it against three criteria"
- "Not yet" — description: "We'll build one through three questions, one at a time"

## Path routing

- **They have a persona → Path A (Pressure Test).** Ask: "Share your persona — as much or
  as little as you have." Then **load and follow `reference/path-a-pressure-test.md`**.
- **They don't → Path B (Build).** Say: "We'll work through three questions. Your product
  stays out until the end. Let's start." Then **load and follow `reference/path-b-build.md`**.

Both paths end at Closing below.

## Closing — hand the founder their conclusions

When the persona passes all three validation criteria, **load `reference/output-format.md`** and:

1. Collect Current Behavior and Key Quote per `reference/output-format.md` §1 (probe the
   founder or surface from discovery data if not already gathered).
2. Show the founder their completed persona block (format §2) — the **information and
   conclusions** so they can finalize their template. Say: "Drop each line into the matching
   section of your `A.3-User-Persona` template. The reasoning next to each is so you remember
   why it's there."
3. Use the **AskUserQuestion** tool: "Anything you want to edit before I save this?" with
   options "Looks good — save it" / "I want to edit something". If they want to edit,
   adjust one thing at a time, re-show the block, and ask again until confirmed.

### Quietly record the deliverable

For the skill chain's reference (not something the founder edits), write the derived
deliverable to `2_Outputs/.agents/A.3-User-Persona/User-Persona.md` using the file
template in `reference/output-format.md` §3. Do this **silently** — don't announce the
path or make the founder manage a file.

Then fold distilled persona essence into company ground truth via `util_get_company_info`
(`set(03_Users, …)`) per `reference/output-format.md` §4 — under a `## User Persona`
header so it updates in place. The full block stays in the output file, not in `0_Company/`.

Say: "Saved. The JTBD skill will read from that file automatically — you don't need to copy
anything. Ready for the JTBD exercise?"

## Guardrails

- Never write the identity, situation, or need fields on behalf of the founder — not even a draft.
- The founder's template in `1_Product_Week/A.3-User-Persona/` is theirs and human-owned — guide them to fill it; never fill it for them.
- The `2_Outputs/.agents/A.3-User-Persona/User-Persona.md` file is the chain's reference, written quietly — surface the conclusions to the founder, not the file.
- Move forward with two person types still in play: always hard-stop and force a choice first.
- Never accept a product feature or tool as the "need"; never accept a full job-format statement ("When I… I want to… so I can…") — that belongs to the JTBD exercise.
- Ask only one question per message.
- If the founder asks "can I have two personas?": "Not for this exercise. Which one is more urgent for what you are building right now? Start there — you can define a second after the JTBD exercise."
- If the founder conflates persona with JTBD: "A persona describes who this person is and what moment they are in. JTBD describes what they are trying to get done. We are in the persona — we will write the job statement in the next exercise."
- If the founder conflates persona with a buyer profile card (demographics, age, income): "We are not building a marketing persona here — no demographics, no psychographics. We need one real person, one moment, one need."
- Resolve inputs through `util_get_inputs`; read `0_Company/`/`0_User/` only through their utilities.

## Quick reference

| Step | Core question | Done when |
|------|--------------|-----------|
| Opening fork | Do you have a persona? | Path selected |
| **Path A** — Pressure test | Does it pass all 3 criteria? | All pass or founder revises until they do |
| **Path B** — The Person | Who is the one person this is for? | One role + context, no segment, no multiples |
| **Path B** — The Situation | What moment does the problem surface? | Specific task or decision point — not a general state |
| **Path B** — The Need | What do they most need done in that moment? | One thing, solution-agnostic, no product |
| Synthesis | Why this ICP over others? | Evidence or reasoned commitment stated |
| Validation | Does it pass all 3 criteria? | Single person, specific moment, solution-agnostic need |
| Output | Save to `2_Outputs/.agents/A.3-User-Persona/User-Persona.md` | File written silently, founder given conclusions |
