# Import Mechanics — pull one skill, license-clean + tracked

The goal: land a single skill at `.agents/skills/<function>/<skill>/`, preserve its license, and
record where it came from. Two paths — prefer the first.

> Office-document skills (`pdf`/`docx`/`pptx`/`xlsx`) are **never** imported — they're native to
> Claude. See catalog §3.

## Path A — `npx skills` (primary; needs Node 18+, checked at bootstrap)

```bash
# discover (optional)
npx skills find "<topic>"
# install one skill (writes to .claude/skills/ or .agents/skills/ + a skills-lock.json)
npx skills add <owner/repo> --skill <name>
```

Then move/ensure the skill folder sits at `.agents/skills/<function>/<name>/`. Capture the
`source`, `ref` (full commit SHA), and integrity hash from the `skills-lock.json` it writes — these
feed the manifest below.

## Path B — git fallback (no Node)

```bash
# sparse-checkout just the skill subpath
git clone --no-checkout --depth 1 <repo-url> /tmp/skill-src
cd /tmp/skill-src
git sparse-checkout init --cone
git sparse-checkout set <subpath-to-skill>
git checkout
git rev-parse HEAD          # <- record this commit SHA for the manifest
# place it
mkdir -p <repo>/.agents/skills/<function>/<name>
cp -r /tmp/skill-src/<subpath-to-skill>/* <repo>/.agents/skills/<function>/<name>/
```

(For a single file, `curl -O https://raw.githubusercontent.com/<owner>/<repo>/<sha>/<path>` works;
pin the SHA, not a branch.)

## Preserve attribution (both paths)

Copy the upstream `LICENSE` (and `NOTICE` if present) into the skill folder:
`.agents/skills/<function>/<name>/LICENSE`. Apache-2.0 requires the NOTICE be preserved; MIT
requires the copyright line be kept.

## Record provenance

1. Append an entry to `.agents/skills/skills-manifest.json` (create it if missing):

```json
{
  "schema_version": 1,
  "skills": [
    {
      "name": "<name>",
      "source_repo": "https://github.com/<owner>/<repo>",
      "source_subpath": "<subpath>",
      "resolved_commit_sha": "<full SHA>",
      "spdx_license_id": "MIT",
      "license_file_path": ".agents/skills/<function>/<name>/LICENSE",
      "copyright_notice": "Copyright <year> <author>",
      "notice_file_path": null,
      "author": "<author>",
      "import_date": "<YYYY-MM-DD>",
      "local_path": ".agents/skills/<function>/<name>"
    }
  ]
}
```

2. Regenerate `.agents/skills/THIRD_PARTY_NOTICES.md` — a human-readable list of every imported
   skill: name, author, license (SPDX), source URL. (Same format Anthropic uses in their repo.)

## Index

```bash
python3 0_System/scripts/scan-skills.py
```

This registers the skill in `.agents/skills/skills.json` (enabled by default). It's discoverable
through `find-skills`, which reads the skill folders on disk directly.

## Storage model — why a vendored copy

Plain copy tracked in git + the manifest above. **Not** a git submodule (stores only a pointer —
breaks offline use and `git clone`), and **not** a subtree (bloats history, founder-unfriendly).
Re-running the importer overwrites the folder and updates the manifest entry to a new commit SHA.
