# Colour — Settled

> [Produced via settle command — approved by human]

## Direction Selected

**Concept 4 — The Achromatic Foundation**, from `colour/colour_concepts_v1.md`, developed through colour exploration that resolved the accent hue, foundation values, and token naming structure.

The colour system is achromatic. This is the governing principle, not a starting point. One precision accent hue is admitted as the minimum necessary departure from that principle — functioning exclusively as an interactive state signal where value alone is insufficient for legibility. The system does not have a brand colour; it has an achromatic default and one named exception.

### Why This Palette Exists

Krutho is not a conventional product brand. It is a cryptographic identity primitive — infrastructure that binds human authorisation to AI agents in a verifiable and portable way. Its authority does not come from performance. It comes from precision.

If colour is expressive, it implies personality.
If colour is dominant, it implies ownership.
If colour performs authority, it contradicts the mechanism — because the authority resides in the human who approved, not in Krutho.

The palette exists to create space, not assertion. Form carries meaning. Structure carries hierarchy. Interaction carries signal. Colour never carries personality.

### The Governing Logic

The system is achromatic by default. Colour is admitted only when a value-based solution would fail interactive clarity. This is not minimalism as aesthetic preference — it is discipline as structural alignment.

The neutral foundation carries hierarchy, legibility, grouping, contrast, and invitation. The action hue is a bounded exception. It exists for interaction and activation only. It is not a brand colour. It is a functional state.

### The Two-Gate Test

Every use of `color.action.*` must clear both gates:

1. **Is this achromatic?** — if yes, use surface, text, or border tokens.
2. **Would a value-based solution fail interactive clarity here?** — only if yes is the action hue admitted.

Both gates must clear. If only the second clears without asking the first, the concept has become Concept 2.

### What This Is Not

The system is not minimal with a "pop of colour." It is not "near-achromatic with a brand accent." The framing is precise: achromatic is the rule; the action hue is the concession to operational reality. The distinction determines drift behaviour under production pressure. A team that treats the action hue as a brand accent will expand its use. A team that treats it as a functional concession will not.

### Controlled Brand Emergence

A critical insight from exploration: even when colour is admitted only where necessary, repeated use at links, buttons, active states, and focus rings inevitably creates brand recognition over time. The system does not deny this — it controls it.

The accent is designed so that if repeated frequently, it reads as infrastructural rather than expressive. If used at large scale (slide covers, documentation covers), it reads as depth rather than marketing. If encountered alone, it signals system gravity rather than personality.

Brand presence is acknowledged and contained. This is not accidental repetition — it is controlled expression.

---

## The Foundation

**Principle:** Slightly softened neutrals, no temperature bias. The system avoids clinical white and harsh black without introducing warmth that reads as approachability. The interface feels calm, precise, and open. Nothing styled; nothing severe.

| Token | Value | Rationale |
|---|---|---|
| `color.surface.primary` | `#FAFAFA` | Avoids clinical white; remains open and unencumbered |
| `color.surface.secondary` | `#F2F2F2` | Panels, code blocks, table rows; structural grouping |
| `color.surface.tertiary` | `#EAEAEA` | Deeper grouping where needed; not a category signal |
| `color.surface.inverse` | `#181818` | Inverse surfaces; avoids harsh pure black |
| `color.border.subtle` | `#E0E0E0` | Lightest structural division |
| `color.border.default` | `#D8D8D8` | Standard dividers, input borders, card edges |
| `color.border.strong` | `#C8C8C8` | Emphasis division where clarity requires it |
| `color.text.primary` | `#181818` | All primary prose, headings, labels; avoids harsh pure black |
| `color.text.secondary` | `#707070` | Captions, metadata, helper text; subordinate but legible |
| `color.text.tertiary` | `#9A9A9A` | Disabled text, placeholder text; clearly recessive |
| `color.text.inverse` | `#F4F4F4` | Text on inverse surfaces |

The grey scale is evenly stepped, not stylised. No temperature pull. Hierarchy is created through value contrast, weight, scale, and space — not through hue.

---

## The Action Hue — `#1D4A4B`

### Derivation

The hue was derived along a spectrum between visibility and substrate — from clearer teal at one end to deep structural teal-black at the other.

At the clearer end: colour felt like brand performance. It asserted itself. At the deeper end: colour became heavy and receded into background.

`#1D4A4B` sits at the structural inflection point:

- Deep enough to avoid SaaS-teal territory
- Dark enough to avoid corporate blue
- Controlled enough to avoid personality
- Clear enough to maintain interaction visibility
- Durable enough to outlast trend cycles

It behaves like a system state, not a flourish. When used in UI, it reads as activation. When repeated, it becomes recognition — but not performance.

### Token Naming — `color.action.*` not `color.accent`

The action hue is named `color.action.*`, not `color.accent` or `color.brand`. This is a structural governance decision: the name reinforces function and prevents decorative use by encoding the governance rule directly into the token name. If someone uses `color.action.default` for a section background, the name itself signals that it is semantically incorrect. That is structural enforcement.

| Token | Value | Role |
|---|---|---|
| `color.action.default` | `#1D4A4B` | Primary interactive elements: button fill, link text, toggle on-state |
| `color.action.hover` | `#183E40` | Hover state — slightly darker; still the action hue |
| `color.action.active` | `#153536` | Pressed/active state |
| `color.action.subtle` | `#E9F1F1` | Background wash for active containers, selected rows — lowest-saturation form of the hue |
| `color.action.focus-ring` | `#1D4A4B` | Accessibility focus indicator; non-negotiable |

Token derivation documentation states: "these tokens represent the minimum necessary departure from the achromatic governing principle, admitted for interactive legibility only. `color.action.*` is not a brand colour. It is a bounded system signal."

---

## Status Tokens

Conventional functional defaults. Not derived from `color.action.*` and not derived from brand logic. These complete the specification; they are not brand expression.

| Token | Value | Semantic |
|---|---|---|
| `color.status.success` | `#1F7A3D` | Conventional green; semantic convention only |
| `color.status.warning` | `#B26A00` | Conventional amber |
| `color.status.error` | `#B3261E` | Conventional red |
| `color.status.info` | `#1D4ED8` | Conventional blue |

Token documentation states: "conventional system defaults for semantic clarity — derivation is semantic convention, not aesthetic derivation from brand logic. These tokens must never be aliased to action tokens."

---

## Interaction Layer Tokens

| Token | Value | Role |
|---|---|---|
| `color.state.disabled` | `#CFCFCF` | Disabled elements; achromatic |
| `color.state.overlay` | `rgba(0,0,0,0.04)` | Hover state surface overlay; non-expressive |
| `color.state.scrim` | `rgba(0,0,0,0.6)` | Modal overlays |

Still neutral. Still non-expressive.

---

## Token Namespace

All tokens use the namespace `color.{category}.{role}`:

- `color.surface.*` — page and screen surfaces
- `color.text.*` — all text
- `color.border.*` — structural dividers
- `color.action.*` — interaction and activation only
- `color.status.*` — semantic system states
- `color.state.*` — interaction layer utilities

Note: tokens use `color` (American English / CSS convention). Design documentation uses `colour` (British English). This is intentional — the token system follows programming convention; the design language follows house style.

---

## Governance Rule

Before using `color.action.*`, ask:

**Would a value-based solution fail interactive clarity here?**

If no: use surface, border, or text tokens.
If yes: the action hue is permitted at that specific point.

This rule is the only governance mechanism. It is simple enough to enforce under production pressure. The token name reinforces it — `color.action.default` cannot be used as a decorative background without the name itself flagging the error.

The most likely drift path is gradual: a designer who answers "the accent would be better here" instead of "value-alone would fail here" has overridden the first gate. System documentation must name this distinction explicitly as the governance boundary.

---

## Contrast & Accessibility

- `color.text.primary` on `color.surface.primary`: WCAG AAA target
- `color.action.default` as interactive text on `color.surface.primary`: WCAG AA minimum — confirmed at `#1D4A4B`
- `color.text.secondary` on `color.surface.primary`: WCAG AA minimum
- `color.action.focus-ring`: must achieve sufficient contrast to be immediately visible; non-negotiable
- Status tokens: WCAG AA in application contexts

Contrast targets are part of the token derivation rules, not constraints applied after the fact.

---

## Structural Properties Confirmed

- **Governing principle:** Achromatic by default. All passive states — surfaces, borders, text, iconography — are value-based.
- **Action hue:** `#1D4A4B`. Admitted as a bounded exception for interactive legibility. Named `color.action.*` to encode governance into the token name. Not a brand colour.
- **Foundation:** Softened neutrals. No temperature bias. #FAFAFA to #181818 scale, evenly stepped.
- **Two-gate test:** "Is this achromatic?" then "Would value alone fail?" — both must clear before `color.action.*` appears.
- **Token namespace:** `color.{category}.{role}` throughout.
- **Status tokens:** Conventional defaults. Explicitly separate from action tokens. Not brand expression.

---

## Constraints for Downstream Modules

**Typography**
Typography inherits this colour system. The weight ceiling (Regular/Medium, no Bold) from `typography_settled.md` remains fixed. All colour assignment for type is governed by this token system — no typographic colour decisions are made at the type module.

**Layout**
The achromatic default extends to all spatial and structural elements. No coloured structural elements. Dividers, grid lines, and section markers use border tokens only.

**UI**
The two-gate test applies in all UI contexts without exception. `color.action.subtle` (`#E9F1F1`) is available for selected/active container backgrounds but inherits the same governance gate. The typographic weight ceiling remains in force.

**Imagery**
Diagram colour (Concept 2 — The Mechanism) is achromatic by default; `color.action.*` may appear at active or highlighted diagram elements on the same governance rule. Photography treatment (Concept 3 — The Authorization Moment) is monochrome or near-monochrome throughout. No imagery surface introduces colour not admitted by this token system.
