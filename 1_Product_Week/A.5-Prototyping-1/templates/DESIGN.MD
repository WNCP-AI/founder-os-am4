# DESIGN.MD — Design System

This doc defines your product's visual language: colors, type, spacing, and component patterns. This template gives you the structure a generated design system doc should follow. Claude Design or Stitch fills in the values; you review and adjust before handing it to the builder tool.

**Status:** Tool-generated — Claude Design or Stitch produces this doc. Review it, adjust one or two tokens if needed, then hand it to the builder tool as context.

**Use it when:** any lane where visual quality matters — Frontend-first (Stitch, Claude Design), Full web app (Google AI Studio, Lovable), Mobile (PWA, Bolt, Replit), or Full stack (Claude Code, Codex). Skip it only for throwaway proof-of-concept builds where you are testing logic, not appearance.

**Stage:** This doc is used in the vibe coding and AI rapid prototyping stages. An engineering-grade build would replace it with a formal design system handoff.

**Prototype guardrails:**
- This prototype stores no permanently-stored sensitive PII.
- This prototype handles no real payments.

**How to generate:** Open Claude.ai (or Stitch at stitch.withgoogle.com — note: access may require a Google account and waitlist approval). Paste the prompt from the "Ask the LLM" section below. Review the output, adjust any token you dislike, then copy the result into this file. Stitch users: export design tokens from the export panel and map them into the tables below.

---

## Creative north star

<!-- guidance: One sentence. Name the mood, aesthetic, or reference that defines the product's look and feel. Think of a magazine, a brand you admire, or an adjective pair. Example pattern: "[Personality] meets [reference] — [one visual quality]." Keep it to one line. The generator uses this to make every downstream decision consistent. -->

___________________________________________________________________________

---

## Color tokens

<!-- guidance: Three to six tokens is enough for a prototype. Every color should have a clear job — primary action, background, text, border, accent, error. Avoid decorative colors that have no assigned role. The generator will propose these based on your north star; edit the table to correct any token before passing it to the builder tool. -->

| Token | Value | Use |
|---|---|---|
| `--color-primary` | <!-- hex, e.g. #1A56DB --> | Primary action — buttons, links, focus rings |
| `--color-primary-dark` | <!-- hex --> | Hover / pressed state for primary elements |
| `--color-bg` | <!-- hex --> | Default page background |
| `--color-surface` | <!-- hex --> | Card, panel, input background |
| `--color-text` | <!-- hex --> | Body text on light background |
| `--color-muted` | <!-- hex --> | Captions, labels, placeholder text |
| `--color-border` | <!-- hex --> | Card borders, dividers, input outlines |
| `--color-error` | <!-- hex --> | Validation errors, destructive actions |

---

## Typography

<!-- guidance: Two font families is enough. One for headings (display weight, strong personality), one for body (readable at small sizes). Add a monospace font only if your product shows code, prompts, or structured data. The generator will suggest web-safe or Google Fonts options. -->

**Heading font:** ___________________________________________________________________________

**Body font:** ___________________________________________________________________________

**Mono font (optional):** ___________________________________________________________________________

### Type scale

<!-- guidance: Fill in the size and where each level is used. The generator will propose these; delete rows you will not use. -->

| Level | Size | Weight | Use |
|---|---|---|---|
| Display | <!-- px or rem --> | <!-- e.g. 700 --> | Hero title, page name |
| Heading 1 | | | Section titles |
| Heading 2 | | | Sub-section, card titles |
| Body large | | | Standard paragraphs |
| Body small | | | Supporting text, card body |
| Label | | | Tags, metadata, ALL-CAPS short strings |

**Letter spacing notes:** <!-- guidance: e.g. tight on headlines (-0.02em), wide on uppercase labels (0.12em) -->

___________________________________________________________________________

---

## Layout and spacing

<!-- guidance: Pick a max content width and a spacing scale. If you do not know, the generator will choose. Keep it simple — one column is fine for a prototype. -->

**Max content width:** ___________________________________________________________________________

**Base grid or column approach:** ___________________________________________________________________________

### Spacing scale

<!-- guidance: Six to eight steps. Each step should be roughly 1.4–1.6× the previous. -->

| Token | Value | Typical use |
|---|---|---|
| `--space-1` | <!-- e.g. 4px --> | Tightest inline gap |
| `--space-2` | | Label-to-icon gap, tight inline |
| `--space-3` | | Internal padding (buttons, chips) |
| `--space-4` | | Standard paragraph and list gap |
| `--space-5` | | Between related elements in a section |
| `--space-6` | | Between sections |
| `--space-7` | | Page top and bottom padding |

**Corner radius:** <!-- guidance: 0px for angular/minimal feel; 4–8px for neutral; 12–16px for friendly/soft. Pick one value and apply it everywhere. -->

___________________________________________________________________________

**Shadows / elevation:** <!-- guidance: Describe if and how you use shadow — e.g. "none — elevation is tonal only", "1 level of card shadow (0 2px 8px rgba(0,0,0,0.08))". -->

___________________________________________________________________________

---

## Component patterns

<!-- guidance: Describe the visual spec for the 3–5 components your product actually uses. Do not spec every possible UI element. Focus on the ones the builder tool will need to construct correctly. The generator will produce these based on your screen list and north star. -->

### Primary button

<!-- guidance: Background color, text color, padding, border radius, hover state. -->

___________________________________________________________________________

### Input / form field

<!-- guidance: Border style, focus state (color, width), placeholder style, error state. -->

___________________________________________________________________________

### Card

<!-- guidance: Background, border or shadow, padding, radius, any hover behavior. -->

___________________________________________________________________________

### Navigation (if applicable)

<!-- guidance: Top bar, sidebar, or tab bar — whichever your product uses. Background, height, item spacing. -->

___________________________________________________________________________

### [Add a fourth component your product needs]

<!-- guidance: Examples: data table, empty state, modal, tag/chip, avatar. Only spec what your build actually uses. -->

___________________________________________________________________________

---

## Accessibility

<!-- guidance: The generator should verify these. Check each one before handing DESIGN.MD to the builder. These are non-negotiable even in a prototype — they cost almost nothing to get right from the start. -->

- [ ] All text-on-background color pairs meet WCAG AA contrast (4.5:1 for body, 3:1 for large text / UI components). <!-- guidance: Use https://webaim.org/resources/contrastchecker/ to verify. -->
- [ ] Focus states are visible — not removed or hidden with `outline: none`. Specify the focus ring style: ___________________________________________________________________________
- [ ] Touch targets are at least 44x44px on mobile.
- [ ] Error states communicate in text, not color alone.
- [ ] All images have alt text; decorative images have `alt=""`.

---

## Ask the LLM

Paste these into Claude, ChatGPT, or Gemini to fill this doc through back-and-forth. Use them in order.

1. "I am building [product name and one-sentence description]. My creative north star is [paste your north star line]. Suggest a color palette for this product: 6–8 tokens, each with a hex value and a clear role (primary action, background, surface, body text, muted text, border, error). Explain the emotional rationale for each color choice in one line."

2. "Based on that palette, suggest two Google Fonts — one for headings, one for body text — that fit the [mood / north star]. For each font, name one alternative if the first is unavailable. Then give me a complete type scale: Display, H1, H2, Body Large, Body Small, Label — with px size, font weight, and one-line usage note for each."

3. "Now give me a spacing scale with 7 steps, starting at 4px. Show the multiplier pattern you used and name the typical use for each step. Also recommend a corner radius value and explain whether to use shadows or flat elevation for this product."

4. "Give me a detailed visual spec for these four components: primary button, form input field, card, and [your fourth component]. For each: background color using the tokens above, text color, border, padding, corner radius, hover state, and focus state. Format as a markdown table."

5. "Check this color palette for WCAG AA contrast compliance. List every foreground-on-background pair, its contrast ratio, and whether it passes AA for body text (4.5:1) or large text / UI (3:1). Flag any failures and suggest corrected hex values."

6. "Summarize the complete design system in one DESIGN.MD document using this structure: Creative north star, Color tokens table, Typography section with type scale table, Layout and spacing section with spacing scale table, Component patterns for the four components, Accessibility checklist. Use the values we agreed on above. Output raw markdown."

---

## Done when

- [ ] Creative north star is one clear sentence that a builder tool can act on.
- [ ] Color token table has 5 or more tokens, each with a hex value and a named role — no empty cells.
- [ ] Type scale table has at least 4 levels filled in with size and weight.
- [ ] At least 3 component patterns are specified with enough detail that a builder tool can render them without guessing.
- [ ] Accessibility checklist is complete — contrast ratios verified, focus state defined.
