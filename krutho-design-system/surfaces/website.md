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

Structural breakpoints trigger at the smallest viewport producing column width 32 under the breakpoint's column count, margin, and gutter. SM is the smallest viewport addressed; surface instances requiring support below 320 document the extension with a stated functional reason.

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
| MD         | 8    | 48     | 32     | grid-16      | 32               |
| LG         | 16   | 48     | 32     | grid-16      | 32               |
| Display-SM | 16   | 48     | 32     | grid-16      | 48               |
| Display-MD | 16   | 48     | 32     | grid-16      | 64               |
| Display-LG | 16   | 48     | 32     | grid-16      | 80               |

**Column count.** SM uses 2 for a binary split at small viewport. MD uses 8 and LG uses 16; count increases with surface width to support finer subdivisions.

**Margin.** Margin 48 at MD through Display-LG: the edge-buffer function is independent of viewport scale at mid-viewport size and above. Margin 16 at SM keeps the edge buffer proportionate at small viewport scale.

**Gutter.** Gutter 32 at all breakpoints. At SM (column count 2), the gutter exceeds the margin to make the binary split visually clear.

**Primary grid.** grid-16 at all breakpoints. It is the largest grid value that divides both the declared margins (16, 48) and the gutter (32) without remainder.

Column width is derived per the layout formulas. Within each breakpoint's range, column width varies fluidly with viewport.

---

## Content lock

At viewport 1856 and above, content area is locked at 1760. Margins expand symmetrically to fill the remaining viewport width.

1760 is the content area at Display-LG minimum viewport (1856 minus two margins of 48). Beyond this, an expanding content area would push column width above 80, into page-scale rather than element-scale dimensions.

---

## Type role set

A role specifies how a content function is rendered: type style, size, weight, line height, case, and tracking. The web surface declares eleven content roles. The role set is canonical across web content surfaces. Product and application UI surfaces declare their own role set.

| Role      | Style | Weight         |
|-----------|-------|----------------|
| Display 1 | sans  | Regular (400)  |
| Display 2 | sans  | Regular (400)  |
| Heading 1 | sans  | Semibold (600) |
| Heading 2 | sans  | Semibold (600) |
| Heading 3 | sans  | Semibold (600) |
| Heading 4 | sans  | Semibold (600) |
| Lead      | sans  | Regular (400)  |
| Body      | sans  | Regular (400)  |
| Caption   | sans  | Regular (400)  |
| Code      | mono  | Regular (400)  |
| Eyebrow   | mono  | Regular (400)  |

The Style column references the typography foundation's style slots. Each slot resolves to a system default or a brand-supplied typeface. Inline body emphasis is Bold (700) applied within Body flow where emphasis is functionally required. It is a weight variant, not a role.

**Role definitions.**

**Display 1.** The largest type on a surface. Reserved for surfaces where a single statement is the surface's reason for existing. Hero surfaces, title slides, landing pages.

**Display 2.** Secondary display size. Admitted where Display 1 exceeds the surface instance's line-count threshold at its assigned column span, or where a stepped relationship to Display 1 is required in a multi-display composition.

**Heading 1.** The top of the structural hierarchy within content. Page title where Display roles are not present. Primary section title where Display roles are present.

**Heading 2.** Section divisions within content.

**Heading 3.** Subsection divisions within a Heading 2.

**Heading 4.** Deeper subsection divisions.

**Lead.** An emphasised opening paragraph or standfirst. Body-adjacent in function. Where Lead and Heading 4 share a size at a breakpoint, the two are differentiated by weight (Lead Regular, Heading 4 Semibold) and by position (Lead opens a content block, Heading 4 divides one).

**Body.** The default reading size for continuous content.

**Caption.** Secondary supporting text. Metadata, image captions, annotations, fine print.

**Code.** Renders code, tokens, CLI representations, and other structured or verifiable content.

**Eyebrow.** An identifier placed above a heading: section number, taxonomy path, kind-of-content tag, or other identifier drawn from a fixed set. Renders in uppercase per the Case assignment section and carries tracking per the Tracking assignment section.

---

## Type role size assignment

| Role      | SM | MD | LG | Display-SM | Display-MD | Display-LG |
|-----------|----|----|----|------------|------------|------------|
| Display 1 | 48 | 48 | 48 | 64         | 80         | 96         |
| Display 2 | 40 | 40 | 40 | 48         | 64         | 80         |
| Heading 1 | 32 | 32 | 32 | 40         | 48         | 64         |
| Heading 2 | 24 | 24 | 24 | 32         | 40         | 48         |
| Heading 3 | 20 | 20 | 20 | 24         | 32         | 40         |
| Heading 4 | 18 | 18 | 18 | 20         | 24         | 32         |
| Lead      | 18 | 18 | 18 | 18         | 18         | 24         |
| Body      | 16 | 16 | 16 | 16         | 16         | 20         |
| Caption   | 14 | 14 | 14 | 14         | 14         | 16         |
| Code      | 14 | 14 | 14 | 14         | 14         | 16         |
| Eyebrow   | 12 | 12 | 12 | 12         | 12         | 14         |

SM, MD, and LG share a single token assignment per role. Per-column content density is equivalent across these breakpoints; column count differs but role presence relative to its column holds.

At Display breakpoints, Display and Heading roles advance one type token per breakpoint. Lead, Body, Caption, Code, and Eyebrow hold through Display-MD and advance at Display-LG only, where viewing distance increases.

At Display-LG, Body advances from type-16 to type-20. Lead, Code, Caption, and Eyebrow advance to the next type token above their baseline that preserves the baseline ordering Lead > Body > Code = Caption > Eyebrow.

Scaling down from LG and proportional scaling to column width are not admitted.

---

## Line height assignment

Each role uses a line height variant.

| Role      | Variant |
|-----------|---------|
| Display 1 | Tight   |
| Display 2 | Tight   |
| Heading 1 | Tight   |
| Heading 2 | Tight   |
| Heading 3 | Tight   |
| Heading 4 | Tight   |
| Lead      | Default |
| Body      | Default |
| Caption   | Default |
| Code      | Default |
| Eyebrow   | Default |

For each role at each breakpoint, the line height token is `lh-{size}-{variant}`. Surface instances may declare Loose for specific contexts with a stated functional reason.

---

## Case assignment

| Role       | Case     |
|------------|----------|
| Eyebrow    | Upper    |
| All others | Original |

Upper applies as CSS `text-transform: uppercase` at render time. The underlying content holds its schema-defined case.

---

## Tracking assignment

Tracking is expressed as a percentage of type size so the value scales with size across breakpoints.

| Role       | Tracking |
|------------|----------|
| Eyebrow    | +5%      |
| All others | 0        |

+5% restores optical balance for Eyebrow's uppercase identifier rendering at type-12 and type-14. The percentage applies as CSS `letter-spacing` in em (0.05em) and as Figma `letterSpacing` with unit PERCENT.