---
title: "5_Library/discovery — Customer Discovery Assets"
phase: "P.1 (pre-week)"
updated: 2026-06-12
---

# Customer Discovery Assets

**Phase:** P.1 — Pre-Week (complete at least 5 customer interviews before the Jun 15 kickoff)

These assets support founders in moving from assumptions to evidence before building. The skill (AI coach) and tracker are the two tools founders actually use; the deck and one-pager explain the sequence.

## Contents

| Path | Type | What it is |
|---|---|---|
| `Customer-Discovery-One-Pager.md` | Markdown | Founder-facing overview explaining the two-tool kit and 6-step sequence |
| `Customer-Discovery-Tracker.xlsx` | Binary | Five-tab Excel tracker; hypotheses entered once in the Guide tab, all other tabs populate automatically |
| `founder-kit/Customer-Discovery-Kit.zip` | Binary | Packaged zip of the kit distributed to founders |
| `founder-kit/Customer-Discovery-Tracker.xlsx` | Binary | Tracker copy distributed inside the founder kit |
| `founder-kit/START-HERE.md` | Markdown | Founder-facing instructions: how to install the skill, run a coaching session, and use the tracker |

> **The coach skill** ships with the OS at `.agents/skills/wncp-ai/3-customer-discovery-coach/` — find it with `find-skills` (say "get me started" or ask for customer discovery help). `founder-kit/START-HERE.md` covers running a coaching session and using the tracker.

## Session / Phase

| Phase | Activity |
|---|---|
| P.1 (pre-week) | Founders install the coach skill, run a coaching session, enter hypotheses in the tracker, and complete 5+ interviews before Jun 15 |
| A.4 (week, JTBD session) | Discovery patterns feed into JTBD statement construction |
| A.5 onwards | JTBD → PRD → Roadmap; this data is the upstream evidence chain |

## Founder Flow

1. Install `customer-discovery-coach.skill` in the Claude app (Customize → Skills)
2. Run a coaching session → get ranked hypotheses + interview guide
3. Paste hypotheses into the Guide tab of `Customer-Discovery-Tracker.xlsx`
4. Run interviews; log responses in the Question Log
5. Review the Pattern Summary tab after every 5 interviews
6. Bring findings to Product Week — feeds directly into JTBD (session A.4)
