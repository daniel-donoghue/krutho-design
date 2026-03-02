# Typography System Generator

**Purpose:** Generates three structurally distinct typography system directions derived from the active hypothesis. Produces conceptual exploration briefs to initiate design work — not finished specifications or font selections.
**When to Use:** After hypothesis lock.
**Dependencies:** `02_foundational_brief.md`, `04_active_hypothesis.md`
**Output:** `typography_concepts_vX.md`

---

## Pre-Module Rules

**Source discipline.**
Use only `02_foundational_brief.md` and `04_active_hypothesis.md` as inputs.
Do not import typographic preferences, font families, or stylistic instincts from previous projects or general design knowledge unless explicitly flagged: `[External — not from project files]`

**Tracing is required.**
Every concept must demonstrate how its typographic logic follows from the active hypothesis and brief.
Citation format: `[Hypothesis — section]` or `[Brief — Section X]`
If a concept cannot be traced, it is not ready.

**Structural distinction is mandatory.**
Three concepts means three different typographic logics — not serif vs sans, not "modern vs classic." The distinction must be structural: different hierarchy philosophies, different authority models, different behavioural postures.

Self-check before output:
- Does each concept follow from the hypothesis in a different way?
- Does each concept produce a system that cannot coexist with the others?
- Would a designer working from Concept 1 make fundamentally different decisions than from Concept 2 or 3?

If any answer is no, revise before delivering.

**Do not lead with font names.**
Define system logic first — hierarchy, weight behaviour, spacing philosophy, case strategy. If specific font families are referenced, they must be structurally justified, not used as shorthand for a direction.

---

## Instruction

Read `src/outputs/00-foundation/04_active_hypothesis.md` and `src/outputs/00-foundation/02_foundational_brief.md` in full before generating any concept.

Generate three structurally distinct typography system directions.

Apply the identity gate from the brief to each concept and record the pressure test in full.

Rank all three and make a clear recommendation.

Output a single file: `src/outputs/01-systems/typography_concepts_vX.md`

---

## Required Output Structure

---

## Concept 1 — [Short Structural Name]

### Grounding Statement

In one sentence: how does this concept follow from the active hypothesis?

Cite: `[Hypothesis — Organising Principle]` and `[Brief — Section X]`

If this cannot be written clearly, the concept is not grounded. Do not proceed with it.

---

### Structural Typographic Logic

- What typographic principle governs this system?
- How does it express the organising principle through typographic behaviour?
- How does it position the brand within or against its category?

---

### Hierarchy Model

- How levels are defined and differentiated (size, weight, case, spacing — which levers, and why)
- How emphasis is created — and where it is forbidden
- How restraint is enforced structurally

---

### Weight & Emphasis Behaviour

- How many weights are structurally necessary — and the reason for that number
- Where emphasis is permitted and where it breaks the system
- What weight combinations are structurally excluded

---

### Scale & Proportion Strategy

- Base scale logic (modular, fluid, fixed intervals, etc.)
- Ratio philosophy and why it follows from the hypothesis
- Behaviour across different environments and output sizes

---

### Spacing & Rhythm Logic

- Letter spacing philosophy
- Line length and measure strategy
- Density vs openness — and what the organising principle demands
- Rhythm behaviour and how it enforces the structural idea

---

### Case Strategy

- Upper / lower / mixed — and the structural reason for each choice
- Where case signals authority, and where it must not

---

### Pairing Logic

- Single family or dual system — and the structural reason
- If dual: functional separation (display vs body, UI vs editorial) and why that separation exists
- What a second family must do that the first cannot

---

### Cross-Context Behaviour

- Product UI
- Marketing / web
- Long-form content / documentation
- Presentations (if relevant)

For each: what the system must accomplish and where it is most stressed.

---

### What This Makes Impossible

- Typographic territories that are structurally excluded
- Aesthetic registers that cannot coexist with this logic
- Category signals that must be avoided

If the list is vague, the concept is not strong enough.

---

### Category & Mis-Signal Risk

- What this could accidentally signal
- Where it could drift under pressure
- How the risk is mitigated structurally

---

### Identity Gate Pressure Test

Apply every gate question from `02_foundational_brief.md` Section 10.

For each question:
- **Pass / Conditional / Fail**
- One sentence justification

If any question results in Fail: state whether this is a fatal flaw or a resolvable condition.

---

### Exploration Brief

What the designer should begin from.

- The system behaviour to define first
- The hierarchy levels to prototype
- The specific tension to test (e.g. restraint vs legibility, authority vs warmth)
- What to avoid immediately — the traps this concept is most vulnerable to

---

## Concept 2 — [Short Structural Name]

*(Same structure as Concept 1)*

---

## Concept 3 — [Short Structural Name]

*(Same structure as Concept 1)*

---

## Structural Comparison

### Divergence Verification

For each pairing, explain the structural difference at the level of typographic logic — not aesthetic preference:

**Concept 1 vs Concept 2:**

**Concept 1 vs Concept 3:**

**Concept 2 vs Concept 3:**

If divergence in any pairing is primarily aesthetic, revise before proceeding.

---

### Hypothesis Coverage

Which concept most directly expresses the organising principle through typographic behaviour?
Which concept takes the greatest structural risk?
Which concept is most conservative relative to the hypothesis?

---

## Ranking & Recommendation

### Rank Order

Rank based on:
- Structural alignment with hypothesis
- Authority fit
- System scalability
- Durability over time
- Risk exposure

| Rank | Concept | Primary Reason |
|---|---|---|
| 1 | | |
| 2 | | |
| 3 | | |

### Recommendation

State which concept is structurally strongest and why. Include the condition under which the second-ranked might be preferable.

Do not soften the recommendation.

---

## Human Handoff

When reviewing `typography_concepts_vX.md`, consider:

1. Does the recommended concept feel right for this entity's communication needs — not just structurally correct?
2. Does the hierarchy model reflect how this brand actually needs to communicate across contexts?
3. Is there a typographic logic not represented here that you want to explore?
4. Are the exploration briefs specific enough to begin system definition from?
5. Does any concept risk drifting toward a category competitor's typographic territory?

You may select the recommendation, choose a different concept, introduce a new direction, or request a revised set. If introducing a new direction, define its grounding statement before beginning work.

Confirm your selected direction before proceeding.
