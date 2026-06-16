# PRD.MD — Product Requirements Document

The single source of truth for what you are building and why. Every tool, every build lane, and every AI you work with during prototyping reads from this doc first. If it is not here, the AI will invent it — and you will not like what it invents.

**Status:** Required

**Use it when:** All four build lanes — Frontend-first (Stitch, Claude Design), Full web app (Google AI Studio, Lovable), Mobile (PWA, Bolt, Replit), Full stack (Claude Code, Codex).

**Note on prior work:** If you completed session A.5-PRD-v1 earlier in the week, you already drafted a version of this doc. Start there. The skill at `.agents/skills/wncp-ai/8-draft-prd/SKILL.md` walks you through the draft step by step. This template is the prototyping-ready version — tighter, with a Prototype section the earlier draft does not have.

**Stage:** This prototype operates at stage one or two of a three-stage arc: vibe coding leads to AI rapid prototyping (where this session sits) leads to engineering-grade. Build accordingly — you are not writing production code.

---

## 1. Company & Value Proposition

<!-- guidance: Keep this section to three fields. The value proposition is one sentence in this format: "[Product] lets [user] [do the thing] without [the friction they hate]." Do not expand it here. -->

| | |
|---|---|
| Company name | <!-- Your venture's name exactly as you use it day-to-day --> |
| One-line product | <!-- What the product does, in plain language. Not a tagline. Example structure: "[Product] lets [user] [do the thing] without [the friction they hate]." --> |
| The change it creates | <!-- What is different in the user's life or work after they use it? One sentence. This is not a feature — it is the outcome. --> |

---

## 2. Target User

<!-- guidance: Describe one real person, not a demographic bucket. If you have done discovery calls, base this on the person who had the most acute version of the pain. Do not describe two user types here — pick the primary one. -->

| | |
|---|---|
| Who they are | <!-- One-line identity: role, context, defining characteristic. Example structure: "A [role] who [defining situation]." --> |
| Their context | <!-- What are they doing, or trying to do, when this problem shows up? Be specific about the moment, not the category. --> |
| The pain | <!-- What goes wrong, costs them, or frustrates them right now? State it plainly. If you heard a user say it in their own words during discovery, use that quote here. --> |

---

## 3. Job To Be Done

<!-- guidance: A "job to be done" is the thing the user is trying to accomplish — independent of any product. The format is: When [situation], I want to [goal], so I can [outcome]. Fill in one job only — the top-priority one your prototype will address. If you have a ranked JTBD list from A.4, copy the #1 job here. -->

**The single top job:**

> When _____________________________, I want to _____________________________, so I can _____________________________.

**The trigger:**

<!-- guidance: What specific event or moment causes the user to feel the job urgently? This is the moment your prototype must catch them. One sentence. -->

_______________________________________________

**Their current workaround:**

<!-- guidance: What do they do today instead of using your product? Name the tool, the behavior, or the manual step. This is what you are replacing. -->

_______________________________________________

---

## 4. Features

<!-- guidance: List every feature you are considering. Then ruthlessly mark priorities. A prototype only needs the Must-have features — everything else is Future. "Why it serves the job" forces you to connect each feature back to Section 3. If you cannot complete that column, the feature probably does not belong in the prototype. -->

| Feature | Why it serves the job | Priority |
|---|---|---|
| <!-- Name the capability in plain language --> | <!-- One sentence connecting it to the job in Section 3 --> | Must have |
| | | Must have |
| | | Nice to have |
| | | Nice to have |
| | | Future |
| | | Future |

### Not in scope

<!-- guidance: List what this prototype explicitly will NOT do. This is as important as the feature list. State it plainly so the AI builder does not add it. Common examples: user accounts and login, payment processing, email notifications, admin dashboards, third-party integrations. -->

- _______________________________________________
- _______________________________________________
- _______________________________________________

**Prototype guardrails — state these to your AI builder at the start of every session:**
- This prototype stores no permanently-stored sensitive PII.
- This prototype handles no real payments.

---

## 5. The Prototype

<!-- guidance: A prototype tests one hypothesis with the minimum set of features. Do not build everything in Section 4 — build the ONE flow that answers your riskiest question. Fill in each field below before you open any build tool. -->

**The one flow to build first:**

<!-- guidance: Describe the single user journey from start to finish. What does the user do, in what order, to accomplish the top job? Write it as steps. Three to five steps is usually right. -->

1. _______________________________________________
2. _______________________________________________
3. _______________________________________________
4. _______________________________________________
5. _______________________________________________

**The hypothesis:**

<!-- guidance: Complete this sentence exactly. Do not paraphrase the structure — the structure is doing work. "Observable result" means something you can see or measure after a user tries the flow: they completed it, they said a specific thing, they asked to use it again. -->

> This prototype tests whether [user] can [do the job] using [feature]. A pass = [observable result].

**The riskiest assumption:**

<!-- guidance: What is the one thing that, if it turns out to be wrong, kills the idea? Name it plainly. This is what you are actually testing — everything else is secondary. One sentence. -->

_______________________________________________

---

## Ask the LLM

Paste these into Claude, ChatGPT, or Gemini one at a time. Answer its follow-up questions before moving to the next prompt. Each prompt fills a specific section of this doc.

1. "I am a non-technical founder filling in a PRD for an AI prototyping session. My product is [describe it in 2-3 sentences]. Help me write the one-line product description for my PRD using this format: '[Product] lets [user] [do the thing] without [the friction they hate].' Ask me any questions you need before you write it."

2. "Here is my target user: [paste your Section 2 draft or describe them]. Write a one-sentence 'job to be done' for this user in this format: When [situation], I want to [goal], so I can [outcome]. Then tell me what their most likely current workaround is. Ask me questions if you are not sure."

3. "Here is my top job to be done: [paste from Section 3]. List 5 features a prototype could include to help the user accomplish this job. For each one, write one sentence explaining why it directly serves the job. Then mark each one Must have, Nice to have, or Future — where Must have means the prototype is useless without it."

4. "Based on the features I marked Must have: [list them]. What should this prototype explicitly NOT do? Give me a short 'not in scope' list I can paste into my PRD to prevent the AI builder from adding features I do not need."

5. "Here is my full top job and the must-have features: [paste]. Write the single user flow — 3 to 5 steps, from the moment the user opens the app to the moment the job is done. Then complete this hypothesis sentence for me: 'This prototype tests whether [user] can [do the job] using [feature]. A pass = [observable result].'"

6. "Here is my PRD so far: [paste the whole doc]. What is the single riskiest assumption buried in this PRD — the one thing that, if wrong, means the product does not work? Give me one sentence."

7. "Read my PRD and tell me: is there anything in the 'Not in scope' list that I probably forgot? What are the three most common things non-technical founders accidentally ask AI builders to build, that they later wish they had excluded from the prototype?"

8. "I have these Must-have features: [list them]. I only have 2.5 hours to build a prototype. Which single feature or interaction gives me the most evidence about whether this product idea works? Tell me what one flow to build and why everything else can wait."

---

## Done when

- [ ] Sections 1-3 are filled in — every blank has a real answer, not a placeholder.
- [ ] The Feature table has at least two Must-have features and a Not-in-scope list with at least three items.
- [ ] The Prototype section has a numbered flow, a completed hypothesis sentence, and a riskiest assumption.
- [ ] The prototype guardrails (no sensitive PII, no real payments) are acknowledged.
- [ ] You can read the hypothesis sentence aloud and a person who has never heard of your product understands exactly what you are testing.
