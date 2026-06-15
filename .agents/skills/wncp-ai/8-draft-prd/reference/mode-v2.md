# Mode v2 — PRD Day 3 (All 9 Sections)

Load this when the founder selects PRD v2. This mode extends PRD v1 — it carries §§ 1–6
forward and adds four new sections (Market Dynamics, Assumptions & Risks, OKRs, Roadmap).
The founder fills in their `C.3-PRD-v2` template by hand; PRD v1 is **kept, never overwritten**.

**Core rules:**
- Read files, pre-fill, confirm gaps — do not re-run prior exercises.
- Push back on weak answers once before accepting. A weak answer sounds good but doesn't hold up
  under one follow-up question. Surface what the files say, then challenge the founder to make it
  stronger. One pushback per field — don't interrogate, but don't just collect either.
- Present one section at a time. Wait for confirmation before moving to the next.
- Do not show two sections in the same message.

---

## Carry-Forward: Sections 1, 3, 4, 5, 6 (from PRD v1)

Read `2_Outputs/.agents/A.5-PRD-v1/PRD-v1.md` for the base. Present one section at a time.
For each carried section, ask: "Does this still hold, or has anything shifted?" One exchange —
collect any correction, then move on.

Note: the v2 template renumbers the sections (v1 §1 Company+VP → v2 §1 Company+Problem; v1 §2
Target User → v2 §3 Target User; v1 §3 Jobs → v2 §4 Jobs; v1 §4 Features → v2 §5 Features;
v1 §5 Prototype → v2 §6 Prototype). Always refer to sections by name, not number.

---

## Company + Problem (v2 §1) — two new fields

Carry forward Company name, Value proposition, and Why us from PRD v1. Add two new fields —
ask one at a time, wait for the answer before moving to the next.

### Problem evidence

Surface the sharpest quote or stat from the A.3-User-Persona output or any discovery signals
in the A.3-Value-Prop or JTBD-Prioritized outputs. Present it: "Is this the sharpest signal
from your customer discovery, or is there a better quote or data point?"

Wait for confirmation before asking the next field.

### Why now

Only after Problem evidence is confirmed — ask directly: "What changed recently — in technology,
behavior, or the market — that makes this the right moment to build this?"

**Pushback signals:**
- "AI makes this easier" → challenge: "That's true for every AI product right now. What
  specifically changed for *this customer* in *this workflow* that didn't exist 2 years ago?"
- Generic trend → challenge: "What's the event or shift that makes this year different from
  last year for your specific customer?"

---

## Market Dynamics (v2 §2 — new section)

Pull signals from the A.3-User-Persona output (tools customers mentioned, how often the pain
occurs, cost or time they named) and from the A.3-Value-Prop output (the alternative / workaround
they're replacing). Present a draft of market context and competitive gaps.

Ask: "What makes this hard to copy once you have traction?"

**Pushback signals for defensible edge:**
- "Our distribution" → challenge: "A larger competitor with an existing founder community could
  replicate that. What do you have that compounds over time — data, relationships, switching costs?"
- "Our technology" → challenge: "LLMs are available to everyone. What's the layer on top that's
  specific to you?"
- "First mover" → challenge: "First mover only matters if there's a switching cost or network
  effect. What locks users in after they've tried it once?"

Do not ask for TAM — ask for the signal and the defensible edge.

---

## Target User (v2 §3) — one new field

Carry forward Who, Situation, High-value need, and Current behavior from PRD v1. Add one new
field:

**Customer evidence:** Pull the best direct quote from the A.3-User-Persona output. Present it:
"Is this the sharpest thing a customer said about this problem, or is there a better one?"

---

## Jobs to Be Done (v2 §4) — one new column: Rationale

Carry forward job statements, AI roles, and priority from PRD v1. Add a Rationale column — pull
from "Why #X" fields in the A.4-JTBD-Prioritized output. Present and confirm. No new questions
needed for this column.

---

## Features (v2 §5) — versioning layer added

Carry forward the feature table from PRD v1 (Feature, Job #, What it does, Scope boundary,
Priority). Add a versioning layer:

Map: Must have → V0.1, Nice to have → V0.2, Future → V1.0.

Present the mapping and ask: "Does this versioning feel right, or should anything move?"
Accept any adjustment.

---

## Prototype (v2 §6)

Carry prototype as-is from PRD v1. Add one note: "Your hypothesis here becomes Assumption #1
in Assumptions & Risks."

---

## Assumptions & Risks (v2 §7 — new section)

Internally derive the assumption table from:
1. The Prototype hypothesis from PRD v1 → Assumption #1, type: Solution
2. "Watch out for" fields in the A.4-JTBD-Prioritized output → Solution assumptions
3. Claims in PRD v1 that have no supporting discovery evidence → Market or Problem assumptions
4. Any risk signals surfaced in the JTBD-Prioritized output → additional seeds

Do not explain this derivation to the founder. Just present the completed table with Type,
Assumption, and "What could kill it" already filled. Then go through assumptions one at a time —
use AskUserQuestion per row with **High** / **Medium** / **Low** confidence options.

Do not ask about multiple assumptions in the same message.

**Confidence key (for the founder's reference):**
- **H — High:** Supported by multiple customer conversations or data points
- **M — Medium:** Supported by one or two signals, but not yet confirmed at scale
- **L — Low:** Still a hypothesis — no customer evidence yet

Do not suggest how to test — testing methodology is handled separately and requires Mom
Test-quality questions, not hypotheticals.

---

## OKRs (v2 §8 — new section, carries from C.2)

Check for `2_Outputs/.agents/C.2-Metrics-OKR/Metrics-OKR.md`.

**If the file exists:** Transfer Objective + Key Results directly from it. Do not ask the
founder to re-derive them.

Then go through KRs one at a time — ask: "Which assumption from your Assumptions & Risks does
[KR] prove or disprove?" Wait for the answer before asking about the next KR. Always refer to
it as "Assumptions & Risks" — never by section number.

**If no OKR file exists:** Tell the founder: "Complete the C.2 Metrics Workshop first — OKRs
should come from that exercise, not be guessed here." Do not proceed past this section until
the OKR file exists.

Never guess OKRs — they must come from the C.2 output.

---

## Roadmap (v2 §9 — new section)

Derive three phases from the versioned features + OKR success criteria:

- **V0.1 — Prototype:** Must have features (V0.1 versioning). Success = hypothesis from Prototype
  section confirmed or invalidated.
- **V0.2 — Validated MVP:** Nice to have features (V0.2). Success = KR1 + KR2 hit.
- **V1.0 — Product:** Future features (V1.0). Success = OKR objective met.

Present the draft phases. Ask one question: "Target dates — when do you aim to complete each phase?"

---

## Validation — before moving to Closing

Before handing off to the Closing section, check:

| Criterion | Pass | Fail → one probe |
|---|---|---|
| Problem evidence is a direct quote or stat | Specific, verifiable signal | "That's a paraphrase — do you have the actual quote or a specific number?" |
| Why now is a specific change | Named event or shift | "What specifically changed? 'AI' or 'the market' alone isn't enough." |
| Defensible edge answers the copycat question | Not just distribution or first mover | "What compounds over time once you have traction?" |
| Every Must Have feature has a version tag | V0.1, V0.2, or V1.0 | "Where does [feature] belong in V0.1 / V0.2 / V1.0?" |
| OKR file was used or section is blocked | Never guessed | Block the section if no C.2 output exists |
| Roadmap phases set after OKRs are locked | Phases reference KR success criteria | "Does each phase's success criteria tie back to a KR?" |

Ask one probe at a time. Wait for the answer. One pass only — don't loop.

When all nine sections hold up, return to the Closing in the SKILL.
