# Layout

## Terms

- **Column.** A vertical division of the content area. Columns share the content area equally.
- **Content area.** The horizontal extent of a surface minus its margins. Where no margin is present, the content area is the full horizontal extent.
- **Margin.** The horizontal buffer between the edge of a surface and the content area. When present, it is applied equally on both sides and its value is a spacing token.
- **Gutter.** The fixed gap between adjacent columns. When present, its value is a spacing token.

## Column count

Admitted column counts: 2, 4, 8, 12, 16.

At counts of 4 and above, the count is a multiple of 4, which supports half-width and quarter-width spans without remainder. 12 additionally divides by 3 and 6. 2 is admitted as the minimum count: a single binary split. Counts above 16 produce column widths that approach the minimum widths of standard components.

| Count | Subdivisions supported           |
|-------|----------------------------------|
| 2     | halves                           |
| 4     | halves, quarters                 |
| 8     | halves, quarters                 |
| 12    | halves, thirds, quarters, sixths |
| 16    | halves, quarters, eighths        |

## Column width

Column width is derived from surface width, margin, column count, and gutter. Four configurations:

**Without margin, without gutter**

`column width = surface width / column count`

**Without margin, with gutter**

`column width = (surface width - ((column count - 1) × gutter)) / column count`

**With margin, without gutter**

`content area = surface width - (2 × margin)`
`column width = content area / column count`

**With margin, with gutter**

`content area = surface width - (2 × margin)`
`column width = (content area - ((column count - 1) × gutter)) / column count`

The derived column width is not subject to the conformance test. It is a structural consequence of the other values.