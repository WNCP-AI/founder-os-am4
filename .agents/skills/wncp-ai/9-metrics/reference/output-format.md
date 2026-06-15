# Output Format

Load this at the Closing step for the exact formats.

## 1 — What to show the founder (their conclusions)

Present the OKR block so they can finalize their session template and paste into PRD v2 §8.
The `← signal` column traces each KR back to its validation signal type.

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
METRICS / OKR
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Riskiest Assumption
[the assumption locked in Phase 0]

Objective
[founder's Objective]

Key Results
KR1: [text]    ← signal: [type]
KR2: [text]    ← signal: [type]
KR3: [text, if applicable]    ← signal: [type]
KR4: [text, if applicable]    ← signal: [type]

Target hit rate: 50–60%
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

Then say: "Copy each line into the OKR section of your `C.2-Metrics-OKR` template, then
paste the block into PRD v2 §8 by hand. Target hit rate: 50–60%."

---

## 2 — The derived deliverable file (written silently)

Write this to `2_Outputs/.agents/C.2-Metrics-OKR/Metrics-OKR.md` for the chain's
reference — silently; don't announce the path to the founder.

```markdown
---
type: metrics-okr
session: C.2-Metrics-OKR
---

# Metrics / OKR

## Riskiest Assumption

[the assumption locked in Phase 0]

## Objective

[founder's Objective]

## Key Results

| # | Key Result | Signal type |
|---|---|---|
| KR1 | [text] | [type] |
| KR2 | [text] | [type] |
| KR3 | [text, if applicable] | [type] |
| KR4 | [text, if applicable] | [type] |

## Ambition

Target hit rate: 50–60%
```

---

## 3 — The essence folded into ground truth

Call `util_get_company_info` `set(05_Traction, <essence>)`. Pass the content under a
`## OKR Snapshot` section header so subsequent runs update that section in place rather
than appending a new one — Objective and KR list only:

```markdown
## OKR Snapshot

**Objective:** [founder's Objective]

**Key Results:**
- KR1: [text]
- KR2: [text]
- KR3: [text, if applicable]
- KR4: [text, if applicable]

Target hit rate: 50–60%
```
