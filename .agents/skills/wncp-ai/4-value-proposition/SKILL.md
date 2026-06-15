---
name: am4-value-proposition
description: >
  AM4 WNCP AI guided exercise that walks a founder through completing their Value Proposition
  template by hand — building or pressure-testing the value prop one section at a time, grounded
  in their own data. Use when: "write my value prop", "what is my value proposition", "sharpen my
  value prop", "value proposition exercise". Make sure to use this skill whenever the user mentions
  value proposition, why my product exists, or positioning statement — even if they don't
  explicitly say am4-value-proposition.
---

# Value Proposition Exercise

A guided exercise. You walk the founder through their value proposition **one section at a time**,
helping them reach each answer from their own evidence — they write the answers into their
template by hand. Two modes: build from scratch, or pressure-test what they have.

This is a thinking exercise the founder owns. You create the conditions and ask the questions;
**they** write the sentence. Their working template lives in `1_Product_Week/A.3-Value-Prop/` and
they fill it in themselves.

This SKILL is the orchestrator — it loads a reference file at each step rather than carrying every
table inline.

## Phase 0 — Resolve and load inputs

Don't hardcode where context comes from. Call **`util_get_inputs`** (`get("value-proposition")`)
to get this exercise's input map, then pull each source via the access method it returns. For this
task that is:

- **Discovery evidence** *(primary)* — the standardized customer data in `5_Library/sources/processed/`.
- **Company ground truth** *(primary)* — via `util_get_company_info`.
- **The founder's session template** *(primary)* — read `1_Product_Week/A.3-Value-Prop/`; build
  on whatever they've already filled in rather than starting cold.
- **Founder profile** *(optional)* — via `util_get_user_info`, to match their working style.
- **Configured sources** *(optional)* — anything else the input map lists.

Value-prop building blocks may already be present across these — a problem named in their company
overview, a customer quote in the evidence, a half-written line in their template. Gather broadly
and hold the strongest signals: the sharpest problem, who feels it most acutely, the workaround
and its cost, and any alternative they'd revert to.

**If discovery data is missing or thin**, don't stop — recover with the founder (see
`util_get_inputs` → *When a primary input is missing*):

> "I don't have customer discovery data on file yet. Do you have your own notes or research from
> talking to customers that you'd like to use — or would you rather answer a few quick questions
> so we can build the value proposition from what you know right now?"

Use whatever they bring, or guide them through the discovery questions inline, then continue —
flagging that the value prop is running on lighter evidence than usual.

## Opening message

One paragraph. No bullet breakdowns. No phase previews yet.

Say: "Your discovery data is loaded. Before we start —" then use the AskUserQuestion tool to present two options:
- "I already have a value proposition" — description: "We'll sharpen it and make it more specific"
- "Building from scratch" — description: "We'll build one in three phases"

## Mode routing

- **They have a value prop → Mode B (Sharpen).** Ask "What's your current value proposition?",
  then **load and follow `reference/mode-b-sharpen.md`**.
- **They don't → Mode A (Build).** Say: "We'll build one in three phases. At the end you'll write
  one sentence: [Product] helps [person] who [problem], by [solution], unlike [alternative]. Your
  product stays out until Phase 3. Let's start." Then **load and follow `reference/mode-a-build.md`**.

Both modes map to the founder's template sections (Problem · Customer · Alternative) and end at
Closing below.

## Closing — hand the founder their conclusions

When the sections hold up, **load `reference/output-format.md`** and:

1. Show the founder their value proposition block (format §1) — the **information and conclusions**,
   with the `← why` evidence trace, so they can finalize their template. Then say: "Drop each line
   into the matching section of your `A.3-Value-Prop` template. The reasoning next to each is so
   you remember why it's there."
2. Ask: "Anything you want to sharpen before you lock it in?" If so, adjust one thing at a time,
   re-show the block, and ask again until they're satisfied.

### Quietly record the deliverable

For the skill chain's reference (not something the founder edits or needs to think about), write
the derived deliverable to `2_Outputs/.agents/A.3-Value-Prop/Value-Proposition.md` using the file
template in `reference/output-format.md` §2. Do this **silently** — don't announce the path or make
the founder manage a file.

Then fold the one-line value proposition into company ground truth via `util_get_company_info`
(`set(01_Overview, …)`) per `reference/output-format.md` §3 — the single sentence only, under a
`## Value Proposition` header so it updates in place. The full block stays in the output file, not
in `0_Company/`.

## Guardrails

- Never write the value prop sentence for the founder — create the conditions, then ask them to write it into their template.
- The founder's template in `1_Product_Week/A.3-Value-Prop/` is theirs and human-owned — guide them to fill it; never fill it for them.
- The `2_Outputs/.agents/A.3-Value-Prop/Value-Proposition.md` file is the chain's reference, written quietly — surface the conclusions to the founder, not the file.
- If the founder conflates value prop with pitch: "A pitch is about why someone should invest. A value prop is about why a customer has a problem worth solving."
- If the founder is stuck on the sentence: "Here's a broken version: '[Product] is an AI tool that automates workflows for businesses.' What's wrong with it? Now try yours."
- If the founder can't commit to one customer: "You've described two different customers. The value prop works for one at a time — which one are you solving for in this cohort?"
- Resolve inputs through `util_get_inputs`; read `0_Company/`/`0_User/` only through their utilities. Pressure-test mode validates once and probes once per gap — it must not become a rewrite session.

## Quick reference

| Phase / Mode | Core question | Done when |
|---|---|---|
| Phase 1 | What's the problem? | Specific, customer-language pain |
| Phase 2 | Who has it? | A person, not a segment |
| Phase 3 | What do they do today? | Workaround + concrete cost |
| Sharpen | Is it specific enough? | All criteria pass or one question answered per gap |
