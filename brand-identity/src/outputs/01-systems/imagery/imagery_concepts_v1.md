# Imagery System — Concepts v1

**Entity:** Krutho
**Module:** Imagery
**Version:** 1
**Sources:** `02_foundational_brief.md`, `04_active_hypothesis.md`, `logo_settled.md`, `typography_settled.md`
**Date:** 2026-03-02

---

## Settled Module Constraints Applied

**From Logo Settled:**
- There is no symbol to reference or echo. Imagery must be selected on its own structural terms.
- The technical precision of the `r` and `o` letterforms signals that constructed, precise imagery is in register — atmospheric, illustrative, or emotional imagery is not. `[Logo Settled — Imagery]`

**From Typography Settled:**
- No direct constraint from typography. Imagery must be selected on its own structural terms. `[Typography Settled — Imagery]`

The logo settled constraint is substantive: constructed and precise is in register; atmospheric, illustrative, and emotional is not. This is binding on all three concepts.

---

## Concept 1 — The Absent Image

### Grounding Statement

If the standard does not assert, and imagery asserts, then imagery has no structural role in this system. The visual register of specifications is text. The system is complete without images. `[Hypothesis — Organising Principle]` `[Brief — Section 7]`

If this cannot be written clearly, the concept is not grounded. It can be written clearly.

---

### Structural Imagery Logic

- **Principle:** Imagery is absent by policy, not by constraint. This is not "minimal imagery" — it is a principled decision that imagery has no structural function in this system. The system refuses imagery the same way the type system refuses bold running prose: not because images are inherently wrong, but because they make claims before the argument has been made. In this system, only the argument may make claims.
- **How it expresses the organising principle:** A specification document — RFC, X.509 profile, NIST publication — has no photographs, no illustrations, no imagery. The visual register of standards is text. To introduce imagery is to operate in a different register from the one the identity inhabits. The most direct expression of "the brand is the format, not the company" is a system with no brand imagery — only the format's content. `[Hypothesis — Organising Principle]`
- **Category positioning:** Enterprise IAM vendors use imagery pervasively — office photography, people in control, security metaphors. AI companies use generated and abstract imagery as aesthetic identity. A system with no imagery refuses both registers simultaneously and definitively. It cannot be mistaken for either category. `[Brief — Section 9]`

---

### Subject & Content Logic

- **What is shown:** Nothing. The system contains no photographs, no illustrations, no figurative or abstract images.
- **What is never shown:** People, environments, devices, abstract patterns, AI visualizations, security metaphors, cryptographic representations, data flows — all absent.
- **Human presence:** Absent. The human accountability argument is made through language and structure, not through depicting a human subject.
- **Product / service depiction:** Absent. The product manifests as code, documentation, and terminal output — these appear as text, not as product photography.
- **Abstract vs concrete:** The question does not apply. The visual system is typographic throughout.

---

### Formal Behaviour

- **Composition:** Entirely typographic and spatial. The absence of imagery is a compositional decision — space that would normally carry an image remains open, which amplifies typographic content and demands that the spatial system carry full structural weight.
- **Scale and cropping:** Not applicable.
- **Relationship with other system elements:** Imagery has no relationship with type, colour, or layout because it does not exist. The layout system must be designed with the assumption that no image will ever occupy any space.
- **Grid interaction:** The grid is designed for text and space only. No image zones are reserved.

---

### Treatment Logic

- Not applicable. No imagery exists to treat.
- **The only caveat:** Technical diagrams that function as text — certificate field tables, code blocks, command-line outputs — are part of the typography and layout system, not the imagery system. They are not excluded by this concept.

---

### Cross-Context Behaviour

**Product UI**
The least stressed context. Product UI is inherently text-driven — dashboards, certificate views, API documentation. The absence of figurative imagery is the norm in this environment, not a constraint. `[Brief — Section 9]`

**Marketing / web**
The most stressed context. A page without imagery places the entire communicative burden on typography, spatial composition, and the wordmark. At display scale, this demands exceptional layout execution. If the spatial and typographic systems cannot hold the attention of a visitor on a bare page, this concept cannot be deployed at marketing scale.

**Documentation**
The most natural context. Technical documentation is text-driven. The absence of imagery is expected and appropriate. The concept is at home here.

**Social / editorial**
Very stressed. Social surfaces — particularly X/Twitter, LinkedIn — have strong expectations for visual content. A text-only social presence reads as either precisely controlled or under-resourced. At this brand stage, maintaining that distinction under production pressure is extremely difficult.

---

### What This Makes Impossible

- Photography of any kind, in any context
- Illustration of any kind, in any context
- Abstract visual compositions, generative imagery, or pattern imagery
- Visual metaphors for security, cryptography, or AI
- Any surface that relies on imagery to establish brand presence or visual interest
- Photography used to humanize or warm the brand

---

### Category & Mis-Signal Risk

- **Primary risk:** At marketing and social scale, no imagery reads as either high-confidence minimalism or as an incomplete brand. The distinction is determined by the quality of the typographic and spatial execution — which must be near-perfect. At ordinary execution quality, this concept reads as unbuilt. `[Hypothesis — Structural Risks]`
- **Secondary risk:** The social layer is permanently stressed. Krutho's developer audience operates primarily on platforms that reward visual content. A text-only social presence reduces discoverability and engagement — this is an operational constraint, not a design failure, but it must be named.
- **Mitigation:** The concept only holds if every other system — typography, spatial, layout — is at its best. There is no imagery budget to compensate for weakness elsewhere. This concept sets the execution bar at the level required for the other systems to exist without visual support.

---

### Identity Gate Pressure Test

1. **Does it read as infrastructure rather than a product?**
**Strong pass.** A system without figurative imagery reads as exactly the register of specifications and standards. `[Brief — Section 10]`

2. **Does it signal technical credibility to a developer on first contact?**
**Pass.** Absence of promotional imagery is legible as technical discipline. Text-only systems are developer-native.

3. **Does it avoid implying that Krutho must be present at verification?**
**Pass.** No imagery carries such an implication.

4. **Would a technically skeptical developer trust it?**
**Pass.** No imagery means no visual claim the developer cannot verify. Trust by absence of assertion.

5. **Could this be the identity of a cryptographic standard, not a startup?**
**Strong pass.** Standards have no brand imagery. This concept is the visual register of a standard.

6. **Does it demonstrate intellectual honesty?**
**Pass.** No imagery means no claim the system cannot support through text and argument.

7. **Does it exclude the wrong categories clearly enough?**
**Strong pass.** Nothing to mis-signal. The category is excluded by the absence of the aesthetic tools those categories rely on.

**Overall: Strong pass on all gates.** Highest operational risk at marketing and social scale. Requires every other system to perform without visual support. The concept that proves the most, at the highest execution cost.

---

### Exploration Brief

**Begin from:** Design a full marketing page with no images. Can the typographic and spatial system carry the page at display scale? Test the above-the-fold treatment first — what does the page open to if no image is present?

**Primary tension to test:** Precision vs. poverty. Does the text-only system read as deliberately controlled, or as incomplete? The test is conducted with a specific viewer in mind: a developer who is evaluating a new infrastructure tool. Does the absence of imagery increase or decrease confidence?

**What to avoid immediately:** Adding any image "just for this context." The first exception is the end of the concept. If an image is needed, the concept should be abandoned in favour of Concept 2 rather than compromised.

---

## Concept 2 — The Mechanism

### Grounding Statement

The brand demonstrates through specificity. The mechanism — certificate structure, verification chain, trust hierarchy — is the structural subject of imagery. Images show how the standard works. `[Hypothesis — Authority Expression]` `[Brief — Section 6]` `[Logo Settled — Imagery]`

If this cannot be written clearly, the concept is not grounded. It can be written clearly.

---

### Structural Imagery Logic

- **Principle:** Imagery has a specific function: documenting and demonstrating the mechanism. It does not decorate, establish atmosphere, or represent brand world. It shows the structure of the standard, in the same register that the standard's own documentation uses — precise, technical, constructed.
- **How it expresses the organising principle:** "Authority demonstrated through specificity, not asserted through claims." A diagram of a certificate's field structure is authority through specificity — it names the mechanism, shows its parts, demonstrates how verification works. This is imagery as evidence, not imagery as communication. The image shows the work. `[Hypothesis — Authority Expression]`
- **The settled module constraint is satisfied directly:** "constructed, precise imagery is in register." A certificate anatomy diagram is the most constructed, most precise image in the system. It is built from the same logic as the wordmark — derived from rules, not drawn by instinct. `[Logo Settled — Imagery]`
- **Category positioning:** Enterprise security vendors use diagrams as marketing infographics — stylised, rounded, icon-heavy, colour-coded. This system uses diagrams as specification documents — precise, minimal, labeled, structurally faithful to what they represent. The difference in register is the category signal. `[Brief — Section 9]`

---

### Subject & Content Logic

- **What is shown:** The structure and operation of the standard. Certificate anatomy — the fields, their relationships, what each proves. Chain-of-trust hierarchy — human principal → biometric authorization → credential issued → agent operates → verifier checks. Verification flow — how a verifier with only the root CA public key can confirm the credential offline. Data structure representations — CBOR encoding, capability claims.
- **What is never shown:** Photographs of any kind. Illustrations that are not technical diagrams. Decorative abstract imagery. AI visualisations. Security metaphors (shields, locks, networks). People in context.
- **Human presence:** Present as a structural node in diagrams — labeled and positioned, not depicted. "Human Principal" is a named element in the trust chain, represented as a precise geometric node. The accountability is named and positioned, not photographed.
- **Product / service depiction:** The product IS the mechanism. Depicting the mechanism is depicting the product — but at the level of the standard, not the platform.
- **Abstract vs concrete:** Concrete in structure (the mechanism is precisely depicted), abstract in representation (no physical world, no environment, no person).

---

### Formal Behaviour

- **Framing and composition:** Diagrams are composed with the same precision logic as the wordmark. Consistent stroke weights — monolinear, matching the wordmark's construction. Consistent node geometry. Consistent label placement and spacing. The diagram grammar is derived from the typographic system. `[Logo Settled — Construction logic]`
- **Scale and cropping:** Diagrams appear at documentation and explanation scale — where the mechanism needs to be understood. At marketing scale, a diagram functions as evidence: a precisely cropped section of a certificate field structure, or a single line of the verification chain. Diagrams are not used as decorative heroes.
- **Relationship with type:** The diagram is an extension of the typography system. The same typeface labels nodes. The same spacing logic governs layout. A diagram could be reproduced in a markdown table and lose no essential content — the visual form is the presentation layer of structural information, not a separate visual language.
- **Grid interaction:** Diagrams respect the spatial system. They are not free-floating compositions; they occupy named zones within the layout.

---

### Treatment Logic

- **Production approach:** Constructed, not photographed. Diagrams are drawn to specification — not designed with aesthetic intent. Each element of a diagram has a structural reason to exist; nothing appears for visual effect.
- **Colour treatment:** Inherits the colour system. The achromatic foundation holds throughout. If the colour system admits an accent (as in Concepts 2 or 4 of the colour module), the accent appears at highlighted or active elements within a diagram — the same rule as in UI. No additional colour is introduced for diagram differentiation. Diagrams are monochrome by default.
- **What breaks this:** Rounded "infographic" styling. Gradient fills. Icon-based nodes (shields, locks, silhouettes). Colour-coded categories. Any diagram that reads as a marketing explainer rather than a specification document. If the diagram looks like a slide from a vendor pitch deck, it has failed.

---

### Cross-Context Behaviour

**Product UI**
The most natural context. Certificate display, credential structure, capability claims — the product surfaces that show the mechanism's output are already specification-format by necessity. Diagrams of certificate field structure appear in documentation, help content, and onboarding. `[Brief — Section 9]`

**Marketing / web**
Diagrams function as evidence for claims. A marketing page that states "verifiable by anyone offline" can show the verification chain diagram — one diagram, precisely placed, to substantiate the claim. The diagram is not the hero of the page; it is the proof point. No diagram should appear on a marketing surface without a structural justification for its presence.

**Documentation**
Primary context. Technical documentation uses technical diagrams. This concept is at home here — the system is designed for the documentation register. The imagery system and the documentation system are the same system.

**Social / editorial**
A single precisely cropped diagram — a certificate field hierarchy, a trust chain node pair — can function at social scale. It reads as technical content rather than brand content, which is the correct register. The social presence is evidence of technical depth, not marketing.

**Print / physical**
Diagrams translate cleanly to print. No colour dependency. The monochrome construction works at any scale.

---

### What This Makes Impossible

- Photography of any kind
- Illustration that is not a precise technical diagram
- Decorative or abstract visual compositions
- Stylised infographic treatment of any diagram
- Icon-based node systems (shields, locks, person-silhouettes)
- Colour-coded diagram systems
- Diagrams used as decorative backgrounds or surface texture
- Any image that cannot be labeled with structural precision

---

### Category & Mis-Signal Risk

- **Primary risk:** Technical diagrams done poorly read as enterprise security vendor explainer content — the exact category Krutho rejects. A diagram with rounded corners, icons, and pastel colour-coding is an IAM vendor marketing diagram. The distinction — specification-grade vs. marketing-grade — is entirely in the execution discipline. `[Brief — Section 9]`
- **Secondary risk:** "Showing the mechanism" can drift into making the product look more complex than it is. A diagram that shows all the complexity of the standard at once reads as a 6-month integration project. Every diagram must be selected for what it proves at that scale, not for comprehensiveness.
- **Mitigation:** The diagram grammar must be explicitly defined: monolinear strokes, geometric nodes, typographic labels in the system typeface, no decorative additions. A diagram that introduces any element outside this grammar has drifted.
- **Drift:** Under production pressure, stock "tech infographic" diagrams will appear. The system must make this visually unambiguous as a failure — if a diagram doesn't share the typographic grammar of the system, it is not a system diagram.

---

### Identity Gate Pressure Test

1. **Does it read as infrastructure rather than a product?**
**Strong pass.** Diagrams documenting a standard's structure read as infrastructure. They do not represent a company; they document a specification. `[Brief — Section 10]`

2. **Does it signal technical credibility to a developer on first contact?**
**Strong pass.** A developer encountering a precise certificate anatomy diagram recognises it as technically grounded. It makes a specific claim that can be verified — which is the correct relationship to the developer audience. `[Brief — Section 10]`

3. **Does it avoid implying that Krutho must be present at verification?**
**Pass.** Diagrams showing the verification flow can explicitly demonstrate offline, dependency-free verification. The imagery can reinforce this differentiator rather than contradict it. `[Brief — Section 1.2 Observation 2]`

4. **Would a technically skeptical developer trust it?**
**Strong pass.** Precise technical diagrams are developer-native content. A developer reads diagrams the way they read code — looking for correctness and specificity. If the diagram is correct, it earns trust. `[Brief — Section 10]`

5. **Could this be the identity of a cryptographic standard, not a startup?**
**Strong pass.** Standards are documented with technical diagrams. RFCs include precise protocol flow diagrams. NIST publications include data structure specifications. This concept is native to that register. `[Brief — Section 10]`

6. **Does it demonstrate intellectual honesty?**
**Strong pass.** A diagram of the mechanism shows the work with maximum specificity. It is the most direct form of intellectual honesty available in an imagery system — here is how it works, verifiable by anyone with the knowledge to read it. `[Brief — Section 6]`

7. **Does it exclude the wrong categories clearly enough?**
**Pass.** Precise specification-grade diagrams exclude both IAM vendor explainer aesthetics and AI company abstract imagery. The specification register is sufficiently distinct. `[Brief — Section 9]`

**Overall: Strong pass on all gates, multiple at strong pass.** Highest hypothesis alignment. Gives imagery a structural function that scales across all contexts. Most defensible under production pressure because the grammar is explicit.

---

### Exploration Brief

**Begin from:** Define the diagram grammar before producing any diagram. Establish: stroke weight (monolinear, consistent with the wordmark's construction logic), node geometry (geometric, named, no icons), label placement (typographic, using the system typeface), colour (achromatic by default). Then produce one diagram: the chain-of-trust hierarchy, from human principal to credential to verifier. This is the most fundamental diagram in the system and the test case for the grammar.

**Primary tension to test:** Specification-grade vs. marketing-grade. Produce the same verification flow diagram in two versions: one following the specification grammar, one with rounded nodes, colour-coding, and simplified labels. The difference names the line that must not be crossed. Commission or produce these as the first deliverable.

**What to test across contexts:** A single diagram appearing at three scales — as a full-page documentation diagram, as a marketing proof point (cropped to one chain segment), and at social scale (one node pair). Does the same grammar hold at all three scales?

**Avoid immediately:** Adding icons to nodes for "clarity." The label IS the node's identity. A node labeled "Human Principal" does not need a person icon — the icon is the drift signal.

---

## Concept 3 — The Authorization Moment

### Grounding Statement

Human accountability is the root of the trust chain. The authorization moment — the point at which a deliberate decision becomes a credential — is the structural subject of imagery. What that moment looks like is the exploration question, not a fixed answer. `[Brief — Section 1.2 Observation 1]` `[Hypothesis — Structural Thesis]`

If this cannot be written clearly, the concept is not grounded. It can be written clearly.

---

### Structural Imagery Logic

- **Principle:** The hypothesis states "the human is the source of authority, not the system." If imagery has a subject in this system, it is the moment that authority is exercised — the point of deliberate decision that becomes fixed in the credential. That moment may be represented through a person, through the artifact the decision produces, through an interaction state, or through something else. The concept commits to the moment as the structural subject — not to the form that moment takes.
- **How it expresses the organising principle:** The structural thesis states that every agent action is traceable to a specific human's deliberate act. Imagery shows that act — or its immediate trace — with precision and without sentiment. Not the system, not the infrastructure. The moment where accountability is fixed. `[Hypothesis — Structural Thesis]`
- **Critical distinction:** This is not "person using technology" imagery and it is not security metaphor imagery. It is imagery of a specific structural event — the authorization moment — in whatever form best represents that event with precision. The subject is the decision and its trace, not the technology or the abstract concept. `[Brief — Section 9 — Aesthetic tropes to reject]`
- **Category positioning:** Enterprise security vendors use imagery to perform authority — environments, roles, control. This concept uses imagery to locate a structural event — a specific moment where authority is exercised. The register differs: performed authority (vendor) vs. a precise, located moment (Krutho). `[Brief — Section 9]`

---

### Subject & Content Logic

- **What is shown:** The authorization moment — the point at which a deliberate decision becomes a credential. The form is not fixed: this may be a person at the moment of authorization; it may be the artifact produced; it may be an interaction state or a trace of the decision. Each is a valid structural subject. The exploration determines which form is most precise and least susceptible to mis-signal in context.
- **What is never shown:** Biometric imagery (faces at recognition scale, fingerprints, iris recognition). Group photography. Enterprise environments. "Technology in use" as the primary subject (devices, screens, hands on keyboards). Security metaphors (shields, locks, networks). Any imagery that depicts the system or infrastructure rather than the moment.
- **Human presence:** Possible, not required. Where a person appears, they are the accountable party — the authorization root — not a brand representative or product user. Where a person does not appear, the image must still locate the moment of accountable decision with equivalent precision.
- **Product / service depiction:** Never the subject. The mechanism is invisible; the authorization moment is its only visible trace.
- **Abstract vs concrete:** The exploration question. The image must be precise — but precision can be achieved through a concrete subject or through a precisely constructed representation. What it cannot be is vague, atmospheric, or emotionally coded.

---

### Formal Behaviour

- **Framing:** Precise and close. Whatever the subject, it is isolated from context. The frame shows only what the argument requires.
- **Scale and cropping:** Imagery appears at moments where the claim "human accountability is the root" needs grounding. It does not appear at every surface. Each use must be structurally justified.
- **Relationship with type:** Imagery functions as evidence. Adjacent text names what it is evidence of. The image does not speak alone.
- **Colour treatment:** Monochrome or heavily desaturated throughout. The image does not introduce colour the colour system has not admitted. Atmospheric tones, warm grading, and emotional colour treatment are excluded.

---

### Treatment Logic

- **Post-production approach:** Precise reduction. Whatever the subject, it is treated to remove aesthetic character — no atmospheric lighting, no editorial warmth, no mood. The image is stripped to what it shows structurally.
- **Colour:** Monochrome or desaturated to near-monochrome. Consistent with the achromatic foundation of the colour system.
- **What breaks this:** Atmospheric treatment of any kind. Warm tones. Environmental context used for mood. Any image that could appear in enterprise security vendor materials or startup culture photography. The test: does this image show a structural event with precision, or does it perform an emotional register?

---

### Cross-Context Behaviour

**Product UI**
Imagery of this type does not appear in the product UI. The product surface is text-driven, data-driven, mechanism-driven. `[Brief — Section 9]`

**Marketing / web**
Imagery grounds the "human accountability" claim at the brand level. It appears where that claim is being named — once, with structural justification. Not decoration.

**Documentation**
Does not appear in technical documentation. The documentation register is text and diagrams only. `[Brief — Section 9]`

**Social / editorial**
A precisely treated image of the authorization moment — in whatever form — can function at social scale as a content signal: this brand has a specific claim about accountability, and the image makes that visible.

**Print / physical**
Monochrome/desaturated treatment works at any scale and prints cleanly.

---

### What This Makes Impossible

- Biometric imagery (faces at recognition scale, fingerprints, iris recognition)
- Group photography
- Environmental photography (offices, data centres, enterprise contexts)
- "Technology in use" as the primary subject (devices, screens, hands on keyboards)
- Security metaphors (shields, locks, networks, data flows)
- Warm, atmospheric, or emotionally coded imagery
- Imagery used as decoration or background texture
- Any image that depicts the system or infrastructure rather than the authorization moment
- Any image that could appear in enterprise security vendor or startup brand materials without modification

---

### Category & Mis-Signal Risk

- **Primary risk:** The authorization moment as a subject is open enough to drift toward enterprise security aesthetics (control, surveillance, verification as threat) if framing is imprecise. The structural constraint — the moment of deliberate authorization, not the system that enables it — must be maintained. `[Brief — Section 9]`
- **Secondary risk:** If the subject is a person, the photography risks premium consumer brand associations. If the subject is an artifact, it risks product photography. Both drifts are addressable through exploration — the risk is naming which form has the least drift exposure.
- **Structural risk:** The form of the subject is the exploration question, which means the concept is not fully governable until that question is answered. Exploration must produce a definition specific enough to reject non-conforming imagery visibly.
- **Mitigation:** Every image must be able to answer: "what moment of authorization does this show, and what decision does it trace?" If the image cannot answer that question, it does not belong in the system.

---

### Identity Gate Pressure Test

1. **Does it read as infrastructure rather than a product?**
**Conditional.** Imagery of an authorization moment can read as infrastructure if the moment is shown with precision and without product context. Risk depends on the form the subject takes and the treatment. `[Brief — Section 10]`

2. **Does it signal technical credibility to a developer on first contact?**
**Conditional.** Depends on form. An artifact-based or interaction-based subject may carry more technical register than a portrait. The exploration determines this. `[Brief — Section 10]`

3. **Does it avoid implying that Krutho must be present at verification?**
**Pass.** The authorization moment precedes the credential. It does not require Krutho's ongoing presence. `[Brief — Section 1.2 Observation 2]`

4. **Would a technically skeptical developer trust it?**
**Conditional.** Depends on form and treatment. Precise imagery of an artifact or interaction may hold more trust than portrait photography. The test is whether the image reads as documentary evidence or as brand communication.

5. **Could this be the identity of a cryptographic standard, not a startup?**
**Conditional.** Standards do not typically use this kind of imagery. The structural justification is strong — but execution must be precise enough that the image reads as evidence, not branding.

6. **Does it demonstrate intellectual honesty?**
**Pass.** The subject is grounded in the brief's own structural observation: the human is the source of authority. Imagery of the moment where that authority is exercised is evidence for a claim the mechanism makes. `[Brief — Section 6]`

7. **Does it exclude the wrong categories clearly enough?**
**Conditional.** Requires form and treatment to be defined precisely enough that non-conforming imagery is visibly wrong. Until the exploration produces a grammar for this subject, the concept is not fully governable.

**Overall: Multiple conditional passes** — for a structural reason rather than an inherent one. The conditionality is in the open form question. Exploration resolves it.

---

### Exploration Brief

**The primary question:** What does the authorization moment look like? This is the exploration's first task — not what treatment to apply, but what the subject is. Produce at least two visual representations of the authorization moment using different subjects: a person at the moment of authorization; the artifact produced by that act; an interaction state or trace of the decision. Evaluate each against the identity gate before proceeding.

**Primary tension to test:** Evidence vs. symbol. The image must read as precise documentation of a structural event — not as a symbol for accountability, not as a metaphor for trust. The line between evidence and symbol is the most important distinction this concept must navigate.

**What to test across contexts:** Does the chosen form hold at marketing scale, documentation scale, and social scale? A form that only works in one context is not the right form for this system.

**Avoid immediately:** Settling on the human subject by default — it is the most available form, not necessarily the most structurally correct one. The exploration should produce the form that passes the identity gate most cleanly and is most governable under production conditions.

---

## Structural Comparison

### Divergence Verification

**Concept 1 vs Concept 2:**
Concept 1 refuses imagery entirely — the system has no images. Concept 2 admits imagery for one specific function: documenting the mechanism. A designer from Concept 1 has no image budget. A designer from Concept 2 has a diagram grammar. The question that separates them is not "what should this look like?" but "does imagery have a structural function in this system?" Concept 1 answers no; Concept 2 answers yes — one function only.

**Concept 1 vs Concept 3:**
Both reach different conclusions from the same restraint principle. Concept 1 concludes that no imagery is needed. Concept 3 concludes that one photographic subject is structurally justified. The divergence is in whether the human accountability argument can be served by text alone (Concept 1) or requires a photographic grounding (Concept 3). A designer from Concept 1 communicates "human accountability" through language. A designer from Concept 3 communicates it through a precise photograph of a human making an accountable decision.

**Concept 2 vs Concept 3:**
Both admit imagery but for different structural subjects. Concept 2's subject is the mechanism — the invisible structure of the standard made visible through constructed diagrams. Concept 3's subject is the authorization moment — the point where a deliberate decision becomes a credential, in whatever form best represents that event. A designer from Concept 2 asks: "what does the mechanism look like at the structural level?" A designer from Concept 3 asks: "what does the authorization moment look like — and in what form?" These produce different image types, scales, and contexts. Concept 2 images are always constructed; Concept 3 images may be photographed, constructed, or something else — the form is the open exploration question. Concept 2 images are native to documentation and technical contexts; Concept 3 images appear at brand and marketing moments.

---

### Hypothesis Coverage

**Which concept most directly expresses the organising principle through imagery behaviour?**
Concept 2. "Authority demonstrated through specificity" — a diagram of a certificate's field structure is the most direct expression of that principle in imagery. It shows the work, names the mechanism, and stops when the explanation is complete. `[Hypothesis — Authority Expression]`

**Which concept takes the greatest structural risk?**
Concept 1. No imagery places the maximum burden on every other system. It requires the typographic and spatial systems to be exceptional. It is permanently stressed at marketing and social scale. The concept with the highest right-answer potential and the most brittle execution requirements.

**Which concept is most conservative relative to the hypothesis?**
Concept 3 as currently framed — the authorization moment without a fixed subject. It is the most open concept, which makes it the hardest to govern before the exploration resolves the form question. Conservative in that it defers the defining decision to exploration; riskiest in that it cannot be fully evaluated until that question is answered.

---

## Ranking & Recommendation

### Rank Order

| Rank | Concept | Primary Reason |
|---|---|---|
| 1 | Concept 2 — The Mechanism | Most directly expresses the organising principle. Strong pass on all gates, multiple at strong pass. Gives imagery a specific, auditable function. The diagram grammar is explicit enough to enforce under production pressure. Satisfies the logo settled constraint directly. |
| 2 | Concept 1 — The Absent Image | Purest hypothesis expression. Highest operational risk at marketing and social scale. Right choice if every other system can hold without visual support. |
| 3 | Concept 3 — The Authorization Moment | Structurally grounded but multiple conditional passes on identity gates. The form of the subject is unresolved — which means it cannot be fully evaluated or governed until exploration answers that question. |

### Recommendation

**Concept 2 — The Mechanism** is structurally strongest.

It gives imagery a specific structural function — demonstrating the mechanism — that cannot be misused without violating the grammar. The diagram system is explicit: monolinear strokes, geometric nodes, typographic labels. A diagram that violates this grammar is visibly wrong. This produces a more governable imagery system than either alternative. The concept also satisfies the logo settled constraint directly: "constructed, precise imagery is in register." A diagram built from the same construction logic as the wordmark is the most direct extension of that settled property.

The condition under which Concept 1 is preferable: if the spatial and typographic systems are strong enough to hold the marketing and social surfaces without visual support, Concept 1 is the more structurally honest position — it makes no admission that imagery is necessary. The test is the marketing page: can it hold attention at display scale with no image? If yes, Concept 1 is defensible.

The condition under which Concept 3 is preferable: if exploration resolves the form question with a subject that passes the identity gate cleanly and produces a more governable grammar than expected. The exploration brief is the test — if it produces a form that reads as documentary evidence rather than brand communication, the ranking should be revisited.

---

## Human Handoff

When reviewing this document, consider:

1. Does Concept 2's diagram grammar feel workable as a production system — is there a team or resource that can produce specification-grade diagrams at the required precision, and sustain that quality over time?

2. Does the absence of figurative photography in both Concepts 1 and 2 feel right for how Krutho needs to represent itself — particularly at social and community-building contexts where the developer audience is the target?

3. Is there an imagery logic not represented here that you want to explore? For example: a concept that uses constructed imagery derived from the technical materials themselves (actual certificate field data, rendered precisely) rather than diagrammatic interpretation.

4. Are the exploration briefs specific enough to begin commissioning or production work?

5. Does any concept risk drifting into stock photography territory or into the imagery conventions of the categories Krutho explicitly rejects?

Select the concept you want to explore, or introduce a new direction with a grounding statement. Once a direction is selected, run `settle imagery` after the exploration phase to record the outcome.
