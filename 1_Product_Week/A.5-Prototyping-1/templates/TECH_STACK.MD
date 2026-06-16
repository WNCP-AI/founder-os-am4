# TECH_STACK.MD

Tells the AI builder exactly what tools, services, and structure to use — so you don't get a random framework on your first build attempt.

**Status:** Required

**Use it when:** All four lanes. Fill this before you prompt any AI builder.

---

## Stack at a glance

<!-- guidance: Pick one choice per row. If you don't know what a layer means, leave it blank and use the "Which lane am I in" section below to get defaults. The AI builder will fill the gaps if you give it this file. -->

| Layer | Choice | Notes |
|---|---|---|
| Frontend | <!-- e.g. React / Next.js, plain HTML, React Native (Expo) --> | |
| Backend | <!-- e.g. None, Supabase, Neon + serverless functions, Firebase --> | |
| Database | <!-- e.g. None, Supabase Postgres, Neon Postgres --> | |
| Auth | <!-- e.g. None, Supabase Auth, Clerk --> | |
| Hosting / Deploy | <!-- e.g. Vercel (default), Netlify, Replit (built-in) --> | |
| Repo / version control | <!-- e.g. GitHub (required at Lane 2 and Lane 4; recommended at Lane 3; optional at Lane 1) --> | |

---

## Which lane am I in

<!-- guidance: Find your lane from the PRD.MD. Copy the default stack for that lane into the table above. Adjust only if you have a specific reason. -->

| Lane | Description | Default stack |
|---|---|---|
| **1 — Frontend-first** | Static UI, no accounts, no shared data. Landing page, clickable demo, single-user tool. | Stitch or Claude Design → export HTML/React. Deploy to Vercel. No backend, no database, no auth. GitHub optional. |
| **2 — Full web app** | User accounts, persistent data, multi-user. | Lovable or Google AI Studio. Supabase (database + auth). Deploy to Vercel. GitHub required. |
| **3 — Mobile** | Phone-first interface; needs a real device for user testing. See the mobile note below. | Build a responsive web app in Bolt or Replit, host it, and add to home screen as a PWA (default). Expo Go via Bolt is an optional step further if you want a native-feeling preview on a real device. Supabase if data storage needed. GitHub recommended. |
| **4 — Full stack** | Complex logic, custom API, technical founder or developer involved. | Claude Code or Codex. Next.js. Supabase or Neon. Deploy to Vercel. GitHub required. |

**Mobile lane note (Lane 3).** A PWA — a website that installs on a phone like an app — is the only realistic mobile-feeling output a non-technical founder can reach in 2.5 hours. Here is what that means in practice:

- Open your hosted URL on a phone browser, tap "Add to Home Screen." It gets an icon, launches full-screen, and can work offline. That is your prototype.
- Bolt's Expo integration lets you go one step further: prompt Bolt with the React Native / Expo template, scan the QR code with the free Expo Go app on your phone, and preview a native-feeling app on a real device. That is the full session deliverable.
- Getting into the App Store or Google Play is a separate project. It requires a paid developer account (Apple: $99/year; Google: $25 one-time), code-signing certificates, a native build pipeline, and platform review that can take days. None of that happens in this session.
- If your idea genuinely requires native hardware — Bluetooth, NFC, contacts access beyond what a browser can reach — flag it now. Otherwise build the PWA first, test it with real users, and decide whether a native app is worth the investment once you have validated the concept.
- Lane 3 is the most demanding lane for a non-technical founder in a 2.5-hour session. Choose it only if your PRD requires a mobile-first interface that a responsive web app cannot satisfy, or if your user testing specifically requires a phone-native experience.

---

## Repository layout

<!-- guidance: Paste the folder structure your AI builder creates, or use the skeleton below. The AI builder will generate this — update it here after the first build so you know where your files are. -->

```
[your-project-name]/
├── PRD.MD                  <!-- required -->
├── TECH_STACK.MD           <!-- this file -->
├── UI.MD                   <!-- optional — add if you filled one -->
├── DESIGN.MD               <!-- tool-generated — add if Claude Design or Stitch produced one -->
├── DATA.MD                 <!-- optional — backend only -->
├── API.MD                  <!-- optional — backend only -->
└── [source code folder]    <!-- e.g. src/, app/, components/ — AI builder creates this -->
```

<!-- guidance: Keep all your spec docs at the project root alongside the source code. This is how AI builders like Claude Code and Codex find them. -->

---

## Runtime dependencies

<!-- guidance: List the packages or services your app depends on at runtime. Your AI builder will generate a package.json or requirements.txt — copy the key items here so you can recreate the environment if something breaks. Lane 1 projects often have zero runtime dependencies. -->

- <!-- e.g. Next.js ^15.x -->
- <!-- e.g. React ^19.x -->
- <!-- e.g. @supabase/supabase-js -->
- <!-- e.g. None — static HTML only -->

---

## Build & run

<!-- guidance: Copy the exact commands to start your app locally from whatever the AI builder produces. If you are using a web-based tool (Lovable, Bolt, Replit) that runs in the browser, write "Web-based — no local setup required" and note the preview URL instead. -->

**Local setup (Lane 4 only):**

```bash
# Install dependencies
npm install

# Start local dev server
npm run dev
# App runs at http://localhost:3000
```

**Web-based tools (Lane 1 / Lane 2 / Lane 3 via Bolt or Replit):**

```
Preview URL: ___________________________
No local install required. All building happens in the browser.
```

---

## Deploy

<!-- guidance: Fill in the deploy target that matches your lane. You do not need all three options — delete the ones that don't apply. -->

**Vercel (default for all lanes).**
Push your code to GitHub. Connect the repo to Vercel at vercel.com. Every push to your main branch deploys automatically. Free tier is sufficient for a prototype.

```
Production URL: ___________________________
Vercel project name: ___________________________
GitHub repo: ___________________________
```

**Netlify (alternative to Vercel).**
Same flow as Vercel — connect a GitHub repo, auto-deploy on push. Use Netlify if Vercel isn't working or if your builder tool exports a ZIP that you want to drag-and-drop into a host.

**Supabase vs. Neon — pick one if you need a database.**

| | Supabase | Neon |
|---|---|---|
| What it gives you | Database + auth + file storage in one dashboard | Database only (serverless Postgres) |
| Best for | Founders who want everything in one place; easiest full backend setup | Founders who only need a database and are handling auth separately (e.g. Clerk) |
| Free tier | One project free; limits apply | More generous free tier; good if you are running multiple test projects |
| Recommendation | Start here unless you have a specific reason not to | Use if you hit Supabase's free-tier limits or if auth is handled elsewhere |

**Mobile lane (Lane 3) — PWA deploy note.**
A PWA requires no special deploy step. Host your web app on Vercel or Replit's built-in hosting, open the URL on a phone, and tap "Add to Home Screen." Android supports full PWA install natively. iOS (Safari) supports Add to Home Screen with more limited feature parity. That is the complete deploy for a mobile prototype.

---

## What this stack is NOT

<!-- guidance: Read this section before you share your prototype with anyone. These are the boundaries every prototype must stay within, regardless of lane. -->

- **Not production.** This is a prototype for concept validation and user testing. It is not built to the security or reliability standards of a shipping product.
- **Not a place for real sensitive data.** Do not store passwords, payment information, social security numbers, medical records, or other sensitive personal information in a prototype. This is a program guardrail, not a suggestion.
- **Not a payment processor.** Do not connect real Stripe keys or any live payment integration. If payment flow is part of your product, mock it — show the UI, skip the real charge.
- **Not a native app store listing.** A PWA or Expo Go preview is not in the App Store or Google Play. That step requires a paid developer account, certificates, and platform review — it is an engineering-grade deliverable that follows a validated prototype.
- **Not a finished codebase.** Vibe coding and AI rapid prototyping produce working demos, not maintainable production code. The three-stage framing applies: vibe coding -> AI rapid prototyping -> engineering-grade. This session delivers stage one or two.

---

## Why these choices

<!-- guidance: This section is for you. Write one sentence per choice explaining why you picked it over an alternative. This helps you explain the stack to a developer if you hand off the project after the session. If you used defaults from "Which lane am I in," write "Default for Lane [X]." -->

| Choice | Why |
|---|---|
| <!-- e.g. Lovable --> | <!-- e.g. Default for Lane 2. No local setup required. --> |
| <!-- e.g. Supabase --> | <!-- e.g. Needed user auth and a database; Supabase gives both in one place. --> |
| <!-- e.g. Vercel --> | <!-- e.g. Default for all lanes. Free tier, auto-deploys from GitHub. --> |
| | |

---

## Ask the LLM

Paste these into Claude, ChatGPT, or Gemini to fill this document through conversation. Go one question at a time.

1. "I'm building [describe your product in one sentence]. It needs [list any features from your PRD that involve data storage, user accounts, or real-time updates — or say 'none']. Which of these four build lanes fits best: (1) Frontend-first, (2) Full web app, (3) Mobile, (4) Full stack? Give me a one-paragraph reason and name the default stack for that lane."

2. "Given that lane, what should I put in the 'Stack at a glance' table in my TECH_STACK.MD? Give me a completed table with one choice per row: Frontend, Backend, Database, Auth, Hosting/Deploy, Repo/version control."

3. "I'm using [tool from your lane, e.g. Lovable / Bolt / Claude Code]. What folder structure will it create? Give me a short directory tree I can paste into the 'Repository layout' section of TECH_STACK.MD."

4. "What are the three to five npm packages or services my app will depend on at runtime, given this stack? List them with version numbers if you know them."

5. "I'm deploying with [Vercel connected to GitHub / Replit's built-in hosting]. Walk me through the exact steps to get a live URL I can share and open on a phone. What will the URL look like?"

6. "I need a database. Compare Supabase and Neon for my use case: [describe what data you need to store and roughly how many users will test the prototype]. Which should I use and why?"

7. "Write the 'Why these choices' table for my TECH_STACK.MD. I chose [list your stack choices]. Give me one plain-English sentence per choice explaining why it fits a non-technical founder building a prototype in 2.5 hours."

8. "Review my completed TECH_STACK.MD and tell me: (a) anything that contradicts my PRD, (b) any layer I left blank that I actually need, (c) any choice that adds complexity I can cut for a prototype."

---

## Done when

- [ ] Every row in "Stack at a glance" is filled in or intentionally left blank with a note (e.g. "None — Lane 1, no backend needed").
- [ ] Lane is identified and the default stack matches the lane or you have written a reason for deviating.
- [ ] Deploy target is named (Vercel URL, Replit URL, or equivalent) — not just "TBD."
- [ ] Confirmed: no sensitive personal data fields (passwords, payment info, SSNs, medical records) are in the planned data schema, and no real payment keys will be used in this prototype.
- [ ] "Why these choices" table has at least one row filled in per non-obvious choice.
