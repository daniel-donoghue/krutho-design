# Sanity Gate

**Purpose:** A rapid structural stress test for a single concept, direction, or decision. Faster than a full alignment check — designed to be run in the moment when something feels uncertain or needs quick validation before proceeding.
**When to Use:** When a single concept or decision needs quick structural validation. Before presenting a single direction. When something feels right but you can't articulate why — or feels wrong but you can't articulate why.
**Dependencies:** `02_foundational_brief.md`, `04_active_hypothesis.md`, the single item to be tested.
**Output:** `sanity_check.md`

---

## Pre-Gate Rules

**One item only.**
This tool tests a single concept, direction, or decision — not a system. For system-level audits, use the Alignment Check.

**Source discipline.**
Evaluate only against the brief and hypothesis. Do not introduce external design standards, aesthetic preferences, or category conventions.

**Binary discipline.**
Every assessment in this tool results in a clear position. No hedging. If the answer is genuinely uncertain, the uncertainty itself is the finding — state it explicitly and name what would resolve it.

**This is not an execution critique.**
Do not assess craft, finish, or aesthetic quality. Assess structural integrity only.

---

## Instruction

Read `src/outputs/00-foundation/02_foundational_brief.md` and `src/outputs/00-foundation/04_active_hypothesis.md` in full.

Then apply the gate to the concept or item under review.

Output a single file: `src/outputs/02-governance/sanity_check.md`

---

## Required Output Structure

---

### What Is Being Tested

Name the item and state in one sentence what structural claim it is making.

If the item's structural claim cannot be articulated, that is the first finding: the concept lacks a legible structural argument. Do not proceed with the gate — return the finding and stop.

---

### Structural Summary

3–5 sentences.

- What structural argument does this concept express?
- Does it clearly embody the organising principle?
- What is the strongest thing about it structurally?
- What is the most exposed thing about it structurally?

---

### Inevitable or Plausible?

Classify the concept as one of:

- **Inevitable** — this is a clear structural consequence of the hypothesis. It is hard to argue against given the brief.
- **Plausible** — this could work, but it is not structurally necessary. Another direction could be equally justified.
- **Decorative** — the concept has aesthetic merit but no discernible structural argument. It is not grounded in the hypothesis.

Justify the classification with specific reference to the hypothesis and brief.

If Plausible or Decorative: state what would need to change to make it Inevitable.

---

### Organising Principle Check

- Does this concept reinforce the active hypothesis directly?
- Where does it weaken or blur the organising principle?
- Is any part of it operating on a different structural logic than the hypothesis?

Be specific. Cite `[Hypothesis — section]` for each finding.

---

### Identity Gate Audit

Apply every gate question from `02_foundational_brief.md` Section 10.

For each question:
- **Pass / Conditional / Fail**
- One sentence justification

For any Fail:
- Is this a fatal flaw (concept cannot proceed without structural rework)?
- Or a correctable condition (specific element can be adjusted)?

---

### What This Makes Impossible

What does this concept structurally exclude?

If the answer is nothing meaningful — if this concept could coexist with almost anything — it is structurally weak. State that directly.

---

### Drift Detection

Does this concept introduce any of the following? State present / absent for each with evidence:

- **Structural drift** — weakens or replaces the organising principle
- **Tonal drift** — shifts emotional register away from the brief
- **Category drift** — signals a different or adjacent category
- **Behavioural contradiction** — conflicts with other established system elements

---

### Durability Test

Answer each directly:

- Does this rely on current taste or trend?
- Would it survive significant market or cultural shift?
- Does it scale into a full system or does it depend on a single execution?

---

### Risk Classification

**Low Risk** — structurally sound, gate passes, proceed with confidence
**Moderate Risk** — one or two conditional findings, refinement required before proceeding
**High Risk** — gate failures or structural misalignment, rework required

State the classification and the specific finding driving it.

---

### Verdict

One of four outcomes — no ambiguity:

- **Proceed** — structurally sound, continue development
- **Refine** — element-level correction needed, specific issue identified, rework is minor
- **Rework** — structural issue, concept needs to be rebuilt from the organising principle
- **Revisit hypothesis** — the concept is coherent but reveals a problem with the hypothesis or brief itself

State the verdict and the one sentence reason for it.

---

## Human Handoff

The gate has given a verdict. You decide what to do with it.

- If Proceed: continue with confidence, or note any Conditional findings to watch.
- If Refine: is the specific correction clear enough to act on?
- If Rework: is the structural problem identified precisely enough to rebuild from?
- If Revisit hypothesis: does the finding reveal something true about the hypothesis that needs addressing before more work is done?

The gate is a structural instrument. Your creative judgment governs what happens next.
