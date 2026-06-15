# 2_Outputs — Agent Work Products

The full record of what the **agent** produces — the markdown deliverable each pipeline skill
writes, derived from the founder's hand-completed template (in `1_Product_Week/<session>/`) plus
evidence. Intended to be shared, shown to stakeholders, and built upon.

This top level is just a pointer. The actual outputs live in a **dotfile-prefixed
`.agents/` layer** — agent-owned, **not hand-edited** — mirroring `1_Product_Week/`
session-for-session:

```
2_Outputs/
└── .agents/                       # agent-owned working layer (don't hand-edit)
    ├── A.3-Value-Prop/Value-Proposition.md
    ├── A.3-User-Persona/User-Persona.md
    ├── A.4-JTBD/JTBD.md · JTBD-Prioritized.md
    ├── A.5-PRD-v1/PRD-v1.md        # extended to PRD-v2.md after C.2
    ├── C.2-Metrics-OKR/Metrics-OKR.md
    └── …                          # one subfolder per session
```

**Rule — three homes, two owners:**
- `1_Product_Week/<session>/` — the founder's **hand-completed template** (human-owned input). Founders fill these themselves; the agent never fills them.
- `2_Outputs/.agents/<session>/` — the agent's full markdown work products (agent-owned, not hand-edited). What you ship and point stakeholders to.
- `0_Company/` — only the **distilled essence** the next skill reads (via `util_get_company_info`).

The three grow together, in three places.
