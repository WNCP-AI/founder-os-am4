---
title: "Prototyping Guide — Day 3"
session: "C.3"
session_type: "Workshop"
owner: "Rita"
date: "Jun 17"
time: "2:00–4:45"
summary: "In-session guide and skill for the second prototype build — takes Peer Court feedback and PRD v2 to refine or rebuild the Day 1 prototype, attaches a lightweight feedback mechanism, and closes with a next-cycle hypothesis."
---

# Prototyping Guide — Day 3

## Time

**C.3 Second Prototype Build:** Wed Jun 17, 2:00–4:45 (2h 45m + optional AI Clinic). Follows the Metrics Workshop (C.2, 12:00–1:00). Founders arrive with Peer Court notes from C.1 (morning) and a draft PRD v2 with OKRs from C.2.

## Inputs

- **Peer Court feedback** (from C.1, Wed morning) — specific critique on the Day 1 prototype and PRD
- **PRD v2 draft** (from C.2) — with OKRs and metrics that define what "done" looks like for the refined prototype
- **Day 1 prototype** (from A.5, Mon Jun 15) — saved to `4_Dev_Projects/` project folder as `prototype-day1.md`; Day 3 refines or rebuilds from this baseline

## Founder Prerequisites

- Day 1 prototype saved as `prototype-day1.md` in the `4_Dev_Projects/` project folder — without it, Day 3 loses the refinement framing and starts from scratch
- Peer Court notes captured with at least one specific change and one thing to keep — vague feedback produces a vague refined prototype
- PRD v2 draft in progress with at least a draft OKR — defines the "pass" bar the refined prototype is tested against
- PRD v2 §7 (assumptions to test) exists as at least a stub by end of C.2 (1:00 PM) — C.3 Phase 3.3 links the next-cycle hypothesis into §7; if §7 doesn't exist at Day 3 start, that link is lost

## Outcomes

**Primary (max 2)**
- Founder can run the Day 3 skill against their Peer Court notes and PRD v2 and produce a refined or rebuilt prototype with a documented change from Day 1 — without facilitation
- Founder can attach a lightweight feedback mechanism to their prototype and describe how the results will drive their Sprint 3 decision (double-down, pivot, or kill)

**Secondary (max 2)**
- Founder leaves with a written next-cycle hypothesis: "Based on [what we learned], Sprint 3 will test [X] by [how]"
- Refined prototype and feedback mechanism are saved to the `4_Dev_Projects/` project folder and linked in PRD v2 §7 (assumptions to test)

## Founder Operating Process

> OPEN — process below is proposed, not sourced from agenda or deliverables spec. Confirm with Rita before building the skill and guide.

#### Phase 1 — Triage the Feedback
- **1.1** — Open Peer Court notes; identify the single change with the highest signal — not all feedback is equal, pick the one that, if true, changes the prototype most
- **1.2** — Check that change against PRD v2 OKRs: does it move toward the defined "done"? If yes, it goes in. If not, note why and park it for a later cycle.
- **1.3** — Write the refined scope: "Day 1 tested [X]. Day 3 changes [Y] because Peer Court said [Z]."

#### Phase 2 — Build the Refinement
- **2.1** — Open `prototype-day1.md` from the `4_Dev_Projects/` project folder and launch the Day 3 skill with Peer Court notes and PRD v2 as inputs
- **2.2** — Skill generates the refined scaffold — same tool as Day 1 (default) or a new tool if the P.3.1 routing skill recommends switching based on the changed scope [proposed skill behavior — OPEN: Day 3 skill not yet built; handoff to P.3.1 TBD]
- **2.3** — Build until the changed element is testable by a real person; stop when the core change is demonstrable, not when the whole product feels done

#### Phase 3 — Add the Feedback Mechanism and Close the Loop
- **3.1** — Choose a feedback format: short survey (tool per P.3.1 tool list — OPEN), structured review prompt (runs in Claude Code), or an observation script for a live demo
- **3.2** — Attach the mechanism to the prototype — a link at the end of the flow, a follow-up message, or a facilitator-run script
- **3.3** — Write the next-cycle hypothesis and save to the `4_Dev_Projects/` project folder; link it in PRD v2 §7

## Format

In-session guide used during C.3.

Delivered as:
- **Day 3 prototyping skill** (markdown, runs in Claude Code) — takes Peer Court notes + PRD v2 as inputs, generates refined prototype scaffold; includes feedback-mechanism templates (survey, review prompt, observation script); calls P.3.1 routing skill when changing tools
- **In-session reference** (format TBD) — skill output or printed one-pager usable without a facilitator during the session

> OPEN — pending Damien: whether any post-week reference ships alongside this (PDF, Student Hub page, or skill output only) and whether that lives here or under P.3.

## Failure States
- Peer Court feedback wasn't specific — "make it better" gives the Day 3 skill nothing to work with and the refined prototype is indistinguishable from Day 1
- Feedback mechanism is skipped — prototype is refined but the learn loop doesn't close; the next-cycle hypothesis has no data behind it
- Day 1 prototype not in your `4_Dev_Projects/` project folder — Day 3 skill has no baseline to diff against; the "what changed and why" documentation is lost before Demo Day

## Founder Callouts

- **AquaPot** — physical hardware (water treatment): feedback mechanism is a structured deck or spec review (not a user-click survey); who reviews it — municipal engineer, DOE program officer, or procurement contact — and what structured questions do they answer?
- **Bimefy** — SaaS sold to construction buyers: feedback mechanism is a structured demo walkthrough with a GC or engineering contact, or a task-completion test against the BIM integration mock
- **Xplarion** — analytics SaaS for mining buyers: feedback mechanism is a structured expert review with a geologist or mining exploration contact evaluating the analytical output (data quality, result interpretation, drill target usefulness)
- **Data Love Co.** — their prototype is likely a dashboard or data pipeline mock; the feedback mechanism must be distinct from the data interface being tested — use an observation script or structured expert review with a nonprofit data lead, not a survey
- **Aika** — two-sided marketplace: feedback mechanism should cover both supply and demand sides, or explicitly pick one and flag the other as a Day 3+ gap
