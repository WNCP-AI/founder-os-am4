# Ingestion engine tiers

Ingestion auto-selects the best engine present on the machine, per file (best-installed-wins).

| Tier | Engine | Handles | Cost |
|---|---|---|---|
| **Docling** | `pip install docling` | scanned/complex PDFs, OCR, tricky tables, office docs | heavier (pulls PyTorch + ~hundreds-MB models); CPU-fine |
| **MarkItDown** | `pip install "markitdown[pdf,docx,pptx,xlsx]"` | digital PDFs + Office docs, fully offline | light, pure-pip |
| **Tier 0 — agent-native** | *(no install)* | the agent reads PDFs/images directly in-session | zero deps; PDFs/images only |
| **stdlib** | *(built in)* | `.txt`/`.md`/`.csv` | always available |

The table is ordered by **fidelity, not selection order**: `.txt`/`.md`/`.csv` are always handled
by stdlib with no engine or Tier 0 needed. Tier 0 is the fallback for **PDFs/images only**, used by
`ingest-sources` when no engine is installed. An engine (Docling/MarkItDown) is only needed for
office docs (docx/pptx/xlsx) and for higher-fidelity PDF/image conversion.

**Audio/video** is *not* converted locally by default — recommend a transcript (Zoom/Otter/Granola
export) dropped into `raw/`, or `pip install faster-whisper` for local transcription.
