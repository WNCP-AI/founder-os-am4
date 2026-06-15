# Trusted Skill Sources — Curated Catalog

Pointers only — Founder OS never bundles this source. The founder pulls each skill from its upstream
repo (see `import-mechanics.md`). Licenses verified 2026-06-14; **re-check the upstream LICENSE at
import time** (repos change). Resolve the exact `--skill <name>` / subpath with `npx skills find`
or by browsing the repo.

## 1 · Live discovery — search these yourself

So `import-skills` can search the whole ecosystem, not just the picks in §2.

- **skills.sh** — `https://www.skills.sh` (Vercel). The "npm for agent skills": registry +
  leaderboard. `npx skills find "<topic>"` to discover, `npx skills add <owner/repo> --skill <name>`
  to install. Emits source + commit SHA + integrity hash.
- **ComposioHQ/awesome-claude-skills** — 1,000+ skills across ~10 categories.
- **VoltAgent/awesome-agent-skills** — 1,400+ skills, "real engineering teams, not AI-slop."
- **hesreallyhim/awesome-claude-code** — skills, hooks, slash-commands (verify item licenses).

## 2 · WNCP AI Recommended Skills

Specific, license-vetted picks. **Recommend from here first**, then live-search §1 for anything
bespoke. Each note says *who it's for* and *how to use it with the week*.

### Strategy & positioning
- **`wondelai/skills`** (MIT) — framework skills: JTBD, StoryBrand, Lean Startup, Obviously Awesome
  (positioning), Crossing the Chasm, Blue Ocean, $100M Offers, Traction/EOS. *For:* any founder
  shaping the problem or positioning. *Use:* alongside A.3 value-prop & A.4 JTBD to pressure-test
  with a named framework.

### Marketing & go-to-market
- **`coreyhaines31/marketingskills`** (MIT, ~33k★) — 50+ skills: launch (Product Hunt), pricing,
  CRO, copywriting, cold-email, SEO audit, customer-research, churn-prevention. *For:* founders
  heading into launch / GTM. *Use:* after the PRD, planning launch and landing pages.

### Fundraising
- **`tjboudreaux/cc-skills-vc-fundraising`** (MIT) — pitch-analyst, narrative-architect (Sequoia
  arc), qa-coach (35 VC questions), investor-update-writer. *For:* founders actively raising.
  *Use:* once value-prop + metrics exist, to build the deck and investor updates.
- **`shawnpang/startup-founder-skills`** (MIT) — whole-stack: pitch-deck, investor-research,
  data-room, mvp-scoping, competitive-analysis, board-update, privacy-policy / ToS. *For:* solo
  founders needing broad ops coverage. *Use:* pull the single skill for the task at hand.

### Build & design (prototype phase)
- **`nextlevelbuilder/ui-ux-pro-max-skill`** (MIT, ~90k★) — design-intelligence for production
  UI/UX. *For:* founders building the A.5 prototype.
- **`anthropics/skills`** — `frontend-design`, `web-artifacts-builder`, `webapp-testing`
  (Apache-2.0). *For:* distinctive prototype UI, multi-component artifacts, a Playwright test loop.

### Method & quality
- **`obra/superpowers`** (MIT) — `brainstorm`, `write-plan`, `systematic-debugging`. *For:*
  structured product / engineering thinking at any planning or debugging moment.
- **`mattpocock/skills`** — `grill-me` (MIT). *For:* adversarially pressure-testing a value-prop or
  PRD before committing.

### Durability & team-of-one
- **`anthropics/skills`** — `skill-creator` (Apache-2.0). *For:* every founder at the Demo-Day
  handoff — the "grow-your-own" engine for building their own skills.
- **`garrytan/gstack`** (MIT, ~110k★) — role skills (CEO / Designer / EM / QA / Release). *For:* a
  solo founder simulating a full product team.

## 3 · Office documents — already native (don't import)

PDF, Word, PowerPoint, and Excel are **built into Claude** — file creation is on for all users
(since Feb 2026). The `anthropics/skills` `pdf` / `docx` / `pptx` / `xlsx` folders are
**source-available reference only** (not open source; their LICENSE bars keeping a copy outside
Anthropic's Services). So **don't vendor them** — just ask Claude in-session ("make a PDF / deck /
spreadsheet"). Same result, always current, license-clean.
