---
name: util_get_inputs
description: >
  The single place that tells a skill where its inputs come from. Pipeline skills call this at the
  start of a run to resolve "what should I read, and from where" for the task at hand, instead of
  hardcoding input locations. Routes to company ground truth (via util_get_company_info), the
  founder profile (via util_get_user_info), standardized discovery evidence
  (5_Library/sources/processed/), the founder's session template (1_Product_Week/<session>/),
  upstream pipeline outputs (2_Outputs/.agents/<session>/), and any additional configured sources
  (.env, connected data, MCPs). Triggers whenever a skill needs to gather context/inputs, or the
  founder asks "what does this exercise read".
---

# util_get_inputs — Input Lookup

You are the central map of where inputs come from. Pipeline skills call you before they run so
they never hardcode where to read. You return the ordered list of input sources for the task,
how to access each, and which are primary vs. supplementary. The calling skill then pulls the content
itself using the access methods below — you return the map, not the content.

## Why this exists

Outputs are deterministic — each skill writes to one known place, hardcoded in the skill. Inputs
are not. A value prop can draw on discovery evidence, company ground truth, the founder's own
profile, a prior output, or a source we add later (a `.env` value, a connected data source, an
MCP). Skills ask you rather than assume, so when a new source type appears we register it here
once instead of editing every skill.

## Access methods — how to read each source type

| Source | How to access |
|---|---|
| Company ground truth | call `util_get_company_info` (`get()`) — never read `0_Company/` directly |
| Founder profile | call `util_get_user_info` (`get()`) — never read `0_User/` directly |
| Discovery evidence | read every file in `5_Library/sources/processed/` (the standardized A.2 output) |
| Founder's session template | read the working template in `1_Product_Week/<session>/` (human-owned; may be blank or partly filled) |
| Upstream pipeline output | read `2_Outputs/.agents/<upstream-session>/<File>.md` |
| Configured / external | a `.env` value, connected data source, or MCP — see "Registering a new source" |

## Interface

- `get(task)` → return the input map for `task` (rows below): each source tagged **primary** or
  **supplementary**, with its access method from the table above. The calling skill pulls from each.
- `get()` → return the whole map (all tasks).

Return the map only. You don't gather content; the calling skill does, via the access methods.

## The input map — task → sources

Sources are tagged **primary** (shapes a strong result) or **supplementary** (enriches). A
missing primary source is never a stop — the calling skill recovers it with the founder (see
*When a primary input is missing* below).

| Task (skill / session) | Primary | Supplementary |
|---|---|---|
| `value-proposition` (A.3-Value-Prop) | discovery evidence · company ground truth · `A.3-Value-Prop` session template | founder profile · configured sources |
| `user-persona` (A.3-User-Persona) | `A.3-Value-Prop` output · discovery evidence · company ground truth · `A.3-User-Persona` session template | founder profile |
| `jtbd` (A.4-JTBD) | `A.3-Value-Prop` output · `A.3-User-Persona` output · company ground truth · `A.4-JTBD` session template | discovery evidence |
| `jtbd-prioritizer` (A.4-JTBD) | `A.4-JTBD` output · company ground truth | — |
| `draft-prd` (A.5-PRD-v1 / C.3-PRD-v2) | `A.3-Value-Prop` · `A.3-User-Persona` · `A.4-JTBD-Prioritized` outputs · company ground truth · session template (`A.5-PRD-v1`, or `C.3-PRD-v2` in v2 mode) · `A.5-PRD-v1` output (v2 mode — v2 extends v1) | v2 mode: `C.2-Metrics-OKR` output |
| `spec-docs` (A.5-Prototyping-1) | `A.5-PRD-v1` output · company ground truth · spec-doc templates (`1_Product_Week/A.5-Prototyping-1/templates/`) | founder profile |
| `metrics` (C.2-Metrics-OKR) | `A.5-PRD-v1` output · `A.4-JTBD-Prioritized` output · company ground truth · `C.2-Metrics-OKR` session template | discovery evidence |
| `customer-discovery-coach` (pre-A.3) | discovery evidence · company ground truth | founder profile |

`ingest-sources` (A.2) is intentionally absent: it produces evidence (reads `5_Library/sources/raw/`,
writes `5_Library/sources/processed/`) rather than consuming pipeline inputs, so it does not call this lookup.

## When a primary input is missing — recover, never stop

A skill never stops because an upstream document or source is absent. Founders arrive with
different histories — some have run earlier sessions, some bring their own research, notes, or
tools from elsewhere. So when a primary input is missing, recover *with* the founder instead of
gating:

1. **Say what's missing, plainly.** "I don't have your [value prop / persona / PRD v1] from a
   previous session on file."
2. **Offer the choice — ask the founder.** In one question: do they have their own material for
   this (notes, research, a doc from another tool) they'd like to use, or would they rather answer
   a few quick questions to fill the gap here?
3. **Use what they bring, or guide them through the gap.** If they share material, use it. If they
   pick the questions, pull the core questions from the upstream skill that would have produced the
   missing input (e.g. the value-prop skill's problem/customer questions) and walk them through
   just those — enough to continue, not the whole exercise.
4. **Continue.** Proceed using what you gathered. Flag any input that's still thin so the founder
   knows that part is lighter than usual.

This applies to every pipeline skill. A primary input shapes a strong result, but its absence is a
recovery path, never a dead end.

### Special case — discovery evidence is empty (`5_Library/sources/processed/`)

Ingestion is **optional**, so an empty `processed/` folder is normal, not an error. When a skill
wants discovery evidence and finds none:

1. **Offer ingestion first.** "I don't see any processed discovery data. Want to run the ingestion
   workflow (`ingest-sources`) to bring in interviews, notes, research, or field docs first?"
2. **If yes** → pause here, let the founder run `ingest-sources`, then resume — re-read
   `5_Library/sources/processed/` once it's populated, and continue.
3. **If no** → proceed on what's already known: `0_Company/` ground truth (via
   `util_get_company_info`) and any prior deliverables in `2_Outputs/.agents/`. Note the stage is
   running lighter on direct evidence; never block.

## Registering a new source

When inputs start coming from a new place (a `.env` value, a connected data source, an MCP), add
it to the access-methods table and to the relevant task rows above — once, centrally — rather than
teaching each skill about it.

## Guardrails

- You return the map, not the content — the calling skill reads each source via its access method.
- Always route `0_Company/` and `0_User/` reads through their utilities; never name those files directly.
- Primary vs. supplementary matters: a missing **primary** source is a recovery path, not a stop —
  the calling skill tells the founder what's missing and gathers it with them (see *When a primary
  input is missing*). Supplementary sources enrich but are never expected.
- Keep this map current — it is the one place input locations live, so skills don't hardcode them.
- Outputs are not your concern — each skill hardcodes its own single output destination.
