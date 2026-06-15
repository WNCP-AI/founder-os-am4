# templates/ — No-AI Fallbacks

Every pipeline exercise has a fillable markdown template here, for working a stage by hand
without running the skill. Founders copy the master into their session folder
(`1_Product_Week/<session>/`) at session time, fill it in, and the next skill picks up
the result exactly as if the founder had run the skill conversationally.

The skill chain's derived markdown lives at `2_Outputs/.agents/<session>/<File>.md` —
the template and the derived file are two different artifacts with two different roles
(the template is the founder's working surface; the derived file is the chain's
machine-readable reference). Do not collapse them into one.

## Files

| Stage | Session | Template | Supporting | Skill output |
|---|---|---|---|---|
| Value proposition | `A.3-Value-Prop` | `A.3-Value-Prop-Template.md` | — | `2_Outputs/.agents/A.3-Value-Prop/Value-Proposition.md` |
| User persona | `A.3-User-Persona` | `A.3-User-Persona-Template.md` | — | `2_Outputs/.agents/A.3-User-Persona/User-Persona.md` |
| Jobs to be done | `A.4-JTBD` | `A.4-JTBD-Template.md` | `A.4-JTBD-Guide.md` · `A.4-JTBD-Prioritizer.csv` | `2_Outputs/.agents/A.4-JTBD/JTBD.md` · `JTBD-Prioritized.md` |
| PRD v1 | `A.5-PRD-v1` | `A.5-PRD-v1-Template.md` | — | `2_Outputs/.agents/A.5-PRD-v1/PRD-v1.md` |
| PRD v2 | `C.3-PRD-v2` | `C.3-PRD-v2-Template.md` | — | `2_Outputs/.agents/C.3-PRD-v2/PRD-v2.md` (new file; v1 kept) |
| Metrics / OKRs | `C.2-Metrics-OKR` | `C.2-Metrics-OKR-Template.md` | — | `2_Outputs/.agents/C.2-Metrics-OKR/Metrics-OKR.md` |

## Notes

- **`Full-PRD-Template.md`** — standalone comprehensive PRD format (pre-week, generic
  structure: problem, market dynamics, mission, segments, JTBD, features, design,
  risks, projections). No deliverable counterpart; distinct from the session-week
  PRD v1/v2 pair. Investor-style reference template.
- **Two copies, same content.** The master at `5_Library/templates/<Name>-Template.md`
  is the system source of truth. The copy at `1_Product_Week/<session>/<Name>-Template.md`
  is the founder's working surface. The founder fills the copy; the master stays
  unchanged so the next migration can re-derive from it.
- **Field names match the skill's closing block.** Templates are derived from each
  pipeline skill's `reference/output-format.md` — the founder transcribes from
  the skill's chat into the matching field. Renaming a field in the template
  breaks that copy step; do not paraphrase.
