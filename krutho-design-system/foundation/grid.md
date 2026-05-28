# Grid

A grid value is a cell size, defining where geometry sits on a pixel raster. A spacing value is an interval, defining the distance between elements. A grid value and a spacing value may share the same number (grid-4 and space-4 are both 4px), but their functions are distinct.

Grid values serve two functions: as construction references for geometry, and as the underlying structure for layout columns. When a grid underlies a layout, the grid value must divide the surface's margin and gutter without remainder; otherwise column edges do not fall on grid intersections and the grid stops functioning as a reference.

## Conformance test

`value = 2ⁿ`, where n is an integer in the range 2 ≤ n ≤ 6.

Grid values are a subset of spacing values. They satisfy two additional conditions: they are powers of 2, and they fall within the range admitted for construction reference.

**Powers of 2.** The sub-grid condition requires that a grid cell size halves to an integer at every step down to 1px. Powers of 2 starting at 4 satisfy this: 64 → 32 → 16 → 8 → 4 → 2 → 1. Non-power-of-2 multiples of 4 fail: 12 halves to 12 → 6 → 3 → 1.5.

**Range.** The minimum is 4px (the spacing minimum). The maximum is 64px. 128px is too coarse for construction reference: it operates at the dimension of layout sections, not the dimension at which geometry is placed.

## Admitted values

| Token   | Value | Sub-grid chain     |
|---------|-------|--------------------|
| grid-4  | 4px   | 2, 1               |
| grid-8  | 8px   | 4, 2, 1            |
| grid-16 | 16px  | 8, 4, 2, 1         |
| grid-32 | 32px  | 16, 8, 4, 2, 1     |
| grid-64 | 64px  | 32, 16, 8, 4, 2, 1 |

## Sub-grid

A sub-grid cell size is exactly half the parent grid cell size. The relationship is recursive and terminates at 1px.

Sub-grid values of 2px and 1px are construction references only. They are not spacing values: the spacing system excludes them on rendering grounds. They define where geometric edges sit on the pixel raster (curve termini, stroke endpoints), not where spatial intervals between elements are placed.

A surface declares whether a sub-grid is active and states its cell size.