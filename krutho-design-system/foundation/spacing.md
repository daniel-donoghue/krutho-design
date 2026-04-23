# Krutho Spacing System

Last edit 23rd April 2026

---

## Grounding Statement

This document is the Krutho Spacing System. It operates under the Krutho Design Philosophy and derives from the Krutho Substrate. The substrate (2px), the substrate conformance test, the zone boundaries, the 10% derivation, and the production context are defined in that document.

This document applies additional constraints to the substrate's scale: a spacing-specific conformance test, the generative rule, the zone intervals, density registers, and surface-level extension conditions.

---

## Terms

Two terms are defined here. Each is used throughout this document in its defined sense only. Terms defined in the Krutho Substrate (medium, unit of medium, substrate, zone, interval) are used throughout in their substrate-defined senses.

**Step.** A specific admitted spacing value. step(n) = n × 4px, where n is a positive integer. A step is identified by its multiplier: step 4 is 16px.

**Register.** A named configuration defining the spatial character of a surface class: its information density, white space behaviour, and the subset of the spacing scale appropriate to it. A register is a selection from the scale. Registers are defined and owned by this document.

---

## Conformance Test

Spacing admits even multiples of the substrate.

**Conformance test:** value mod 4 = 0.

**4px as the minimum spacing value.** A gap is a binary feature: present or absent. At 2px, a gap may round to 0 or 4 physical pixels on non-integer DPI displays. A value that renders inconsistently as separation does not perform the function of spacing. The minimum spacing value is therefore two substrate steps: 4px.

**Even multiples only.** From 4px, admitting odd multiples of the substrate (6, 10, 14) would place consecutive scale values 2px apart, reintroducing the unstable interval. Even multiples produce a scale whose step size matches its minimum value.

**Surface-level layout units.** A surface spec may define a layout unit larger than 4px. Any such unit satisfies the spacing conformance test. Surface-level layout units are defined by the surface spec. The Krutho Surface System will document the layout units used by each surface class.

---

## Generative Rule

The spacing scale is a rule.

step(n) = n × 4px, for any positive integer n.

The scale extends as far as the surface requires with no upper bound. A value is valid if and only if it satisfies the spacing conformance test.

The designed spacing set defined later in this document is a selection from the admitted scale, representing the values a surface is most likely to need. Surface-level extension beyond the designed set is permitted under the conditions stated in the Generative Escape section.

---

## Zone Intervals

Zone boundaries are defined in the Krutho Substrate: 20, 40, 80, 160, and 320 from the 10% threshold applied to the substrate's step sequence (2, 4, 8, 16, 32).

The spacing conformance test admits even multiples of the substrate. Consecutive admitted spacing values are separated by at least 4px. The spacing interval within a zone is therefore twice the substrate step that defines the zone's boundary.

| Zone      | Substrate step | Spacing interval |
|-----------|----------------|------------------|
| Fine      | 2px            | 4px              |
| Mid       | 4px            | 8px              |
| Display   | 8px            | 16px             |
| Large     | 16px           | 32px             |
| Statement | 32px           | 64px             |

### Admitted spacing values per zone

| Zone      | Interval | Upper boundary | Admitted spacing values |
|-----------|----------|----------------|-------------------------|
| Fine      | 4px      | 20px           | 4, 8, 12, 16, 20        |
| Mid       | 8px      | 40px           | 24, 32, 40              |
| Display   | 16px     | 80px           | 48, 64, 80              |
| Large     | 32px     | 160px          | 96, 128, 160            |
| Statement | 64px     | 320px          | 192, 256, 320           |

On-grid values between admitted steps within a zone are valid by the generative rule but are not in the designed step set. 28px, for example, satisfies the spacing conformance test (28 mod 4 = 0) and falls within the mid zone (20px to 40px), but the mid zone admits values at an 8px interval (24, 32, 40). Use at surface level requires documented justification.

---

## Density Registers

A register defines a surface class. It specifies the information density and white space behaviour that characterise the class, and the subset of the spacing scale appropriate to it.

Three registers are defined. A surface spec selects a register and applies the spatial values from this document.

**Register selection.** The register is selected by matching the surface's characteristics against the register descriptions below. A surface spec states which register it uses and which characteristics determine that selection. The selection is verifiable: an independent party can read the surface spec's stated characteristics and confirm they match the selected register's description.

Register selection is principled judgment applied to the surface's functional requirements. The register descriptions provide the criteria; the application of those criteria to a given surface is a human decision, recorded in the surface spec.

**Responsive surfaces.** A surface whose spatial character varies with scale may declare a register per scale class. Each register is selected by the rule above, applied to that scale class's characteristics. Spacing values at each scale class are drawn from the designed set of its declared register.

Multi-register declaration requires real variation in spatial character. A surface that uses different values at different scales but retains the same information density is a single-register surface. The reality of the variation is inspected before the declaration.

---

### Compact

**Surface class:** High information density. White space separates elements and aids scanning. Examples: documentation, dense UI, mobile application.

**Spatial character:** Tight internal spacing. Component padding and element gaps draw from the lower end of the spacing scale. Margins and section separation draw from the mid range.

**Designed spacing set:**

| Token    | Value |
|----------|-------|
| space-4  | 4px   |
| space-8  | 8px   |
| space-12 | 12px  |
| space-16 | 16px  |
| space-20 | 20px  |
| space-24 | 24px  |
| space-32 | 32px  |
| space-40 | 40px  |
| space-48 | 48px  |

Extension beyond space-48 is available by the generative rule. Surface-level use requires documentation.

---

### Standard

**Surface class:** Medium information density. White space balances structural and expressive functions. Examples: web, tablet, presentation deck.

**Spatial character:** Component padding and element gaps draw from the lower and mid ranges. Section separation and layout intervals draw from the mid and display ranges. The full designed set is in scope.

**Designed spacing set:**

| Token    | Value |
|----------|-------|
| space-4  | 4px   |
| space-8  | 8px   |
| space-12 | 12px  |
| space-16 | 16px  |
| space-20 | 20px  |
| space-24 | 24px  |
| space-32 | 32px  |
| space-40 | 40px  |
| space-48 | 48px  |
| space-64 | 64px  |
| space-80 | 80px  |
| space-96 | 96px  |

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

## Generative Escape

The designed spacing set for each register covers the range a surface in that class is most likely to need. A value outside the designed set is permitted under the following conditions.

The value satisfies the spacing conformance test for its production context.

The value is documented at surface level with a functional reason. The reason traces to a specific surface requirement that the designed set does not meet. Preference is not a functional reason.

The value is a surface-level extension of the register's designed set. Consistent need for values outside a register's designed set signals that the register selection is incorrect.

---

## Spacing Token Set

The full designed spacing token set, from which register-level designed sets are drawn. All values satisfy the spacing conformance test.

| Token     | Value | Step |
|-----------|-------|------|
| space-4   | 4px   | 1    |
| space-8   | 8px   | 2    |
| space-12  | 12px  | 3    |
| space-16  | 16px  | 4    |
| space-20  | 20px  | 5    |
| space-24  | 24px  | 6    |
| space-32  | 32px  | 8    |
| space-40  | 40px  | 10   |
| space-48  | 48px  | 12   |
| space-64  | 64px  | 16   |
| space-80  | 80px  | 20   |
| space-96  | 96px  | 24   |
| space-128 | 128px | 32   |
| space-160 | 160px | 40   |
| space-192 | 192px | 48   |

The token set is the union of the admitted spacing values for each zone. Within each zone, consecutive admitted values are separated by the zone's spacing interval: 4px in the fine zone, 8px in the mid zone, 16px in the display zone, 32px in the large zone, and 64px in the statement zone. The token set thins as the zone intervals widen.

On-grid values between admitted steps within a zone are valid by the generative rule but are not in the designed set. Examples: 28 between mid steps 24 and 32; 56 between display steps 48 and 64; 112 between large steps 96 and 128. Their absence follows from the zone structure. Use at surface level applies the generative escape conditions.

Values above space-192 are available by the generative rule with no upper bound. Surface-level use requires documentation.

---

## Governing Conditions

The following conditions state every assessable rule in this specification. Each can be applied by inspection to any value or output. Conditions that apply to the substrate (conformance at the 2px level, zone boundaries, production context declaration) are stated in the Krutho Substrate.

1. A spacing value is valid if and only if value mod 4 = 0 in the unit of the declared production context.
2. The spacing interval within each zone is stated in the Zone Intervals section. Spacing values on-grid for the substrate that fall between admitted spacing steps within a zone are valid by the generative rule. Surface-level use requires documentation with a functional reason.
3. Values outside the designed spacing set of a register are valid by the generative rule. Surface-level use requires documentation with a functional reason.
4. A functional reason traces to a specific surface requirement that the designed set does not meet. Preference is not a functional reason.
5. The designed spacing sets govern by default. The generative rule extends them where a documented surface-level reason applies.
6. Register selection is principled judgment applied against the register descriptions. The surface spec records the selection and the characteristics that determine it. Consistent use of values outside the selected register's designed set signals an incorrect register selection.
7. A responsive surface whose spatial character varies with scale may declare a register per scale class. The surface specification states each scale class, the register at each, and the characteristics that determine each selection. Multi-register declaration requires real variation in spatial character.
