# Design system rationale

This document captures the reasoning behind the design system: why each foundation exists, why each value was chosen, and how the system holds together. The foundation and surface docs specify what the system is; this doc specifies why.

The reasoning is brand-agnostic. Specific values, such as typefaces and colour anchors, are properties of consuming projects, supplied through the system's slots. A new brand inherits this rationale and substitutes its own values.

---

## Philosophy

A design system is a set of admitted values and the rules that govern them. The system's job is to make consistency mechanical: a designer or developer reaches for a token from the admitted set, applies it, and the result is correct by construction. There is no judgment call about whether a value is allowed; the answer is in the token set.

This shifts cognitive load from individual decisions to system design. The system's coherence comes from how its values are chosen, not from collective vigilance during use.

Three properties follow:

**Derived, not invented.** Every value traces to a foundation. New values arise by applying a derivation rule, not by intuition.

**Token sets, not infinite scales.** Although derivation rules admit infinite values, the system curates a finite token set for everyday use. Values outside the set remain admissible by the rule but require a stated reason at the surface level.

**Tokens as governance.** The token set itself is the system's enforcement mechanism. A design that uses only tokens is automatically conformant.

---

## Medium

The medium is screen.

This is a deliberate choice over print-first or print-equivalent systems. Screen surfaces are now the primary delivery channel for most design output; print, where it occurs, derives from screen-source material. The unit that follows is the CSS logical pixel: a device-independent abstraction that maps to physical pixels through the rendering engine.

A point (1/72 inch) is admitted as the unit for print production. The arithmetic of the design system is identical in both units; only the rendering target differs. A surface declares its production context, and that declaration determines the unit.

---

## Substrate

The substrate is 2px. This value is the system's foundation; every other value derives from it.

Three conditions had to be satisfied simultaneously:

**Stability.** A value smaller than 2px (i.e., 1px) is unstable. On non-integer-scaled displays, 1px may round to 0 or 2 physical pixels. A foundation that rounds unpredictably defeats its purpose.

**Halving.** The substrate must halve to integers, recursively, down to 1px. This is required for sub-grid construction: a grid value that doesn't halve cleanly cannot serve as a reference for finer geometry. 2 → 1 satisfies this; 3 → 1.5 does not.

**Typographic resolution.** The substrate determines which type sizes are admissible. The standard range (10, 12, 14, 16, 18, 20px) is essential for reading hierarchy. A 4px substrate would exclude 10, 14, and 18, narrowing the typographic palette unacceptably.

2 is the smallest value satisfying all three. Larger substrates would compromise typographic resolution.

---

## Conformance patterns

Each foundation system has a conformance test, derived from the substrate:

| System     | Test                                         | Basis                                 |
|------------|----------------------------------------------|---------------------------------------|
| Typography | value mod 2 = 0                              | Admits substrate directly             |
| Spacing    | value mod 4 = 0                              | Even multiples of substrate           |
| Grid       | value = 2ⁿ, where n is integer, 2 ≤ n ≤ 6    | Powers of 2 within construction range |

**Why typography admits the substrate directly.** Type sizes are values, not gaps. They don't suffer the gap-rendering instability that constrains spacing. A 2px difference between 10 and 12 reads as a hierarchy step.

**Why spacing admits even multiples only.** Spacing values are gaps, and gaps need to render as gaps. At 2px, a gap may collapse to 0 on some displays. From a 4px minimum, admitting odd multiples (6, 10, 14) would place consecutive scale values 2px apart, reintroducing the instability. Even multiples only ensure the step size matches the minimum value.

**Why grid admits powers of 2.** Grid values must support sub-grid recursion: each cell halves into four equal cells, recursively, down to 1px. Powers of 2 satisfy this; non-power-of-2 multiples of 4 (12, 24) fail because they don't halve cleanly.

This family of tests gives each system the resolution it needs without admitting unstable values.

---

## Token sets

The conformance test for each system admits infinite valid values. The token set is a curated finite subset: the values a surface is most likely to need.

Two principles govern token selection:

**Interval widening at scale.** Perceptual differences scale with absolute size. A 4px difference at body size reads as a clear hierarchy step; the same 4px difference at 96px is below perceptual threshold. The token set widens its intervals as values grow, so each step remains a meaningful change.

This pattern repeats across systems. Spacing intervals widen from 4px at the lower end to 32px at the upper end. Type sizes widen from 2px between small sizes to 32px or more between large ones. The widening reflects perceptual sensitivity, not arithmetic.

**Open-ended.** The generative rule keeps the system extensible. A surface that needs a value outside the token set (e.g., 56 between 48 and 64) can use it, with a stated functional reason. The token set is the convention; the rule is the truth.

---

## Density registers

Three registers define a surface's spatial character: Compact, Standard, Expressive.

Three was chosen as the smallest count that spans the design space without overlap. Two would conflate distinct cases (a dense documentation site and a balanced marketing site shouldn't share a register). Four or more would introduce distinctions without meaningful difference.

The registers differ in two things: information density (how much content per unit area) and how white space functions (separator vs structural element).

| Register   | Density | White space role     |
|------------|---------|----------------------|
| Compact    | High    | Separates elements   |
| Standard   | Medium  | Balanced             |
| Expressive | Low     | Structural element   |

A register selects a subset of the spacing scale appropriate to its character. Compact surfaces draw from the lower end. Standard surfaces draw from the lower and middle. Expressive surfaces draw from the middle and upper, including the largest tokens for page-scale intervals.

The same logic extends to grids and column counts: each foundation that has a usage decision attached benefits from being keyed to a register.

---

## Typography

**Three typeface styles: sans, mono, display.**

Three is the smallest set that covers the system's functional needs without redundancy. Sans carries continuous reading and structural hierarchy. Mono carries code and any context where character alignment is functional. Display carries type at the largest sizes, where the scale makes the letterforms legible as a design element and a distinct cut earns its place.

Serif is excluded. The medium is screen, where serif's print-reading advantage does not apply, and the system's typographic character is carried by the sans and display cuts. A surface that needs a serif can supply one, with a stated reason.

The foundation names a specific typeface for each slot, with a fallback to the platform's native typeface in that style. Surfaces reference roles by style rather than by typeface, so a typeface change propagates without surface changes.

**Four weights: Regular (400), Medium (500), Semibold (600), Bold (700).**

Four is the smallest count that supports the typographic functional categories without collapse:

- Display content
- Structural division (headings)
- Continuous reading (body)
- Inline emphasis

Fewer than four collapses categories: structural shares with display, or inline emphasis cannot separate from structural. More than four introduces distinctions within a category, which size already handles.

The mapping of weight to function is a surface decision. The foundation declares the admitted weights; the surface assigns each weight to a role.

**Three line height ratios: Tight (1.2), Default (1.4), Loose (1.6).**

Each ratio was selected on a specific basis:

- **Tight at 1.2.** The minimum ratio at which descender clearance is reliably maintained across typefaces. At 1.1, descenders and ascenders risk visual collision in typefaces with varying descender depth.
- **Default at 1.4.** Typographic research places comfortable sustained reading at 120 to 145% of type size. 1.4 accommodates x-height variation; 1.3 may read tight on typefaces with tall x-heights.
- **Loose at 1.6.** Completes the three-step set at a consistent 0.2 interval. 1.5 would produce uneven intervals (0.2 from Tight to Default, 0.1 from Default to Loose); 1.6 maintains the structure.

Line heights round up to the nearest even integer to satisfy the substrate conformance test. The derived line height for any size at any variant is reproducible by formula.

---

## Grid

**Powers of 2 for grid values.** A grid cell halves into four equal sub-cells, recursively. The chain must terminate at 1px (the pixel raster) with integers at every step. 64 → 32 → 16 → 8 → 4 → 2 → 1 satisfies this; 12 → 6 → 3 → 1.5 does not.

**Range bounded to 4 through 64.** The minimum is the spacing minimum: a grid value smaller than 4 has no spacing-system relationship. The maximum is 64 because 128 operates at layout-section dimensions rather than the element scale where construction reference applies.

**Sub-grid as pixel raster reference.** Sub-grid values of 2 and 1 are not spacing values, since they're too small to render reliably as gaps, but they're valid construction references. They place curve termini, stroke endpoints, and edge geometry on the pixel raster with precision.

The grid serves two distinct functions: as the underlying alignment for layout columns, and as the construction reference for any geometry. These functions share the same values but operate at different scales.

---

## Layout

**Admitted column counts: 2, 4, 8, 12, 16.**

At counts of 4 and above, the count is a multiple of 4, supporting half-width and quarter-width spans without remainder. 12 additionally divides by 3 and 6, giving it the widest range of clean subdivision. 2 is admitted as the minimum: a single binary split. Counts above 16 produce column widths that approach minimum component widths at typical viewport sizes.

**Column width as derived value.** Column width is not subject to the spacing or grid conformance test. It is a structural consequence of surface width, margin, column count, and gutter (each of which is a foundation token or substrate-conformant value). The system admits whatever column width follows from those inputs.

This is a deliberate decision. Forcing column width onto the token grid would mean constraining surface widths, margins, or gutters to make the math work, which complicates the layout system without improving the outcome.

---

## Colour

The colour system is structured in three layers: primitive scales, semantic layer, component tokens.

Three principles govern how colour is applied across the system.

**Neutral first.** Every design must function completely in neutral before colour is applied. Colour is added to a working neutral system. A component, diagram, or layout that requires colour to be understood fails this condition.

**Colour asserts, not decorates.** Colour is applied in three conditions only: to signal state, to signal action, and to signal system response. An element carrying colour must carry a reason that traces to one of these three conditions.

**No luminous effects.** Colour is embedded in the surface. Glow, neon, bloom, and light-emitting treatments are not admitted. These effects perform a property (energy, dynamism, modernity) that the construction does not carry.

**Why three layers.** Each layer separates a concern. Primitives hold raw values; this is the one place hex appears. The semantic layer holds functional meaning (error, success, warning, info) with light and dark mode resolution; updating how a state appears system-wide happens here, once. Component tokens hold application-specific assignments (surface, text, border, icon, action, feedback); these reference the semantic layer or directly reference primitives without restating values.

Traceability runs in one direction: any component token traces back to a primitive in two steps (or one, when the component token references a primitive directly without going through semantic).

**Ramps as curated values.** Primitive ramps are hand-tuned sets, not algorithmically derived. The 11-stop standard scale (50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950) provides positions; specific values at each position are chosen by designers, drawing from established palettes (Tailwind, Radix, Open Color, or a brand-defined anchor) and adjusted by hand.

Algorithmic derivation in a perceptually uniform space (OKLCH) was tested and rejected. No single derivation method reproduced the variation present across ramps: each ramp carries its own hue drift, saturation curve at extremes, and per-stop tuning. Curation preserves the designer's judgement at the cost of mechanical reproducibility, which is the right trade for a system where the ramps are the system's surface character.

**Anchor stop.** Each ramp declares an anchor stop: the canonical brand value for the ramp. Foundation ramps anchor at 600 (error) or 700 (success, warning). The anchor names which value is the reference; surrounding stops support it.

Perceptual spacing across the ramp is verified by eye against soft lightness targets (roughly 50 ≈ 0.97 through 950 ≈ 0.20 in OKLCH). The targets guide construction without binding it.

**Off-standard stops.** The neutral ramp admits four off-standard stops:

- **0** (pure white): required for label text on saturated fills, where the 50 stop's near-white tint is insufficient contrast.
- **450** (between 400 and 500): required for placeholder text, which needs a value perceptibly between disabled (400) and faint (500).
- **825** and **850** (between 800 and 900): required for dark mode surface hierarchy, which needs four distinct dark values, more than the standard scale provides at that end.

These exist because specific UI tokens require values that the standard scale does not provide.

**Semantic source layer.** Each functional state has a single source token that resolves to a primitive stop. Component tokens reference the source token rather than the primitive directly. Light and dark mode handling lives at the source layer; downstream tokens inherit automatically. To change how a state appears across the system, update the source layer only.

**Dark feedback surface derivation.** Dark mode feedback surfaces (error, warning, success, info backgrounds) are computed by compositing the semantic source over the dark mode base surface at 12% opacity. The opacity value was selected as the midpoint of the viable range: above 15%, the surface competes with node-level colour; below 8%, the tint falls below perceptual threshold. The formula produces reproducible values without storing them as additional primitives.

---

## System character

Several cross-cutting properties hold across all foundations.

**Derivation chains.** Every value traces to a foundation, and foundations chain to the substrate. Spacing derives from substrate. Typography admits substrate directly. Grid is a subset of spacing. Layout uses spacing tokens. Colour stands as its own foundation (a primitive scale isn't derived from spatial measurements) but shares the architectural pattern of layered tokens.

**Tokens as governance.** The system doesn't require external compliance rules. A design that uses only foundation tokens is conformant by construction. Where surface-level needs go beyond the token set, the generative rules admit values with documented reasoning.

**Conformance by inspection.** Conformance can be checked by reading values against the admitted token sets and derivation rules. No interpretation required. This makes the system verifiable without requiring the original designer.

**Foundation and surface separation.** Foundations specify the mechanical system: values, derivations, conformance tests. Surfaces apply the system to rendering contexts: which tokens, which register, which assignments. The separation keeps the foundation reusable across surfaces, and makes surface decisions explicit rather than implicit in the system itself.

**Brand-agnostic foundation.** The system's structure (the values, derivations, conformance tests) is independent of brand. Typography slots admit any typefaces. Primitive scales admit any anchor values. A brand layer inherits the system's structure and supplies brand-specific values: typefaces, colour anchors, additional ramps where the brand palette extends beyond foundation.