# Founder OS — Access Mode Cohort 4

A cloneable product workspace for the **Access Mode AI-Driven Product Week**
(Jun 15–18, 2026), built by [WNCP AI](https://wncp.ai). You run the whole week inside this
repo — and you keep it after.

It's an **agentic operating system**: a folder of markdown files, conventions, and skills
that an AI agent (Claude Code) reads and works in. You load it with your own customer
discovery data, then run the product pipeline against it — value proposition → user
persona → jobs-to-be-done → PRD → OKRs — with each skill reading the previous one's
output. No copy-pasting between tools, no starting cold.

Two goals, in order:

1. **Run the week.** Clone, bootstrap, ingest your data, run the pipeline on your own
   product. By Thursday: a PRD, a working prototype, and OKRs — grounded in your data.
2. **Outlast the week.** This system codifies *your* product thinking into something
   repeatable — that you can extend with your own skills and hand to your team.

## Quickstart

1. **Clone this repo** and open the folder in [Claude Code](https://claude.com/claude-code)
   (CLI, desktop app, or VS Code extension) or any `AGENTS.md`-aware agent.
2. **Say "get me started."** The bootstrap walks you through everything: OS detect, creates
   the `CLAUDE.md → AGENTS.md` symlink, then a short interview that builds your profile
   (`0_User/`) and company context (`0_Company/`). Bring your own agent — no model key
   needed from us.
3. **Drop your discovery data into `5_Library/sources/raw/`** — interviews, notes,
   analytics, research, field reports. Any format. Then say "ingest my data."

That's it. The pipeline skills take it from there, session by session.

## The week

| Day | What happens here |
|---|---|
| **Mon** | A.1 clone + bootstrap · A.2 data ingestion · A.3 value prop + persona · A.4 JTBD · A.5 PRD v1 + first prototype |
| **Tue** | Flex day — build, plus in-person 1:1 deep dives |
| **Wed** | Prototype presentations · C.2 metrics + OKRs · prototyping round 2 |
| **Thu** | Demo with judges · roadmapping · take-home handoff |

## What's inside

```
0_System/           # Repo engine: bootstrap script, skill-manifest scanner
0_User/             # Your profile — built by the bootstrap interview
0_Company/          # GROUND TRUTH — topic files: one-liner, product, stage, customers, gtm…
1_Product_Week/     # The program — one self-contained subfolder per session
2_Outputs/          # Full work products: value-prop, persona, jtbd, prd, okrs, learnings…
3_Projects/         # Non-dev working projects (post-week)
4_Dev_Projects/     # Dev builds — prototypes, apps, anything with its own repo
5_Library/
  sources/raw/      #   Your data as it arrives — any format (gitignored, stays local)
  sources/processed/#   Standardized markdown/CSV — what the skills actually read
  templates/        #   No-AI fallback templates for every exercise
  wiki/             #   Static index (carries until the local RAG MCP lands)
.agents/skills/     # Bucketed skills — find-skills/ finder + wncp-ai/<n>-skill/ pipeline
```

## The pipeline

Run in order. Every skill reads the founder's hand-completed template from
`1_Product_Week/<session>/`, plus evidence from `5_Library/sources/processed/` and ground
truth from `0_Company/`. The founder fills the template by hand; the skill's markdown output
lands in `2_Outputs/.agents/<session>/`, and its distilled essence folds back into
`0_Company/` for the next skill to read.

| # | Skill | Session | Writes (under `2_Outputs/.agents/`) |
|---|---|---|---|
| 1 | `founder-bootstrap` | A.1 | `0_User/` + `0_Company/` topic files |
| 2 | `ingest-sources` *(optional)* | A.2 | `5_Library/sources/processed/` |
| 3 | `customer-discovery-coach` | pre-A.3 | coaching (chat) |
| 4 | `value-proposition` | A.3 | `A.3-Value-Prop/Value-Proposition.md` → essence to `0_Company/` |
| 5 | `user-persona` | A.3 | `A.3-User-Persona/User-Persona.md` → essence to `0_Company/` |
| 6 | `jtbd` | A.4 | `A.4-JTBD/JTBD.md` → essence to `0_Company/` |
| 7 | `jtbd-prioritizer` | A.4 | `A.4-JTBD/JTBD-Prioritized.md` |
| 8 | `draft-prd` | A.5 · C.3 | `A.5-PRD-v1/PRD-v1.md` · `C.3-PRD-v2/PRD-v2.md` → essence to `0_Company/` |
| 9 | `metrics` | C.2 | `C.2-Metrics-OKR/Metrics-OKR.md` |

Prefer to work without AI on any stage? Every exercise has a plain template in
`5_Library/templates/`.

## Your data, your machine

- `5_Library/sources/raw/` is **gitignored** — raw discovery data never leaves your machine
  through this repo. Check what's in `5_Library/sources/processed/` before pushing anywhere.
- Bring your own agent — Founder OS provisions and routes nothing. No key to store.
- `CLAUDE.md` is a **symlink to `AGENTS.md`** created at bootstrap — never edit it directly.
- Markdown is the strategy: well-structured local files are what keep the agent grounded
  in *your* facts instead of hallucinating.
- Working with sensitive data (regulated, defense-adjacent, under NDA)? Ask in session —
  guidance on private inference options is part of the program.

## After the week

The Demo Day handoff adds the "grow your own" layer: a skill-creator (codify your own SOPs
into new skills) and roadmapping (Now/Next/Later for Sprint 3+). They're deliberately not
in the Day-1 surface — feel the pipeline work first.

---

Built by WNCP AI for the Access Mode Cohort 4 Product Week · Jun 2026
