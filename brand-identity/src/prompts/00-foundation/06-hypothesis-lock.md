# 06-hypothesis-lock.md

**Purpose:** Compresses the selected hypothesis into a single governing structural position. This document becomes the primary input for all downstream modules. Everything built after this point is built on it.
**When to Use:** After you have confirmed your selected direction from `03_hypotheses_ranked.md`.
**Dependencies:** `03_hypotheses_ranked.md`, `02_foundational_brief.md`, your confirmed direction (A / B / C / Hybrid / New).
**Output:** `04_active_hypothesis.md`

---

## Pre-Lock Rules

**This is the structural point of no return.**
After this document is confirmed, the organising principle is fixed. Modules operate within it. If something feels uncertain, resolve it before running this prompt — not after.

**Source discipline.**
Use `03_hypotheses_ranked.md` as the primary input and `02_foundational_brief.md` as the validation reference. The lock must be consistent with the brief. If compression reveals a conflict with the brief, surface it — do not silently resolve it.

**Do not simply restate the hypothesis.**
Compress, clarify, and make explicit. Remove explanation that was scaffolding in the hypothesis stage. What remains should be denser and more precise, not shorter for its own sake.

**Every section traces to the brief.**
Citation format: `[Brief Section X]` or `[Hypothesis X]`
If a claim cannot be traced, label it: `[Inference — not from prior documents]`

---

## Direction Received

State which direction has been selected before proceeding:

- **Hypothesis A / B / C** — compress and formalise as-is
- **Hybrid** — define what is retained from each, what is discarded, and why. Remove incompatible logic before proceeding.
- **Human-introduced direction** — if a new direction was introduced at the handoff stage, treat it as a new hypothesis and apply the full structure below. Trace it to the brief to confirm it is grounded. If it cannot be traced, flag the gap before locking.

State the selected direction clearly at the top of the output file.

---

## Instruction

Read `src/outputs/00-foundation/02_foundational_brief.md` and `src/outputs/00-foundation/03_hypotheses_ranked.md` in full before beginning.

Compress the selected direction into `04_active_hypothesis.md`.

This document is read alongside `src/outputs/00-foundation/02_foundational_brief.md` at the start of every module prompt. Write it to be used, not admired. A designer reading it should be able to start work, know what to avoid, and recognise drift immediately.

Output a single file: `src/outputs/00-foundation/04_active_hypothesis.md`

---

## Required Output Structure

---

### Selected Direction

State clearly: which hypothesis (or hybrid, or new direction) this lock is based on, and confirm it was selected by the human reviewer.

---

### Organising Principle

One tight paragraph. The structural idea in its most compressed, precise form.

Must:
- Be explainable without visual reference
- Exclude alternatives
- Stand on its own without the hypothesis document behind it

Cite source: `[Hypothesis X — Organising Principle]`

---

### Structural Thesis

What this entity fundamentally is under this hypothesis. How it reframes or positions within its category. The structural shift this direction embodies.

This is internal logic — not positioning copy, not a tagline. Write it as a statement a designer would use to govern decisions, not a statement a client would read.

Trace to: `[Brief — Section 4]` and `[Hypothesis X]`

---

### Tension Resolution

For each active tension carried through from the brief (Brief Section 3):

- State the tension
- How this hypothesis resolves or holds it
- If it is held rather than resolved: what this means for design

No tension from the brief should be absent from this section. If a tension is no longer relevant under the selected direction, explain why.

---

### Design Consequences

The structural idea translated into system behaviour. These are inevitabilities, not preferences.

Define consequences for:
- Form logic (precision, openness, containment, reduction, etc.)
- Authority expression
- Tone boundaries
- Behavioural posture
- Scalability over time

Each consequence should read as: *given this organising principle, this follows necessarily.*

---

### What This Makes Impossible

The explicit exclusions. Be specific enough to use as a real filter.

- Aesthetic directions that are now off-limits
- Tonal registers that are incompatible
- Category signals that must be rejected
- Behaviours or claims the brand cannot make under this hypothesis

If something could still coexist, it is not excluded enough.

---

### Non-Negotiable Invariants

The structural truths that must remain intact across every element: logo, typography, colour, layout, imagery, UI behaviour, language.

Keep this tight: 5–8 maximum. These are the constants modules are tested against.

Cite each to the brief or hypothesis.

---

### Structural Risks

- Where this position is vulnerable
- What it depends on to succeed
- Under what conditions it should be re-evaluated
- What would constitute structural failure vs execution failure

---

### Durability Test

Answer directly:
- Does this rely on current taste?
- Would this survive market or cultural shift?
- Does it mature over time, or peak at launch?
- What would age poorly?

State any weaknesses found. Do not omit them.

---

### Final Structural Summary

5–7 sentences.

Written for a designer beginning module work. Clear enough to:
- Start work without ambiguity
- Identify what to avoid
- Identify what to reinforce
- Recognise drift the moment it occurs

No marketing tone. No softness. No hedging.

---

## Human Confirmation

Before any module begins, confirm this document is correct.

Review `04_active_hypothesis.md` and check:

1. Does the organising principle capture the direction you selected — precisely, without dilution?
2. Do the design consequences feel like they follow necessarily, or do they feel like preferences?
3. Is anything from the brief missing or contradicted?
4. Are the invariants tight enough to constrain the modules, or too broad to be useful?
5. Does the final summary give a designer a clear enough starting point?

If anything is wrong, correct it now. Once modules begin, the lock governs.

Confirm before proceeding.
