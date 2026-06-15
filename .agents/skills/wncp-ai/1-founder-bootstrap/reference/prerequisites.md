# Prerequisites — install commands by OS (Step 2 detail)

These were in the pre-week checklist (P.2), so most founders arrive ready. Confirm each; if
missing, give the install command for their OS.

| Prerequisite | Check | Mac | Windows | Linux |
|---|---|---|---|---|
| **git** | `git --version` | `brew install git` | `winget install Git.Git` | `apt install git` |
| **Node.js 18+** | `node --version` | `brew install node` | `winget install OpenJS.NodeJS.LTS` | nodejs.org (LTS) |

Node is only needed for the `setup.mjs` bootstrap script — if it's missing, don't block; continue
and note it.

**After any `winget install`:** open a **new** terminal so `PATH` refreshes before re-checking
versions.
