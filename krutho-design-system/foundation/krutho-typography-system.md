# Krutho Typography System

Last edit 17th April 2026

---

## Grounding Statement

This document operates under the Krutho Design Philosophy. The terms precision, correctness, verifiability, and truth are used throughout in the senses defined there. Every decision in this document traces to a reason that excludes the alternatives.

The Krutho typography system defines the type token set, the line height token set, the typeface tier model, and the weight vocabulary. These are the system-level primitives. Surface specifications select from these tokens and apply human judgment to assign them to roles, establish hierarchy, and respond to context. That judgment belongs at the surface layer, not here.

The zone structure in this document is shared with the Krutho Spacing System and is reproduced here in full. Each document must be independently verifiable. Any change to the base unit or zone derivation requires updating both documents.

---

## Terms

Six terms are defined here. Each is used throughout this document in its defined sense only.

**Base unit.**
The irreducible value from which all type sizes are derived. A value that is not a multiple of the type base unit is not a valid type size.

**Step.**
A specific multiple of the base unit. step(n) = n × 2px, where n is a positive integer.

**Tier.**
A typographic function category corresponding to a specific typeface. Three tiers are defined. Every typographic decision belongs to exactly one tier. The term tier is used in this document to avoid collision with the term layer defined in the Krutho Colour System, which carries a different meaning.

**Tight.**
The line height variant derived at ratio 1.2. The minimum ratio at which descender clearance is reliably maintained across typefaces without typeface-specific calibration.

**Default.**
The line height variant derived at ratio 1.4. The ratio providing comfortable sustained reading across typefaces with differing x-height proportions.

**Loose.**
The line height variant derived at ratio 1.6. The ratio completing a three-step set at a consistent interval of 0.2 from Tight through Default.

---

## Base Unit

The type base unit is **2px**.

This value is a CSS logical pixel: device-independent, defined by the W3C as 1/96th of an inch at arm's length viewing distance. It is not a physical pixel. On high-density displays, the rendering engine maps logical pixels to physical pixels. The logical pixel value remains stable.

**Type conformance test:** value mod 2 = 0.

A value that fails this test is not a valid type size.

**Why 2px and not an alternative.**

1px fails on rendering stability. On non-integer-scaled displays, 1px values may render as 0 or 2px depending on subpixel alignment. Type sizes must be stable. 1px is excluded.

3px fails because it does not divide cleanly into the spacing base unit (4px). A 3px type base and a 4px spacing base share multiples only at 12px, 24px, 36px and their multiples. Values such as 16px, 20px, 28px, 32px, 40px, 48px, 64px would be valid for spacing but not for type, introducing a fractional relationship where a clean one is required.

4px provides rendering stability and a clean relationship with the spacing base unit, but loses resolution at small sizes. The range 10, 12, 14, 16, 18, 20px must be available. At 4px granularity it is not.

2px satisfies all three conditions: rendering stability, a clean divisor relationship with the spacing base unit (4 / 2 = 2, exact), and adequate resolution at small sizes. These conditions converge on 2px and exclude all alternatives.

**Relationship to the spacing base unit.**

The spacing base unit is 4px. The type base unit is 2px. Any spacing value is a valid type size. A type size is a valid spacing value only if it also satisfies the spacing conformance test (value mod 4 = 0). The type system admits 10px, 14px, and 18px; the spacing system does not. This asymmetry is structural and intentional.

---

## Generative Rule

The type scale is not a list. It is a rule.

step(n) = n × 2px, for any positive integer n.

There is no upper bound. A value is valid if and only if it satisfies the type conformance test. The type token set defined in this document is a designed convenience set, not a constraint on the full scale. A surface may use any conformant value not in the token set with a stated functional reason.

---

## Zone Structure

The scale is divided into zones. Within each zone, consecutive admitted values are separated by a fixed interval. The interval increases as sizes increase. Zones structure the intervals of the type token set. They are not carried on the tokens.

This zone structure is reproduced in full from the Krutho Spacing System.

### Derivation

The interval for a zone is the smallest step value that, at the largest size within the zone, represents at least 10% of that size.

**Why 10%.**

The 10% threshold is a hierarchy threshold, not a perceptibility threshold. Perceptibility research places reliable size discrimination at approximately 5–7%. A difference of 7% is detectable but does not read as a deliberate hierarchy step. For a size step to signal hierarchy rather than variation, the difference must be obvious rather than merely detectable.

The specific value of 10% is determined by the arithmetic of the base unit. At 10%, every zone boundary falls exactly on a multiple of 4px. At any lower threshold, boundaries require rounding. At 9%, the fine zone boundary falls at 2 / 0.09 = 22.2px, not on-grid. At 10%, 2 / 0.10 = 20px exactly. The 10% threshold is the smallest value at which the zone derivation is exact. This is the reason that excludes the alternatives.

**Zone derivation:**

| Interval | Boundary derivation       | Zone upper boundary |
|----------|---------------------------|---------------------|
| 2px      | 2 / 0.10 = 20px exactly   | 20px                |
| 4px      | 4 / 0.10 = 40px exactly   | 40px                |
| 8px      | 8 / 0.10 = 80px exactly   | 80px                |
| 16px     | 16 / 0.10 = 160px exactly | 160px               |
| 32px     | 32 / 0.10 = 320px exactly | 320px               |

### Zone table

| Zone      | Interval | Upper boundary |
|-----------|----------|----------------|
| Fine      | 2px      | 20px           |
| Mid       | 4px      | 40px           |
| Display   | 8px      | 80px           |
| Large     | 16px     | 160px          |
| Statement | 32px     | 320px          |

---

## Typeface Tier Model

Three tiers are defined. Every typographic decision belongs to exactly one tier. The tier determines the typeface.

### Tier 1: System Interface — Spline Sans

**Function:** Operational clarity. The primary voice of the system.

**Applies to:** All content where Tier 2 or Tier 3 does not apply. Default.

### Tier 2: System Mechanism — Spline Mono

**Function:** Verifiable structure. System-derived output.

**Applies to:** Content that is structured, verifiable, or system-generated: code, tokens, certificate identifiers, TTL values, logs, structured data, CLI representations, pseudo-code.

**Admission test:** Could the content be independently verified by a machine without contextual interpretation? Content with a fixed schema, a correct value, and a determinable correctness condition qualifies. Content requiring editorial judgment does not. Tier 2 is never used for aesthetic contrast.

### Tier 3: Meaning — Enra

**Function:** Interpretive weight. Significance.

**Applies to:** Content whose removal would deprive the surface of emphasis without removing a unit of content.

**Admission test:** If the element is removed, does the surface lose emphasis or content? An element that carries content is a Tier 1 or Tier 2 decision. An element whose removal deprives the surface of emphasis without removing content is a candidate for Tier 3.

---

## Weight Vocabulary

Two weights are admitted.

**Regular (400).** Default. Applied to all Tier 1 informational content, all Tier 2 content, and all Tier 3 content.

**Medium (500).** Applied to Tier 1 structural content where weight reinforces hierarchy alongside size. Tier 2 and Tier 3 do not use Medium.

**Why Medium is the ceiling.**

At SemiBold (600), stroke thickening produces mass concentration at junction points within letterforms. At display and heading sizes, this concentration introduces visual weight that competes with the spatial hierarchy established by the spacing system. Medium provides reliable differentiation from Regular without crossing into mass competition. SemiBold is the first weight at which the competition begins and is therefore excluded. Bold and above are excluded by the same reason applied with greater force.

| Tier | Typeface     | Weight admitted       |
|------|--------------|-----------------------|
| 1    | Spline Sans  | Regular, Medium       |
| 2    | Spline Mono  | Regular               |
| 3    | Enra         | Regular               |

---

## Line Height Derivation

Line height tokens are derived from type sizes using three ratios corresponding to three line interval variants: Tight, Default, and Loose.

**Ratios:**

| Variant | Ratio | Exclusion reasoning                                                                                                                                                                                                                                                                                                                                                                                                                        |
|---------|-------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Tight   | 1.2   | The minimum at which descender clearance is reliably maintained across typefaces without typeface-specific calibration. At 1.1, the vertical gap risks visual collision between descenders of one line and ascenders of the next across typefaces with varying descender depth. 1.1 is excluded on that ground. 1.2 is the smallest value that provides reliable clearance universally.                                                       |
| Default | 1.4   | Typographic research places comfortable sustained reading at 120–145% of type size. The lower bound (1.2) is already the Tight ratio. 1.3 sits in the middle of the range but is excluded: typefaces with tall x-heights may still read tight at 1.3 because the x-height occupies a larger proportion of the line interval. 1.4 provides a margin sufficient to accommodate x-height variation without typeface-specific calibration. 1.3 does not. |
| Loose   | 1.6   | The three ratios are separated by an equal interval of 0.2. This structural reason excludes all alternatives. 1.5 would produce an uneven interval (0.2 from Tight to Default, 0.1 from Default to Loose), making the step between the first two variants twice the magnitude of the step between the last two. A fourth variant at the 0.2 interval would require either 1.0 (below descender clearance minimum) or 1.8 (beyond practical use). Three variants at 1.2 / 1.4 / 1.6 is the smallest set covering the useful range at a consistent interval. These reasons converge on 1.6 and exclude the alternatives.                                                                                                             |

**Rounding convention:** ceiling to the nearest even integer (mod 2 = 0).

lh = ⌈(size × ratio) / 2⌉ × 2

This produces values that satisfy the type conformance test. Line heights are not required to satisfy the spacing conformance test.

**Derivation table:**

| Type token | Size  | Tight (×1.2) | Default (×1.4) | Loose (×1.6) |
|------------|-------|--------------|----------------|--------------|
| type-10    | 10px  | 12px         | 14px           | 16px         |
| type-12    | 12px  | 16px         | 18px           | 20px         |
| type-14    | 14px  | 18px         | 20px           | 24px         |
| type-16    | 16px  | 20px         | 24px           | 26px         |
| type-18    | 18px  | 22px         | 26px           | 30px         |
| type-20    | 20px  | 24px         | 28px           | 32px         |
| type-24    | 24px  | 30px         | 34px           | 40px         |
| type-28    | 28px  | 34px         | 40px           | 46px         |
| type-32    | 32px  | 40px         | 46px           | 52px         |
| type-40    | 40px  | 48px         | 56px           | 64px         |
| type-48    | 48px  | 58px         | 68px           | 78px         |
| type-64    | 64px  | 78px         | 90px           | 104px        |
| type-80    | 80px  | 96px         | 112px          | 128px        |
| type-96    | 96px  | 116px        | 136px          | 154px        |
| type-128   | 128px | 154px        | 180px          | 206px        |
| type-192   | 192px | 232px        | 270px          | 308px        |

---

## Type Token Set

| Token    | Size  |
|----------|-------|
| type-10  | 10px  |
| type-12  | 12px  |
| type-14  | 14px  |
| type-16  | 16px  |
| type-18  | 18px  |
| type-20  | 20px  |
| type-24  | 24px  |
| type-28  | 28px  |
| type-32  | 32px  |
| type-40  | 40px  |
| type-48  | 48px  |
| type-64  | 64px  |
| type-80  | 80px  |
| type-96  | 96px  |
| type-128 | 128px |
| type-192 | 192px |

Values not in this set are available by the generative rule. Use requires a stated functional reason at surface level.

---

## Line Height Token Set

Tokens are named by size and variant. The surface selects the token appropriate to its context.

| Token           | Value |
|-----------------|-------|
| lh-10-tight     | 12px  |
| lh-10-default   | 14px  |
| lh-10-loose     | 16px  |
| lh-12-tight     | 16px  |
| lh-12-default   | 18px  |
| lh-12-loose     | 20px  |
| lh-14-tight     | 18px  |
| lh-14-default   | 20px  |
| lh-14-loose     | 24px  |
| lh-16-tight     | 20px  |
| lh-16-default   | 24px  |
| lh-16-loose     | 26px  |
| lh-18-tight     | 22px  |
| lh-18-default   | 26px  |
| lh-18-loose     | 30px  |
| lh-20-tight     | 24px  |
| lh-20-default   | 28px  |
| lh-20-loose     | 32px  |
| lh-24-tight     | 30px  |
| lh-24-default   | 34px  |
| lh-24-loose     | 40px  |
| lh-28-tight     | 34px  |
| lh-28-default   | 40px  |
| lh-28-loose     | 46px  |
| lh-32-tight     | 40px  |
| lh-32-default   | 46px  |
| lh-32-loose     | 52px  |
| lh-40-tight     | 48px  |
| lh-40-default   | 56px  |
| lh-40-loose     | 64px  |
| lh-48-tight     | 58px  |
| lh-48-default   | 68px  |
| lh-48-loose     | 78px  |
| lh-64-tight     | 78px  |
| lh-64-default   | 90px  |
| lh-64-loose     | 104px |
| lh-80-tight     | 96px  |
| lh-80-default   | 112px |
| lh-80-loose     | 128px |
| lh-96-tight     | 116px |
| lh-96-default   | 136px |
| lh-96-loose     | 154px |
| lh-128-tight    | 154px |
| lh-128-default  | 180px |
| lh-128-loose    | 206px |
| lh-192-tight    | 232px |
| lh-192-default  | 270px |
| lh-192-loose    | 308px |

---

## Production Context

The base unit is defined as a CSS logical pixel. This governs all screen surfaces.

Print surfaces use the point (pt), where 1pt = 1/72 inch. The arithmetic is identical, the unit differs.

**Screen:** base unit 2px. Conformance test: value mod 2 = 0.

**Print:** base unit 2pt. Conformance test: value mod 2 = 0pt.

A surface specification declares its production context. That declaration determines which unit and conformance test govern.

---

## Governing Conditions

The following conditions state every assessable rule in this specification.

1. A type size is valid if and only if value mod 2 = 0 (screen) or value mod 2 = 0pt (print).
2. Zone boundaries are 20px, 40px, 80px, 160px, and 320px. These are derived values and are not subject to modification.
3. Every typographic decision belongs to exactly one tier. The tier determines the typeface. A decision may not use a typeface from a different tier.
4. Tier 2 (Spline Mono) is admitted only where the content satisfies the admission test: could the content be independently verified by a machine without contextual interpretation? Tier 2 is never used for aesthetic contrast.
5. Tier 3 (Enra) is admitted only where the admission test is satisfied: if the element were removed, would the surface lose emphasis or content? Tier 3 carries emphasis, not content.
6. No weight above Medium (500) is admitted. Tier 2 and Tier 3 use Regular (400) only.
7. Line height tokens are derived by the rule stated in the Line Height Derivation section. The derivation is the specification. Derived values satisfy the type conformance test.
8. Type sizes not in the designed token set are valid by the generative rule. Use at surface level requires a stated functional reason.
9. A surface specification declares its production context. That declaration determines the unit and conformance test.
