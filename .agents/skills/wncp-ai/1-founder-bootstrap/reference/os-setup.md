# OS detection & CLAUDE.md symlink (Step 0 detail)

## CLAUDE.md → AGENTS.md

The repo root needs a `CLAUDE.md` so Claude Code can read the agent conventions. `CLAUDE.md` is a
**symlink to `AGENTS.md`** — one source of truth, no drift. `0_System/bootstrap/setup.mjs` creates
it per-OS (true symlink on Mac/Linux; a generated copy on Windows, where symlinks need elevated
privileges) and is gitignored (generated plumbing, not content).

If Node isn't available, create the symlink directly:

- **Mac/Linux:** `ln -sf AGENTS.md CLAUDE.md`
- **Windows (PowerShell, as admin):** `New-Item -ItemType SymbolicLink -Name CLAUDE.md -Target AGENTS.md`

## Detect OS

- **Mac:** `uname -s` returns `Darwin`
- **Linux:** `uname -s` returns `Linux`
- **Windows:** `$env:OS` returns `Windows_NT` (PowerShell), or `ver` shows a Windows version.
  **Do not assume WSL or Git Bash** — founders on Windows may be in plain PowerShell or the Claude
  Code desktop app with no Unix shell.

State what you detected and confirm before proceeding. Every OS-specific command branches on this.
