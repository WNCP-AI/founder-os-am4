# API.MD — API Design Document

Defines the endpoints your backend exposes, what data flows in and out, how requests prove who is making them, and how errors are reported. Gives the AI a single reference so it builds all parts of the app speaking the same language.

**Status:** Optional — backend only

**Use it when:** Full stack (Claude Code, Codex) and Full web app (Google AI Studio, Lovable) builds that require a backend with more than one or two endpoints. Skip for Frontend-first and Mobile lanes, and for any build where the tool can infer the API shape on its own.

**Prototype scope:** This doc covers prototype-grade API design only. A prototype stores no permanently-stored sensitive PII and handles no real payments. Do not design endpoints for those concerns here.

This doc belongs to the AI rapid prototyping stage. At vibe coding stage the AI infers the API; at engineering-grade stage a full OpenAPI spec replaces this. For Cohort 4, stop here.

---

## Endpoints

<!-- guidance: List every endpoint your prototype needs to expose. One row per endpoint. Method = HTTP verb (GET, POST, PUT, PATCH, DELETE). Path = the URL path starting with /. Purpose = one plain sentence on what it does. Auth = who can call it: "public" (no login needed), "user" (any logged-in user), or "admin" (restricted role). Add rows as needed. If you are not sure whether an endpoint belongs here, ask: does the frontend need to call the backend to do this thing? If yes, it belongs here. -->

| Method | Path | Purpose | Auth |
|--------|------|---------|------|
| <!-- GET / POST / etc --> | <!-- /resource --> | <!-- What this endpoint does in one sentence --> | <!-- public / user / admin --> |
| | | | |
| | | | |
| | | | |
| | | | |

---

## Contracts

<!-- guidance: For each key endpoint in the table above, write one block showing: (1) what the request sends, and (2) what a successful response looks like. Copy the example format below once per key endpoint. You do not need a block for every endpoint — cover the ones where the shape of the data matters for your UI or business logic. Keep fields flat — no deeply nested objects at prototype stage. -->

<!-- EXAMPLE FORMAT — delete this block and replace with your own -->
<!--
### `[METHOD] /your-path-here`

[One-line description of what this call does]

**Request body (if applicable):**
```
<!-- paste your fields here — list each field name, its data type, and what it contains -->
```

**Success response:**
```
<!-- paste the fields the API returns on success — list field names, types, and what they mean -->
```
-->
<!-- End example format -->

<!-- Add your endpoint contract blocks here, one block per key endpoint, following the example format above -->

---

## Auth Model

<!-- guidance: Describe how a request proves who is making it. Pick the pattern that matches your tech stack and answer the questions below. You do not need to write code — write the answers in plain English so the AI can implement it correctly. -->

**Auth provider:**
<!-- Which service handles login? Options: Supabase Auth, Clerk, custom JWT, none (public prototype). Write the name — or paste from TECH_STACK.MD. -->
___________________________

**Token type:**
<!-- How does a logged-in user prove identity on each request? Most tools use a Bearer token in the Authorization header. Write: "Bearer token in Authorization header" unless you know otherwise. -->
___________________________

**Session handling:**
<!-- Where does the auth token live on the client? For a prototype, localStorage is acceptable. Production security choices (such as httpOnly cookies) belong to the engineering-grade stage — do not make that call here. Write your choice. -->
___________________________

**Protected vs. public routes:**
<!-- Which endpoints in your Endpoints table above require a logged-in user, and which are open to anyone? List the paths that are public; assume everything else requires auth. -->

Public (no token required):
- ___________________________
- ___________________________

---

## Error Conventions

<!-- guidance: Define how your API signals that something went wrong. Consistent error shapes mean the AI can write one error-handling function on the frontend instead of guessing per endpoint. Fill in the three items below. -->

**HTTP status codes this API uses:**

<!-- guidance: Fill in the table below with the HTTP status codes your prototype will return and what each means in your context. Common codes to choose from: 200 (success), 201 (resource created), 400 (bad input), 401 (not logged in / token expired), 403 (logged in but not permitted), 404 (not found), 500 (server error). Only include codes your prototype will actually use. -->

| Code | When it is returned |
|------|---------------------|
| ___ | ___ |
| ___ | ___ |
| ___ | ___ |
| ___ | ___ |

**Error response shape:**

<!-- guidance: Define the JSON shape your API returns for every error response — same shape regardless of which endpoint fails. Decide the field names you want. Common choices: a plain-English "message" field the dev log can show, and a short machine-readable "code" field the frontend can check in logic. Write your chosen shape below. -->

```
<!-- paste your error response shape here — define the field names and what each field contains -->
```

**Validation errors:**

<!-- guidance: When the caller sends bad input (400), should the API return one error or a list of field-level errors? Choose: "single top-level error message" (simpler, fine for prototype) or "array of field errors with field name + message" (more work but better UX). Write your choice. -->
___________________________

---

## Ask the LLM

Paste these prompts one at a time into Claude, ChatGPT, or Gemini to fill this doc through conversation. Start with your PRD.MD and TECH_STACK.MD open — reference them in your prompts.

1. "Here is my PRD: [paste PRD.MD]. Based on the features listed, what API endpoints does my backend need to expose? Give me a table with columns: Method, Path, Purpose, Auth. Keep it to the minimum set for a working prototype."

2. "Here are my endpoints: [paste your Endpoints table]. For each POST or PUT endpoint, write the request body and success response as JSON. Keep field names short and flat — no nested objects. Use placeholder values so I can see the shape."

3. "My auth provider is [paste your auth provider from TECH_STACK.MD]. How should a logged-in user prove identity on each API request — what goes in the request header? Give me the exact header format and a one-sentence explanation of where the token comes from."

4. "Which of these endpoints should be public (no login required) and which should require a logged-in user? [paste your Endpoints table]. Explain your reasoning for each one."

5. "Write a standard error response shape in JSON that covers: bad input (400), unauthenticated (401), not found (404), and server error (500). Use the same shape for all four — one 'error' object with 'message' and 'code' fields."

6. "I am building a [describe your product in one sentence]. Are there any endpoints I am missing from this list? [paste your Endpoints table]. Flag any gap that would block a user from completing the core workflow."

7. "Review my full API.MD draft: [paste the doc]. Flag anything that is over-engineered for a prototype — endpoints or data fields I do not need yet. Suggest what to cut."

---

## Done when

- [ ] Every endpoint the frontend needs to call has a row in the Endpoints table, with a method, path, purpose, and auth level filled in.
- [ ] At least the two or three most important endpoints have request and response shapes defined in the Contracts section.
- [ ] The Auth model names a specific provider and describes how the token travels on each request.
- [ ] The error response shape is defined and consistent — same JSON structure regardless of which endpoint fails.
- [ ] Nothing in this doc requires permanently storing sensitive PII or processing real payments.
