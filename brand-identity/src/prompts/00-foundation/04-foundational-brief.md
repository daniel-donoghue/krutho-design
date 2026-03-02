# 04-foundational-brief.md

**Purpose:** Applies the active lens to the reviewed extraction to produce a structurally grounded brand brief. This is where analysis begins. The lens activates here for the first time.
**When to Use:** After `01_repo_extraction.md` has been reviewed and sense-checked.
**Dependencies:** `01_repo_extraction.md` (reviewed), active lens file.
**Output:** `02_foundational_brief.md`

---

## Pre-Brief Rules

**The lens is now active.**
Apply the Open If lens to everything in this stage. All structural observations, tensions, and brief sections are governed by it.

**The extraction is the only permitted source.**
`01_repo_extraction.md` is the sole input. Do not reach back to the original repository files. Do not introduce external knowledge about the company or its market unless explicitly flagged as: `[External — not from extraction]`

**This prompt runs in two stages. Both stages appear in the output.**
Stage 1 produces a structural interrogation — what the evidence means, what tensions emerge, what the lens surfaces.
Stage 2 produces the brief — built directly from Stage 1.

This structure is mandatory. It makes the reasoning visible and auditable. The brief cannot be cleaner than the interrogation supports.

**Do not resolve what cannot be resolved.**
If a tension is genuine, carry it forward as an active tension. Do not smooth it into a position. The brief is allowed to contain unresolved questions. Forcing resolution at this stage produces false confidence downstream.

**Every brief claim must trace to the extraction.**
Citation format: `[Extraction Section X — paraphrase or direct quote]`
If a claim cannot be traced, it must be labelled: `[Inference — not directly evidenced]`

---

## Instruction

Read `src/outputs/00-foundation/01_repo_extraction.md` in full before beginning either stage.

Then complete both stages in sequence.

Do not generate hypotheses.
Do not generate visual solutions.
Do not generate positioning copy or slogans.

Output a single file: `src/outputs/00-foundation/02_foundational_brief.md`

---

## Stage 1 — Structural Interrogation

This section appears first in the output. It is the reasoning layer — what the lens sees when applied to the extraction. Brief sections in Stage 2 must be traceable back to observations made here.

---

### 1.1 — What This Is (Structurally)

In plain language, what is this entity at its core — not what it claims, but what it structurally is based on the evidence?

Write 2–3 sentences. No marketing language. No borrowed vocabulary from the repo.

Cite which extraction sections this is drawn from.

---

### 1.2 — Structural Observations

What does the lens surface when applied to the extraction? List the most significant structural observations — things that are true about this entity that have consequences for identity.

Each observation must:
- Be traceable to the extraction
- Have a consequence (state it)
- Be written as a plain factual statement, not an analytical flourish

Format each as:
**Observation:** [what is true]
**Consequence:** [what this means for identity]
**Source:** [Extraction section]

---

### 1.3 — Tensions Identified

What genuine tensions exist in the material? A tension is a real conflict between two things that are both true — not a problem to solve, but a condition to design within.

For each tension:
- State it in one sentence
- Confirm it is evidenced (cite sources), not inferred
- State whether it appears resolvable from the extraction, or must remain open

If no genuine tensions exist in the evidence, state that. Do not manufacture them.

---

### 1.4 — What the Extraction Cannot Answer

What questions are material to brief formation but unanswered by the extraction?

List only questions that would change the brief if answered differently. Minor gaps do not belong here.

For each:
- State the question
- State what the brief must assume in its absence
- State the risk if that assumption is wrong

---

## Stage 2 — Foundational Brief

Built from Stage 1. Every section traces to an observation, tension, or source in Stage 1 or the extraction.

---

### 1. Strategic Summary

2–3 sentences. What this entity is, structurally, and what the identity work must accomplish.

No slogans. No marketing voice. Written as if briefing a senior designer on day one.

---

### 2. Structural Shift Required

What must change as a result of this identity work?

State plainly:
- The current state (evidenced or assumed — label which)
- The required state
- What achieving the shift depends on

If this cannot be determined from the extraction, state what must be validated and by whom.

---

### 3. Active Tensions

Carry forward all unresolved tensions from Stage 1.3.

For each:
- Tension statement (one sentence)
- Why it exists (cite extraction)
- What it means for design (consequence, not resolution)
- Whether it should be resolved before hypotheses, or designed within

Do not collapse tensions into positions here. That is the work of hypotheses.

---

### 4. Central Position

Define the position as a structural argument, not a tagline.

Include:
- Category framing (where it sits / how it reframes)
- Axis of differentiation (what makes it structurally distinct)
- One-sentence central claim (their argument, not a slogan)
- What it refuses to be (one sentence)

Every element must trace to Stage 1 or the extraction.

---

### 5. Audience

Define primary and secondary audiences from the extraction.

For each:
- Who they are (evidenced descriptors only)
- What they need to believe for this identity to work
- What they must feel
- What would break trust

Do not invent audiences not present in the extraction. If audience data is sparse, say so and flag it as a gap.

---

### 6. Authority

Where credibility comes from, structurally. Select from the list below and justify each selection with evidence from the extraction.

- Technical authority
- Institutional authority
- Relational authority
- Operational authority
- Visionary authority
- Infrastructural authority

Also define:
- How authority should feel in expression
- What would undermine it

---

### 7. Emotional Register

Define the emotional range the identity must operate within.

Include:
- The required register (plain descriptors — e.g. precise, assured, direct)
- What must be avoided and why
- The danger tone — the one register that would break trust immediately

Ground each in extraction evidence or label as inference.

---

### 8. Constraints

Summarise constraints as design consequences.

Format each as: **Constraint → Consequence**

Separate into:
- Hard constraints (cannot break — cite source)
- Soft constraints (avoid unless strong reason — cite source)
- Unknown constraints (must validate before modules begin)

---

### 9. Rejection Criteria

Define what will be rejected immediately, regardless of execution quality.

Include:
- Category mis-signals (what it must not resemble)
- Aesthetic tropes that imply the wrong thing
- Behavioural anti-patterns
- Narrative anti-patterns (what it must not claim)

Each item should be specific enough to use as a real filter, not a general preference.

---

### 10. Identity Gate

The test harness used by all downstream prompts — hypotheses, modules, and governance tools.

#### Gate Questions (Pass / Fail)

5–9 questions maximum. Each must be:
- Answerable using evidence from this brief
- A genuine structural constraint, not a taste preference
- Usable as a binary pass/fail test

#### Required Invariants

What must remain true across every expression: logo, type, colour, layout, imagery, language, UI behaviour.

Keep this tight — 5–8 maximum. If everything is invariant, nothing is.

#### Failure Modes

What would invalidate downstream form at a structural level — not execution quality, but structural misalignment.

---

### 11. Open Questions

Carry forward all unresolved questions from Stage 1.4, plus any that emerged during brief formation.

For each:
- The question
- What the brief currently assumes
- The risk if the assumption is wrong
- Who can resolve it

---

## Reviewer Handoff

This is the most significant review point in the process. You are not checking formatting — you are engaging with the structural argument.

When reviewing `02_foundational_brief.md`, ask:

1. Does Stage 1 show its reasoning clearly, or does it jump to conclusions?
2. Do the brief sections in Stage 2 follow logically from Stage 1?
3. Do the active tensions feel real, or has the model smoothed them over?
4. Does the central position feel like it follows from the evidence — or does it feel invented?
5. Are the rejection criteria specific enough to use, or are they generic?
6. Are the identity gate questions real constraints or reworded preferences?
7. Does anything feel like it came from outside the extraction?

If the brief can pass this review, hypotheses can be generated from it with confidence.
If it cannot, identify which sections need revisiting before proceeding.
