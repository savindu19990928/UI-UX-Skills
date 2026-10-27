# WCAG 2.1 AA Accessibility Audit Checklist

A practical verification checklist for ensuring production UI passes WCAG 2.1 Level AA criteria.

## 1. Perceivable (Content must be perceptible to all senses)

### 1.1 Text Alternatives (Non-text Content - WCAG 1.1.1)
- [ ] Every informative `<img>` has a concise, descriptive `alt` attribute.
- [ ] Purely decorative images use `alt=""` or `aria-hidden="true"`.
- [ ] Icon-only buttons (search, close, hamburger, social) have an explicit `aria-label` or visually-hidden screen reader text (`.sr-only`).
- [ ] Complex SVGs contain `<title>` and `<desc>` or an `aria-label` on the `<svg>` container.

### 1.2 Contrast Ratios (Minimum Contrast - WCAG 1.4.3)
- [ ] **Body text (< 18pt or < 14pt bold)**: Contrast ratio ≥ **4.5:1** against its background.
- [ ] **Large text (≥ 18pt or ≥ 14pt bold)**: Contrast ratio ≥ **3.0:1** against its background.
- [ ] **UI Components & Graphical Objects (WCAG 1.4.11)**: Interactive borders, checkmarks, input outlines, and icons have ≥ **3.0:1** contrast against adjacent backgrounds.
- [ ] **Dark Mode**: Avoid pure white (`#FFFFFF`) text on pure black (`#000000`) to reduce halation; use off-white (e.g. `#F8FAFC` on `#0F172A`).
- [ ] **Placeholder Text**: Form placeholders must NOT be the sole label, and if used, should still meet readable contrast or be accompanied by visible floating labels.

### 1.3 Text Resizing & Reflow (WCAG 1.4.4 & 1.4.10)
- [ ] Page can be zoomed to **200%** in the browser without clipping text or breaking functionality.
- [ ] Content reflows into a single column at **320px width** without requiring horizontal scrolling (except for data tables or code blocks).
- [ ] Do not disable pinch-to-zoom: ensure `<meta name="viewport" content="width=device-width, initial-scale=1">` without `user-scalable=no` or `maximum-scale=1`.

---

## 2. Operable (UI components and navigation must be operable)

### 2.1 Keyboard Accessibility (WCAG 2.1.1 & 2.1.2)
- [ ] Every interactive control (links, buttons, inputs, modals, tabs, accordions) can be reached and activated using only the keyboard (`Tab`, `Shift+Tab`, `Enter`, `Space`, `Arrow keys`, `Escape`).
- [ ] **No Keyboard Traps**: Focus can enter and freely exit any interactive widget or modal.
- [ ] **Modal Dialog Focus Trap**: When a modal is open, focus is trapped *within* the modal; pressing `Escape` closes the modal and returns focus to the trigger button.
- [ ] **Skip Links**: Include a skip-to-content link (`<a href="#main" class="sr-only focus:not-sr-only">Skip to main content</a>`) as the first focusable element.

### 2.2 Focus Visibility (WCAG 2.4.7)
- [ ] Never remove focus outlines using `outline: none` without providing an equal or superior visible `:focus-visible` ring.
- [ ] Focus ring has at least **2px width** with at least **3:1 contrast** against both the element and background, ideally with a 2px offset (`outline-offset: 2px`).

### 2.3 Target Size & Spacing (WCAG 2.5.5 / 2.5.8)
- [ ] Mobile tap targets are at least **44 × 44px** (iOS HIG) or **48 × 48dp** (Android Material).
- [ ] Desktop interactive elements meet at least **24 × 24px** with adequate padding.
- [ ] Adjacent buttons and links have at least **8px spacing** to prevent mis-clicks.

### 2.4 Motion & Animation (WCAG 2.3.3)
- [ ] Respect user preference for reduced motion:
  ```css
  @media (prefers-reduced-motion: reduce) {
    *, ::before, ::after {
      animation-duration: 0.01ms !important;
      animation-iteration-count: 1 !important;
      transition-duration: 0.01ms !important;
      scroll-behavior: auto !important;
    }
  }
  ```
- [ ] Avoid animations that flash more than 3 times in any 1-second period (seizure risk).

---

## 3. Understandable (Information and operation must be understandable)

### 3.1 Language & Headings (WCAG 3.1.1 & 2.4.6)
- [ ] HTML document specifies language: `<html lang="en">`.
- [ ] Exactly **one** `<h1>` per page representing the page title.
- [ ] Headings follow a strict nested order (`<h1>` → `<h2>` → `<h3>`) without skipping levels for visual styling.

### 3.2 Form Usability & Error Handling (WCAG 3.3.1 & 3.3.2)
- [ ] Every form field has a permanently visible `<label>` bound via `for="id"`.
- [ ] Required fields are programmatically indicated via `required` or `aria-required="true"`, with a visible indicator (e.g. `*`).
- [ ] Error messages are placed directly adjacent to the input field, linked via `aria-describedby="error-id"`, and highlighted with both color and an icon or text description (never color alone).
- [ ] Inputs have appropriate autocomplete attributes (`autocomplete="email"`, `autocomplete="tel"`, etc.).

---

## 4. Robust (Content must be robust enough for diverse user agents)

### 4.1 Valid Markup & ARIA Roles (WCAG 4.1.2)
- [ ] Use native HTML elements (`<button>`, `<a>`, `<input>`, `<select>`) whenever possible.
- [ ] Custom controls use appropriate ARIA roles (`role="dialog"`, `role="tablist"`, `role="combobox"`).
- [ ] Dynamic updates communicate state changes with `aria-live="polite"` (e.g. notification toasts, search result counts).
- [ ] Ensure all `id` attributes on the page are unique.
