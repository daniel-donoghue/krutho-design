# Krutho Grid System

Version 0.2 — Last edit 10th April 2026

---

## Grounding Statement

This document operates under the Krutho Design Philosophy. The terms precision, correctness, verifiability, and truth are used throughout in the senses defined there. Every decision in this document traces to a reason that excludes the alternatives.

The Krutho grid system defines the square pixel grid used as a construction reference on any surface. It is not the column layout system, which governs horizontal subdivision into content columns. It is not the spacing system, which governs the spatial intervals between elements. The grid governs alignment: the common reference frame against which all geometry is placed. A grid value is a cell size: it defines where geometry sits on a pixel raster. A spacing value is an interval: it defines the distance between two elements. Grid values and spacing values may share the same number (the value 4 is both the grid cell size grid-4 and the spacing token space-4) but their functions are distinct, and the grid is not derived from the spacing token set even where individual values coincide.

**Dependencies.** This document inherits the base unit from the Krutho Spacing System: 4px. It references the density registers defined in the Krutho Spacing System and Krutho Typography System. It operates alongside the Krutho Layout System: the layout system governs column structure; this document governs the pixel grid that underlies it. An independent inspector can verify any grid specification against this document without consulting additional documents.

---

## Terms

Four terms are defined here. Each is used throughout this document in its defined sense only.

**Grid.** A uniform division of a two-dimensional surface into equal square cells, defined by a single value: the side length of each cell in the production context unit. All cells in a grid are identical. The grid is a construction reference. It provides a shared frame for placing and aligning geometry. It does not generate spacing values.

**Sub-grid.** A grid whose cell size is exactly half the cell size of a parent grid. A sub-grid subdivides each parent cell into four equal squares. The sub-grid relationship is recursive: a sub-grid may itself have a sub-grid. The chain terminates at the minimum cell size of 1px.

**Admitted value.** A cell size that satisfies the grid conformance test. Only admitted values are valid grid cell sizes. A cell size that does not satisfy the conformance test is not a grid value in this system.

**Alignment condition.** The requirement that, where a surface has a margin or gutter, the selected grid cell size divides both the margin and gutter values exactly. Failure of this condition means column edges do not fall on grid intersections, which defeats the grid's function as a construction reference.

---

## Base Unit and Conformance

The grid system inherits the base unit from the Krutho Spacing System: **4px**.

The grid conformance test is stricter than the spacing conformance test. The spacing conformance test is value mod 4 = 0. The grid conformance test is:

**Grid conformance test:** value = 2ⁿ, where n is an integer in the range 2 ≤ n ≤ 6, in the production context unit.

This means admitted grid values are restricted to powers of 2 from 4px (2²) to 64px (2⁶) inclusive. The lower bound and upper bound are derived in the Admitted Grid Values section.

**Why powers of 2, not all multiples of 4.**

All multiples of 4 satisfy the spacing conformance test. Not all support the sub-grid condition. The sub-grid condition requires that a grid cell size halves to an integer value at every step of the recursive chain, down to 1px.

Consider 12px. Its sub-grid chain is: 12 → 6 → 3 → 1.5. The value 1.5 is not an integer. A grid whose sub-grid chain produces a non-integer cell size has introduced a value that cannot be placed on any pixel grid. The sub-grid relationship breaks. 12px is excluded.

Consider 24px. Its chain is: 24 → 12 → 6 → 3 → 1.5. Same failure.

The powers-of-2 series beginning at 4px divides cleanly at every step without exception: 64 → 32 → 16 → 8 → 4 → 2 → 1. No step produces a non-integer. This series is the complete set of values that satisfies both the base-unit requirement and the sub-grid condition. These two conditions together produce the conformance test. No other test produces the same result.

---

## Admitted Grid Values

The admitted grid values are 4, 8, 16, 32, and 64 px.

| Token    | Value | Derivation | Sub-grid chain        |
|----------|-------|------------|-----------------------|
| grid-4   | 4px   | 2²         | 2, 1                  |
| grid-8   | 8px   | 2³         | 4, 2, 1               |
| grid-16  | 16px  | 2⁴         | 8, 4, 2, 1            |
| grid-32  | 32px  | 2⁵         | 16, 8, 4, 2, 1        |
| grid-64  | 64px  | 2⁶         | 32, 16, 8, 4, 2, 1   |

**Why 4px is the minimum.** The minimum admitted spacing value is 4px. A grid cell smaller than the minimum spacing value has no useful relationship to the spacing system. Construction decisions traced to a 2px or 1px grid position cannot be represented as valid spacing values. They are valid only as sub-grid construction references. The primary grid operates at the level of the spacing system: 4px is the minimum.

**Why 64px is the maximum.** The spacing system defines zone boundaries derived from the 10% hierarchy threshold. The display zone upper boundary is 80px. Values at 80px and above enter the large zone, which governs page-scale layout intervals: section separation, surface-level structural gaps. Construction references operate below page-scale layout. The maximum admitted grid value is therefore the largest power of 2 that falls within or at the display zone boundary. 2⁶ = 64px, which is below 80px. 2⁷ = 128px, which exceeds 80px and enters the large zone. The maximum is 64px, derived from the display zone boundary, which is itself derived from the spacing system's 10% threshold. The derivation is exact and requires no additional condition.

---

## Sub-grid

Any admitted grid value may have a sub-grid. The sub-grid value is the parent grid value divided by 2. This sub-grid may itself have a sub-grid, recursively, down to a minimum cell size of 1px.

The full sub-grid chain for any admitted value is derivable by repeated halving. All values in the chain are integers. No rounding is required. The chain terminates at 1px and does not extend below it.

Sub-grid values of 2px and 1px are valid construction references. They are not spacing values. The spacing system excludes 2px on rendering grounds: a 2px spacing interval does not render predictably on all display densities. A 2px sub-grid position is a different thing. It defines where a geometric edge sits on the pixel raster. Placing a curve terminus or stroke endpoint at a 2px sub-grid position is a precision operation in construction, not a spatial interval between elements. The distinction is between a construction reference and a spacing value. The same coordinate can serve as the former without existing in the spacing system as the latter.

The surface spec declares whether a sub-grid is active and states its cell size.

---

## Application

The grid is applied in two distinct contexts. The contexts have different selection rules.

**Construction context** (mark design, component design, iconography, technical diagrams): the grid provides the construction reference for all geometry. The construction context selects the finest admitted grid appropriate to the precision required by the construction. Construction context selection is recorded in the design specification for the constructed object.

**Layout surface** (web, app, presentation deck): the layout system defines the column structure. The grid underlies that structure. Column boundaries, margin edges, and gutter edges should fall on grid intersections. A grid value that does not divide the margin and gutter values exactly places column edges between grid lines, removing the grid's function as a construction reference. The alignment condition must hold.

**Checking the alignment condition.** Three cases apply.

*Case 1: surface has both a margin m and a gutter g.* Select the largest admitted grid value that divides both m and g without a remainder. This value is the correct grid for that surface.

*Case 2: surface has only a margin, or only a gutter.* Select the largest admitted grid value that divides the present value without a remainder.

*Case 3: surface has neither margin nor gutter.* The alignment condition is vacuously satisfied: there are no margin or gutter edges to align with grid intersections. Grid selection follows the density register guidance alone, recorded in the surface spec.

If, in Case 1 or Case 2, no admitted value divides the relevant value(s) exactly, the alignment condition cannot be satisfied with the current spacing token selection. The resolution rule is: the spacing token selection for the surface must be revised until the alignment condition is satisfiable. A layout surface whose margin and gutter values yield no valid grid is a layout surface that is not fully specified. Proceeding without satisfying the alignment condition is not permitted. The surface spec records which admitted grid value satisfies the condition and confirms that the relevant margin and gutter values divide by it exactly.

---

## Density Register and Grid Selection

The density registers are defined in the Krutho Spacing System and Krutho Typography System. The same three registers apply here. Register definitions are reproduced below in condensed form for independent verification. A change to the register definitions in either source document requires updating this table.

| Register   | Surface class                                                        | Typical primary grid | Sub-grid depth |
|------------|----------------------------------------------------------------------|----------------------|----------------|
| Compact    | High information density. Tight spacing. Examples: CLI, data tables. | grid-4 or grid-8     | To 1px         |
| Standard   | Medium density. Balanced spacing. Examples: web, app, deck.          | grid-8 or grid-16    | To 2px or 4px  |
| Expressive | Low density by intent. White space is structural. Examples: posters, hero surfaces, brand artifacts. | grid-16 or grid-32 | To 4px |

The register provides a starting point for selection. The surface spec states the selected grid value and records the reason. Where the alignment condition requires a specific grid value, that condition governs over the register guidance.

---

## Production Context

**Screen surfaces** (web, app, deck, screen-rendered output): cell size is in CSS logical pixels. Grid conformance test: value = 2ⁿ, where n is an integer in the range 2 ≤ n ≤ 6, in px. The sub-grid minimum is 1px.

**Print surfaces** (physically printed output): cell size is in points (pt). The same conformance test applies: value = 2ⁿ, where n is an integer in the range 2 ≤ n ≤ 6, in pt. The sub-grid minimum is 1pt.

The surface spec declares its production context. That declaration determines the unit. A grid value that is on-grid for screen is not automatically on-grid for print unless the unit is also confirmed.

---

## Governing Conditions

The following conditions state every assessable rule in this specification. Each can be applied by inspection to any output.

1. The grid cell size is an admitted value: 4, 8, 16, 32, or 64 px (screen) or pt (print). No other value is admitted.
2. The grid conformance test is: value = 2ⁿ, where n is an integer in the range 2 ≤ n ≤ 6, in the production context unit. A value that fails this test is not a grid value in this system.
3. A sub-grid cell size is exactly half the parent grid cell size. No other relationship defines a sub-grid.
4. The sub-grid chain is recursive and terminates at 1px (screen) or 1pt (print). All values in the chain are integers.
5. Sub-grid values of 2px and 1px are valid construction references. They are not spacing values and do not enter the spacing system.
6. The alignment condition is assessed in three cases. Where a layout surface has both a margin and a gutter, the selected grid cell size divides both values exactly. Where a layout surface has only one of the two, the selected grid cell size divides the present value exactly. Where a layout surface has neither, the alignment condition is vacuously satisfied. A grid selection that fails the applicable case does not satisfy the alignment condition for that surface.
7. Grid selection follows the density register of the surface. The surface spec states the selected value and the reason for that selection within the register.
8. The grid introduces no spacing values. Spatial intervals between elements are governed by the Krutho Spacing System. The grid governs construction alignment only.
