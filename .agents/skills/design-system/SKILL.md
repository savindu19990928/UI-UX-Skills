---
name: design-system
description: "Token architecture, component specifications, and design system engineering. Three-layer tokens (primitive → semantic → component), CSS custom properties, spacing & typography scales, component state specifications, Tailwind theme integration, and token validation."
argument-hint: "[component or token]"
license: MIT
metadata:
  author: nextlevelbuilder
  version: "2.0.0"
---

# Design System Engineering

Systematic design token architecture, component specifications, CSS variables, and design-to-code automation.

## When to Use

- Creating or refactoring design tokens (colors, spacing, typography, elevation, radii)
- Implementing a 3-layer design token architecture (Primitive → Semantic → Component)
- Generating CSS variables (`:root`, `.dark`) from token JSON specifications
- Exporting semantic tokens into Tailwind CSS theme configuration
- Defining component specifications and interaction states (Default, Hover, Focus, Active, Disabled)
- Auditing source code for hardcoded color/spacing values that bypass tokens
- Establishing design consistency across multi-page applications

## Token Architecture

Read: `references/token-architecture.md`

### Three-Layer Structure

```
Primitive (raw values: palette hex, raw rem/px)
       ↓
Semantic (intent & purpose aliases: primary, background, surface, muted, destructive)
       ↓
Component (component-scoped bindings: button-bg, card-border, input-focus-ring)
```

**Example:**
```css
/* 1. Primitive Layer */
--color-blue-600: #2563EB;
--spacing-4: 1rem;
--radius-md: 0.375rem;

/* 2. Semantic Layer */
--color-primary: var(--color-blue-600);
--color-primary-fg: #FFFFFF;
--color-background: #020617;
--color-foreground: #F8FAFC;

/* 3. Component Layer */
--button-primary-bg: var(--color-primary);
--button-primary-text: var(--color-primary-fg);
--card-bg: var(--color-background);
```

## Quick Start

### 1. Starter Token Configuration
Use `templates/design-tokens-starter.json` as the baseline schema conforming to the Design Tokens Community Group specification.

### 2. Generate CSS Variables
```bash
node scripts/generate-tokens.cjs --config tokens.json -o tokens.css
```
Generates `:root` variables for primitives, semantic tokens, component tokens, and `.dark` variables for dark mode overrides.

### 3. Generate Tailwind Theme Config
```bash
node scripts/generate-tokens.cjs --config tokens.json --format tailwind
```

### 4. Validate Token Compliance (Find hardcoded values in code)
```bash
node scripts/validate-tokens.cjs --dir src/
```

## Component Specification Pattern

Every interactive component must document tokens across all interaction states:

| Property | Default | Hover | Focus-Visible | Active | Disabled |
|----------|---------|-------|---------------|--------|----------|
| Background | `--btn-primary-bg` | `--btn-primary-hover` | `--btn-primary-bg` | `--btn-primary-active` | `--btn-muted-bg` |
| Text | `--btn-primary-fg` | `--btn-primary-fg` | `--btn-primary-fg` | `--btn-primary-fg` | `--btn-muted-fg` |
| Border | `--btn-primary-border` | `--btn-primary-border` | `--ring-color` (2px offset) | `--btn-primary-border` | `--btn-muted-border` |
| Shadow | `--shadow-sm` | `--shadow-md` | `--shadow-sm` + focus ring | `--shadow-inner` | none |
| Cursor | `pointer` | `pointer` | `pointer` | `pointer` | `not-allowed` |

## Reference Guides

| Topic | Reference File | Purpose |
|-------|----------------|---------|
| Token Architecture | `references/token-architecture.md` | Core 3-layer architecture theory & design decisions |
| Primitive Tokens | `references/primitive-tokens.md` | Scales for color ramps, modular spacing, and typography scales |
| Semantic Tokens | `references/semantic-tokens.md` | Intent mappings for light/dark themes and accessibility |
| Component Tokens | `references/component-tokens.md` | Component-level token naming patterns and encapsulation |
| Component Specs | `references/component-specs.md` | Layout, padding, states, and responsive specifications |
| States & Variants | `references/states-and-variants.md` | Micro-interactions, hover/focus/active state matrices |
| Tailwind Integration | `references/tailwind-integration.md` | Hooking design tokens into Tailwind v3 config & Tailwind v4 `@theme` |

## Scripts & Tools

| Script | Command | Purpose |
|--------|---------|---------|
| `generate-tokens.cjs` | `node scripts/generate-tokens.cjs -c tokens.json -o tokens.css` | Compiles JSON tokens into CSS variables and Tailwind colors |
| `validate-tokens.cjs` | `node scripts/validate-tokens.cjs --dir src/` | Scans source files for raw hex/pixel values that break token discipline |
| `embed-tokens.cjs` | `node scripts/embed-tokens.cjs` | Embeds tokens directly into application CSS roots |

## Integration with Other UI/UX Skills

- **`ui-ux-pro-max`**: Pull industry-tested color palettes (`--domain color`) and typography pairs (`--domain typography`) into the primitive & semantic token layers.
- **`ui-styling`**: Map semantic tokens directly to Radix UI / shadcn/ui components and Tailwind CSS utilities.
- **`design-review`**: Audit live components to guarantee token consistency, WCAG AA contrast (≥4.5:1), and visible focus rings across all viewports.
