---
name: am4-spec-docs
description: >
  AM4 WNCP AI guided exercise — turns a finished PRD into the spec documents an AI builder needs
  (TECH_STACK, UI, DESIGN, DATA, API). Use when: "set up my spec docs", "tech stack doc", "generate
  my spec files", "what files does my AI builder need", "prep my prototype build", "create
  TECH_STACK / UI / DATA / API", or "spec out my prototype". Make sure to use this skill whenever
  the founder is moving from their PRD to building a prototype and needs the supporting spec files —
  even if they don't explicitly say am4-spec-docs.
---

# Spec Docs Exercise

A guided exercise. The founder already has a PRD. You help them turn it into the small set of spec
documents an AI builder reads, so it builds the right thing the first time — one document at a time,
grounded in their PRD, using the prototyping templates and their built-in "Ask the LLM" prompts. You
only build the documents their chosen build path actually needs.

The PRD is the only required input; TECH_STACK is required for any build. UI, DESIGN, DATA, and API
are added based on the build lane. DESIGN is normally generated for the founder by a design tool
(Claude Design / Stitch), not hand-written.

## Phase 0 — Resolve and load inputs

Call **`util_get_inputs`** (`get("spec-docs")`) to get this exercise's input map, then pull each
source via the access method it returns. For this task:

**Primary:**
- **A.5-PRD-v1 output** *(primary)* — read `2_Outputs/.agents/A.5-PRD-v1/PRD-v1.md`. This is the
  founder's product spec; everything here derives from it.
- **Company ground truth** *(primary)* — via `util_get_company_info`.
- **Spec-doc templates** *(primary)* — the six templates in
  `1_Product_Week/A.5-Prototyping-1/templates/` (`PRD.MD`, `TECH_STACK.MD`, `UI.MD`, `DESIGN.MD`,
  `DATA.MD`, `API.MD`). Each template carries its own fill-in structure, an `## Ask the LLM` question
  set, and a `## Done when` checklist — you drive each document from these.

Never read `0_Company/` directly. Always go through the utility.

**If the PRD is missing,** don't stop — recover with the founder (see `util_get_inputs` → *When a
primary input is missing*). Tell them you don't have their PRD on file, then ask whether they have
one (or an equivalent product spec) to paste, or want to run the PRD exercise (`am4-prd`) first. The
spec docs need a problem, a user, and at least one scoped feature to build from.

Once inputs are loaded, say one sentence: "I've got your PRD — I'll use it to spin up the spec files
your builder needs, so you're not writing them from scratch." Then move to lane selection.

## Phase 1 — Pick the build path

Before generating anything, use **AskUserQuestion** to set the build lane — it decides which docs you
create:

- **Frontend-first** — "A clickable front-end or landing page (Stitch, Claude Design). No backend."
- **Full web app** — "A working web app with accounts and data (Google AI Studio, Lovable)."
- **Mobile** — "A mobile app, PWA-first (Bolt, Replit)."
- **Full stack** — "Engineering-grade build in a coding agent (Claude Code, Codex)."

If the PRD clearly implies a lane (e.g. it needs user accounts and stored data, so not
frontend-first), recommend that lane in the question and say why in one line. The founder still
chooses.

Map the lane to the document set:

| Lane | Required | Recommended | Skip |
|---|---|---|---|
| Frontend-first | TECH_STACK | UI (if visual-heavy), DESIGN (via tool) | DATA, API |
| Full web app | TECH_STACK | UI, DESIGN, DATA, API | — |
| Mobile | TECH_STACK | UI, DESIGN, DATA, API (+ PWA notes) | — |
| Full stack | TECH_STACK | UI, DESIGN, DATA, API | — |

(The PRD is already done in every lane.)

## Phase 2 — Set up the build folder

The spec docs live with the build, so the AI builder reads them together.

1. Ask the founder for a short project name; slugify it (lowercase, hyphens).
2. Create `4_Dev_Projects/<slug>/` if it doesn't exist.
3. Copy the PRD in as `4_Dev_Projects/<slug>/PRD.MD`, shaped to the `PRD.MD` template. Filenames are
   ALL CAPS including the extension — `PRD.MD`, `TECH_STACK.MD`, etc. — always.

## Phase 3 — Generate each spec doc, one at a time

For each document the lane needs, in this order — **TECH_STACK → UI → DESIGN → DATA → API** — do:

1. **Open the matching template** in `1_Product_Week/A.5-Prototyping-1/templates/<DOC>.MD`. Read its
   structure, its `## Ask the LLM` prompts, and its `## Done when` check.
2. **Walk the founder through it**, grounded in their PRD. Pull every answer you can straight from the
   PRD; ask the founder only what the PRD doesn't already settle, using the template's `## Ask the
   LLM` questions — one question per message.
3. **Write the completed document** to `4_Dev_Projects/<slug>/<DOC>.MD`, following the template's
   structure with the founder's real answers (not the blanks).
4. **Check it against `## Done when`** before moving on. Then go to the next doc.

**DESIGN.MD is special.** It's normally generated for you. For any visual build, don't hand-write it —
tell the founder to generate it with Claude Design or Stitch (the template's `## How to generate this`
section has the steps), export it, and drop it in as `4_Dev_Projects/<slug>/DESIGN.MD`. Hand-fill it
only if they have no design tool.

**Only build what the lane needs.** Skip DATA.MD and API.MD entirely for a frontend-first build — say
so plainly rather than walking through empty docs.

## Closing — hand the founder their build

When the lane's docs are done:

1. Show a short list: which spec files now sit in `4_Dev_Projects/<slug>/`, and which (if any) the
   founder still needs to generate (e.g. DESIGN.MD via a tool).
2. Say:
   > "Your spec folder is ready. Open your build tool, point it at `4_Dev_Projects/<slug>/`, and tell
   > it to build the prototype from these specs — start with the one flow in your PRD's Prototype
   > section. The Prototyping Guide walks the rest."

Point them to the guide: `1_Product_Week/A.5-Prototyping-1/Prototyping-Guide.md`.

#### Quietly record the deliverable

Write a short index **silently** to `2_Outputs/.agents/A.5-Prototyping-1/Spec-Docs.md` — the build
lane, the project slug, and the list of spec files created (with their paths). Frontmatter
`type: spec-docs`, `session: A.5-Prototyping-1`. Don't announce the path.

## Guardrails

- One document at a time; one question per message. Never show two docs or bundle questions.
- Pull from the PRD first — never ask the founder something their PRD already answers.
- Only generate the docs the chosen lane needs. Frontend-first never gets DATA.MD or API.MD.
- DESIGN.MD is tool-generated — guide them to generate it; don't hand-write it unless they can't.
- Spec filenames are ALL CAPS including the extension, always: `PRD.MD`, `TECH_STACK.MD`, `UI.MD`,
  `DESIGN.MD`, `DATA.MD`, `API.MD`.
- A prototype stores no permanently-stored sensitive PII and handles no real payments — say so when
  DATA.MD or auth comes up.
- The spec files in `4_Dev_Projects/<slug>/` are the founder's to edit and feed their builder — they
  are the real deliverable. The `2_Outputs/.agents/` index is written silently, never announced.
- Resolve inputs through `util_get_inputs`; read `0_Company/` only through its utility.
- Don't re-run the PRD exercise — read the PRD, confirm, and build from it.

## Quick reference

| Lane | Docs you create (PRD already done) |
|---|---|
| Frontend-first | TECH_STACK · UI (if visual-heavy) · DESIGN (via tool) |
| Full web app | TECH_STACK · UI · DESIGN (via tool) · DATA · API |
| Mobile | TECH_STACK · UI · DESIGN (via tool) · DATA · API · PWA notes |
| Full stack | TECH_STACK · UI · DESIGN (via tool) · DATA · API |

| Item | Location |
|---|---|
| Templates | `1_Product_Week/A.5-Prototyping-1/templates/<DOC>.MD` |
| PRD input | `2_Outputs/.agents/A.5-PRD-v1/PRD-v1.md` |
| Founder's spec files | `4_Dev_Projects/<slug>/<DOC>.MD` |
| Deliverable index | `2_Outputs/.agents/A.5-Prototyping-1/Spec-Docs.md` |
