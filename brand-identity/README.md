# Brand Identity Methodology

This system defines how brand identity is developed from structural truth to scalable design system.

It is modular, repeatable, and machine-operable. It is designed to be run by a human and a machine together — the machine does analytical work, the human does creative work. There are explicit handoff points between them.

---

## How It Works

The process has three phases:

**Phase 0 — Setup.** Load the lens and declare the repository. Confirmations only. No outputs.

**Phase 1 — Extraction.** The machine reads the repository and produces a factual record. The lens is not active. No analysis, no interpretation, no design thinking. One human review point.

**Phase 2 — Foundation.** The lens activates. The machine applies it to the factual record to produce a structural brief. One human review point — this is the most important one.

**Phase 3 — Hypothesis.** Three structurally distinct directions are generated and ranked. One human decision point — you select the direction.

**Phase 4 — Lock.** The selected direction is compressed into a governing document. One human confirmation point — the structural position is fixed after this.

**Phase B — Modules.** Design exploration begins. Each module produces three concept directions with exploration briefs. You decide what to pursue. Modules can run in any order and can be rerun.

**Governance Tools.** Can be run at any point from Phase 4 onward to test alignment, stress-test a concept, or extract the current system state.

All outputs are single-file artefacts stored in `src/outputs/`.
All instructions live in `src/prompts/`.
No project memory carries across projects.

---

## Files & Folder Structure

```
src/repo/                        — Client materials (place all client files here)

src/resources/lenses/
  open-if-lens.md                — The analytical lens

src/prompts/00-foundation/
  00-reset.md                    — Declare clean slate and surface contamination risk
  01-lens-activation.md          — Load and activate the lens
  02-repo-declaration.md         — Declare and bind the repository
  03-kickoff-and-extraction.md   — Phase 1: factual extraction
  04-foundational-brief.md       — Phase 2: interrogation + brief
  05-hypothesis.md               — Phase 3: generate and rank hypotheses
  06-hypothesis-lock.md          — Phase 4: compress and lock the direction

src/prompts/01-system-modules/
  logo-concept.md
  typography-system.md
  color-system.md
  layout-system.md
  imagery-system.md
  ui-system.md

src/prompts/02-governance-tools/
  alignment-check.md
  sanity-gate.md
  token-snapshot.md

src/outputs/
  00-foundation/                 — All Phase 0–4 outputs live here
  01-systems/                    — All module outputs live here
  02-governance/                 — All governance outputs live here

src/import/                      — Staging folder for external work (see Working Externally)

delivery/                        — Client-facing deliverables
```

---

## Phase 0 — Setup

Run at the start of every new project. No outputs generated.

Place all client materials in `src/repo/` first, then type `start`.
→ Runs `00-reset.md`, `01-lens-activation.md`, and `02-repo-declaration.md` in sequence.
→ Declares clean slate. Surfaces any prior session context, external knowledge, or pattern transfer risk.
→ Confirms the lens is loaded and the repo is bound.
→ If prior project material is present in the session: start a new conversation before proceeding.

---

## Phase 1 — Extraction

**Step 4.**
Type `next`.
→ Machine reads all files in `src/repo/` and completes the extraction schema.
→ Every claim is cited. No analysis. No lens.
→ Output: `01_repo_extraction.md`

**→ Human review.**
Read the extraction. You are checking discipline, not domain accuracy:
- Does each claim have a citation?
- Does anything read like analysis rather than documentation?
- Is the coverage assessment honest?

Check the sparse repo flag at the end. If 6+ sections are not evidenced, consider pausing to request more material before proceeding.

---

## Phase 2 — Foundation

**Step 5.**
Type `next`.
→ Lens activates here for the first time.
→ Machine runs in two stages: structural interrogation, then brief.
→ Both stages appear in the output — the reasoning is visible.
→ Output: `02_foundational_brief.md`

**→ Human review.**
This is the most significant review point. You are engaging with the structural argument:
- Does Stage 1 show its reasoning or jump to conclusions?
- Do the brief sections follow logically from Stage 1?
- Do the active tensions feel real?
- Does the central position follow from the evidence or feel invented?
- Are the identity gate questions real constraints?

If the brief cannot pass this review, identify which sections need revisiting before proceeding.

---

## Phase 3 — Hypothesis

**Step 6.**
Type `next`.
→ Three structurally distinct directions generated and ranked.
→ Each is pressure-tested against the identity gate automatically.
→ Output: `03_hypotheses_ranked.md`

**→ Human decision.**
This is the primary creative decision point. Review the ranking, challenge it if needed, and confirm your selected direction — or introduce a new one. You are not obligated to follow the recommendation.

---

## Phase 4 — Hypothesis Lock

**Step 7.**
State your selected direction, then type `next`.
→ Selected direction compressed and formalised into the governing document.
→ Output: `04_active_hypothesis.md`

**→ Human confirmation.**
Review the lock document carefully. Once confirmed, the structural position governs all downstream work. Correct anything now — not after modules begin.

---

## Phase B — System Modules

Run after hypothesis lock. Modules can run in any order and can be rerun at any version.

For each module:
1. Type `run [module]` — e.g. `run logo`, `run typography`
2. Review the three concept directions and exploration briefs
3. Select your direction and begin design exploration

| Module | Command | Output |
|---|---|---|
| Logo | `run logo` | `logo_concepts_vX.md` |
| Typography | `run typography` | `typography_concepts_vX.md` |
| Colour | `run colour` | `colour_concepts_vX.md` |
| Layout | `run layout` | `layout_concepts_vX.md` |
| Imagery | `run imagery` | `imagery_concepts_vX.md` |
| UI Behaviour | `run ui` | `ui_behaviour_concepts_vX.md` |

---

## Governance Tools

Run at any point from Phase 4 onward. Can be used as often as needed.

**Alignment Check** — Structural audit across two or more system elements. Detects drift, contradiction, and weakening of the hypothesis. Run before presenting work or after adding a new element.
→ Type `alignment check`
→ Output: `alignment_review.md`

**Sanity Gate** — Rapid stress test of a single concept or decision. Faster than a full alignment check. Run in the moment when something feels uncertain.
→ Type `sanity gate [item being tested]`
→ Output: `sanity_check.md`

**Token Snapshot** — Extracts the current system state into structured tokens. Can be run at concept level (structural rules) or execution level (actual values). Do not run before at least two or three modules are developed.
→ Type `token snapshot`
→ Output: `design_tokens_snapshot.md`

---

## Working Externally

Any phase or module can be run outside this process — in another LLM, by a colleague, or manually. The `export` and `import` commands handle the transfer.

**To send work out:**
Type `export [target]`. This compiles the relevant prompt and its dependencies into a single file at `src/import/export_[target].md`. Take that file to your external tool, run it, and save the result back to `src/import/` using the expected output filename.

**To bring work back in:**
Save the external output to `src/import/` named as the expected output file (e.g., `03_hypotheses_ranked.md`), then type `import`. The system reads every file in `src/import/`, confirms any conflicts before overwriting, and reports which downstream files may be stale.

| Export target | Expected return filename |
|---|---|
| `export phase1` | `01_repo_extraction.md` |
| `export phase2` | `02_foundational_brief.md` |
| `export phase3` | `03_hypotheses_ranked.md` |
| `export phase4` | `04_active_hypothesis.md` |
| `export logo` | `logo_concepts_v[n].md` |
| `export typography` | `typography_concepts_v[n].md` |
| `export colour` | `colour_concepts_v[n].md` |
| `export layout` | `layout_concepts_v[n].md` |
| `export imagery` | `imagery_concepts_v[n].md` |
| `export ui` | `ui_behaviour_concepts_v[n].md` |
| `export alignment` | `alignment_review.md` |
| `export sanity [item]` | `sanity_check.md` |
| `export tokens` | `design_tokens_snapshot.md` |

**Note on foundational files.** If you replace `02_foundational_brief.md` or `04_active_hypothesis.md` via import, all downstream outputs may be stale. The import command will warn you and list what is affected.

---

## When to Return to Phase A

Return to Phase 2 (brief) or earlier if:
- Alignment Check classifies risk as Structural Breakdown
- Multiple modules contradict the organising principle
- A concept cannot pass the Identity Gate without qualification
- The hypothesis lock no longer feels true to the entity

Return to Phase 1 (extraction) if:
- New repository material becomes available that materially changes the factual record
- The brief reveals that key information was missing from the original extraction

---

## Operating Principles

- The lens governs analysis. The extraction governs facts. These are not the same operation.
- Every claim traces to a source. Every structural assertion traces to the brief.
- Extraction is factual. Interrogation is analytical. Design is creative. These phases do not bleed into each other.
- Tensions that cannot be resolved are carried forward explicitly. They are not smoothed over.
- Exclusion is as important as inclusion. A direction that cannot exclude alternatives is not strong enough.
- One prompt → one output file. No exceptions.
- The human decides. The machine analyses, generates, and recommends.

---

## Clean Slate Rule

Every project begins with:
- No inherited aesthetic decisions
- No transferred tone or structural logic from previous projects
- Only project files as source of truth

If prior knowledge influences any output, it must be labelled explicitly: `[External — not from project files]`

---

## Platform Note

This process runs in Claude Code. Each conversation starts with no session context from prior projects — there is no persistent cross-session memory to manage.

**Starting a new project:** start a new conversation and type `start`. That is the clean slate.

**Returning to a project in progress:** open the project in a new conversation and type `resume`. This reloads the lens, reads the existing outputs to restore context, and reports where the project is and what comes next. Do not type `start` — that is for new projects only.
