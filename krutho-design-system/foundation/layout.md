# Krutho Layout System

Last edit 21st April 2026

---

## Grounding Statement

This document operates under the Krutho Design Philosophy. The terms precision, correctness, verifiability, and truth are used throughout in the senses defined there. Every decision in this document traces to a reason that excludes the alternatives.

The Krutho layout system defines the column grid that structures content on any surface. Margins and gutters are drawn from the Krutho Spacing System. The layout system introduces no new values. It defines the rules for composing spacing and column structures into a verifiable grid.

**Dependency.** This document requires the Krutho Spacing System for margin and gutter values. The spacing token set is reproduced in the Spacing Token Reference at the end of this document. An independent inspector can verify any layout specification against this document and the reproduced token set without consulting additional documents.

---

## Terms

Four terms are defined here. Each is used throughout this document in its defined sense only.

**Column.** A vertical division of the content area. Columns share the content area equally. A column has no intrinsic meaning: it is a unit of subdivision. Its value is that it can be combined with adjacent columns into spans, and that those spans are proportionally consistent across a surface.

**Content area.** The horizontal extent of a surface minus its margins. Where no margin is present, the content area is the full horizontal extent of the surface. The margin is not part of the content area.

**Margin.** The horizontal buffer between the edge of a surface and the content area. When present, it is applied equally on both sides. The margin value is a spacing token from the Krutho Spacing System. A margin is not required. Its absence is a valid configuration.

**Gutter.** The fixed gap between adjacent columns. When present, its value is a spacing token from the Krutho Spacing System. A gutter is not required. Its absence is a valid configuration.

---

## Column Count

The admitted column counts are 2, 4, 8, 12, and 16. No other value is admitted.

**Why the admitted set.**

At counts of 4 and above, the count is a multiple of 4, following the arithmetic logic of the Krutho Spacing System base unit. Multiples of 4 support half-width and quarter-width spans without a remainder. 12 additionally divides by 3 and 6, giving it the widest range of clean subdivision. Column counts above 2 that are not multiples of 4 cannot be quartered without a remainder. They introduce a subdivision logic inconsistent with the arithmetic of the spacing base unit and are excluded on that ground.

2 is admitted at scales where a binary split is the correct grid. A binary split does not subdivide further: it produces two equal halves, which is the minimum grid a content surface can support without producing column widths too narrow for functional content. At scales where finer subdivision is structurally meaningful, 2 is not the correct grid. The surface specification declares whether its scale admits 2.

More than 16 columns produces individual column widths that, at the viewport sizes this system addresses, approach the minimum widths of standard components. A column count above 16 is not a structural tool in this context and is excluded on that ground.

**Column count and density register.**

| Count | Subdivisions supported | Register |
|-------|------------------------|----------|
| 2 | halves | Compact |
| 4 | halves, quarters | Compact |
| 8 | halves, quarters | Standard |
| 12 | halves, thirds, quarters, sixths | Standard |
| 16 | halves, quarters, eighths | Expressive |

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

The derived column width is not subject to the spacing conformance test. It is a structural consequence of the other values, not a deliberate spacing decision.

---

## Governing Conditions

The following conditions state every assessable rule in this specification. Each can be applied by inspection to any output.

1. The column count is one of 2, 4, 8, 12, or 16. No other value is admitted. Column count 2 is admitted only at scales where a binary split is the correct grid, as declared in the surface specification.
2. The column count matches the density register of the surface as specified in the Column Count table. Where multiple counts are assigned to the same register (Compact: 2 and 4; Standard: 8 and 12), the surface spec states which applies and why, including the scale condition where 2 is selected.
3. The margin, when present, is a spacing token from the Krutho Spacing System. It is equal on both sides.
4. The gutter, when present, is a spacing token from the Krutho Spacing System.
5. Where a margin is present, the gutter value does not exceed the margin value. This rule applies at column counts of 4 and above, where content flows across multiple columns as a series and the gutter-margin relationship governs the perceived coherence of the content area as a single multi-column region. At column count 2, content is grouped as two halves rather than as a flowing series; the gutter-margin relationship at column count 2 is governed by the surface specification that admits 2 columns, which states the values and the reason. Where no margin is present, the gutter value does not exceed the unguttered column width, defined as surface width / column count.
6. Column width is derived by the formula matching the surface configuration: without margin and without gutter: surface width / column count; without margin and with gutter: (surface width - ((column count - 1) x gutter)) / column count; with margin and without gutter: (surface width - (2 x margin)) / column count; with margin and with gutter: (surface width - (2 x margin) - ((column count - 1) x gutter)) / column count. Column width is not set independently.
7. The derived column width is not subject to the spacing conformance test.
8. The layout system introduces no spacing values. Every spacing value in a layout specification traces to the Krutho Spacing System.

---

## Spacing Token Reference

Reproduced from the Krutho Spacing System for independent verification. These values are not defined by this document. A change to the Krutho Spacing System requires updating this table.

| Token | Value |
|-------|-------|
| space-4 | 4px |
| space-8 | 8px |
| space-12 | 12px |
| space-16 | 16px |
| space-20 | 20px |
| space-24 | 24px |
| space-32 | 32px |
| space-40 | 40px |
| space-48 | 48px |
| space-64 | 64px |
| space-80 | 80px |
| space-96 | 96px |
| space-128 | 128px |
| space-160 | 160px |
| space-192 | 192px |
