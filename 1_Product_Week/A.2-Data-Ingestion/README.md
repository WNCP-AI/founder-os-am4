# A.2-Data-Ingestion

Mon Jun 15 · 10:00–11:00 AM · In-person — Valerius Living, Denver · 15m teach / 45m workshop.

Bootstrap every founder's Founder OS and ingest their discovery data — the **C (Collect)** and **R (Refine)** of CRAFT+. AI principles are taught here so the kickoff stays light on them.

Founders leave with Founder OS downloaded, the agent confirmed working and able to reach the repo's skills, bootstrap complete with company information in the raw folder (at minimum: customer interview transcripts), all discovery data standardized into `5_Library/sources/processed/`, and some basic experience querying their system for information on their customers.

**The beat — AI is a tool, not a source of truth.** AI is like Wikipedia — powerful, but you must validate it. AI enhances a human and is bad at replacing one. AI slop is *your* fault: either you hired AI for a job it's bad at, or you didn't give it enough constraints. Don't over-invest in AI unless it's your core business. AI works with the same two things as a great hire: clear instructions (SOPs) and good information.

**What you do.** Run the bootstrap / Founder OS setup. Drop raw discovery files into `5_Library/sources/raw/` (subfolders are mirrored); the agent helps convert via the `ingest-sources` skill — it runs a tiered converter (Docling → MarkItDown → built-in text/CSV), never installs anything, and stubs what it can't convert. Founder fills the data-ingestion template by hand.

Rename Agentic OS → Founder OS everywhere. The skill must NOT auto-generate output — humans fill a human-completable template in the product-week folder by talking to the agent. If A.2 gets this wrong, every later talk inherits the mistake. Surface thin data now — the chain starves downstream.
