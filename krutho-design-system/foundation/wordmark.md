# Krutho Wordmark

Last edit 10th April 2026

---

## Grounding Statement

This document operates under the Krutho Design Philosophy. The terms precision, correctness, verifiability, and truth are used throughout in the senses defined there. Every decision in this document traces to a reason that excludes the alternatives.

---

## Intent

The Krutho wordmark was designed to a standard of correctness. Each letterform was constructed through a strict geometric process. The construction is not incidental: it is the specification.

The wordmark was constructed against a 16-unit grid. The stroke width is 4 grid units. The cap height is 27 grid units. Every relationship in the construction derives from these values.

The slight awkwardness that emerges from strict geometric process is not a failure of the system. It is evidence of the system. Pure geometry applied without modification produces something that is correct but not legible at the optical level. The small human modifications introduced to achieve correct optical reading are themselves system decisions: each traces to a legibility condition, not to preference. The wordmark is precise after those modifications, not before them.

The truncated r, a stem and arm with no bowl, is the most visible expression of this logic. It is a correct letterform, produced by the same construction constraints governing every other character in the wordmark. Its code-adjacent appearance is a consequence of process.

---

## Construction

The wordmark letterforms were constructed geometrically. The following properties are registered as construction invariants. These are the criteria against which a given instance of the wordmark is assessed for correctness.

**Stroke weight.** A single stroke weight is used throughout. The stroke width is 4 grid units. No letterform departs from this weight. Optical corrections that appear to modify weight do so through geometry, not through a change in the underlying stroke value.

**Bowl geometry.** Round characters derive their bowl shapes from circular construction. The circles are defined as exact geometric primitives. Curvature deviates from the circle only where optical correction requires it, and each such deviation is a minimum necessary adjustment.

**Stem consistency.** Vertical stems share a consistent width, derived from the stroke weight. The K diagonal strokes are constructed at angles traceable to the geometric grid.

**Human modifications.** Three optical corrections were applied to the geometrically constructed forms. Each traces to a specific legibility condition.

Overshoot: round characters extend fractionally beyond the cap height and baseline. Without this correction, round forms read as smaller than flat-topped characters at the same metric height.

Junction compensation: where the K diagonals meet the vertical stem, the intersection mass is reduced. Unmodified, diagonal-to-stem junctions accumulate optically and read as heavier than the surrounding stroke weight.

Terminal refinement: the truncated r arm terminus is adjusted to resolve cleanly. The arm ends without a bowl. The termination requires precision to read as a construction decision rather than an incomplete form.

---

## Colour

The wordmark is rendered in three values. No other colour treatment is permitted.

### Registered values

**Near-black** `#181818`. Applied on light backgrounds: surface-overlay, surface-raised, and surface-base as defined in the Krutho Colour System. This is the primary application.

**White** `#FFFFFF`. Applied on dark backgrounds: surface-base dark, surface-raised dark, and deep base values as defined in the Krutho Colour System.

**Signal Blue** `#1A6FFF`. The third admitted value. Applied in Layer 3 brand expression contexts as defined in the Krutho Colour System, at or above the registered minimum size.

### Contrast basis

Signal Blue against each registered background has been verified by calculation against the WCAG relative luminance formula. Results are recorded here as a specification condition.

| Background   | Value     | Ratio  | AA normal text | AA large / display |
|--------------|-----------|--------|----------------|--------------------|
| Near-black   | `#181818` | 4.03:1 | Fail           | Pass               |
| White        | `#FFFFFF` | 4.41:1 | Fail           | Pass               |
| Deep base    | `#000035` | 4.53:1 | Pass           | Pass               |

Signal Blue on deep base is admissible at all registered wordmark sizes.

Signal Blue on near-black and white passes at display scale. The applicable threshold at display scale is 3:1. Both pairings exceed this. The boundary between normal and large text is defined by WCAG at 18pt, resolving to 24px as a CSS logical pixel value. The minimum size registered in the Scale section closes this condition. Signal Blue on near-black and white is admissible at or above 24px cap height.

### Exclusions

The wordmark is not tinted, gradiated, or placed against a background that reduces its contrast below the applicable threshold for its rendered size. Colour decisions not recorded here are not permitted.

---

## Clear Space

Clear space is the minimum protected boundary around the wordmark. No element may enter this boundary.

The registered unit for clear space is the stroke width of the wordmark at its rendered size, applied equally on all four sides. The boundary protecting the mark is measured in the same unit that defines it. The relationship is derivable without reference to a separate value. At any given rendering size, the stroke width can be derived from the construction. The clear space value is self-contained.

---

## Scale

**Minimum size.** 24px cap height.

This value is a CSS logical pixel, device-independent across display densities. It is derived from two independent conditions that resolve to the same threshold.

The first is mathematical. Signal Blue on near-black and white does not reach the WCAG AA normal-text contrast ratio of 4.5:1. It passes at the large-text threshold of 3:1. WCAG defines the large-text boundary at 18pt, which resolves to 24px as a CSS logical pixel value. Below this point, Signal Blue is not admissible on near-black or white.

The second is optical. The truncated r, as the character with the least redundant geometry, is the performance indicator at small sizes. It reads correctly at this threshold.

Both conditions are satisfied at 24px cap height. The minimum is not a compromise between them. It is the point at which both hold.

The wordmark is not used below this size.

---

## Layout

**Orientation.** The wordmark is always horizontal. No rotation is permitted.

**Position.** The wordmark is placed top left on all surfaces where content is present.

This position is governed by what the wordmark does, not by convention. Krutho is not a brand assertion. It is a source identifier: the mark indicates that what follows is verifiable. A source identifier precedes the content it covers. Top left is the entry point on any left-to-right surface. The wordmark at the entry point is correct for this function. The position is derivable from the function, and the function excludes all other positions.

On surfaces where the wordmark is the sole content element, including loading states, standalone brand artifacts, and title slides where no body content is present, the source-identifier function has no content to precede. The wordmark is centered. This is the only condition under which top left does not apply.

---

## Governing Conditions

The following conditions summarise the assessable rules in this specification. Each can be applied by inspection to any output.

1. The wordmark is rendered only in near-black `#181818`, white `#FFFFFF`, or Signal Blue `#1A6FFF`.
2. The rendered colour achieves the contrast ratio required for its size against its background.
3. Signal Blue is used on near-black and white only at or above 24px cap height. Signal Blue on deep base `#000035` is admissible at all registered wordmark sizes.
4. Clear space on all four sides equals the stroke width of the wordmark at its rendered size.
5. The wordmark is always horizontal.
6. The wordmark is rendered from its registered construction without modification.
7. The wordmark is placed top left when content is present on the surface. It is centered when it is the sole content element.

---

## Colour Token Reference

This document references surface and brand context tokens defined in the Krutho Colour System. Those references are reproduced here so that this specification is independently verifiable without consulting another document. A change to the Krutho Colour System requires updating this section.

### Surface tokens

The wordmark is admitted on the following surfaces in light and dark modes. Values are the resolved hex of the named token.

| Token                  | Light mode | Dark mode |
|------------------------|------------|-----------|
| --color-surface-overlay | `#FFFFFF`  | `#343434` |
| --color-surface-raised  | `#FAFAFA`  | `#202020` |
| --color-surface-base    | `#F2F2F2`  | `#181818` |

### Deep base anchors

Structural deep base values used for diagram headers and dark narrative backgrounds. The wordmark in Signal Blue is admissible against deep-base-a at all registered sizes.

| Token                    | Hex     |
|--------------------------|---------|
| --primitive-deep-base-a  | `#000035` |
| --primitive-deep-base-b  | `#010364` |

### Layer reference

The Krutho Colour System defines three operating contexts as Layers. The wordmark Colour section references Layer 3 in connection with brand expression usage of Signal Blue.

| Layer | Name              | Function                                                              |
|-------|-------------------|-----------------------------------------------------------------------|
| 1     | Core Technology   | Product surfaces. Krutho itself.                                      |
| 2     | Enterprise Context | Krutho rendered within client environments.                          |
| 3     | Brand Expression  | Narrative, investor, and positioning contexts. Signal Blue admitted.  |

The Layer reference here is to the Krutho Colour System's defined term, not to the Krutho Typography System's Tier model.
