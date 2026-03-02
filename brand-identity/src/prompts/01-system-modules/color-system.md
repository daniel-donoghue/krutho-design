# Colour System Generator

**Purpose:** Generates three structurally distinct colour system directions derived from the active hypothesis. Produces conceptual exploration briefs — not palettes, not hex values.
**When to Use:** After hypothesis lock.
**Dependencies:** `02_foundational_brief.md`, `04_active_hypothesis.md`
**Output:** `colour_concepts_vX.md`

---

## Pre-Module Rules

**Source discipline.**
Use only `02_foundational_brief.md` and `04_active_hypothesis.md` as inputs.
Do not import colour tendencies, palettes, or aesthetic instincts from previous projects or general design knowledge unless explicitly flagged: `[External — not from project files]`

**Tracing is required.**
Every concept must demonstrate how its colour logic follows from the active hypothesis and brief.
Citation format: `[Hypothesis — section]` or `[Brief — Section X]`
If a concept cannot be traced, it is not ready.

**Structural distinction is mandatory.**
Three concepts means three different colour system logics — not three palettes. The distinction must be at the level of how colour is used to construct meaning, signal authority, and govern behaviour.

Self-check before output:
- Does each concept follow from the hypothesis in a different way?
- Does each concept make colour behave differently as a structural element?
- Would a designer working from Concept 1 produce a system that could not have come from Concept 2 or 3?

If any answer is no, revise before delivering.

**Do not lead with hex values or named colours.**
Define role logic, behaviour, and usage rules first. Specific colour values are the designer's decision — this stage defines what colour must do, not what it must be.

---

## Instruction

Read `src/outputs/00-foundation/04_active_hypothesis.md` and `src/outputs/00-foundation/02_foundational_brief.md` in full before generating any concept.

Generate three structurally distinct colour system directions.

Apply the identity gate from the brief to each concept and record the pressure test in full.

Rank all three and make a clear recommendation.

Output a single file: `src/outputs/01-systems/colour_concepts_vX.md`

---

## Required Output Structure

---

## Concept 1 — [Short Structural Name]

### Grounding Statement

In one sentence: how does this concept follow from the active hypothesis?

Cite: `[Hypothesis — Organising Principle]` and `[Brief — Section X]`

If this cannot be written clearly, the concept is not grounded. Do not proceed with it.

---

### Structural Colour Logic

- What role does colour play in this system — how does it construct meaning rather than decorate?
- How does this colour approach express the organising principle?
- How does it signal or reframe category position?

---

### Role Model

How colour is used to structure information and signal intent:
- Where colour carries authority
- Where colour is suppressed or neutral
- Where colour signals state, status, or action
- What colour is never allowed to do in this system

---

### Token Roles

Define the functional roles — no hex values required:
- Background / surface
- Primary text / secondary text
- Border / divider
- Accent / highlight
- Interactive / focus state
- Status signals: success / warning / error / info (if applicable)

For each role: what it must communicate and what it must never imply.

---

### Contrast & Accessibility Strategy

- Contrast philosophy (where high contrast is required, where it is deliberately reduced)
- What must always remain readable regardless of context
- Accessibility intent and the structural reason for it

---

### Behaviour by Context

How the system behaves across different surfaces:
- Product UI
- Marketing / web
- Documentation / diagrams
- Print / physical (if relevant)

For each: what the colour system must accomplish and where it is most stressed.

---

### What This Makes Impossible

- Colour approaches that are structurally excluded
- Palette territories that would mis-signal
- Combinations that cannot coexist with this logic

If the list is vague, the concept is not strong enough.

---

### Category & Mis-Signal Risk

- What this could accidentally signal (competitor territory, wrong category, wrong emotional register)
- Where it could drift under production pressure
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

- The role or relationship to define first
- The primary contrast decision to make
- What to test across contexts before committing
- What to avoid immediately — the specific traps this concept is most vulnerable to

---

## Concept 2 — [Short Structural Name]

*(Same structure as Concept 1)*

---

## Concept 3 — [Short Structural Name]

*(Same structure as Concept 1)*

---

## Structural Comparison

### Divergence Verification

For each pairing, explain the structural difference at the level of colour logic — not palette aesthetics:

**Concept 1 vs Concept 2:**

**Concept 1 vs Concept 3:**

**Concept 2 vs Concept 3:**

If divergence in any pairing is primarily aesthetic, revise before proceeding.

---

### Hypothesis Coverage

Which concept most directly expresses the organising principle through colour behaviour?
Which concept takes the greatest structural risk?
Which concept is most conservative relative to the hypothesis?

---

## Ranking & Recommendation

### Rank Order

Rank based on:
- Structural alignment with hypothesis
- Authority fit
- Durability under cultural and market shift
- Operational usability at scale
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

When reviewing `colour_concepts_vX.md`, consider:

1. Does the recommended concept feel right for this entity's authority and emotional register?
2. Does the role model reflect how this brand actually needs to use colour across its contexts?
3. Is there a colour logic not represented here that you want to explore?
4. Are the exploration briefs specific enough to begin palette development from?
5. Does any concept risk drifting into competitor or category-generic territory?

You may select the recommendation, choose a different concept, introduce a new direction, or request a revised set. If introducing a new direction, define its grounding statement before beginning work.

Confirm your selected direction before proceeding.
