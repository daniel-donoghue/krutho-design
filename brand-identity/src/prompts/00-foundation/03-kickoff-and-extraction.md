# 03-kickoff-and-extraction.md

**Purpose:** Extracts a factual, citation-grounded inventory of the subject entity from the project repository. This is a documentary operation only — no analysis, no interpretation, no lens.
**When to Use:** After lens activation and repo declaration. Before any brief or strategy work.
**Dependencies:** Project repository (declared in 02-repo-declaration.md).
**Output:** `01_repo_extraction.md`

---

## Pre-Extraction Rules

Read these before beginning. They govern the entire operation.

**The lens is not active during extraction.**
Do not apply Pentagram lens vocabulary, frameworks, or questions at any point in this stage.
Concepts such as "structural tension", "organising principle", "durability", and "authority model" are lens concepts. They do not belong here.

**The repository is the only permitted source.**
Do not supplement with external knowledge about the company, its industry, or its competitors.
If something is generally known about this company but not stated in the repository, it does not appear in this document.
If prior knowledge influences a claim, mark it explicitly: `[External — not from repo]`

**Every claim requires a source citation.**
Citation format: `[Filename, section or page if available, direct quote or close paraphrase]`
If a claim cannot be cited, it does not belong in this document.

**No interpretation.**
Record what the repository says, not what it might mean.
Do not infer intent, imply positioning, or read between lines.
If something is ambiguous in the repo, record it as ambiguous — do not resolve it.

**No inference labelling as a workaround.**
The previous version of this process used "label as inference" as a permission structure. That permission no longer exists at this stage. Inference moves to Phase 2. If it is not stated in the repo, it is not recorded here.

---

## Instruction

Read all files in `src/repo/` before completing any section.

Then complete each section of the schema below using only what the repository explicitly states.

Where a section has no relevant content in the repository, write: `Not evidenced in repository.`

Do not skip sections. Gaps are data.

Produce a single file: `src/outputs/00-foundation/01_repo_extraction.md`

---

## Extraction Schema

---

### Section 1 — Entity Basics

The fundamental facts about what this is.

| Field | Extracted Content | Source Citation |
|---|---|---|
| Entity name | | |
| Entity type (company, product, platform, service, etc.) | | |
| One-sentence functional description (their words, not yours) | | |
| Year founded / operational since | | |
| Geography (HQ, markets served) | | |
| Company stage (startup, scale-up, enterprise, etc.) | | |
| Headcount or size indicators | | |
| Ownership / funding status | | |

---

### Section 2 — What It Does

How the entity functions. Focus on mechanism, not marketing.

| Field | Extracted Content | Source Citation |
|---|---|---|
| Core function (what it does at the most basic level) | | |
| How it works (mechanism or process, stated) | | |
| Key features or capabilities (list each separately) | | |
| Technology or infrastructure (if described) | | |
| Delivery model (SaaS, service, physical, hybrid, etc.) | | |
| Integrations or dependencies (stated) | | |

---

### Section 3 — Who It Serves

Audiences, customers, and users as described in the repository.

| Field | Extracted Content | Source Citation |
|---|---|---|
| Primary audience (stated) | | |
| Secondary audiences (stated) | | |
| Audience descriptors used (job titles, industries, contexts) | | |
| Stated customer pain points or needs | | |
| Stated customer outcomes or benefits | | |
| Any named customers or case studies | | |

---

### Section 4 — What It Claims

Value propositions, differentiators, and positioning statements as the repo states them. Record exact language where possible.

| Field | Extracted Content | Source Citation |
|---|---|---|
| Primary value proposition (their words) | | |
| Secondary value propositions | | |
| Stated differentiators ("unlike X, we...") | | |
| Stated competitive positioning | | |
| Claims about category or market leadership | | |
| Any guarantees, SLAs, or performance claims | | |

---

### Section 5 — Market & Industry Context

What the repo says about where this entity operates.

| Field | Extracted Content | Source Citation |
|---|---|---|
| Industry or sector (stated) | | |
| Market size or opportunity (if stated) | | |
| Named competitors (if stated) | | |
| Regulatory or compliance context (if stated) | | |
| Market trends referenced | | |
| Category language used to describe themselves | | |

---

### Section 6 — Business Direction

Stated goals, plans, and strategic intent.

| Field | Extracted Content | Source Citation |
|---|---|---|
| Stated mission | | |
| Stated vision | | |
| Stated values (list each) | | |
| Short-term goals (stated) | | |
| Long-term ambitions (stated) | | |
| Growth or expansion plans (stated) | | |
| Any stated pivots or changes in direction | | |

---

### Section 7 — Existing Brand & Visual Identity

What the repo contains about the current brand expression.

| Field | Extracted Content | Source Citation |
|---|---|---|
| Current brand name(s) in use | | |
| Logo or mark (described or present) | | |
| Colour palette (stated or present) | | |
| Typography (stated or present) | | |
| Existing brand guidelines or rules | | |
| Brand history or previous identities | | |
| Brand assets provided (list files) | | |
| Any stated brand problems or dissatisfactions | | |

---

### Section 8 — Language & Communication

How the entity writes and speaks. Record directly — do not editorialize.

**Repeated phrases or slogans** (list with citation for each):

**Key terms or vocabulary unique to this entity** (list with citation):

**Tone descriptors used in the repo** (how they describe their own voice):
| Descriptor | Citation |
|---|---|
| | |

**Sample language** — select 5–8 representative passages that best illustrate how this entity communicates. Choose variety: headlines, body copy, product descriptions, about page, etc.

| Passage | Source |
|---|---|
| | |

**Inconsistencies in language** — where the repo uses conflicting terms, tones, or descriptions for the same thing. Record without interpretation:
| Inconsistency observed | Source A | Source B |
|---|---|---|
| | | |

---

### Section 9 — People & Culture

What the repo says about the team, founders, and internal culture.

| Field | Extracted Content | Source Citation |
|---|---|---|
| Named founders or leadership | | |
| Founder background or credentials (stated) | | |
| Team size or composition (stated) | | |
| Culture descriptors (stated) | | |
| Hiring or talent positioning | | |

---

### Section 10 — Project-Specific Context

Anything the repo states about this engagement specifically, if applicable.

| Field | Extracted Content | Source Citation |
|---|---|---|
| Stated brief or design requirements | | |
| Stated deliverables expected | | |
| Stated timeline or constraints | | |
| Stated stakeholders or decision-makers | | |
| Previous agency or design work referenced | | |
| Any stated reasons for rebrand or new identity | | |

---

## Coverage Assessment

Complete this after all sections are filled.

Rate each section:

- **Well Evidenced** — multiple sources, clear and consistent information
- **Partially Evidenced** — some information present, gaps exist
- **Not Evidenced** — no relevant content found in repository

| Section | Coverage Rating | Notes on Gaps |
|---|---|---|
| 1. Entity Basics | | |
| 2. What It Does | | |
| 3. Who It Serves | | |
| 4. What It Claims | | |
| 5. Market & Industry | | |
| 6. Business Direction | | |
| 7. Brand & Visual Identity | | |
| 8. Language & Communication | | |
| 9. People & Culture | | |
| 10. Project-Specific Context | | |

---

### Sparse Repo Flag

Count the number of sections rated "Not Evidenced" or "Partially Evidenced".

**0–2 gaps:** Proceed to Phase 2.

**3–5 gaps:** Flag to reviewer. Proceed with caution. Gaps will carry forward as explicit unknowns into the brief.

**6+ gaps:** Recommend pausing. The repository does not contain sufficient material to support a well-grounded brief. Note which sections are missing and recommend what additional material should be requested before Phase 2 begins.

State the flag level clearly at the top of the Coverage Assessment.

---

## What This Document Is Not

This document does not contain:

- Strategic recommendations
- Positioning statements
- Design directions
- Tensions or contradictions (analysis moves to Phase 2)
- Inferences or implications
- Lens-derived observations of any kind

If any of the above appear in this document, they must be removed before Phase 2 begins.

---

## Reviewer Sense Check (for human review)

When reviewing this document, you are checking:

1. Does each claim have a citation?
2. Does anything read like analysis rather than documentation?
3. Does anything seem invented or inconsistent with the repo?
4. Are any significant gaps visible that aren't flagged?
5. Is the coverage assessment honest?

You do not need domain expertise to do this. You are checking the machine's discipline, not the accuracy of the subject matter.

If something looks wrong, flag it before proceeding to Phase 2.
