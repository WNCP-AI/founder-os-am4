---
title: "Roadmapping Template & Skills"
session: "D"
session_type: "Virtual"
owner: "Damien"
date: "Jun 18"
time: "2:00 PM MST"
summary: "Now/Next/Later prioritization template with (Impact × Confidence) / Effort scoring — converts PRD outputs into a repeatable sprint cycle founders run with their team in Sprint 3+"
---
now 
# Roadmapping Template & Skills

## Time

Demo Day close (Thu Jun 18, 2:00 PM MST), "Next-Cycle Commitments" segment. Briefly introduced — not a workshop. 

## Inputs

- **PRD v2** (Sections 1–9) — Section 5 "Won't have" items lock the Kill column; Section 7 assumptions inform Impact; Section 8 OKRs define "done" per Now item; Section 9 phase roadmap (V0.1/V0.2/V1.0) maps to Now/Next/Later placement
- **Demo Day feedback** — what to promote (Next → Now) or defer (Now → Later)
- **Process Card** — the CRAFT+ cadence the roadmap executes

## Founder Prerequisites

- **PRD v2 complete** — Section 5 "Won't have" items and Section 8 OKRs are required inputs
- **A team or solo plan** — works best shared with a team; works solo for the cohort's three solo founders

## Outcomes

**Primary (max 2)**
- Founder can score any initiative — build or test — on Impact (1–5), Confidence (1–5), and Effort (1–5) and place it in Now/Next/Later from the Score = (Impact × Confidence) / Effort; any item with Confidence 1 and Impact 4–5 auto-elevates to Now as a must-test risk regardless of Score
- Founder can run a cycle review independently — update scores from learnings, promote Next items, generate new PRD tasks — closing the CRAFT+ loop (Forge → Test → Collect → Refine → Analyze) without facilitation

**Secondary (max 2)**
- Founder leaves Demo Day with a written Sprint 3 Now list: scored, Kill list imported, cycle length and review date set
- Template lives in Founder OS beside the PRD, keeping the chain intact (value prop → JTBD → PRD → roadmap)

## Founder Operating Process

#### Phase 1: Generate
- **1.1** — List every candidate: features, improvements, pivots, open questions (from Demo Day feedback, PRD Section 7 assumptions, un-built JTBD items)

#### Phase 2: Score
Score every item — build or test — against the same three dimensions. Scores are relative to your product and your capacity, not absolute. Any score of 4 or 5 on Impact or Confidence must be backed by a specific customer signal or behavioral evidence — gut feel is not a score.

- **2.1 — Impact (1–5):** value delivered *if* this works. For build items: outcome to the user. For test items: risk reduced by answering the question.
  - `1` you thought of it — no customer has mentioned it · `2` mentioned once or twice, or inferred · `3` customers acknowledged the problem but have workarounds they're OK with · `4` customers said it would change their behavior or decision to pay or stay · `5` multiple customers named this unprompted as the thing blocking them
  - *Calibration question: "What did a customer actually say or do that tells you this is a 4 or 5?"*

- **2.2 — Confidence (1–5):** how certain are you this is the right thing to build or test, based on actual evidence. Sourced directly from PRD v2 Section 7 — H→5, M→3, L→1. The skill asks inline: *"Is this still the right confidence level since Demo Day?"* Update here — do not go back to the PRD first.
  - `1` pure hypothesis — no customer has confirmed it · `2` inferred from the persona, not heard directly · `3` 1–2 customers confirmed when asked; no behavioral signal yet · `4` 2+ customers named this unprompted in their own words · `5` customers demonstrated through behavior — paid, switched, or changed their workflow
  - *Calibration question: "Are you confident because of evidence, or because you want this to be true?"*

- **2.3 — Effort (1–5):** real cost to ship given your actual team, skills, and available hours — not best-case capacity. The same item scores differently per company.
  - `1` hours–days — you've done this exact thing before, no new tools or skills · `2` ~a week — familiar territory, one new thing to figure out · `3` 2–4 weeks — mostly familiar, at least one part you haven't built before · `4` 1–2 months — significant new capability required or a dependency you don't control · `5` months — hire, major procurement, regulatory approval, or infrastructure you don't have
  - *Three calibration questions before accepting a score: (1) "Have you built something like this before — how long did it actually take?" (2) "Do you have the skills to build this yourself, or do you need help?" (3) "How many hours a week do you realistically have this cycle — not in theory, in practice?"*
  - If you haven't done it before, score up one level. First-time builds almost always take 3× longer than estimated.

- **2.4 — Score:** `(Impact × Confidence) / Effort` — higher score = higher priority. Calculate per item; rank to inform placement.

- **2.5 — Risk flag:** if Confidence = 1 AND Impact ≥ 4, auto-elevate to Now regardless of Score. A high-impact belief with no evidence is the most dangerous thing on your board — test it before building anything else.

#### Phase 3: Place & Lock
- **3.1** — Plot by Score: highest Score → **Now** · risk-flagged items (Confidence 1 + Impact ≥ 4) → **Now** regardless of Score · high Score + high Effort → **Next** · low Score → **Later** · Section 5 "Won't have" items → **Kill**
- **3.2** — Cap Now at 2–3 items. If more qualify, rescore until only the top remain. The team works these and nothing else.
- **3.3** — Per Now item: name its PRD and write the Next gate ("moves up when Now proves ___")

#### Phase 4: Commit & Cycle
- **4.1** — Set cycle length (founder's choice — not assumed 2 weeks) and a first review date before leaving
- **4.2** — Each review: close or kill Now items, promote qualifying Next items, generate new PRD tasks from learnings — the loop restarts here
- **4.3** — Repeat. The board is never done; the rhythm is the discipline, not the cycle length.

## Format

Introduced at Demo Day close — not a workshop. Founders receive the Excel template plus a companion roadmapping skill (markdown, for Claude Code) and use both independently from Sprint 3 onward. The Excel is the live working board; the skill runs the scoring and cycle-review process. Neither is used interactively during Demo Day — they're handed off as Sprint 3+ tools.

The skill accepts as inputs: PRD v2 (all sections), raw Demo Day feedback, and customer evidence (interview notes, usage signals, behavioral data). It asks calibration questions before accepting any Impact or Confidence score and outputs a scored Now/Next/Later recommendation with a one-line rationale per item and each Now item linked to the hypothesis it is testing or the assumption it is validating. Output is written to `sources/processed/roadmap.md` and displayed inline. The skill does not modify any other file.

The Excel template mirrors a Trello / Asana / Notion board — single file, numbered item system. Requirements:

- **Hierarchical** — work items with sub-items (task/sub-task, story/sub-story); user picks the unit
- **Kanban + rating** — Now / Next / Later / Kill columns; Impact, Confidence, Effort, and auto-calculated Score per item; risk flag auto-applied
- **Drill-down** — each item expands to its Impact evidence, Confidence source, Effort breakdown, PRD link, and sub-items
- **Numbered** — every item carries an ID for reference across cycles

Two views ship in the template:

**1 — Project Roadmap** (the board)

```markdown
# [Company] Roadmap — Cycle [n]
Cycle length: [2wk] · Review: [date] · Owner: [name]

## NOW  (max 2–3)
| ID | Type  | Initiative | Score | Impact | Confidence | Effort | Risk | PRD |
|----|-------|------------|:-----:|:------:|:----------:|:------:|:----:|-----|
| 1  | Test  | [item]     | 5.0   | 5      | 1          | 1      | ⚠   | [link] |
| 2  | Build | [item]     | 4.0   | 4      | 5          | 5      |     | [link] |

## NEXT  (conditional)
| ID | Type  | Initiative | Score | Impact | Confidence | Effort | Gate — moves to Now when… |
|----|-------|------------|:-----:|:------:|:----------:|:------:|---------------------------|
| 3  | Build | [item]     | 3.1   | 5      | 4          | 4      | item 1 proves [X]         |

## LATER  (parked, no dates)
| ID | Type  | Initiative | Score | Impact | Confidence | Effort |
|----|-------|------------|:-----:|:------:|:----------:|:------:|
| 4  | Build | [item]     | 1.5   | 3      | 2          | 4      |

## KILL  (from PRD Section 5 "Won't have" — do not re-score)
| ID | Item   | Why killed |
|----|--------|------------|
| —  | [item] | [reason]   |
```

**2 — Body of Work** (one card, drill-down per item)

```markdown
## [ID] [Initiative name]
Placement: Now · PRD: [link] · Status: in-progress

Impact      5/5 — [customer signal: what they said or did]
Confidence  1/5 — [PRD Section 7 source — confirmed or updated at Demo Day]  ⚠ risk flagged
Effort      2/5 — [what it takes given current team + capacity check]
Score       2.5 — (5×1)/2
Gate (if Next) — moves to Now when [condition]

### Sub-tasks
- [ ] [ID].1  [task]
- [ ] [ID].2  [task]

### Cycle review  (fill at review date)
- Shipped:
- Learned:
- New PRD tasks:
```

## Failure States

- Everything scores 5 and Now fills with 6–8 items — if nothing gets cut, the scoring is broken; enforce the 2–3 cap
- Kill list not imported from PRD Section 5 "Won't have" — killed items resurface in standups; the week's discipline collapses
- Built once and never revisited — a static doc, not a living Kanban; the value is the cycle review, not the first build
- No cycle length set — founders work everything in parallel and Now/Next/Later dissolves
- Confidence scores inflated to H with no evidence — if every item is High confidence, the scoring is broken; Confidence must reflect what is in PRD Section 7, not aspiration

## Founder Callouts

- **AquaPot, Xplarion, Bimefy** — long-cycle/hardware: cycles run 4–12 weeks. Define a testable increment per type (field pilot, client sim, regulatory checkpoint); Effort reflects procurement and build reality.
- **AFFIRMED, Time to Play, TimeBridge** — solo founders: Now cap 1–2. Effort must be honest about solo capacity or cycles overload and produce nothing reviewable.
- **Aika** — marketplace: supply and demand don't move together. Two parallel Now tracks, one item each, so the chicken-and-egg constraint stays visible.
