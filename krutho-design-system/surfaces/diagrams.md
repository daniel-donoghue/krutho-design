# Krutho Diagram Surface

Last edit 23rd April 2026

---

## Grounding Statement

This document is the Krutho Diagram Surface. It operates under the Krutho Design Philosophy and derives from the Krutho Colour System.

This document defines the colour token set for technical diagrams and data visualisations. Every token references a primitive stop defined in the Krutho Colour System. The governing principles of the Krutho Colour System apply to all tokens defined here. The gradient exception stated in Principle 4 of that document is scoped to this surface.

Diagram tokens and UI component tokens do not cross. Semantic tokens apply to diagrams only when the diagram operates in semantic mode, in which case the semantic source tokens apply directly.

Referenced primitive stops are reproduced in the Primitive Reference at the end of this document for independent verification.

---

## Colour Modes

Every diagram operates in one or more of five colour modes. The mode is determined by the type of information being communicated.

| Mode        | Question the colour answers              | Typical diagram types                                        |
|-------------|------------------------------------------|--------------------------------------------------------------|
| Signal      | What matters in this diagram?            | Process flows, swimlanes, architectural diagrams             |
| Categorical | Which group is this?                     | Architecture, network graphs, categorical data charts        |
| Sequential  | How much, or how far?                    | Heatmaps, timelines, density charts, volume series           |
| Diverging   | Which direction from the centre?         | Delta charts, valid/expired distributions, before/after      |
| Semantic    | What does the system judge this to be?   | Status dashboards, compliance matrices, threshold alerts     |

A diagram that cannot be assigned to any defined mode requires a specification addition before colour is applied. Using an existing mode for an unspecified purpose is a conformance failure.

---

## Signal Mode

Signal mode is used when a diagram is primarily neutral and colour marks only those moments that carry distinct meaning within that neutrality. The majority of nodes remain neutral. Signal is withheld until a signal condition is met.

Two signal conditions are defined.

**Trust layer active.** A component, node, or step in which cryptographic verification, identity assertion, or trust chain operations are occurring. Filled with signal-blue · 50. Bordered with signal-blue · 500. Text in signal-blue · 800.

**Human decision in motion.** A step at which a person must act. White fill, strong neutral border. The border weight distinguishes the node from infrastructure. Blue is reserved for the trust layer; a human is not the trust layer.

Signal mode extends to connectors only when the connection represents a trust handoff. A connector between two trust-layer nodes is not itself a trust event. The connector-trust token is applied only when the connection is the handoff.

### Signal mode tokens

| Token                               | Description                              | Light              | Dark               |
|-------------------------------------|------------------------------------------|--------------------|--------------------|
| --color-diagram-signal-trust-fill   | Trust layer node or container fill       | signal-blue · 50   | signal-blue · 900  |
| --color-diagram-signal-trust-border | Trust layer node or container border     | signal-blue · 500  | signal-blue · 500  |
| --color-diagram-signal-trust-text   | Text on trust layer fill                 | signal-blue · 800  | signal-blue · 200  |
| --color-diagram-signal-human-border | Human action node border                 | neutral · 900      | neutral · 50       |

---

## Categorical Mode

Categorical mode is used when distinct domains, systems, or entity types require simultaneous visual separation. All members of the same category receive the same colour treatment. Categories carry no hierarchy; colour does not rank.

Maximum four categories. A fifth category is rendered neutral and its role is documented in the diagram key. A diagram requiring more than four colour-separated categories requires structural redesign before a fifth colour.

Each categorical token is defined by function. Ordinal names (cat-1, cat-2) specify position without carrying function; an independent party reading an ordinal token cannot determine what class of entity receives it. Functional names (trust, integration, transport, state) make correct use assessable by inspection.

### Category definitions

**Trust (signal-blue family)** Applied to components, systems, or processes that perform or rely on cryptographic verification, identity assertion, or trust chain operations. The defining criterion: correct behaviour depends on cryptographic proof rather than assumed permission.

**Integration (secondary-signal family)** Applied to partner systems, external services, and third-party components that communicate with the trust layer through defined interfaces. Connected to the trust chain but external to it. Does not itself perform verification.

**Transport (teal family)** Applied to network infrastructure, connectivity layers, routing, and data-in-motion systems. The defining criterion: the component's primary function is movement of data, not computation or storage of it.

**State (amber family)** Applied to storage systems, credential stores, databases, and data-at-rest. The defining criterion: the component's primary function is persistence of data, not movement or transformation of it.

Where an entity satisfies more than one definition, assign by primary function. Where an entity satisfies none, render it neutral and annotate.

### Relationship to signal tokens

The trust categorical tokens and the signal trust tokens reference the same primitive stops. Their distinction is scope. Signal tokens mark specific nodes in a predominantly neutral diagram. Categorical tokens mark all entities of a domain in a diagram where multiple domains require simultaneous colour distinction. A node correctly marked with diagram-signal-trust is also correctly categorised as diagram-cat-trust when the diagram operates in categorical mode.

### Categorical tokens

| Token                                  | Light                  | Dark                   |
|----------------------------------------|------------------------|------------------------|
| --color-diagram-cat-trust-fill         | signal-blue · 50       | signal-blue · 900      |
| --color-diagram-cat-trust-border       | signal-blue · 500      | signal-blue · 500      |
| --color-diagram-cat-trust-text         | signal-blue · 800      | signal-blue · 200      |
| --color-diagram-cat-integration-fill   | secondary-signal · 50  | secondary-signal · 900 |
| --color-diagram-cat-integration-border | secondary-signal · 500 | secondary-signal · 500 |
| --color-diagram-cat-integration-text   | secondary-signal · 800 | secondary-signal · 200 |
| --color-diagram-cat-transport-fill     | teal · 50              | teal · 900             |
| --color-diagram-cat-transport-border   | teal · 500             | teal · 500             |
| --color-diagram-cat-transport-text     | teal · 800             | teal · 200             |
| --color-diagram-cat-state-fill         | amber · 50             | amber · 900            |
| --color-diagram-cat-state-border       | amber · 500            | amber · 500            |
| --color-diagram-cat-state-text         | amber · 800            | amber · 200            |

---

## Sequential Mode

Sequential mode is used for ordered data with a single direction. The colour encodes position in the sequence. Signal-blue is the default sequential ramp. A second sequential variable in the same diagram uses the teal ramp.

Five stops are defined for standard use. These are the stops at which perceptual differentiation is reliable at typical diagram and chart dimensions. The full primitive ramp is available for precise mapping where finer gradation is required.

| Token                      | Primitive reference  | Position                     |
|----------------------------|----------------------|------------------------------|
| --color-diagram-seq-1      | signal-blue · 50     | Lowest / earliest / weakest  |
| --color-diagram-seq-2      | signal-blue · 200    |                              |
| --color-diagram-seq-3      | signal-blue · 400    | Mid                          |
| --color-diagram-seq-4      | signal-blue · 500    |                              |
| --color-diagram-seq-5      | signal-blue · 700    | Highest / latest / strongest |
| --color-diagram-seq-alt-1  | teal · 50            | Alternate ramp, lowest       |
| --color-diagram-seq-alt-2  | teal · 200           |                              |
| --color-diagram-seq-alt-3  | teal · 400           | Alternate ramp, mid          |
| --color-diagram-seq-alt-4  | teal · 500           |                              |
| --color-diagram-seq-alt-5  | teal · 700           | Alternate ramp, highest      |

---

## Diverging Mode

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

## Semantic Mode

Semantic mode uses the semantic source tokens from the Krutho Colour System directly. No separate diagram tokens are defined for this mode.

Status conditions map as follows.

| Condition                    | Token family       |
|------------------------------|--------------------|
| Valid / confirmed            | semantic · success |
| Invalid / failed             | semantic · error   |
| Expired / expiring / caution | semantic · warning |
| Informational / pending      | semantic · info    |

---

## Structural Tokens

Structural tokens apply to all diagram types regardless of mode. They govern headers, default nodes, annotations, connectors, and boundaries.

| Token                                 | Description                                                                                    | Light              | Dark               |
|---------------------------------------|------------------------------------------------------------------------------------------------|--------------------|--------------------|
| --color-diagram-header-bg             | Swimlane headers, container label tabs                                                         | deep-base-b        | deep-base-b        |
| --color-diagram-header-text           | Text on diagram headers                                                                        | neutral · 0        | neutral · 0        |
| --color-diagram-node-fill             | Default node fill                                                                              | neutral · 0        | neutral · 850      |
| --color-diagram-node-border           | Default node border                                                                            | neutral · 500      | neutral · 600      |
| --color-diagram-node-text             | Default node text                                                                              | neutral · 900      | neutral · 200      |
| --color-diagram-node-decision-border  | Decision / branch node, dashed, same colour as node border                                     | neutral · 500      | neutral · 600      |
| --color-diagram-annotation-fill       | Callout annotation background                                                                  | neutral · 200      | neutral · 825      |
| --color-diagram-annotation-text       | Callout annotation text                                                                        | neutral · 700      | neutral · 400      |
| --color-diagram-connector             | Standard connector line                                                                        | neutral · 500      | neutral · 600      |
| --color-diagram-connector-trust       | Trust handoff connector, used only when the connection is the handoff, not when adjacent to one | signal-blue · 500  | signal-blue · 500  |
| --color-diagram-connector-optional    | Non-critical or opportunistic path, fine dash                                                  | neutral · 400      | neutral · 600      |
| --color-diagram-boundary-physical     | Physical environment perimeter, coarse dash                                                    | neutral · 600      | neutral · 500      |
| --color-diagram-boundary-logical      | Logical grouping boundary, fine dash                                                           | neutral · 400      | neutral · 600      |
| --color-diagram-lane-divider          | Swimlane separator                                                                             | neutral · 200      | neutral · 825      |

---

## Governing Conditions

The following conditions state every assessable rule in this specification.

1. Every diagram operates in one or more of five colour modes: Signal, Categorical, Sequential, Diverging, Semantic. The mode is determined by the type of information being communicated.
2. A diagram that cannot be assigned to any defined mode requires a specification addition before colour is applied. Using an existing mode for an unspecified purpose is a conformance failure.
3. Maximum four categories in categorical mode. A fifth category is rendered neutral and documented in the diagram key.
4. Where an entity satisfies more than one category definition, assign by primary function. Primary function is the function the entity exists to perform.
5. Signal mode extends to connectors only where the connection represents a trust handoff.
6. Semantic mode uses the semantic source tokens from the Krutho Colour System directly. No separate diagram tokens are defined for this mode.
7. Diagram tokens are used in diagrams only. Semantic tokens are used in diagrams only when the diagram operates in semantic mode.
8. The gradient exception stated in Principle 4 of the Krutho Colour System applies to this surface: a single linear gradient between two stops of the same primitive ramp, used in illustrative diagrams to represent a continuous physical property.

---

## Primitive Reference

Reproduced from the Krutho Colour System for independent verification. These values are not defined by this document. A change to the Krutho Colour System requires updating this table.

### --primitive-neutral (referenced stops)

| Stop | Hex     |
|------|---------|
| 0    | #FFFFFF |
| 50   | #FAFAFA |
| 200  | #E6E6E6 |
| 300  | #D6D6D6 |
| 400  | #C4C4C4 |
| 500  | #9A9A9A |
| 600  | #707070 |
| 700  | #505050 |
| 825  | #2A2A2A |
| 850  | #202020 |
| 900  | #181818 |

### --primitive-signal-blue (referenced stops)

| Stop | Hex     |
|------|---------|
| 50   | #EBF3FF |
| 200  | #94BBFF |
| 400  | #3D85FF |
| 500  | #1A6FFF |
| 600  | #0055DD |
| 700  | #0044BB |
| 800  | #003399 |
| 900  | #001F6B |

### --primitive-secondary-signal (referenced stops)

| Stop | Hex     |
|------|---------|
| 50   | #EEEEFF |
| 200  | #B0B3F0 |
| 500  | #5C60D6 |
| 800  | #20228A |
| 900  | #10126A |

### --primitive-teal (referenced stops)

| Stop | Hex     |
|------|---------|
| 50   | #E0F4FA |
| 200  | #7DCAE3 |
| 400  | #1A96BE |
| 500  | #0A7CA4 |
| 700  | #004964 |
| 900  | #00203A |

### --primitive-amber (referenced stops)

| Stop | Hex     |
|------|---------|
| 50   | #FFF5E6 |
| 200  | #F5C478 |
| 500  | #C47B1A |
| 600  | #A86210 |
| 800  | #6C3804 |
| 900  | #4E2602 |

### --primitive-deep-base (referenced values)

| Name | Hex     |
|------|---------|
| b    | #010364 |
