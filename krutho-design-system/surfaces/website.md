# Krutho Web Surface

Last edit 27th April 2026

---

## Grounding Statement

This document is the Krutho Web Surface specification. It operates under the Krutho Design Philosophy and derives from the Krutho Spacing System, the Krutho Typography System, the Krutho Grid System, the Krutho Layout System, and the Krutho Colour System.

The Web Surface specification declares how the foundation documents are realised on content surfaces rendered in a web browser. Every value in this document traces to a foundation document.

**Scope.** This specification governs content surfaces on the web: marketing, documentation, narrative, and informational pages. Product and application UI surfaces are governed by a separate surface specification. Colour assignment at surface level will be added in a subsequent revision.

---

## Terms

The following terms are defined here. Terms not defined here inherit their definitions from the foundation documents named in the Grounding Statement.

**Breakpoint.** A viewport width threshold at which the surface adapts its structure or its typographic assignments. Two categories are defined.

**Structural breakpoint.** A breakpoint where the column count or the margin changes. Three are declared: SM, MD, LG.

**Display breakpoint.** A breakpoint where the grid structure holds and type role assignments advance to reflect larger column widths. Three are declared: Display-SM, Display-MD, Display-LG.

**Role.** A content function assigned to a specific combination of typeface tier, type size, weight, line height, case, and tracking. Roles are declared in the Type Role Set section.

---

## Production Context

The production context is screen. All values are in CSS logical pixels (px).

---

## Density Register

The Web Surface is a responsive surface per the Krutho Spacing System. A register is declared at each structural scale class. Display breakpoints inherit the LG register because they preserve the LG grid and add only type role advancement.

| Breakpoint | Register   |
|------------|------------|
| SM         | Compact    |
| MD         | Standard   |
| LG         | Expressive |
| Display-SM | Expressive |
| Display-MD | Expressive |
| Display-LG | Expressive |

Spacing values at each breakpoint are drawn from the declared register's designed set per the Krutho Spacing System.

---

## Breakpoint System

| Breakpoint | Viewport range | Category   |
|------------|----------------|------------|
| SM         | 320 to 575     | Structural |
| MD         | 576 to 1087    | Structural |
| LG         | 1088 to 1343   | Structural |
| Display-SM | 1344 to 1599   | Display    |
| Display-MD | 1600 to 1855   | Display    |
| Display-LG | 1856 and above | Display    |

Structural breakpoints trigger at the smallest viewport producing column width 32 (mid zone first admitted step) under the breakpoint's column count, margin, and gutter. SM is the smallest viewport addressed; surface instances requiring support below 320 document the extension under the generative escape rule.

Display breakpoints trigger where column width under the LG grid configuration reaches a display zone admitted step: 48 at Display-SM, 64 at Display-MD, 80 at Display-LG. Beyond Display-LG, column width would cross into the large zone; the Content Lock section governs surface behaviour at that point.

---

## Grid Structure

| Breakpoint | Cols | Margin | Gutter | Primary grid | Col width at min |
|------------|------|--------|--------|--------------|------------------|
| SM         | 2    | 16     | 32     | grid-16      | 128              |
| MD         | 8    | 48     | 32     | grid-16      | 32               |
| LG         | 16   | 48     | 32     | grid-16      | 32               |
| Display-SM | 16   | 48     | 32     | grid-16      | 48               |
| Display-MD | 16   | 48     | 32     | grid-16      | 64               |
| Display-LG | 16   | 48     | 32     | grid-16      | 80               |

**Column count.** SM uses 2 per the Krutho Layout System's binary-split admission. MD uses 8 and LG uses 16 per the register-to-count mapping in the Layout System.

**Margin.** Margin 48 at MD through Display-LG: the edge-buffer function is independent of viewport scale at mid-viewport size and above. Margin 16 at SM keeps the edge buffer proportionate at small viewport scale.

**Gutter.** Gutter 32 at all breakpoints. At SM (column count 2), the gutter exceeds the margin to make the binary split visually clear; this is admitted by the Krutho Layout System at column count 2.

**Primary grid.** grid-16 at all breakpoints. It is the largest admitted grid value satisfying the alignment condition against the declared margins and gutter.

Column width is derived per the Krutho Layout System. Within each breakpoint's range, column width varies fluidly with viewport.

---

## Content Lock

At viewport 1856 and above, content area is locked at 1760. Margins expand symmetrically to fill the remaining viewport width.

1760 is the content area at Display-LG minimum viewport (1856 minus two margins of 48). Beyond 1856, an expanding content area would push column width past 80 into the large zone, which governs page-scale intervals rather than element-scale modules per the Krutho Spacing System.

---

## Type Role Set

The Web Surface declares eleven content roles. The role set is canonical across Krutho web content surfaces. Product and application UI surfaces declare their own role set.

| Role      | Tier | Typeface         | Weight         | Tier 1 functional category |
|-----------|------|------------------|----------------|----------------------------|
| Display 1 | 3    | Enra             | Regular (400)  |                            |
| Display 2 | 3    | Enra             | Regular (400)  |                            |
| Heading 1 | 1    | Spline Sans      | Semibold (600) | Structural                 |
| Heading 2 | 1    | Spline Sans      | Semibold (600) | Structural                 |
| Heading 3 | 1    | Spline Sans      | Semibold (600) | Structural                 |
| Heading 4 | 1    | Spline Sans      | Semibold (600) | Structural                 |
| Lead      | 1    | Spline Sans      | Regular (400)  | Continuous reading         |
| Body      | 1    | Spline Sans      | Regular (400)  | Continuous reading         |
| Caption   | 1    | Spline Sans      | Regular (400)  | Continuous reading         |
| Code      | 2    | Spline Sans Mono | Regular (400)  |                            |
| Eyebrow   | 2    | Spline Sans Mono | Regular (400)  |                            |

The Tier 1 functional category column applies only to Tier 1 roles. For Tier 2 and Tier 3 roles, the typeface and weight are determined by tier.

Inline body emphasis is Bold (700) applied within Body flow where emphasis is functionally required. It is a weight variant, not a role.

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

**Code.** Tier 2. Renders code, tokens, CLI representations, and other structured or verifiable content in monospaced type.

**Eyebrow.** Tier 2. An identifier placed above a heading: section number, taxonomy path, kind-of-content tag, or other identifier drawn from a fixed set. Renders in uppercase per the Case Assignment section and carries tracking per the Tracking Assignment section.

---

## Type Role Size Assignment

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
| Caption   | 12 | 12 | 12 | 12         | 12         | 14         |
| Code      | 14 | 14 | 14 | 14         | 14         | 16         |
| Eyebrow   | 12 | 12 | 12 | 12         | 12         | 14         |

SM, MD, and LG share a single token assignment per role. Per-column content density is equivalent across these breakpoints; column count differs but role presence relative to its column holds.

At Display breakpoints, Display and Structural roles advance one zone-admitted spacing step per breakpoint. Continuous reading and Tier 2 roles hold through Display-MD and advance at Display-LG only, where viewing distance increases.

At Display-LG, Body advances per the spacing-admitted step progression (type-16 to type-20). Lead, Caption, Code, and Eyebrow advance to the next designed type token above their baseline that preserves the baseline ordering Lead > Body > Code > Caption, with Eyebrow tracking Caption.

Scaling down from LG and proportional scaling to column width are not admitted.

---

## Line Height Assignment

For Tier 1 roles, the line height variant is determined by the Tier 1 functional category. For Tier 2 and Tier 3 roles, the variant is declared directly.

| Tier 1 functional category | Variant |
|----------------------------|---------|
| Display                    | Tight   |
| Structural                 | Tight   |
| Continuous reading         | Default |

| Tier 2 / 3 role | Variant |
|-----------------|---------|
| Display 1       | Tight   |
| Display 2       | Tight   |
| Code            | Default |
| Eyebrow         | Default |

For each role at each breakpoint, the line height token is lh-{size}-{variant}, resolving against the Krutho Typography System Line Height Token Set. Surface instances may declare Loose for specific contexts under the generative escape rule.

---

## Case Assignment

| Role       | Case     |
|------------|----------|
| Eyebrow    | Upper    |
| All others | Original |

Upper applies as CSS text-transform: uppercase at render time. The underlying content holds its schema-defined case.

---

## Tracking Assignment

Tracking is expressed as a percentage of type size so the value scales with size across breakpoints.

| Role       | Tracking |
|------------|----------|
| Eyebrow    | +5%      |
| All others | 0        |

+5% restores optical balance for Eyebrow's uppercase identifier rendering at type-12 and type-14. The percentage applies as CSS letter-spacing in em (0.05em) and as Figma letterSpacing with unit PERCENT.

---

## Governing Conditions

The following conditions state the assessable rules in this specification. Conditions belonging to upstream documents are stated there.

1. The production context is screen. All values are in CSS logical pixels (px).
2. The density register at each breakpoint follows the Density Register table.
3. The six breakpoints follow the Breakpoint System table.
4. Column count, margin, gutter, and primary grid follow the Grid Structure table.
5. Content area is locked at 1760 when viewport reaches or exceeds 1856.
6. Type role tier, typeface, and weight follow the Type Role Set table. Bold (700) is admitted only as an inline weight variant for Body emphasis.
7. Type role sizes per breakpoint follow the Type Role Size Assignment table.
8. Line height variants follow the Line Height Assignment section.
9. Case assignments follow the Case Assignment table.
10. Tracking assignments follow the Tracking Assignment table.
11. Every value in this specification derives from a foundation document.
