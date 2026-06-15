# Customer Discovery Kit — Start Here

Two tools that take you from assumptions to evidence before you build the wrong thing. Use them **before** Product Week — aim for **at least 5 customer interviews completed before Jun 15**.

This kit has two files:

| File | What it is | Where it runs |
|---|---|---|
| `customer-discovery-coach.skill` | An AI coach that turns raw assumptions into a ranked hypothesis stack + a ready-to-use interview guide | The **Claude app** (claude.ai) — *not* Claude Code |
| `Customer-Discovery-Tracker.xlsx` | A five-tab tracker — enter your hypotheses once, every tab populates automatically | Excel / Google Sheets |

---

## Step 1 — Install the Customer Discovery Coach

1. Open the **Claude app** (claude.ai or the desktop app).
2. Go to **Customize → Skills**, click **+**, then **Upload a skill**.
3. Select `customer-discovery-coach.skill` from this kit.
4. Toggle it **on**. It's now available in any Claude conversation.

> **Heads up:** this skill installs in the **Claude app**, not Claude Code. Claude Code is a separate tool you'll set up for Product Week itself — see the install requirements in the email. Don't try to load this `.skill` into Claude Code.

## Step 2 — Run a coaching session

Start a Claude conversation and ask about your customer interviews. The coach will ask whether you already have hypotheses or are starting cold — either works. By the end you'll have a ranked hypothesis stack and a full interview guide.

## Step 3 — Set up the Tracker

Open `Customer-Discovery-Tracker.xlsx`. In the **Guide** tab, enter your hypotheses — this is the *only* place you type them; every other tab pulls from here. Paste your interview questions into the **Question Log**, tagging each with the hypothesis it tests.

## Step 4 — Interview, then look for patterns

Ask the same questions to everyone. Log key quotes as you go. After each interview, mark each hypothesis **Validated / Invalidated / Inconclusive** in the Hypothesis Matrix — be honest, an invalidated hypothesis is worth more than a dishonest "inconclusive." Review the **Pattern Summary** tab after every 5 interviews.

---

**Where this leads:** Customer Discovery → JTBD → Prioritizer → PRD. What you capture here feeds directly into everything you build during Product Week, so every later decision is grounded in what real customers actually told you.

Questions before the week? Reply to the email or reach out on Slack.
