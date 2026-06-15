# Mode B — Validate a Draft

Load this when the founder has pasted their Objective and Key Results. Your job is to
stress-test what they have — not rewrite it for them.

---

## Step 1 — Extract and confirm

Read the draft. Extract:
- The Objective (1 qualitative statement)
- Each KR (numbered list)

Confirm back: "Got it — here's what I see:

**Objective:** [extracted objective]
**KR1:** [text]
**KR2:** [text]
…

Is that right?"

Wait for confirmation before proceeding. If their draft is missing an Objective or has
only 1 KR, note the gap: "I see [X] — you'll want at least 2 KRs and a clear Objective
before we stress-test." Then use `AskUserQuestion` to ask whether they want to add the
missing piece now or proceed with what they have.

---

## Step 2 — Objective check

Run internally — ask one probe if needed:

| Criterion | Pass | Fail → ask this |
|---|---|---|
| Qualitative direction | Not a number | "This reads as a metric. What's the qualitative goal behind it?" |
| Tied to the riskiest assumption | Relates to what was locked in Phase 0 | "Does this Objective directly test [riskiest assumption], or is it a different bet?" |
| Time-bound | Has a timeframe | "By when? Add a time horizon." |

Work through any failed criteria one at a time. When the Objective passes (or the founder
has addressed each gap), move to Step 3.

---

## Step 3 — KR check

For each KR, run the validation table from `reference/mode-a-build.md` — same rules apply
whether the KR was drafted by the founder or built from scratch.

One KR at a time. Wait for the answer before moving to the next.

When all KRs pass (or have been rewritten), return to Phase 3 (stress-test) in the SKILL.
