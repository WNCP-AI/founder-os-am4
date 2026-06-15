# sources/ — Your Data

The data convention the whole pipeline runs on.

## raw/

Drop everything here: interview transcripts and recordings notes, call notes, analytics
exports, survey results, market research, competitor notes, field test results, technical
specs, regulatory documents. **Any format.** This folder is gitignored — its contents stay
on your machine.

## processed/

Standardized markdown/CSV produced by the `ingest-sources` skill (or by you, using the
same conventions). **This is the only folder pipeline skills read.** Tracked in git so your
working data is versioned with your workspace.

Naming convention:

| Data type | Filename |
|---|---|
| Interview | `interview-<who>-<YYYY.MM.DD>.md` |
| Call / meeting notes | `notes-<topic>-<YYYY.MM.DD>.md` |
| Analytics export | `analytics-<source>.md` / `.csv` |
| Survey | `survey-<topic>.md` / `.csv` |
| Market / competitor research | `research-<topic>.md` |
| Field / technical / regulatory | `field-<topic>.md` |

This folder holds **evidence only**. Agent-generated pipeline artifacts (value prop, persona, JTBD, PRD…) live in `2_Outputs/.agents/<session>/`, not here.

## Privacy

Raw data is gitignored by default. Before pushing this repo anywhere, check
`sources/processed/` for anything customer-identifying or sensitive — redact (names →
roles) or keep those files local. If your data is regulated or under NDA, raise it in
session for private-inference options.
