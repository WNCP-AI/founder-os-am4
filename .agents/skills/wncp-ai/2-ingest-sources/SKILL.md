---
name: ingest-sources
description: >
  Standardizes a founder's raw discovery data so the product pipeline can read it. Triggers
  when the user says "ingest my data", "process my sources", "standardize my files", drops
  files into 5_Library/sources/raw/, or in session A.2 (Data Ingestion & Prep). Converts
  every raw file — interview transcripts, call notes, analytics exports, market research,
  surveys, field/technical/regulatory documents — into clean markdown or CSV in
  5_Library/sources/processed/ (browsable by source), files them by naming convention with
  frontmatter, and reports what data exists, what's thin, and what's ready for the
  value-prop → persona → JTBD chain.
---

# ingest-sources — Raw → Processed Data Ingestion

You are standardizing a founder's discovery data into the format every pipeline skill reads.
Work file by file. Preserve evidence — never summarize away the founder's raw material.

## The convention

- **`5_Library/sources/raw/`** — input. Anything, any format (txt, docx, pdf, csv, xlsx,
  html, md, exported chats, photos of whiteboards). Organized into **subfolders** if the
  founder likes — the layout is mirrored into `processed/`. Gitignored; never modified by
  this skill.
- **`5_Library/sources/processed/`** — output. Clean markdown (or CSV for tabular data) only,
  mirroring the `raw/` subfolder layout. This folder is the single place pipeline skills look
  for raw evidence. Tracked in git.

## Step 1 — Inventory the raw folder

List every file in `5_Library/sources/raw/`. For each, identify what it is. Ask the founder
only when a file's nature is genuinely unclear. **Not all discovery data is interviews** —
hardware, deep-tech, and long-cycle founders bring field test results, technical specs,
regulatory documents, pilot reports, RFP responses. All of it counts; standardize it, don't
reject it.

## Step 2 — Run the tiered converter (the engine does the heavy lifting)

Office docs and PDFs can't be read by the agent's plain file tools, so a converter does the
extraction. Run it — it auto-detects the **best engine installed** and uses it per file
(Docling → MarkItDown → stdlib for text/CSV), mirroring `raw/` subfolders into `processed/`:

```bash
python3 0_System/scripts/parse-sources.py
```

The script **never installs anything**. For any file it can't convert with what's installed it
writes a `status: stub` placeholder naming the exact install command. After it runs, handle the
results:

- **Converted files** — a first pass with mechanical names (`<source-stem>.md`) and basic
  frontmatter. Refine these in Step 3 (semantic names, richer frontmatter, quote preservation).
- **Stubbed PDFs / images** — use **Tier 0 (agent-native)**: read the file yourself and replace
  the stub with the real content. No install needed.
- **Stubbed Office docs (docx/pptx/xlsx)** — you can't read these directly; surface the install
  command (`pip install "markitdown[docx,pptx,xlsx]"`), let the founder run it, then re-run the
  converter. **Never install it yourself.**
- **Stubbed audio/video** — ask for a transcript (drop it in `raw/`) or point them at
  `pip install faster-whisper`; leave the stub until then.

If the founder would rather set up the right engine first, send them to `ingest-init` — it
recommends the best converter for their file mix without installing anything.

## Step 3 — Refine each converted file

Refine the converter's first pass (and write any Tier-0/text files) into the house convention —
one processed file per raw source (merge only trivial fragments), semantic name, upgraded
frontmatter. The single rule that matters most: **keep verbatim customer quotes verbatim** — they
are the raw material for value-prop and JTBD. Full naming table, frontmatter spec, and conversion
rules: [reference/naming-and-frontmatter.md](reference/naming-and-frontmatter.md).

## Step 4 — Confirm the processed tree

No index to maintain — the pipeline reads `5_Library/sources/processed/` directly. After
converting, make the output browsable: it mirrors the `raw/` subfolder layout, so group files
sensibly (by source), each with frontmatter and named per the convention above. List the
resulting tree so the founder sees what landed where.

## Step 5 — Report: what you have, what's thin

End with a short readiness report in chat:

1. **What you have** — counts by type (e.g. "4 interviews, 1 analytics export, 2 research docs")
2. **What's thin** — gaps that will starve specific pipeline stages (e.g. "no direct
   customer quotes → value-prop will lean on your own framing; flag during A.3")
3. **Ready for the chain?** — explicit yes/no for the next stage (`value-proposition`),
   and what to gather later if no.

A founder with thin data still proceeds — downstream skills recover with the founder rather than
block (see `util_get_inputs` → *When a primary input is missing*) — but they should hear it stated
plainly now, not discover it mid-exercise.

## Guardrails

- Never modify or delete anything in `5_Library/sources/raw/`
- **Never install or upgrade a converter engine yourself.** When a file needs Docling/MarkItDown
  /faster-whisper, surface the exact command and let the founder run it — installing changes
  their Python environment, which is their call.
- **Best installed wins** — let the converter pick the engine; don't force a heavier one.
- Never send the founder's data to external services — all processing happens locally,
  in this conversation
- Don't editorialize on the founder's business in processed files — that's the pipeline's
  job, with the founder in the loop
