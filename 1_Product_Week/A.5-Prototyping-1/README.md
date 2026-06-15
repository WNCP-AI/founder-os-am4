# A.5-Prototyping-1

Mon Jun 15 · 1:30–3:45 PM (shared with A.5-PRD-v1) · In-person — Valerius Living, Denver · 20m teach / 1h 55m workshop.

First prototyping session: pick the right tool tier for your product and build a working first prototype or testable mock against your PRD v1.

**The beats — three maturity stages and three tiers.** Vibe coding: you say something, it produces something, no security awareness — the floor. AI rapid prototyping: purpose-built, testable, explicitly not handling payments or permanently storing sensitive user data — the target for Product Week. Full software engineering: production-grade, code quality, full spec discipline — what you build toward after the week. The tier defines capability, not skill level: **Tier 1** (front-end clickable) is Google AI Studio, Stitch, Claude Artifacts/Design, ChatGPT Canvas, v0; **Tier 2** (+ back-end, Lovable = default) adds Supabase / Neon / Clerk / Bolt / Replit / Base44; **Tier 3** (engineering-grade, Claude Code = default) runs on your machine and edits files directly. GitHub is the cross-tier foundation. Spec-driven development at Tier 2+: write PRD + tech-stack.md (plus UI.md / data.md / api.md as needed) before implementation — agents in execution mode do not always make the best architectural choices on the fly. The prototype boundary: no payments, no permanent storage of sensitive user data.

**What you do.** Run the routing skill to confirm your tool tier — do not pick by default. Write your one-sentence test before the first build prompt: *"My Day 1 prototype tests [X]. A pass means [Y]."* Build against PRD v1 — scope to one flow, one feature, one user action. Ask your builder tool to run its built-in security audit before sharing the prototype outside the room.

**Where work goes.** The prototype artifact lives in `4_Dev_Projects/`, linkable for Day 3 and Peer Court reference; the agent's derived notes land in `2_Outputs/.agents/A.5-Prototyping-1/`. Mobile app development is Tier 3 only and out of scope this week — redirect to PWA if mobile experience is the requirement. Vercel is the recommended deployment target across all tiers.
