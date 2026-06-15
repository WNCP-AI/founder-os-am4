# 0_User — Founder Profile

Who runs this workspace — personal context the agent reads at the start of every session to
adapt to how you work. Personal only; company facts live in `0_Company/`.

Structured as numbered Title-Case topic files, read/written only via the `util_get_user_info`
skill — the `1-founder-bootstrap` interview seeds them; no skill edits the layout directly.

```
0_User/
├── 01_Overview.md      # name, role, identity
├── 02_Expertise.md     # background, domain expertise, strengths, gaps
├── 03_Preferences.md   # working style: tone, depth, pace, decisions, tools
├── 04_Goals.md         # what you want during & after the program
└── Z_Library.md        # fuller background, referenced by file name + section header
```

The folder starts empty — run **"Let's get started"** and the bootstrap skill fills it in.
