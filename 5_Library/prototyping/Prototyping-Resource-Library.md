---
title: "Prototyping Resource Library"
session: "P.3.1"
session_type: "Self-Serve"
owner: "Damien"
date: "Jun 14"
summary: "Curated tool library with descriptions, YouTube links, and a routing skill — the shared foundation both prototyping sessions draw on for tool selection, and a standalone reference founders keep and reuse post-week."
---

# Prototyping Resource Library

## Time

Published as part of the Student Hub (P.3) by **Jun 14** (INDEX build deadline). Not distributed as a pre-week send — lives at a persistent URL on the Student Hub throughout Jun 15–18 and post-week. Both A.5 and C.3 prototyping sessions link directly to it. Dependency gate for A.5 (Jun 15 AM): P.3.1 must be live before the first prototyping session.

## Inputs

None — standalone library. Curated from Damien's prior program experience (MLT20 Buildathon, Access Mode prior cohorts). No founder artifact required to use it.

## Founder Prerequisites

None — designed as an entry point for any founder regardless of technical level. The routing skill handles qualification; founders don't need to know the tool landscape before they arrive.

## Outcomes

**Primary (max 2)**
- Routing skill is live and functional: asks founders qualifying questions and returns a recommended tool with rationale — OPEN: exact question set (proposed: product type, technical level, prototype goal), question count, and response format pending owner sign-off
- Every tool entry includes: name, description, best-fit use case, and at least one quick-start link — OPEN: field schema and link requirements pending owner review

**Secondary (max 2)**
- Founders can browse the full tool list without the skill, to compare options independently
- Library page is linked from both the A.5 and C.3 session pages on the Student Hub

## Founder Operating Process

> OPEN — process below is proposed, not sourced from agenda or deliverables spec. Confirm with owner before building the routing skill.

#### Phase 1 — Use the Routing Skill
- **1.1** — Open the library page on the Student Hub and launch the routing skill
- **1.2** — Answer the qualifying questions [proposed — OPEN: question wording, categories, and option sets TBD per owner sign-off on routing skill design]
- **1.3** — Review the recommended tool and rationale; follow the linked quick-start resource before the session if time allows

#### Phase 2 — Browse Independently (if routing didn't land)
- **2.1** — Scan the tool list by category (no-code web, AI-assisted code, design/mockup, hardware sim, survey/feedback)
- **2.2** — Use the use-case fit descriptions to select an alternative; note that switching tools mid-week carries a setup cost

## Format

A page on the Student Hub (P.3) containing:
- **Routing skill** (markdown, runs in Claude Code) — qualification questions → tool recommendation with rationale; called from both the A.5 and C.3 prototyping skills
- **Tool library** (structured list on the page) — name, description, best-fit use case, quick-start link(s) per tool

> OPEN — pending Damien: tool list is not yet finalized. Expected categories and candidates:
- No-code web: Google AI Studio, Stitch
- AI-assisted code: Claude Code, Cursor, Bolt
- Design / mockup: Figma, v0, Lovable
- Hardware / physical sim: deck spec conventions, 3D model brief template
- Survey / feedback: Tally, Google Forms

## Failure States
- Routing skill recommends a tool the founder can't access or set up quickly — they stall at tool selection instead of building
- Tool entries ship without quick-start links — founders land in an unfamiliar tool with no entry point and the library doesn't close the gap
- Library page isn't linked from A.5 and C.3 session pages in the Student Hub — founders don't discover it mid-session when they need it most

## Founder Callouts

- **AquaPot** — physical hardware (water treatment): routing skill must surface deck spec and 3D model brief as first-class outputs; the hardware-sim category must have real content at launch
- **Bimefy** — SaaS sold to construction buyers: routing skill must classify as software and recommend Figma, v0, or working-code path; "construction" describes the buyer, not the prototype form
- **Xplarion** — analytics SaaS for mining buyers: routing skill must classify as data/software and recommend a dashboard mock or analytical workflow demo; "mining" describes the buyer, not the prototype form
- **Data Love Co.** — data/nonprofit: routing skill should recognize "dashboard mock" and "data pipeline simulation" as prototype goals and recommend accordingly
- **Aika** — two-sided marketplace: routing skill must ask "which side of your marketplace are you testing?" before recommending a tool; routing without surfacing the side-selection constraint will produce an unusable scope
