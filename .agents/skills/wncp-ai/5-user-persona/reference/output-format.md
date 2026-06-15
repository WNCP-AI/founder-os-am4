# Output Format

Load this at the Closing step for the exact formats.

## 1 — Gather Current Behavior and Key Quote

Before producing the output block, collect two fields from the discovery data:

**Current behavior** — look for "what they do today" or "workaround" sections in the files
under `5_Library/sources/processed/`. If found, use it. If not found, ask the founder:

> "What does [person] do today to work around this problem?"

**Key quote** — scan `5_Library/sources/processed/` for a direct quote that best validates
the persona. Surface it and ask:

> "Does this quote capture the pain well — does it back up your persona?
> '[candidate quote]'"

If they agree, use it. If they disagree, ask them to suggest a better one or confirm there
isn't one. Do not invent a quote.

---

## 2 — What to show the founder (their conclusions)

Present the persona block so they can finalize their `A.3-User-Persona` template:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
USER PERSONA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Identity         — [role, company type/stage, one-line context]     ← why: [signal from discovery]
Situation        — [the specific moment the problem surfaces]         ← why: [the evidence]
Need             — [one thing, solution-agnostic]
Current behavior — [what they do today to work around the problem]
Key quote        — "[one line in their own words]"
Why this ICP     — [one line of evidence or reasoned commitment]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
OUT OF SCOPE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[Plausible user types explicitly ruled out — derive from the person named above
and any alternatives the founder considered during the exercise]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
IN SCOPE FOR JTBD
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
The "need" above is the seed for your job statement.
The JTBD skill will read this automatically —
you do not need to copy anything.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## 3 — The derived deliverable file (written quietly)

Write this to `2_Outputs/.agents/A.3-User-Persona/User-Persona.md` for the chain's reference —
silently; don't announce the path.

```markdown
---
type: user-persona
session: A.3-User-Persona
---

# User Persona

## Identity
[role, company type/stage, one-line context]

## Situation
[the specific moment the problem surfaces]

## High-Value Need
[one thing, solution-agnostic]

## Current Behavior
[what they do today to work around the problem — extracted from discovery data or founder answer]

## Key Quote
"[one line in their own words — extracted from discovery data or founder confirmed]"

## Why This ICP
[one line of evidence or reasoned commitment]

## Out of Scope
[plausible user types explicitly ruled out]
```

---

## 4 — The essence folded into ground truth

Call `util_get_company_info` `set(03_Users, <essence>)`. Pass the content under a
`## User Persona` section header so subsequent runs update that section in place rather than
appending a new one — the identity, situation, and need only:

```markdown
## User Persona

Identity:  [role, company type/stage, one-line context]
Situation: [the specific moment the problem surfaces]
Need:      [one thing, solution-agnostic]
Why this ICP: [one line of evidence or reasoned commitment]
```

The full persona block stays in the output file, not in `0_Company/`.
