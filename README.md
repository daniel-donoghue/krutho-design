# Krutho Design System

Specification documents for the Krutho brand and product design system.

## Structure

```
krutho-design-system/
├── krutho-philosophy.md
├── foundation/
├── surfaces/
└── figma/
```

The system is organised in layers. The philosophy governs the foundation. The foundation governs the surfaces. Every document derives from the one above it and traces its decisions to reasons that exclude the alternatives.

## Documents

**[Krutho Design Philosophy](krutho-design-system/krutho-philosophy.md)**
The governing document. Defines the four terms (Precision, Correctness, Verifiability, Truth), the chain that connects them, and the operational conditions that govern every document derived from it. Read this first.

**[foundation/](krutho-design-system/foundation/)**
Specifications for the construction primitives.

- [Wordmark](krutho-design-system/foundation/wordmark.md)
- [Colour](krutho-design-system/foundation/colour.md)
- [Typography](krutho-design-system/foundation/typography.md)
- [Spacing](krutho-design-system/foundation/spacing.md)
- [Grids](krutho-design-system/foundation/grids.md)
- [Layout](krutho-design-system/foundation/layout.md)

**[surfaces/](krutho-design-system/surfaces/)**
Specifications for rendered surface contexts. A surface consumes foundation tokens and adds surface-specific rules.

- [Diagrams](krutho-design-system/surfaces/diagrams.md)
- [Website](krutho-design-system/surfaces/website.md)

**[figma/](krutho-design-system/figma/)**
Token generator and companion Figma plugin. `build.py` emits `foundation.json` (imported into every Figma file) and per-surface payloads (e.g. `surface-diagrams.json`) that are added only where that surface is in use.

## Reading conventions

Every document follows the same structure. Each is self-contained: it can be read and verified without consulting another document. Each begins with a Grounding Statement linking it to the philosophy. Each defines its terms, derives its values, and states its Governing Conditions explicitly so that any output can be checked against them.

## Verifying conformance

Read the relevant document. Check the output against the document's Governing Conditions section. If conformance cannot be assessed from the document alone, that is a failure of the specification, not the output.
