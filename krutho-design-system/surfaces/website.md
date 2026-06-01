# Web surface

This specification governs content surfaces on the web: marketing, documentation, narrative, and informational pages. Product and application UI surfaces are governed by a separate surface specification. Colour assignment at surface level will be added in a subsequent revision.

---

## Production context

The production context is screen. All values are in CSS logical pixels (px).

---

## Breakpoint system

The web surface is responsive across six breakpoints. Structural breakpoints (SM, MD, LG) change the column count or margin. Display breakpoints (Display-SM, Display-MD, Display-LG) hold the grid and advance type role assignments to reflect larger column widths.

| Breakpoint | Viewport range | Category   |
|------------|----------------|------------|
| SM         | 320 to 575     | Structural |
| MD         | 576 to 1087    | Structural |
| LG         | 1088 to 1343   | Structural |
| Display-SM | 1344 to 1599   | Display    |
| Display-MD | 1600 to 1855   | Display    |
| Display-LG | 1856 and above | Display    |

The structural boundaries 576 and 1088 sit at the smallest viewport producing column width 32 for an 8-column and a 16-column grid at margin 48. MD holds the 576 boundary but reduces its margin to 32, which widens its minimum column to 36. SM is the smallest viewport addressed; surface instances requiring support below 320 document the extension with a stated functional reason.

Display breakpoints trigger where column width under the LG grid configuration reaches 48 (Display-SM), 64 (Display-MD), or 80 (Display-LG). Beyond Display-LG, column width would exceed 80, at which point the Content lock section governs surface behaviour.

---

## Density register

A register is declared at each structural breakpoint. Display breakpoints inherit the LG register because they preserve the LG grid and add only type role advancement.

| Breakpoint | Register   |
|------------|------------|
| SM         | Compact    |
| MD         | Standard   |
| LG         | Expressive |
| Display-SM | Expressive |
| Display-MD | Expressive |
| Display-LG | Expressive |

Spacing values at each breakpoint are drawn from the declared register's designed set.

---

## Grid structure

| Breakpoint | Cols | Margin | Gutter | Primary grid | Col width at min |
|------------|------|--------|--------|--------------|------------------|
| SM         | 2    | 16     | 32     | grid-16      | 128              |
| MD         | 8    | 32     | 32     | grid-16      | 36               |
| LG         | 16   | 48     | 32     | grid-16      | 32               |
| Display-SM | 16   | 48     | 32     | grid-16      | 48               |
| Display-MD | 16   | 48     | 32     | grid-16      | 64               |
| Display-LG | 16   | 48     | 32     | grid-16      | 80               |

**Column count.** SM uses 2 for a binary split at small viewport. MD uses 8 and LG uses 16; count increases with surface width to support finer subdivisions.

**Margin.** Margin 48 at LG through Display-LG: the edge-buffer function is independent of viewport scale at large-viewport size and above. Margin 32 at MD widens the content area at mid-viewport widths, taking the minimum column from 32 to 36. Margin 16 at SM keeps the edge buffer proportionate at small viewport scale.

**Gutter.** Gutter 32 at all breakpoints. At SM (column count 2), the gutter exceeds the margin to make the binary split visually clear.

**Primary grid.** grid-16 at all breakpoints. It is the largest grid value that divides the declared margins (16, 32, 48) and the gutter (32) without remainder.

Column width is derived per the layout formulas. Within each breakpoint's range, column width varies fluidly with viewport.

---

## Content lock

At viewport 1856 and above, content area is locked at 1760. Margins expand symmetrically to fill the remaining viewport width.

1760 is the content area at Display-LG minimum viewport (1856 minus two margins of 48). Beyond this, an expanding content area would push column width above 80, into page-scale rather than element-scale dimensions.

---

## Type role set

A role specifies how a content function is rendered: type style, size, weight, and line height. The web surface declares eleven content roles. The role set is canonical across web content surfaces. Product and application UI surfaces declare their own role set.

| Role      | Style   | Weight         |
|-----------|---------|----------------|
| Display 1 | display | Regular (400)  |
| Display 2 | display | Regular (400)  |
| Heading 1 | display | Regular (400)  |
| Heading 2 | sans    | Medium (500)   |
| Heading 3 | sans    | Medium (500)   |
| Heading 4 | sans    | Semibold (600) |
| Lead      | sans    | Regular (400)  |
| Body      | sans    | Regular (400)  |
| Caption   | sans    | Regular (400)  |
| Code      | mono    | Regular (400)  |
| Eyebrow   | sans    | Regular (400)  |

The Style column references the typography foundation's style slots. The display slot carries the three largest roles (Display 1, Display 2, Heading 1); sans carries the structural headings and the reading roles; mono carries Code. Inline body emphasis is Bold (700) applied within Body flow where emphasis is functionally required. It is a weight variant, not a role.

**Role definitions.**

**Display 1.** The largest type on a surface. Reserved for surfaces where a single statement is the surface's reason for existing. Hero surfaces, title slides, landing pages.

**Display 2.** Secondary display size. Admitted where Display 1 exceeds the surface instance's line-count threshold at its assigned column span, or where a stepped relationship to Display 1 is required in a multi-display composition. The two converge at SM, where both cap at type-32.

**Heading 1.** The top of the structural hierarchy within content. Rendered in the display typeface. Page title where Display roles are not present. Primary section title where Display roles are present.

**Heading 2.** Section divisions within content.

**Heading 3.** Subsection divisions within a Heading 2.

**Heading 4.** Deeper subsection divisions.

**Lead.** An emphasised opening paragraph or standfirst. Body-adjacent in function. Where Lead and Heading 4 share a size at a breakpoint, the two are differentiated by weight (Lead Regular, Heading 4 Semibold) and by position (Lead opens a content block, Heading 4 divides one).

**Body.** The default reading size for continuous content.

**Caption.** Secondary supporting text. Metadata, image captions, annotations, fine print.

**Code.** Renders code, tokens, CLI representations, and other structured or verifiable content.

**Eyebrow.** A short identifier placed above a heading: section number, taxonomy path, or kind-of-content tag. Rendered in sans at the Lead size, differentiated from Lead by its tight line height and its position above a heading.

---

## Type role size assignment

| Role      | SM | MD | LG | Display-SM | Display-MD | Display-LG |
|-----------|----|----|----|------------|------------|------------|
| Display 1 | 32 | 48 | 80 | 96         | 128        | 128        |
| Display 2 | 32 | 40 | 64 | 80         | 96         | 96         |
| Heading 1 | 28 | 32 | 40 | 48         | 64         | 80         |
| Heading 2 | 20 | 24 | 24 | 28         | 32         | 40         |
| Heading 3 | 18 | 18 | 18 | 20         | 24         | 28         |
| Heading 4 | 16 | 16 | 16 | 18         | 20         | 24         |
| Lead      | 18 | 18 | 18 | 18         | 18         | 20         |
| Body      | 16 | 16 | 16 | 16         | 16         | 18         |
| Caption   | 14 | 14 | 14 | 14         | 14         | 16         |
| Code      | 16 | 16 | 16 | 16         | 16         | 18         |
| Eyebrow   | 18 | 18 | 18 | 18         | 18         | 20         |

The table is the authoritative per-role, per-breakpoint size assignment. Three behaviours shape it.

**Display and heading roles scale with viewport.** Display 1, Display 2, Heading 1, and the structural headings advance through larger type tokens as the viewport widens, so the hierarchy reads at the surface's scale. Display 1 and Display 2 reach their cap at Display-MD; Display-LG holds them there, since a further step exceeds what the surface needs at scale.

**SM caps the display roles.** At SM, Display 1 and Display 2 share type-32, the largest size that wraps cleanly at a 320 viewport, and Heading 1 sits at type-28. A larger display size breaks across too many lines to function at 320.

**Content roles hold, then advance once.** Lead, Body, Caption, Code, and Eyebrow hold a single size from SM through Display-MD, where per-column reading density is equivalent. At Display-LG each advances one type token, where the larger display's viewing distance warrants it.

MD and LG share a size assignment for the content roles and for Heading 2 through 4. The display-font roles take smaller values at MD: Heading 1 by one token, Display 1 and Display 2 by two tokens. Proportional scaling of type to column width is not admitted: each breakpoint takes a fixed token.

---

## Line height assignment

Each role uses a line height variant. For each role at each breakpoint, the line height token is `lh-{size}-{variant}`.

| Role      | Variant |
|-----------|---------|
| Display 1 | Tight   |
| Display 2 | Tight   |
| Heading 1 | Tight   |
| Heading 2 | Tight   |
| Heading 3 | Default |
| Heading 4 | Default |
| Lead      | Default |
| Body      | Default |
| Caption   | Default |
| Code      | Default |
| Eyebrow   | Tight   |

Surface instances may declare Loose for specific contexts with a stated functional reason.
