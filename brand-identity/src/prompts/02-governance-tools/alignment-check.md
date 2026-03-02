# Alignment Check

**Purpose:** Performs a structural audit across developed system elements to detect drift, contradiction, and weakening of the active hypothesis. Can be run against concept files or actual design outputs.
**When to Use:** After two or more system elements exist. Run whenever coherence is in question, before presenting work, or after introducing a new element.
**Dependencies:** `02_foundational_brief.md`, `04_active_hypothesis.md`, all element files to be audited.
**Output:** `alignment_review.md`

---

## Pre-Audit Rules

**Source discipline.**
Evaluate only against the project files. Do not introduce new strategy, reinterpret the hypothesis, or apply external design standards.
The brief and active hypothesis are the sole reference points.

**This is a structural audit, not an execution critique.**
Do not assess craft quality, aesthetic preference, or production standards.
Assess only whether each element is structurally coherent with the organising principle and whether the system holds together across elements.

**Distinguish what is being audited.**
Before beginning, identify whether the element files being assessed are:
- Concept files (from module prompts — structural directions, not finished work)
- Design outputs (actual developed work — assets, specifications, prototypes)

State this at the top of the output. The audit applies to both, but the implications differ: concept-level drift can be corrected before work begins; output-level drift may require rework.

**Concrete findings only.**
Every finding must identify a specific element, a specific section or decision within it, and a specific conflict with the brief or hypothesis. Vague observations are not useful and should not be included.

---

## Instruction

Read `src/outputs/00-foundation/02_foundational_brief.md` and `src/outputs/00-foundation/04_active_hypothesis.md` in full before auditing any element.

Assess each element file in `src/outputs/` in turn.

Do not audit the lens, brief, or hypothesis files — these are the reference standards, not the subject of the audit.

Output a single file: `src/outputs/02-governance/alignment_review.md`

---

## Required Output Structure

---

### Audit Context

- Files being audited (list each)
- Whether these are concept files or design outputs
- Which version of the brief and hypothesis this audit is against

---

### Structural Summary

5–8 sentences.

- Is the system coherent as a whole?
- Where does it reinforce itself productively?
- Where is coherence breaking down?
- What is the single most urgent structural issue?

Readable as a standalone summary before the detail sections.

---

### Element-by-Element Assessment

For each element file:

#### [Element Name]

**Structural Alignment:** Strong / Moderate / Weak
Cite the specific section of the element and the section of the brief or hypothesis it conflicts with or supports.

**Hypothesis Fidelity:** Strong / Moderate / Weak
Does this element express the organising principle, or does it merely not contradict it? These are different. Be explicit.

**Authority Fit:** Strong / Moderate / Weak
Does the authority signal match what the brief defines? Cite specifically.

**Category Signal:** Clear / Mixed / Misaligned
What does this element signal about category? Is that correct?

**Constraint Compliance:** Yes / Partial / No
List any hard constraints from the brief this element breaks or risks breaking.

---

### Cross-Element Coherence

**Reinforcement:** Where do elements amplify each other structurally? Be specific.

**Contradiction:** Where do elements work against each other? Name the specific conflict and which element it originates from.

**Silent Divergence:** Where do elements appear compatible but are operating on different structural logics? This is the hardest to catch and the most damaging — name it if present.

---

### Identity Gate Audit

Apply every gate question from `02_foundational_brief.md` Section 10 to the system as a whole.

For each question:
- **Pass / Conditional / Fail**
- Which element(s) provide the evidence
- Risk level if Conditional or Fail: Low / Medium / High
- Action required if not passing

---

### Drift Detection

For each drift type, state whether it is present, absent, or unclear — with specific evidence:

**Structural drift** — Has the organising principle been weakened or quietly replaced?

**Tonal drift** — Has the emotional register shifted away from what the brief defines?

**Category drift** — Is the system beginning to signal a different category than intended?

**Behavioural drift** — Does interaction logic diverge from visual logic?

**Accumulation drift** — Do individual decisions that each pass in isolation combine to produce a system that fails collectively? This must be assessed even when no individual element is flagged.

---

### Risk Level

| Level | Meaning |
|---|---|
| **Stable** | System is coherent. Continue. |
| **Early Drift** | One or two elements showing divergence. Correct before expanding. |
| **Significant Drift** | Multiple elements diverging. Pause new work and address. |
| **Structural Breakdown** | Organising principle no longer holds. Return to hypothesis or brief. |

State the level and explain what is driving the classification.

---

### Strongest Reinforcement

Which element most clearly and directly expresses the active hypothesis?
What specifically makes it strong?
What can other elements learn from it?

---

### Weakest Structural Link

Which element most threatens system coherence?
What specifically is the problem?
What would need to change to correct it?

---

### Recommendation

State clearly what should happen next. One primary action:

- **Continue exploration** — system is stable, proceed
- **Correct specific element(s)** — name which, what must change, what the brief demands instead
- **Revisit active hypothesis** — hypothesis may be underdefined; return to `05-hypothesis-lock.md`
- **Pause and clarify brief** — a gap in the brief is producing drift; return to `03-foundational-brief.md`

Be direct. State what should happen and why.

---

## Human Handoff

When reviewing `alignment_review.md`:

1. Does the structural summary reflect what you are seeing in the work?
2. Are any drift findings surprising — and if so, do they reveal something true?
3. Is the recommended action correct, or is there a different priority?
4. Are there elements not yet built that would resolve current tensions?
5. Does the weakest structural link require correction before more work continues?

This audit is a tool, not a verdict. Use the findings to direct your next decision.
