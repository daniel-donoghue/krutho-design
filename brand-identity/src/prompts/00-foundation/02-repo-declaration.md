# 02-repo-declaration.md

**Purpose:** Explicitly binds the project repository in `src/repo/` as the sole source of subject evidence and separates it from all other files in the session.
**When to Use:** After lens activation and before extraction.
**Dependencies:** Project repository files in `src/repo/`.
**Output:** Confirmation only (no file generated).

---

## Prompt

The files in `src/repo/` constitute the project repository.

This repository is the subject of the project. It defines the entity that will be extracted.

Confirm the following by responding to each point explicitly:

**1. Repository contents**
List every file in `src/repo/`. Do not summarise — list them individually.

**2. Source separation**
Confirm which files in this session are repository files and which are not. The session currently contains:
- The project repository (listed above)
- The Open If lens file
- Methodology and prompt files

State clearly which is which.

**3. Source rules**
Confirm:
- The repository files are the sole source of subject evidence.
- The lens file is analytical infrastructure, not subject content.
- Methodology and prompt files are operational instructions, not subject content.
- None of the non-repository files will be treated as evidence about the entity being extracted.

**4. Lens status**
Confirm that the lens is loaded but not yet active. It will not be applied until Phase 2.

Do not begin extraction.
Do not summarise any file contents.
Do not analyse anything.
Return the four confirmations above only.
