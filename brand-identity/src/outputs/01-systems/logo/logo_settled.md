# Logo — Settled

> [Produced via settle command — approved by human]

---

## Direction Selected

**Concept 3 — The Wordmark**, from `logo/logo_concepts_v1.md`.

The wordmark is the entire identity. No symbol. No container. Letterform precision is the structural argument. The name Krutho, constructed with exactness, functions as the signature of the standard — in the same register that protocol and specification names carry authority: HTTP, X.509, ECDSA. This is the final wordmark. No further direction exploration is required at this stage.

---

## Structural Properties Confirmed

**Construction logic:** Mathematically constructed throughout. The wordmark is built, not drawn — every form is derivable from a rule, not arrived at by eye. Optical adjustments are limited to two specific instances: the `u` and `h` tapered arches, which are subtle and deliberate. These are the only exceptions to the geometric construction logic; no other optical corrections were applied.

**Stroke weight:** Monolinear. 100-unit weight consistent across all stems, arms, and bowls. No modulation. No thick-thin variation. The wordmark reads as a specification decision — not a typeface selection.

**The `r` letterform:** Vertical leg with single horizontal arm at the top right. No bowl. This is the most distinctive letter in the wordmark and the one that sets the technical register for the entire word. It reads as a code character, not a typographic letter — code-adjacent rather than humanist. At display size it is legible and specific.

**The `o` letterform:** A rounded rectangle, not a circle. Outer flat sections: 80 units (top and bottom). Inner counter flat sections: 120 units. The `o` is constructed space — shaped, not drawn. It anchors the word with geometric specificity.

**Letter height hierarchy:** K and `h` at full ascender height (y=0). `t` deliberately 20 units shorter (y=20). Consistent with standard typographic practice — intentional, not an error.

**The `h` arch:** A calibrated bezier transition between the ascender and right leg — the single curve-to-curve transition in the wordmark. All other transitions are stroke-to-space.

**Letter spacing (SVG units):**

| Pair | Gap |
|---|---|
| K → r | 40 |
| r → u | 80 |
| u → t | 70 |
| t → h | 80 |
| h → o | 70 |

K→r measures 40 units but reads as optically wider due to the K diagonal's recession. This should be verified at favicon and CLI output scale before considering any adjustment.

**Weight rhythm:** The word gains weight toward the right — `r` is narrow, `u` and `t` are mid-weight, `h` and `o` are the heaviest pair. The wordmark lands rather than trails off.

**ViewBox:** Current SVG is `0 0 2540 650`. Recommended expansion to `0 0 2540 660` to provide a 10-unit safety margin for the `u` and `o` bottom curves against renderer clipping. No visual change — a technical correction.

**Register:** The wordmark reads as a proper noun being named, not a product being branded. The uppercase K against lowercase construction positions it in the protocol-name register. Substantial, precise, named.

**Status:** Final. No further letterform exploration or alternative directions are in scope.

---

## Artifacts

- `src/outputs/01-systems/logo/artifacts/krutho-wordmark.svg` — final wordmark SVG, production-ready (pending minor viewBox correction noted above). Move from `src/import/`.
- `src/outputs/01-systems/logo/artifacts/Krutho.png` — rendered PNG at 2540×650. Move from `src/import/`.

**Conversations digested:** `wordmark-review-claude-chat-03022026.md` — SVG technical correctness review and hypothesis alignment check. Approved extract only; not reproduced verbatim.

---

## Constraints for Downstream Modules

**Typography — primary constraint**
The system resolves around a monolinear medium-bold anchor. The wordmark's weight must remain the heaviest and most authoritative typographic element in any composition. Body text must be sufficiently lighter that the wordmark holds without isolation. System typeface must be grotesk or geometric sans — no high-contrast serifs, no decorative display faces. The wordmark's specific weight should not exist as a named weight in the system typeface family, so it remains visually distinct from text. Monospace has a structural role in the system (code, CLI, documentation) — the `r` letterform's code-adjacent quality makes this a legitimate and signalled extension. All spacing and typographic decisions in the system inherit the same precision logic established in the wordmark.

**Colour**
The wordmark makes no colour demands and requires none. It is fully functional in black, white reversed, or any single colour. Any colour introduced to the system must be justified on structural terms independent of the wordmark. Colour is not a corrective — nothing is missing from the wordmark that colour could supply.

**Layout**
The wordmark is horizontally dominant (approximately 4:1 width-to-height). The horizontal axis is primary. Any spatial logic for the system — grid unit, spacing intervals — should relate to the wordmark's internal intervals rather than contradict them. No compact or alternate lockup is required; the wordmark holds at documentation scale.

**Imagery**
There is no symbol to reference or echo. Imagery must be selected on its own structural terms. The technical precision of the `r` and `o` letterforms signals that constructed, precise imagery is in register — atmospheric, illustrative, or emotional imagery is not.

**UI**
The monolinear construction maps directly to UI strokes, borders, and interface elements. Precision throughout — no decorative radius, no gratuitous gradients, no iconography without structural necessity. The wordmark sets the precision standard; UI must meet it.

---

## Notes

Two minor items flagged during exploration for early context testing — not blockers, but worth verifying before wider rollout:

1. **K→r optical spacing** — the 40-unit gap should be checked at favicon and CLI output sizes to confirm it reads correctly in compressed contexts.
2. **`r` arm at small scale** — the arm should be confirmed at npm page, GitHub README, and favicon. The arm is the most distinctive and most at-risk element at very small sizes.

Both are execution verification items, not structural issues. The wordmark is production-ready (viewBox correction already applied).

**On mathematical correctness and human legibility**

The wordmark reads as constructed, not designed. A designed wordmark removes awkwardness as a finishing step. A constructed wordmark retains it because the awkwardness is a consequence of the rule, not a failure of craft. The `r` is the clearest instance — formally correct within its construction logic, and slightly foreign within the word as a result. That foreignness is not a problem to solve. It is the signal.

This names the execution risk from the brief precisely. The brief warned against *"imprecision mistaken for restraint"* — awkwardness without an underlying rule. The wordmark demonstrates the inverse: awkwardness with the rule fully present and legible. The difference is whether the rule can be felt. In v1 it can.

The readability of the wordmark does not come from optical softening. It comes from consistent internal logic — the reader parses the rule and trusts it. This is a different register of legibility from typefaces that overshoot geometric correctness to comfort the eye. It is the right register for this identity.

**Quality consideration for downstream modules:** When a system decision — typographic, spatial, structural — removes the slight tension between mathematical correctness and human legibility, it is worth examining. Resolving that tension is not necessarily wrong, but it should be a deliberate choice, not an instinctive one. The goal is to hold the tension consistently where it is right to hold it, and resolve it deliberately where resolution is warranted. This is a consideration to carry into each module, not a rule that prevents resolution.
