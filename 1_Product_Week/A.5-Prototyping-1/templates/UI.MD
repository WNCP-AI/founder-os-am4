# UI.MD — Screen Layout & Visual Spec

This doc describes what your product looks like and how it behaves. It tells the AI builder exactly which screens to create, what goes on each one, and how a user moves through them.

This doc belongs to the vibe coding and AI rapid prototyping stages. You are not designing a finished product — you are giving the AI enough to generate a testable first version.

**Status:** Optional — recommended for complex or visual-heavy designs

**Use it when:** Any lane where the look matters. Especially important for Full web app, Mobile, and Full stack. Useful for Frontend-first if the design has more than two or three screens or a non-standard layout.

<!-- guidance: Mobile lane means a PWA (progressive web app) — not a native iOS or Android app. Design for a browser on a phone screen. -->

**This doc is founder-written.** The AI does not generate it for you. You know your user and your product. Spend 15 minutes here and you will save hours of back-and-forth with the builder later. See DESIGN.MD for the visual style layer (colors, type, spacing) — that one the AI can generate for you. UI.MD is your job.

**Prototype guardrails:** A prototype built from this doc must not store sensitive personal information permanently and must not process real payments. If a screen collects payment details or sensitive data, note that it is a UI placeholder only.

---

## Screen inventory

<!-- guidance: List every distinct screen your product has. A screen is any full view the user lands on. Don't list modals unless they are the primary interaction surface. Aim for 3–8 screens for a prototype. -->

| # | Screen name | Who sees it | When they see it |
|---|-------------|-------------|-----------------|
| 1 | _____ | _____ | _____ |
| 2 | _____ | _____ | _____ |
| 3 | _____ | _____ | _____ |
| 4 | _____ | _____ | _____ |
| 5 | _____ | _____ | _____ |

<!-- guidance: Add or remove rows as needed. "Who sees it" might be "any visitor", "logged-in user", "admin only", etc. -->

---

## Screen details

<!-- guidance: Copy the block below once per screen. Replace <Screen name> with the name from your inventory. The ASCII wireframe is a rough sketch — boxes, labels, and lines only. It does not need to be pretty. It needs to show the AI what goes where. -->

<!-- guidance: If building for Mobile, note touch target sizes, bottom navigation placement, and that content should assume a ~390px wide viewport. Describe any swipe gestures as primary actions. -->

### <Screen name>

<!-- guidance: Draw a rough ASCII wireframe. Use brackets [ ] for buttons, pipes | | for borders, dashes --- for dividers, and plain words for content areas. Aim for 15–30 lines. Think of it as a napkin sketch, not a Figma file. -->

```
+--------------------------------------------------+
|                                                  |
|  [Header / Nav bar]                              |
|                                                  |
+--------------------------------------------------+
|                                                  |
|  Content area — label what goes here             |
|                                                  |
|  [ Primary action button ]                       |
|                                                  |
+--------------------------------------------------+
|  Footer                                          |
+--------------------------------------------------+
```

<!-- guidance: Replace the template wireframe above with your actual screen layout. -->

**Key components:**

<!-- guidance: List the distinct UI pieces on this screen. Be specific. Not "a list" — "a list of recent invoices showing invoice number, date, and status". -->

- _____
- _____
- _____

**Primary action:**

<!-- guidance: One sentence. What does the user do on this screen that moves them forward? -->

_____

---

### <Screen name>

<!-- guidance: Draw a rough ASCII wireframe. Use brackets [ ] for buttons, pipes | | for borders, dashes --- for dividers, and plain words for content areas. Aim for 15–30 lines. Think of it as a napkin sketch, not a Figma file. -->

```
+--------------------------------------------------+
|                                                  |
|  [Header / Nav bar]                              |
|                                                  |
+--------------------------------------------------+
|                                                  |
|  Content area — label what goes here             |
|                                                  |
|  [ Primary action button ]                       |
|                                                  |
+--------------------------------------------------+
|  Footer                                          |
+--------------------------------------------------+
```

<!-- guidance: Replace the template wireframe above with your actual screen layout. -->

**Key components:**

<!-- guidance: List the distinct UI pieces on this screen. Be specific. Not "a list" — "a list of recent invoices showing invoice number, date, and status". -->

- _____
- _____
- _____

**Primary action:**

<!-- guidance: One sentence. What does the user do on this screen that moves them forward? -->

_____

---

<!-- guidance: Paste the screen detail block above for each additional screen in your inventory. -->

---

## Navigation & flow

<!-- guidance: Describe how a user gets from screen to screen. A sentence or two per transition is enough. You can also draw a simple text diagram with arrows (->). Cover the happy path first, then any important branch (e.g. error state that sends the user back). -->

**Happy path:**

_____  ->  _____  ->  _____  ->  _____

<!-- guidance: Walk through each arrow above in plain English. For example: "From the Home screen, the user clicks [Get started] and lands on the Onboarding screen." -->

| From | Action | To |
|------|--------|----|
| _____ | _____ | _____ |
| _____ | _____ | _____ |
| _____ | _____ | _____ |
| _____ | _____ | _____ |

**Back navigation:**

<!-- guidance: Note whether the user can go back and how. For example: "Back arrow on all screens returns to the previous screen. The Home screen has no back." -->

_____

---

## States

<!-- guidance: For each important screen, describe what it looks like in three situations: empty (first time, no data), loading (waiting on the server or AI), and error (something went wrong). This prevents the AI builder from leaving blank white screens or ignoring failure cases. You do not need to cover every screen — focus on the ones where these states are most visible to the user. -->

### <Screen name> — states

| State | What the user sees |
|-------|--------------------|
| Empty | _____ <!-- guidance: e.g., "A centered message: 'No projects yet. Create your first one.' with a [+ New project] button." --> |
| Loading | _____ <!-- guidance: e.g., "A spinner in the center of the content area. The primary action button is disabled." --> |
| Error | _____ <!-- guidance: e.g., "A red banner at the top: 'Something went wrong. Try again.' with a [Retry] link." --> |

### <Screen name> — states

| State | What the user sees |
|-------|--------------------|
| Empty | _____ |
| Loading | _____ |
| Error | _____ |

<!-- guidance: Add a states table for each screen that has meaningful empty, loading, or error behavior. -->

---

## Ask the LLM

Paste these one at a time into Claude, ChatGPT, or Gemini to fill out each section. Share your PRD.MD first so the AI has context.

1. "I shared my PRD above. List every distinct screen my product needs for a working prototype. For each one, give me: the screen name, who sees it, and when they land on it. Keep the list under 8 screens."

2. "Pick the most important screen from that list. Describe exactly what UI components appear on it — be specific about labels, input fields, buttons, and any data displayed. Then draw a rough ASCII wireframe showing the layout, nothing fancy."

3. "Take the next screen from the inventory. Describe its key UI components — be specific about labels, inputs, and buttons — then draw a simple ASCII wireframe showing the layout."

4. "Describe how a user moves from screen to screen on a first visit. Start from the moment they open the app. Walk me through each transition in plain English, one step at a time."

5. "Take the next screen from the list. Describe what the user sees in three situations: no data yet, page is loading, and something went wrong. One to two sentences each."

6. "Look at the screen inventory and wireframes we have. What important screen am I missing? What navigation path did I forget to describe? What state (empty, loading, or error) would surprise a user if it was blank?"

7. "Rewrite my navigation flow table so it covers every possible action that changes screens, including going back and any error redirects."

---

## Done when

- [ ] Every screen in the inventory has a wireframe, a key components list, and a named primary action.
- [ ] The navigation table covers every transition on the happy path and at least one error or back path.
- [ ] Each screen that has meaningful loading or empty behavior has those states described.
- [ ] A non-technical teammate could hand this doc to an AI builder and get a recognizable first draft without asking you any follow-up questions.
- [ ] Any reference to visual style (color, font, spacing) has been moved to DESIGN.MD; this doc covers layout and behavior only.
