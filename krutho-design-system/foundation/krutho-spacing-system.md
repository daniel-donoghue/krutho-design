# Krutho Spacing System

Version 0.3 — Last edit 10th April 2026

---

## Grounding Statement

This document operates under the Krutho Design Philosophy. The terms precision, correctness, verifiability, and truth are used throughout in the senses defined there. Every decision in this document traces to a reason that excludes the alternatives.

The Krutho spacing system is a derivation, not a selection. Every admitted value traces to a single base unit through arithmetic. Every rule in this document is a consequence of that derivation, not a design decision made independently of it.

This document establishes the base unit, the generative rule, the zone structure that governs interval behaviour at different scales, the density registers that define the spatial character of each surface class, and the conditions under which surface-level extension is permitted.

The zone structure established in this document is shared with the Krutho Typography System. Both documents derive from the same base unit and zone derivation. The zone structure is reproduced in full in each document because each must be independently verifiable. Any change to the base unit or zone derivation requires updating both documents.

---

## Terms

Five terms are defined here. Each is used throughout this document in its defined sense only.

**Base unit.**
The irreducible value from which all spacing values are derived. A value that is not a multiple of the base unit is not a valid spacing value.

**Step.**
A specific multiple of the base unit. step(n) = n × 4px, where n is a positive integer. A step is identified by its multiplier: step 4 is 16px.

**Zone.**
A range of the scale within which a consistent interval applies. The interval is the step gap between consecutive admitted values within the zone. Zone boundaries are derived from the perceptibility threshold defined in the Zone Structure section.

**Register.**
A named configuration that defines the spatial character of a surface class: its information density, the behaviour of white space on that surface, and the subset of the spacing scale appropriate to it. A register is a selection from the scale, not a modification of it. The register names used in this document are the same names used in the Krutho Typography System. The two documents are complementary: this document governs spatial values, the typography document governs typographic values, within the same register framework.

**Interval.**
The step gap between consecutive values within a zone. The interval differs by zone. It is derived, not chosen.

---

## Base Unit

The spacing base unit is **4px**.

The spacing system and the typography system share an underlying unit of 2px. Spacing values are always even multiples of 2px, which is the same as multiples of 4px. The typography system uses 2px directly, admitting odd multiples of 2 (14px, 18px) for fine typographic resolution. The spacing system does not: spatial intervals do not require the same resolution as type sizes, and the 4px minimum provides a clean, stable, and practically complete range for spatial work. The type conformance test (value mod 2 = 0) is owned by the Krutho Typography System. This document owns the spacing conformance test.

**Spacing conformance test:** value mod 4 = 0.

A value that fails this test is not a spacing value. It is not an edge case or a near-miss. It does not exist in the spacing system.

**Why 4px and not an alternative.**

The candidates are any even multiple of 2px: 2px, 4px, 6px, 8px, and larger values.

2px fails because it is within the territory of rendering variation. On non-integer-scaled displays, 2px values can render as 1px or 3px depending on subpixel alignment. A spacing value that does not render predictably is not a spacing value. 2px is excluded on rendering grounds.

6px fails because it does not produce clean multiples with common layout values. 6px does not divide into 16px, 24px, 32px, or 64px without a remainder. A base unit that creates fractional relationships with values it will routinely coexist with introduces arithmetic that cannot be verified by inspection. 6px is excluded on arithmetic grounds.

8px passes the rendering and arithmetic tests. It is stable and produces clean multiples. It fails on range grounds: an 8px spacing minimum eliminates 4px and 12px. Both are required. 4px is the correct minimum for tight component spacing: icon-to-label gaps, internal padding in dense components, and inline element separation in compact surfaces all operate at 4px. 12px is required as a distinct step between 8px and 16px in the compact and standard registers. A spacing system without 4px and 12px is not complete for the surface classes this system governs. 8px is excluded because the designed range requires a finer minimum.

4px renders consistently, produces clean multiples, and covers the full practical range of spacing needs from tight component internals to large-format layout intervals. It is also the physical correlate of approximately 1mm at 96dpi, the smallest spatial increment that reads as intentional at arm's length on a screen surface. These reasons converge on 4px and exclude all alternatives.

**Surface-level layout units.**

A surface spec may define a layout unit larger than the base for use within that surface. Any such layout unit is a spacing value: it must satisfy the spacing conformance test (value mod 4 = 0). Surface-level layout units are derived from the spacing base unit and defined by the surface spec, not by this document. The Krutho Surface System will document the layout units used by each surface class.

---

## Generative Rule

The spacing scale is not a list. It is a rule.

step(n) = n × 4px, for any positive integer n.

There is no upper bound. The scale extends as far as the surface requires. A value is valid if and only if it satisfies the spacing conformance test. A value that fails the test is not valid regardless of functional need.

The designed spacing set defined later in this document is a convenience layer. It represents the values a surface is most likely to need. It is not a constraint on the full scale. Surface-level extension beyond the designed set is permitted under the conditions stated in the Generative Escape section.

---

## Zone Structure

The scale is divided into zones. Within each zone, consecutive admitted values are separated by a fixed interval. The interval increases as sizes increase.

### Derivation

The interval for a zone is the smallest step value that, at the largest size within the zone, represents at least 10% of that size.

**Why 10% and not a different threshold.**

The 10% threshold is not a perceptibility threshold. It is a hierarchy threshold. Perceptibility research places reliable size discrimination at approximately 5–7%. A size difference of 7% is detectable. It does not read as a deliberate step in a hierarchy. For a size step to signal hierarchy rather than variation, the difference must be obvious rather than merely detectable.

The specific value of 10% is determined by the arithmetic of the base unit. At 10%, every zone boundary in a base-2 step system falls exactly on a multiple of 4px. At any lower threshold, the boundaries require rounding and are no longer exactly derivable. At 9%, the fine zone boundary falls at 2 / 0.09 = 22.2px, which is not on-grid and requires approximation. At 10%, 2 / 0.10 = 20px exactly. The 10% threshold is the smallest value at which the zone derivation is exact. This is the reason that excludes the alternatives.

**Zone derivation by interval:**

| Interval | Boundary derivation       | Zone upper boundary |
|----------|---------------------------|---------------------|
| 2px      | 2 / 0.10 = 20px exactly   | 20px                |
| 4px      | 4 / 0.10 = 40px exactly   | 40px                |
| 8px      | 8 / 0.10 = 80px exactly   | 80px                |
| 16px     | 16 / 0.10 = 160px exactly | 160px               |
| 32px     | 32 / 0.10 = 320px exactly | 320px               |

Every boundary is a multiple of 4px. This is a consequence of the derivation, not a separate decision.

### Zone table

| Zone      | Interval | Upper boundary |
|-----------|----------|----------------|
| Fine      | 2px      | 20px           |
| Mid       | 4px      | 40px           |
| Display   | 8px      | 80px           |
| Large     | 16px     | 160px          |
| Statement | 32px     | 320px          |

Values between zone upper boundaries are not in the designed step set of any zone. The value 22px, for example, falls between the fine upper boundary (20px) and the mid zone start (24px). It is valid by the generative rule and satisfies the spacing conformance test. Its use at surface level requires documented justification.

---

## Density Registers

A register defines a surface class. It specifies the information density and white space behaviour that characterise the class, and the subset of the spacing scale appropriate to it.

Three registers are defined. The same register names apply in the Krutho Typography System, where typographic values for each class are specified. A surface spec selects a register and applies both the spatial values from this document and the typographic values from the typography document.

**Register selection.** The register is selected by matching the surface's characteristics against the register descriptions below. A surface spec states which register it uses and which characteristics of the surface determine that selection. The selection is verifiable: an independent party can read the surface spec's stated characteristics and confirm that they match the selected register's description. If no register matches without significant mismatch on multiple criteria, the surface spec documents the closest match and specifies the deviation.

Register selection cannot be fully derived by arithmetic. It requires judgment applied to the surface's functional requirements. This is a named gap in the specification: the register descriptions provide the criteria, but the application of those criteria to a given surface requires a human decision. That decision must be recorded in the surface spec.

---

### Compact

**Surface class:** High information density. White space is structural: it separates elements and aids scanning. It is not expressive. Examples: documentation, dense UI, mobile application.

**Spatial character:** Tight internal spacing. Component padding and element gaps draw from the lower end of the spacing scale. Margins and section separation draw from the mid range. Display-scale spacing is not required within this register.

**Designed spacing set:**

| Token     | Value |
|-----------|-------|
| space-4   | 4px   |
| space-8   | 8px   |
| space-12  | 12px  |
| space-16  | 16px  |
| space-20  | 20px  |
| space-24  | 24px  |
| space-32  | 32px  |
| space-40  | 40px  |
| space-48  | 48px  |

Extension beyond space-48 is available by the generative rule. Surface-level use requires documentation.

---

### Standard

**Surface class:** Medium information density. White space balances structural and expressive functions. Examples: web, tablet, presentation deck.

**Spatial character:** Component padding and element gaps draw from the lower and mid ranges. Section separation and layout intervals draw from the mid and display ranges. Spacing values across the full designed set are in scope for this register.

**Designed spacing set:**

| Token     | Value |
|-----------|-------|
| space-4   | 4px   |
| space-8   | 8px   |
| space-12  | 12px  |
| space-16  | 16px  |
| space-20  | 20px  |
| space-24  | 24px  |
| space-32  | 32px  |
| space-40  | 40px  |
| space-48  | 48px  |
| space-64  | 64px  |
| space-80  | 80px  |
| space-96  | 96px  |

Extension beyond space-96 is available by the generative rule. Surface-level use requires documentation.

---

### Expressive

**Surface class:** Low information density by intent. White space is the primary structural element. Spatial intervals between elements are large. Examples: large-format display, hero surfaces, brand artifacts, posters.

**Spatial character:** Internal element spacing draws from the mid range. Section and zone separation draws from the display and large ranges. Page-scale intervals may extend into the upper range.

**Designed spacing set:**

| Token     | Value |
|-----------|-------|
| space-16  | 16px  |
| space-24  | 24px  |
| space-32  | 32px  |
| space-40  | 40px  |
| space-48  | 48px  |
| space-64  | 64px  |
| space-80  | 80px  |
| space-96  | 96px  |
| space-128 | 128px |
| space-160 | 160px |
| space-192 | 192px |

Extension beyond space-192 is available by the generative rule. Surface-level use requires documentation.

---

## Production Context

The base unit is defined as a CSS logical pixel. This governs all screen surfaces.

Print surfaces use a different native unit: the point (pt), where 1pt = 1/72 inch. The arithmetic is identical, but the unit differs.

**Screen surfaces** (web, app, deck, screen-rendered PDF): base unit 4px. Conformance test: value mod 4 = 0.

**Print surfaces** (physically printed A4, physical large-format): base unit 4pt. Conformance test: value mod 4 = 0pt.

A surface spec declares its production context. That declaration determines which unit governs and which conformance test applies. A value that is on-grid for print is not automatically on-grid for screen. The surface spec resolves this by declaring context and working in the native unit for that context.

---

## Generative Escape

The designed spacing set for each register covers the range a surface in that class is most likely to need. It is not exhaustive.

When a required spacing value is outside the designed set, the following conditions apply.

The value must satisfy the spacing conformance test for its production context. A value that fails the conformance test is not admissible regardless of functional need.

The value must be documented at surface level with a stated reason. The reason must be functional: it must trace to a specific requirement of the surface that the designed set does not meet. A preference for a value not in the designed set is not a reason.

The value does not modify the designed set or the register. It is a surface-level extension. If a surface consistently requires values outside its register's designed set, this is a signal that the register selection is incorrect for the surface class, not that the system requires modification.

---

## Spacing Token Set

The full designed spacing token set, from which register-level designed sets are drawn. All values satisfy the spacing conformance test.

| Token      | Value | Step |
|------------|-------|------|
| space-4    | 4px   | 1    |
| space-8    | 8px   | 2    |
| space-12   | 12px  | 3    |
| space-16   | 16px  | 4    |
| space-20   | 20px  | 5    |
| space-24   | 24px  | 6    |
| space-32   | 32px  | 8    |
| space-40   | 40px  | 10   |
| space-48   | 48px  | 12   |
| space-64   | 64px  | 16   |
| space-80   | 80px  | 20   |
| space-96   | 96px  | 24   |
| space-128  | 128px | 32   |
| space-160  | 160px | 40   |
| space-192  | 192px | 48   |

The token set follows a consistent selection rule: within the fine zone, every spacing step is admitted (4px intervals: 4, 8, 12, 16, 20, 24). At mid zone and above, every other step of the zone interval is admitted, doubling the effective interval at each zone. This produces 8px spacing increments in the mid zone, 16px in the display zone, and 32px in the large zone. The selection rule thins the token set at the same rate as the zone intervals widen.

By this rule: 28, 36, 44 are excluded (mid zone alternate steps). 56, 72 are excluded (display zone alternate steps). 112, 144 are excluded (large zone alternate steps). Their absence is not an oversight. It is the consequence of the selection rule. If a surface requires one of these values, the generative escape conditions apply.

Values above space-192 are available by the generative rule. No upper bound is defined. Surface-level use requires documentation.

---

## Governing Conditions

The following conditions state every assessable rule in this specification. Each can be applied by inspection to any value or output.

1. A spacing value is valid if and only if value mod 4 = 0 (screen) or value mod 4 = 0pt (print).
2. Zone boundaries are 20px, 40px, 80px, 160px, and 320px. These are derived from the 10% threshold and are not subject to surface-level modification.
3. Values between zone upper boundaries are valid by the generative rule but require surface-level documentation with a stated functional reason.
4. Values outside the designed spacing set of a register are valid by the generative rule but require surface-level documentation with a stated functional reason.
5. A preference is not a functional reason. A functional reason traces to a specific requirement of the surface that the designed set does not meet.
6. The surface spec declares its production context. That declaration determines the unit and conformance test.
7. The designed spacing sets defined in the Register section are a starting point. The generative rule governs. The designed sets govern only in the absence of a documented surface-level reason to extend them.
8. Register selection requires human judgment applied against the register descriptions. The surface spec records the selection and states the characteristics that determine it. Consistent use of sizes outside the selected register's designed set signals an incorrect register selection, not a system deficiency.
