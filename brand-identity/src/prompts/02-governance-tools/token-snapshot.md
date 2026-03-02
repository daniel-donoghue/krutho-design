# Token Snapshot

**Purpose:** Extracts the current state of the design system into structured, reusable tokens. Documents what has been defined, what remains undefined, and flags anything inferred rather than explicitly stated.
**When to Use:** At meaningful milestones, before handoff to development, or before scaling the system. Not appropriate before at least two or three modules have been developed.
**Dependencies:** `04_active_hypothesis.md`, all current element files.
**Output:** `design_tokens_snapshot.md`

---

## Pre-Snapshot Rules

**This is extraction, not strategy.**
Extract only what is explicitly defined in the project files.
Do not invent missing values or rules.
Do not reinterpret the hypothesis.
Do not fill gaps with reasonable assumptions — gaps are data.

**Two modes of token.**
This tool can be run at two stages and will produce different outputs accordingly:

- **Concept-level snapshot** — taken from module concept files. Produces structural rules and system logic, not values. No hex codes, no specific typeface names unless they appear in the files.
- **Execution-level snapshot** — taken from developed design outputs. Produces actual values, specifications, and implementation-ready tokens.

State which mode applies at the top of the output. If a mix of concept and execution files are present, state which file contributes which level.

**Inferred content must be labelled.**
If a rule is implied by a decision but not explicitly stated, it may be included — but must be labelled clearly: `[Inferred]`
Inferred tokens should be reviewed and either confirmed or removed before handoff.

**Do not fill gaps.**
If a system area is not covered by the project files, record it as undefined. Do not generate placeholder logic.

---

## Instruction

Read `src/outputs/00-foundation/04_active_hypothesis.md` and all element files in `src/outputs/` before beginning.

Extract the current system state into structured tokens.

Identify all gaps — areas where the system has not yet been defined.

Output a single file: `src/outputs/02-governance/design_tokens_snapshot.md`

---

## Required Output Structure

---

### Snapshot Context

- Files included in this snapshot (list each)
- Snapshot mode: Concept-level / Execution-level / Mixed (specify)
- Which system areas are covered by this snapshot
- Which system areas are not yet defined

---

### Structural Foundation

Extracted directly from `04_active_hypothesis.md`:

- Organising principle (verbatim from hypothesis)
- Non-negotiable invariants (list each, verbatim)
- Active constraints relevant to all tokens

Source: `[04_active_hypothesis.md]`

---

### Typography Tokens

#### Scale System
- Base size (if defined — value or rule)
- Scale ratio or logic (if defined)
- Heading levels and their differentiation method

#### Weight Logic
- Permitted weights
- Restricted weights and the structural reason

#### Hierarchy Rules
- Primary emphasis method
- Secondary emphasis method
- Prohibited emphasis patterns

#### Spacing & Rhythm
- Line height logic
- Letter spacing logic
- Measure / line length rules (if defined)
- Density rules

#### Case Strategy
- Upper / lower / mixed rules and where each applies

Source: `[file reference]`
Undefined: [list anything not yet defined in typography]

---

### Colour Tokens

#### Role Definitions
For each role, state the rule — not the value (unless execution-level):
- Background
- Surface
- Primary text / secondary text
- Border / divider
- Accent / highlight
- Interactive / focus state
- Status signals (if defined): success / warning / error / info

#### Contrast Strategy
- High-contrast requirements
- Controlled contrast zones
- Accessibility rules (if explicitly defined)

#### Prohibited Territories
- Colour approaches explicitly excluded

Source: `[file reference]`
Undefined: [list anything not yet defined in colour]

---

### Layout Tokens

#### Grid Logic
- Grid type and structural reason
- Column logic
- Breakpoint behaviour (if defined)

#### Spacing System
- Base unit (if defined)
- Margin and padding rules
- Containment logic

#### Density Rules
- Sparse vs dense zones and when each applies
- White space rules

Source: `[file reference]`
Undefined: [list anything not yet defined in layout]

---

### Mark / Logo Tokens

*(Complete only if a logo concept or output file exists in `src/outputs/`)*

#### Construction Logic
- Geometry type and structural reason
- Containment rules
- Symbol / wordmark relationship

#### Scaling Behaviour
- Minimum size logic
- Monochrome rules
- Exclusion zone logic (if defined)

Source: `[file reference]`
Undefined: [list anything not yet defined for the mark]

---

### UI Behaviour Tokens

*(Complete only if a UI concept or output file exists in `src/outputs/`)*

#### Interaction Principles
- Agency model (system-led / user-led / collaborative)
- Decision posture

#### Motion Rules
- Motion presence (present / minimal / absent)
- Speed logic (if defined)
- What motion is structurally prohibited

#### Feedback Patterns
- Confirmation behaviour
- Error tone and recovery logic

Source: `[file reference]`
Undefined: [list anything not yet defined for UI behaviour]

---

### Imagery Tokens

*(Complete only if an imagery concept or output file exists in `src/outputs/`)*

#### Subject Rules
- What is permitted
- What is excluded
- Human presence rules

#### Treatment Rules
- Post-production level
- Colour treatment in relation to colour system

Source: `[file reference]`
Undefined: [list anything not yet defined for imagery]

---

### Non-Negotiables & Anti-Patterns

Extracted from the hypothesis and brief — apply across all tokens:

**Structural invariants** (must remain true in every expression):

**Explicit anti-patterns** (must never appear, regardless of context):

Source: `[02_foundational_brief.md — Section 10]` and `[04_active_hypothesis.md]`

---

### Inferred Tokens

List all tokens marked `[Inferred]` in this snapshot.

For each:
- The inferred rule
- What it was inferred from
- What would confirm or invalidate it

These should be reviewed and resolved before this snapshot is used for handoff.

---

### System Gaps

List every system area not yet defined — with no placeholder logic.

| Area | Status | Blocking? |
|---|---|---|
| | Not yet defined | Yes / No |

A gap is blocking if it must be resolved before another element can be correctly developed or before the system can be implemented.

---

## Human Handoff

When reviewing `design_tokens_snapshot.md`:

1. Are the inferred tokens correct? Confirm or remove each one.
2. Are the gaps blocking anything in your current work plan?
3. Does anything in the snapshot contradict your understanding of the system?
4. Is this snapshot complete enough to support handoff, or does more definition work need to happen first?

This document is only as accurate as the files it was extracted from. If the system has evolved beyond the current project files, update the source files before running this tool again.
