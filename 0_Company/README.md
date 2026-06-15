# 0_Company — Ground Truth

The single source of company truth — the authoritative layer every skill reads before it
runs. Structured as short topic files (no index), so the agent can read the whole folder
before any exercise. The `founder-bootstrap` skill seeds these from its interview; each
pipeline stage distills its output back into the relevant file here.

Core topic files (grow with the chain):

```
0_Company/
├── 01_Overview.md      # one-liner, identity, stage
├── 02_Product.md       # what it is, what it does, the core mechanism
├── 03_Users.md         # who you serve, segments, early adopters
├── 04_Market.md        # market, competition, positioning
├── 05_Traction.md      # stage, metrics, OKRs
├── 06_Team.md          # founders, roles
├── 07_PW_Insights.md   # running takeaways across Product Week
└── Z_Library.md        # deeper detail, referenced by file name + section header
```

Read/written only via the `util_get_company_info` skill — no other skill touches the layout directly.

**Rule:** distilled essence only — not full work products. The PRD lives in `2_Outputs/.agents/A.5-PRD-v1/PRD-v1.md`; a
one-paragraph product summary distilled from it lives here. This is what makes the chain
compound: A.3 updates the ground truth, A.4 reads the updated truth — no re-explaining
context from scratch. Raw evidence doesn't live here either; that's `5_Library/sources/`.
