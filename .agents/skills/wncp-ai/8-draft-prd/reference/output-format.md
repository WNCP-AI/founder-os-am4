# Output Format

Load this at the Closing step for the exact formats for both v1 and v2.

---

## 1-v1 — What to show the founder after v1 (their conclusions)

Present the five sections in a clean summary block with `← why` evidence traces so the founder
can finalize their `A.5-PRD-v1` template:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
YOUR PRD v1 — SECTIONS 1–5
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Company + Value Proposition
  Company:    [name]
  Value prop: [one sentence]                    ← from A.3-Value-Prop
  Why us:     [one sentence]

Target User
  Who:        [role / type]                     ← from A.3-User-Persona
  Situation:  [the moment]
  Need:       [one thing]
  Behavior:   [workaround]
  Quote:      "[direct voice]"

Jobs to Be Done
  1st: [job statement] — [AI role]              ← from A.4-JTBD-Prioritized
  2nd: [job statement] — [AI role]
  Prototype focus: Job [#]

Features (Must have → prototype scope)
  [Feature] → [Screen] — does [X], NOT [Y]
  ...
  Not in scope: [Nice to have + Future list]

Prototype
  Hypothesis: [testable assumption]
  Flow:       1. [step] / 2. [step] / ...
  Output:     [what user receives]
  Exclude:    [no auth / no backend / ...]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## 2-v1 — The derived v1 deliverable file (written quietly)

Write this to `2_Outputs/.agents/A.5-PRD-v1/PRD-v1.md` for the chain's reference — silently;
don't announce the path.

```markdown
---
type: prd-v1
session: A.5-PRD-v1
---

# PRD v1

## Section 1 — Company + Value Proposition

| | |
|---|---|
| Company name | [name] |
| Value proposition | [one sentence] |
| Why us | [one sentence] |

## Section 2 — Target User

| | |
|---|---|
| Who | [role / type of person] |
| Situation | [the moment the problem hits] |
| High-value need | [the one thing they need most] |
| Current behavior | [the workaround] |
| Key quote | "[direct customer voice]" |

## Section 3 — Jobs to Be Done

| Job statement | AI role | Priority |
|---|---|---|
| [When X, I want to Y, so I can Z] | [core/feature/not-yet] | 1st |
| [When X, I want to Y, so I can Z] | [core/feature/not-yet] | 2nd |

Prototype focus: Job [#]

## Section 4 — Features

| Feature | Job # | What it does | Scope boundary | Priority |
|---|---|---|---|---|
| [feature] | [#] | [what it does] | Does [X] — does NOT [Y] | Must have |
| [feature] | [#] | [what it does] | — | Nice to have |
| [feature] | [#] | [what it does] | — | Future |

## Section 5 — Prototype

| | |
|---|---|
| Hypothesis | [testable assumption] |
| Output | [what user receives] |

User flow:
1. [step]
2. [step]
3. [step]

What to exclude:
- No user authentication or login
- No backend or database — hardcoded placeholder data only
- No error handling beyond basic input validation
- [founder's additions]
```

---

## 1-v2 — What to show the founder after v2 (their conclusions)

Present all nine sections in a clean summary block so the founder can finalize their
`C.3-PRD-v2` template. Use the same `← why` evidence trace format as v1, extended to all 9
sections. Key additions to highlight:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
YOUR PRD v2 — ALL 9 SECTIONS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[Sections 1, 3, 4, 5, 6 carry forward from PRD v1 — show confirmed / updated versions]

Market Dynamics (§2)
  Market context: [primary market + tailwind]
  Defensible edge: [what compounds over time]
  Competitive gaps: [what they miss]

Assumptions & Risks (§7)
  #1 Solution: [hypothesis from prototype]      Confidence: [H/M/L]
  #2 [Type]:   [assumption]                     Confidence: [H/M/L]
  ...

OKRs (§8)                                       ← from C.2-Metrics-OKR
  Objective: [time-bound direction]
  KR1: [result] — proves assumption #[#]
  KR2: [result] — proves assumption #[#]
  ...

Roadmap (§9)
  V0.1 — Prototype:      [scope] / Success: hypothesis confirmed or invalidated
  V0.2 — Validated MVP:  [scope] / Success: KR1 + KR2 hit
  V1.0 — Product:        [scope] / Success: OKR objective met
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## 2-v2 — The derived v2 deliverable file (written quietly)

Write this to `2_Outputs/.agents/C.3-PRD-v2/PRD-v2.md` for the chain's reference — silently;
don't announce the path. PRD v1 at `2_Outputs/.agents/A.5-PRD-v1/PRD-v1.md` is kept unchanged.

```markdown
---
type: prd-v2
session: C.3-PRD-v2
---

# PRD v2

## Section 1 — Company + Problem

| | |
|---|---|
| Company name | [name] |
| Value proposition | [one sentence] |
| Why us | [one sentence] |
| Why now | [specific change that makes this the right moment] |
| Problem evidence | [direct quote or stat from customer discovery] |

## Section 2 — Market Dynamics

| | |
|---|---|
| Market context | [primary market + tailwind] |
| Defensible edge | [what compounds over time] |

| Competitor / category | What they do well | What they miss | Why customers leave |
|---|---|---|---|
| [name] | [strength] | [gap] | [reason] |

## Section 3 — Target User

| | |
|---|---|
| Who | [role / type of person] |
| Situation | [exact moment the problem hits] |
| High-value need | [the one thing] |
| Current behavior | [the workaround] |
| Customer evidence | "[direct quote]" |

## Section 4 — Jobs to Be Done

| Job statement | AI role | Priority | Rationale |
|---|---|---|---|
| [When X, I want to Y, so I can Z] | [core/feature/not-yet] | 1st | [why this job] |

## Section 5 — Features

| Feature | Job # | What it does | Scope boundary | Priority | Version |
|---|---|---|---|---|---|
| [feature] | [#] | [what it does] | Does [X] — does NOT [Y] | Must have | V0.1 |
| [feature] | [#] | [what it does] | — | Nice to have | V0.2 |
| [feature] | [#] | [what it does] | — | Future | V1.0 |

## Section 6 — Prototype

| | |
|---|---|
| Hypothesis (= Assumption #1) | [testable assumption] |
| Output | [what user receives] |

User flow: [steps]

What to exclude: [list]

## Section 7 — Assumptions & Risks

| # | Type | Assumption — what must be true | Confidence | What could kill it |
|---|---|---|---|---|
| 1 | Solution | [prototype hypothesis] | [H/M/L] | [kill signal] |
| 2 | [Market/Problem/Solution] | [assumption] | [H/M/L] | [kill signal] |

## Section 8 — OKRs

| | |
|---|---|
| Objective | [time-bound qualitative direction] |

| # | Key Result | Signal type | Proves assumption # |
|---|---|---|---|
| KR1 | [result] | [type] | [#] |
| KR2 | [result] | [type] | [#] |

## Section 9 — Roadmap

| Phase | What's in scope | Success criteria | Target date |
|---|---|---|---|
| V0.1 | Must have features | Hypothesis confirmed or invalidated | [date] |
| V0.2 | Nice to have features | KR1 + KR2 hit | [date] |
| V1.0 | Future features | OKR objective met | [date] |
```

---

## 3 — The essence folded into company ground truth (both modes)

After writing the output file, call `util_get_company_info` `set(02_Product, <essence>)`.
Pass the content under a section header so subsequent runs update that section in place:

**v1 mode:** use header `## PRD v1 Summary`

```markdown
## PRD v1 Summary

[Company name] is building [value proposition one-line]. The core prototype tests [hypothesis],
built for [chosen job statement — one line]. Must have features: [1–3 features in a short list].
```

**v2 mode:** use header `## PRD v2 Summary`

```markdown
## PRD v2 Summary

[Company name] is building [value proposition one-line]. The riskiest assumption is [lowest-
confidence assumption — one line]. V0.1 scope: [must-have features]. OKR objective: [one-liner].
```

Full PRD stays in `2_Outputs/.agents/<session>/` — only the distilled summary goes to `0_Company/`.
