# Krutho Design System

This document is the entry point. It orients a reader to the structure of the system and how its documents relate.

The system is structured in three layers: foundations specify the mechanical system, surfaces apply the foundations to rendering contexts, and a Figma plugin emits importable payloads from those specifications.

---

## Foundations

Six foundation documents specify the mechanical system. Foundations derive from one another in a chain rooted at the substrate.

| Document   | Derives from              | Governs                                             |
|------------|---------------------------|-----------------------------------------------------|
| Substrate  |                           | Medium, unit, conformance, production context       |
| Typography | Substrate                 | Typefaces, weights, sizes, line heights             |
| Spacing    | Substrate                 | Spatial intervals, density registers, tokens        |
| Grid       | Substrate through Spacing | Construction references, sub-grid structure         |
| Layout     | Spacing                   | Column structure, margins, gutters, column width    |
| Colour     |                           | Primitive scales, semantic tokens, component tokens |

Foundations are specified with the precision of formal outputs. Tokens, conformance tests, and derivations are inspectable by any party.

Source files live in [foundation/](foundation/).

---

## Rationale

The reasoning behind the system, including why each foundation exists and why each value was chosen, is captured in [rationale.md](rationale.md). It is brand-agnostic; specific values (typefaces, colour anchors) belong to consuming projects.

---

## Surfaces

Surfaces apply the foundations to rendering contexts.

| Document | Applies to                                                                |
|----------|---------------------------------------------------------------------------|
| Website  | Marketing, documentation, narrative, informational pages rendered on web  |

A surface specification declares its production context, density register, and selections from the foundation tokens appropriate to its purpose. Surfaces derive from the foundations; they do not modify them.

Source files live in [surfaces/](surfaces/).

---

## Document structure

Each document specifies the values it governs: tokens, conformance tests where applicable, and derivation rules. Terms are defined inline where used, or in a Terms section where multiple coupled definitions warrant collection. Cross-document references are by token name.

---

## Conventions

**Em dashes are excluded.** All output uses the correct alternative determined by sentence structure: colon, period, comma, or restructuring.

**Terminology is exact.** Each document uses its terms in the sense it defines them.

**Values are derived.** Every value in the system traces to a foundation. Surface specifications and applications select from admitted values.

**Conformance is assessable by inspection.** Every value in the system is admitted or derived. Conformance is established by checking values against the admitted token sets and derivation rules in each document.

---

## Extending the system

A new surface specification declares its production context, selects its density register, and applies the foundation tokens appropriate to its purpose. It derives; it does not modify.

A new foundation document derives from the substrate through the existing chain. It applies additional constraints to admitted values rather than introducing new values.

Refinement of existing documents follows the same approach: the system within each document is the subject of the work; the document around the system is adjusted without modifying the mechanics.

---

## Figma plugin

The system ships a Figma plugin and a build script that emits importable payloads from the foundation and surface specs. Output matches the specification documents by construction.

| Path                                                       | Role                                                           |
|------------------------------------------------------------|----------------------------------------------------------------|
| [figma/build.py](figma/build.py)                           | Generates JSON payloads from the spec values                   |
| [figma/foundation.json](figma/foundation.json)             | Colour primitives, colour semantic, spacing, grid, typography  |
| [figma/surface-website.json](figma/surface-website.json)   | Website text styles, one set per breakpoint                    |
| [figma/plugin/](figma/plugin/)                             | The Figma plugin that imports the payloads                     |

**Regenerate the payloads.**

```
cd figma
python3 build.py                    # foundation + website surface
python3 build.py foundation         # foundation only
python3 build.py surface website    # website surface only
```

**Import into Figma.** Load the plugin from [figma/plugin/](figma/plugin/) via Figma's Plugins, Development, Import plugin from manifest. The plugin reads the emitted JSON files and creates variable collections and text styles in the current Figma file.

Foundation is imported once per file. Surfaces are imported where the surface specification applies. Text styles are a surface-layer concept: they bundle typography variables into role-specific applicable styles.

---

Last edit 15th May 2026