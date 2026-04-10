# Krutho Typography System

Version 0.2 — Last edit 10th April 2026

---

## Grounding Statement

This document operates under the Krutho Design Philosophy. The terms precision, correctness, verifiability, and truth are used throughout in the senses defined there. Every decision in this document traces to a reason that excludes the alternatives.

The Krutho typographic system is a structural language. It does not decorate. It assigns function: to every size, every typeface, every weight. A typographic decision that cannot be traced to a function is not a typographic decision. It is an arbitrary mark.

This document establishes the type base unit, the zone structure shared with the Krutho Spacing System, the line height rule, the typeface tier model, the weight vocabulary, and the typographic values for each density register. It owns the type conformance test. The spacing conformance test is owned by the Krutho Spacing System.

The zone structure in this document is shared with the Krutho Spacing System and is reproduced here in full. Each document must be independently verifiable. Any change to the base unit or zone derivation requires updating both documents.

---

## Terms

Six terms are defined here. Each is used throughout this document in its defined sense only.

**Base unit.**
The irreducible value from which all type sizes are derived. A value that is not a multiple of the type base unit is not a valid type size.

**Step.**
A specific multiple of the base unit. step(n) = n × 2px, where n is a positive integer. A step is identified by its multiplier: step 8 is 16px.

**Zone.**
A range of the scale within which a consistent interval applies. The interval is the step gap between consecutive admitted values within the zone. Zone boundaries are derived from the threshold defined in the Zone Structure section.

**Register.**
A named configuration that defines the typographic values appropriate to a surface class. The register names used in this document are the same names used in the Krutho Spacing System. The two documents are complementary: the spacing document governs spatial values, this document governs typographic values, within the same register framework.

**Tier.**
A typographic function category, corresponding to a specific typeface. Three tiers are defined. Every typographic role belongs to exactly one tier. The term *tier* is used in this document to avoid collision with the term *layer* defined in the Krutho Colour System, which carries a different meaning.

**Role.**
A named position within a register's typographic scale, assigned a tier, a size, and a weight. The role names used in the register tables of this document are reference labels for that specific register. They are not consistent across registers: the same size may carry different role names in different registers, because the size occupies a different structural position within each register's scale. This is expected and correct. A surface spec may use a different role vocabulary entirely, provided each role traces to one of the three tiers and uses the size and weight specified for its position in the register.

---

## Base Unit

The type base unit is **2px**.

This value is a CSS logical pixel: device-independent, defined by the W3C as 1/96th of an inch at arm's length viewing distance. It is not a physical pixel. On high-density displays, the rendering engine maps logical pixels to physical pixels. The logical pixel value remains stable.

**Type conformance test:** value mod 2 = 0.

A value that fails this test is not a type size in this system.

**Why 2px and not an alternative.**

The question is which even multiple of 1px produces the correct resolution for type while maintaining a clean relationship with the spacing base unit (4px).

1px fails because it falls below rendering stability. On non-integer-scaled displays, 1px values may render as 0 or 2px depending on subpixel alignment. Type sizes must be stable. 1px is excluded.

3px fails because it does not divide cleanly into the spacing base unit (4px). A 3px type base and a 4px spacing base share multiples only at 12px, 24px, 36px and their multiples. Values such as 16px, 20px, 28px, 32px, 40px, 48px, 64px would be valid for spacing but not for type, introducing a fractional relationship where a clean one is required.

4px provides rendering stability and a clean relationship with the spacing base unit, but loses resolution at small sizes. At 4px granularity, the fine zone contains only 12, 16, and 20px. There is no 14px and no 18px. Practical typographic work at small sizes requires these values. The range 12, 14, 16, 18, 20 must be available.

2px is the largest value that satisfies all three conditions: rendering stability, a clean divisor relationship with the spacing base unit (4 / 2 = 2, exact), and adequate resolution at small sizes. These conditions converge on 2px and exclude all alternatives.

**Relationship to the spacing base unit.**

The spacing base unit is 4px. The type base unit is 2px. Any spacing value is a valid type size. A type size is a valid spacing value only if it also satisfies the spacing conformance test (value mod 4 = 0). The type system admits 14px and 18px; the spacing system does not. This asymmetry is structural and intentional.

**Minimum type size.**

12px for screen surfaces. This is the smallest size at which all three typefaces in the system maintain legibility across common display densities. Sizes below 12px are not in the designed base of any register for screen surfaces. 10px is available by the generative rule at surface level, with a documented functional reason, in specific contexts where condensed labelling is the only option (native mobile tab labels, for example).

For print surfaces, the minimum is 10pt. At 72dpi, 10pt = 10px, which is step 5, on-grid for the print base unit. Print context is defined in the Production Context section.

---

## Generative Rule

The type scale is not a list. It is a rule.

step(n) = n × 2px, for any positive integer n.

There is no upper bound. The scale extends as far as the surface requires. A value is valid if and only if it satisfies the type conformance test. A value that fails the test is not valid regardless of functional need.

The designed type scales defined in the Register section are a convenience set. They are not constraints on the full scale. Surface-level extension is permitted under the conditions stated in the Generative Escape section.

---

## Zone Structure

The scale is divided into zones. Within each zone, consecutive admitted values are separated by a fixed interval. The interval increases as sizes increase.

This zone structure is derived from the same base unit and threshold as the Krutho Spacing System. It is reproduced here in full.

### Derivation

The interval for a zone is the smallest step value that, at the largest size within the zone, represents at least 10% of that size.

**Why 10% and not a different threshold.**

The 10% threshold is a hierarchy threshold, not a perceptibility threshold. Perceptibility research places reliable size discrimination at approximately 5–7%. A difference of 7% is detectable but does not read as a deliberate step in a hierarchy. For a size step to signal hierarchy rather than variation, the difference must be obvious rather than merely detectable.

The specific value of 10% is determined by the arithmetic of the base unit. At 10%, every zone boundary in a base-2 step system falls exactly on a multiple of 4px. At any lower threshold, boundaries require rounding and are no longer exactly derivable. At 9%, the fine zone boundary falls at 2 / 0.09 = 22.2px, which is not on-grid. At 10%, 2 / 0.10 = 20px exactly. The 10% threshold is the smallest value at which the zone derivation is exact. This is the reason that excludes the alternatives.

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

| Zone      | Interval | Upper boundary | Size range    |
|-----------|----------|----------------|---------------|
| Fine      | 2px      | 20px           | 12px – 20px   |
| Mid       | 4px      | 40px           | 24px – 40px   |
| Display   | 8px      | 80px           | 48px – 80px   |
| Large     | 16px     | 160px          | 96px – 160px  |
| Statement | 32px     | 320px          | 192px – 320px |

Values between zone upper boundaries are not in the designed step set of any zone. The value 22px, for example, falls between the fine upper boundary (20px) and the mid zone start (24px). It is valid by the generative rule. Its use at surface level requires documented justification.

---

## Typeface Stack

Three typefaces are defined. Each corresponds to one tier. No other typefaces are admitted.

**Spline Sans.** Tier 1: System Interface. The primary voice of the system. Used for all content, UI, documentation, and structural text. Source: Google Fonts, SIL OFL. This licence permits identical implementation by any party, which mirrors the system's verification posture: the typeface can be reproduced without trust in the maker.

**Spline Mono.** Tier 2: System Mechanism. Used exclusively for structured, verifiable, or system-derived content: code, tokens, identifiers, certificate values, system outputs, CLI representations. Source: Google Fonts, SIL OFL. Same licence and same infrastructure neutrality rationale as Spline Sans. Both typefaces share a common design origin, which maintains visual coherence across tier transitions.

**Enra.** Tier 3: Meaning. Used for key statements, section anchors, and short phrases that carry interpretive weight. Not used for UI, continuous body text, or structural content. Its presence signals that what follows is significant. It is used sparingly: an element that appears frequently cannot signal importance through presence alone.

**Licence verification required.** The infrastructure neutrality argument stated for Spline Sans and Spline Mono depends on both typefaces being available under SIL OFL via Google Fonts. This condition is confirmed for Spline Sans and Spline Mono. Enra's licence and distribution channel must be confirmed before this specification is settled. If Enra is not available under SIL OFL or an equivalent open licence permitting identical implementation by any party, the infrastructure neutrality argument does not extend to Tier 3. The surface spec for any implementation using Tier 3 must state the licence condition that governs it. Until Enra's licence is confirmed, this section is marked as requiring verification.

**On infrastructure neutrality.** Spline Sans and Spline Mono are sourced from Google Fonts under SIL OFL. A system that requires proprietary font access to implement correctly is not independently verifiable. Any party must be able to clone and implement the typeface stack identically. This condition is satisfied for Tiers 1 and 2. Tier 3 is pending the licence verification above.

---

## Typeface Tier Model

Three tiers are defined. Every typographic role belongs to exactly one tier. The tier determines the typeface. No role may use a typeface from a different tier.

### Tier 1: System Interface — Spline Sans

**Function:** The system speaking. Operational clarity. Continuity across surfaces.

**Applies to:** All informational and structural content. UI labels, navigation, body text, headings, captions, supporting copy, documentation.

**Behaviour:** Default. Carries the majority of content. Establishes consistency. Is never absent from a surface.

### Tier 2: System Mechanism — Spline Mono

**Function:** The system proving. Verifiable structure. System-derived output.

**Applies to:** Content that is structured, verifiable, or system-generated. Code, tokens, certificate identifiers, TTL values, logs, structured data, CLI representations, pseudo-code.

**Behaviour:** Used only where the content qualifies by function. The test: could the content be independently verified by a machine? If yes, Mono is admitted. If the answer requires judgment, Mono is not the correct tier.

**Never used:** For aesthetic effect, for contrast against body text as a stylistic choice, for any content that is not structured or system-derived.

### Tier 3: Meaning — Enra

**Function:** The system contextualised. Interpretation. Significance.

**Applies to:** Key statements, section anchors, short phrases where importance must be signalled through typographic voice rather than structural position alone.

**Behaviour:** Appears with intent. Its presence is the signal. Frequency dilutes the signal. A surface where Enra appears on multiple elements is a surface where no element is emphasised.

**Never used:** For UI, body text, dense copy, structural headings, or any content requiring sustained reading.

**The admission test for Tier 3:** Remove the element. Does the surface lose a point of interpretive emphasis, or does it lose a content element? If it loses content, the element is not a Tier 3 role. Tier 3 carries weight, not content.

---

## Weight Vocabulary

Two weights are admitted. No other weights are used.

**Regular (400).** The default weight. Used for all body text, captions, supporting copy, and informational roles. Used for Enra at all Tier 3 roles. Used for Spline Mono at all Tier 2 roles.

**Medium (500).** Used for structural roles within Tier 1 (Spline Sans) where hierarchy must be reinforced through weight as well as size. Applied at heading-level roles and above. Medium is the ceiling. No weight above 500 is admitted.

**Why no weight above Medium.**

Weight above Regular signals structural emphasis. The system's primary hierarchy is expressed through size, typeface tier, and spacing. Weight is a secondary signal, deployed only where size alone is insufficient to establish the required hierarchy. The weight vocabulary is therefore minimal: the fewest weights that cover the required range of differentiation.

Medium (500) is the ceiling. SemiBold (600) is excluded for a specific reason: at SemiBold, stroke thickening produces mass concentration at junction points, where strokes meet or intersect within a letterform. At display and heading sizes, this concentration creates visual weight that competes with the spatial hierarchy established by the spacing system. The system's hierarchy must be legible through space and size. A weight that introduces competing visual mass undermines this. Medium provides reliable differentiation from Regular without crossing into mass competition. SemiBold is the first weight at which the competition begins and is therefore excluded. Bold (700) and above are excluded by the same reason, which applies with greater force at higher weights.

The wordmark uses a single constructed weight throughout, derived geometrically rather than selected from a type weight axis. The typographic system operates with the same restraint applied to the weight axis of the selected typefaces.

**Weight by tier:**

| Tier  | Typeface     | Informational roles | Structural roles |
|-------|--------------|---------------------|------------------|
| 1     | Spline Sans  | Regular (400)       | Medium (500)     |
| 2     | Spline Mono  | Regular (400)       | Regular (400)    |
| 3     | Enra         | Regular (400)       | Regular (400)    |

Spline Mono and Enra do not use Medium. Their tier function is carried by the typeface itself, not by weight. Introducing weight variation within these tiers would create a second axis of emphasis where one is sufficient.

---

## Line Height Rule

Line height is derived from the type size and zone. It is not chosen independently.

**For roles in the fine, mid, and display zones:**

lh = ⌈(size × ratio\_min) / interval⌉ × interval

The result is always a multiple of the zone interval and always on-grid by construction.

**Ratio minimums by zone:**

| Zone    | Ratio minimum | Reason                                                    |
|---------|---------------|-----------------------------------------------------------|
| Fine    | 1.4           | Minimum for comfortable continuous reading                |
| Mid     | 1.4           | Minimum for comfortable continuous reading                |
| Display | 1.2           | Minimum for multi-line display text with descender clearance |

**Grounding for 1.4 (fine and mid zones).**

Typographic research establishes 120–145% of type size as the range for comfortable sustained reading. The lower bound of this range, 1.2, is the minimum at which inter-line white space supports tracking across multiple lines without active effort. The upper bound, approximately 1.45, is the point beyond which line spacing becomes spatially dominant and text reads as separated units rather than continuous content.

The 1.4 minimum is chosen rather than a lower value within this range for a structural reason: at fine-zone sizes (12–20px), the absolute gap produced by 1.3 minimum may resolve to the same derived value as 1.4 minimum at some sizes, due to the ceiling function and the 2px interval. At 1.4, the derived values are consistently distinct from the type size by at least one clear spacing step across all fine-zone sizes. 1.4 is the lower value in the comfortable reading range that produces stable results at fine-zone granularity.

**Grounding for 1.2 (display zone).**

Display-zone type (48px–80px) is not read continuously. It is scanned or read as short statements. The line height needs to provide clearance between lines when wrapping occurs, without adding excessive visual weight through large spacing. 1.2 is the minimum at which descender clearance is maintained at display sizes without relying on knowledge of the specific typeface's descender depth. At 1.1, the derived line height for 48px is 56px (7px above the size in absolute terms), which at display scale provides insufficient separation and risks visual collision on deep descenders. At 1.2, the derived line height for 48px is 64px (16px above the size), which provides reliable clearance across the typefaces in this system.

**Validation note.**

The ratio targets are derived from typographic principles and are not calibrated to the specific metrics of Spline Sans and Enra. These typefaces have specific cap height, x-height, ascender, and descender proportions relative to their em square. Documenting these metrics and deriving typeface-specific line heights using the Capsize approach would produce more precise values. This is a direction for a future iteration of this document. Until those metrics are documented, the ratio targets in this specification hold and produce correct results within an acceptable tolerance.

**For roles in the large and statement zones:**

Single-line intent is the reasonable assumption at these sizes. A line height derived from a ratio applied to a size that will not wrap does not reflect use. The surface spec declares the line height for large and statement zone roles.

If multi-line use applies at these sizes, the surface spec states the line count and applies the derivation rule above using the zone's interval (16px for large, 32px for statement). If single-line use applies, line height is set to the size value or to the next spacing step above it, according to the layout requirement. Either declaration is documented in the surface spec.

### Line height derivation examples

| Size  | Zone    | Ratio | Interval | Derivation                            | lh    |
|-------|---------|-------|----------|---------------------------------------|-------|
| 12px  | Fine    | 1.4   | 2px      | ⌈(12 × 1.4) / 2⌉ × 2 = ⌈8.4⌉ × 2   | 18px  |
| 14px  | Fine    | 1.4   | 2px      | ⌈(14 × 1.4) / 2⌉ × 2 = ⌈9.8⌉ × 2   | 20px  |
| 16px  | Fine    | 1.4   | 2px      | ⌈(16 × 1.4) / 2⌉ × 2 = ⌈11.2⌉ × 2  | 24px  |
| 18px  | Fine    | 1.4   | 2px      | ⌈(18 × 1.4) / 2⌉ × 2 = ⌈12.6⌉ × 2  | 26px  |
| 20px  | Fine    | 1.4   | 2px      | ⌈(20 × 1.4) / 2⌉ × 2 = ⌈14.0⌉ × 2  | 28px  |
| 24px  | Mid     | 1.4   | 4px      | ⌈(24 × 1.4) / 4⌉ × 4 = ⌈8.4⌉ × 4   | 36px  |
| 28px  | Mid     | 1.4   | 4px      | ⌈(28 × 1.4) / 4⌉ × 4 = ⌈9.8⌉ × 4   | 40px  |
| 32px  | Mid     | 1.4   | 4px      | ⌈(32 × 1.4) / 4⌉ × 4 = ⌈11.2⌉ × 4  | 48px  |
| 40px  | Mid     | 1.4   | 4px      | ⌈(40 × 1.4) / 4⌉ × 4 = ⌈14.0⌉ × 4  | 56px  |
| 48px  | Display | 1.2   | 8px      | ⌈(48 × 1.2) / 8⌉ × 8 = ⌈7.2⌉ × 8   | 64px  |
| 64px  | Display | 1.2   | 8px      | ⌈(64 × 1.2) / 8⌉ × 8 = ⌈9.6⌉ × 8   | 80px  |
| 80px  | Display | 1.2   | 8px      | ⌈(80 × 1.2) / 8⌉ × 8 = ⌈12.0⌉ × 8  | 96px  |

---

## Density Registers

Three registers are defined, corresponding to the registers in the Krutho Spacing System. The typographic values for each register are specified here. A surface spec selects a register and applies both the spatial values from the spacing document and the typographic values from this document.

**On role names.** The role names in the tables below are reference labels used to describe position and intent within the system. They describe a content-structured surface. A surface with a different structure (a product UI, for example) may use a different role vocabulary. Any surface role is valid if it traces to one of the three typeface tiers, uses the size and weight specified for its position in the register, and is documented in the surface spec.

---

### Compact

**Surface class:** High information density. Type operates at the fine-zone scale with limited extension into the mid zone. The full range from caption to display is available, but the display range is compressed relative to other registers.

**Anchor:** 16px (step 8). Body text. Tier 1, Regular.

| Role       | Size  | lh    | Zone  | Tier  | Weight  | Notes         |
|------------|-------|-------|-------|-------|---------|---------------|
| caption    | 12px  | 18px  | Fine  | 1     | Regular |               |
| secondary  | 14px  | 20px  | Fine  | 1     | Regular |               |
| body       | 16px  | 24px  | Fine  | 1     | Regular | Anchor        |
| lead       | 18px  | 26px  | Fine  | 1     | Regular |               |
| heading-sm | 20px  | 28px  | Fine  | 1     | Medium  |               |
| heading-md | 24px  | 36px  | Mid   | 1     | Medium  | Zone boundary |
| heading-lg | 32px  | 48px  | Mid   | 1     | Medium  |               |
| display    | 40px  | 56px  | Mid   | 1     | Medium  |               |

**Mono positions in this register:** Any role may use Tier 2 (Spline Mono) where the content is structured or system-derived, at the same size and weight as the Tier 1 role it occupies. The typeface changes. The size and weight do not.

**Note on 10px.** For print-rendered A4 at physical output, 10pt (= 10px at 72dpi) is available as a minimum below caption. Its use requires surface-level declaration. It is not in the designed base.

---

### Standard

**Surface class:** Medium information density. Type operates across the fine and mid zones for content roles and extends into the display zone for structural roles.

**Anchor:** 16px (step 8). Body text. Tier 1, Regular.

| Role       | Size  | lh    | Zone    | Tier  | Weight  | Notes         |
|------------|-------|-------|---------|-------|---------|---------------|
| caption    | 12px  | 18px  | Fine    | 1     | Regular |               |
| secondary  | 14px  | 20px  | Fine    | 1     | Regular |               |
| body       | 16px  | 24px  | Fine    | 1     | Regular | Anchor        |
| lead       | 20px  | 28px  | Fine    | 1     | Regular |               |
| heading-sm | 24px  | 36px  | Mid     | 1     | Medium  | Zone boundary |
| heading-md | 32px  | 48px  | Mid     | 1     | Medium  |               |
| heading-lg | 48px  | 64px  | Display | 1     | Medium  |               |
| display    | 64px  | 80px  | Display | 1     | Medium  |               |
| hero       | 80px  | 96px  | Display | 1     | Medium  |               |

**Tier 3 position in this register:** Enra is applied at heading-md (32px) or heading-lg (48px) for key statements and section anchors. It is not applied below heading-md in this register. It uses Regular weight.

---

### Expressive

**Surface class:** Low information density by intent. Type spans from fine-zone content through to statement-zone display. The content range is minimal. The structural and display range is the primary concern.

**Anchor:** 20px (step 10). Lead text. Tier 1, Regular.

| Role        | Size  | lh    | Zone      | Tier  | Weight  | Notes                  |
|-------------|-------|-------|-----------|-------|---------|------------------------|
| caption     | 14px  | 20px  | Fine      | 1     | Regular |                        |
| body        | 16px  | 24px  | Fine      | 1     | Regular |                        |
| lead        | 20px  | 28px  | Fine      | 1     | Regular | Anchor                 |
| heading-sm  | 28px  | 40px  | Mid       | 1     | Medium  |                        |
| heading-md  | 40px  | 56px  | Mid       | 1     | Medium  | Zone boundary          |
| heading-lg  | 48px  | 64px  | Display   | 1     | Medium  |                        |
| heading-xl  | 64px  | 80px  | Display   | 1     | Medium  |                        |
| display     | 96px  | —     | Large     | 1     | Medium  | Surface declares lh    |
| hero        | 128px | —     | Large     | 1     | Medium  | Surface declares lh    |
| statement   | 192px | —     | Statement | 1     | Medium  | Surface declares lh    |

**Tier 3 position in this register:** Enra is applied at heading-md (40px) or above for key statements. It is the primary tier for statement-level roles on expressive surfaces where a single phrase carries brand weight. It uses Regular weight.

**Anchor note.** The expressive register anchors at 20px rather than 16px. The reason is structural. The expressive register's primary content is display-scale type. Body and lead text are present but subordinate. An anchor at 16px would place the body text in the lower half of the fine zone, producing a 12px gap to the first heading (28px, mid zone). An anchor at 20px places the body text at the fine zone ceiling. The gap to the first heading remains 8px in absolute terms, but the zone boundary falls between them: body sits at the fine zone ceiling, heading-sm sits in the mid zone. The zone transition is the structural signal of the shift from supporting content to primary content. Anchoring at the zone ceiling positions body text at the structural departure point of the hierarchy, which is correct for a register where the display range is the primary voice. 16px would not produce this zone-boundary separation between body and the first heading role.

---

## Role Model

The role names in the register tables are reference labels for a content-structured surface. They are not the only valid role vocabulary.

A surface spec introduces its own role names when the reference labels do not describe the surface's structure. A product UI has labels, values, helper text, tab titles, and modal headings. None of these map directly to body or heading-sm. The surface spec assigns these roles to positions in the register and specifies which tier each uses. The constraints from this document still apply: the typeface follows the tier assignment, the size follows the register position, the weight follows the weight vocabulary.

The test for any surface role: it must declare its tier (1, 2, or 3), its size position within the register, and its weight. If any of these three cannot be declared, the role is not specified.

---

## Production Context

The base unit is defined as a CSS logical pixel. This governs all screen surfaces.

Print surfaces use the point (pt), where 1pt = 1/72 inch. The arithmetic is identical, but the unit differs.

**Screen surfaces** (web, app, deck, screen-rendered PDF): base unit 2px. Conformance test: value mod 2 = 0.

**Print surfaces** (physically printed A4, physical large-format): base unit 2pt. Conformance test: value mod 2 = 0pt. At 72dpi, 10pt = step 5. At 72dpi, 12pt = step 6. The designed base for print compact begins at 10pt.

A surface spec declares its production context. That declaration determines which unit governs. A value on-grid for print is not automatically on-grid for screen.

---

## Generative Escape

The designed type scale for each register covers the range a surface in that class is most likely to require. It is not exhaustive.

When a required type size is outside the designed scale, the following conditions apply.

The value must satisfy the type conformance test for its production context.

The value must be documented at surface level with a stated functional reason.

The value does not modify the designed scale or the register. Consistent use of values outside the designed scale signals an incorrect register selection.

The role must still declare its tier, size, and weight. The tier and weight constraints apply to all roles, including those using generative-escape sizes.

---

## Governing Conditions

The following conditions state every assessable rule in this specification. Each can be applied by inspection to any typographic output.

1. A type size is valid if and only if value mod 2 = 0 (screen) or value mod 2 = 0pt (print).
2. Zone boundaries are 20px, 40px, 80px, 160px, and 320px. These are derived values and are not subject to surface-level modification.
3. Every typographic role belongs to exactly one tier. The tier determines the typeface. A role may not use a typeface from a different tier.
4. Tier 2 (Spline Mono) is admitted only where the content is structured, verifiable, or system-derived. The test: could the content be independently verified by a machine without contextual interpretation? Content with a fixed schema, a correct value, and a determinable correctness condition qualifies. Content that requires editorial judgment to assess does not. Tier 2 is never used for aesthetic contrast.
5. Tier 3 (Enra) is admitted only where the role carries interpretive weight rather than content. The test: if the element is removed, does the surface lose a point of emphasis or a unit of content? An element that carries content is a Tier 1 or Tier 2 role. An element whose removal deprives the surface of emphasis without removing content is a candidate for Tier 3. The surface spec records which elements use Tier 3 and states the reason each passes this test.
6. No weight above Medium (500) is admitted. Tier 2 and Tier 3 roles use Regular (400) only.
7. Line heights for fine, mid, and display zone roles are derived by the rule stated in the Line Height Rule section and are not chosen independently. These derived values hold within an acceptable tolerance for the typefaces in this system. They are not calibrated to the specific metrics of Spline Sans and Enra. Typeface metric documentation and the Capsize derivation approach represent the path to closing this gap in a future iteration of this document.
8. Line heights for large and statement zone roles are declared by the surface spec. The declaration states whether use is single-line or multi-line, and derives accordingly.
9. The role names in the register tables are reference labels. A surface spec may use a different role vocabulary, provided each role declares its tier, size position, and weight.
10. 12px is the minimum type size for screen surfaces in the designed base. Use below 12px requires surface-level declaration with stated reason.
11. Values between zone upper boundaries are valid by the generative rule but require surface-level documentation with a stated functional reason.
12. Values outside the designed type scale of a register are valid by the generative rule but require surface-level documentation with a stated functional reason.
13. The surface spec declares its production context. That declaration determines the unit and conformance test.
14. Register selection is a surface-level decision. Consistent use of sizes outside the selected register's designed scale signals an incorrect register selection, not a system deficiency.
