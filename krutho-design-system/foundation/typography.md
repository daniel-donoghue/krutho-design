# Krutho Typography System

Last edit 23rd April 2026

---

## Grounding Statement

This document is the Krutho Typography System. It operates under the Krutho Design Philosophy and derives from the Krutho Substrate. Typography admits the substrate directly: its conformance test is the substrate conformance test.

This document establishes the typeface tier model, the weight vocabulary, the line height derivation, the type token set, and the line height token set. These are system-level primitives. Surface specifications derive from them, assigning roles, establishing hierarchy, and responding to context.

---

## Terms

Four terms are defined here. Each is used throughout this document in its defined sense only. Terms defined in the Krutho Substrate (medium, unit of medium, substrate, zone, interval) are used throughout in their substrate-defined senses.

**Tier.** A typographic function category corresponding to a specific typeface. Three tiers are defined. Every typographic decision belongs to exactly one tier.

**Tight.** The line height variant derived at ratio 1.2. The minimum ratio at which descender clearance is reliably maintained across typefaces without typeface-specific calibration.

**Default.** The line height variant derived at ratio 1.4. The ratio providing comfortable sustained reading across typefaces with differing x-height proportions.

**Loose.** The line height variant derived at ratio 1.6. The ratio completing a three-step set at a consistent interval of 0.2 from Tight through Default.

---

## Scale

Typography admits the substrate directly. A type size is valid if and only if it satisfies the substrate conformance test (value mod 2 = 0).

The zone structure and boundaries are defined in the Krutho Substrate. Within each zone, admitted type sizes are separated by the substrate step that defines the zone's boundary: 2px in the fine zone, 4px in the mid zone, 8px in the display zone, 16px in the large zone, and 32px in the statement zone.

The type token set is a selection from the admitted scale. A surface may use any conformant value outside the token set with a stated functional reason.

---

## Typeface Tier Model

Three tiers are defined. Every typographic decision belongs to exactly one tier. The tier determines the typeface.

### Tier 1: System Interface, Spline Sans

**Function:** Operational clarity. The primary voice of the system.

**Applies to:** All content where Tier 2 or Tier 3 does not apply. Default.

### Tier 2: System Mechanism, Spline Mono

**Function:** Verifiable structure. System-derived output.

**Applies to:** Content that is structured, verifiable, or system-generated: code, tokens, certificate identifiers, TTL values, logs, structured data, CLI representations, pseudo-code.

**Admission test:** Could the content be independently verified by a machine without contextual interpretation? Content with a fixed schema, a correct value, and a determinable correctness condition qualifies. Tier 2 is never used for aesthetic contrast.

### Tier 3: Meaning, Enra

**Function:** Interpretive weight. Significance.

**Applies to:** Content whose removal would deprive the surface of emphasis without removing a unit of content.

**Admission test:** If the element is removed, does the surface lose emphasis without losing content? An element that carries content is a Tier 1 or Tier 2 decision.

---

## Weight Vocabulary

Four weights are admitted.

**Regular (400).** The baseline weight across all tiers. Applied to continuous reading and to content whose presence is carried by size, position, or typeface.

**Medium (500).** The display weight within Tier 1. Applied to content whose role is surface presence at display size. Size carries the role; Medium adds structural presence without mass that would compete with display openness.

**Semibold (600).** The structural weight within Tier 1. Applied to headings at sizes close to body scale, where size alone cannot reliably divide continuous reading flow. Semibold provides division against body Regular.

**Bold (700).** The inline emphasis weight within Tier 1. Applied to emphasized inline content within body flow. Bold exceeds Semibold (the structural heading weight) so inline emphasis reads as emphasis rather than as a structural division.

---

**Weight assignment within Tier 1.**

Tier 1 content belongs to one of four functional categories. The weight is determined by the functional category. The functional category is determined at surface specification.

| Functional category | Weight         | Function                                      |
|---------------------|----------------|-----------------------------------------------|
| Display             | Medium (500)   | Surface presence, sized to anchor the surface |
| Structural          | Semibold (600) | Visible division of continuous reading flow   |
| Continuous reading  | Regular (400)  | Body and body-adjacent content                |
| Inline emphasis     | Bold (700)     | Emphasis within continuous reading flow       |

**Four weights, derivation.** The four functional categories (display, structural, continuous reading, inline emphasis) require distinct weights to remain visually separable. Fewer than four collapses categories: structural shares with display, or inline emphasis cannot separate from structural. More than four introduces distinctions within a category, which size already handles. Four is the smallest count encoding each category distinctly.

**Tier-level admission.**

| Tier | Typeface    | Weights admitted                |
|------|-------------|---------------------------------|
| 1    | Spline Sans | Regular, Medium, Semibold, Bold |
| 2    | Spline Mono | Regular                         |
| 3    | Enra        | Regular                         |

Tier 2 uses Regular only. Weight above Regular would read as emphasis rather than as a distinct tier, competing with inline Bold in surrounding body. The tier distinction is carried by typeface.

Tier 3 uses Regular only. Enra draws its presence from the typeface itself. Additional weight would compound a mechanism the tier already carries.

---

## Line Height Derivation

Line height tokens are derived from type sizes using three ratios corresponding to three line interval variants: Tight, Default, Loose.

**Tight at 1.2.** The minimum ratio at which descender clearance is reliably maintained across typefaces. At 1.1, descenders and ascenders risk visual collision across typefaces with varying descender depth.

**Default at 1.4.** Typographic research places comfortable sustained reading at 120 to 145% of type size. 1.4 accommodates x-height variation; 1.3 may read tight on typefaces with tall x-heights.

**Loose at 1.6.** The three ratios are separated by a consistent interval of 0.2. 1.5 would produce uneven intervals (0.2 from Tight to Default, 0.1 from Default to Loose). 1.6 completes the three-step set.

**Rounding convention.** Ceiling to the nearest even integer (mod 2 = 0).

lh = ⌈(size × ratio) / 2⌉ × 2

Line heights satisfy the substrate conformance test. They derive from type size, not from the spacing scale.

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

Values outside this set are available by the generative rule. Use requires a stated functional reason at surface level.

---

## Line Height Token Set

Tokens are named by size and variant. The surface selects the token appropriate to its context.

| Token          | Value |
|----------------|-------|
| lh-10-tight    | 12px  |
| lh-10-default  | 14px  |
| lh-10-loose    | 16px  |
| lh-12-tight    | 16px  |
| lh-12-default  | 18px  |
| lh-12-loose    | 20px  |
| lh-14-tight    | 18px  |
| lh-14-default  | 20px  |
| lh-14-loose    | 24px  |
| lh-16-tight    | 20px  |
| lh-16-default  | 24px  |
| lh-16-loose    | 26px  |
| lh-18-tight    | 22px  |
| lh-18-default  | 26px  |
| lh-18-loose    | 30px  |
| lh-20-tight    | 24px  |
| lh-20-default  | 28px  |
| lh-20-loose    | 32px  |
| lh-24-tight    | 30px  |
| lh-24-default  | 34px  |
| lh-24-loose    | 40px  |
| lh-28-tight    | 34px  |
| lh-28-default  | 40px  |
| lh-28-loose    | 46px  |
| lh-32-tight    | 40px  |
| lh-32-default  | 46px  |
| lh-32-loose    | 52px  |
| lh-40-tight    | 48px  |
| lh-40-default  | 56px  |
| lh-40-loose    | 64px  |
| lh-48-tight    | 58px  |
| lh-48-default  | 68px  |
| lh-48-loose    | 78px  |
| lh-64-tight    | 78px  |
| lh-64-default  | 90px  |
| lh-64-loose    | 104px |
| lh-80-tight    | 96px  |
| lh-80-default  | 112px |
| lh-80-loose    | 128px |
| lh-96-tight    | 116px |
| lh-96-default  | 136px |
| lh-96-loose    | 154px |
| lh-128-tight   | 154px |
| lh-128-default | 180px |
| lh-128-loose   | 206px |
| lh-192-tight   | 232px |
| lh-192-default | 270px |
| lh-192-loose   | 308px |

---

## Governing Conditions

The following conditions state every assessable rule in this specification. Each can be applied by inspection to any value or output. Conditions that apply to the substrate (conformance at the 2px level, zone boundaries, production context declaration) are stated in the Krutho Substrate.

1. A type size is valid if and only if it satisfies the substrate conformance test (value mod 2 = 0 in the unit of the declared production context).
2. Every typographic decision belongs to exactly one tier. The tier determines the typeface.
3. Tier 2 (Spline Mono) is admitted only where the content satisfies the admission test: could the content be independently verified by a machine without contextual interpretation? Tier 2 is never used for aesthetic contrast.
4. Tier 3 (Enra) is admitted only where the admission test is satisfied: if the element were removed, would the surface lose emphasis without losing content?
5. Admitted weights are Regular (400), Medium (500), Semibold (600), and Bold (700). Tier 2 and Tier 3 use Regular only. Within Tier 1, weight is assigned by functional category: Display uses Medium, Structural uses Semibold, Continuous reading uses Regular, Inline emphasis uses Bold.
6. Line height tokens are derived by the rule stated in the Line Height Derivation section. Derived values satisfy the substrate conformance test.
7. Type sizes outside the designed token set are valid by the generative rule. Use at surface level requires a stated functional reason.
