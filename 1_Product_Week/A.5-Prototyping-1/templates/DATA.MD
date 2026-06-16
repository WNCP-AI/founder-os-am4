# DATA.MD — Database Schema

Defines the tables, fields, and access rules your backend needs. Gives the AI builder a precise target instead of guessing at your data structure.

**Status:** Optional — backend only

**Use it when:** Full web app (Lovable, Google AI Studio + Firebase), Mobile (Bolt, Replit), Full stack (Claude Code, Codex). Skip it for frontend-only prototypes — those have no backend and no persistent database.

> Prototype guardrail: a prototype stores no permanently-stored sensitive PII and handles no real payments. Design your schema accordingly — collect only what the prototype needs to function.

---

## Entities

<!-- guidance: List every table (entity) your app needs. Each table holds one type of thing — a user, a listing, a booking, a message, etc. Start with the minimum set. You can add tables later. One bullet per table. -->

- `______` <!-- e.g. users -->
- `______`
- `______`
- `______` <!-- add or remove rows as needed -->

---

<!-- guidance: Repeat the section below once for each table you listed above. Copy the heading and table, fill in the fields. Delete any blank rows you don't use. -->

### `______` <!-- table name -->

<!-- guidance: Field = column name (snake_case). Type = text, integer, boolean, timestamp, uuid, json. Required = Yes or No. Notes = any constraint, default value, or clarification. -->

| Field | Type | Required | Notes |
|-------|------|----------|-------|
| `id` | uuid | Yes | Primary key, auto-generated |
| `created_at` | timestamp | Yes | Set automatically on insert |
| `______` | ______ | ______ | <!-- what this field stores --> |
| `______` | ______ | ______ | |
| `______` | ______ | ______ | |

---

### `______` <!-- table name -->

| Field | Type | Required | Notes |
|-------|------|----------|-------|
| `id` | uuid | Yes | Primary key, auto-generated |
| `created_at` | timestamp | Yes | Set automatically on insert |
| `______` | ______ | ______ | |
| `______` | ______ | ______ | |
| `______` | ______ | ______ | |

---

### `______` <!-- table name -->

| Field | Type | Required | Notes |
|-------|------|----------|-------|
| `id` | uuid | Yes | Primary key, auto-generated |
| `created_at` | timestamp | Yes | Set automatically on insert |
| `______` | ______ | ______ | |
| `______` | ______ | ______ | |
| `______` | ______ | ______ | |

---

## Relationships

<!-- guidance: Describe how your tables connect. Use plain English. One bullet per relationship. State the direction: "A [table] belongs to one [table]" or "A [table] can have many [table]s". These become foreign keys in Supabase or Neon. -->

- A `______` belongs to one `______` <!-- e.g. "A listing belongs to one user" -->
- A `______` can have many `______`s
- A `______` belongs to one `______`

---

## Access Rules

<!-- guidance: Define who can read or write each table. Common roles: "public" (anyone, no login), "authenticated" (logged-in users), "owner" (the user who created the row), "admin" (a specific role you define). Keep it simple — prototype-grade security only. Do not store real passwords, financial data, government IDs, or health records. -->

| Table | Who can read | Who can write | Notes |
|-------|-------------|---------------|-------|
| `______` | <!-- e.g. authenticated --> | <!-- e.g. owner only --> | |
| `______` | | | |
| `______` | | | |

<!-- guidance: For Supabase, these rules map directly to Row Level Security (RLS) policies. For Neon, your app layer enforces them. Tell the AI builder which backend you are using (see TECH_STACK.MD) so it writes the right enforcement code. -->

---

## Ask the LLM

Paste these prompts into Claude, ChatGPT, or Gemini — one at a time. Use the answers to fill in the sections above.

1. "I am building [describe your product in one sentence]. What are the minimum database tables I need for a prototype? List each table name and one sentence on what it stores."

2. "For the [table name] table in my app, what fields does it need? Give me a list with field name, data type (text, integer, boolean, timestamp, uuid, json), whether it is required, and a short note. Keep it to what the prototype actually needs."

3. "How do these tables relate to each other: [paste your table list]? Describe each relationship in plain English — for example, 'a booking belongs to one user and one listing'."

4. "For my prototype, who should be able to read and write each of these tables: [paste your table list]? Give me simple access rules using roles like public, authenticated, owner, and admin. I am using [Supabase / Neon]."

5. "Am I storing any sensitive personal data in this schema: [paste your entities and fields]? Flag anything I should remove or anonymize for a prototype. I do not want to store permanent sensitive PII."

6. "Are there any fields or tables I listed that the prototype does not actually need yet? Help me cut this schema to the minimum that makes the core user flow work."

7. "Rewrite my DATA.MD schema section as a single prompt I can paste into [Lovable or Google AI Studio — Full web app / Bolt or Replit — Mobile / Claude Code or Codex — Full stack] to generate the database automatically. Include table names, fields, types, and relationships."

---

## Done when

- [ ] Every table that the core user flow touches is listed with a name and purpose
- [ ] Each table has a fields table with at least `id`, `created_at`, and the columns the app reads or writes
- [ ] Relationships between tables are described in plain English (at least one relationship per linked pair)
- [ ] Access rules are defined for every table — no table is left with undefined read/write permissions
- [ ] No sensitive PII (government IDs, passwords, financial account numbers, health data) appears anywhere in the schema
