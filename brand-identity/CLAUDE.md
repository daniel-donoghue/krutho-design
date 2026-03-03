# Brand Identity Process — Claude Code Orchestration

This file governs how the brand identity process runs in Claude Code. Read it at the start of every project conversation.

Full process documentation: [`README.md`](README.md)

---

## Project Structure

```
src/repo/                          ← All client materials go here
src/resources/lenses/
  open-if-lens.md                  ← The analytical lens
src/prompts/00-foundation/         ← Phase 0–4 prompt files
src/prompts/01-system-modules/     ← Module prompt files
src/prompts/02-governance-tools/   ← Governance prompt files
src/outputs/00-foundation/         ← Phase 0–4 outputs
src/outputs/01-systems/            ← Module outputs
  [module]/                       ← One subfolder per module, created when the module is first run
    [module]_concepts_v[n].md     ← Claude-generated concept directions
    [module]_settled.md           ← Approved exploration outcome (human/collaborative)
    artifacts/                    ← Design artifacts: images, fonts, Keynotes, etc. (referenced, not ingested)
src/outputs/02-governance/         ← Governance outputs
src/outputs/decisions.md           ← Decision log (appended at each hard stop)
src/import/                        ← Staging folder: structured exports + exploration conversations
delivery/                          ← Client-facing deliverables
```

---

## State Detection

Before responding to any command, check which files exist in `src/outputs/`. This determines the current phase.

| State | Condition |
|---|---|
| **Not started** | No files in `src/outputs/` |
| **Phase 0 complete** | No output files (Phase 0 produces no files — infer from conversation) |
| **Phase 1 complete** | `src/outputs/00-foundation/01_repo_extraction.md` exists |
| **Phase 2 complete** | `src/outputs/00-foundation/02_foundational_brief.md` exists |
| **Phase 3 complete** | `src/outputs/00-foundation/03_hypotheses_ranked.md` exists |
| **Phase 4 complete** | `src/outputs/00-foundation/04_active_hypothesis.md` exists |
| **Modules in progress** | Subfolders exist in `src/outputs/01-systems/` |
| **Module settled** | `[module]_settled.md` exists in `src/outputs/01-systems/[module]/` |

Report the detected state to the user before executing anything.

---

## Commands

### `help`

Read [`COMMANDS.md`](COMMANDS.md) and display its contents to the user.

---

### `log`

Read `src/outputs/decisions.md` and display its contents. If the file does not exist, tell the user no decisions have been recorded yet.

---

### `resume`

Use when returning to an in-progress project. Does not run reset or contamination checks — those are for new projects only.

1. Read `src/resources/lenses/open-if-lens.md` — the lens has no persistent memory and must be reloaded each session.
2. Scan `src/outputs/` to detect current phase.
3. Read the governing documents that exist, in order:
   - `src/outputs/decisions.md` if it exists — this gives decision context the output files alone do not contain
   - `src/outputs/00-foundation/04_active_hypothesis.md` if it exists
   - `src/outputs/00-foundation/02_foundational_brief.md` if it exists
   - Any `*_settled.md` files in `src/outputs/01-systems/[module]/` — these carry confirmed structural properties from completed modules
   - The most recent concepts file in `src/outputs/01-systems/[module]/` if any exist
4. Report the current state:
   - Which phase the project is at
   - What outputs have been written
   - Which modules have concepts only vs. a settled record
   - What the last human decision point was and whether it was confirmed
   - What any open module directions are (if concepts exist but module is not yet settled)
   - What the next step is
5. Ask the user what they want to do.

**Do not run any phase or module automatically on resume.** Orient first, act on instruction.

---

### `start` or `new project`

**Before doing anything else:** check whether files exist in `src/outputs/`.

- If files exist: stop. Tell the user which output files are present and that a project is already in progress. Ask: **Resume existing project or start fresh?**
  - If resume: run the `resume` command instead.
  - If start fresh: tell the user to manually clear `src/outputs/` first, then type `start` again. Do not delete files on their behalf.
- If no output files exist: proceed with Phase 0 below.

Run Phase 0 setup. No output files are generated.

1. Read and execute [`src/prompts/00-foundation/00-reset.md`](src/prompts/00-foundation/00-reset.md) — surfaces contamination risk. **Stop and surface findings for human review before continuing.**
2. Read and execute [`src/prompts/00-foundation/01-lens-activation.md`](src/prompts/00-foundation/01-lens-activation.md) — reads `src/resources/lenses/open-if-lens.md` and confirms the lens is loaded.
3. Read and execute [`src/prompts/00-foundation/02-repo-declaration.md`](src/prompts/00-foundation/02-repo-declaration.md) — confirms the repo is bound.

Phase 0 is complete when all three steps are confirmed. Tell the user to say `next` to begin extraction.

---

### `next` or `continue`

Detects the current state and runs the next phase. Follows the sequence below. Do not skip phases.

**If Phase 0 complete → run Phase 1:**
Read and execute [`src/prompts/00-foundation/03-kickoff-and-extraction.md`](src/prompts/00-foundation/03-kickoff-and-extraction.md).
Write output to `src/outputs/00-foundation/01_repo_extraction.md`.
**Hard stop:** surface the reviewer sense check questions from the prompt. Wait for confirmation before proceeding.

**If Phase 1 complete → run Phase 2:**
Read and execute [`src/prompts/00-foundation/04-foundational-brief.md`](src/prompts/00-foundation/04-foundational-brief.md).
Write output to `src/outputs/00-foundation/02_foundational_brief.md`.
**Hard stop:** surface the human review questions from the prompt. This is the most significant review point. Wait for confirmation before proceeding.

**If Phase 2 complete → run Phase 3:**
Read and execute [`src/prompts/00-foundation/05-hypothesis.md`](src/prompts/00-foundation/05-hypothesis.md).
Write output to `src/outputs/00-foundation/03_hypotheses_ranked.md`.
**Hard stop:** ask the user to select a direction (or introduce a new one) before proceeding.

**If Phase 3 complete → run Phase 4:**
The user must have selected a direction. State it clearly when executing.
Read and execute [`src/prompts/00-foundation/06-hypothesis-lock.md`](src/prompts/00-foundation/06-hypothesis-lock.md).
Write output to `src/outputs/00-foundation/04_active_hypothesis.md`.
**Hard stop:** ask the user to confirm the lock document. Once confirmed, structural position is fixed.

**If Phase 4 complete:**
Modules are available. Tell the user which modules can be run and ask which to start.

---

### `review [target]`

Re-engages with an existing output without regenerating it. Use when you want to re-read, question, and re-confirm a phase — not start it again from scratch.

**Targets:** `phase1`, `phase2`, `phase3`, `phase4`

1. Read the target output file.
2. Read the review/decision questions from the corresponding prompt file (the "Human review" or "Human decision" section).
3. Surface those questions to the user and invite discussion.
4. When the user confirms, append a "re-reviewed" entry to `src/outputs/decisions.md`.

**If the target does not exist:** tell the user the output has not been generated yet.

**Review does not overwrite anything.** It is a re-engagement with work that already exists. If the discussion reveals something that needs to change, use `rerun [target]` to regenerate.

---

### `rerun [target]`

Regenerates an output from scratch using the corresponding prompt. Use when the existing output needs to be replaced — not just re-read.

**Targets:** `phase1`, `phase2`, `phase3`, `phase4`, or any module name

**Before regenerating:**
1. Read the existing output file and display its section headers.
2. State which downstream files will potentially become stale (use the dependency map below).
3. Ask: **Regenerate and overwrite / Cancel.**
4. If cancel: stop. If regenerate: proceed.

**Regenerate:**
- Run the corresponding prompt (same as `next` would run for that phase, or `run [module]` for modules).
- Overwrite the canonical output file.
- Append a "rerun" entry to `src/outputs/decisions.md` — include the reason if the user provides one.
- Report which downstream files are now potentially stale and what action the user should consider.

**Modules** already version by default (`_v1`, `_v2`). `rerun [module]` increments the version rather than overwriting — consistent with existing module behaviour.

**Staleness map for phase reruns:**

| Rerun target | Potentially stale downstream |
|---|---|
| `phase1` | `02_foundational_brief.md`, `03_hypotheses_ranked.md`, `04_active_hypothesis.md`, all module outputs |
| `phase2` | `03_hypotheses_ranked.md`, `04_active_hypothesis.md`, all module outputs |
| `phase3` | `04_active_hypothesis.md` |
| `phase4` | All module outputs |

After a phase rerun, the user must decide whether to rerun downstream phases or proceed with existing outputs. Do not rerun anything downstream automatically.

---

### `run [module]`

Available after Phase 4. Modules can run in any order and can be rerun.

| Command | Prompt file | Output file |
|---|---|---|
| `run logo` | [`src/prompts/01-system-modules/logo-concept.md`](src/prompts/01-system-modules/logo-concept.md) | `src/outputs/01-systems/logo/logo_concepts_v[n].md` |
| `run typography` | [`src/prompts/01-system-modules/typography-system.md`](src/prompts/01-system-modules/typography-system.md) | `src/outputs/01-systems/typography/typography_concepts_v[n].md` |
| `run colour` or `run color` | [`src/prompts/01-system-modules/color-system.md`](src/prompts/01-system-modules/color-system.md) | `src/outputs/01-systems/colour/colour_concepts_v[n].md` |
| `run layout` | [`src/prompts/01-system-modules/layout-system.md`](src/prompts/01-system-modules/layout-system.md) | `src/outputs/01-systems/layout/layout_concepts_v[n].md` |
| `run imagery` | [`src/prompts/01-system-modules/imagery-system.md`](src/prompts/01-system-modules/imagery-system.md) | `src/outputs/01-systems/imagery/imagery_concepts_v[n].md` |
| `run ui` | [`src/prompts/01-system-modules/ui-system.md`](src/prompts/01-system-modules/ui-system.md) | `src/outputs/01-systems/ui/ui_behaviour_concepts_v[n].md` |

Version suffix: check `src/outputs/01-systems/[module]/` for existing files. Increment `v[n]` on rerun.

**Before reading the module prompt:** scan `src/outputs/01-systems/` subfolders for any `*_settled.md` files from other modules. If any exist, read them. Treat confirmed structural properties from settled modules as additional source context — this module must respect constraints set by modules that have already been resolved. Cite settled records explicitly in the output alongside `02_foundational_brief.md` and `04_active_hypothesis.md`.

After writing the output: surface the human handoff questions from the prompt. Wait for the user to select a direction. Once a direction is selected, tell the user to run `settle [module]` to record the exploration outcome before moving to the next module.

---

### `settle [module]`

Available after a module has been run. Records the outcome of the design exploration phase — direction selected, structural properties confirmed through exploration, artifacts produced, and constraints for downstream modules. Produces `src/outputs/01-systems/[module]/[module]_settled.md`.

The settled record is the authoritative outcome of a module. It is what downstream modules read — not the concepts file.

**Before settling:**

1. Check that `[module]_concepts_v[n].md` exists in `src/outputs/01-systems/[module]/`. If not, tell the user to run the module first.
2. Read the most recent concepts file for that module.
3. Check `src/import/` for any files that do not match known structured output filenames (see import section). These are treated as exploration conversations.

**If exploration conversations are found in `src/import/`:**

4. Read each file in full.
5. Extract signal by category:
   - **Decisions made** — what was confirmed or rejected, and why if stated
   - **Structural properties confirmed** — things that are now fixed as a result of exploration
   - **Directions explored and abandoned** — with brief reason if available
   - **Artifacts referenced** — any files, tools, or outputs mentioned
   - **Open questions raised** — anything unresolved that may affect downstream modules
6. Present a summary per file: what was found, how each item is categorised, what is recommended for inclusion in the settled record.
7. The user approves, corrects, or discards items. **Do not assimilate anything without explicit approval.**
8. Carry only the distilled, approved extract forward. Do not reproduce conversation content verbatim.

**Then, for all settle operations:**

9. Ask the user:
   - Which concept direction was selected or developed from?
   - What structural properties are now confirmed through exploration? (What is fixed that wasn't before?)
   - What artifacts exist — and where are they? (Default location: `src/outputs/01-systems/[module]/artifacts/`, but record whatever path the user provides.)
   - What constraints or signals does this module send to downstream modules — what must they respect?
   - Any additional notes from the design process worth recording?

10. Synthesise all approved information into `src/outputs/01-systems/[module]/[module]_settled.md`:

```markdown
# [Module] — Settled

> [Produced via settle command — approved by human]

## Direction Selected
[Which concept from [module]_concepts_v[n].md, or description of what was developed from it]

## Structural Properties Confirmed
[Properties determined through exploration that are now fixed]
[These are authoritative inputs for downstream modules]

## Artifacts
[List of files with paths and brief descriptions — images, fonts, Keynotes, renders, etc.]
[Conversations digested: [filenames] — approved extract only, not verbatim content]

## Constraints for Downstream Modules
[Explicit signals this module sends forward — what subsequent modules must not contradict]

## Notes
[Any additional context from the design process worth preserving]
```

11. Ask "Would you like to note your reasoning for this decision?" then append an entry to `src/outputs/decisions.md`.
12. Delete processed exploration conversation files from `src/import/` after the settled record is written and approved. Confirm with the user before deleting.

---

### Governance tools

Available any time after Phase 4.

**`alignment check`**
Read and execute [`src/prompts/02-governance-tools/alignment-check.md`](src/prompts/02-governance-tools/alignment-check.md).
Write output to `src/outputs/02-governance/alignment_review.md`.
Surface the human handoff questions after writing.

**`sanity gate [item]`**
Read and execute [`src/prompts/02-governance-tools/sanity-gate.md`](src/prompts/02-governance-tools/sanity-gate.md).
Write output to `src/outputs/02-governance/sanity_check.md`.
The verdict is one of: Proceed / Refine / Rework / Revisit hypothesis.

**`token snapshot`**
Read and execute [`src/prompts/02-governance-tools/token-snapshot.md`](src/prompts/02-governance-tools/token-snapshot.md).
Write output to `src/outputs/02-governance/design_tokens_snapshot.md`.
Do not run before at least two or three modules are developed.

---

### `export [target]`

Compiles a prompt and its dependencies into a single file in `src/import/` for use in an external LLM or manual workflow.

After writing the file, tell the user: "When you have the output, save it as `[expected filename]` in `src/import/` and type `import`."

| Command | Bundles | Expected return filename |
|---|---|---|
| `export phase1` | `03-kickoff-and-extraction.md` only — note that `src/repo/` files must be uploaded separately | `01_repo_extraction.md` |
| `export phase2` | `04-foundational-brief.md` + `01_repo_extraction.md` | `02_foundational_brief.md` |
| `export phase3` | `05-hypothesis.md` + `02_foundational_brief.md` | `03_hypotheses_ranked.md` |
| `export phase4` | `06-hypothesis-lock.md` + `03_hypotheses_ranked.md` + `02_foundational_brief.md` | `04_active_hypothesis.md` |
| `export logo` | `logo-concept.md` + `04_active_hypothesis.md` + `02_foundational_brief.md` | `logo_concepts_v[n].md` |
| `export typography` | `typography-system.md` + `04_active_hypothesis.md` + `02_foundational_brief.md` | `typography_concepts_v[n].md` |
| `export colour` | `color-system.md` + `04_active_hypothesis.md` + `02_foundational_brief.md` | `colour_concepts_v[n].md` |
| `export layout` | `layout-system.md` + `04_active_hypothesis.md` + `02_foundational_brief.md` | `layout_concepts_v[n].md` |
| `export imagery` | `imagery-system.md` + `04_active_hypothesis.md` + `02_foundational_brief.md` | `imagery_concepts_v[n].md` |
| `export ui` | `ui-system.md` + `04_active_hypothesis.md` + `02_foundational_brief.md` | `ui_behaviour_concepts_v[n].md` |
| `export alignment` | `alignment-check.md` + `04_active_hypothesis.md` + `02_foundational_brief.md` + all files in `src/outputs/01-systems/` (all module subfolders) | `alignment_review.md` |
| `export sanity [item]` | `sanity-gate.md` + `04_active_hypothesis.md` + `02_foundational_brief.md` | `sanity_check.md` |
| `export tokens` | `token-snapshot.md` + `04_active_hypothesis.md` + all files in `src/outputs/01-systems/` (all module subfolders) | `design_tokens_snapshot.md` |

**Compiled file format.** Write to `src/import/export_[target].md` using this structure:

```
# Export: [target]
Expected output filename: [filename]

---

The following files are inputs to this task. Read them in full before proceeding.

## [filename]

[full file content]

---

## [next filename]

[full file content]

---

## Task

[full prompt file content]
```

---

### `import`

Reads all files in `src/import/` (excluding files prefixed `export_`) and incorporates structured output files into `src/outputs/`.

**`import` handles structured output files only** — files whose names match known output filenames. Exploration conversations, external LLM transcripts, and other unstructured files dropped in `src/import/` are processed by `settle [module]`, not `import`. If an unrecognised file is found, tell the user: "This file doesn't match a known output filename. If it's an exploration conversation, run `settle [module]` — it will read `src/import/` automatically."

**For each structured file found:**

1. Match filename to a destination in `src/outputs/`:
   - Foundation files (`01_repo_extraction.md`, `02_foundational_brief.md`, `03_hypotheses_ranked.md`, `04_active_hypothesis.md`) → `src/outputs/00-foundation/`
   - Module files → `src/outputs/01-systems/[module]/` (match by filename prefix to determine the module subfolder)
   - Governance files → `src/outputs/02-governance/`
   - Unrecognised filename: ask the user to confirm the destination before proceeding.

2. If destination does not exist: write the file, delete from `src/import/`, confirm.

3. If destination exists:
   - State what already exists and what is incoming (section headers of each).
   - If this is a foundational file (`02_foundational_brief.md` or `04_active_hypothesis.md`): warn that replacing it may make downstream outputs stale.
   - Ask: **Replace / Create as new version / Skip.**
   - Act on the user's choice. Delete from `src/import/` only after Replace or Skip.

4. Add this header to every imported file: `> [Imported — generated outside this process]`

5. After all files processed: report which downstream files may now be stale.

**Dependency impact map:**

| Imported file | May make these stale |
|---|---|
| `01_repo_extraction.md` | `02_foundational_brief.md` and all downstream |
| `02_foundational_brief.md` | `03_hypotheses_ranked.md`, `04_active_hypothesis.md`, all module outputs |
| `03_hypotheses_ranked.md` | `04_active_hypothesis.md` |
| `04_active_hypothesis.md` | All module outputs |
| Any module output | Governance outputs |

---

## Execution Rules

- **Read the prompt file before executing it.** Every prompt contains rules that govern the operation. The schema, source discipline, and output structure are all in the prompt.
- **One output file per prompt.** Write the full output to the specified path. No exceptions.
- **Hard stops are non-negotiable.** Do not advance past a human decision point without explicit confirmation.
- **Never proceed to Phase 2 if the extraction is not confirmed.** Never proceed to Phase 3 if the brief is not confirmed. Never begin modules if the hypothesis is not locked.
- **Source discipline applies to all outputs.** Every claim must cite a source file. Any external knowledge must be labelled `[External — not from project files]`.
- **Do not interpret the hypothesis.** Only cite it.

---

## Hard Stops — Summary

| After | Stop and ask |
|---|---|
| Phase 0 (reset) | Confirm contamination declarations before proceeding to lens activation |
| Phase 1 output | Confirm extraction passes the reviewer sense check |
| Phase 2 output | Confirm the structural brief before generating hypotheses |
| Phase 3 output | User selects a direction |
| Phase 4 output | User confirms the lock document |
| Each module | User selects a direction from the three concepts |

---

## Decision Recording

At every hard stop, after the human confirms their decision, append an entry to `src/outputs/decisions.md`. Create the file if it does not exist.

**At minor confirmations** (Phase 0 reset, Phase 1 extraction, Phase 4 lock): record the decision without prompting for reasoning unless the human volunteers it.

**At significant decisions** (Phase 2 brief, Phase 3 direction, each module direction): ask "Would you like to note your reasoning for this decision?" before writing the entry. Record whatever they provide — or leave the Notes field blank if they decline.

**Entry format:**

```markdown
## [Context] — [Decision type]

**Date:** [YYYY-MM-DD]
**Decision:** [What was confirmed or selected]
**Alternatives:** [What was not chosen, if applicable]
**Notes:** [Human's reasoning, if provided]

---
```

**What to record at each stop:**

| Stop | Decision field | Alternatives field |
|---|---|---|
| Phase 0 — Reset confirmed | "Contamination check passed. Proceeding." | — |
| Phase 1 — Extraction confirmed | "Confirmed" or "Confirmed with flags: [list]" | — |
| Phase 2 — Brief confirmed | "Confirmed" or "Confirmed — [sections challenged and resolved]" | — |
| Phase 3 — Direction selected | Direction name and one-line description | The directions not selected and the ranking |
| Phase 4 — Lock confirmed | "Confirmed. Structural position fixed." | — |
| Module — Direction selected | Concept name and one-line description | The concepts not selected |
| Module — Settled | Direction + key structural properties confirmed | Concepts not selected; exploration paths abandoned |
| Import — Conflict resolved | "Replaced / Created as v[n] / Skipped: [filename]" | — |
