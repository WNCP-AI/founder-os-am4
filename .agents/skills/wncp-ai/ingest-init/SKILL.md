---
name: ingest-init
description: >
  Sets up ingestion before A.2 — figures out the best way to convert THIS founder's files on
  THIS machine. Triggers when the user says "set up ingestion", "what do I need to process my
  files", "do I need to install anything to convert my files", "get ready to ingest", or when founder-bootstrap checks
  data readiness. Scans 5_Library/sources/raw/, reports which converter engines are installed
  (Docling / MarkItDown), and recommends the single best engine for the founder's file mix with
  the exact install command for them to run. ADVISORY ONLY — it never installs or upgrades
  anything; the founder runs any install themselves. Hands off to ingest-sources for the actual
  conversion.
---

# ingest-init — Ingestion Setup & Engine Recommendation

You are helping a founder get ready to convert their raw files into the markdown the pipeline
reads. Your job is to **assess and recommend**, not to convert and not to install. Conversion
is `ingest-sources`. Installing engines is the founder's call — you give the exact command,
they run it.

## The tiers (best installed wins)

Ingestion auto-selects the best engine installed, per file: **Docling → MarkItDown → stdlib**
(text/CSV); PDFs/images with no engine fall to **Tier 0** (the agent reads them in-session);
audio/video → bring a transcript. Full table, costs, and selection logic:
[reference/engine-tiers.md](reference/engine-tiers.md).

## Step 1 — Read the situation

Run the converter's dry-run plan — it writes nothing, just reports what each file would do and
what's installed:

```bash
python3 0_System/scripts/parse-sources.py --plan
```

If `raw/` is empty, tell the founder where to drop files (`5_Library/sources/raw/`, any format,
**organized into subfolders if they like — the layout is mirrored into `processed/`**) and stop
here; there's nothing to set up yet.

## Step 2 — Recommend the right engine for THEIR files

Read the plan output and the founder/company context (`util_get_user_info`,
`util_get_company_info` — how technical they are, what kind of data they have). Then recommend:

- **Everything already converts** (only text/CSV, or an engine is installed that covers their
  files) → say so; no install needed. Go to Step 3.
- **Office docs / digital PDFs, nothing installed** → recommend **MarkItDown** (light, offline):
  `pip install "markitdown[pdf,docx,pptx,xlsx]"`.
- **Scanned PDFs, image-heavy, or complex tables/layout** → recommend **Docling**:
  `pip install docling` (note the heavier one-time model download).
- **Just a few PDFs/images and they'd rather not install anything** → tell them Tier 0 works:
  `ingest-sources` will have the agent read those directly, no install.
- **Audio/video present** → recommend bringing a transcript, or `pip install faster-whisper`.

Recommend **one** primary path — the lightest engine that covers their mix — and give the exact
command. Briefly say why it fits them. If they're non-technical, keep it to a single copy-paste
line and offer the Tier 0 / bring-a-transcript route as the no-install alternative.

## Step 3 — Hand off

Confirm what (if anything) they chose to install, then hand off:

- If they installed an engine: confirm it worked, then say *"run `ingest-sources` and it'll use
  the best engine you've got."*
- If they're going install-free: *"run `ingest-sources` — it'll convert what it can and read any
  PDFs/images directly."*

Do not run the conversion yourself — that's `ingest-sources`.

## Guardrails

- **Never install or upgrade anything** — recommend the exact command; the founder runs it (it
  changes their Python environment). This holds even if they ask you to "just set it up."
- **Best installed wins** — recommend the *lightest* engine that covers their files, not the heaviest.
- Never read, modify, or move anything in `5_Library/sources/raw/` beyond listing it via `--plan`;
  never send the founder's files to an external service.
