# 00-reset.md

**Purpose:** Establishes a clean starting condition before a new project begins. Surfaces any prior context the model is carrying so you can assess contamination risk before running setup.
**When to Use:** At the very start of every new project, before lens activation.
**Dependencies:** None.
**Output:** Confirmation and declaration only. No file generated.

---

## Before Running This Prompt

This process runs in Claude Code. There is no persistent cross-session memory to manage — each conversation starts fresh.

The clean slate requirement is simple: start a new conversation for each project. Do not run this process in a conversation that already contains prior project material from a different client.

Residual contamination risks — external knowledge and pattern transfer — are addressed by the declarations below.

---

## What Contaminates a Project

There are three forms of contamination that can affect downstream work:

**Session context.** Prior outputs from another project are present in this conversation. The model has read them. This is the strongest form of contamination. The correct response is to start a new conversation. A prompt cannot fully clear material the model has already processed.

**External knowledge.** If the brand being worked on is a known public entity, the model carries knowledge of it from training — its existing identity, its market position, how it is publicly discussed. This cannot be cleared. It is mitigated by the extraction discipline: the repository is the only permitted source, and any external knowledge that surfaces must be labelled explicitly.

**Pattern transfer.** Structural decisions made recently — the type of organising principle chosen, how tensions were framed, what hypothesis structure felt like "a good answer" — can create implicit defaults that shape how the next project is approached. This is the subtlest form and the hardest to eliminate. It can be present even in a fresh session if the model has recently run similar work.

---

## Prompt

You are about to begin a new brand identity project.

Before proceeding, complete the following declaration.

**1. Session status**

Is this a new conversation with no prior project work present?

- If yes: state that clearly and proceed.
- If no: state what prior material is present (project name, phase reached, any outputs generated). Recommend whether the human should start a new conversation based on how much structural work was completed.

**2. Memory status**

This process runs in Claude Code. There is no persistent cross-session memory.

Confirm: no prior project material from a different client is present in this conversation beyond what was introduced in step 1.

**3. External knowledge declaration**

Do you have prior knowledge of the brand or entity named in the repository you are about to receive — from training data, public knowledge, or any other source?

- If yes: state what you know and from what source. This knowledge must be labelled `[External — not from repo]` throughout the extraction if it surfaces.
- If no: state that clearly.

**4. Pattern transfer declaration**

Have you recently worked on a brand identity project — either in this session or in immediately prior context — where structural decisions were made (organising principle, hypothesis structure, tension framing)?

- If yes: name the structural patterns you are aware of carrying. These are prohibited from influencing the current extraction or brief. If they surface in any output, they must be labelled `[External — pattern transfer risk]` and flagged for review.
- If no: state that clearly.

**5. Clean slate confirmation**

Confirm:
- This project will be treated as structurally independent from all prior work
- No organising logic, hypothesis structure, tension framing, or form tendency will transfer from previous projects
- The repository is the only permitted source of subject evidence
- Any prior knowledge or pattern that surfaces will be labelled and flagged, not silently applied

---

## Human Decision Point

Read the declarations before proceeding.

**If prior session material is present:** start a new conversation. Do not proceed in the current session.

**If external knowledge is declared:** note it. Watch for it surfacing unlabelled during extraction. The extraction discipline is your primary defence.

**If pattern transfer risk is declared:** note the specific patterns named. When reviewing the extraction and brief, check whether these patterns appear to have shaped the output. If they have, flag and correct before proceeding.

**If all declarations are clear:** proceed to lens activation.

---

## On Pattern Transfer Risk

Pattern transfer cannot be fully eliminated by instruction. The declarations above make it visible rather than invisible — which is the most useful thing a prompt can do.

The defence against pattern transfer is the extraction discipline in Phase 1. If the extraction is genuinely factual, cited, and schema-driven, there is limited surface for prior patterns to enter. They are most likely to appear in Phase 2 — in how tensions are framed and what structural observations are made. This is why the brief requires explicit tracing back to the extraction. If a structural observation cannot be traced, it may be a pattern transfer artefact rather than a genuine finding.

When in doubt: if something in the brief feels familiar from a previous project, interrogate it. Familiarity is not validity.
