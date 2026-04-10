# Krutho Colour System

Last edit 10th April 2026

---

## Grounding Statement

This document operates under the Krutho Design Philosophy. The terms precision, correctness, verifiability, and truth are used throughout in the senses defined there. Every decision in this document traces to a reason that excludes the alternatives.

---

## Scope

This document covers five layers.

**Primitive scales.** The raw colour ramps from which all other values are derived. Primitive values are not used directly in components or diagrams. They are reference points for the semantic and diagram layers.

**Semantic tokens.** Named values that carry intent. Each semantic token references one primitive stop. Each token has one function. No token is used outside its defined function.

**Diagram tokens.** Named values for use in technical diagrams and data visualisations. Diagram tokens reference primitive stops. Diagram tokens are not used in UI components.

**System architecture.** The three-tier model that governs how colour operates across product, enterprise, and brand contexts.

**Governing principles.** The conditions that constrain colour application. These principles are specifications, not preferences. Conformance is assessable.

---

## System Architecture

The colour system operates across three distinct contexts. Each context has a defined relationship to colour. The three contexts are not modes of the same system — they are separate operating conditions with separate constraints.

```
Layer 1 — Core Technology    → Product truth. Krutho itself.
Layer 2 — Enterprise Context → Client environment. Krutho within Delta,
                                Aldar, and equivalent deployments.
Layer 3 — Brand Expression   → Narrative, investor, and positioning
                                contexts where client environment is absent.
```

**Layer 1 — Core Technology.** The neutral system is always present. Colour is applied only as state, action, or system response. The product must function clearly and completely without reliance on colour. Colour failure must not produce a failure of function or comprehension.

**Layer 2 — Enterprise Context.** Krutho is visualised within the client's world. Client colour systems may be introduced. Krutho does not override — it integrates. The structural layer (surface hierarchy, text hierarchy, component behaviour) is fixed. The colour expression adapts to the client context. Krutho remains structurally consistent and visually coherent within the enterprise environment.

This principle reinforces trust, compatibility, and adoption readiness. A system that imposes its own visual language into a client environment signals that it has not been designed to coexist. Krutho is designed to coexist.

**Layer 3 — Brand Expression.** Controlled use of Krutho brand colours. More expressive than product contexts but still restrained. Brand expression is strongest where client context is absent — investor presentations, narrative documents, and brand communications. Brand colours at this layer operate at higher density than in product or enterprise contexts, but the governing principles still apply.

**The constant across all three layers.** Structure is fixed. Colour is contextual. Meaning is consistent.

---

## Governing Principles

These principles constrain how colour is applied across all three layers. Each is stated as a condition. Conformance is assessable. A practitioner can inspect any output and determine whether it conforms.

**Principle 1 — Neutral first.** Every design must function completely in neutral before colour is applied. Colour is added to a working neutral system. It is not used to construct function that neutral cannot provide. A component, diagram, or layout that requires colour to be understood has failed this condition before colour was considered.

**Principle 2 — Colour asserts, not decorates.** Colour is applied in three conditions only: to signal state, to signal action, and to signal system response. Colour applied for visual variety, background styling, or spatial decoration is a conformance failure. An element that carries colour must carry a reason for that colour that traces to one of the three conditions.

**Principle 3 — Single colour dominance.** Exactly one brand colour is dominant in any given context, component, or view. Dominance is defined under Perceptual Weight: a brand colour is dominant when its chromatic area exceeds twice the chromatic area of any other brand colour in the same context. Where two or more brand colours occupy comparable chromatic area, no colour is dominant and this principle fails. Multiple brand colours in simultaneous use do not compound meaning: they cancel it. The presence of a second brand colour at or above half the dominant colour's chromatic area is a conformance failure unless the second colour is a semantic state token (error, success, warning, info), in which case it is not a brand colour occurrence but a system response.

**Principle 4 — Colour independence.** Each colour in the system is complete and independent. Colours are not positioned relative to adjacent colours. They do not form gradients as a base brand expression. A colour that requires adjacent colour to produce its intended effect has failed this condition.

Gradients are not a base brand expression. They are permitted in one defined exception: a single linear gradient between two stops of the same primitive ramp, used in illustrative diagrams to represent a continuous physical property (temperature, pressure, concentration). This exception is scoped to the diagram layer. Gradients do not appear in UI components.

**Principle 5 — No luminous effects.** Colour is embedded in the surface. It does not project from it. Glow, neon, bloom, and light-emitting treatments are not permitted. These effects perform a property (energy, dynamism, modernity) that is not present in the construction. The philosophy excludes elements that perform properties they do not have.

**Principle 6 — Mode-invariant brand colours.** Brand colours are identical in light and dark modes. A brand colour does not have a light-mode version and a dark-mode version. Alternate versions of brand colours imply that the colours are contextual rather than assertive, which contradicts their defined role. The surface context changes — ink on light, embedded in dark — but the colour value is constant.

Semantic feedback colours (error, success, warning, info) are an exception: their dark mode values are defined to maintain contrast on dark surfaces. This exception is functional, not expressive. It is documented in the semantic source layer.

**Principle 7 — Usage ratios.** Across any Layer 1 or Layer 2 surface, the neutral system accounts for 85–95% of the surface by perceptual weight. Brand and semantic colour accounts for 5–15%. Perceptual weight is defined and computed in the Perceptual Weight section. This ratio is a verifiable constraint: an inspector can classify each rendered element by OKLCH chroma and measure fractional area without judgment. A Layer 1 or Layer 2 layout that inverts this ratio, where chromatic content is the ground and neutral is the figure, has failed the neutral-first principle at the compositional level.

Layer 3 (brand expression) is not bounded by a numeric ratio. It remains bound by the neutral-first principle (Principle 1): the surface must function completely without colour before colour is applied.

**Principle 8 — System character.** The following properties are present in the construction of every element. They are not performed.

- Control: every colour decision is bounded and traceable
- Precision: every value is defined without ambiguity
- Authority: colour appears when something warrants it, not when space permits
- Restraint: the system withholds colour as its default position
- Clarity: colour increases legibility; it does not compete with it

---

## Notation

A value expressed as `ramp · stop` refers to a specific stop on a named primitive scale. `signal-blue · 500` refers to the 500 stop of the --primitive-signal-blue scale. The resolved hex value is defined in the primitive scale table for that ramp.

The notation `semantic · [state]` refers to a semantic source token. The source token carries its own light and dark values. Tokens that reference a source token inherit the correct value for the current mode without restating it.

`neutral · 0` refers to #FFFFFF. This stop is outside the standard 50–950 range and is defined explicitly in the neutral scale table.

---

## Perceptual Weight

Several governing principles in this document constrain the relationship between neutral and chromatic content on a surface. Those constraints depend on a measurement method. This section defines the method so that conformance can be assessed by inspection rather than judgment.

**Definition.** Perceptual weight is the visual prominence of a rendered element, assessed by classifying the element as neutral or chromatic and measuring its fractional surface area.

**Classification rule.** Each rendered element is classified by the OKLCH chroma value of its primary fill or text colour.

- An element with OKLCH chroma below 0.02 is **neutral**.
- An element with OKLCH chroma at or above 0.02 is **chromatic**.

The 0.02 threshold is the point at which OKLCH chroma becomes visually distinguishable from achromatic neutral on typical sRGB displays. Below this value, an element reads as neutral regardless of its underlying hue.

**Surface measurement.** The neutral and chromatic weights of a surface are computed as fractions of total rendered area:

```
neutral weight   = total area of neutral elements / total rendered area
chromatic weight = total area of chromatic elements / total rendered area
```

The two weights sum to 1. They are expressed as percentages where the governing principles require ratios.

**Dominance.** A brand colour is **dominant** in a context when its chromatic area exceeds twice the chromatic area of any other brand colour in the same context. Where two or more brand colours occupy comparable chromatic area (where no colour exceeds another by a factor of 2 or more), no colour is dominant and any principle requiring single dominance fails.

The 2× factor is the smallest multiple at which area difference is reliably detectable by inspection without measurement instruments. A 1.5× difference reads as approximately equal at typical viewing distances. A 2× difference reads as one element clearly exceeding the other. The factor is the threshold at which dominance is assessable by eye.

Semantic state colours (error, success, warning, info) are excluded from dominance assessment. They are system responses, not brand colour occurrences.

---

## Primitive Scales

Primitive scales are sequential ramps from lightest to darkest. Lower stop numbers are lighter. Higher stop numbers are darker. The standard range is 50 to 950. Stops outside this range are defined explicitly, and the basis for each is documented.

The primitive layer is the only layer where raw hex values are specified. No other layer contains raw hex values, with the exception of dark feedback surfaces, which are derived by formula from primitive values. The formula is specified under Dark Feedback Surface Derivation in the Semantic Layer section.

---

### --primitive-neutral

Pure achromatic scale. No warm or cool undertone. Powers all surface, text, border, and icon tokens in both light and dark modes.

| Stop | Hex     | Key references                                                    |
|------|---------|-------------------------------------------------------------------|
| 0    | #FFFFFF | surface-overlay light, text-on-accent, action-primary-text        |
| 50   | #FAFAFA | surface-raised light, text-strong dark                            |
| 100  | #F2F2F2 | surface-base light, text-default dark                             |
| 200  | #E6E6E6 | surface-sunken light, border-subtle light                         |
| 300  | #D6D6D6 | border-default light                                              |
| 400  | #C4C4C4 | text-disabled light                                               |
| 450  | #AFAFAF | text-placeholder light                                            |
| 500  | #9A9A9A | text-faint light, border-strong dark, text-subtle dark            |
| 600  | #707070 | text-subtle light, border-strong light                            |
| 700  | #505050 | text-disabled dark, action-disabled-text dark                     |
| 800  | #343434 | text-default light, border-default dark, surface-overlay dark     |
| 825  | #2A2A2A | border-subtle dark, action-secondary-active dark                  |
| 850  | #202020 | surface-raised dark, action-secondary-hover dark                  |
| 900  | #181818 | text-strong light, surface-base dark, surface-inverse light       |
| 950  | #0A0A0A | surface-sunken dark                                               |

Stops 0, 450, 825, and 850 fall outside the standard range. Each is defined by a specific token requirement with no equivalent at adjacent stops. The basis for each is documented in Decision Record DR-001.

---

### --primitive-signal-blue

Primary brand signal. Anchored at 500. Powers action-primary, text-link, border-focus, diagram signal tokens, and the sequential diagram scale.

| Stop | Hex     | Key references                                                         |
|------|---------|------------------------------------------------------------------------|
| 50   | #EBF3FF | surface-info light, diagram-signal-trust-fill light                    |
| 100  | #C5DBFF |                                                                        |
| 200  | #94BBFF | text-link dark, diagram-seq-2                                          |
| 300  | #5C9AFF | action-primary-active dark, semantic-info dark                         |
| 400  | #3D85FF | action-primary-hover dark, diagram-seq-3                               |
| 500  | #1A6FFF | action-primary, border-focus, text-link light, semantic-info light     |
| 600  | #0055DD | action-primary-hover light                                             |
| 700  | #0044BB | action-primary-active light, diagram-seq-5                             |
| 800  | #003399 | diagram-signal-trust-text light                                        |
| 900  | #001F6B | diagram-signal-trust-fill dark                                         |
| 950  | #000E40 |                                                                        |

Brand anchor: 500 = #1A6FFF (Primary Signal).

---

### --primitive-secondary-signal

Secondary brand colour. Anchored at 500. Powers diagram categorical integration tokens.

| Stop | Hex     |
|------|---------|
| 50   | #EEEEFF |
| 100  | #D0D2F8 |
| 200  | #B0B3F0 |
| 300  | #9092E8 |
| 400  | #7476DC |
| 500  | #5C60D6 |
| 600  | #4448BF |
| 700  | #3234A8 |
| 800  | #20228A |
| 900  | #10126A |
| 950  | #06084A |

Brand anchor: 500 = #5C60D6 (Secondary Signal).

---

### --primitive-teal

Derived from brand Accent (#004964). Anchored at 700. Mid-tone stops are constructed above the anchor to provide usable fills for diagram categorical transport tokens. Anchoring at 700 rather than 500 is documented in Decision Record DR-003.

| Stop | Hex     |
|------|---------|
| 50   | #E0F4FA |
| 100  | #B0E0EF |
| 200  | #7DCAE3 |
| 300  | #40B0D4 |
| 400  | #1A96BE |
| 500  | #0A7CA4 |
| 600  | #086688 |
| 700  | #004964 |
| 800  | #003550 |
| 900  | #00203A |
| 950  | #000E22 |

Brand anchor: 700 = #004964 (Accent).

---

### --primitive-amber

Net-new ramp. Not present in the existing brand palette. Required for diagram categorical state tokens and the negative pole of the diverging scale. Admission is documented in Decision Record DR-004. The amber ramp does not appear in any surface, text, border, icon, action, or feedback token. Its scope is restricted to the diagram layer.

| Stop | Hex     |
|------|---------|
| 50   | #FFF5E6 |
| 100  | #FFDFB0 |
| 200  | #F5C478 |
| 300  | #E8A840 |
| 400  | #D68E22 |
| 500  | #C47B1A |
| 600  | #A86210 |
| 700  | #8A4C08 |
| 800  | #6C3804 |
| 900  | #4E2602 |
| 950  | #301600 |

Conceptual anchor: 500 = #C47B1A. Warm gold. Distinct in hue from the brownish-amber of the warning ramp (#92400E at warning-700).

---

### --primitive-deep-base

Fixed structural anchors. Not a ramp. Not stops on any scale. Used exclusively for diagram headers, swimlane bars, and label tabs. Exclusion from the signal-blue ramp is documented in Decision Record DR-003.

| Name                    | Hex     | Function                                                    |
|-------------------------|---------|-------------------------------------------------------------|
| --primitive-deep-base-a | #000035 | Near-black with blue undertone. Dark narrative backgrounds. |
| --primitive-deep-base-b | #010364 | Deep navy. All diagram headers, swimlane bars, label tabs.  |

These values have no neighbours on any scale. They do not participate in hover, active, or tonal relationships.

---

### --primitive-error

| Stop | Hex     | Key references                                      |
|------|---------|-----------------------------------------------------|
| 50   | #FEF2F2 | feedback-error-surface light                        |
| 100  | #FFCFCF |                                                     |
| 200  | #FFAAAA | semantic-error dark                                 |
| 300  | #FF7A7A |                                                     |
| 400  | #F04848 |                                                     |
| 500  | #E02828 |                                                     |
| 600  | #C0251D | semantic-error light, action-destructive resting    |
| 700  | #9B1C1C | action-destructive-hover light                      |
| 800  | #7B1414 | action-destructive-active light                     |
| 900  | #5A0C0C |                                                     |
| 950  | #380606 |                                                     |

Semantic anchor: 600 = #C0251D.

---

### --primitive-success

| Stop | Hex     | Key references          |
|------|---------|-------------------------|
| 50   | #F0FDF4 | feedback-success-surface light |
| 100  | #CBFADE |                         |
| 200  | #9AEEC0 | semantic-success dark   |
| 300  | #5EDE9A |                         |
| 400  | #30C478 |                         |
| 500  | #18A85A |                         |
| 600  | #128C46 |                         |
| 700  | #166534 | semantic-success light  |
| 800  | #0F4826 |                         |
| 900  | #083018 |                         |
| 950  | #03160C |                         |

Semantic anchor: 700 = #166534.

---

### --primitive-warning

| Stop | Hex     | Key references          |
|------|---------|-------------------------|
| 50   | #FFFBEB | feedback-warning-surface light |
| 100  | #FDEFC8 |                         |
| 200  | #FAD88E |                         |
| 300  | #F5BC50 | semantic-warning dark   |
| 400  | #E89A20 |                         |
| 500  | #CC7A0A |                         |
| 600  | #AA5E08 |                         |
| 700  | #92400E | semantic-warning light  |
| 800  | #7A2E08 |                         |
| 900  | #5A1E04 |                         |
| 950  | #3A1002 |                         |

Semantic anchor: 700 = #92400E. Brownish-amber. Distinct in both hue and function from the amber ramp used for diagram categorical state tokens.

---

## Semantic Layer

### Source Tokens

Source tokens define the single resolved value for each feedback state. All semantic text, border, icon, and feedback tokens reference these values using var() rather than restating primitive references. Light and dark mode resolution is handled at this layer. Downstream tokens inherit automatically.

To update how an error state appears throughout the system, update this layer only.

| Token                    | Description                                   | Light               | Dark                  |
|--------------------------|-----------------------------------------------|---------------------|-----------------------|
| --color-semantic-error   | Core error colour. Source for all error states.   | error · 600         | error · 200           |
| --color-semantic-success | Core success colour. Source for all success states. | success · 700     | success · 200         |
| --color-semantic-warning | Core warning colour. Source for all cautionary states. | warning · 700  | warning · 300         |
| --color-semantic-info    | Core informational colour. Source for all info states. | signal-blue · 500 | signal-blue · 300 |

Info uses the signal-blue ramp directly. No separate info primitive ramp is required.

---

### Dark Feedback Surface Derivation

Dark feedback surfaces are derived by compositing the semantic source stop over neutral-900 at 12% opacity.

```
dark-surface = neutral-900 + semantic-source-stop at 12% opacity
```

RGB calculation: each channel = round(base + (source − base) × 0.12) where base = neutral-900 = rgb(24, 24, 24)

| Token                         | Source stop              | Source RGB          | Derived dark value |
|-------------------------------|--------------------------|---------------------|--------------------|
| --color-surface-error dark    | error · 600 (#C0251D)    | rgb(192, 37, 29)    | #2C1A19            |
| --color-surface-warning dark  | warning · 700 (#92400E)  | rgb(146, 64, 14)    | #271D17            |
| --color-surface-success dark  | success · 700 (#166534)  | rgb(22, 101, 52)    | #18211B            |
| --color-surface-info dark     | signal-blue · 500 (#1A6FFF) | rgb(26, 111, 255) | #182234           |

The same formula and derived values apply to the corresponding --color-feedback-[state]-surface dark tokens.

These values are reproducible by any party from the defined primitives and formula. The basis for the 12% figure is documented in Decision Record DR-002.

---

### Surface

| Token                    | Description                                                              | Light             | Dark        |
|--------------------------|--------------------------------------------------------------------------|-------------------|-------------|
| --color-surface-overlay  | Modals, drawers, dialogs — sits above all other surfaces                 | neutral · 0       | neutral · 800 |
| --color-surface-raised   | Cards, panels, dropdowns, tooltips                                       | neutral · 50      | neutral · 850 |
| --color-surface-base     | Default page background — the primary content canvas                     | neutral · 100     | neutral · 900 |
| --color-surface-sunken   | Input fills, code blocks, inset areas — recedes below base               | neutral · 200     | neutral · 950 |
| --color-surface-inverse  | Dark chips, inverted banners, tooltips on dark backgrounds               | neutral · 900     | neutral · 200 |
| --color-surface-error    | Background fill for error alerts, banners, and validation areas          | error · 50        | derived     |
| --color-surface-warning  | Background fill for warning alerts and cautionary notices                | warning · 50      | derived     |
| --color-surface-success  | Background fill for success confirmations and positive states            | success · 50      | derived     |
| --color-surface-info     | Background fill for informational notices and highlighted content        | signal-blue · 50  | derived     |

"Derived" indicates the dark feedback surface formula applies.

---

### Text

#### Hierarchy

| Token               | Description                                                        | Light         | Dark          |
|---------------------|--------------------------------------------------------------------|---------------|---------------|
| --color-text-strong  | Maximum contrast — headings, UI labels, data values requiring emphasis | neutral · 900 | neutral · 50  |
| --color-text-default | Body copy, standard reading weight                                 | neutral · 800 | neutral · 200 |
| --color-text-subtle  | Supporting copy, secondary labels, captions, helper text           | neutral · 600 | neutral · 500 |
| --color-text-faint   | Metadata, timestamps, character counts, lowest-priority annotations | neutral · 500 | neutral · 600 |

#### Functional states

| Token                    | Description                                              | Light         | Dark          |
|--------------------------|----------------------------------------------------------|---------------|---------------|
| --color-text-disabled    | Labels on inactive controls, disabled fields and buttons | neutral · 400 | neutral · 700 |
| --color-text-placeholder | Placeholder text inside empty input fields               | neutral · 450 | neutral · 700 |

#### Inverse

| Token                  | Description                                                          | Light         | Dark          |
|------------------------|----------------------------------------------------------------------|---------------|---------------|
| --color-text-inverse   | Text rendered on surface-inverse                                     | neutral · 100 | neutral · 900 |
| --color-text-on-accent | Text rendered on brand or action-coloured fills — always white       | neutral · 0   | neutral · 0   |

#### Semantic

Values reference the semantic source layer. Light and dark resolution is handled upstream. Do not replace these references with primitive values.

| Token                | Description                                          | Value                                       |
|----------------------|------------------------------------------------------|---------------------------------------------|
| --color-text-link    | Hyperlinks and inline text actions                   | signal-blue · 500 / signal-blue · 300       |
| --color-text-error   | Validation error messages, destructive state copy    | semantic · error                            |
| --color-text-success | Confirmation messages, positive state copy           | semantic · success                          |
| --color-text-warning | Cautionary messages, non-blocking alert copy         | semantic · warning                          |
| --color-text-info    | Informational copy, neutral system messages          | semantic · info                             |

---

### Border

#### Weight scale

| Token                  | Description                                                          | Light         | Dark          |
|------------------------|----------------------------------------------------------------------|---------------|---------------|
| --color-border-strong  | High-emphasis dividers, selected state outlines, active edges        | neutral · 600 | neutral · 500 |
| --color-border-default | Standard component borders — inputs, cards, panels                   | neutral · 300 | neutral · 800 |
| --color-border-subtle  | Hairlines, table rules, section dividers, low-priority separators    | neutral · 200 | neutral · 825 |

#### Functional

| Token                  | Description                                                          | Light                | Dark                 |
|------------------------|----------------------------------------------------------------------|----------------------|----------------------|
| --color-border-focus   | Keyboard focus ring — always 2px, identical in both modes            | signal-blue · 500    | signal-blue · 500    |
| --color-border-inverse | Borders rendered on surface-inverse                                  | neutral · 800        | neutral · 300        |

#### Semantic

Values reference the semantic source layer.

| Token                  | Description                                              | Value              |
|------------------------|----------------------------------------------------------|--------------------|
| --color-border-error   | Outline on invalid inputs and error state components     | semantic · error   |
| --color-border-success | Outline on valid inputs and confirmed state components   | semantic · success |
| --color-border-warning | Outline on cautionary state components                   | semantic · warning |
| --color-border-info    | Outline on informational components and highlighted areas | semantic · info   |

---

### Icon

Icon tokens mirror the text hierarchy directly. An icon paired with a text token uses the corresponding icon token. icon-strong pairs with text-strong. icon-subtle pairs with text-subtle.

#### Hierarchy

| Token               | Description                                                        | Light         | Dark          |
|---------------------|--------------------------------------------------------------------|---------------|---------------|
| --color-icon-strong  | High-emphasis icons — primary actions, active states               | neutral · 900 | neutral · 50  |
| --color-icon-default | Standard icon colour for most UI contexts                          | neutral · 800 | neutral · 200 |
| --color-icon-subtle  | Supporting icons, decorative indicators                            | neutral · 600 | neutral · 500 |
| --color-icon-faint   | Low-priority icons, metadata-level indicators                      | neutral · 500 | neutral · 600 |

#### Functional states

| Token                | Description                                              | Light         | Dark          |
|----------------------|----------------------------------------------------------|---------------|---------------|
| --color-icon-disabled | Icons on inactive controls and disabled components      | neutral · 400 | neutral · 700 |

#### Inverse

| Token                  | Description                                              | Light         | Dark          |
|------------------------|----------------------------------------------------------|---------------|---------------|
| --color-icon-inverse   | Icons rendered on surface-inverse                        | neutral · 100 | neutral · 900 |
| --color-icon-on-accent | Icons rendered on brand or action-coloured fills         | neutral · 0   | neutral · 0   |

#### Semantic

Values reference the semantic source layer.

| Token                | Description                                              | Value              |
|----------------------|----------------------------------------------------------|--------------------|
| --color-icon-link    | Icons accompanying hyperlinks or inline actions          | signal-blue · 500 / signal-blue · 300 |
| --color-icon-error   | Icons in error states and destructive alerts             | semantic · error   |
| --color-icon-success | Icons in success confirmations and positive states       | semantic · success |
| --color-icon-warning | Icons in warning alerts and cautionary states            | semantic · warning |
| --color-icon-info    | Icons in informational components and system notices     | semantic · info    |

---

### Action

#### Primary (filled)

| Token                        | Description                             | Light              | Dark               |
|------------------------------|-----------------------------------------|--------------------|--------------------|
| --color-action-primary       | Resting fill for primary CTA buttons    | signal-blue · 500  | signal-blue · 500  |
| --color-action-primary-hover | Fill on hover                           | signal-blue · 600  | signal-blue · 400  |
| --color-action-primary-active | Fill on press                          | signal-blue · 700  | signal-blue · 300  |
| --color-action-primary-text  | Label colour — always white             | neutral · 0        | neutral · 0        |

#### Secondary (outlined)

| Token                                | Description                               | Light         | Dark          |
|--------------------------------------|-------------------------------------------|---------------|---------------|
| --color-action-secondary             | Resting fill — transparent                | transparent   | transparent   |
| --color-action-secondary-hover       | Fill on hover                             | neutral · 100 | neutral · 850 |
| --color-action-secondary-active      | Fill on press                             | neutral · 200 | neutral · 825 |
| --color-action-secondary-border      | Resting border                            | neutral · 300 | neutral · 800 |
| --color-action-secondary-border-hover | Border on hover                          | neutral · 500 | neutral · 500 |
| --color-action-secondary-border-active | Border on press — maximum contrast     | neutral · 800 | neutral · 200 |
| --color-action-secondary-text        | Label colour                              | neutral · 900 | neutral · 200 |

#### Ghost

| Token                       | Description                               | Light         | Dark          |
|-----------------------------|-------------------------------------------|---------------|---------------|
| --color-action-ghost        | Resting fill — transparent, no border     | transparent   | transparent   |
| --color-action-ghost-hover  | Fill on hover                             | neutral · 100 | neutral · 850 |
| --color-action-ghost-active | Fill on press                             | neutral · 200 | neutral · 825 |
| --color-action-ghost-text   | Label and icon colour                     | neutral · 900 | neutral · 200 |

#### Destructive

| Token                              | Description                                    | Light        | Dark         |
|------------------------------------|------------------------------------------------|--------------|--------------|
| --color-action-destructive         | Resting fill for irreversible actions          | error · 600  | error · 600  |
| --color-action-destructive-hover   | Fill on hover                                  | error · 700  | error · 400  |
| --color-action-destructive-active  | Fill on press                                  | error · 800  | error · 200  |
| --color-action-destructive-text    | Label colour — always white                    | neutral · 0  | neutral · 0  |

#### Disabled

| Token                       | Description                                    | Light         | Dark          |
|-----------------------------|------------------------------------------------|---------------|---------------|
| --color-action-disabled     | Fill for any disabled button variant           | neutral · 200 | neutral · 825 |
| --color-action-disabled-text | Label colour on any disabled button           | neutral · 500 | neutral · 700 |

---

### Feedback

Surfaces use the derivation formula for dark values. Text, border, and icon tokens reference the semantic source layer. Mode resolution is handled at the source layer. The "—" in the Dark column denotes that the token references a source token which carries its own dark value.

#### Error

| Token                          | Description                                                    | Light          | Dark    |
|--------------------------------|----------------------------------------------------------------|----------------|---------|
| --color-feedback-error-surface | Background fill for error alert and banner components          | error · 50     | derived |
| --color-feedback-error-text    | Message text inside error alerts                               | semantic · error | —     |
| --color-feedback-error-border  | Border on error alert components                               | semantic · error | —     |
| --color-feedback-error-icon    | Icon colour inside error alerts                                | semantic · error | —     |

#### Warning

| Token                            | Description                                                    | Light            | Dark    |
|----------------------------------|----------------------------------------------------------------|------------------|---------|
| --color-feedback-warning-surface | Background fill for warning alert and banner components        | warning · 50     | derived |
| --color-feedback-warning-text    | Message text inside warning alerts                             | semantic · warning | —    |
| --color-feedback-warning-border  | Border on warning alert components                             | semantic · warning | —    |
| --color-feedback-warning-icon    | Icon colour inside warning alerts                              | semantic · warning | —    |

#### Success

| Token                            | Description                                                    | Light            | Dark    |
|----------------------------------|----------------------------------------------------------------|------------------|---------|
| --color-feedback-success-surface | Background fill for success alert and confirmation components  | success · 50     | derived |
| --color-feedback-success-text    | Message text inside success alerts                             | semantic · success | —    |
| --color-feedback-success-border  | Border on success alert components                             | semantic · success | —    |
| --color-feedback-success-icon    | Icon colour inside success alerts                              | semantic · success | —    |

#### Info

| Token                          | Description                                                    | Light              | Dark    |
|--------------------------------|----------------------------------------------------------------|--------------------|---------|
| --color-feedback-info-surface  | Background fill for informational alert and notice components  | signal-blue · 50   | derived |
| --color-feedback-info-text     | Message text inside info alerts                                | semantic · info    | —       |
| --color-feedback-info-border   | Border on info alert components                                | semantic · info    | —       |
| --color-feedback-info-icon     | Icon colour inside info alerts                                 | semantic · info    | —       |

---

## Diagram Colour System

The same chain applies to diagrams as to the semantic layer: every value traces to a primitive, every token has one function, and every decision records its reason.

Diagram tokens are not used in UI components. Semantic tokens are not used in diagrams unless the diagram type is status or threshold data, in which case the semantic mode applies directly. The two layers do not cross.

---

### Colour Modes

Every diagram operates in one or more of five colour modes. The mode is determined by the type of information being communicated. Diagram type is not a colour specification. Colour mode is.

| Mode        | Question the colour answers              | Typical diagram types                                        |
|-------------|------------------------------------------|--------------------------------------------------------------|
| Signal      | What matters in this diagram?            | Process flows, swimlanes, architectural diagrams             |
| Categorical | Which group is this?                     | Architecture, network graphs, categorical data charts        |
| Sequential  | How much, or how far?                    | Heatmaps, timelines, density charts, volume series           |
| Diverging   | Which direction from the centre?         | Delta charts, valid/expired distributions, before/after      |
| Semantic    | What does the system judge this to be?   | Status dashboards, compliance matrices, threshold alerts     |

A diagram that cannot be assigned to any defined mode requires a specification addition before colour is applied. Using an existing mode for an unspecified purpose is a conformance failure.

---

### Signal Mode

Signal mode is used when a diagram is primarily neutral and colour marks only those moments that carry distinct meaning within that neutrality. The majority of nodes remain neutral. Signal is withheld until a signal condition is met.

Two signal conditions are defined.

**Trust layer active.** A component, node, or step in which cryptographic verification, identity assertion, or trust chain operations are occurring. Filled with signal-blue · 50. Bordered with signal-blue · 500. Text in signal-blue · 800.

**Human decision in motion.** A step at which a person must act. No fill colour is applied — white fill, strong neutral border. The border weight distinguishes the node from infrastructure. No blue fill is used because the human is not the trust layer.

Signal mode does not extend to connectors unless the connection itself represents a trust handoff. A connector between two trust-layer nodes is not itself a trust event. The connector-trust token is used only when the connection is the handoff, not merely adjacent to one.

#### Signal mode tokens

| Token                               | Description                              | Light              | Dark               |
|-------------------------------------|------------------------------------------|--------------------|--------------------|
| --color-diagram-signal-trust-fill   | Trust layer node or container fill       | signal-blue · 50   | signal-blue · 900  |
| --color-diagram-signal-trust-border | Trust layer node or container border     | signal-blue · 500  | signal-blue · 500  |
| --color-diagram-signal-trust-text   | Text on trust layer fill                 | signal-blue · 800  | signal-blue · 200  |
| --color-diagram-signal-human-border | Human action node border                 | neutral · 900      | neutral · 50       |

---

### Categorical Mode

Categorical mode is used when distinct domains, systems, or entity types require simultaneous visual separation. All members of the same category receive the same colour treatment. Categories carry no hierarchy. No category is more important than another by virtue of its colour.

Maximum four categories. A fifth category is rendered neutral and its role is documented in the diagram key. The specification does not define a fifth categorical colour. A diagram requiring more than four colour-separated categories requires structural redesign before it requires a fifth colour.

Each categorical token is defined by a function, not an ordinal position. The basis for role-defined names is documented in Decision Record DR-005.

#### Category definitions

**Trust (signal-blue family)** Applied to components, systems, or processes that perform or rely on cryptographic verification, identity assertion, or trust chain operations. The defining criterion: correct behaviour depends on cryptographic proof rather than assumed permission.

**Integration (secondary-signal family)** Applied to partner systems, external services, and third-party components that communicate with the trust layer through defined interfaces. Connected to the trust chain but external to it. Does not itself perform verification.

**Transport (teal family)** Applied to network infrastructure, connectivity layers, routing, and data-in-motion systems. The defining criterion: the component's primary function is movement of data, not computation or storage of it.

**State (amber family)** Applied to storage systems, credential stores, databases, and data-at-rest. The defining criterion: the component's primary function is persistence of data, not movement or transformation of it.

Where an entity satisfies more than one definition, assign by primary function. Where an entity satisfies none, render it neutral and annotate.

#### Relationship to signal tokens

The trust categorical tokens and the signal trust tokens reference the same primitive stops. Their distinction is scope. Signal tokens mark specific nodes in a predominantly neutral diagram. Categorical tokens mark all entities of a domain in a diagram where multiple domains require simultaneous colour distinction. A node correctly marked with diagram-signal-trust is also correctly categorised as diagram-cat-trust when the diagram operates in categorical mode.

#### Categorical tokens

| Token                                | Light                   | Dark                      |
|--------------------------------------|-------------------------|---------------------------|
| --color-diagram-cat-trust-fill       | signal-blue · 50        | signal-blue · 900         |
| --color-diagram-cat-trust-border     | signal-blue · 500       | signal-blue · 500         |
| --color-diagram-cat-trust-text       | signal-blue · 800       | signal-blue · 200         |
| --color-diagram-cat-integration-fill | secondary-signal · 50   | secondary-signal · 900    |
| --color-diagram-cat-integration-border | secondary-signal · 500 | secondary-signal · 500   |
| --color-diagram-cat-integration-text | secondary-signal · 800  | secondary-signal · 200    |
| --color-diagram-cat-transport-fill   | teal · 50               | teal · 900                |
| --color-diagram-cat-transport-border | teal · 500              | teal · 500                |
| --color-diagram-cat-transport-text   | teal · 800              | teal · 200                |
| --color-diagram-cat-state-fill       | amber · 50              | amber · 900               |
| --color-diagram-cat-state-border     | amber · 500             | amber · 500               |
| --color-diagram-cat-state-text       | amber · 800             | amber · 200               |

---

### Sequential Mode

Sequential mode is used for ordered data with a single direction. The colour encodes position in the sequence. Signal-blue is the default sequential ramp. A second sequential variable in the same diagram uses the teal ramp.

Five stops are defined for standard use. These are the stops at which perceptual differentiation is reliable at typical diagram and chart dimensions. The full primitive ramp is available for precise mapping where finer gradation is required.

| Token                      | Primitive reference  | Position                    |
|----------------------------|----------------------|-----------------------------|
| --color-diagram-seq-1      | signal-blue · 50     | Lowest / earliest / weakest |
| --color-diagram-seq-2      | signal-blue · 200    |                             |
| --color-diagram-seq-3      | signal-blue · 400    | Mid                         |
| --color-diagram-seq-4      | signal-blue · 500    |                             |
| --color-diagram-seq-5      | signal-blue · 700    | Highest / latest / strongest |
| --color-diagram-seq-alt-1  | teal · 50            | Alternate ramp — lowest     |
| --color-diagram-seq-alt-2  | teal · 200           |                             |
| --color-diagram-seq-alt-3  | teal · 400           | Alternate ramp — mid        |
| --color-diagram-seq-alt-4  | teal · 500           |                             |
| --color-diagram-seq-alt-5  | teal · 700           | Alternate ramp — highest    |

---

### Diverging Mode

Diverging mode is used for data with a meaningful centre point. Two hues extend outward from a neutral midpoint with equal visual weight. The centre represents zero, baseline, threshold, or balance.

For Krutho data: the positive pole (valid, trusted, above threshold) uses signal-blue. The negative pole (expired, revoked, below threshold) uses amber. The midpoint is neutral.

| Token                               | Primitive reference   | Position        |
|-------------------------------------|-----------------------|-----------------|
| --color-diagram-div-negative-strong | amber · 600           | Strong negative |
| --color-diagram-div-negative-subtle | amber · 200           | Subtle negative |
| --color-diagram-div-midpoint        | neutral · 300         | Centre          |
| --color-diagram-div-positive-subtle | signal-blue · 200     | Subtle positive |
| --color-diagram-div-positive-strong | signal-blue · 600     | Strong positive |

---

### Semantic Mode

Semantic mode uses the existing semantic source tokens directly. No diagram-specific tokens are introduced for this mode.

Status conditions map as follows.

| Condition                    | Token family       |
|------------------------------|--------------------|
| Valid / confirmed            | semantic · success |
| Invalid / failed             | semantic · error   |
| Expired / expiring / caution | semantic · warning |
| Informational / pending      | semantic · info    |

---

### Structural Tokens

Structural tokens apply to all diagram types regardless of mode. They govern headers, default nodes, annotations, connectors, and boundaries.

| Token                                 | Description                                                                                    | Light              | Dark               |
|---------------------------------------|------------------------------------------------------------------------------------------------|--------------------|--------------------|
| --color-diagram-header-bg             | Swimlane headers, container label tabs                                                         | deep-base-b        | deep-base-b        |
| --color-diagram-header-text           | Text on diagram headers                                                                        | neutral · 0        | neutral · 0        |
| --color-diagram-node-fill             | Default node fill                                                                              | neutral · 0        | neutral · 850      |
| --color-diagram-node-border           | Default node border                                                                            | neutral · 500      | neutral · 600      |
| --color-diagram-node-text             | Default node text                                                                              | neutral · 900      | neutral · 200      |
| --color-diagram-node-decision-border  | Decision / branch node — dashed, same colour as node border                                    | neutral · 500      | neutral · 600      |
| --color-diagram-annotation-fill       | Callout annotation background                                                                  | neutral · 200      | neutral · 825      |
| --color-diagram-annotation-text       | Callout annotation text                                                                        | neutral · 700      | neutral · 400      |
| --color-diagram-connector             | Standard connector line                                                                        | neutral · 500      | neutral · 600      |
| --color-diagram-connector-trust       | Trust handoff connector — used only when the connection is the handoff, not when adjacent to one | signal-blue · 500 | signal-blue · 500 |
| --color-diagram-connector-optional    | Non-critical or opportunistic path — fine dash                                                 | neutral · 400      | neutral · 600      |
| --color-diagram-boundary-physical     | Physical environment perimeter — coarse dash                                                   | neutral · 600      | neutral · 500      |
| --color-diagram-boundary-logical      | Logical grouping boundary — fine dash                                                          | neutral · 400      | neutral · 600      |
| --color-diagram-lane-divider          | Swimlane separator                                                                             | neutral · 200      | neutral · 825      |

---

## Decision Records

Decision records document the reasoning that excludes alternatives. They are part of the specification. A decision recorded here is not subject to re-evaluation without updating this record. A decision not recorded here is not a decision in the sense this philosophy defines — it is an arbitrary choice and must be resolved before use.

---

### DR-001: Neutral scale additional stops

**Stops added:** neutral-0, neutral-450, neutral-825, neutral-850.

**Basis for neutral-0 (#FFFFFF).** Pure white is required for action button label text, icon-on-accent, and action-primary-text. The 50 stop (#FAFAFA) is not sufficient. The contrast difference between #FAFAFA and a saturated fill is not equivalent to white. White is the specified value in the Krutho palette documentation and in standard accessibility practice for text on saturated fills.

**Basis for neutral-450 (#AFAFAF).** text-placeholder light requires a value perceptibly lighter than text-disabled (neutral-400, #C4C4C4) and darker than text-faint (neutral-500, #9A9A9A). No adjacent stop serves this function. The value is the arithmetic midpoint: (196 + 154) / 2 = 175 = RGB(175, 175, 175) = #AFAFAF. The derivation is reproducible without reference to the original authoring decision.

**Basis for neutral-825 (#2A2A2A) and neutral-850 (#202020).** The Krutho palette document specifies four distinct dark background values: #343434,
#2A2A2A, #202020, #181818. Each must map to a distinct primitive stop.
On a standard 11-stop scale, only #343434 (neutral-800) and #181818 (neutral-900) have natural positions. Adding neutral-825 and neutral-850 accommodates all four values without compression. Compressing two values onto a single stop would make them indistinguishable by reference, which defeats the function of the primitive scale.

---

### DR-002: Dark feedback surface derivation method

**Formula.** Dark feedback surfaces are derived by compositing the semantic source stop over neutral-900 (#181818) at 12% opacity.

**Basis for the method.** Four dark feedback surface values were previously specified as authored hex values without a derivation basis. An authored hex value without a derivation basis cannot be verified by inspection. It requires trust in the maker's judgment. The philosophy defines correctness that cannot be verified as indistinguishable from incorrectness.

A formula derivable from the defined primitives resolves this. Any party can compute the expected value and confirm the rendered value matches.

**Basis for the 12% figure.** The opacity must produce a tint that is perceptible on a dark background without dominating it. Below 8%, the tint is below perceptual threshold at typical viewing distances. Above 15%, the surface begins to compete with node-level colour when diagrams are rendered on dark backgrounds. 12% is the midpoint of the viable range. The result at 12% is verifiable against the formula by any party.

---

### DR-003: Deep base values excluded from signal-blue ramp, and teal anchored at 700

**Deep base exclusion.** Including deep-base-a (#000035) and deep-base-b (#010364) as stops on the signal-blue ramp would compress the dark end of the scale. The perceived lightness difference between signal-blue-900 (#001F6B) and #000035 is below the threshold of reliable discrimination at the sizes used in UI and diagram contexts. A ramp with indistinguishable adjacent stops fails its function as a reference scale.

Additionally, ramp membership implies tonal relationships: hover states, surface tints, and text contrast pairs. The deep base values are structural anchors used for fixed elements. A structural anchor that acquires hover and tint relationships through ramp membership has been misclassified. Fixed identity is the required property. Ramp membership contradicts it.

**Teal anchored at 700.** The Accent value #004964 has a relative luminance of approximately 3.5%, placing it perceptually at the dark end of a ramp. Anchoring at 500 would compress the lighter stops to a degree where fills (stops 50 through 300) would not be perceptually distinct from neutral at the node sizes used in diagrams. Anchoring at 700 allows lighter stops to carry sufficient saturation for categorical fill use while preserving the brand anchor value at its correct tonal position.

---

### DR-004: Amber ramp admitted to the system

**Basis.** The amber ramp is admitted on two independent grounds. Either alone is sufficient.

**Ground one — diverging scale.** Diverging data requires two hues extending outward from a neutral midpoint with equal visual weight. The positive pole uses signal-blue. A warm complement is required for the negative pole. No warm hue exists in the current brand palette at any stop. Without an amber ramp, a diverging scale cannot be constructed from defined primitives. The ramp is admitted to close a functional gap.

**Ground two — categorical coverage.** The four categorical diagram tokens require four perceptually distinct hue families. The three existing brand families — signal-blue at approximately 220°, secondary-signal at approximately 238°, and teal at approximately 198° — are all cool hues in the blue-to-teal sector. At the fill and node sizes used in these diagrams, three variants of the same cool hue sector are not reliably discriminated. A warm hue at approximately 37° (amber) produces a categorical set where each member is distinguishable from all others under normal viewing conditions.

Both grounds are functional, not aesthetic. The ramp's scope is restricted to the diagram layer. It does not appear in surface, text, border, icon, action, or feedback tokens.

---

### DR-005: Categorical diagram tokens named by role, not ordinal position

**Previous form.** The categorical tokens were initially specified as --color-diagram-cat-1 through --color-diagram-cat-4. Ordinal names specify position in a sequence. They do not specify function.

**Failure.** An independent party reading --color-diagram-cat-2 cannot determine, without external knowledge, what class of entity receives that token. Correct use cannot be assessed. A specification that requires external knowledge to interpret is not independently verifiable.

**Resolution.** Each token is named to specify its assigned function: trust, integration, transport, state. Each is defined by a criterion precise enough that two independent parties would reach the same assignment for any entity encountered in the diagram types covered by this specification.

**Boundary condition.** Where an entity satisfies more than one definition, the assignment rule is: assign by primary function. Primary function is the function the entity exists to perform. Secondary functions do not determine category assignment. This rule is deterministic. It does not require judgment about which definition is more relevant.

---

### DR-006: Surface elevation naming convention

**Previous form.** The Krutho palette documentation named surfaces as Base, Raised, Section, and Structure. The new document uses overlay, raised, base, and sunken.

**Basis for the change.** The original naming placed Base at the lightest (most elevated) stop and applied no term for the recessed input-fill surface. This created two problems. First, "Base" as a name for the highest surface is directionally ambiguous — it connotes ground-level, not elevation. Second, the absence of a recessed surface token meant inputs inside cards had no neutral way to visually recede below the card surface.

The elevation metaphor — overlay floats above all; raised floats above page; base is the page; sunken recedes below — is directionally unambiguous. Each name describes where in the z-axis the surface sits. The term "sunken" closes the input-fill gap.

The values for raised (#FAFAFA light) and base (#F2F2F2 light) are preserved from the original specification. Section (#E6E6E6) becomes sunken. Structure (#D6D6D6) is not carried forward: no token use case requires a fourth distinct surface stop in the light theme. Its omission is documented here as a boundary condition of the specification, not as an oversight.

---

### DR-007: Gradient exclusion with defined exception

**General rule.** Gradients are not part of the core colour system. A gradient requires two colours to produce its effect. Principle 4 (colour independence) requires each colour to be complete and independent. A gradient violates this principle structurally.

**Exception.** A single linear gradient between two stops of the same primitive ramp is permitted in illustrative diagrams where the gradient represents a continuous physical property (temperature stratification, pressure distribution, concentration gradient). The property must be genuinely continuous in the subject being illustrated. The gradient must use exactly two stops from one ramp. No radial gradients. No multi-stop gradients. No gradients used for aesthetic effect.

**Scope of exception.** The exception is scoped to the diagram layer, illustrative mode only. It does not apply to UI components, brand expression, or any other diagram mode.

---

### DR-008: Primitive ramp derivation method

**Standing condition.** DR-002 establishes that authored hex values without a derivation basis cannot be verified by inspection: an inspector must trust the maker's judgment. The philosophy treats correctness that cannot be verified as indistinguishable from incorrectness. DR-002 closes this gap for dark feedback surfaces through a compositing formula. The same standard applies to the primitive ramps themselves, which are currently authored at every stop except the brand anchors and a single arithmetic midpoint (neutral-450, DR-001).

**Target method.** Primitive ramp stops are derived by OKLCH lightness stepping from the brand anchor.

- The anchor stop's hex value is fixed at its registered position in the ramp.
- Other stops are derived by fixed lightness (L) intervals in OKLCH space, with chroma (C) and hue (H) held constant from the anchor.
- Where a derived stop falls outside the displayable sRGB gamut, chroma is reduced to the maximum displayable value at that lightness. The reduction is recorded against the affected stop.

OKLCH is selected over HSL because OKLCH is perceptually uniform: a fixed ΔL produces an approximately equal perceived lightness step at every position on the ramp. HSL does not have this property. Perceptual uniformity is required because the ramp's function is to provide reliably differentiated stops to a human inspector. A ramp constructed in a non-uniform space produces stops that compress perceptually at one end of the ramp and expand at the other, which defeats the purpose of an evenly-spaced reference.

**Lightness positions.** The target L value at each standard stop is:

| Stop | L value |
|------|---------|
| 50   | 0.97    |
| 100  | 0.92    |
| 200  | 0.83    |
| 300  | 0.74    |
| 400  | 0.65    |
| 500  | 0.56    |
| 600  | 0.47    |
| 700  | 0.38    |
| 800  | 0.29    |
| 900  | 0.20    |
| 950  | 0.11    |

These values produce ΔL = 0.09 between adjacent standard stops, with denser sampling at the lighter end (ΔL = 0.05 between 50 and 100) reflecting the greater perceptual sensitivity to lightness differences in the lighter half of the range. The anchor's actual L value may not fall exactly on the target for its stop; in that case, the anchor's L value defines a local origin and other stops are derived from the anchor by the same intervals, preserving the brand colour exactly.

Off-standard stops (neutral-0, neutral-450, neutral-825, neutral-850) retain their function-based derivations from DR-001 and are not subject to OKLCH stepping. Their basis is documented separately.

**Current state.** The ramp stops in this document are transitional. They were authored before this derivation method was specified. The hex values in the primitive scale tables do not yet conform to the OKLCH derivation defined here. The brand anchors are correct by definition; the surrounding stops are approximate.

**Closure path.** Re-derivation of every primitive ramp by OKLCH stepping from its registered anchor is a named gap in this specification. Until re-derivation is complete, ramp stops other than anchors are documented as transitional. A future revision of this document will replace the current hex values with the derived values and remove the transitional designation. The neutral, signal-blue, secondary-signal, teal, amber, error, success, and warning ramps are all in scope for re-derivation.

**Verifiability under the transitional state.** While transitional, the primitive ramps remain inspectable: their values are listed in this document and reproducible by any party. They are not yet inspectable as derivations from the anchor. The verifiability gap is named here so that readers can distinguish between values that are correct against the target method and values that are pending re-derivation.
