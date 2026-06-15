# 1_Product_Week — The Program Scaffold

One self-contained subfolder per session, structured for live facilitated use during the
AI-Driven Product Week (Jun 15–18, 2026). This is where the work *happens* during the week —
not where outputs land.

Each session subfolder holds:
- `README.md` — step-by-step instructions for running that session
- the working **template** for the exercise (blank version sourced from `5_Library/templates/`) — **you complete it by hand, and your completed version stays in this folder**
- any session-specific assets

Sessions map to the agenda:

| Folder | Session | Exercise | Skill |
|---|---|---|---|
| `A.1-Kickoff-Setup/` | A.1 | Kickoff + bootstrap the workspace | `founder-bootstrap` |
| `A.2-Data-Ingestion/` | A.2 | Ingest & standardize discovery data *(optional)* | `ingest-sources` |
| `A.3-Value-Prop/` | A.3 | Value proposition | `value-proposition` |
| `A.3-User-Persona/` | A.3 | User persona | `user-persona` |
| `A.4-JTBD/` | A.4 | Jobs-to-be-done + prioritize & kill | `jtbd`, `jtbd-prioritizer` |
| `A.5-PRD-v1/` | A.5 | PRD v1 + first prototype | `draft-prd` |
| `C.2-Metrics-OKR/` | C.2 | Metrics + OKRs | `metrics` |

(Other session folders — `A.5-Prototyping-1`, `A.6-Show-What-You-Broke`, `B-Product-Reviews`,
`C.1-Peer-Court`, `C.3-PRD-v2`, `C.3-Prototyping-2`, `D.1-Demo-Day` — run without a pipeline skill.)

**Rule:** founders complete the templates **by hand** — the agent never fills them, and your
completed template stays here (human-owned). The agent's derived markdown deliverable lands in
`2_Outputs/.agents/<session>/` (agent-owned), and its distilled essence folds into `0_Company/`.
Each session is self-contained — opening any one folder gives you everything you need for that
exercise without context from the others.
