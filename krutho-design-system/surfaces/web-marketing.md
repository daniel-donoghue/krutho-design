# Krutho Marketing Website Surface

Last edit 17th April 2026

First-pass specification. Values in this document are proposals for a working base. The structure is settled. The specific token selections are starting points for refinement.

---

## Grounding Statement

This document operates under the Krutho Design Philosophy. The terms precision, correctness, verifiability, and truth are used throughout in the senses defined there. Every decision traces to a reason that excludes the alternatives.

This is a surface specification. It extends the Krutho foundation for one specific surface: the marketing website. Foundation documents define universal primitives. This document defines rules that apply to this surface only. Decisions here do not propagate back to the foundation.

---

## Dependencies

This document depends on:

- Krutho Design Philosophy
- Krutho Colour System
- Krutho Spacing System
- Krutho Typography System
- Krutho Grid System
- Krutho Layout System
- Krutho Wordmark

All token references resolve to the values defined in those documents. This document introduces no primitives.

---

## Register

**Register:** Expressive.

The marketing website operates with low information density by intent. White space is the primary structural element. Spatial intervals between elements are generous. These are the conditions that define the Expressive register in the Krutho Spacing System.

The register governs the spatial character of the whole site. Column count adapts to viewport within this register; the adaptation is recorded in the Breakpoints section. A viewport that physically cannot hold 16 columns does not invalidate the register: the register is the spatial intent, and the column count is the mechanism by which that intent is realised at each viewport.

---

## Breakpoints

Three breakpoints are defined. Each declares a column count, margin, gutter, and grid value. The grid value satisfies the alignment condition defined in the Krutho Grid System.

| Breakpoint | Viewport range   | Columns | Margin   | Gutter   | Grid     |
|------------|------------------|---------|----------|----------|----------|
| Small      | up to 640px      | 4       | space-16 | space-16 | grid-16  |
| Medium     | 640px to 1024px  | 12      | space-32 | space-16 | grid-16  |
| Large      | 1024px and above | 16      | space-64 | space-16 | grid-16  |

**Width derivation.** 640px is the point at which a body-text column at the body anchor exits comfortable single-column measure and a 12-column composition becomes physically realisable. 1024px is the point at which a 16-column Expressive composition holds without individual columns collapsing below a usable working width. Both widths are multiples of the grid value.

**Column count derivation.** Small uses 4 columns: the minimum admitted column count in the layout system. 12 and 16 are the admitted counts above 4. Medium uses 12 because 16 at this viewport range reduces individual column width below a usable working width. Large uses 16: the admitted count for Expressive.

**Alignment condition.** Grid-16 divides space-16, space-32, and space-64 exactly. The condition is satisfied at all three breakpoints with a single grid value, which is the preferred outcome.

---

## Typography Roles

Each role declares: element attachment, tier, type token at each breakpoint, line height variant, weight, and use condition.

Roles are grouped by function. Within each group, the role set is what this surface needs. Roles not listed are not admitted on this surface.

### Structural

| Role      | Elements | Tier | Small     | Medium    | Large     | Weight |
|-----------|----------|------|-----------|-----------|-----------|--------|
| Heading 1 | `<h1>`   | 1    | type-40   | type-64   | type-80   | 500    |
| Heading 2 | `<h2>`   | 1    | type-28   | type-40   | type-48   | 500    |
| Heading 3 | `<h3>`   | 1    | type-20   | type-24   | type-28   | 500    |
| Eyebrow   | `<p>` with role class | 1 | type-14 | type-14 | type-14 | 500    |

Heading 1 is the hero-scale heading. One per page. Heading 2 marks major sections. Heading 3 marks subsections within sections. Heading levels below Heading 3 are not admitted on this surface; if a page appears to require `<h4>`, the content structure is reconsidered.

Eyebrow sits above a heading and classifies it. Size holds across breakpoints because its function is reference, not hierarchy.

### Body

| Role       | Elements | Tier | Small     | Medium    | Large     | Weight |
|------------|----------|------|-----------|-----------|-----------|--------|
| Lead       | `<p>` with role class | 1 | type-18 | type-20 | type-24 | 400    |
| Body       | `<p>`    | 1    | type-16   | type-16   | type-16   | 400    |
| Body small | `<p>` with role class, `<small>` | 1 | type-14 | type-14 | type-14 | 400    |
| Caption    | `<figcaption>`, `<p>` with role class | 1 | type-12 | type-12 | type-12 | 400    |

Body is the anchor. It holds across all breakpoints. Reason: the browser default is 16px; most assistive configurations are tuned to it; body text is the most repeated element on the surface and benefits from stability across viewports. Hierarchy is carried by heading scale, which does vary.

Lead sits between a heading and body and carries introductory text. It scales with breakpoint.

### Inline semantics

| Role    | Elements | Tier | Style         | Weight |
|---------|----------|------|---------------|--------|
| Link    | `<a>`    | 1    | upright       | 400 in body, inherits in headings |
| Strong  | `<strong>` | 1  | upright       | 500    |
| Em      | `<em>`, `<cite>`, `<i>` | 1 | italic | 400 |

Italic on this surface is admitted on `<em>`, `<cite>`, and `<i>` for reader-convention reasons recorded in earlier sessions. Composed cases (`<strong><em>`) render italic at weight 500.

Link colour and underline treatment are defined in the Link Styling section below.

### Technical (Tier 2)

| Role        | Elements | Tier | Small   | Medium  | Large   | Weight |
|-------------|----------|------|---------|---------|---------|--------|
| Inline code | `<code>` inside prose | 2 | type-14 | type-14 | type-14 | 400    |
| Block code  | `<pre><code>` | 2 | type-14 | type-14 | type-14 | 400    |

Tier 2 sizes sit one step below adjacent body text. Spline Mono at the same pixel size as Spline Sans reads slightly heavier because of its fixed-width construction. Sizing one step below compensates and produces optical parity in running prose.

Block code in prose context sits inside a bordered container with its own padding. Container treatment is a colour and component decision, not a typography decision; it is flagged for refinement.

### UI and navigation

| Role        | Elements | Tier | Small   | Medium  | Large   | Weight |
|-------------|----------|------|---------|---------|---------|--------|
| Button      | `<button>`, `<a>` with role class | 1 | type-16 | type-16 | type-16 | 500    |
| Nav primary | `<a>` inside primary nav | 1 | type-16 | type-16 | type-16 | 400 |
| Footer text | `<p>`, `<a>` inside footer | 1 | type-14 | type-14 | type-14 | 400 |

Tier 3 (Enra) is not assigned to any role in this first pass. If a hero tagline or a pull quote requires interpretive weight beyond Tier 1, Tier 3 is admissible under the typography system's admission test. This is flagged for refinement.

### Line Height

Line height variant for each role is derived by rule. Variants (Tight, Default, Loose) are defined in the Krutho Typography System.

**Headings (Heading 1, Heading 2, Heading 3).** Tight when the rendered size is above 40px. Default when the rendered size is 40px or below.

40px is the zone boundary between the mid zone and the display zone, derived from the 10% hierarchy threshold. The perceptual behaviour of line height tracks this boundary. At display sizes, the Default 1.4 ratio produces a vertical interval large enough to read as disconnection between lines; Tight at 1.2 produces a deliberate, controlled interval. Below the display zone, Tight produces crowding; Default provides reliable clearance. The zone boundary is the threshold at which the variant changes. This reason excludes the alternatives.

Applied across the breakpoints:

| Role      | Small             | Medium            | Large           |
|-----------|-------------------|-------------------|-----------------|
| Heading 1 | default (type-40) | tight (type-64)   | tight (type-80) |
| Heading 2 | default (type-28) | default (type-40) | tight (type-48) |
| Heading 3 | default (type-20) | default (type-24) | default (type-28) |

**Prose body roles (Lead, Body, Body small).** Loose.

The surface operates in the Expressive register. Expressive spatial character calls for generous vertical breathing room between lines of running prose. Loose at 1.6 reinforces that character. Default at 1.4 is the universally comfortable ratio without register-specific character. Loose is the register-specific selection for prose on this surface. This reason applies uniformly to the three prose roles and excludes other variants.

**Other roles.**

| Role         | Variant | Reason                                                                 |
|--------------|---------|------------------------------------------------------------------------|
| Eyebrow      | default | Single-line reference element; standard single-line treatment.         |
| Caption      | default | Metadata, not sustained prose; register extension to Loose does not apply. |
| Button       | tight   | Single-line UI label; minimises vertical ink mass in the control.      |
| Nav primary  | default | Single-line navigation; standard single-line treatment.                |
| Footer text  | default | Utility content, not sustained prose; conservative selection.          |
| Block code   | default | Tier 2 structured content; stable baseline.                            |

**Inline roles.** Link, Strong, Em, Cite, I, and Inline code inherit line height from their parent role. Inline roles do not set line height independently.

---

## Vertical Rhythm

Each typography role declares a space-above value. This value governs the interval between the element and the element immediately preceding it. The space-above value is applied regardless of what precedes the element. A role's vertical spacing is a property of the role, not of the surrounding content. This produces consistent rhythm: the gap before body copy is the same whether body follows a heading, a lead, or another paragraph.

No space-below value is declared on any role. The interval between two adjacent elements is determined entirely by the following element's space-above.

| Role         | Space above |
|--------------|-------------|
| Heading 1    | space-96 (when not at page top) |
| Heading 2    | space-96    |
| Heading 3    | space-48    |
| Lead         | space-32    |
| Body         | space-24    |
| Body small   | space-16    |
| Caption      | space-16    |
| Block code   | space-24    |
| Eyebrow      | space-96    |

Values are proposals for this first pass; refine against page prototypes.

### Eyebrow and heading coupling

Eyebrow and its heading form a labeling compound. The eyebrow carries the section-level space-above for the compound. When a heading immediately follows an eyebrow, the heading's space-above reduces to space-16. This is the only admitted exception to the space-above-only rule on this surface. Reason: eyebrow and heading are a single semantic unit; applying both roles' declared space-above values would compound the gap into a value that does not occur elsewhere in the rhythm.

---

## Measure

Body text has a maximum line length. Excessive line length degrades reading. On this surface, body text is constrained to a maximum of 10 columns within the 16-column grid at Large, 8 columns of 12 at Medium, and the full 4 columns at Small. Expressed as approximate character counts, this produces 65 to 72 characters per line at the body anchor. The constraint applies to prose blocks, not to structural elements (headings, buttons, nav).

| Breakpoint | Body max-width |
|------------|----------------|
| Small      | full content area (4 columns) |
| Medium     | 8 of 12 columns |
| Large      | 10 of 16 columns |

---

## Alignment

Default text alignment is left. The surface is left-to-right. Centered alignment is admitted only for: heading text in hero contexts where the hero is centered as a composition; button labels within buttons; single-word navigation items. Right alignment is not admitted on this surface.

---

## Link Styling

Link colour and underline treatment are defined here at role level. Colour token selections reference the Krutho Colour System.

| State     | Colour token | Underline |
|-----------|--------------|-----------|
| Default   | semantic link colour (to be confirmed against colour system) | yes |
| Hover     | semantic link hover colour | yes |
| Visited   | default colour | yes |
| Focus     | default colour with focus ring | yes |

Link treatment is an open refinement. The specific colour tokens resolve against the Krutho Colour System and are flagged as a dependency check.

---

## Governing Conditions

1. The register is Expressive. Column count adapts to viewport within the register.
2. Three breakpoints govern the surface: Small (up to 640px), Medium (640 to 1024px), Large (1024px and above). Responsive behaviour is discrete token swaps at breakpoint boundaries. Fluid type sizing is not admitted.
3. Every type role on this surface is listed in the Typography Roles section. Roles not listed are not admitted.
4. Body anchor holds at type-16 across all breakpoints.
5. Heading roles admitted on this surface are Heading 1, Heading 2, Heading 3, attached to `<h1>`, `<h2>`, `<h3>` respectively. `<h4>` and below are not admitted.
6. Tier 3 is not currently assigned to any role. Its admission on this surface requires a named role and a stated reason consistent with the typography system's Tier 3 admission test.
7. Italic is admitted on `<em>`, `<cite>`, and `<i>` at weight 400.
8. Line height variants are derived by the rule stated in the Line Height subsection. Tight applies to headings rendered above 40px and to Button. Default applies to headings rendered at 40px or below and to Eyebrow, Caption, Nav primary, Footer text, and Block code. Loose applies to Lead, Body, and Body small. Inline roles inherit from the parent role.
9. Vertical rhythm between typography elements is governed by the following element's declared space-above value. No space-below values are declared on any role. The only admitted exception is the eyebrow and heading coupling stated in the Vertical Rhythm section.
10. Default text alignment is left. Centered and right alignments are restricted to the conditions stated in the Alignment section.
11. Every value in this specification is either drawn from a Krutho foundation token set or derived by rule from those token sets. The surface introduces no primitives.

---

## Open for Refinement

Items flagged in the first pass that benefit from review before the spec is considered settled.

1. **Heading scale at Large.** Heading 1 at type-80 is proposed. type-64 and type-96 are both admitted zone-adjacent alternatives. Decision depends on hero composition and the visual weight of the wordmark placed alongside.
2. **Eyebrow treatment.** Proposed at type-14 Medium with no transformation. Marketing convention often renders eyebrows uppercase with positive letter-spacing. Neither uppercase transform nor letter-spacing tokens are registered in the Krutho Typography System. Admitting either on this surface is a surface-level extension that needs a stated reason.
3. **Tier 3 assignment.** Admissible under the system. Not assigned in the first pass. A hero tagline or pull quote is the most likely candidate if Tier 3 is introduced.
4. **Link treatment.** Colour tokens and underline convention need resolution against the colour system.
5. **Block code container.** Treatment of the bordered container around block code is a component decision carried here as a dependency.
6. **Vertical rhythm values.** Proposed values are conventional for an Expressive surface. Refine against page prototypes.
7. **Measure.** Proposed column spans for body max-width need verification against typeset prototypes at each breakpoint.
