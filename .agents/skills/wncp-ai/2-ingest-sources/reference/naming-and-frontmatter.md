# Processed file naming, frontmatter & conversion rules

Refine the converter's output (and any Tier-0/text files) into this convention — one processed
file per raw source (merge only trivial fragments).

## Naming

| Data type | Processed filename |
|---|---|
| Customer/user interview | `interview-<who>-<YYYY.MM.DD>.md` |
| Call / meeting notes | `notes-<topic>-<YYYY.MM.DD>.md` |
| Analytics / metrics export | `analytics-<source>.md` (or `.csv`) |
| Survey results | `survey-<topic>.md` (or `.csv`) |
| Market / competitor research | `research-<topic>.md` |
| Field test / technical / regulatory | `field-<topic>.md` |

## Frontmatter

Every processed markdown file starts with:

```yaml
---
type: interview | notes | analytics | survey | research | field
source: <original filename in 5_Library/sources/raw/>
date: <date of the data itself, if known>
processed: <today's date>
---
```

The converter's first pass writes a coarser `type` (the file extension) and may add an `engine:`
line recording which converter produced it — keep `engine:` as provenance and upgrade `type` to the
semantic value above as you refine.

## Conversion rules

- **Keep verbatim quotes verbatim.** Customer language is the raw material for value-prop and JTBD
  work — mark quotes clearly, attribute them (`— buyer, logistics co.`).
- Structure with headers, don't rewrite. Fix transcription noise, keep meaning intact.
- Tabular data stays tabular — CSV or markdown tables, not prose.
- Redact obvious sensitive identifiers if the founder asks (or flags their data as sensitive) —
  names can become roles.
- Never invent or infer data that isn't in the source.
