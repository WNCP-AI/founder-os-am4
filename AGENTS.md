# Founder OS — Access Mode Cohort 4

Your product workspace for the AI-Driven Product Week (Jun 15–18, 2026) — and after it.
This repo is an **agentic operating system**: a folder of markdown files, conventions, and
skills that an AI agent (Claude Code) reads and works inside. You load it with your own
discovery data, then run the product pipeline against it: value prop → persona →
jobs-to-be-done → PRD → OKRs. Each skill reads the previous one's output. You own every
artifact it helps you produce.

## Getting started

**New founder?** Open this repo in **Claude Code** (CLI, desktop app, or VS Code extension)
— or any `AGENTS.md`-aware agent — and say **"get me started"** — the `founder-bootstrap`
skill detects your OS, creates the `CLAUDE.md → AGENTS.md` symlink, then interviews you to
build your profile (`0_User/`) and company context (`0_Company/`). Bring your own agent —
no model key needed from us.

Optional script form of the same setup checks:

```
node 0_System/bootstrap/setup.mjs
```

`setup.mjs` creates the `CLAUDE.md → AGENTS.md` symlink and verifies your environment
(Node, git). Re-run it whenever `AGENTS.md` changes. If you skip it, the `founder-bootstrap`
skill handles the symlink and environment check on first run — no script required, any OS.

## Repo structure

```
0_System/           # Repo engine: bootstrap script, skill-manifest scanner
0_User/             # Your profile — who you are, how you work (bootstrap builds this)
0_Company/          # GROUND TRUTH — topic files: one-liner, product, stage, customers, gtm…
1_Product_Week/     # The program — one subfolder per session; holds the template YOU fill by hand
2_Outputs/          # Agent work products, in a hidden .agents/<session>/ layer (don't hand-edit)
3_Projects/         # Non-dev working projects — strategy, research, partnerships, SOPs
4_Dev_Projects/     # Dev builds — prototypes, apps, anything with its own repo (YYYY.MM Name)
5_Library/
  sources/raw/      #   Drop zone, any format — GITIGNORED, never leaves the machine
  sources/processed/#   Standardized markdown/CSV, browsable by source — tracked; what the pipeline reads
  templates/        #   Master no-AI fallback templates for every pipeline stage
  wiki/             #   Legacy index — dormant; removed when the local RAG MCP lands
.agents/skills/     # Bucketed skills — auto-discovered via find-skills/ and scan-skills.py
  find-skills/      #   THE finder: one skill that locates all the others
  wncp-ai/          #   Skills we author, numbered in deliverable order:
    1-founder-bootstrap/        #   "Get me started" onboarding
    2-ingest-sources/           #   raw → processed standardization
    3-customer-discovery-coach/ #   discovery prep
    4-value-proposition/        #   ─┐
    5-user-persona/             #    │
    6-jtbd/                     #    ├─ the product-thinking pipeline
    7-jtbd-prioritizer/         #    │
    8-draft-prd/                #    │
    9-metrics/                  #   ─┘ (OKRs)
    import-skills/              #   pull in useful third-party skills (F8)
    ingest-init/                #   recommend the best file converter for A.2 (no install)
  <function groups>/            #   General / third-party skills — added via import-skills
```

## The pipeline

**Setup → (optional) ingest → run the chain.** Skills 1–2 set you up; 3–9 are the
product-thinking chain. Each chain skill reads your **hand-completed template** in
`1_Product_Week/<session>/`, evidence in `5_Library/sources/processed/`, and ground truth in
`0_Company/`; it writes its full output to `2_Outputs/.agents/<session>/` (agent-owned, hidden)
and folds the essence back into `0_Company/` for the next skill. **You fill the template by hand —
the skill never does.** A missing input is never a dead end: skills recover with you (offer to
ingest or gather it, then continue).

| # | Skill | Session | Writes (under `2_Outputs/.agents/`) |
|---|---|---|---|
| 1 | `founder-bootstrap` | A.1 | `0_User/` + `0_Company/` topic files |
| 2 | `ingest-sources` *(optional)* | A.2 | `5_Library/sources/processed/` |
| 3 | `customer-discovery-coach` | pre-A.3 | coaching (chat) |
| 4 | `value-proposition` | A.3 | `A.3-Value-Prop/Value-Proposition.md` |
| 5 | `user-persona` | A.3 | `A.3-User-Persona/User-Persona.md` |
| 6 | `jtbd` | A.4 | `A.4-JTBD/JTBD.md` |
| 7 | `jtbd-prioritizer` | A.4 | `A.4-JTBD/JTBD-Prioritized.md` |
| 8 | `draft-prd` | A.5 · C.3 | `A.5-PRD-v1/PRD-v1.md` · `C.3-PRD-v2/PRD-v2.md` |
| 9 | `metrics` | C.2 | `C.2-Metrics-OKR/Metrics-OKR.md` |

## Data convention

- **`5_Library/sources/raw/`** — drop everything here: interview transcripts, notes,
  analytics exports, market research, field/technical/regulatory docs. Any format; organize
  into subfolders if you like — the layout is mirrored into `processed/`.
  Gitignored — raw dumps never leave your machine via this repo.
- **`5_Library/sources/processed/`** — cleaned, standardized markdown/CSV the skills read,
  browsable by source, mirroring the `raw/` subfolder layout. The **optional** `ingest-sources`
  skill runs a tiered converter (`0_System/scripts/parse-sources.py`) that auto-uses the best
  engine installed (Docling → MarkItDown → built-in text/CSV) and stubs what it can't convert;
  for PDFs/images with no engine, the skill reads them directly (agent-native, Tier 0). It
  recommends installs but never runs them. `ingest-init` suggests the right converter for your
  files. The pipeline scans this tree directly (no index to maintain). Skip ingestion and skills
  run on `0_Company/` ground truth instead.

## Conventions

- `AGENTS.md` (this file) is the source of truth for agent instructions; `CLAUDE.md` is a
  **symlink to `AGENTS.md`** created at bootstrap — never hand-edit `CLAUDE.md` directly
- Project folders in `4_Dev_Projects/` use `YYYY.MM Short Name` naming
  (e.g. `2026.06 Prototype Sprint 1`)
- Skills are bucketed under `.agents/skills/`: use `find-skills` to locate the right skill
  across all buckets; each `SKILL.md` frontmatter is the source of truth, and
  `0_System/scripts/scan-skills.py` records their enabled state in `skills.json`
- Skills are thought partners — they coach, draft, and structure, but you make the calls
  and you own the artifacts. Read what they produce; don't let generated content you never
  read feed back into the system
- Use YAML frontmatter on processed source files (type, date, source) so the agent can
  index them

## Key reference files

| Question | File |
|---|---|
| Who am I working with? | `0_User/` (topic files) |
| What is this company/product? | `0_Company/` |
| What data do we have? | `5_Library/sources/processed/` |
| What skills are available? | `.agents/skills/` SKILL.md files (use `find-skills`) |
| How does the engine work? | `0_System/README.md` |
| Where are the no-AI templates? | `5_Library/templates/` |

## Boundaries — do not

- Commit `.env` or any secret — never commit credentials or API keys to the repo
- Edit `CLAUDE.md` directly — it is a symlink to `AGENTS.md`; edit this file instead
- Push customer-identifying or sensitive discovery data to any public repo —
  `5_Library/sources/raw/` is gitignored for a reason; check before you commit anything
  from `5_Library/sources/processed/`
- Send sensitive data to external services without the founder's explicit say-so
- Generate large volumes of artifacts the founder hasn't asked for — one artifact per
  pipeline stage, owned and edited by the founder
- Fill in the founder's session template for them — **they complete it by hand** in
  `1_Product_Week/<session>/`; your derived markdown goes only to `2_Outputs/.agents/<session>/`
