---
title: "Prototyping Guide — Day 1"
session: "A.5"
session_type: "Workshop"
owner: "Rita"
date: "Jun 15"
time: "2:15–5:00"
summary: "In-session guide and skill for building a first testable prototype from PRD v1 — scopes the prototype, selects the right tool via the P.3.1 routing skill, and produces a testable first artifact by end of day across software, hardware sim, and workflow mock paths."
---

# Prototyping Guide — Day 1

## Time

**A.5 Prototype Build:** Mon Jun 15, 2:15–5:00 (2h 45m flex). Follows PRD v1 completion earlier in A.5. First 15–30 minutes may overlap with PRD v1 wrap-up; usable prototype build time is approximately 2–2.5 hours.

## Inputs

- **PRD v1** (from A.5, same session) — problem statement, primary user, and one scoped feature to prototype
- **JTBD prioritized list** (from A.4) — anchors the prototype to the highest-priority job, prevents scope creep — OPEN: confirm whether the skill reads this directly or relies on PRD v1's synthesis of it

## Founder Prerequisites

- PRD v1 complete with a problem statement, user, and at least one feature scoped — without these the prototype has no scope and A.5 becomes a brainstorm
- Founder OS environment running (for the technical track); a browser is sufficient for the non-technical track (Google AI Studio, Stitch, or equivalent)

## Outcomes

**Primary (max 2)**
- Founder can run the Day 1 skill against their PRD v1 and produce a working first prototype or testable mock — without asking for help
- Founder can write one sentence describing what their prototype tests and what a "pass" looks like — so Peer Court and Day 3 have a hypothesis to refine, not just an artifact to polish

**Secondary (max 2)**
- Founder has used the P.3.1 routing skill to select their tool — not by habit or default
- Prototype is saved to the `4_Dev_Projects/` project folder and linkable for Day 3 reference

## Founder Operating Process

> OPEN — process below is proposed, not sourced from agenda or deliverables spec. Confirm with Rita before building the skill and guide.

#### Phase 1 — Scope
- **1.1** — Read PRD v1 problem statement and the top JTBD item; write one sentence: "This prototype tests whether [user] can [do the job] using [scoped feature]"
- **1.2** — Choose prototype form: working software, workflow mock, hardware deck/3D spec, or simulated service; run the P.3.1 routing skill [OPEN — not yet built] if unsure which tool to use
- **1.3** — Cap scope to one flow, one feature, one user action — anything additional is Day 3

#### Phase 2 — Build
- **2.1** — Open the selected tool; run the Day 1 skill with PRD v1 as input — it generates the prototype scaffold (code prompt, mockup spec, or deck outline depending on form) [OPEN — skill not yet built; scaffold behavior TBD]
- **2.2** — Iterate until the prototype is testable: a real person could interact with or review it and give a yes/no on the core hypothesis
- **2.3** — If stuck, return to the P.3.1 routing skill before switching tools — changing tools mid-build without a reason wastes the remaining session time

#### Phase 3 — Capture
- **3.1** — Save the prototype artifact (link, file, or deck) to the `4_Dev_Projects/` project folder as `prototype-day1.md` (or a linked reference file by that name for non-text artifacts); C.3 locates the baseline using this filename
- **3.2** — Write the one-sentence hypothesis ("My Day 1 prototype tests [X]. A pass means [Y].") and save it alongside the prototype — this feeds into Peer Court (C.1); Peer Court feedback then feeds the Day 3 guide (C.3)

## Format

In-session guide used during A.5. Delivered as:
- **Day 1 prototyping skill** (markdown, runs in Claude Code) — takes PRD v1 as input, generates prototype scaffold, calls the P.3.1 routing skill for tool selection; branches by prototype form (software / hardware / workflow mock)
- **Founder reference card** (one-page markdown) — scope checklist, form decision guide, and the one-sentence hypothesis template; founders keep it and bring it to Day 3

> OPEN — pending Damien: whether the reference card is embedded in the skill output or ships as a separate standalone doc.

## Failure States
- PRD v1 has no single scoped feature — prototype scope stays undefined and 2.5 hours disappear without a testable artifact
- Founder picks a tool by habit rather than using the P.3.1 routing skill — technical founders over-engineer, non-technical founders pick the wrong surface; both waste build time
- Prototype isn't saved to your `4_Dev_Projects/` project folder — Day 3 and Peer Court have no baseline to reference

## Founder Callouts

- **AquaPot** — physical hardware (water treatment): prototype form is a deck spec or 3D model brief; the skill must treat this as a first-class path, not a fallback
- **Bimefy** — SaaS sold to construction buyers: prototype form is a working app or Figma flow demonstrating BIM integration, not a deck spec; "construction" describes the buyer
- **Xplarion** — analytics SaaS for mining buyers: prototype form is a data dashboard or workflow mock (geological data input → insight output); use the data-interface scope path
- **Data Love Co.** — prototype may be a dashboard mock or simulated data pipeline; scope checklist must include "data interface" as a valid prototype form
- **Aika** — two-sided marketplace: Day 1 caps to one side only; cohort data (6 paying providers, 200 weekly visitors) indicates supply-side is the active constraint — default to supply-side first unless PRD v1 argues otherwise
- **TimeBridge** — two distinct use cases (memory capture vs. legacy planning) produce entirely different prototypes; the one-sentence hypothesis template must force a use-case choice before building starts
- **AFFIRMED** — three-way GTM ambiguity (B2C individual professional, B2B enterprise HR, referral marketplace); PRD v1 must commit to one primary user before the skill runs; do not proceed without a single user specified
