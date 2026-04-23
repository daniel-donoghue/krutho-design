# Krutho Grid System

Last edit 23rd April 2026

---

## Grounding Statement

This document is the Krutho Grid System. It operates under the Krutho Design Philosophy and derives from the Krutho Substrate through the Krutho Spacing System.

The grid governs alignment: the common reference frame against which all geometry is placed. A grid value is a cell size, defining where geometry sits on a pixel raster. A spacing value is an interval, defining the distance between two elements. A grid value and a spacing value may share the same number (grid-4 and space-4 are both 4px), but their functions are distinct.

Grid values are a subset of spacing values. This document applies an additional constraint (powers of 2) and an additional range (bounded by the substrate's display zone). The density registers referenced here are defined in the Krutho Spacing System. The grid operates alongside the Krutho Layout System, which governs column structure.

---

## Terms

Four terms are defined here. Each is used throughout this document in its defined sense only.

**Grid.** A uniform division of a two-dimensional surface into equal square cells, defined by a single value: the side length of each cell in the production context unit. All cells in a grid are identical. The grid is a construction reference: it provides a shared frame for placing and aligning geometry.

**Sub-grid.** A grid whose cell size is exactly half the cell size of a parent grid. A sub-grid subdivides each parent cell into four equal squares. The relationship is recursive: a sub-grid may itself have a sub-grid. The chain terminates at the minimum cell size of 1px.

**Admitted value.** A cell size that satisfies the grid conformance test.

**Alignment condition.** The requirement that where a surface has a margin or gutter, the selected grid cell size divides both values exactly. Where this fails, column edges do not fall on grid intersections, defeating the grid's function as construction reference.

---

## Conformance

The grid admits a subset of spacing values. Grid values are spacing values that satisfy two additional conditions: they are powers of 2, and they fall within a range derived from the substrate's display zone boundary.

**Grid conformance test:** value = 2ⁿ, where n is an integer in the range 2 ≤ n ≤ 6, in the unit of the declared production context.

This admits 4, 8, 16, 32, and 64 as grid values. The lower bound (4px) is the spacing minimum. The upper bound (64px) is derived in the Admitted Grid Values section from the substrate's display zone boundary.

**Powers of 2, derivation.**

The sub-grid condition requires that a grid cell size halves to an integer value at every step of the recursive chain, down to 1px. Powers of 2 starting at 4 satisfy this: 64 → 32 → 16 → 8 → 4 → 2 → 1, integers at every step.

Non-power-of-2 multiples of 4 fail. 12 halves to 12 → 6 → 3 → 1.5, breaking the chain. 24 halves to 24 → 12 → 6 → 3 → 1.5, same failure. Powers of 2 starting at 4 are the complete set satisfying both the spacing conformance test and the sub-grid condition.

---

## Admitted Grid Values

The admitted grid values are 4, 8, 16, 32, and 64 px.

| Token   | Value | Derivation | Sub-grid chain      |
|---------|-------|------------|---------------------|
| grid-4  | 4px   | 2²         | 2, 1                |
| grid-8  | 8px   | 2³         | 4, 2, 1             |
| grid-16 | 16px  | 2⁴         | 8, 4, 2, 1          |
| grid-32 | 32px  | 2⁵         | 16, 8, 4, 2, 1      |
| grid-64 | 64px  | 2⁶         | 32, 16, 8, 4, 2, 1  |

**4px as minimum.** The minimum admitted spacing value is 4px. A primary grid cell smaller than this has no relationship to the spacing system. 2px and 1px positions are valid as sub-grid construction references.

**64px as maximum.** The display zone upper boundary is 80px. Values at 80px and above enter the large zone, which governs page-scale layout intervals. Construction references operate below page-scale layout. The maximum admitted grid value is the largest power of 2 below the display zone boundary: 2⁶ = 64. 2⁷ = 128 enters the large zone.

---

## Sub-grid

Any admitted grid value may have a sub-grid. The sub-grid value is the parent grid value divided by 2. This sub-grid may itself have a sub-grid, recursively, down to a minimum cell size of 1px.

The full sub-grid chain for any admitted value is derivable by repeated halving. All values in the chain are integers. The chain terminates at 1px.

Sub-grid values of 2px and 1px are construction references. They are not spacing values. The spacing system excludes 2px on rendering grounds: a 2px spacing interval does not render predictably on all display densities. A 2px sub-grid position is a different thing: it defines where a geometric edge sits on the pixel raster. Placing a curve terminus or stroke endpoint at a 2px sub-grid position is a precision operation in construction. The same coordinate serves as a construction reference without being a spacing value.

The surface spec declares whether a sub-grid is active and states its cell size.

---

## Application

The grid is applied in two distinct contexts. The contexts have different selection rules.

**Construction context** (mark design, component design, iconography, technical diagrams): the grid provides the construction reference for all geometry. The construction context selects the finest admitted grid appropriate to the precision required by the construction. The selection is recorded in the design specification for the constructed object.

**Layout surface** (web, app, presentation deck): the layout system defines the column structure, the grid underlies it. Column boundaries, margin edges, and gutter edges fall on grid intersections. The alignment condition must hold.

**Checking the alignment condition.** Three cases apply.

*Case 1: surface has both a margin m and a gutter g.* Select the largest admitted grid value that divides both m and g without a remainder. This value is the correct grid for that surface.

*Case 2: surface has only a margin, or only a gutter.* Select the largest admitted grid value that divides the present value without a remainder.

*Case 3: surface has neither margin nor gutter.* The alignment condition is vacuously satisfied: there are no margin or gutter edges to align with grid intersections. Grid selection follows the density register guidance alone, recorded in the surface spec.

If, in Case 1 or Case 2, no admitted value divides the relevant values exactly, the spacing token selection must be revised until the alignment condition is satisfiable. The surface spec records which admitted grid value satisfies the condition and confirms the margin and gutter values divide by it exactly.

---

## Density Register and Grid Selection

The density registers are defined in the Krutho Spacing System. The same three registers apply here. The table below maps each register to its typical grid selection and sub-grid depth.

| Register   | Surface class                                                                                           | Typical primary grid | Sub-grid depth |
|------------|---------------------------------------------------------------------------------------------------------|----------------------|----------------|
| Compact    | High information density. Tight spacing. Examples: CLI, data tables.                                    | grid-4 or grid-8     | To 1px         |
| Standard   | Medium density. Balanced spacing. Examples: web, app, deck.                                             | grid-8 or grid-16    | To 2px or 4px  |
| Expressive | Low density by intent. White space is structural. Examples: posters, hero surfaces, brand artifacts.    | grid-16 or grid-32   | To 4px         |

The register provides a starting point for selection. The surface spec states the selected grid value and records the reason. Where the alignment condition requires a specific grid value, that condition governs over the register guidance.

---

## Governing Conditions

The following conditions state every assessable rule in this specification. Each can be applied by inspection to any output. Conditions that apply to the substrate (conformance at the 2px level, zone boundaries, production context declaration) are stated in the Krutho Substrate.

1. The grid cell size is an admitted value: 4, 8, 16, 32, or 64, in the unit of the declared production context.
2. The grid conformance test is: value = 2ⁿ, where n is an integer in the range 2 ≤ n ≤ 6, in the unit of the declared production context.
3. A sub-grid cell size is exactly half the parent grid cell size.
4. The sub-grid chain is recursive and terminates at 1 in the unit of the declared production context. All values in the chain are integers.
5. Sub-grid values of 2 and 1 are construction references only. They are not spacing values.
6. The alignment condition is assessed in three cases. Where a layout surface has both a margin and a gutter, the selected grid cell size divides both values exactly. Where a layout surface has only one of the two, the selected grid cell size divides the present value exactly. Where a layout surface has neither, the alignment condition is vacuously satisfied.
7. Grid selection follows the density register of the surface. The surface spec states the selected value and the reason for that selection within the register.
8. The grid introduces no spacing values. Spatial intervals between elements are governed by the Krutho Spacing System. The grid governs construction alignment only.
