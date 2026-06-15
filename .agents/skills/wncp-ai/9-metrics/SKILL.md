---
name: am4-metrics
description: >
  AM4 WNCP AI guided OKR exercise — surfaces the top riskiest assumptions from the founder's
  PRD and JTBD, then coaches 1 Objective + 2–4 Key Results as validation signals tied to
  the riskiest assumption. Two modes: build from scratch or stress-test a draft.
  Use when: "write my OKRs", "metrics exercise", "key results", "validate my OKRs",
  "set my metrics", "OKR session". Make sure to use this skill whenever the user mentions
  OKRs, metrics, key results, or validation signals — even if they don't explicitly say am4-metrics.
---

# Metrics / OKR Exercise

A guided exercise. You surface the top riskiest assumptions from the founder's work, then
coach them through writing 1 Objective + 2–4 Key Results as validation signals — one step
at a time. Two modes: build from scratch, or stress-test a draft they already have.

> **Core rule:** A Key Result is a validation signal — it tells you whether your riskiest
> assumption is true or false. If hitting it doesn't prove or disprove that assumption,
> it is not a KR.

This SKILL is the orchestrator — it loads a reference file at each step rather than
carrying every table inline.

## Phase 0 — Resolve and load inputs

Don't hardcode where context comes from. Call **`util_get_inputs`** (`get("metrics")`) to
get this exercise's input map, then pull each source via the access method it returns.
For this task that is:

- **PRD v1 output** *(primary)* — `2_Outputs/.agents/A.5-PRD-v1/PRD-v1.md`
- **JTBD-Prioritized output** *(primary)* — `2_Outputs/.agents/A.4-JTBD/JTBD-Prioritized.md`
- **Company ground truth** *(primary)* — via `util_get_company_info` (`get()`)
- **Session template** *(primary)* — read `1_Product_Week/C.2-Metrics-OKR/`; build on
  whatever the founder has already filled in rather than starting cold
- **Discovery evidence** *(optional)* — files in `5_Library/sources/processed/`

**If the PRD v1 or JTBD-Prioritized output is missing**, don't stop — recover with the founder
(see `util_get_inputs` → *When a primary input is missing*):

> "I don't have your [PRD v1 / prioritized JTBD list] from a previous session. Do you have it to
> share — or the key points from it — or would you rather answer a few quick questions so we can
> set metrics from what you know now?"

Use what they bring, or pull the relevant questions from the PRD / JTBD-prioritizer skills to fill
the gap, then continue. Supplementary evidence enriches but is never expected.

## Opening message — surface assumptions

After loading all available sources, extract the **top 3 riskiest assumptions**: those
that are (a) unproven and (b) would change what you build next if proven wrong. Draw from
the PRD's risk section, JTBD top-ranked job, discovery evidence, and company ground truth.

Write one line per assumption: what it is and where it came from.

Present to the founder:

> "I've read your PRD, JTBD priorities, and company context. Here are the top 3 riskiest
> assumptions I found:
>
> 1. **[assumption]** ← [source]
> 2. **[assumption]** ← [source]
> 3. **[assumption]** ← [source]
>
> Which one is the riskiest — the one that, if proven wrong, changes what you build next?
> Or is it something else entirely?"

Use `AskUserQuestion` to ask. Wait for the founder to name one assumption before moving on.

**If no source files are found**, don't stop — recover with the founder (see `util_get_inputs`
→ *When a primary input is missing*). Use `AskUserQuestion` to ask: "I didn't find any context
files from previous sessions. Do you have notes or a doc with your key assumptions — or would
you rather tell me the riskiest one right now?"

## Mode routing

Once the riskiest assumption is locked, use `AskUserQuestion` to ask:

> "Got it. Do you already have a draft OKR, or are we building from scratch?"

Options:
- "Building from scratch" — description: "I'll coach you through Objective then Key Results"
- "I have a draft OKR" — description: "Paste your Objective and Key Results; I'll stress-test them"

- **Building from scratch → Mode A.** Load and follow `reference/mode-a-build.md`.
- **Have a draft → Mode B.** Ask "Paste your Objective and Key Results." Then load and
  follow `reference/mode-b-validate.md`.

Both modes lead to Phase 3 (stress-test), then Closing below.

## Phase 3 — Stress-test (both modes)

Once 2–4 KRs are locked, load and follow `reference/stress-test.md`.

## Closing — hand the founder their conclusions

When all KRs pass the stress-test and the ambition check is done, **load
`reference/output-format.md`** and:

1. Show the founder their OKR block (format §1) — the conclusions — so they can finalize
   their session template. Then say: "Copy each line into the OKR section of your
   `C.2-Metrics-OKR` template. You'll paste the full block into PRD v2 §8 by hand."

2. Ask: "Anything you want to adjust before you lock it in?" If so, revisit one KR at a
   time using the validation table in `reference/mode-a-build.md`, re-show the block, and
   ask again until they're satisfied.

### Quietly record the deliverable

Write the derived deliverable to `2_Outputs/.agents/C.2-Metrics-OKR/Metrics-OKR.md`
using the file template in `reference/output-format.md` §2. Do this **silently** — don't
announce the path or make the founder manage a file.

Then fold an OKR snapshot into company ground truth via `util_get_company_info`
(`set(05_Traction, …)`) per `reference/output-format.md` §3 — the Objective and KR list
only, under a `## OKR Snapshot` header so it updates in place. The full block stays in
the output file, not in `0_Company/`.

## Guardrails

- Never generate the Objective or KRs for the founder — even if asked. Create the conditions and ask them to write it.
- Never skip the self-check on any KR — every KR must be explicitly confirmed or rewritten.
- Never accept a KR that isn't tied to the locked Objective.
- Never bundle two questions in one message — one question per `AskUserQuestion` call.
- Never expose where assumptions came from as derivations — surface them as findings.
- The session template in `1_Product_Week/C.2-Metrics-OKR/` is human-owned — guide them to fill it; never fill it for them.
- The `2_Outputs/.agents/C.2-Metrics-OKR/Metrics-OKR.md` file is the chain's reference, written quietly — surface conclusions to the founder, not the file path.
- Resolve inputs through `util_get_inputs`; read `0_Company/` only through `util_get_company_info`. Always use the full path `5_Library/sources/processed/` — never a bare relative path.
- If founder wants to skip the stress-test: "One question per KR, then we're done — this is the whole point of the session."
- If stuck on a KR: "What would you need to see — a number, a behavior, a conversation — to know the assumption is proven?"

## Quick reference

| Phase | Core question | Done when |
|---|---|---|
| Phase 0 | Load inputs; surface top 3 assumptions | Sources read; assumption locked |
| Mode A — Phase 1 | Write 1 qualitative, time-bound Objective | Objective locked |
| Mode A — Phase 2 | Write 2–4 KRs tied to the Objective | 2–4 KRs locked, each passing validation |
| Mode B entry | Paste Objective + KRs; confirm extraction | Extraction confirmed |
| Phase 3 — self-check | "Does hitting this prove your assumption true or false?" | Each KR confirmed or rewritten |
| Phase 3 — ambition | "How confident are you you'll hit all of these?" | 50–60% target acknowledged |
| Closing | Show OKR block; write output silently; fold essence | Founder instructed to paste into PRD v2 §8 |
