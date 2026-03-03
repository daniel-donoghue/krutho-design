# Typography System — Concepts v1

**Entity:** Krutho
**Module:** Typography
**Version:** 1
**Sources:** `02_foundational_brief.md`, `04_active_hypothesis.md`, `logo_settled.md`
**Date:** 2026-03-02

---

## Settled Module Constraints Applied

Logo module is settled. The following constraints are structurally binding on this output. `[Logo Settled — Constraints for Downstream Modules]`

- The wordmark is the heaviest and most authoritative typographic element in any composition. Body text must be sufficiently lighter that the wordmark holds without isolation.
- System typeface must be grotesk or geometric sans — no high-contrast serifs, no decorative display faces.
- The wordmark's specific weight must not exist as a named weight in the system typeface family, so it remains visually distinct from text.
- Monospace has a structural role in the system (code, CLI, documentation) — the `r` letterform's code-adjacent quality makes this a legitimate and signalled extension.
- All spacing and typographic decisions in the system inherit the same precision logic established in the wordmark.

---

## Concept 1 — The Omission Standard

### Grounding Statement

The typographic system earns authority by demonstrating discipline in what it withholds: one family, one primary weight, hierarchy created only through size and case — not decoration, not weight variation. The less the system asserts, the more it proves.

`[Hypothesis — Organising Principle]` `[Brief — Section 7]`

If this cannot be written clearly, the concept is not grounded. It can be written clearly.

---

### Structural Typographic Logic

- **Principle:** Authority by omission. The system achieves its signal by refusing typographic tools that are available — not because those tools are wrong in themselves, but because each tool used must be earned. Using only size and case to create hierarchy is not a limitation; it is the demonstration of the principle.
- **Organising expression:** The wordmark is the heaviest typographic element in any composition. The text system stays well below it in weight, ensuring the name carries the authority. The text system does not compete. `[Logo Settled — Primary constraint]`
- **Category positioning:** Against IAM vendor aesthetics (which use multiple weights and sizes to perform technical complexity), Krutho's typography reads as disciplined, not sparse. Against startup visual energy (bold type for its own sake), it reads as restrained and deliberate. `[Brief — Section 9]`

---

### Hierarchy Model

- **Levels:** Three maximum — Heading, Body, Detail/Label. No tertiary sublevels.
- **Differentiation levers:** Size only, with case as a secondary marker for functional categories (labels, metadata, technical identifiers). Weight is not a hierarchy lever in this concept — it is reserved for rare structural emphasis only (e.g. a technical term being named in a definition, not emphasised in running prose).
- **Restraint enforcement:** The system has no bold text in running prose. If the argument requires emphasis, the prose must be restructured to make the emphasis structural, not typographic. This is the direct typographic expression of "no word that is not doing work." `[Hypothesis — Invariant 5]`
- **Emphasis prohibition:** Bold prose is a category signal failure. It reads as startup copy. The system refuses it.

---

### Weight & Emphasis Behaviour

- **Weights structurally necessary:** Two. One for body and interface (Regular or Book). One for headings (Medium) — specifically: the heading weight must be lighter than the wordmark's visual weight. The wordmark is outside the family's named weight range by structural requirement. `[Logo Settled — Typography primary constraint]`
- **Permitted emphasis:** Weight step at Heading level only, never mid-paragraph. Case change for identifiers and labels. No italic.
- **Excluded combinations:** Bold + large size (asserts rather than demonstrates). Weight + case emphasis simultaneously (doubles the signal, which is a failure of discipline). `[Hypothesis — Form Logic]`

---

### Scale & Proportion Strategy

- **Base scale:** Fixed. A small number of named sizes defined by function: Heading, Body, Caption. Not a fluid scale — a specification has defined values, not a range.
- **Ratio philosophy:** The interval between levels is measurable and demonstrable. If a designer extracts the font sizes and builds a table, the logic should be legible from the numbers alone. The ratio is not a preference — it is a structural parameter.
- **Environment behaviour:** The system maintains fixed sizes in code/documentation environments. Headings may scale within a tighter range for screen vs. print. Body text does not scale — it is a specification value, not a preference.

---

### Spacing & Rhythm Logic

- **Letter spacing:** Tight to default on body. No loose tracking used for aesthetic effect. Uppercase labels and identifiers carry defined positive tracking — functional, not decorative.
- **Line length:** Constrained. Documentation: 65–75 characters. UI: shorter by context. Prose must not sprawl; measure is a structural decision, not a layout preference.
- **Density vs openness:** The system defaults toward density, not openness. Openness is allocated at the layout level, not the typographic level. The text block is tight; the page breathes around it. `[Hypothesis — Design Consequences — Form Logic]`
- **Rhythm:** Consistent leading. Paragraph spacing is a multiple of the base line height. The rhythm should feel like a grid — because it is.

---

### Case Strategy

- **Prose:** Sentence case. No exceptions for brand terms except proper names.
- **Labels, identifiers, metadata:** Uppercase with measured positive tracking. This signals a register change — from prose to system output — without needing a weight change.
- **Code content:** As-is. The monospace carries its own case conventions. The system does not override programming notation.
- **What case must not do:** Perform authority. "SECURE" in uppercase is not more secure. Case is functional, not decorative.

---

### Pairing Logic

- **Single family for prose/UI/editorial:** Geometric grotesk. Family must be grotesk or geometric sans only — no high-contrast serifs. The wordmark's specific weight must not exist as a named weight in the family. `[Logo Settled — Typography primary constraint]`
- **Monospace for code, CLI, technical identifiers:** Not a separate brand voice — a functional extension. The monospace is where the mechanism speaks. Its role is pre-defined by the `r` letterform's code-adjacent quality. `[Logo Settled — Constraints]`
- **Pairing discipline:** The monospace is not used decoratively. It is not used for pull quotes, emphasis phrases, or anywhere the code register would be misapplied. Its appearance signals: this is mechanism output, not editorial content.

---

### Cross-Context Behaviour

**Product UI**
One weight for most elements. Size to separate. Labels in uppercase with tracking. Monospace for all technical identifiers, certificate fields, API responses. The UI reads like a structured form or specification view — not a dashboard. `[Brief — Section 9]`

**Marketing / web**
Same system — this is not a context where the system relaxes. The discipline is the positioning. Heading sizes may be larger on display contexts; the system logic holds. No decorative typographic treatment of any kind.

**Documentation**
Prose in the grotesk. Code blocks in monospace. No typographic decoration. Headings are navigational, not expressive.

**CLI / terminal output**
Monospace only. The system does not intrude on terminal conventions. `[Logo Settled — Notes on `r` at small scale]`

---

### What This Makes Impossible

- Bold running prose — any document that emphasises through weight rather than structure
- Italic as a standard tone marker
- Multiple heading weights (heavy, bold, semibold) — the system admits two weights maximum
- Display typography as a visual statement independent of the content it carries
- Typographic playfulness of any kind
- Warmth signals through rounded display type or casual weight selection

---

### Category & Mis-Signal Risk

- **Risk:** A single-weight geometric grotesk risks reading as generic or unfinished. The difference between disciplined and cheap is the quality of the type selection and the specificity of execution. `[Hypothesis — Structural Risks]`
- **Risk:** The system may read as austere to non-developer audiences. This is structurally acceptable — developer-first register is non-negotiable. `[Brief — Section 5]`
- **Mitigation:** The monospace pairing, used precisely, signals technical depth. The case system creates register clarity without additional weights. The risk is in execution, not logic.
- **Drift risk:** Under pressure to "make it feel more alive," a designer will reach for a second or third weight, or introduce italic. The system must be defined tightly enough that deviation reads as a mistake, not a choice.

---

### Identity Gate Pressure Test

1. **Does it read as infrastructure rather than a product?**
**Pass.** The typographic restraint — one weight, functional case — reads as specification-grade. No type selection performs product personality.

2. **Does it signal technical credibility to a developer on first contact?**
**Conditional.** The system is credible only if the family selection is excellent. A poor geometric grotesk will read as generic. The execution must be precise. `[Hypothesis — Execution failure risk]`

3. **Does it avoid implying that Krutho must be present at verification?**
**Pass.** Typography carries no such implication.

4. **Would a technically skeptical developer trust it?**
**Pass.** The restraint reads as deliberate, not accidental. A developer who understands design discipline will recognise what the system is doing.

5. **Could this be the identity of a cryptographic standard, not a startup?**
**Pass.** The sparse, interval-driven system is consistent with how standards documentation looks and feels — RFCs, NIST publications, X.509 documentation.

6. **Does it demonstrate intellectual honesty — does it show the reasoning?**
**Conditional.** The system logic is demonstrable but not self-announcing. The third read must find the reasoning without a guide. If the intervals are clean enough, they will.

7. **Does it exclude the wrong categories clearly enough?**
**Pass.** No weight complexity, no display personality, no warmth signals. IAM/PAM vendor aesthetics require multiple weights and expressive type — this system refuses them.

**Overall: Pass with one execution-dependent condition.** The system's strength depends on the quality of the family selection. The logic is sound; the risk is craft.

---

### Exploration Brief

**Begin from:** Define the size scale first. Name three sizes only: Heading, Body, Detail. Establish the ratio between them. Check that the ratio holds across three output sizes: marketing page heading, documentation body, UI label. If the ratio works across all three, the system has a backbone.

**Hierarchy to prototype:** One heading size and one body size. Test the difference between them — is the hierarchy clear without a weight change? If a reader cannot tell which is the heading at a glance, the size interval is too small.

**Tension to test:** Restraint vs. legibility. Can the system hold authority at body scale with only Regular weight? The test is a documentation page with four heading levels and long paragraphs. Does it read, or does it collapse into visual noise?

**Avoid immediately:** Adding a third weight because the two-weight system "doesn't feel expressive enough." The system is not meant to feel expressive. It is meant to feel exact. If a designer reaches for expressiveness, the brief has been forgotten.

---

## Concept 2 — Two Voices, One Structure

### Grounding Statement

The typographic system acknowledges the structural duality at the heart of Krutho's mechanism — the human-facing explanation and the machine-legible specification — by assigning a separate typographic voice to each: a grotesk family for prose, narrative, and interface, and a monospace family for mechanism output, technical identifiers, and specification content. Hierarchy within each register is kept deliberately flat; the register change IS the hierarchy signal.

`[Hypothesis — Structural Thesis]` `[Brief — Section 4]` `[Logo Settled — Constraints for Downstream Modules]`

---

### Structural Typographic Logic

- **Principle:** Register is hierarchy. The primary structural distinction in Krutho's communication is not between "big" and "small" or "bold" and "light" — it is between the human layer (what is being authorised, why it matters, how to implement) and the mechanism layer (what the certificate contains, what the format specifies, what the cryptographic claim is). These are different languages, and the typography embodies that difference.
- **Organising expression:** The grotesk reads prose. The monospace reads mechanism. Neither is decorative. The `r` letterform in the wordmark already signals this duality — code-adjacent, precise, not purely typographic. The typography extends that signal into the full system. `[Logo Settled — The `r` letterform]`
- **Category positioning:** This system positions Krutho in the infrastructure layer — not the product layer. Products have one voice. Infrastructure speaks in multiple registers because it operates at multiple levels of the stack. `[Brief — Section 6]`

---

### Hierarchy Model

- **Levels within grotesk:** Two. Heading (for navigation and section naming). Body (for prose and explanation). Differentiated by size and weight — but the weight range is narrow: Regular to Medium maximum.
- **Levels within monospace:** One. Monospace appears at a consistent size within its contexts — it does not have its own internal heading hierarchy. Its presence is the hierarchy signal.
- **Emphasis within prose:** Size only. Within technical content — the monospace block is already the emphasis. No additional emphasis within monospace blocks.
- **Restraint enforcement:** A typeface switch is a significant typographic event. Overusing monospace for aesthetic reasons (to "feel technical") would collapse the signal. Monospace appears only where mechanism content appears. `[Hypothesis — Invariant 5]`

---

### Weight & Emphasis Behaviour

- **Grotesk weights:** Two. Regular for body and most UI. Medium for headings. The heading Medium must be visually lighter than the wordmark — the wordmark holds the weight authority in any composition. `[Logo Settled — Typography primary constraint]`
- **Monospace weight:** One. Monospace does not use weight emphasis — its register is already distinct. Adding a bold weight to monospace would be a second signal on top of an already-distinct register change, which doubles without adding.
- **Excluded combinations:** Bold grotesk in prose. Italic in any context. Monospace with additional weight emphasis.

---

### Scale & Proportion Strategy

- **Base scale:** Two independent scales — one for grotesk (three levels), one for monospace (one consistent level). The monospace scale is simpler; the grotesk scale has three steps maximum.
- **Proportion:** Monospace is typically set slightly smaller than comparable grotesk body text — not as a hierarchy statement, but because monospace proportions at equivalent point sizes run wider and require optical adjustment.
- **Environment behaviour:** In documentation, the two registers alternate by content type, not by section. A paragraph may be followed immediately by a technical block — the switch signals content type, not section change. In UI, monospace appears for identifiers, certificate fields, and output; grotesk for labels, navigation, prose. In marketing, monospace appears for technical claims stated in specification format — not for decoration.

---

### Spacing & Rhythm Logic

- **Grotesk:** Default tracking. Measure limited to 70–80 characters. Line height 1.5 for body.
- **Monospace:** Tighter line height (1.4). Measure matched to code output conventions — wide enough for full certificate blocks without wrapping. Horizontal rhythm is the monospace grid, which is inherent to the typeface.
- **Register transition spacing:** A consistent block spacing before and after monospace blocks in prose contexts — the gap names the transition without requiring a label.
- **Density:** The system is dense in technical content (monospace blocks run close). Grotesk prose breathes more. The contrast in density between registers is functional — it signals content type.

---

### Case Strategy

- **Grotesk prose:** Sentence case.
- **Labels and navigation:** Uppercase with tracking — same logic as Concept 1.
- **Monospace:** As-is. Technical identifiers use their actual case conventions: `ECDSA_P256`, `krutho-core`, etc. The system does not impose its case conventions on mechanism output.

---

### Pairing Logic

- **Primary family:** Geometric grotesk. Grotesk or geometric sans only. `[Logo Settled — Typography primary constraint]`
- **Secondary family:** Monospace. A monospace whose weight and x-height are compatible with the grotesk — they must be able to appear in adjacent blocks without visual clash.
- **Pairing selection criteria:** The grotesk and monospace should share geometric construction values — ideally both read as built rather than drawn. This makes the pairing coherent rather than contrasted. `[Logo Settled — Construction logic]`
- **What the monospace must do that the grotesk cannot:** Signal mechanism output unambiguously. Be readable at block scale (certificate display, JSON output). Not feel like decoration.

---

### Cross-Context Behaviour

**Product UI**
Grotesk for all navigational and explanatory elements. Monospace for all certificate content, API parameters, technical identifiers, and output fields. The register split maps directly to the product's own information architecture — human layer vs. specification layer.

**Marketing / web**
Grotesk for all prose and headings. Monospace for technical claims quoted in specification format, code samples, and mechanism-level descriptions. The moment monospace appears on a marketing page, it signals: we are now at the mechanism level. This must be used precisely — not as decoration.

**Documentation**
Full register system in use. Prose in grotesk, code in monospace, technical definitions in monospace. The most natural environment for this system — it maps exactly to how technical documentation operates.

**CLI / terminal**
Monospace only in output. Grotesk has no role in terminal contexts.

---

### What This Makes Impossible

- Running prose in monospace — collapses the register signal
- Decorative monospace (pull quotes, stylistic code fragments used as imagery)
- A third family
- Weight complexity within either family
- Any display or editorial register within grotesk — the family is not used as a personality vehicle

---

### Category & Mis-Signal Risk

- **Risk:** Monospace as aesthetic choice has been widely adopted by tech companies as developer credibility theater — the use of monospace to signal technical depth without genuine depth. This system must be rigorous: mechanism content only.
- **Risk:** A dual family system risks feeling "designed" in a way that compromises the specification register. If the pairing is chosen for visual effect rather than structural necessity, the system contradicts itself.
- **Mitigation:** The pairing rationale must be articulable without reference to aesthetics. The monospace is justified by the `r` letterform's code-adjacent quality and by the structural role of monospace in Krutho's actual content types — documentation, CLI, certificate display. `[Logo Settled — Constraints]`
- **Drift risk:** Using monospace for anything other than mechanism content. This is the single most likely way the system will be compromised over time.

---

### Identity Gate Pressure Test

1. **Does it read as infrastructure rather than a product?**
**Pass.** Two registers — one human, one mechanism — is an infrastructure-grade typographic structure. Products have one voice.

2. **Does it signal technical credibility to a developer on first contact?**
**Pass.** Monospace is the developer's native environment. Its precise use — mechanism only — signals that Krutho understands the distinction.

3. **Does it avoid implying that Krutho must be present at verification?**
**Pass.** Typography carries no such implication.

4. **Would a technically skeptical developer trust it?**
**Pass.** The register discipline — using monospace only where it belongs — is itself a credibility signal. A developer who sees monospace used decoratively loses trust.

5. **Could this be the identity of a cryptographic standard, not a startup?**
**Pass.** Standards documentation always distinguishes prose from specification content. This system encodes that distinction structurally.

6. **Does it demonstrate intellectual honesty — does it show the reasoning?**
**Pass.** The register separation is demonstrable — a reader can extract the rule from observation. Mechanism = monospace. Explanation = grotesk. The system shows its work.

7. **Does it exclude the wrong categories clearly enough?**
**Pass.** The precise use of monospace — not decoration, not vibe — is anti-category for IAM/PAM and AI company aesthetics alike.

**Overall: Strong pass.** The system's logic is tight and demonstrable. Risk is in execution discipline — particularly whether monospace remains a mechanism-only signal over time.

---

### Exploration Brief

**Begin from:** Define the pairing. Find two families — one grotesk, one monospace — whose construction values are compatible without being identical. Test them side-by-side in a certificate display context: a block of prose explaining a field, followed immediately by the field's monospace value. Does the register change read clearly? Does it feel structural rather than designed?

**Hierarchy to prototype:** A documentation section with: one heading, two body paragraphs, and one technical block (certificate or code). The test is whether the register change communicates content type without a label.

**Tension to test:** Signal vs. noise. If monospace appears too frequently, the register signal collapses into pattern. If it appears too rarely, the system reads as single-family with occasional code blocks. Find the frequency at which the register split is structurally felt.

**Avoid immediately:** Monospace for anything expressive. If a designer finds monospace "cool" or reaches for it as personality, the brief has been misread.

---

## Concept 3 — The Demonstrable System

### Grounding Statement

The typographic system earns authority the way the whitepaper earns authority: by showing its work. Hierarchy levels are defined by explicit, articulable rules. Size intervals are derived from a named principle. The system demonstrates its own logic — which is the direct typographic expression of "authority demonstrated through specificity, not asserted through claims."

`[Hypothesis — Authority Expression]` `[Brief — Section 6]`

---

### Structural Typographic Logic

- **Principle:** A specification names its own parameters. This typographic system names its own rules — and those rules must be legible from the output. A designer looking at a Krutho document should be able to extract the scale, deduce the ratio, and state the logic. The system shows the work.
- **Organising expression:** Authority comes from the demonstrability of the system, not from visual weight or expressive range. The hierarchy is deliberately legible because legibility of structure is the brand's argument. `[Hypothesis — Organising Principle]`
- **Category positioning:** Against IAM/PAM vendors (which use typography to perform authority — heavy weights, enterprise hierarchy, thick visual steps) and against startup visual energy (bold type as personality), Krutho's type system demonstrates precision through structural logic, not through weight or size assertion. `[Brief — Section 9]`

---

### Hierarchy Model

- **Levels:** Four, each defined by a rule that can be stated: Display (heading-of-headings, reserved for primary marketing and document titles), Section (primary navigation and document headings), Body (running prose), Detail (labels, metadata, captions).
- **Differentiation levers:** Size (primary). Weight (secondary, used precisely at one step). Case (for functional register, not hierarchy position). Each level is governed by one defining lever — not a combination of levers stacked for effect.
- **What makes this different:** The size intervals are derived from a named ratio. The weight steps are defined: Regular and Medium. The case strategy is defined by content type. The system can be documented in a table, and that table IS part of the system's expression. `[Hypothesis — Authority through specificity]`
- **Restraint:** More levels than Concept 1, but each is constrained by a single rule. Complexity is earned by the demonstrability of the logic.

---

### Weight & Emphasis Behaviour

- **Weights:** Two from the primary family. Regular (body and detail). Medium (section headings and named technical terms being defined). The Medium must be lighter than the wordmark. `[Logo Settled — Typography primary constraint]`
- **Permitted emphasis:** Medium weight for section headings only. Bold is not in the system — there is no Bold weight. If an argument requires Bold for emphasis, it must be restructured to not require it.
- **Named technical terms:** When the system explicitly names a mechanism — "X.509v3", "EC P-256", "CBOR-encoded capabilities" — the name may be set in Medium as a structural marker that this term is being defined, not used. This is not decoration — it is a named rule in the system.
- **Excluded:** Italic, Bold, any weight above Medium.

---

### Scale & Proportion Strategy

- **Base scale:** Derived from a stated modular ratio. The ratio must be specifiable — not "looks right" but a named value (e.g. 1:1.333, a musical fourth). The specific ratio is secondary to the requirement that it be nameable and consistent.
- **Named sizes:** Four. Not "H1/H2/H3/body" — function names: `display`, `section`, `body`, `detail`. These names are part of the system's expression — they appear in design tokens, documentation, and engineering handoffs.
- **Ratio philosophy:** The ratio is chosen for legibility across the system's key environments. The test: does the ratio between Section and Body create enough visual separation without requiring a weight change? If yes, the ratio is right. `[Hypothesis — Form Logic]`
- **Behaviour across environments:** Fixed. A specification has defined parameter values. Screen vs. print may differ by medium constraint; the named scale holds.

---

### Spacing & Rhythm Logic

- **Letter spacing:** Defined per level and documented. Body: default tracking. Section headings: minimal optical tightening (not aesthetic). Detail/labels: positive tracking with uppercase — functional, not decorative. These values are named.
- **Line height:** Defined per level and documented. Body: 1.5. Section: 1.25. Detail: 1.2. Named.
- **Measure:** Named. 65 characters for body. Shorter for detail. The measure is a documented system parameter, not a preference.
- **The demonstrability principle:** A developer reading the design tokens should be able to reconstruct the typographic system from the parameters alone, without a visual reference. This is the expression of the hypothesis at the system level — the type system is a verifiable specification.

---

### Case Strategy

- **Body:** Sentence case. Named rule: sentence case in all prose.
- **Detail/labels:** Uppercase. Named rule: uppercase with defined positive tracking for any element functioning as a label or identifier.
- **Named technical terms in body:** As-is. The system does not impose case on technical notation — `ECDSA_P256` retains its own case convention. Named rule: technical identifiers use native case.
- **What case must not do:** Perform hierarchy. The system uses size and weight for hierarchy, and case for register type. These are distinct levers with distinct functions — they must not be treated as interchangeable.

---

### Pairing Logic

- **Structure:** Single primary family (geometric grotesk) + monospace for mechanism content. Same structural rationale as Concept 2, but governed by one additional rule: the monospace must have documented metrics (line height, character width) that are named in the same token system as the grotesk. The monospace is not an add-on — it is part of the named, demonstrable system.
- **What the documentation contains:** The type system documentation names both families, documents all size steps, defines all spacing values, and states the derivation logic for each parameter. The documentation IS part of the identity expression. `[Hypothesis — Authority through showing the work]`
- **Wordmark constraint respected:** The grotesk family's named weights do not include the wordmark's weight. `[Logo Settled — Typography primary constraint]`

---

### Cross-Context Behaviour

**Product UI**
The named system maps directly to UI design tokens. Engineers implement from a token file, not from a visual reference. This is the correct expression of the hypothesis in engineering contexts: the system is demonstrable from its parameters. Monospace for mechanism content.

**Marketing / web**
The Display level appears on marketing surfaces. The named ratio ensures it scales at large sizes without requiring a different family. The system's demonstrability is visible to any developer who reads the source — they recognise the same type scale.

**Documentation**
The system is most at home in documentation — where its named levels map to document structure, its spacing parameters map to renderer defaults, and its monospace register maps to code blocks. The documentation type system and the brand type system are the same system.

**Design tokens (public)**
The type system is expressed as design tokens. The tokens are public. A developer who wants to implement Krutho's typographic identity can read the tokens and implement them. This is the open standard logic applied to the typography system itself. `[Brief — Section 1.2 Observation 3]`

---

### What This Makes Impossible

- Arbitrary type choices — every decision requires a named rule
- Typographic improvisation under time pressure ("just make it bigger")
- A third weight
- Any size or spacing value that cannot be derived from the named scale
- Departures from the token system that are not documented as named exceptions

---

### Category & Mis-Signal Risk

- **Risk:** A named, documented type system could read as over-engineered — a design exercise rather than a working identity. The mitigation is use, not documentation. The system is only what it produces in application.
- **Risk:** The four-level hierarchy is more complex than Concept 1. Under pressure, Display may be misused for emphasis rather than its named function. The system must include an explicit rule for when Display is not used.
- **Drift risk:** Adding parameters to the token system without removing anything. The system must have a governance principle: new parameters must be justified, and each addition tested against the hypothesis.

---

### Identity Gate Pressure Test

1. **Does it read as infrastructure rather than a product?**
**Pass.** A type system expressed as public design tokens that a developer can read and implement is infrastructure behaviour — the identity itself operates as a standard.

2. **Does it signal technical credibility to a developer on first contact?**
**Pass.** The demonstrable system — with named parameters and derivable logic — is precisely what technically credible infrastructure looks like to a developer. It is readable, not just visible.

3. **Does it avoid implying that Krutho must be present at verification?**
**Pass.** Typography carries no such implication.

4. **Would a technically skeptical developer trust it?**
**Pass.** A developer who can extract the rules and verify them is in the same relationship to the type system as a developer who can verify a certificate: independent of Krutho, holding nothing on trust.

5. **Could this be the identity of a cryptographic standard, not a startup?**
**Strong pass.** A cryptographic standard publishes its parameters. This type system publishes its parameters. The analogy is structural, not cosmetic.

6. **Does it demonstrate intellectual honesty — does it show the reasoning?**
**Strong pass.** This is the most direct expression of intellectual honesty in the three concepts. Every parameter is nameable; every rule can be stated.

7. **Does it exclude the wrong categories clearly enough?**
**Pass.** The precision of the system excludes the intuitive, personality-driven type choices of IAM/PAM vendors and startups alike.

**Overall: Strong pass on all gates.** Highest gate score of the three concepts. Most direct tracing from the hypothesis.

---

### Exploration Brief

**Begin from:** Name the scale. Decide the ratio. Write it as a rule: "Section is Body × [ratio]. Display is Section × [ratio]." Then prototype one Section heading, two Body paragraphs, and one Detail label. Does the system hold at this minimal level?

**Hierarchy to prototype:** All four levels in a single documentation page. The test is whether the four-level system creates clarity without weight support. If a second weight feels necessary for the distinction to land, reconsider the size ratio before adding weight.

**Tension to test:** Demonstrability vs. readability. A perfectly demonstrable system may have intervals that look mechanical rather than felt. Test whether the ratio produces a system that "reads" before it is "read" — i.e. a user can navigate by intuition, not only by reading size labels. The goal is a system that is demonstrable AND felt.

**Avoid immediately:** Adding a fifth level or a third weight because "the hierarchy doesn't feel rich enough." If the hierarchy doesn't feel rich enough, adjust the scale ratio — do not add complexity.

---

## Structural Comparison

### Divergence Verification

**Concept 1 vs Concept 2:**
Concept 1 uses a single family and achieves all hierarchy through size and case only — weight variation is not a hierarchy lever. Concept 2 introduces a second family (monospace) and uses register change — not size — as the primary hierarchy signal between human-facing and mechanism content. Concept 1's authority is through omission; Concept 2's authority is through structural separation. A designer working from Concept 1 asks: "What can I remove?" A designer working from Concept 2 asks: "Which register does this content belong in?" These produce fundamentally different typographic decisions.

**Concept 1 vs Concept 3:**
Concept 1 refuses complexity — two weights maximum, three levels. Concept 3 embraces documented complexity — four named levels, two defined weights, named spacing parameters, public design tokens. Both reject arbitrary choices, but through different mechanisms: Concept 1 rejects by omission; Concept 3 rejects by naming. A designer from Concept 1 has fewer tools. A designer from Concept 3 has more tools but must document and justify each one. The output looks similar; the internal system discipline is different.

**Concept 2 vs Concept 3:**
Concept 2 is structurally organised around a register distinction (grotesk vs. monospace). Concept 3 is structurally organised around demonstrability (every parameter is named and derived). Both use grotesk + monospace, but their governing logic differs. Concept 2's decisions are driven by: "Which voice is appropriate for this content?" Concept 3's decisions are driven by: "Does this follow from the named rule?" Concept 2 is a communication system. Concept 3 is a specification system.

---

### Hypothesis Coverage

**Which concept most directly expresses the organising principle through typographic behaviour?**
Concept 3. The demonstrable system is the most direct expression of "authority demonstrated through specificity, not asserted through claims." The system shows its work at the typographic level — in the same way the mechanism shows its work at the cryptographic level.

**Which concept takes the greatest structural risk?**
Concept 1. A system with maximum restraint — one weight, three levels — is most vulnerable to execution failure reading as poverty rather than precision. The execution bar is higher than the other two concepts.

**Which concept is most conservative relative to the hypothesis?**
Concept 2. The dual-register system is structurally sound and the least likely to fail under execution pressure. It provides clear decision rules (which register?) without requiring the near-perfection of execution that Concept 1 demands or the governance discipline that Concept 3 requires.

---

## Ranking & Recommendation

### Rank Order

| Rank | Concept | Primary Reason |
|---|---|---|
| 1 | Concept 3 — The Demonstrable System | Most direct tracing from the hypothesis. Shows the work. Scales into public design tokens — an infrastructure expression of the brand's own proposition. Passes every identity gate question, two at strong pass. |
| 2 | Concept 2 — Two Voices, One Structure | Structurally sound, logically grounded, lowest execution risk. The dual register is directly signalled by the logo's `r` letterform and confirmed by the settled constraints. Strong pass on all gates. |
| 3 | Concept 1 — The Omission Standard | Strongest hypothesis logic; highest execution risk. Requires exceptional type selection and near-perfect execution discipline. Not the recommended starting point at this stage of the brand's development. |

### Recommendation

**Concept 3 — The Demonstrable System** is structurally strongest.

It is the most direct typographic expression of Krutho's organising principle. A standard publishes its parameters. This type system publishes its parameters. The analogy is not cosmetic — it is structural. A developer who can read the design tokens and reconstruct the system is in the same relationship to the typography as a verifier who can check a certificate: independent of Krutho, holding nothing on trust.

The system also extends naturally into public design tokens — which is not incidental. If the brand is the format, then the typography system should be expressible as a format: a set of named values that anyone can read, implement, and verify. This is the hypothesis applied to the typography layer.

The condition under which Concept 2 is preferable: if the monospace register distinction is the most important structural signal in Krutho's communication (particularly for developer-facing documentation, CLI work, and certificate display), and the system must operate with absolute register clarity above all other considerations, Concept 2's simplicity of decision-making may outperform Concept 3's greater structural complexity under production conditions. If the team lacks governance capacity to maintain a named token system, Concept 2 is the safer choice.

Do not choose Concept 1 as the exploration starting point. The execution conditions required for it to succeed are higher than the current design stage can support without significant risk of the system reading as unfinished rather than precise.

---

## Human Handoff

When reviewing this document, consider:

1. Does the recommended concept feel right for Krutho's communication needs — not just structurally correct? The system will be used in documentation, CLI, product UI, and marketing. Does Concept 3's demonstrability feel like a strength or a governance overhead?

2. Does the hierarchy model in any concept reflect how Krutho actually needs to communicate across contexts — GitHub README, npm page, documentation, dashboard UI?

3. Is there a typographic logic not represented here that you want to explore? (For example: a system even more minimal than Concept 1, using only one size and one weight throughout; or a system that carries more warmth at the DevRel and community layer.)

4. Are the exploration briefs specific enough to begin system definition from?

5. Does any concept risk drifting toward a category competitor's typographic territory?

Select the concept you want to explore, or introduce a new direction with a grounding statement. Once a direction is selected, run `settle typography` after the exploration phase to record the outcome.
