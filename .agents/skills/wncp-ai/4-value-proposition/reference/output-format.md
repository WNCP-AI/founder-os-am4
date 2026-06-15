# Output Format

Load this at the Closing step for the exact formats.

## 1 — What to show the founder (their conclusions)

Present the information and the conclusions so they can finalize their template. The `← why`
column traces each line back to the evidence — it's what teaches the founder to ground positioning
in data rather than assertion.

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
YOUR VALUE PROPOSITION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[Product] helps [person] who [problem], by [solution], unlike [alternative].

Problem:        [what they struggle with]    ← why: [the signal it came from]
Customer:       [who, in what situation]      ← why: [the evidence]
Alternative:    [what they do today + cost]    ← why: [the workaround named]
Differentiator: [unlike X, we do Y]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## 2 — The derived deliverable file (written quietly)

Write this to `2_Outputs/.agents/A.3-Value-Prop/Value-Proposition.md` for the chain's reference —
silently; don't announce the path.

```markdown
---
type: value-prop
session: A.3-Value-Prop
---

# Value Proposition

[Product] helps [person] who [problem], by [solution], unlike [alternative].

## Components

Customer:       [who]
Problem:        [what they struggle with]
Solution:       [what the product does]
Differentiator: [unlike X, we do Y]
```

## 3 — The essence folded into ground truth

Call `util_get_company_info` `set(01_Overview, <essence>)`. Pass the content under a
`## Value Proposition` section header so subsequent runs update that section in place rather than
appending a new one — the single sentence only:

```markdown
## Value Proposition

[Product] helps [person] who [problem], by [solution], unlike [alternative].
```
