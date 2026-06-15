# Output Format — JTBD-Prioritized.md

Load this at the Closing step for the exact file format to write silently.

## The derived deliverable file (written quietly)

Write this to `2_Outputs/.agents/A.4-JTBD/JTBD-Prioritized.md` for the chain's reference —
silently; don't announce the path to the founder.

```markdown
---
type: jtbd-prioritized
session: A.4-JTBD
---

# JTBD — Prioritized

## #1 — Top Job
**Statement:** [job statement]
**Primary layer:** [tag]
**AI role:** [tag] — [rationale from JTBD.md]
**Why #1:** [2–3 sentence rationale from the conversation]
**Watch out for:** [honest risk or assumption]
**Decision:** KEEP — top job

## #2
**Statement:** [job statement]
**Primary layer:** [tag]
**AI role:** [tag] — [rationale from JTBD.md]
**Why #2:** [rationale]
**Watch out for:** [risk or assumption]
**Decision:** [KEEP — reason / KILL — stated reason]

[repeat for all jobs]

## Next step
[Concrete validation action for the top job — specific to the job and its watch-out-for]
```

This file is the chain's reference. The `8-draft-prd` skill reads it as `A.4-JTBD-Prioritized`
input automatically. The founder records their decisions in their own
`1_Product_Week/A.4-JTBD/` template by hand.

## No essence fold

This skill has no essence target (`—`). Do NOT call `util_get_company_info` `set()` after
writing the output file. The JTBD essence fold is handled by skill 6 (`am4-jtbd`).
