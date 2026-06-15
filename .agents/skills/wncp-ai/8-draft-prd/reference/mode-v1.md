# Mode v1 — PRD Day 1 (§§ 1–5)

Load this when the founder selects PRD v1. Walk all five sections in order; wait for
confirmation before moving to the next. The founder fills in their `A.5-PRD-v1` template
by hand — you pre-fill from their existing outputs and guide each decision.

**Core rule:** This mode reads and assembles. It does not re-run value prop, persona, or JTBD.
The only genuinely new decisions are: Why us, the narrowest features per chosen job, and what
the prototype is testing.

---

## Section 1 — Company + Value Proposition

**Produce:** confirmed company name, value proposition, one-sentence Why us.

Present company name and value proposition pre-filled from the A.3-Value-Prop output. Ask the
founder: "Does this still match, or has anything shifted?" One exchange — collect any correction.

**Why us:** If the company ground truth (`util_get_company_info`) or any founder background
material contains domain experience, personal connection to the problem, or unfair access — draft
a one-sentence Why us and present it for confirmation. If nothing relevant is found, ask: "Why
are you the right person for this problem?" Accept whatever they give; don't push for more.

Move on when the founder confirms or corrects the three fields.

---

## Section 2 — Target User

**Produce:** all five persona fields confirmed.

Present all five fields pre-filled from the A.3-User-Persona output:
- Who (role / type of person)
- Situation (the moment the problem hits)
- High-value need (the one thing they need most)
- Current behavior (what they do today — the workaround)
- Key quote (direct customer voice)

Ask: "Are these still accurate, or has anything shifted?" If yes, move on. If something shifted,
collect the correction. One exchange maximum.

---

## Section 3 — Jobs to Be Done

**Produce:** confirmed job list + one chosen job for the prototype.

Present the ranked job table pre-filled from the A.4-JTBD-Prioritized output, including AI role
tags (core / feature / not-yet), exactly as they appear. Do not re-coach the tags — carry them
forward.

Ask: "Does this ranking still hold, or did the order shift?" Accept any adjustment.

Then: "The prototype tests one job. Which one are you building for?" Recommend Job 1. Accept any
answer. All other jobs carry into Features as Future items.

---

## Section 4 — Features

**Produce:** feature table with each feature separated, prioritized, dependency-checked,
and Must Have items scope-bounded.

### Step 1 — Narrowest wedge

Ask: "For [chosen job] — what's the absolute minimum version that still gets this job done?
Not a list — the simplest single thing where the job actually works."

If the founder describes a flow with multiple steps, separate each into its own feature. Each
feature is one sentence starting with a user action verb.

### Step 2 — Confirm and separate

Reflect the list back and ask if anything is missing.

Run a dependency check: does any feature require something else to exist first? Common hidden
dependencies: "send email" requires a contact list; "personalized output" requires stored profile
data; "dashboard" requires stored records. Name any dependency as a separate feature.

### Step 3 — Priority

Work through the list one feature at a time. Give your recommendation first:
"I'd call this Must have because without it the job doesn't happen — does that feel right?"

Use AskUserQuestion for each: **Must have** / **Nice to have** / **Future**.

Push back if Must Haves can't realistically be built in 60–90 minutes.
If Must Have count exceeds 3, flag: "Can you build all of these in 60–90 minutes?"

Nice to have and Future stay in the table — they feed the exclusion list.

### Step 4 — Scope boundaries (Must Have only)

For each Must Have, draft: "[Feature] does [X] — does NOT [Y]." The "does NOT" comes from Nice to
have and Future items already identified. Confirm each. Then ask: "What screen does the user see
when they use this feature?"

Show a scope summary before moving on:

```
Must have:
- [Feature] → [Screen] — does [X], NOT [Y]

Not in the prototype:
- [Nice to have + Future features]
```

Confirm before proceeding to Section 5.

---

## Section 5 — Prototype

**Produce:** hypothesis, user flow, output, exclusion list. One field at a time.

### Hypothesis

Ask: "What's the one assumption this prototype is testing — the thing that, if false, changes
what you build next?"

This is required — a prototype without a hypothesis is a demo, not a test. Don't move on until
the founder has a specific, testable assumption.

### User flow

Derive numbered steps from the Must Have features in order — starting from the named interface,
through to the final outcome. Present for confirmation. If a step jumps without explanation, add
it and flag it. Check that the last step produces the output the founder described.

### Output

Draft what the user receives at the end of the flow from the final Must Have feature. Ask them
to confirm or be more specific about format.

### What to exclude

Pre-populate from:
- Scope boundaries (the "does NOT" items from each Must Have)
- Nice to have and Future features
- Standard exclusions: no auth, no backend, no error handling

Ask: "Anything else that should stay out?"

---

## Validation — before moving to Closing

Before handing off to the Closing section, check:

| Criterion | Pass | Fail → one probe |
|---|---|---|
| Hypothesis is testable | A specific assumption, not a goal | "That's a goal, not a hypothesis — what would prove this wrong?" |
| Every Must Have traces to the chosen job | Direct connection | "Which part of [job statement] does this feature enable?" |
| Scope boundaries set for all Must Haves | Each has a "does NOT" | "What does this feature explicitly NOT do?" |
| Must Have count ≤ 3 | Realistic for 60–90 min build | Flag: "Can you build all of these in 60–90 minutes?" |

Ask one probe at a time. Wait for the answer. One pass only — don't loop.

When all five sections hold up, return to the Closing in the SKILL.
