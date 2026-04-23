# Krutho Design System

The Krutho design system governs visual output across product, enterprise, and brand contexts. It operates under the Krutho Design Philosophy: the brand does not claim, it demonstrates.

This document is the entry point. It orients a reader to the structure of the system and how its documents relate.

---

## Start here

Three documents establish the system's disposition and direction:

- **Philosophy.** What Krutho values and why the design reflects those values.
- **Principles.** The operating framework for design decisions.
- **Evaluation.** The inspection layer for finished work.

Read these in order. Together they take under fifteen minutes.

---

## Foundations

Seven foundation documents specify the mechanical system. Foundations derive from one another in a chain rooted at the substrate.

| Document   | Derives from              | Governs                                          |
|------------|---------------------------|--------------------------------------------------|
| Substrate  | —                         | Medium, unit, conformance, zone structure        |
| Typography | Substrate                 | Typeface tiers, weights, sizes, line heights     |
| Spacing    | Substrate                 | Spatial intervals, density registers, tokens     |
| Grids      | Substrate through Spacing | Construction alignment, sub-grid chain           |
| Layout     | Spacing                   | Column structure, margins, gutters, column width |
| Colour     | —                         | Primitive scales, semantic tokens, three layers  |
| Wordmark   | References Colour         | Construction, scale, position                    |

Foundations are specified with the precision of formal outputs. Tokens, conformance tests, and derivations are inspectable by any party.

---

## Surfaces

Surfaces apply the foundations to rendering contexts.

| Document | Applies to                                                                |
|----------|---------------------------------------------------------------------------|
| Web      | Marketing, documentation, narrative, informational pages rendered on web  |
| Diagrams | Technical diagrams and data visualisations                                |

A surface specification declares its production context, density register, and selections from the foundation tokens appropriate to its purpose. Surfaces derive from the foundations; they do not modify them.

---

## Document structure

Each document follows a consistent structure:

- **Grounding Statement.** What the document is, what governs it, what it establishes.
- **Terms.** Defined where the document introduces or uses terms in a specific sense.
- **Body.** The specification itself.
- **Governing Conditions.** The assessable rules, inspectable by any party.

Foundation and surface documents reproduce cross-referenced tables at the end so that each document remains self-contained and independently verifiable.

---

## Conventions

**Em dashes are excluded.** All Krutho output uses the correct alternative determined by sentence structure: colon, period, comma, or restructuring.

**Terminology is exact.** Defined terms are used in their defined sense throughout. Where the same word carries different meanings in different documents (Layer in Colour, Tier in Typography), each document uses its own defined term.

**Values are derived.** Every value in the system traces to a foundation. Surface specifications and applications select from admitted values.

**Conformance is assessable by inspection.** Every specification states its conditions as rules that can be applied to any output without requiring contextual interpretation.

---

## Extending the system

A new surface specification declares its production context, selects its density register, and applies the foundation tokens appropriate to its purpose. It derives; it does not modify.

A new foundation document derives from the substrate through the existing chain. It applies additional constraints to admitted values rather than introducing new values.

Refinement of existing documents follows the same approach: the system within each document is the subject of the work; the document around the system is adjusted without modifying the mechanics.

---

## Figma plugin

The system ships a Figma plugin and a build script that emits importable payloads from the foundation and surface specs. Output matches the specification documents by construction.

| Path                                     | Role                                                           |
|------------------------------------------|----------------------------------------------------------------|
| [figma/build.py](krutho-design-system/figma/build.py)                     | Generates JSON payloads from the spec values                   |
| [figma/foundation.json](krutho-design-system/figma/foundation.json)       | Colour primitives, colour semantic, spacing, grid, typography  |
| [figma/surface-diagrams.json](krutho-design-system/figma/surface-diagrams.json) | Diagram colour collection                                      |
| [figma/surface-website.json](krutho-design-system/figma/surface-website.json)   | Website text styles, one set per breakpoint                    |
| [figma/plugin/](krutho-design-system/figma/plugin/)                       | The Figma plugin that imports the payloads                     |

**Regenerate the payloads.**

```
cd krutho-design-system/figma
python3 build.py                    # foundation + all surfaces
python3 build.py foundation         # foundation only
python3 build.py surface diagrams   # diagrams surface only
python3 build.py surface website    # website surface only
```

**Import into Figma.** Load the plugin from [figma/plugin/](krutho-design-system/figma/plugin/) via Figma's Plugins, Development, Import plugin from manifest. The plugin reads the emitted JSON files and creates variable collections and text styles in the current Figma file.

Foundation is imported once per file. Surfaces are imported where the surface specification applies. Text styles are a surface-layer concept: they bundle typography variables into role-specific applicable styles.

---

Last edit 23rd April 2026
