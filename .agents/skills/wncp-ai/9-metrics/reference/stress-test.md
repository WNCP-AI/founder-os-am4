# Phase 3 — Stress-Test

Load this for Phase 3. Both Build and Validate modes converge here. Run self-check first,
then the ambition check. One `AskUserQuestion` call per KR — never bundle.

---

## Self-check — one KR at a time

For each KR, ask:

> "Self-check on KR[N]: If you fully hit this, does it prove that **[riskiest assumption]**
> is true or false?"

| Answer type | Response |
|---|---|
| "Yes — hitting this proves the assumption" | Accept — move to next KR |
| "Not sure / I could hit it without proving the assumption" | "Then this KR doesn't validate your assumption. What would you need to see to know the assumption is actually proven?" |
| Rewritten KR | Re-run self-check on the new version before moving on |

Never skip a KR. Every KR must be explicitly confirmed or rewritten.

---

## Ambition check — once all KRs pass

Ask (one `AskUserQuestion` call):

> "If you hit every KR, how confident are you? Target: **50–60% hit rate** — ambitious
> enough to push you, grounded enough to be real."

| Answer type | Response |
|---|---|
| "Probably 50–70%" | Accept — move to Closing in the SKILL |
| "I'll hit all of them" | "Then they aren't ambitious enough. Which KR could you raise the bar on?" → one revision, re-run self-check on that KR, then move to Closing |
| "I'll miss most of them" | "Too aggressive. Which KR is least grounded in what you know?" → one revision, re-run self-check on that KR, then move to Closing |

After the ambition check resolves, return to Closing in the SKILL.
