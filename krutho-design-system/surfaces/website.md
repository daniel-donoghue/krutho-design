# Krutho Web Surface

Last edit 23rd April 2026

---

## Grounding Statement

This document is the Krutho Web Surface specification. It operates under the Krutho Design Philosophy and derives from the Krutho Spacing System, the Krutho Typography System, the Krutho Grid System, the Krutho Layout System, and the Krutho Colour System.

The Web Surface specification declares how the foundation documents are realised on content surfaces rendered in a web browser. Every value in this document traces to a foundation document. Reference tables from the foundations are reproduced at the end so that output can be verified against this specification directly.

**Scope.** This specification governs content surfaces on the web: marketing, documentation, narrative, and informational pages. Product and application UI surfaces are governed by a separate surface specification. Colour assignment at surface level will be added in a subsequent revision.

---

## Terms

The following terms are defined here. Terms not defined here inherit their definitions from the foundation documents named in the Grounding Statement.

**Breakpoint.** A viewport width threshold at which the surface adapts its structure or its typographic assignments. Two categories are defined in this document.

**Structural breakpoint.** A breakpoint where the grid structure, specifically the column count or the margin, changes. Three structural breakpoints are declared: SM, MD, LG.

**Display breakpoint.** A breakpoint where the grid structure holds and type role assignments advance to reflect larger column widths. Three display breakpoints are declared: Display-SM, Display-MD, Display-LG.

**Role.** A content function assigned to a specific combination of typeface tier, type size, weight, and line height. Roles are declared in the Type Role Set section.

**Tier 1 functional category.** A functional category per the Krutho Typography System Weight Vocabulary: Display, Structural, Continuous reading, Inline emphasis. Each Tier 1 role in this specification is assigned to one category. Tier 2 roles are determined by tier alone.

---

## Production Context

This surface declares its production context as screen. All spacing values are in CSS logical pixels (px). All type sizes are in CSS logical pixels. Conformance tests apply in px per the Krutho Spacing System and the Krutho Typography System.

---

## Density Register

The Web Surface is a responsive surface per the Krutho Spacing System's Responsive Surfaces provision. Its spatial character varies across scale classes, so a register is declared at each structural scale class. Registers at Display breakpoints hold the LG register because those breakpoints preserve the LG grid and add only type role advancement.

| Breakpoint | Column count | Register   | Characteristics determining register                                                                                                             |
|------------|--------------|------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| SM         | 2            | Compact    | High information density relative to surface width. Content is tight. White space is structural, separating content rather than expressing it.   |
| MD         | 8            | Standard   | Medium information density. White space balances structural and expressive functions.                                                            |
| LG         | 16           | Expressive | Lower information density than MD. White space begins to express, not only structure. Content intervals grow into the mid and display zones.    |
| Display-SM | 16           | Expressive | Inherits LG register. Expressive character intensifies as column width grows.                                                                    |
| Display-MD | 16           | Expressive | Inherits LG register. Expressive character intensifies as column width grows.                                                                    |
| Display-LG | 16           | Expressive | Inherits LG register. Expressive character is strongest at viewports above 1856.                                                                 |

Each register declaration satisfies the Register selection rule independently per the Krutho Spacing System: the characteristics stated above match the register descriptions in the foundation.

At each breakpoint, the spacing values available to the surface are those in the declared register's designed spacing set. The Compact designed set applies at SM (space-4 through space-48). The Standard designed set applies at MD (space-4 through space-96). The Expressive designed set applies at LG through Display-LG (space-16 through space-192).

---

## Breakpoint System

Six breakpoints are declared. Three are structural and three are display.

| Breakpoint | Viewport range | Category   |
|------------|----------------|------------|
| SM         | 320 to 575     | Structural |
| MD         | 576 to 1087    | Structural |
| LG         | 1088 to 1343   | Structural |
| Display-SM | 1344 to 1599   | Display    |
| Display-MD | 1600 to 1855   | Display    |
| Display-LG | 1856 and above | Display    |

**Structural breakpoint derivation.**

Structural breakpoints trigger at the smallest viewport producing column width at least 32px (mid zone first admitted step per the Krutho Spacing System) under the breakpoint's column count, margin, and gutter.

SM triggers at 320. This is the smallest viewport the specification addresses. Viewports below 320 are outside this specification; surface instances requiring support below 320 document the extension under the generative escape rule.

MD triggers at 576. At 576, 8 columns with margin 48 and gutter 32 produce column width 32.

LG triggers at 1088. At 1088, 16 columns with margin 48 and gutter 32 produce column width 32.

**Display breakpoint derivation.**

Display breakpoints trigger at viewports where column width, under the LG grid configuration (16 cols, margin 48, gutter 32), reaches a display zone admitted step per the Krutho Spacing System.

Display-SM triggers at 1344. Column width is 48 (display zone first admitted step).

Display-MD triggers at 1600. Column width is 64 (display zone middle admitted step).

Display-LG triggers at 1856. Column width is 80 (display zone upper boundary).

Beyond Display-LG, column width would cross into the large zone, which governs page-scale structural intervals rather than element-scale modules. A column occupying page-scale territory is structurally a different entity. The Content Lock section declares surface behaviour at viewports beyond 1856.

**SM column count admission.**

SM uses 2 columns. The Krutho Layout System admits 2 columns at scales where a binary split is the correct grid. This specification declares SM as such a scale: at viewports 320 to 575, the correct content structure is a single visual column with occasional binary splits. Finer subdivision at this scale produces column widths too narrow for functional content.

**SM margin selection.**

SM uses margin 16. At viewports 320 to 575, margin 48 would consume approximately 30 percent of surface width in edge buffer, a disproportionate allocation at small viewport scale. Margin 16 reduces the edge buffer to approximately 10 percent at the SM minimum viewport, matching the proportional balance of larger breakpoints. Margin 16 is a fine zone admitted spacing value.

---

## Grid Structure

The Web Surface declares column count, margin, gutter, primary grid value, and derived column width at each breakpoint.

| Breakpoint | Cols | Margin | Gutter | Primary grid | Col width at min |
|------------|------|--------|--------|--------------|------------------|
| SM         | 2    | 16     | 32     | grid-16      | 128              |
| MD         | 8    | 48     | 32     | grid-16      | 32               |
| LG         | 16   | 48     | 32     | grid-16      | 32               |
| Display-SM | 16   | 48     | 32     | grid-16      | 48               |
| Display-MD | 16   | 48     | 32     | grid-16      | 64               |
| Display-LG | 16   | 48     | 32     | grid-16      | 80               |

**Margin values.**

Margin 48 (mid zone upper admitted step) at MD through Display-LG. The margin function is to provide an edge buffer between content and surface edge. This function is a property of reading and interaction, not of viewport width, so the margin value holds across breakpoints at mid-viewport scale and above.

Margin 16 at SM, as derived in the Breakpoint System section.

**Gutter value.**

Gutter 32 (mid zone middle admitted step) at all breakpoints.

At MD through Display-LG, gutter 32 is two-thirds of margin 48. Gutter 32 does not exceed margin 48, satisfying Governing Condition 5 of the Krutho Layout System at column counts of 4 and above.

At SM, column count is 2. Per the Krutho Layout System Governing Condition 5, the gutter-margin relationship at column count 2 is governed by this surface specification. SM declares margin 16 and gutter 32. Content at column count 2 is grouped as two halves rather than as a flowing series; the gutter governs the visible split between halves. A gutter smaller than the margin would make the binary split ambiguous. A gutter larger than the margin makes the binary split visually clear. The margin remains smaller because its function (edge buffer) does not require the same visual weight as the intra-content split.

**Primary grid.**

grid-16 at all breakpoints. grid-16 is the largest admitted grid value that divides both margin 48 and gutter 32 exactly at MD through Display-LG. At SM, grid-16 also divides both margin 16 and gutter 32 exactly. The alignment condition of the Krutho Grid System is satisfied at every breakpoint.

Larger admitted grid values (grid-32, grid-64) do not divide margin 48 without a remainder and therefore do not satisfy the alignment condition. grid-16 is the largest value that does.

**Derived column width.**

Column width is derived from the surface configuration per the Krutho Layout System. The column width values in the table above are computed at the breakpoint minimum viewport. Within each breakpoint's range, column width varies fluidly with viewport.

---

## Content Lock

At viewport 1856 and above, content area is locked at 1760. Margins expand symmetrically to fill the remaining viewport width.

**Derivation.** 1760 is the content area at Display-LG minimum viewport: 1856 minus two margins of 48 equals 1760. It is the largest content area produced by the grid under the declared structural values before column width would enter the large zone. Beyond 1856, allowing the content area to expand would push column width past 80 into large-zone territory. Per the Krutho Spacing System, values at and above 96 govern page-scale structural intervals, not element-scale modules. A column occupying page-scale territory is structurally a different entity.

1760 sits on the 4px lattice (1760 divided by 4 equals 440). It is a derived structural value, not a spacing token. The value enters this specification only as a consequence of the declared grid structure at Display-LG minimum viewport.

---

## Type Role Set

The Web Surface declares eleven content roles. The role set is canonical across Krutho web content surfaces. Product and application UI surfaces declare their own role set.

| Role      | Tier | Typeface         | Weight         | Tier 1 functional category |
|-----------|------|------------------|----------------|----------------------------|
| Display 1 | 1    | Spline Sans      | Medium (500)   | Display                    |
| Display 2 | 1    | Spline Sans      | Medium (500)   | Display                    |
| Heading 1 | 1    | Spline Sans      | Semibold (600) | Structural                 |
| Heading 2 | 1    | Spline Sans      | Semibold (600) | Structural                 |
| Heading 3 | 1    | Spline Sans      | Semibold (600) | Structural                 |
| Heading 4 | 1    | Spline Sans      | Semibold (600) | Structural                 |
| Lead      | 1    | Spline Sans      | Regular (400)  | Continuous reading         |
| Body      | 1    | Spline Sans      | Regular (400)  | Continuous reading         |
| Caption   | 1    | Spline Sans      | Regular (400)  | Continuous reading         |
| Code      | 2    | Spline Sans Mono | Regular (400)  |                            |
| Eyebrow   | 2    | Spline Sans Mono | Regular (400)  |                            |

The Tier 1 functional category column applies only to Tier 1 roles. Code and Eyebrow are Tier 2; their typeface and weight are determined by tier: Spline Sans Mono, Regular.

Inline body emphasis is Bold (700) applied within Body flow where emphasis is functionally required. It is a weight variant, not a role: the Inline emphasis functional category per the Krutho Typography System.

**Role definitions.**

**Display 1.** The largest type on a surface. Reserved for surfaces where a single statement is the surface's reason for existing. Hero surfaces, title slides, landing pages.

**Display 2.** Secondary display size. Admitted in one of two conditions: where Display 1 exceeds the surface instance's line-count threshold at its assigned column span, or where a stepped relationship to Display 1 is required in a multi-display composition. The line-count threshold is a surface instance decision, documented at that level.

**Heading 1.** The top of the structural hierarchy within content. Page title where Display roles are not present. Primary section title where Display roles are present.

**Heading 2.** Section divisions within content.

**Heading 3.** Subsection divisions within a Heading 2.

**Heading 4.** Deeper subsection divisions. Used where structural depth requires a fourth level below Heading 3.

**Lead.** An emphasised opening paragraph or standfirst. Body-adjacent in function. Where Lead and Heading 4 share a size at a given breakpoint, the two are differentiated by weight (Lead Regular, Heading 4 Semibold) and by position (Lead opens a content block, Heading 4 divides a content block).

**Body.** The default reading size for continuous content.

**Caption.** Secondary supporting text. Metadata, image captions, annotations, fine print.

**Code.** Tier 2 content per the Krutho Typography System. The Code role is the mechanism for rendering code, tokens, CLI representations, and other structured or verifiable content in monospaced type. Differentiation from Tier 1 is carried by the typeface.

**Eyebrow.** An identifier placed above a heading. Carries a schema-defined value: section number, taxonomy path, kind-of-content tag, or other identifier drawn from a fixed set. Eyebrow content satisfies the Tier 2 admission test per the Krutho Typography System: the value is an identifier with determinable correctness against its schema. Differentiation from Tier 1 is carried by the typeface. Eyebrow renders in uppercase per the Case Assignment section and carries tracking per the Tracking Assignment section.

---

## Type Role Size Assignment

Each role is assigned a type token from the Krutho Typography System at each breakpoint. Values in the table are type token sizes in px.

| Role      | SM | MD | LG | Display-SM | Display-MD | Display-LG |
|-----------|----|----|----|------------|------------|------------|
| Display 1 | 48 | 48 | 48 | 64         | 80         | 96         |
| Display 2 | 40 | 40 | 40 | 48         | 64         | 80         |
| Heading 1 | 32 | 32 | 32 | 40         | 48         | 64         |
| Heading 2 | 24 | 24 | 24 | 32         | 40         | 48         |
| Heading 3 | 20 | 20 | 20 | 24         | 32         | 40         |
| Heading 4 | 18 | 18 | 18 | 20         | 24         | 32         |
| Lead      | 18 | 18 | 18 | 18         | 18         | 24         |
| Body      | 16 | 16 | 16 | 16         | 16         | 20         |
| Caption   | 12 | 12 | 12 | 12         | 12         | 14         |
| Code      | 14 | 14 | 14 | 14         | 14         | 16         |
| Eyebrow   | 12 | 12 | 12 | 12         | 12         | 14         |

**Progression rule for SM, MD, LG.**

SM, MD, and LG share a single token assignment. Each role's token at LG is sized for 16-column composition at column width 32. At MD and SM, the column count differs (8 and 2) but the per-column content density is equivalent. A role's presence relative to its column holds across structural breakpoints.

**Progression rule for Display breakpoints.**

At Display breakpoints, column width grows past its LG minimum. Display and structural roles (Display 1, Display 2, Heading 1 through Heading 4) advance through zone-admitted spacing steps at each Display breakpoint. The advancement is one step per breakpoint per role.

Zone-admitted spacing steps, per the Krutho Spacing System, used for this progression:

| Zone    | Admitted steps |
|---------|----------------|
| Fine    | 20             |
| Mid     | 24, 32, 40     |
| Display | 48, 64, 80     |
| Large   | 96             |

Type tokens outside the spacing admitted step progression (type-14, type-18, type-28) appear at the LG baseline for roles where that specific token matches the role's function. They are baseline values, not progression values for display or structural advancement.

**Progression rule for Continuous reading roles and Tier 2 roles.**

Lead, Body, Caption, Code, and Eyebrow hold their token assignment across SM through Display-MD. At Display-LG, all five roles advance to maintain readability at viewing distances typical of displays at 1856 viewport and above.

Two rules govern the advancements. Body is the anchor; the others follow.

**Body advances per the spacing-admitted step progression.** Body advances from type-16 to type-20. The spacing-admitted steps in the fine zone are 4, 8, 12, 16, 20; type-20 is the next admitted step after type-16. Type-18 is a designed type token outside this progression and is not a progression step for Body. Body's position on the spacing-admitted progression is preserved, keeping Body's size in a known structural relationship to the spacing values on the surface.

**Lead, Caption, Code, and Eyebrow advance to the next designed type token above baseline that preserves the baseline ordering Lead > Body > Code > Caption.** This rule applies to Lead, Caption, Code, and Eyebrow. Eyebrow shares Caption's baseline token and tracks Caption's advancement so that the two roles hold a shared size at every breakpoint. Body's advancement is governed by the rule above.

Applying the second rule:

- Lead baseline type-18 advances to type-24. The designed type tokens above type-18 are type-20 and type-24. Body at Display-LG occupies type-20. Lead advances to type-24 to remain above Body.
- Caption baseline type-12 advances to type-14. Type-14 is the next designed type token above type-12 and is below Body's type-20, preserving Caption's position below Body.
- Code baseline type-14 advances to type-16. Type-16 is the next designed type token above type-14 and is below Body's type-20, preserving Code's position below Body.
- Eyebrow baseline type-12 advances to type-14. Eyebrow shares Caption's baseline; the same advancement applies, preserving Eyebrow's position below Body and its shared size with Caption.

Each advancement is the minimum step that satisfies its governing rule. The two rules together produce the Display-LG assignments for continuous reading and Tier 2.

**Excluded progression patterns.**

Scaling down from LG toward SM is not admitted. A role at SM using a smaller token than LG would under-scale the role relative to its column density, which does not change across structural breakpoints.

Proportional scaling to column width is not admitted. Doubling column width from LG to Display-MD (32 to 64) would imply doubling token size, which produces values outside the type token set's designed progression and does not correspond to functional presence requirements.

---

## Line Height Assignment

Line heights are drawn from the Krutho Typography System Line Height Token Set. For Tier 1 roles, the variant is determined by the role's Tier 1 functional category. For Tier 2 roles, the variant is declared directly.

**Variant assignment.**

| Tier 1 functional category | Variant |
|----------------------------|---------|
| Display                    | Tight   |
| Structural                 | Tight   |
| Continuous reading         | Default |

Display and structural roles use Tight because their function is hierarchical signalling within a composition. Inter-line space within a display or heading is tight relative to the space around it, which is produced by spacing tokens rather than line height. Continuous reading roles use Default for sustained reading.

**Code and Eyebrow (Tier 2).** Both Tier 2 roles use the Default variant, declared directly. Default matches body reading cadence for Code, which appears inline within body content. Eyebrow uses Default for consistency with Caption, whose type token assignment it shares at every breakpoint.

**Resolution.**

For each role at each breakpoint, the line height token is lh-{size}-{variant}, where size is the role's type token size and variant is the category variant above (Tier 1 roles) or the declared variant for the role (Tier 2). The lh token resolves to a specific px value per the Krutho Typography System Line Height Token Set.

Surface instances may declare Loose variant for specific contexts (extended documentation, accessibility-led reading surfaces). Instance-level extension follows the generative escape rule.

---

## Case Assignment

Each role renders at a declared case. Case is a presentation-layer transform; it does not alter the stored content.

| Role    | Case     |
|---------|----------|
| Eyebrow | Upper    |
| All others | Original |

**Original.** The role renders at the authored case of its content. This is the default and applies to every role except Eyebrow.

**Upper.** The role renders in uppercase. Eyebrow uses Upper because its content is a schema-defined identifier rather than reading copy. Upper makes the identifier visually distinct from surrounding continuous reading text and matches the monospaced Tier 2 treatment that signals machine-verifiable content.

**Resolution.** Upper is applied at render time via CSS text-transform: uppercase. The underlying content string holds its schema-defined case; no transformation is applied to the source value.

---

## Tracking Assignment

Each role declares a tracking value. Tracking is expressed as a percentage of type size so the value scales with size across breakpoints.

| Role    | Tracking |
|---------|----------|
| Eyebrow | +5%      |
| All others | 0 (Normal) |

**Normal.** Default letter-spacing as set by the typeface. This is the default and applies to every role except Eyebrow.

**+5% Eyebrow tracking.** Eyebrow renders in uppercase at small type tokens (type-12, type-14). At these sizes, uppercase letterforms in Spline Sans Mono set without tracking produce visually tight counters and neighbouring-letter spacing. +5% restores optical balance at identifier scale. The value is the minimum tracking that achieves this without introducing letterform isolation, which would read as emphasis rather than as a label.

**Resolution.** The percentage is applied as CSS letter-spacing expressed in em (+5% resolves to 0.05em). Figma text styles store the equivalent value as letterSpacing with unit PERCENT.

---

## Governing Conditions

The following conditions state the assessable rules in this specification. Each can be applied by inspection to any output rendered under this specification.

1. The production context is screen. All values are in CSS logical pixels (px).
2. The surface is a responsive surface per the Krutho Spacing System's Responsive Surfaces provision. The density register is declared per breakpoint per the Density Register table: SM is Compact, MD is Standard, LG and Display breakpoints are Expressive. Each declared register satisfies the Register selection rule independently.
3. The six breakpoints are SM (320 to 575), MD (576 to 1087), LG (1088 to 1343), Display-SM (1344 to 1599), Display-MD (1600 to 1855), Display-LG (1856 and above).
4. The column count is 2 at SM, 8 at MD, and 16 at LG through Display-LG. SM admission of 2 columns traces to the Krutho Layout System's scale-conditional admission.
5. Margin is 16 at SM. Margin is 48 at MD through Display-LG. Gutter is 32 at all breakpoints.
6. Primary grid is grid-16 at all breakpoints. Sub-grid, where declared by a composition, follows the Krutho Grid System.
7. Content area is locked at 1760 when viewport reaches or exceeds 1856. Margins expand symmetrically to fill the remaining viewport width.
8. Type role assignments follow the Type Role Size Assignment table. SM, MD, LG share a single token assignment. Display-SM, Display-MD, Display-LG each have a distinct token assignment per role.
9. Weight assignments follow the Type Role Set table and the Krutho Typography System Weight Vocabulary. Bold (700) is admitted only as an inline weight variant for Body emphasis.
10. Line height assignments follow the Line Height Assignment section. Instance-level extension to Loose variant requires documentation under the generative escape rule.
11. Case assignments follow the Case Assignment section. Eyebrow renders in uppercase; all other roles render at Original case. Case is a presentation-layer transform and does not alter the stored content.
12. Tracking assignments follow the Tracking Assignment section. Eyebrow carries +5% tracking; all other roles carry Normal tracking. Tracking is expressed as a percentage of type size.
13. Every value in this specification derives from a foundation document.

---

## Reference Tables

Reproduced from foundation documents for independent verification. Values are not defined by this document. A change to a foundation document requires updating the corresponding table below.

**Spacing tokens referenced by this specification.** Reproduced from the Krutho Spacing System.

| Token     | Value |
|-----------|-------|
| space-4   | 4px   |
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

**Zone structure.** Reproduced from the Krutho Spacing System.

| Zone      | Interval | Upper boundary | Admitted spacing values |
|-----------|----------|----------------|-------------------------|
| Fine      | 4        | 20             | 4, 8, 12, 16, 20        |
| Mid       | 8        | 40             | 24, 32, 40              |
| Display   | 16       | 80             | 48, 64, 80              |
| Large     | 32       | 160            | 96, 128, 160            |
| Statement | 64       | 320            | 192, 256, 320           |

**Grid values.** Reproduced from the Krutho Grid System.

| Token   | Value |
|---------|-------|
| grid-4  | 4px   |
| grid-8  | 8px   |
| grid-16 | 16px  |
| grid-32 | 32px  |
| grid-64 | 64px  |

**Type tokens referenced by this specification.** Reproduced from the Krutho Typography System Type Token Set.

| Token   | Size |
|---------|------|
| type-12 | 12px |
| type-14 | 14px |
| type-16 | 16px |
| type-18 | 18px |
| type-20 | 20px |
| type-24 | 24px |
| type-32 | 32px |
| type-40 | 40px |
| type-48 | 48px |
| type-64 | 64px |
| type-80 | 80px |
| type-96 | 96px |

**Weight vocabulary.** Reproduced from the Krutho Typography System Weight Vocabulary.

| Weight   | Value | Functional category within Tier 1 |
|----------|-------|-----------------------------------|
| Regular  | 400   | Continuous reading                |
| Medium   | 500   | Display                           |
| Semibold | 600   | Structural                        |
| Bold     | 700   | Inline emphasis                   |

**Typography tiers.** Reproduced from the Krutho Typography System Typeface Tier Model.

| Tier | Typeface         | Function                                              |
|------|------------------|-------------------------------------------------------|
| 1    | Spline Sans      | Operational clarity. The primary voice of the system. |
| 2    | Spline Sans Mono | Verifiable structure. System-derived output.          |
| 3    | Enra             | Interpretive weight. Significance.                    |

**Density registers.** Reproduced from the Krutho Spacing System and the Krutho Layout System.

| Register   | Information density | Typical column counts (Layout System) |
|------------|---------------------|---------------------------------------|
| Compact    | High                | 2, 4                                  |
| Standard   | Medium              | 8, 12                                 |
| Expressive | Low                 | 16                                    |
