# Colour System — Concepts v1

**Entity:** Krutho
**Module:** Colour
**Version:** 1
**Sources:** `02_foundational_brief.md`, `04_active_hypothesis.md`, `logo_settled.md`, `typography_settled.md`
**Date:** 2026-03-02

---

## Settled Module Constraints Applied

Logo and typography modules are settled. The following constraints are structurally binding on this output.

**From Logo Settled:**
- The wordmark makes no colour demands and requires none. It is fully functional in black, white reversed, or any single colour.
- Any colour introduced to the system must be justified on structural terms independent of the wordmark. Colour is not a corrective — nothing is missing from the wordmark that colour could supply. `[Logo Settled — Colour]`

**From Typography Settled:**
- Typography inherits colour from the system once defined. No typographic colour decisions were made at the typography module. `[Typography Settled — Colour]`

These constraints are permissive in one direction — colour has no obligation to the wordmark or the type system. They are strict in another: colour must be justified entirely on its own structural terms.

---

## Concept 1 — The Achromatic

### Grounding Statement

If colour asserts, and the identity must not assert, then colour has no permitted role in meaning-making. The system operates entirely in values — black, white, grey. No hue signals authority, position, or belonging. The less the system asserts, the more it proves. `[Hypothesis — Organising Principle]` `[Brief — Section 7]`

If this cannot be written clearly, the concept is not grounded. It can be written clearly.

---

### Structural Colour Logic

- **Principle:** Colour is excluded from meaning-making. The communicative work of the system is done entirely by form, weight, scale, and value contrast. Hue carries nothing.
- **How it expresses the organising principle:** A specification document — RFC, X.509 documentation, NIST publication — has no colour identity. No hue marks authority in a standard; the argument marks authority. To introduce hue is to make a claim the standard does not make. Restraint here is not a stylistic choice — it is the structural consequence of operating in the specification register. `[Hypothesis — Design Consequences]`
- **Category positioning:** Enterprise IAM vendors use colour to perform authority — pervasive corporate blue, security-reassurance green, dashboard-warning amber. Startup products use colour as personality. This system refuses both simultaneously by refusing hue. The refusal is legible to a developer on first contact: this is not an IAM vendor, not a startup. `[Brief — Section 9]`

---

### Role Model

- **Where colour carries authority:** Nowhere. Authority is carried by form, weight, and precision of decision. Hue plays no authority role.
- **Where colour is suppressed:** All backgrounds, borders, decorative elements, and passive text states. Value-based throughout.
- **Where colour signals state or action:** Interactive states use value shift only — darkened backgrounds on hover, inverted states on active, high-contrast borders on focus. The signal is created through contrast of value, not introduction of hue.
- **Status signals:** The system's most operationally stressed point. Resolution: conventional status hues (success, warning, error, info) are accepted as functional system defaults — not brand colour, not derived from brand logic. They are named in the token system as `status-*` and explicitly labelled as functional convention, not system expression. A developer reading the token file sees the distinction immediately. `[Brief — Section 10 — Required Invariants]`
- **What colour is never allowed to do:** Carry brand personality. Mark sections for visual variety. Signal the company's presence or ambition. Appear as a decorative element in any context.

---

### Token Roles

**`colour-surface-primary`**
Default page and screen surface. White or near-white. Must communicate: neutral, open, unencumbered. Must never imply: warmth, premium, or brand character.

**`colour-surface-secondary`**
Panels, code blocks, table rows, sidebar backgrounds. A value step above the primary surface — lighter than mid-grey, distinguishable from primary without introducing hue. Must communicate: structural grouping. Must never imply: categorisation by colour.

**`colour-text-primary`**
All primary prose, headings, labels in active use. Near-black — not pure black, which can read as harsh; a very dark warm-neutral that recedes into precision. Must communicate: authoritative, exact. Must never imply: decoration.

**`colour-text-secondary`**
Captions, metadata, secondary labels, helper text. A defined value step lighter than primary text — legible but clearly subordinate. Must communicate: supporting information. Must never imply: hierarchy created through colour.

**`colour-border`**
All structural dividers, input borders, card edges. Light grey — a value step between the surface and secondary text. Must communicate: structure. Must never imply: personality.

**`colour-interactive`**
Hover and focus states. Value-shift only — slightly darkened surface on hover; near-black border on focus ring. No hue. Must communicate: system response. Must never imply: brand identity.

**`colour-status-success` / `colour-status-warning` / `colour-status-error` / `colour-status-info`**
Functional convention only. Conventional hues adopted for legibility and universally understood semantics. Named in the token file as status tokens, not brand tokens. Their derivation in the documentation states: "conventional system defaults, not derived from brand logic." `[Brief — Section 10]`

---

### Contrast & Accessibility Strategy

- **Philosophy:** Maximum legibility everywhere, without exception. No contrast reduction for aesthetic effect. The brand is built on precision and demonstrability — inaccessible text contradicts both. An argument the user cannot read is an argument that does not exist.
- **Text on primary surface:** WCAG AAA target for all body text and headings. AA minimum for all other text.
- **Interactive states:** Focus rings must achieve sufficient contrast to be immediately visible. Accessibility is structural here — not compliance, not courtesy.
- **Status signals:** Must achieve WCAG AA in their application contexts.
- **What must always remain readable regardless of context:** Every word of prose, every code block, every label. No exceptions.

---

### Behaviour by Context

**Product UI**
The operationally hardest context for this concept. All navigation, content, and form elements operate in value. Interactive states communicate through value shift. Status signals use conventional hues as labelled exceptions. The UI reads as a structured form or specification view — which is precisely the correct register. `[Brief — Section 9]`

**Marketing / web**
Same system. No colour budget for marketing visual variety. CTAs use inverted value states (dark background, white text) rather than coloured buttons. The discipline is consistent across contexts — which is itself a structural argument about Krutho's identity.

**Documentation**
The most natural environment for this concept. Prose in value-based type. Code blocks on secondary surface. No syntax highlighting in brand surfaces. The documentation looks like documentation — not a product.

**Print / physical**
The simplest environment. The system translates without adaptation.

---

### What This Makes Impossible

- Any hue as a brand signal or identity element
- Coloured backgrounds for sections, cards, or panels
- Gradients of any kind
- Coloured iconography in passive or decorative states
- Saturated or hue-differentiated interactive states
- Visual differentiation of product areas or content types through colour
- Colour used to express warmth, approachability, or company personality

---

### Category & Mis-Signal Risk

- **Risk:** At this brand stage, achromatic can read as either precise and authoritative (the intended register) or unbuilt (no design investment). The difference is the quality of every other decision — typography, spatial system, proportion, form. The execution bar is extremely high. `[Hypothesis — Structural Risks]`
- **Risk:** At product UI scale, zero hue creates interaction design pressure. Hover states, active states, and focus indicators must communicate clearly without colour differentiation. Under production pressure, a designer will introduce "just one subtle accent." This must be named as a system failure, not a practical compromise.
- **Mitigation:** The single-function rule for status tokens (labelled exceptions only) creates a defensible position. The system is achromatic by principle; functional exceptions are named and bounded.
- **Drift:** The most likely drift path is incremental — one component at a time. Token governance must make each addition require explicit justification. No unnamed colour is permitted.

---

### Identity Gate Pressure Test

1. **Does it read as infrastructure rather than a product?**
**Strong pass.** An achromatic system reads as exactly the authority register of specifications and protocols. `[Brief — Section 10]`

2. **Does it signal technical credibility to a developer on first contact?**
**Conditional.** At high execution quality, yes — it reads as precise and deliberate. At ordinary execution quality, it reads as unbuilt. The concept has no margin for imprecision. `[Hypothesis — Execution failure risk]`

3. **Does it avoid implying that Krutho must be present at verification?**
**Pass.** Colour carries no such implication.

4. **Would a technically skeptical developer trust it?**
**Conditional.** Trust requires the execution to hold. If the achromatic system looks like a CSS reset with no design decisions, it fails. If it looks like everything has been precisely considered, it passes.

5. **Could this be the identity of a cryptographic standard, not a startup?**
**Strong pass.** RFCs, NIST publications, X.509 documentation — the standards register is precisely achromatic. This is the most direct alignment with that register.

6. **Does it demonstrate intellectual honesty?**
**Pass.** No colour means no personality claim. The system makes no visual argument about Krutho's character that cannot be supported by form.

7. **Does it exclude the wrong categories clearly enough?**
**Strong pass.** Enterprise IAM blue, AI gradient, startup colour-personality — all excluded simultaneously and definitively.

**Overall: Pass with high execution dependency.** Most authentic to the specification register. Highest operational risk at product UI scale. Most brittle under production pressure. The concept that requires everything else to be perfect.

---

### Exploration Brief

**Begin from:** Design a product UI screen in pure values — no hue anywhere except labelled status tokens. Test whether interactive states are legible without hue. The question is not whether it looks good — it is whether it is functionally clear. If it is not clear, the concept cannot be executed at this stage.

**Primary contrast decision:** Define the value range. How dark is `colour-text-primary`? How light is `colour-surface-secondary`? How subtle is `colour-border`? The value range defines everything — there is no other variable.

**Tension to test:** Precision vs. poverty. Set a GitHub README, a documentation page, and a product dashboard in the same system. Where does the absence of hue feel inevitable? Where does it feel like something is missing? The answer tells you whether the concept can hold.

**Avoid immediately:** Introducing a "subtle" accent because the system "needs something." That is the moment the concept has failed — and the signal that Concept 2 is the right choice.

---

## Concept 2 — The Signal

### Grounding Statement

Colour earns its presence exactly once — as a structural signal at points of system state and interaction. Every element earns its presence through precision of decision; the single accent earns its presence by being the only one and having an unambiguous function. `[Hypothesis — Invariant 5]` `[Brief — Section 9]`

If this cannot be written clearly, the concept is not grounded. It can be written clearly.

---

### Structural Colour Logic

- **Principle:** One hue. One function. The accent marks where something is active, interactive, or currently significant. The base system is near-achromatic — value-based throughout. The accent appears only where a system state needs naming. Its absence is the neutral condition; its presence is information.
- **How it expresses the organising principle:** A signal light is not a decoration — it is present only when it is active, and its presence means something specific. The accent behaves identically: it appears at interactive elements (primary actions, links, buttons), active and selected states, and focus indicators. It does not appear in backgrounds, passive states, headings, or decorative elements. Colour earns its presence here by having exactly one job and doing only that job. `[Hypothesis — Design Consequences — Form Logic]`
- **Category positioning:** Enterprise IAM vendors use colour pervasively as brand identity — corporate blue across all surfaces, communicating "you are inside our system." Startup products use colour as personality — brand accent on cards, backgrounds, illustrations. This system uses colour as signal, not identity and not personality. One function. Never decorative. The developer reading the system can extract the rule: accent = active state. One rule, no exceptions. This is legible as a different kind of system from both categories. `[Brief — Section 9]`

---

### Role Model

- **Where colour carries authority:** At the exact point of system activity. The accent marks: primary interactive elements (buttons, links), active navigation state, selected state, focus ring, toggle on-state.
- **Where colour is suppressed:** All passive states, all backgrounds, all borders, all text not functioning as a link, all iconography in non-interactive contexts. The default system condition is value-based.
- **Where colour signals state:** The accent is the state signal. When the accent appears, the element is active or actionable. When it is absent, the element is passive. The system is readable at the structural level: colour tells you what you can do.
- **Status signals:** Named and governed separately from the accent. Success, warning, error, info hues are functional convention — named as `status-*` in the token system, explicitly distinct from `colour-accent`. The status hues are not related to the accent; they are adopted convention. `[Brief — Section 10]`
- **What colour is never allowed to do:** Appear in any passive or decorative context. Serve as brand personality or company identity signal. Appear in a heading, a background, or a non-interactive icon. The moment the accent appears outside its signal function, the system has drifted.

---

### Token Roles

**`colour-surface-primary`**
White or near-white. Neutral. Must communicate: open, unencumbered. Must never imply: warmth or brand character.

**`colour-surface-secondary`**
Panels, code blocks, grouped content. Value-based — a step above primary surface. Must communicate: structural grouping. No hue.

**`colour-text-primary`**
Near-black. All primary prose, headings, labels. Must communicate: authoritative, exact. Must never imply: decoration.

**`colour-text-secondary`**
Mid-value grey. Supporting information, captions, metadata. Must communicate: subordinate but legible. Must never imply: hierarchy through colour.

**`colour-border`**
Light grey. Structural dividers, input borders, card edges. Must communicate: structure, separation. Must never imply: personality.

**`colour-accent`**
Single precision hue. Appears exclusively at: primary button fill, link text, active navigation state, selected state, focus ring, toggle on-state. Must communicate: this element is interactive or currently active. Must never imply: brand personality or company identity. The hue must not sit in corporate blue territory (IAM vendor signal), warm orange/amber territory (startup approachability), green territory (status convention contamination), or electric cyan/blue territory (AI company aesthetic). Its specific position is the designer's decision, governed by these exclusions and by the function requirement: it must read as precision signal, not brand colour. `[Brief — Section 9]` `[Hypothesis — What This Makes Impossible]`

**`colour-interactive-hover`**
A value shift from the surface — not hue. The accent is already the signal; hover is a subordinate confirmation that does not need a second colour.

**`colour-focus-ring`**
The accent at full saturation, as a border. The focus ring is a system signal with accessibility weight — it must be immediately visible. This is one of the accent's permitted appearances.

**`colour-status-success` / `colour-status-warning` / `colour-status-error` / `colour-status-info`**
Functional convention. Conventional hues for established semantic meaning. Named as `status-*`, explicitly separate from `colour-accent`. Token documentation states derivation: "conventional system defaults for semantic clarity — not derived from brand logic."

---

### Contrast & Accessibility Strategy

- **Philosophy:** The accent must achieve WCAG AA on `colour-surface-primary` for interactive link text. If the chosen hue cannot achieve this at a saturation that reads as precise rather than aggressive, its value must be adjusted. Accessibility is not a constraint imposed on the system — it is part of the derivation logic.
- **Text:** WCAG AAA target for all body text on primary surface. AA minimum for all other text.
- **Focus ring:** The accent as focus indicator must be high-contrast. The focus ring is not a subtlety — it is a system requirement.
- **Status signals:** All must achieve WCAG AA in application contexts.
- **What must always remain readable:** All prose, all code, all interactive labels, all status messages.

---

### Behaviour by Context

**Product UI**
The accent appears at primary CTAs, navigation active states, form field focus, toggle active state, selected items. Everywhere else: value-based. The UI has one colour and it is always specific. A user navigating the product learns quickly: if the accent appears, the element is interactive or active. `[Brief — Section 9]`

**Marketing / web**
The accent appears at the primary CTA only. Marketing surfaces have lower interactive density than UI — the accent appears less frequently, which raises its signal value. The page is achromatic except at the one point where an action is invited.

**Documentation**
The accent appears at hyperlinks (inline text links, cross-references). All other elements are value-based. Code blocks on secondary surface. No coloured syntax highlighting in brand surfaces. The link behaviour is the only colour in the documentation — which means every instance of the accent is telling the reader "you can go somewhere."

**CLI / terminal**
Not governed by the brand colour system. Terminal conventions apply.

---

### What This Makes Impossible

- Multiple accent colours — the system has one hue, serving one function
- Coloured backgrounds, panels, or decorative surfaces
- Gradient of any kind
- The accent used in a static, non-interactive, non-signal context
- Colour used for content differentiation, section marking, or visual variety
- Brand colour expressed through anything other than the signal function
- Any colour that cannot be assigned to a named functional role

---

### Category & Mis-Signal Risk

- **Primary risk:** The accent hue choice is the single highest-stakes decision in this concept. The wrong hue will read as a category signal before the system's logic is understood. Corporate blue → IAM vendor. Electric cyan → AI company. Warm amber → startup personality. Teal → SaaS product. The hue must be chosen to avoid all of these territories while remaining legible as a precision signal. `[Brief — Section 9]` `[Hypothesis — What This Makes Impossible]`
- **Secondary risk:** Under production pressure, the accent will be used outside its signal function. "Just for this one heading to make the section feel active." This must be named in system documentation as a structural failure, not a practical shortcut. The single-function rule is the governance mechanism.
- **Mitigation:** The rule is simple enough to enforce: accent = system state signal. Every use of the accent must answer one question: "Is this element interactive or currently active?" If no, the accent does not appear. Simple governance is resilient governance.
- **Drift:** The most likely failure mode is gradual. The first undisciplined use of the accent is the signal that governance has failed. The token system should make this visible — if the accent appears outside its defined roles, it is using an undefined token, which is a named system error.

---

### Identity Gate Pressure Test

1. **Does it read as infrastructure rather than a product?**
**Pass.** A near-achromatic system with a single functional signal reads as specification-grade — not a branded product. The absence of pervasive colour is itself a category statement. `[Brief — Section 10]`

2. **Does it signal technical credibility to a developer on first contact?**
**Pass.** One accent, one function, precise application — this is legible as deliberate. A developer can extract the rule immediately: accent = signal. No explanation required. `[Brief — Section 10]`

3. **Does it avoid implying that Krutho must be present at verification?**
**Pass.** Colour carries no such implication.

4. **Would a technically skeptical developer trust it?**
**Pass.** The single-function rule is verifiable by observation. The developer can confirm that the accent appears only at interactive states. When a system follows its own rules visibly, it earns technical trust. `[Brief — Section 10]`

5. **Could this be the identity of a cryptographic standard, not a startup?**
**Pass.** Near-achromatic with a single functional signal is consistent with how technical infrastructure systems — developer tools, protocol documentation, specification renderers — use colour: sparingly, functionally, with discipline.

6. **Does it demonstrate intellectual honesty?**
**Pass.** The logic is extractable. Signal behaviour means signal. The system does not claim more colour authority than it uses.

7. **Does it exclude the wrong categories clearly enough?**
**Pass.** Excluding multi-colour brand palettes and pervasive accent application excludes both enterprise IAM vendor aesthetics and startup personality-through-colour simultaneously. `[Brief — Section 9]`

**Overall: Strong pass on all gates.** Most operationally sound. Holds the hypothesis through a simple, auditable rule. Lowest drift risk of the three concepts because the governance rule is simple enough to enforce under production pressure.

---

### Exploration Brief

**Begin from:** Choose the accent hue. This is the only hue decision in the system and it must be precise — not "a blue that feels technical" but a specific, justifiable position. Test it against three questions before committing: Does it read as signal (not personality)? Does it avoid all the named category territories? Does it achieve WCAG AA on white at a saturation that feels exact rather than aggressive?

**Primary contrast decision:** Accent saturation and value. The target register: precise, not warm; present, not aggressive; signal, not brand colour. Too saturated and it reads as personality. Too muted and it fails to signal at interactive density.

**Test:** The primary CTA button in the accent colour against pure-value prose. Does the accent feel like a signal going on — information appearing — or does it feel like a design preference? The distinction is felt before it is articulated. Test it in the GitHub README context and the product dashboard simultaneously.

**Avoid immediately:** Using the accent anywhere it is not an interactive or active-state signal. The first undisciplined instance is the moment the system becomes Concept 3 without Concept 3's governance structure.

---

## Concept 3 — The Named System

### Grounding Statement

The colour system earns authority the way the whitepaper earns authority — by showing its work. A named, minimal palette with documented derivation, expressed as design tokens alongside the typography system. A designer or developer can read the token file, extract the colour logic, and reconstruct the system without a visual reference. `[Hypothesis — Authority Expression]` `[Brief — Section 6]`

If this cannot be written clearly, the concept is not grounded. It can be written clearly.

---

### Structural Colour Logic

- **Principle:** Every colour token has three properties: a name (the function), a value (the designer's decision constrained by derivation rules), and a derivation (why this value exists). Nothing unnamed is permitted. Nothing without a derivation exists. The system shows its work at the token level.
- **How it expresses the organising principle:** A specification names its parameters. This colour system names its parameters — and the names precede the values. A designer does not choose a colour and then name it; they define the function, state the derivation constraints, and then choose the value that satisfies those constraints. Authority is demonstrated by the specificity of the rules, not by the visual weight of the palette. `[Hypothesis — Organising Principle]` `[Hypothesis — Design Consequences]`
- **Category positioning:** Most design systems have a palette without a derivation rationale — colours chosen by aesthetic preference and named post-hoc. This system has a palette because of derivation rules. The reasoning is the differentiator. A developer reading the token file sees the rules, not just the values. `[Brief — Section 6]`

---

### Role Model

- **Where colour carries authority:** At the level of the named token and its documented function. Authority is not visual weight or saturation — it is the demonstrability of the rule.
- **Where colour is suppressed:** Outside the named token system. No colours exist outside the token file. Any colour that cannot be named and derived does not exist in this system.
- **Where colour signals state:** The accent token, governed by the same single-function rule as Concept 2. Status tokens, named and derived as convention-based functional signals.
- **What colour is never allowed to do:** Exist without a token name. Exist without a derivation rule. Appear in any context that has not been specified in the system documentation.

---

### Token Roles

Each token below requires three documented properties: name, value, derivation. The values are the designer's decision, constrained by the derivation rules. The derivation is what makes this a specification rather than a palette.

**`colour-surface-primary`**
Function: Default page and screen surface. Derivation rule: maximum legibility — primary text must achieve WCAG AAA on this surface. Must communicate: open, neutral. Must never imply: warmth or brand personality.

**`colour-surface-secondary`**
Function: Grouped content — panels, code blocks, table rows. Derivation rule: distinguishable from primary surface by value step; must not introduce hue; must not create significant contrast with text (it is a grouping surface, not a contrast surface). Must communicate: structural grouping.

**`colour-text-primary`**
Function: All primary prose, headings, and labels in use. Derivation rule: WCAG AAA on `colour-surface-primary`. Must communicate: authoritative, precise. The derivation specifies both the contrast requirement and the exclusion of pure black (which can read as harsh — a slightly warm near-black is derivable from the precision requirement).

**`colour-text-secondary`**
Function: Supporting text — captions, metadata, helper text, disabled states. Derivation rule: WCAG AA on `colour-surface-primary`; value step below `colour-text-primary` sufficient to read as subordinate. Must communicate: supporting information.

**`colour-border`**
Function: All structural dividers, input borders, card edges. Derivation rule: a defined step between `colour-surface-secondary` and `colour-text-secondary` on the value scale — creates visible structure without drawing attention. No hue.

**`colour-accent`**
Function: Interactive and active state signal. Identical single-function rule to Concept 2. Derivation rule: must achieve WCAG AA on `colour-surface-primary` for interactive text; must not occupy enterprise blue, warm personality, AI gradient, or green/status territories; must read as precision signal. The derivation rule specifies the exclusions and the function requirement; the specific hue is derived from those constraints. `[Brief — Section 9]` `[Hypothesis — What This Makes Impossible]`

**`colour-accent-subtle`**
Function: Background wash for active containers, selected rows, highlighted sections. A very low-saturation tint derived from `colour-accent`. Derivation rule: low enough saturation that it reads as grouping, not colour statement; derived from `colour-accent` to maintain system coherence. Must communicate: this area is related to an active or selected element.

**`colour-status-success` / `colour-status-warning` / `colour-status-error` / `colour-status-info`**
Function: System state signals. Derivation rule: conventional semantic hues adopted for universal legibility — green/amber/red/blue-info. Token documentation states: "conventional system defaults — derivation is semantic convention, not aesthetic derivation from brand logic. These tokens are part of the specification to complete it; they are not brand colour." `[Brief — Section 10]`

Each token in the published token file includes all three properties. The file is published alongside the typography tokens.

---

### Contrast & Accessibility Strategy

- **Philosophy:** Accessibility requirements are part of the derivation rules, not constraints applied after the fact. Each token's derivation rule includes the contrast requirement that applies to it. The token file documents both the value and the accessibility target it satisfies.
- **`colour-text-primary` on `colour-surface-primary`:** WCAG AAA target. Named in the derivation.
- **`colour-accent` as interactive text:** WCAG AA minimum. Named in the derivation. If the chosen hue cannot achieve AA at a saturation consistent with the signal character requirement, the hue must be replaced — not the requirement.
- **`colour-text-secondary` on `colour-surface-primary`:** WCAG AA minimum. Named in the derivation.
- **Status signals:** WCAG AA in application contexts. Named in the derivation.
- **The structural argument:** A system that shows its work shows its accessibility reasoning. Contrast targets are not bolted on — they are part of the specification.

---

### Behaviour by Context

**Product UI**
Engineers implement from the token file. No visual reference required to build a conformant UI — the token names and their documented functions are sufficient. This is the direct expression of "the identity itself operates as infrastructure." `[Brief — Section 10 — Required Invariants]`

**Marketing / web**
Same token system. The `colour-accent` appears at CTAs; `colour-accent-subtle` may appear in highlighted sections that name active capability. The palette is smaller than most marketing systems — which is the structural argument made visible.

**Documentation**
Prose uses text tokens. Code blocks use surface tokens. Links use `colour-accent`. No coloured syntax highlighting. The type and colour systems are the same system whether you are reading the specification document or the product documentation — one system, all surfaces. `[Typography Settled — Cross-context behaviour]`

**Design tokens (public)**
The colour token file is published alongside the typography token file. A developer implementing Krutho's design system implements both from token files. This is not a documentation supplement — it is the primary implementation specification. The public token file is part of the identity expression.

---

### What This Makes Impossible

- Any colour decision made outside the token system
- Palette expansion without documented derivation and function for each new token
- Visual-variety use of colour — section colours, content-area differentiation, decorative backgrounds
- Any colour that can be identified but not named in the token system
- A colour palette that cannot be documented in a table of names, values, and derivations

---

### Category & Mis-Signal Risk

- **Risk:** A publicly documented, named colour system could read as over-engineered at this brand stage. The mitigation is the same as for the typography system: the system is only what it produces in application. If the output reads as precise, the documentation is evidence of the reasoning; it does not create the effect on its own. `[Hypothesis — Structural Risks]`
- **Risk:** `colour-accent-subtle` introduces a surface-level colour that Concept 2 does not have. Under production pressure it will be used outside its defined function. The derivation rule and function constraint must be tight — `colour-accent-subtle` appears only as a background wash for content directly associated with an active or selected `colour-accent` element.
- **Risk:** The accent hue choice carries the same stakes as in Concept 2. The derivation rules specify the exclusions but do not specify the value. The designer must choose a hue that satisfies the derivation constraints without entering category territory.
- **Drift:** Adding tokens without derivation documentation. Every addition to the token system must include a name, a value, a derivation rule, and a function. If a designer cannot write the derivation, the token does not exist.

---

### Identity Gate Pressure Test

1. **Does it read as infrastructure rather than a product?**
**Strong pass.** A colour system expressed as public design tokens with documented derivation is infrastructure behaviour. The identity operates as a specification at the colour layer — the same way it does at the typography layer. `[Brief — Section 10]`

2. **Does it signal technical credibility to a developer on first contact?**
**Pass.** A developer who reads the token file and can reconstruct the system is in a specific relationship with the brand: independent and verifiable. This is the same posture the mechanism requires of verifiers. `[Brief — Section 10]`

3. **Does it avoid implying that Krutho must be present at verification?**
**Pass.** Colour carries no such implication.

4. **Would a technically skeptical developer trust it?**
**Pass.** The derivation documentation is the evidence. There is no "trust us" in a token file with stated derivation rules. The developer can read the constraints and verify the values against them. `[Brief — Section 10]`

5. **Could this be the identity of a cryptographic standard, not a startup?**
**Strong pass.** Cryptographic standards publish their parameters. This colour system publishes its parameters. The analogy is structural. `[Brief — Section 10]`

6. **Does it demonstrate intellectual honesty?**
**Strong pass.** The most direct expression of intellectual honesty across the three concepts. Every colour token's derivation is stated and verifiable. Nothing is asserted that cannot be demonstrated.

7. **Does it exclude the wrong categories clearly enough?**
**Pass.** A system governed by derivation rules excludes intuitive, personality-driven colour decisions. IAM vendor aesthetics and startup personality-through-colour both depend on aesthetic instinct, not derivation logic. `[Brief — Section 9]`

**Overall: Strong pass on all gates.** Highest hypothesis alignment across the three concepts. Requires the most governance discipline to maintain. The concept most dependent on the team's willingness to enforce the derivation requirement over time.

---

### Exploration Brief

**Begin from:** Write the token names before choosing any values. Define: `colour-surface-primary`, `colour-surface-secondary`, `colour-text-primary`, `colour-text-secondary`, `colour-border`, `colour-accent`, `colour-accent-subtle`, and the four status tokens. Then write the derivation rule for each. Only after the rules are written do the values become choices — and the choices are now constrained by the rules.

**Primary contrast decision:** The accent derivation. State the constraint before choosing the value: what must this hue avoid (named category territories), what must it achieve (WCAG AA on primary surface for interactive text), and what must it communicate (precision signal, not brand personality). The hue that satisfies all three constraints is the correct value.

**Tension to test:** Completeness vs. parsimony. The Named System has more tokens than Concept 2 — `colour-accent-subtle` in particular adds expressiveness. Does that additional token produce a better system, or does it introduce drift risk that the governance structure cannot contain under production conditions?

**Avoid immediately:** Adding tokens before writing their derivation rules. The system grows by derivation, not by necessity. If a designer reaches for a new token because "we need a colour here," the derivation must be written first. If the derivation cannot be written, the colour does not belong.

---

## Concept 4 — The Achromatic Foundation

### Grounding Statement

The system is achromatic. This is the governing principle, not a starting point. One precision accent hue is admitted as the minimum necessary departure from that principle — functioning exclusively as an interactive state signal where value alone is insufficient. The system does not have a brand colour; it has an achromatic default and one named exception. `[Hypothesis — Organising Principle]` `[Hypothesis — Invariant 5]` `[Brief — Section 7]`

If this cannot be written clearly, the concept is not grounded. It can be written clearly.

---

### Structural Colour Logic

- **Principle:** Achromatic is the governing default. The designer's first question is always "is this achromatic?" not "what colour should this be?" The accent is admitted only when that question produces a product failure — when a value-only solution would make interactive states genuinely unclear at product UI scale. The accent is the minimum colour the product requires, not the minimum colour the system permits.
- **How this differs from Concept 1:** Concept 1 tests whether an entirely value-based system can operate without hue. Concept 4 accepts that one hue is the minimum necessary exception for interactive legibility — and names it, bounds it, and admits it for that purpose only. The achromatic principle is held; the product failure of pure value-only interaction is acknowledged and resolved by the smallest possible admission.
- **How this differs from Concept 2:** Concept 2 frames the accent as the system's functional colour property — positive, present, and justified by its signal function. Concept 4 frames the accent as a departure from an achromatic system — the exception that proves the rule. A designer from Concept 2 asks "is this a signal?" A designer from Concept 4 asks "is this achromatic?" first, and reaches for the accent only when that answer is no and no value-based alternative exists. The governing posture is different even when the output is visually similar.
- **The structural argument:** Maximum restraint that does not fail the product. The achromatic default is the argument; the accent is the concession to operational reality. The system admits that one hue is necessary without pretending the colour is anything other than a functional minimum. `[Hypothesis — Design Consequences — Form Logic]`
- **Category positioning:** The governing question — "is this achromatic?" — excludes all category aesthetics by default. Enterprise IAM blue, AI gradient, startup colour-personality: none can pass the achromatic test. The single accent exception is narrow enough that it cannot carry a category signal if it is held to its function. `[Brief — Section 9]`

---

### Role Model

- **The default state:** Achromatic. All surfaces, all borders, all text, all iconography, all passive states — value only. This is not minimalism as style; it is the principle enforced as default.
- **The accent:** Admitted only where value-only would produce operational failure. Specifically: primary interactive elements (buttons, links), active and selected states, focus indicator. At every other point, the question "could this be achromatic?" must be asked, and the answer must be no before the accent appears.
- **The test for accent admission:** "Would a value-based solution fail here?" If the interactive state would be ambiguous without hue, the accent is permitted. If a value shift is sufficient, the accent is not used. This produces a more constrained accent footprint than Concept 2 — the accent appears at fewer points because the test is stricter.
- **Status signals:** Conventional functional defaults, named as `status-*`. Not related to the accent. Not derived from brand logic. Admitted on the same basis as in Concept 1 — functional convention, explicitly labelled as such in the token file.
- **What colour is never allowed to do:** Appear as a default. Appear where a value-based solution would be sufficient. Carry brand personality. Mark sections or content types. Appear in headings, backgrounds, or decorative elements.

---

### Token Roles

The token structure is close to Concept 2. The governing difference is documented in the derivation logic of each token — the achromatic default is stated, and the accent's admission is named as an exception rather than a property.

**`colour-surface-primary`**
White or near-white. Achromatic. Must communicate: open, neutral. Must never imply: warmth or brand character.

**`colour-surface-secondary`**
Value step above primary surface. Achromatic. Must communicate: structural grouping. No hue.

**`colour-text-primary`**
Near-black. All primary prose, headings, labels. Achromatic. Must communicate: authoritative, precise.

**`colour-text-secondary`**
Mid-value grey. Supporting information. Achromatic. Must communicate: subordinate but legible.

**`colour-border`**
Light grey. Structural dividers, input borders. Achromatic. Must communicate: structure.

**`colour-interactive-passive`**
Value shift only. Hover states, background on hover — a slight darkening of the surface, no hue. Used wherever the interactive signal does not require the accent.

**`colour-accent`**
Single precision hue. Admitted as the minimum necessary exception to the achromatic default. Appears at: primary button fill, link text, active navigation state, selected state, focus ring. Token derivation documentation explicitly states: "this token represents a departure from the achromatic governing principle, admitted for interactive legibility only. It is not a brand colour." The hue must not occupy enterprise blue, warm personality, AI gradient, or green/status territories. It must read as a precise functional signal — not a colour choice. `[Brief — Section 9]` `[Hypothesis — What This Makes Impossible]`

**`colour-focus-ring`**
`colour-accent` at full contrast as a border. Accessibility-mandatory. Non-negotiable appearance of the accent.

**`colour-status-success` / `colour-status-warning` / `colour-status-error` / `colour-status-info`**
Conventional functional defaults. Named as `status-*`. Explicitly not derived from `colour-accent` or from brand logic. Token documentation: "conventional system defaults — semantic convention, not brand expression."

---

### Contrast & Accessibility Strategy

- **Philosophy:** The achromatic foundation makes contrast a primary design tool. Value contrast must carry all the communicative weight in passive states. This demands more careful calibration of the value scale than Concept 2 — the grey range must be precise enough to communicate hierarchy without colour support.
- **Text on primary surface:** WCAG AAA target for all body text. This is structural — the achromatic system has no other mechanism for creating legibility.
- **`colour-accent` on primary surface:** WCAG AA minimum for interactive link text. Stated in the token derivation rule as a constraint the hue must satisfy.
- **Focus ring:** High contrast. Non-negotiable. The focus ring is one of the accent's permitted appearances.
- **What must always remain readable:** All prose, all code, all interactive labels, all status messages — without exception.

---

### Behaviour by Context

**Product UI**
The strictest test for this concept. Interactive states use the accent where value alone is insufficient; all other elements are achromatic. The UI reads as a structured specification view. Where Concept 2 permits the accent wherever it qualifies as a signal, Concept 4 withholds it wherever a value solution is viable. The result: the accent appears less frequently, which raises its signal value each time it appears. `[Brief — Section 9]`

**Marketing / web**
Near-achromatic throughout. The accent appears at the primary CTA. Everything else — headings, body, structural elements, supporting content — is value-based. The marketing surface does not compensate for the absence of colour with visual complexity.

**Documentation**
The most natural context. Prose in value-based type. Code blocks on secondary surface. Links in accent. The documentation looks like documentation — which is precisely the specification register.

**CLI / terminal**
Not governed by the brand colour system.

---

### What This Makes Impossible

- Colour as a default in any context
- The accent appearing where a value-based solution would suffice
- Multiple accent colours or any broadening of the accent's admission criteria
- Coloured backgrounds, sections, or decorative elements
- Any colour that cannot pass the test: "is the achromatic solution here insufficient?"
- Colour used for visual variety, personality, or brand expression

---

### Category & Mis-Signal Risk

- **Primary risk:** The accent hue choice carries the same stakes as in Concept 2. The hue must avoid all named category territories. The achromatic default makes the accent more prominent in relative terms — it appears against a completely neutral field, which amplifies any category signal it might carry. The choice must be more precise, not less. `[Brief — Section 9]`
- **Secondary risk:** Under production pressure, the test "would a value-based solution fail here?" will be answered loosely — "it would be better with colour" will substitute for "it would fail without colour." The distinction must be named explicitly in system documentation as the governance rule.
- **Structural advantage over Concept 2:** The governing default is stricter. Where Concept 2's drift risk is "the accent appears in a non-signal context," Concept 4's drift risk requires overriding an explicit achromatic default. The governance posture is more resistant because the default is more defensible.
- **Drift:** Identical accent territory to Concept 2. Governed by the achromatic default first, function test second. Both gates must be cleared for the accent to appear.

---

### Identity Gate Pressure Test

1. **Does it read as infrastructure rather than a product?**
**Strong pass.** An achromatic system with a single, bounded functional exception reads unambiguously as specification-grade — not a product, not a brand system. `[Brief — Section 10]`

2. **Does it signal technical credibility to a developer on first contact?**
**Pass.** The achromatic default communicates deliberate precision. The accent's functional restraint — appearing only at interaction, nowhere else — is legible as a system rule to a developer who reads systems by observation. `[Brief — Section 10]`

3. **Does it avoid implying that Krutho must be present at verification?**
**Pass.** Colour carries no such implication.

4. **Would a technically skeptical developer trust it?**
**Pass.** The system has two verifiable rules: "achromatic by default" and "accent at interaction only." Both can be confirmed by observation. A developer can verify compliance without a guide. `[Brief — Section 10]`

5. **Could this be the identity of a cryptographic standard, not a startup?**
**Strong pass.** The achromatic foundation is the specification register. The single functional exception does not compromise it — it names the minimum concession to product operability, which is itself a precise position. `[Brief — Section 10]`

6. **Does it demonstrate intellectual honesty?**
**Pass.** The system names what it is (achromatic) and names its one departure (functional minimum for interactive legibility). There is no gap between the stated principle and the observed behaviour.

7. **Does it exclude the wrong categories clearly enough?**
**Strong pass.** The achromatic default excludes every category aesthetic simultaneously and structurally — not by avoiding specific colours but by refusing colour as a default. `[Brief — Section 9]`

**Overall: Strong pass on all gates.** The most precisely calibrated position. Holds the achromatic principle at the governing level while acknowledging the operational minimum. Higher drift resistance than Concept 2 because the default is stricter. Requires the same precision in accent hue selection.

---

### Exploration Brief

**Begin from:** Confirm the achromatic system holds before introducing the accent. Build a complete UI screen — including primary CTA, navigation, form fields — in pure values. Identify every point where interactive legibility genuinely fails without hue. That list defines the accent's permitted territory. Only then introduce the accent, only at those points.

**Primary contrast decision:** The value range. Since the system is achromatic in all passive states, the value scale must carry all hierarchy signals. The grey range must be precise enough to communicate primary text, secondary text, borders, secondary surfaces, and hover states — all in value, without hue. If the value range collapses, the concept fails before the accent is needed.

**Test:** Side by side — the same primary CTA, navigation active state, and form field focus in pure value versus with the accent. For each instance, the question is: "does the value solution fail?" Not "is the accent better?" — "does the value solution fail?" Only failures justify the accent.

**Avoid immediately:** Applying the accent wherever it qualifies as a signal (Concept 2's logic). The stricter test is "would the achromatic version fail?" Apply that test at every instance. The accent footprint should be smaller than Concept 2's at the end of exploration — if it is not, the achromatic default is not being enforced.

---

## Structural Comparison

### Divergence Verification

**Concept 1 vs Concept 2:**
Concept 1 excludes hue entirely — value shift alone communicates interactive states. Concept 2 admits one accent hue as a positive functional property of the system. A button in Concept 1 is distinguished from prose by value and weight alone; in Concept 2 it uses the accent fill. The governing question is different at every design decision point.

**Concept 1 vs Concept 3:**
Concept 1 is governed by absence — no colour, no named palette beyond functional status convention. Concept 3 is governed by documentation — every colour is named, derived, and published. Concept 1 has no palette. Concept 3 has a complete named token system. Both can appear visually similar; the designer's decision process and governance structure are different.

**Concept 1 vs Concept 4:**
Both are governed by the achromatic principle. The difference is their resolution to interactive state legibility. Concept 1 tests whether pure value is sufficient throughout. Concept 4 accepts that one hue is the minimum necessary exception at product UI scale, admits it, and names the admission explicitly. Concept 1 asks "can we do this without colour?" Concept 4 answers "we can, except at this one point, and here is the justification."

**Concept 2 vs Concept 3:**
Both admit a single accent hue. Concept 2 governs by a single function rule ("is this a signal?"). Concept 3 governs by derivation documentation ("is this in the named system?"). Concept 2 is simpler to govern. Concept 3 is more complete. Both can produce visually similar output; their internal discipline and drift resistance differ.

**Concept 2 vs Concept 4:**
Visually the most similar pairing. Both: near-achromatic base, one accent, single signal function. The structural difference is the governing default. Concept 2 frames the accent as the system's functional colour property, admitted wherever it qualifies as a signal. Concept 4 frames the system as achromatic; the accent is a named departure admitted only where value alone would fail. The accent footprint in Concept 4 is smaller — the test is stricter — which makes each appearance of the accent more meaningful.

**Concept 3 vs Concept 4:**
Concept 3 governs by documentation completeness. Concept 4 governs by the achromatic default plus a single admission test. Concept 3 can accommodate `colour-accent-subtle` and a fuller token system; Concept 4 cannot — any addition beyond the minimum necessary exception contradicts the governing principle. Concept 3 is more complete. Concept 4 is more restrictive by principle.

---

### Hypothesis Coverage

**Which concept most directly expresses the organising principle through colour behaviour?**
Concept 4. The achromatic default directly expresses "the less it asserts, the more it proves." The named single exception directly expresses "every element earns its presence." Both simultaneously, without compromise.

**Which concept takes the greatest structural risk?**
Concept 1. Maximum restraint with no hue admission. Highest execution risk at product UI scale. No safety net.

**Which concept is most conservative relative to the hypothesis?**
Concept 2. Structurally sound and well-grounded. Concept 4 is more precise; Concept 2 is more forgiving under production conditions.

---

## Ranking & Recommendation

### Rank Order

| Rank | Concept | Primary Reason |
|---|---|---|
| 1 | Concept 4 — The Achromatic Foundation | Most precisely calibrated. Holds achromatic as governing principle while admitting the minimum necessary exception. Higher drift resistance than Concept 2. Strong pass on all gates, two at strong pass. |
| 2 | Concept 2 — The Signal | Strong pass on all gates. Operationally sound. Signal-positive framing is slightly less precise than Concept 4's achromatic-default framing but more forgiving under production pressure. |
| 3 | Concept 3 — The Named System | Most complete. Most directly demonstrates "showing the work." Requires governance discipline that may exceed current team capacity. Right direction if token governance infrastructure is in place. |
| 4 | Concept 1 — The Achromatic | Highest hypothesis purity. Most brittle at product UI scale. Correct only if all other systems are being executed at near-perfect quality and value-only interactive states are confirmed viable. |

### Recommendation

**Concept 4 — The Achromatic Foundation** is structurally strongest.

It holds the achromatic principle at the governing level while naming the one exception operational reality requires. The accent earns its admission not by being a functional colour property of the system but by being the minimum necessary departure from a system that is otherwise without colour. Drift resistance is higher than Concept 2 because overriding an explicit achromatic default requires a stricter justification than applying a signal rule.

The condition under which Concept 2 is preferable: if the achromatic-default framing creates governance friction under production conditions — if teams find it more natural to ask "is this a signal?" than "is this achromatic and would value alone fail?" — Concept 2 achieves similar output with a simpler governance rule.

The condition under which Concept 3 is preferable: if the team treats the public token file as a first-class expression of the brand's standard posture and has governance capacity to maintain derivation documentation for every token.

Do not begin from Concept 1 without confirming through prototype that value-only interactive states are viable across the product UI contexts Krutho will actually ship.

---

## Human Handoff

When reviewing this document, consider:

1. Concept 4 emerged from the review of Concepts 1–3 as a more precisely calibrated position. Does the achromatic-default framing feel like the right governing principle — or does Concept 2's simpler signal-positive governance feel more operationally sustainable for this team?

2. The accent hue selection is the single highest-stakes decision in both Concepts 2 and 4. Are the exploration briefs specific enough to begin that decision from?

3. Does any concept risk drifting into category territory that Krutho must exclude?

4. Is there a colour logic not represented across these four concepts that you want to explore?

Select the concept you want to explore, or introduce a new direction with a grounding statement. Once a direction is selected, run `settle colour` after the exploration phase to record the outcome.
