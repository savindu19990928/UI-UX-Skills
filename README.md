# 🎨 Pure UI/UX Skill Set for AI Coding Assistants

A curated, high-precision skill set containing **only UI/UX design intelligence, styling, token architecture, motion, and accessibility audit capabilities**, extracted and refined from [ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill).

All non-UI/UX bloat (marketing banners, pitch deck slides, corporate brand messaging, logo generation, CIP stationery, and legacy backend/desktop stacks) has been removed.

---

## 🚀 The Complete UI/UX Skill Suite

| Skill | Directory | Primary Role |
|---|---|---|
| **`ui-ux-pro-max`** | [`skills/ui-ux-pro-max`](./skills/ui-ux-pro-max) | **Design Intelligence & Decision Engine**: 79 UI styles, 192 color palettes, 74 font pairings, 119 UX guidelines, 34 landing patterns, 25 chart types, 105 SVG icons, 17 motion presets, and automated design system generation (`--design-system`). |
| **`ui-styling`** | [`skills/ui-styling`](./skills/ui-styling) | **Component & Utility Styling**: Accessible component engineering with shadcn/ui & Radix UI primitives, Tailwind CSS utility styling, mobile-first responsive breakpoints, and dark mode theming. |
| **`design-system`** | [`skills/design-system`](./skills/design-system) | **Token Architecture & Specs**: 3-Layer Design Token Architecture (Primitive → Semantic → Component), CSS variables compiler (`generate-tokens.cjs`), Tailwind theme exporter, and token linting (`validate-tokens.cjs`). |
| **`design-review`** | [`skills/design-review`](./skills/design-review) | **Multi-Viewport Quality Audit**: 7-Phase UI/UX and WCAG 2.1 AA review system, viewport verification (360px→1920px), and automated heuristic audit script (`design-audit.mjs`). |
| **`better-animation`** | [`skills/better-animation`](./skills/better-animation) | **UI Motion & Micro-Interactions** *(from `AnimationUI.md`)*: Fluid transitions, interruptible gestures, spring physics, performance budgets (avoiding layout/reflow jank), and reduced-motion accessibility. |
| **`audit-a11y`** | [`skills/audit-a11y`](./skills/audit-a11y) | **Dedicated WCAG 2.1 AA Compliance** *(from `AuditUI.md`)*: Keyboard navigation, focus traps, screen reader testing, ARIA roles, color contrast validation, and structured audit reporting. |

---

## 🧹 What Was Kept vs. What Was Omitted

### ✅ Retained (Pure UI & UX)
- **Visual Design & Aesthetics**: 79 searchable styles (Glassmorphism, Brutalism, Claymorphism, Minimalism, Neumorphism, Bento Grid, Dark Mode, etc.).
- **Color Architecture**: 192 industry-specific palettes, semantic color mappings, light/dark contrast tokens.
- **Typography**: 74 font pairings, Google Fonts import URLs, typographic scale and line-height standards.
- **Usability & UX Rules**: 119 UX guidelines (touch targets, keyboard focus, error handling, form design, feedback, cognitive load).
- **Design System Generator**: BM25 + regex reasoning engine to generate end-to-end design systems with design dials (`--variance`, `--motion`, `--density`).
- **Layout & Structure**: 34 landing page conversion patterns and section sequencing.
- **Mobile & App UX**: Safe areas, touch gestures, mobile polish checklists.
- **Micro-Interactions & Animation**: 17 GSAP motion presets, spring physics, and reduced-motion compliance rules.
- **Data Visualization**: 25 chart types with accessibility grades and color guidance.
- **Accessible Components**: Radix UI / shadcn/ui patterns (Dialogs, Sheets, Forms, Dropdowns, Tables).
- **Design Tokens**: 3-layer token hierarchy and automated token validation.
- **Quality Audit**: 7-phase design review and multi-viewport automated testing.

### ❌ Omitted (Non-UI/UX Disciplines)
- **Brand Strategy & Copywriting**: Removed `brand` skill (tone of voice, marketing messaging, content strategy).
- **Presentation Slides**: Removed `slides` skill and slide generation scripts/CSVs (pitch decks, business presentations).
- **Ad & Social Banners**: Removed `banner-design` skill (Facebook covers, YouTube channel art, Google Display Ads, print banners).
- **Graphic Design & Corporate Identity**: Removed `design` skill subroutines for AI logo generation and Corporate Identity Program (CIP letterheads, business cards, office reception mockups).
- **Social Media Marketing Images**: Removed Instagram/Pinterest social photo generators.
- **Backend & Legacy Desktop Frameworks**: Pruned `stacks/laravel.csv` (PHP backend) and legacy desktop stacks (`wpf.csv`, `winui.csv`, `uwp.csv`, `avalonia.csv`, `uno.csv`, `javafx.csv`).
- **Code Performance Debugging**: Removed `react-performance.csv` (memoization, re-render debugging, bundle splitting).

---

## 📁 Repository Structure

```
UI-UX-Skills/
├── README.md                                  # Complete documentation
├── package.json                               # Workspace runner scripts
├── scripts/                                   # Workspace-level convenience scripts
│   ├── search.py                              # Direct runner for UI/UX search
│   └── design-audit.mjs                       # Standalone multi-viewport audit tool
├── skills/                                    # Universal Agent Skills directory
│   ├── ui-ux-pro-max/                         # Design Intelligence & Search Engine
│   │   ├── SKILL.md
│   │   ├── data/                              # Cleaned UI/UX CSV databases
│   │   ├── scripts/                           # BM25 search engine & design system generator
│   │   └── references/                        # Quick reference & Pro rules
│   ├── ui-styling/                            # Component Styling (shadcn + Tailwind)
│   │   ├── SKILL.md
│   │   ├── references/                        # Components, accessibility, theming
│   │   └── scripts/                           # shadcn_add.py, tailwind_config_gen.py
│   ├── design-system/                         # Token Architecture & Component Specs
│   │   ├── SKILL.md
│   │   ├── references/                        # Token architecture, states, specs
│   │   ├── scripts/                           # generate-tokens.cjs, validate-tokens.cjs
│   │   └── templates/                         # design-tokens-starter.json
│   ├── design-review/                         # 7-Phase UI/UX Review & Audit
│   │   ├── SKILL.md
│   │   ├── references/                        # Review template & checklists
│   │   └── scripts/                           # design-audit.mjs
│   ├── better-animation/                      # UI Motion & Micro-Interactions (AnimationUI.md)
│   │   └── SKILL.md
│   └── audit-a11y/                            # WCAG 2.1 AA Compliance Audit (AuditUI.md)
│       ├── SKILL.md
│       └── references/                        # WCAG AA checklist
├── .agents/skills/                            # Auto-discovered by Antigravity IDE & Gemini
└── .claude/skills/                            # Auto-discovered by Claude Code
```

---

## ⚡ Quick Start & Usage Examples

### 1. Generate an Automated Design System
Generate a complete, tailored design system (palette, typography, landing pattern, styles, effects, anti-patterns):
```bash
python scripts/search.py "fintech dashboard" --design-system -p "FinFlow"
```

Add design dials to tune variance, motion intensity, and visual density (1–10 scale):
```bash
python scripts/search.py "health wellness app" --design-system --variance 8 --motion 4 --density 6
```

### 2. Search Specific UI/UX Domains
Query individual domains for targeted guidance:
```bash
# UX Guidelines (Accessibility, touch targets, forms)
python scripts/search.py "touch target" --domain ux

# Color Palettes (Tailored by product type)
python scripts/search.py "saas analytics" --domain color

# Typography Pairings (Google Fonts pairings & import links)
python scripts/search.py "modern editorial" --domain typography

# UI Styles (Glassmorphism, Brutalism, Bento Grid, Dark Mode)
python scripts/search.py "dark mode" --domain style

# Data Visualization & Charts
python scripts/search.py "time series" --domain chart

# Mobile & App Touch Interface
python scripts/search.py "safe area" --domain web
```

### 3. Generate CSS Variables from Design Tokens
Compile JSON token files into clean CSS variables with dark mode support:
```bash
node skills/design-system/scripts/generate-tokens.cjs --config skills/design-system/templates/design-tokens-starter.json -o tokens.css
```

Export tokens directly into a Tailwind CSS theme snippet:
```bash
node skills/design-system/scripts/generate-tokens.cjs --config skills/design-system/templates/design-tokens-starter.json --format tailwind
```

### 4. Scan Code for Hardcoded Value Violations
Ensure developers and AI agents adhere to token discipline instead of hardcoding random hex colors:
```bash
node skills/design-system/scripts/validate-tokens.cjs --dir src/
```

### 5. Run a 7-Phase Heuristic UI/UX & Accessibility Audit
Test any running web application or local HTML file across 6 viewport tiers (360px, 390px, 768px, 1024px, 1440px, 1920px):
```bash
# Audit a running dev server
node scripts/design-audit.mjs --url http://localhost:3000

# Audit a static HTML file
node scripts/design-audit.mjs --file ./index.html --out audit-results
```

The audit automatically detects:
- Horizontal scroll overflow on compact devices
- Unsized images (Cumulative Layout Shift risk)
- Missing image `alt` attributes
- Mobile tap targets < 44×44px
- Interactive elements missing visible focus indicators
- Unlabeled buttons or controls missing `aria-label`
- Text contrast ratio approximation

---

## 🛠 Platform Compatibility

This skill set works natively across all major AI agent environments:

- **Google Antigravity IDE**: Discovered automatically via `.agents/skills/`.
- **Gemini CLI / Studio**: Discovered via `.agents/skills/`.
- **Claude Code**: Discovered via `.claude/skills/`.
- **Cursor / Windsurf / Trae / RooCode / Copilot**: Discovered via root `skills/`.

---

## 📄 License
MIT License. Original data and intelligence curated by NextLevelBuilder, refactored and streamlined for dedicated UI/UX workflows.
