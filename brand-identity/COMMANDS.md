# Command Reference

## Session

| Command | When to use | What it does |
|---|---|---|
| `start` | New project, no prior outputs | Runs Phase 0: reset, lens activation, repo declaration |
| `resume` | Returning to a project in progress | Reloads lens, reads existing outputs and decision log, reports current state |
| `log` | Any time | Shows the decision log — every confirmed decision with reasoning |
| `help` | Any time | Shows this command reference |

---

## Process

| Command | Phase | What it does |
|---|---|---|
| `next` | After Phase 0, 1, 2, or 3 | Detects current state and runs the next phase |
| `next` | After Phase 3 | Locks the selected direction — state your direction first |
| `review [target]` | Any time after a phase exists | Re-reads the output, surfaces review questions, allows re-confirmation. No regeneration. |
| `rerun [target]` | Any time after a phase exists | Regenerates the output from scratch. Warns about staleness before overwriting. |

Phases in order:
1. Extraction → `01_repo_extraction.md`
2. Foundation → `02_foundational_brief.md`
3. Hypothesis → `03_hypotheses_ranked.md`
4. Lock → `04_active_hypothesis.md`

Each phase has a human review or decision point before `next` will advance.

Review targets: `phase1` `phase2` `phase3` `phase4`
Rerun targets: `phase1` `phase2` `phase3` `phase4` + any module name

---

## Modules

Run after hypothesis lock. Any order. Rerunnable.

| Command | Output |
|---|---|
| `run logo` | `logo_concepts_v[n].md` |
| `run typography` | `typography_concepts_v[n].md` |
| `run colour` | `colour_concepts_v[n].md` |
| `run layout` | `layout_concepts_v[n].md` |
| `run imagery` | `imagery_concepts_v[n].md` |
| `run ui` | `ui_behaviour_concepts_v[n].md` |

After selecting a direction from a module, drop any exploration materials into `src/import/` and `src/outputs/01-systems/[module]/artifacts/`, then run:

| Command | Output |
|---|---|
| `settle logo` | `logo_settled.md` |
| `settle typography` | `typography_settled.md` |
| `settle colour` | `colour_settled.md` |
| `settle layout` | `layout_settled.md` |
| `settle imagery` | `imagery_settled.md` |
| `settle ui` | `ui_behaviour_settled.md` |

`settle [module]` digests any exploration conversations in `src/import/`, asks structured questions about what was confirmed, and writes the approved outcome. The settled record is what downstream modules read.

---

## Governance

Run any time after Phase 4.

| Command | What it does | Output |
|---|---|---|
| `alignment check` | Structural audit across all developed elements | `alignment_review.md` |
| `sanity gate [item]` | Rapid stress test of a single concept or decision | `sanity_check.md` |
| `token snapshot` | Extracts current system state into structured tokens — not before 2–3 modules exist | `design_tokens_snapshot.md` |

---

## External Workflow

| Command | What it does |
|---|---|
| `export [target]` | Compiles prompt + dependencies into `src/import/export_[target].md` for use in another LLM or manual workflow |
| `import` | Reads structured output files in `src/import/`, incorporates into `src/outputs/`, surfaces conflicts for confirmation |

Export targets: `phase1` `phase2` `phase3` `phase4` `logo` `typography` `colour` `layout` `imagery` `ui` `alignment` `sanity [item]` `tokens`

After export: save the result back to `src/import/` with the expected output filename, then type `import`.

**`import` handles structured output files only.** For exploration conversations and external LLM transcripts, use `settle [module]` — it reads `src/import/` automatically and digests unstructured content with approval before assimilating.
