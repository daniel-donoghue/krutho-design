# Typography — Settled

> [Produced via settle command — approved by human]

## Direction Selected

**Concept 3 — The Demonstrable System**, from `typography/typography_concepts_v1.md`, developed with Spline Sans + Spline Sans Mono as the type family selection.

The typographic system earns authority the way the whitepaper earns authority: by showing its work. Named levels, named spacing parameters, named modular ratio, public design tokens. A developer can read the token file, reconstruct the system, and verify it without a visual reference. This is the hypothesis applied to the typography layer.

### Typeface Selection: Spline Sans + Spline Sans Mono

**Spline Sans** (Regular, Medium) — proportional text
**Spline Sans Mono** (Regular, Medium) — code, CLI, documentation

Both faces from the same family. Single source, single structural decision.

**Register**
Spline Sans is a neo-grotesque. The forms are disciplined without being derived from geometric primitives — the `o` is functional rather than circular, the overall colour is flat and exact. It does not read as warm, considered, or designed. It reads as correct. This is the right register for a type system that must not carry identity weight of its own — the wordmark carries the identity; the type system carries the content.

**Non-interference**
The type system has one structural requirement: not to interfere with the wordmark. Spline Sans meets this at every size tested. At body text it recedes. At heading size in Regular or Light it is subordinate. It carries no aesthetic position of its own that the identity would need to manage or reconcile.

**Weight hierarchy**
The wordmark's monolinear weight sits unambiguously above the type system's range in use. Medium is the ceiling for body and heading use. Medium at display size approaches the wordmark's territory — this is a use constraint, not a typeface failure, and it is manageable by rule: headings are set in Regular or Light; Medium is reserved for UI labels and functional emphasis only.

**The mono role**
Spline Sans Mono has technical authority. It does not read as friendly or approachable — it reads as exact. This is structurally consistent with the wordmark's `r` letterform, noted in the logo document as code-adjacent rather than humanist. The mono face extends that signal into the code and documentation layer without requiring a register shift. A developer reading documentation encounters the same precision posture throughout.

**Family coherence**
Both faces share the same construction origin. Weight increments track consistently across sans and mono — the system does not need to be compensated or adjusted at the boundary between prose and code. No pairing decision, no register conflict, no optical correction required where the two faces meet.

**Availability**
Spline Sans is available on Google Fonts under the SIL Open Font License. A developer can clone the design system, implement it identically, and verify it without a licence conversation. This is not a convenience argument — it mirrors the cryptographic verification posture of the standard itself. The type system is as reproducible as the format.

**What this does not provide**
The type system carries no warmth, no community signal, no personality. This is correct. DevRel and community functions must be built at the product and content layer. The typography will not compensate for the absence of those functions and should not be asked to.

---

## Structural Properties Confirmed

**Family:** Spline Sans (Regular, Medium) for proportional text; Spline Sans Mono (Regular, Medium) for code, CLI, and documentation. Both faces share the same construction origin — single source, single structural decision. No pairing compromise, no optical correction required at the sans/mono boundary.

**Register:** Neo-grotesque. Reads as correct, not warm. The type system carries no aesthetic position of its own. The wordmark carries identity; the type system carries content. Non-interference with the wordmark is the primary structural requirement.

**Weight ceiling:** Regular and Light for headings and body. Medium is the ceiling, reserved for UI labels and functional short-form emphasis only. SemiBold and Bold are available in the family but excluded from use — they approach wordmark weight at display size and would compromise the wordmark's authority position.

**Wordmark authority:** The wordmark's monolinear weight sits unambiguously above the type system's working range. This is fixed. No typographic weight in use competes with it.

**Named levels:** Four — Display, Section, Body, Detail. Each level governed by a single stated rule. Hierarchy by size (primary). Weight at one step only (Regular to Medium at Section level). Case for register type, not hierarchy position.

**Weights in use:** Regular and Medium. No Bold. No italic.

**Monospace role:** Spline Sans Mono for all code, CLI output, token values, version strings, hash values, and any content that is data rather than prose. Not decorative. The register shift between sans and mono is structural — it names the boundary between explanation and specification.

**Availability:** Google Fonts, SIL Open Font License. A developer can clone the design system, implement it identically, and verify it without a licence conversation. This mirrors the cryptographic verification posture of the standard itself. The type system is as reproducible as the format.

**Spacing:** Inherits the precision logic of the wordmark's internal intervals. The type system does not introduce its own spatial logic.

**Colour:** Deferred. Typography inherits colour from the system once defined. No typographic colour decisions made at this module.

---

## Artifacts

- `src/outputs/01-systems/typography/artifacts/Spline_Sans,Spline_Sans_Mono.zip` — Spline Sans and Spline Sans Mono font files (Google Fonts, SIL OFL)

Conversations digested: `spline-sans-reasoning.md` — typeface selection rationale. Content fully integrated into Direction Selected above.

---

## Constraints for Downstream Modules

**Colour**
Typography inherits from the colour system. No typographic colour decisions have been made here — colour module has full latitude, subject to the weight hierarchy and register constraints above.

**Layout**
The type system's named scale and spacing values are fixed structural inputs. Layout must work with them — not around them. Spatial logic is inherited from the wordmark's internal intervals; the layout system should extend that logic, not introduce a competing one.

**UI**
The weight ceiling applies in all contexts without exception. Medium is functional emphasis only — labels, identifiers, short-form UI elements. The sans/mono register boundary is structural and must be respected throughout: monospace appears where mechanism content appears, nowhere else.

**Imagery**
No direct constraint from typography. Imagery must be selected on its own structural terms.

---

## Notes

The type system is as reproducible as the format. This is not incidental — it is the hypothesis applied to the typography layer. A standard publishes its parameters. This type system publishes its parameters. A designer working from the token file and a developer implementing from it are in the same relationship to the system as a verifier checking a certificate: independent of Krutho, holding nothing on trust.
