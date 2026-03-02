# UI Behaviour System Generator

**Purpose:** Generates three structurally distinct UI behaviour directions derived from the active hypothesis. Produces conceptual exploration briefs — not interaction specifications or component libraries.
**When to Use:** After hypothesis lock. Typically after logo and typography have been established.
**Dependencies:** `02_foundational_brief.md`, `04_active_hypothesis.md`
**Output:** `ui_behaviour_concepts_vX.md`

---

## Pre-Module Rules

**Source discipline.**
Use only `02_foundational_brief.md` and `04_active_hypothesis.md` as inputs.
Do not import interaction patterns, motion styles, or UX conventions from previous projects or general design knowledge unless explicitly flagged: `[External — not from project files]`

**Tracing is required.**
Every concept must demonstrate how its behavioural logic follows from the active hypothesis and brief.
Citation format: `[Hypothesis — section]` or `[Brief — Section X]`
If a concept cannot be traced, it is not ready.

**Structural distinction is mandatory.**
Three concepts means three different behavioural philosophies — not three motion styles or three visual treatments of interaction. The distinction must be at the level of how the system relates to its user: who holds control, how trust is constructed, how the system behaves under complexity.

Self-check before output:
- Does each concept follow from the hypothesis in a different way?
- Does each concept define a different relationship between system and user?
- Would a designer working from Concept 1 make fundamentally different interaction decisions than from Concept 2 or 3?

If any answer is no, revise before delivering.

**Describe behavioural philosophy, not animation style.**
Do not lead with motion language (easing, duration, transitions) without first establishing the behavioural principle that demands them.
Every interaction decision must trace to the organising principle.

---

## Instruction

Read `src/outputs/00-foundation/04_active_hypothesis.md` and `src/outputs/00-foundation/02_foundational_brief.md` in full before generating any concept.

Generate three structurally distinct UI behaviour directions.

Apply the identity gate from the brief to each concept and record the pressure test in full.

Rank all three and make a clear recommendation.

Output a single file: `src/outputs/01-systems/ui_behaviour_concepts_vX.md`

---

## Required Output Structure

---

## Concept 1 — [Short Structural Name]

### Grounding Statement

In one sentence: how does this concept follow from the active hypothesis?

Cite: `[Hypothesis — Organising Principle]` and `[Brief — Section X]`

If this cannot be written clearly, the concept is not grounded. Do not proceed with it.

---

### Behavioural Philosophy

The fundamental relationship between the system and the user:
- Who holds control — system-led, user-led, or collaborative?
- Decision posture: guided, permissive, assertive, neutral, invisible — and the structural reason
- How agency is expressed or withheld
- What this says about the brand's relationship to its users

---

### Trust Signalling Logic

How the system communicates certainty and earns confidence:
- How the system communicates what it knows
- How risk and uncertainty are surfaced — or withheld
- How reassurance is provided without false confidence
- What the system must never do to break trust

---

### State & Visibility Strategy

What is revealed, what is progressive, what remains silent:
- What is always visible regardless of context
- What appears only when needed
- What is never surfaced (and the structural reason)
- How the system communicates its own state

---

### Motion & Feedback Behaviour

How the system responds to action:
- Motion posture (present, subtle, declarative, minimal) and the structural reason
- Feedback timing logic — immediate vs deferred, and when each is correct
- Confirmation patterns — when and how the system acknowledges action
- What motion would break the system

---

### Error & Recovery Logic

How the system behaves when things go wrong:
- Tone in failure states — and what tone is structurally forbidden
- Clarity of recovery: how the path forward is communicated
- Attribution of failure: system, user, or external — and how this is handled
- Escalation path under repeated failure

---

### Complexity Scaling

How the system behaves as demands increase:
- Under more data or information density
- Under expanded permissions or user roles
- Under edge cases and exceptions
- What behaviour must remain constant regardless of complexity

---

### What This Makes Impossible

- Interaction patterns that are structurally excluded
- UX conventions that would mis-signal
- Behavioural registers that cannot coexist with this logic

If the list is vague, the concept is not strong enough.

---

### Category & Mis-Signal Risk

- What product category this could accidentally feel like
- What interaction conventions would undermine the brand's authority
- Where it could drift toward generic SaaS patterns under development pressure
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

- The first interaction decision to define (agency model, trust signal, or state logic)
- The primary tension to prototype (e.g. guidance vs autonomy, visibility vs simplicity)
- What to test with a real user task before committing
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

For each pairing, explain the structural difference at the level of behavioural philosophy — not visual or motion style:

**Concept 1 vs Concept 2:**

**Concept 1 vs Concept 3:**

**Concept 2 vs Concept 3:**

If divergence in any pairing is primarily cosmetic, revise before proceeding.

---

### Hypothesis Coverage

Which concept most directly expresses the organising principle through interaction behaviour?
Which concept takes the greatest structural risk?
Which concept is most conservative relative to the hypothesis?

---

## Ranking & Recommendation

### Rank Order

Rank based on:
- Structural alignment with hypothesis
- Authority fit
- Risk mitigation strength
- Durability under scale and complexity
- Operational clarity for a development team

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

When reviewing `ui_behaviour_concepts_vX.md`, consider:

1. Does the recommended concept's behavioural philosophy feel right for how this brand needs to relate to its users?
2. Does the trust signalling logic reflect the actual stakes for this entity's users?
3. Is there a behavioural approach not represented here that you want to explore?
4. Are the exploration briefs specific enough to begin interaction design from?
5. Does any concept risk feeling like a generic SaaS product under development pressure?

You may select the recommendation, choose a different concept, introduce a new direction, or request a revised set. If introducing a new direction, define its grounding statement before beginning work.

Confirm your selected direction before proceeding.
