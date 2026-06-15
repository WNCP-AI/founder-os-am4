# bootstrap/

One script, one job:

```
node 0_System/bootstrap/setup.mjs
```

- On Mac/Linux: creates a real symlink `CLAUDE.md → AGENTS.md` at the repo root
  (gitignored — re-create any time by re-running setup.mjs)
- On Windows, or if the symlink fails (EPERM etc.): generates a copy of `AGENTS.md`
  as `CLAUDE.md` instead
- Warns (never fails) if Node 18+ or git are missing, with per-OS install hints

`AGENTS.md` is the single source of truth for agent instructions. The symlink means
Claude Code (which reads `CLAUDE.md`) and any other AGENTS.md-aware agent get identical
instructions from one file. No model key is stored or required — bring your own agent.

The script is a convenience — the `founder-bootstrap` skill
(`.agents/skills/wncp-ai/1-founder-bootstrap/`) runs the same symlink step agent-side, then
continues with the full guided setup: OS detection, prerequisites, founder profile
(`0_User/`), and company context (`0_Company/`). New founders should open the repo in
their agent and say **"Let's get started."**
