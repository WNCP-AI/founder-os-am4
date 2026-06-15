#!/usr/bin/env python3
"""
verify-skills.py — Dry-run acceptance gate for migrated pipeline skills.

Run from the repo root:
    python 0_System/scripts/verify-skills.py            # lint all in-scope skills
    python 0_System/scripts/verify-skills.py 4-value-proposition   # lint one
    python 0_System/scripts/verify-skills.py --util     # check only the two util skills

What it checks for each skill (static "dry run" — no founder run needed):
  1. SKILL.md exists at the expected bucket path and has YAML frontmatter
     with `name:` matching the contract.
  2. NO legacy/dangling path references survive: bare `sources/processed`,
     `sources/raw`, `1_Company`, `wiki/INDEX` (without the 5_Library prefix),
     or the vague "project folder".
  3. Every top-level zone the skill names (2_Outputs/, 0_Company/,
     5_Library/sources/processed/) is a real directory in the repo.
  4. The skill's declared OUTPUT path(s) match the canonical contract below
     (full work product under 2_Outputs/, essence folded into 0_Company/).
  5. The skill is indexed in .agents/skills/skills.json at the right path.

--util mode checks ONLY the two util skills (util_get_user_info,
util_get_company_info) and exits 0 when they pass. It does not touch the
pipeline skill (3-9) contract logic.

Exit code 0 = all checked skills pass; 1 = at least one failure.
This is the gate the migration loop runs before merging any skill branch.
"""

import json
import os
import re
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SKILLS_DIR = os.path.join(REPO_ROOT, ".agents", "skills")
WNCP = os.path.join(SKILLS_DIR, "wncp-ai")
MANIFEST = os.path.join(SKILLS_DIR, "skills.json")

# Canonical contract — grounded in the find-skills pipeline + locked file-map (PRD v1.7).
# Outputs land in 2_Outputs/.agents/<session>/ with Title-Case filenames; frontmatter names
# carry the am4- prefix.
# folder -> (frontmatter name, [required output paths], chat_only)
CONTRACT = {
    "3-customer-discovery-coach": ("am4-customer-discovery-coach", [], True),
    "4-value-proposition":        ("am4-value-proposition", ["2_Outputs/.agents/A.3-Value-Prop/Value-Proposition.md"], False),
    "5-user-persona":             ("am4-user-persona", ["2_Outputs/.agents/A.3-User-Persona/User-Persona.md"], False),
    "6-jtbd":                     ("am4-jtbd", ["2_Outputs/.agents/A.4-JTBD/JTBD.md"], False),
    "7-jtbd-prioritizer":         ("am4-jtbd-prioritizer", ["2_Outputs/.agents/A.4-JTBD/JTBD-Prioritized.md"], False),
    "8-draft-prd":                ("am4-prd", ["2_Outputs/.agents/A.5-PRD-v1/PRD-v1.md", "2_Outputs/.agents/C.3-PRD-v2/PRD-v2.md"], False),
    "9-metrics":                  ("am4-metrics", ["2_Outputs/.agents/C.2-Metrics-OKR/Metrics-OKR.md"], False),
}
# The skills required to be present for a full-suite PASS (bootstrap/ingest deferred).
REQUIRED = set(CONTRACT)

# Legacy patterns that must NOT appear in a migrated skill body.
FORBIDDEN = [
    (r"(?<![\w/])sources/processed", "bare 'sources/processed' (use 5_Library/sources/processed/)"),
    (r"(?<![\w/])sources/raw", "bare 'sources/raw' (use 5_Library/sources/raw/)"),
    (r"\b1_Company\b", "'1_Company' (renamed to 0_Company)"),
    (r"(?<!5_Library/)wiki/INDEX", "bare 'wiki/INDEX' (use 5_Library/wiki/INDEX.md)"),
    (r"\bproject folder\b", "vague 'project folder' (point at 2_Outputs/ or 0_Company/)"),
]

# Zones that must exist on disk if a skill references them.
ZONES = ["2_Outputs", "0_Company", "5_Library/sources/processed", "5_Library/sources/raw"]


# Util skills live one level deeper: wncp-ai/util_/<folder>/SKILL.md
# Mapping: folder -> (frontmatter name, [substrings the body must contain]).
# For the two folder-contract owners, the list is the FULL set of required topic files —
# so the gate fails if a skill drops any required topic (e.g. 03_Preferences / 05_Traction),
# which is the layout this script exists to protect.
UTIL_CONTRACT = {
    "util_get_user_info":    ("util_get_user_info",
                              ["0_User/", "01_Overview", "02_Expertise", "03_Preferences",
                               "04_Goals", "Z_Library"]),
    "util_get_company_info": ("util_get_company_info",
                              ["0_Company/", "01_Overview", "02_Product", "03_Users", "04_Market",
                               "05_Traction", "06_Team", "07_PW_Insights", "Z_Library"]),
    "util_get_inputs":       ("util_get_inputs",
                              ["5_Library/sources/processed", "util_get_company_info", "2_Outputs/.agents"]),
}

UTIL_DIR = os.path.join(WNCP, "util_")


def frontmatter_name(text):
    m = re.match(r"^---\s*\n(.*?)\n---", text, re.DOTALL)
    if not m:
        return None
    nm = re.search(r"^name:\s*(.+)$", m.group(1), re.MULTILINE)
    return nm.group(1).strip().strip("\"'") if nm else None


def check_skill(folder):
    name, outputs, chat_only = CONTRACT[folder]
    path = os.path.join(WNCP, folder, "SKILL.md")
    fails = []
    if not os.path.isfile(path):
        return [f"missing SKILL.md at wncp-ai/{folder}/"]
    text = open(path, encoding="utf-8").read()

    fm = frontmatter_name(text)
    if fm != name:
        fails.append(f"frontmatter name '{fm}' != contract '{name}'")

    for pat, msg in FORBIDDEN:
        if re.search(pat, text):
            fails.append(f"forbidden ref: {msg}")

    for zone in ZONES:
        if zone in text and not os.path.isdir(os.path.join(REPO_ROOT, zone)):
            fails.append(f"references {zone}/ but that dir does not exist")

    if chat_only:
        if "2_Outputs/" in text:
            fails.append("chat-only skill should not write to 2_Outputs/")
    else:
        for out in outputs:
            if out not in text:
                fails.append(f"missing canonical output ref '{out}'")

    return fails


def check_util(folder, name, required):
    """Verify a util skill at wncp-ai/util_/<folder>/SKILL.md against its contract."""
    path = os.path.join(UTIL_DIR, folder, "SKILL.md")
    fails = []
    if not os.path.isfile(path):
        return [f"missing SKILL.md at wncp-ai/util_/{folder}/"]
    text = open(path, encoding="utf-8").read()

    fm = frontmatter_name(text)
    if fm != name:
        fails.append(f"frontmatter name '{fm}' != contract '{name}'")

    for pat, msg in FORBIDDEN:
        if re.search(pat, text):
            fails.append(f"forbidden ref: {msg}")

    # Each util skill must document the contract markers it owns or routes to
    for needle in required:
        if needle not in text:
            fails.append(f"body does not reference '{needle}'")

    return fails


def in_util_manifest(folder, name):
    """Check that a util skill is indexed in skills.json at the three-level path."""
    if not os.path.isfile(MANIFEST):
        return False
    try:
        with open(MANIFEST, encoding="utf-8") as fh:
            data = json.load(fh)
    except (OSError, json.JSONDecodeError):
        return False
    want = f"wncp-ai/util_/{folder}/SKILL.md"
    return any(s.get("path") == want and s.get("name") == name for s in data.get("skills", []))


def in_manifest(folder, name):
    if not os.path.isfile(MANIFEST):
        return False
    try:
        with open(MANIFEST, encoding="utf-8") as fh:
            data = json.load(fh)
    except (OSError, json.JSONDecodeError):
        return False
    want = f"wncp-ai/{folder}/SKILL.md"
    return any(s.get("path") == want and s.get("name") == name for s in data.get("skills", []))


def main():
    if "--util" in sys.argv:
        print("verify-skills — util skill check\n")
        overall_ok = True
        for folder, (name, required) in UTIL_CONTRACT.items():
            fails = check_util(folder, name, required)
            if os.path.isfile(os.path.join(UTIL_DIR, folder, "SKILL.md")):
                if not in_util_manifest(folder, name):
                    fails.append("not indexed in skills.json (run scan-skills.py)")
            if fails:
                overall_ok = False
                print(f"  ✗ {folder}")
                for f in fails:
                    print(f"      - {f}")
            else:
                print(f"  ✓ {folder}  ({name})")
        print("\n" + ("PASS" if overall_ok else "FAIL"))
        return 0 if overall_ok else 1

    targets = sys.argv[1:] or sorted(CONTRACT)
    bad = [t for t in targets if t not in CONTRACT]
    if bad:
        print(f"Unknown skill(s): {bad}\nKnown: {sorted(CONTRACT)}")
        return 2

    print("verify-skills — dry-run path/contract check\n")
    overall_ok = True
    present = set()
    for folder in targets:
        name = CONTRACT[folder][0]
        fails = check_skill(folder)
        if os.path.isfile(os.path.join(WNCP, folder, "SKILL.md")):
            present.add(folder)
            if not in_manifest(folder, name):
                fails.append("not indexed in skills.json (run scan-skills.py)")
        if fails:
            overall_ok = False
            print(f"  ✗ {folder}")
            for f in fails:
                print(f"      - {f}")
        else:
            print(f"  ✓ {folder}  ({name})")

    missing_required = REQUIRED - present
    if set(targets) >= REQUIRED and missing_required:
        overall_ok = False
        print(f"\n  ✗ required skills not yet present: {sorted(missing_required)}")

    print("\n" + ("PASS" if overall_ok else "FAIL"))
    return 0 if overall_ok else 1


if __name__ == "__main__":
    sys.exit(main())
