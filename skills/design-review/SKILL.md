---
name: design-review
description: "Expert design reviewer for web and mobile interfaces. Conducts 7-phase evidence-based reviews covering visual quality, WCAG 2.1 AA accessibility (contrast, keyboard focus, screen readers), responsiveness across 5 viewports (360px→1920px), interaction feedback, layout shift (CLS), tap targets (≥44px), and error prevention."
argument-hint: "[url or file] [optional focus]"
license: MIT
metadata:
  author: nextlevelbuilder
  version: "2.0.0"
---

# Design Review & UI/UX Audit

An expert product design reviewer system that verifies live interfaces across viewports, interaction states, and accessibility standards. Evaluates the live rendered experience before code inspection to ensure human-grade quality and strict WCAG 2.1 AA compliance.

## When to Apply

- Proactively after any frontend, component, or layout modification
- Before marking any UI/UX task as complete
- When conducting an audit on a live URL, dev-server, or static HTML file
- To verify accessibility compliance (WCAG 2.1 AA)
- To check responsive reflow and mobile tap targets (360px, 390px, 768px, 1024px, 1440px, 1920px)

## Operating Principle: Assess the Live Experience First

Interact with the running UI like a real user before analyzing source code. Findings must be grounded in observable facts (measured contrast ratios, layout shifts, element overlaps, console warnings, or screenshots) — never assumptions.

## The 7-Phase Design Review Process

```
Phase 0: Setup & Baseline (Console, 1440×900 rendering)
   ↓
Phase 1: Interaction & User Flows (States, buttons, inputs, feedback)
   ↓
Phase 2: Responsiveness (360px mobile → 1920px ultrawide reflow)
   ↓
Phase 3: Visual Polish (Token rhythm, typography hierarchy, alignment)
   ↓
Phase 4: WCAG 2.1 AA Accessibility (Contrast ≥4.5:1, keyboard nav, focus rings)
   ↓
Phase 5: Robustness & Edge Cases (Long text, empty states, error boundaries)
   ↓
Phase 6: Health & Performance (CLS < 0.1, unsized media, 404s, clean console)
```

### Phase 0 — Setup & Baseline
- Open target at desktop baseline (1440×900).
- Confirm rendering and check for console errors/warnings immediately.
- Note any render-blocking resources or initial visual glitches.

### Phase 1 — Interaction & User Flows
- Exercise primary user journeys: clicking buttons, opening dropdowns/menus, submitting forms.
- Verify interactive states exist and clearly differ:
  - Default / Idle
  - Hover (subtle transition 150–250ms)
  - Focus-visible (distinct ring, 2px offset minimum)
  - Active / Pressed
  - Disabled (`cursor: not-allowed`, muted opacity, no ghost events)
  - Loading states (skeleton or spinner, button disabled during submit)
> [!TIP]
> For complex gesture handling, spring physics, or motion jank debugging, refer to the **`better-animation`** skill.

### Phase 2 — Responsiveness Across 5 Viewports
Verify layout across all 5 standard tiers:
1. **Mobile Compact (360px & 390px)**: Single column, touch targets ≥ 44×44px, ≥ 8px spacing, hamburger or bottom navigation, zero horizontal scrolling.
2. **Tablet (768px)**: 2-column grids, adaptive navigation, comfortable spacing.
3. **Laptop (1024px)**: Full navigation, multi-column cards, sidebar reflow.
4. **Desktop (1440px)**: Primary design target, contained max-width (e.g. 1280–1400px), balanced whitespace.
5. **Ultrawide (1920px)**: Centered containers with max-width boundaries; no text spanning thousands of pixels.

### Phase 3 — Visual Polish & Token Discipline
- **Spacing Rhythm**: 4px / 8px grid alignment; consistent gaps across cards and sections.
- **Typography Scale**: Maximum 1 `h1` per page; logical heading hierarchy (`h1` → `h2` → `h3`); body text base ≥ 16px; line-height 1.5–1.6 for body.
- **Design Tokens**: Verified use of semantic tokens; absence of arbitrary hardcoded one-off colors.
- **Visual Distinction**: Avoid generic AI defaults; ensure clear hierarchy and intentional styling.

### Phase 4 — WCAG 2.1 AA Accessibility
- **Contrast Ratios**: Normal body text ≥ 4.5:1; large text (≥18pt or bold ≥14pt) ≥ 3:1; UI components and borders ≥ 3:1.
- **Keyboard Navigation**: Full page operable via Tab / Shift+Tab; zero keyboard traps; visible `:focus-visible` styling on every control.
- **Semantic HTML & Screen Readers**: Correct semantic landmarks (`<main>`, `<nav>`, `<header>`, `<footer>`); meaningful `alt` text on images (`alt=""` for decorative); accessible names on all icon buttons (`aria-label`).
- **Motion**: Honor `prefers-reduced-motion: reduce` by replacing motion with static state changes or opacity fades.
> [!NOTE]
> For full compliance audits, automated axe-core/Lighthouse scans, and screen reader manual testing, refer to the dedicated **`audit-a11y`** skill.

### Phase 5 — Robustness & Edge Cases
- Test extreme text strings: very long product titles, user names, URLs (ensure wrapping/ellipsis, no container clipping).
- Test empty states: blank lists, search with zero results, empty carts.
- Test form validation: clear error messages placed directly beside the invalid input with red/destructive accent and descriptive text.

### Phase 6 — Console & Health
- Ensure zero uncaught JavaScript exceptions or failed network requests (404s).
- Verify layout stability: all `<img>` tags specify `width` and `height` attributes to prevent Cumulative Layout Shift (CLS < 0.1).

---

## Automated Heuristic Audit Tool

Run the standalone audit script for instant automated analysis and multi-viewport screenshots:

```bash
# Audit a running local dev server
node scripts/design-audit.mjs --url http://localhost:3000

# Audit a static HTML file
node scripts/design-audit.mjs --file ./index.html --out audit-results
```

The script automatically tests:
- Horizontal scroll overflow
- Unsized media (CLS risk)
- Missing `alt` attributes
- Mobile tap targets < 44×44px
- Missing visible focus indicators
- Controls missing accessible names (`aria-label`)
- Approximate contrast ratio pass
- Multi-viewport screenshots (360px, 390px, 768px, 1024px, 1440px, 1920px)

---

## Review Output Format

Structure all findings using this standardized template:

```markdown
## Design Review: [Target Page / Component]
**Verdict:** [Ship / Ship with Fixes / Needs Work]
**Viewports Audited:** 360px, 390px, 768px, 1024px, 1440px, 1920px

### 🚨 Blockers (Critical: Breaks usability or fails WCAG AA — must fix)
- [Observation] → [Root Cause / WCAG Criterion] → [Concrete Fix] (Evidence: screenshot / DOM element)

### ⚠️ High (Significant: High-priority polish before merge)
- [Observation] → [Why it fails] → [Fix]

### 💡 Medium (Polish: Noticeably improves user experience)
- [Observation] → [Suggested enhancement]

### 🔍 Nitpicks (Prefix with "Nit:")
- Nit: [Minor alignment / spacing adjustment]

### ✅ What's Working
- [Call out intentional, well-executed design decisions so they are preserved]
```
