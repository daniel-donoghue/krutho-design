# Krutho Layout System

Last edit 23rd April 2026

---

## Grounding Statement

This document is the Krutho Layout System. It operates under the Krutho Design Philosophy and derives from the Krutho Spacing System.

The layout system defines the column grid that structures content on any surface. Margins and gutters are drawn from the Krutho Spacing System. The layout system defines the rules for composing spacing and column structures into a verifiable grid.

---

## Terms

Four terms are defined here. Each is used throughout this document in its defined sense only.

**Column.** A vertical division of the content area. Columns share the content area equally. A column is a unit of subdivision; its value is that it combines with adjacent columns into spans that are proportionally consistent across a surface.

**Content area.** The horizontal extent of a surface minus its margins. Where no margin is present, the content area is the full horizontal extent.

**Margin.** The horizontal buffer between the edge of a surface and the content area. When present, it is applied equally on both sides and its value is a spacing token from the Krutho Spacing System. The absence of a margin is a valid configuration.

**Gutter.** The fixed gap between adjacent columns. When present, its value is a spacing token from the Krutho Spacing System. The absence of a gutter is a valid configuration.

---

## Column Count

The admitted column counts are 2, 4, 8, 12, and 16.

**Derivation.**

At counts of 4 and above, the count is a multiple of 4. Multiples of 4 support half-width and quarter-width spans without remainder. 12 additionally divides by 3 and 6, giving it the widest range of clean subdivision. Counts above 2 that are not multiples of 4 cannot be quartered without remainder, introducing subdivision logic inconsistent with the spacing system's arithmetic.

2 is admitted at scales where a binary split is the correct grid. Two equal halves is the minimum grid a content surface can support while preserving column widths functional for content. At scales where finer subdivision is structurally meaningful, 2 does not apply. The surface specification declares whether its scale admits 2.

Counts above 16 produce column widths that approach the minimum widths of standard components at the viewport sizes this system addresses. A count above 16 is not a structural tool in this context.

**Column count and density register.**

| Count | Subdivisions supported          | Register   |
|-------|---------------------------------|------------|
| 2     | halves                          | Compact    |
| 4     | halves, quarters                | Compact    |
| 8     | halves, quarters                | Standard   |
| 12    | halves, thirds, quarters, sixths | Standard   |
| 16    | halves, quarters, eighths       | Expressive |

Both 2 and 4 are assigned to the Compact register. 2 is admitted only at scales where a binary split is the correct grid. 4 is admitted at Compact-register scales where finer subdivision than 2 is structurally meaningful. Both 8 and 12 are assigned to the Standard register. Where multiple counts are assigned to the same register, the surface spec selects one and states the reason.

---

## Column Width Derivation

Column width is derived from the surface width, the margin, the column count, and the gutter. It is not set independently. Four configurations are defined. Every valid layout is covered by exactly one.

**Without margin, without gutter:**

```
column width  =  surface width / column count
```

**Without margin, with gutter:**

```
column width  =  (surface width - ((column count - 1) x gutter)) / column count
```

**With margin, without gutter:**

```
content area  =  surface width - (2 x margin)
column width  =  content area / column count
```

**With margin, with gutter:**

```
content area  =  surface width - (2 x margin)
column width  =  (content area - ((column count - 1) x gutter)) / column count
```

The derived column width is not subject to the spacing conformance test. It is a structural consequence of the other values.

---

## Governing Conditions

The following conditions state every assessable rule in this specification. Each can be applied by inspection to any output.

1. The column count is one of 2, 4, 8, 12, or 16. Column count 2 is admitted only at scales where a binary split is the correct grid, as declared in the surface specification.
2. The column count matches the density register of the surface as specified in the Column Count table. Where multiple counts are assigned to the same register (Compact: 2 and 4; Standard: 8 and 12), the surface spec states which applies and why, including the scale condition where 2 is selected.
3. The margin, when present, is a spacing token from the Krutho Spacing System, applied equally on both sides.
4. The gutter, when present, is a spacing token from the Krutho Spacing System.
5. Where a margin is present and the column count is 4 or above, the gutter value does not exceed the margin value. At column count 2, the gutter-margin relationship is governed by the surface specification. Where no margin is present, the gutter value does not exceed the unguttered column width (surface width / column count).
6. Column width is derived by the formula in the Column Width Derivation section matching the surface configuration. Column width is not set independently.
7. The derived column width is not subject to the spacing conformance test.
8. The layout system introduces no spacing values. Every spacing value in a layout specification traces to the Krutho Spacing System.
