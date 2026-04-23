# Krutho Substrate

Last edit 23rd April 2026

---

## Grounding Statement

This document is the Krutho Substrate. It operates under the Krutho Design Philosophy. The substrate is the root of the system's numerical derivations. It derives from the medium and its unit. Spacing, typography, grid, and layout derive downstream.

This document establishes the medium, unit of medium, substrate, conformance test, zone structure, and production context.

---

## Terms

Six terms are defined here. Each is used throughout this document in its defined sense only.

**Medium.** The rendering context the Krutho design system governs.

**Unit of medium.** The device-independent value native to the medium.

**Stability.** The property of rendering predictably across display densities without subpixel variation.

**Substrate.** The smallest stable value within the unit of medium. The origin of the system's numerical derivations.

**Zone.** A range of the scale within which a consistent interval applies. Zone boundaries are derived from the substrate.

**Interval.** The step gap between consecutive admitted values within a zone. Each derived system specifies its own interval within the zone structure.

---

## Medium

The medium is screen.

Design system output renders on screen as its primary form. Print surfaces derive from screen-first source material and are a secondary production context.

The medium determines the unit.

---

## Unit of Medium

The unit of screen output is the CSS logical pixel.

The CSS logical pixel is defined by the W3C as 1/96 inch at arm's length viewing distance. The rendering engine maps logical pixels to physical pixels on high-density displays. The logical pixel value remains stable across display densities. It is native to the medium.

---

## Substrate

The substrate is **2px**.

**Conformance test:** value mod 2 = 0.

2px satisfies three conditions:

- **Stability.** It renders predictably across display densities without subpixel variation.
- **Arithmetic regularity.** It halves to integers, supporting recursive halving and sub-grid construction downstream.
- **Resolution.** It admits the typographic range 10, 12, 14, 16, 18, 20 px.

1px fails stability (may render as 0 or 2px on non-integer-scaled displays). 3px fails arithmetic regularity (3/2 = 1.5, eliminating recursive halving). 4px fails resolution at small sizes (14 and 18 are not admitted). 2px is the smallest value satisfying all three.

---

## Zone Structure

The substrate produces a scale. The scale is divided into zones. Within each zone, a consistent interval applies. The interval increases with size. Each derived system specifies its own interval within the zone structure.

**Derivation.** Zone boundaries are derived from the substrate. The substrate step that defines a zone's boundary is the smallest value at which that step, at the largest size within the zone, represents at least 10% of that size.

**10% threshold.** 10% is a hierarchy threshold. A step reads as hierarchy when the size difference is obvious; detection (reliable at 5 to 7%) is not sufficient. 10% is also the smallest value at which every zone boundary falls exactly on grid: 2 / 0.10 = 20px exactly; 2 / 0.09 = 22.2px, off-grid. 10% is the smallest threshold at which the derivation is exact.

### Zone table

| Substrate step | Boundary derivation       | Zone upper boundary | Zone      |
|----------------|---------------------------|---------------------|-----------|
| 2px            | 2 / 0.10 = 20px exactly   | 20px                | Fine      |
| 4px            | 4 / 0.10 = 40px exactly   | 40px                | Mid       |
| 8px            | 8 / 0.10 = 80px exactly   | 80px                | Display   |
| 16px           | 16 / 0.10 = 160px exactly | 160px               | Large     |
| 32px           | 32 / 0.10 = 320px exactly | 320px               | Statement |

Every boundary is a multiple of 4px by derivation.

Each derived system specifies its interval within each zone. A system whose conformance test admits the substrate directly (typography) uses intervals equal to the zone's substrate step. A system whose conformance test admits only even multiples of the substrate (spacing) uses intervals of twice the zone's substrate step.

---

## Production Context

The substrate is defined as a CSS logical pixel for screen. Print surfaces use the point (pt), where 1pt = 1/72 inch. The arithmetic is identical. The unit differs.

**Screen surfaces** (web, app, deck, screen-rendered PDF): substrate 2px. Conformance test: value mod 2 = 0.

**Print surfaces** (physically printed output): substrate 2pt. Conformance test: value mod 2 = 0pt.

A surface specification declares its production context. That declaration determines which unit and conformance test govern. On-substrate conformance is confirmed against the unit of the declared production context.

---

## Governing Conditions

The following conditions state every assessable rule in this specification. Each can be applied by inspection to any value or output.

1. The medium is screen. Print is a secondary production context derived from screen-first source material.
2. The unit of medium is the CSS logical pixel (screen) or the point (print).
3. The substrate is 2px (screen) or 2pt (print).
4. A value is within the Krutho numerical system if and only if value mod 2 = 0 in the unit of its declared production context.
5. Zone boundaries are 20, 40, 80, 160, and 320 in the unit of the declared production context, derived from the substrate and the 10% threshold.
6. Derived systems (spacing, typography, grid, layout) derive from the substrate. Each may apply additional constraints to the substrate's scale as further derivations.
7. A surface specification declares its production context. That declaration determines the unit and conformance test.
