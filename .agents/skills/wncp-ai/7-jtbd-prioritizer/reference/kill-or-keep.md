# Kill-or-Keep — Decision Record

Load this after the ranking is confirmed. Work through every job that is not in the top
position, one at a time.

---

## The question

For each non-top job, ask:

> "Job [N] ranked [position]. Are you keeping it as a future candidate, or killing it?
> If killing: one sentence on why."

Use **AskUserQuestion** for this with two options:
- Label: "Keep", Description: "It stays as a future candidate — name what would need to change to move it up."
- Label: "Kill", Description: "One sentence on why — it's off the list."

---

## Response table

| Answer type | Response |
|---|---|
| Keep + brief reason | Accept |
| Kill + stated reason | Accept |
| "I'm not sure" | "Not sure means it stays alive and competes with your top job for your attention. If you're not ready to kill it, keep it — but name what would need to be true to revisit it." |
| Keep with no reason | "What would change for you to move this up the list? What signal would make this the top job?" |

---

## Guardrails

- Every non-top job must get an explicit decision. Never skip one.
- "Keep" without a reason always gets one follow-up: what would need to change?
- A kill decision is final for this round — don't reopen it unless the founder initiates.
- Never accept a kill decision that's really about ease of build rather than customer need
  without noting it: "You're killing this because it's harder to build — that's fine, but
  name it as a resourcing decision, not a strategic one."
