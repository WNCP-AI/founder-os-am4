# Output Format

Load this at the Closing step for the exact formats.

## 1 — What to show the founder (their conclusions)

Present the JOBS TO BE DONE block as plain text so they can finalize their
`1_Product_Week/A.4-JTBD/` template. The layer and AI tags carry forward into
the JTBD Prioritizer — show them here so the founder understands the full record.

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
JOBS TO BE DONE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Job 1 — [statement]
        Layer: [functional / emotional / social]
        AI:    [tag] — [rationale]

Job 2 — [statement]
        Layer: [tag]
        AI:    [tag] — [rationale]

[continue for all jobs]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## 2 — The derived deliverable file (written silently)

Write this to `2_Outputs/.agents/A.4-JTBD/JTBD.md` for the chain's reference —
silently; do not announce the path or make the founder manage the file.

```markdown
---
type: jtbd
session: A.4-JTBD
---

# Jobs to Be Done

## Job 1
**Statement:** When [situation], I want to [motivation], so I can [outcome].
**Primary layer:** [functional / emotional / social]
**AI role:** [tag] — [rationale]

## Job 2
**Statement:** When [situation], I want to [motivation], so I can [outcome].
**Primary layer:** [tag]
**AI role:** [tag] — [rationale]

[repeat for each job]

## Ready for prioritization
[N] jobs ready for the JTBD Prioritizer.
```

## 3 — The essence folded into ground truth

Call `util_get_company_info` `set(03_Users, <essence>)`. Pass a `## Jobs to Be Done`
section header so subsequent runs update that section in place rather than appending.
Include only the top 1–2 job statements (the distilled signal) — full output stays in
`2_Outputs/.agents/A.4-JTBD/JTBD.md`, not in `0_Company/`.

```markdown
## Jobs to Be Done

Job 1: When [situation], I want to [motivation], so I can [outcome]. ([layer] / AI: [tag])
Job 2: When [situation], I want to [motivation], so I can [outcome]. ([layer] / AI: [tag])
[N jobs total — see 2_Outputs/.agents/A.4-JTBD/JTBD.md]
```
