# Mode A — Build from Scratch

Load this when the founder is building an OKR from scratch. Walk Phase 1 then Phase 2 in
order. One question per `AskUserQuestion` call — never bundle two.

---

## Phase 1 — Objective

Ask: "Write 1 Objective — qualitative, focused, tied to your riskiest assumption. It
doesn't need a number. Example: 'Prove founders pay for AI-written investor updates before
building the full product'."

Run the validation table internally. Ask one probe at a time if needed.

| Answer type | Response |
|---|---|
| Qualitative + time-bound | Accept — confirm it's tied to the assumption, move to Phase 2 |
| Qualitative, no time horizon | Accept — use `AskUserQuestion`: "By when?" |
| Numerical ("increase revenue 30%") | "That's a KR — the Objective is the qualitative direction. What's the underlying goal?" |
| Too broad | "Narrow it: what does your riskiest assumption specifically need to prove this quarter?" |
| Multiple objectives | "Pick one — the one most tied to your riskiest assumption." |

Done when: 1 qualitative, time-bound Objective is locked.

---

## Phase 2 — Key Results

Ask: "KRs should prove your riskiest assumption is true or false. Signal types to draw from:

- **Willingness-to-pay signal** — evidence customers value it enough to pay or commit
- **Activation / time-to-first-value** — how fast customers reach their first meaningful outcome
- **Problem-resolution rate** — % of the target problem actually solved for customers
- **Task-completion rate** — % completing a key workflow without dropping off
- **Completion-based** — 'Ship X by Y' — valid for non-quantitative goals

Write your first Key Result."

Run the KR validation table per KR. Offer to stop after KR2.

**KR validation table:**

| KR type | Response |
|---|---|
| Validation outcome tied to the riskiest assumption and consistent with the Objective | Accept — confirm signal type; use `AskUserQuestion`: "Next KR, or are 2 enough?" |
| Activity count (DAUs, sessions, features shipped) | "This tracks effort. If you hit this, does it prove your assumption is true? What's the outcome signal?" |
| KR assumes something the Objective hasn't committed to | "This KR assumes [X]. Your Objective commits to [Y]. What's the signal consistent with what you've actually committed to?" |
| Outcome but not tied to the riskiest assumption | "Good metric — but does it validate your riskiest assumption, or a different one?" |
| Vague / unmeasurable | "What's the concrete thing you'd point to — a number, a threshold, a decision?" |

After KR2: use `AskUserQuestion` to ask: "You have 2 KRs. Add a 3rd, or does this set
fully cover the assumption?"

Done when: 2–4 KRs are locked, each passing the validation table.

Then return to Phase 3 (stress-test) in the SKILL.
