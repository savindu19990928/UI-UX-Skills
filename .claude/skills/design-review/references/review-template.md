# Design Review Audit Report Template

Use this template when reporting the findings of a design review or accessibility audit.

---

# Design Review Report

**Target:** `http://localhost:3000/dashboard` (or file path / screen)  
**Date:** 2026-10-28  
**Reviewer:** Design Review System  
**Verdict:** `[SHIP]` / `[SHIP WITH FIXES]` / `[NEEDS WORK]`  
**Viewports Tested:** 360px (mobile compact), 390px (mobile standard), 768px (tablet), 1024px (laptop), 1440px (desktop), 1920px (ultrawide)

---

## Executive Summary
A 2–3 sentence overview of the page's visual quality, key strengths, and highest-priority fixes required before shipping.

---

## 1. 🚨 Blockers (Must fix before deployment)
*Issues that break core usability, cause layout crashes, or violate WCAG 2.1 AA criteria.*

- **[Criterion / Category]: [Short Title]**
  - **Observed Defect:** *Describe exactly what was seen or measured (e.g. text contrast is 2.8:1 on primary CTA; button lacks keyboard focus outline; page scrolls horizontally at 360px).*
  - **Impact:** *Why this severely impairs users (e.g. keyboard users cannot navigate; low-vision users cannot read button text).*
  - **Fix:** *Specific token, CSS, or markup change to resolve.*
  - **Evidence:** *Screenshot filename, DOM selector, or computed CSS value.*

---

## 2. ⚠️ High Severity (Fix before merge)
*Noticeable defects that degrade user experience or violate secondary standards.*

- **[Criterion / Category]: [Short Title]**
  - **Observed Defect:** ...
  - **Impact:** ...
  - **Fix:** ...

---

## 3. 💡 Medium Severity (Polish & refinement)
*Polish enhancements that elevate the product from functional to premium.*

- **[Criterion / Category]: [Short Title]**
  - **Observed Defect:** ...
  - **Enhancement:** ...

---

## 4. 🔍 Nitpicks
*Minor pixel-level or token observations.*

- Nit: [e.g. Icon alignment is 1px off-center vertically inside button]
- Nit: [e.g. Card padding could increase from 20px to 24px to match design system grid]

---

## 5. ✅ What's Working Well
*Celebrate strong design decisions so they are not accidentally undone in future refactors.*

- **[Feature / Pattern]**: Excellent typography hierarchy and responsive card reflow.
- **[Aesthetic]**: Distinctive visual tone with appropriate whitespace and crisp contrast.
- **[Interaction]**: Smooth, subtle micro-interactions with reduced-motion compliance.

---

## Viewport Breakdown

| Viewport | Width × Height | Status | Key Observation |
|----------|----------------|--------|-----------------|
| Mobile Compact | 360 × 800 | Passed / Issues | Single column layout, tap targets verified |
| Mobile Standard | 390 × 844 | Passed / Issues | Smooth reflow, safe area respected |
| Tablet | 768 × 1024 | Passed / Issues | 2-column grid reflow, navigation collapsed |
| Laptop | 1024 × 768 | Passed / Issues | Full desktop header, sidebar active |
| Desktop Baseline | 1440 × 900 | Passed / Issues | Contained max-width, balanced spacing |
| Ultrawide | 1920 × 1080 | Passed / Issues | Content centered, no stretch distortion |
