# Phase 2 — Foundational Brief

**Entity:** Krutho
**Brief date:** 2026-02-26
**Lens status:** Active — Open If
**Source:** `01_repo_extraction.md`

---

# Stage 1 — Structural Interrogation

---

## 1.1 — What This Is (Structurally)

Krutho is a cryptographic identity primitive — a mechanism for embedding human authorization into an AI agent's operating credential, such that the authorization travels with the agent and can be verified by anyone using only public key cryptography. It does not manage access, control resources, or govern agent behaviour at runtime. It produces and issues a credential that proves a specific human, at a specific moment, authorised a specific agent to act within specific limits.

Its structural position is infrastructure, not product. It is a layer other systems build on top of — not a platform that other systems connect to.

*[Extraction Sections 2, 4, 6]*

---

## 1.2 — Structural Observations

**Observation:** The human is the source of authority, not the system. Every certificate traces to a specific human's biometric act of consent — Face ID, Touch ID, or passkey. Authorization cannot be delegated programmatically; it must be triggered by a human.
**Consequence:** The identity must centre human accountability, not system control. Krutho enables a chain of trust; it does not hold that trust. The authority resides in the human who approved, not in Krutho.
**Source:** Extraction Section 2 — "Human biometric root of trust (Face ID / Touch ID / passkey) for certificate issuance"

---

**Observation:** The credential is self-contained — it does not require Krutho to be present at verification. Any verifier with the root CA public key can validate a certificate offline, peer-to-peer, with no network call and no vendor dependency.
**Consequence:** Krutho is not a gatekeeper. It is not in the verification loop. The identity must not imply central control or ongoing dependency. It must reflect that it enables verification, not that it mediates it.
**Source:** Extraction Section 2 — "Offline peer-to-peer verification (pure cryptography, no network call)"; Section 4 — "No network call. No vendor dependency. No policy engine lookup. Pure cryptography."

---

**Observation:** The business model is explicitly designed to make the credential format free and ubiquitous, including on competitor infrastructure. Revenue comes from the human-linked approval events and the platform layer, not from controlling the format.
**Consequence:** Krutho's identity must build trust in a protocol or standard, not in a proprietary product. Anything that signals vendor lock-in directly contradicts the business model and would undermine developer adoption — the precondition for everything else.
**Source:** Extraction Section 6 — D-68: "Make the cert format free and ubiquitous everywhere, including on competitor CAs"; Section 4 — "The format is free. The human link is the product."

---

**Observation:** Krutho explicitly names a category it claims to be creating — "Human-Rooted Agent Identity" — and positions itself against existing categories (IAM, PAM, NHI, OAuth) by answering a different question: not "can this thing access this resource?" but "who authorized this agent, what did they authorize it to do, and can I verify that without trusting anyone else?"
**Consequence:** The identity has a category-making burden at this stage. It must create recognition for the problem before it can capture it. This is not the same as competing in an existing market — it requires the identity to be educational in a way that established products are not.
**Source:** Extraction Section 4 — "The category we're creating is Human-Rooted Agent Identity"; Section 5 — NIST AI Agent Standards Initiative; Section 5 — "The window is 12–18 months"

---

**Observation:** The primary audience is developers, but the authority and revenue audiences are platform teams and CISOs. These groups have structurally different relationships with the product: developers need it to be as simple as an HTTP request; platform teams need governance and instant revocation; CISOs need cryptographic traceability for compliance.
**Consequence:** The identity must work across registers that are not identical. A single voice must be credible to a developer running npm install and to a CISO reviewing an audit trail. These are not reconcilable through tone alone — the brief must carry this as an unresolved structural constraint.
**Source:** Extraction Section 3 — audience tiers; Section 6 — GTM phases and revenue model

---

**Observation:** Krutho explicitly documents what it does not claim — "We didn't invent a new cryptographic primitive"; "We bridge to OAuth — we don't replace it." Intellectual honesty is stated as a named principle, not a tonal preference.
**Consequence:** The identity earns credibility through precision and restraint, not through assertion. Any overclaiming — visual, verbal, or structural — would directly contradict the intellectual honesty positioning and break trust with the technically skeptical developer audience.
**Source:** Extraction Section 4 — "What We Don't Claim"; Section 8 — "Intellectual honesty builds trust"

---

**Observation:** The moat is explicitly stated as the human trust chain, not the code. The SDK is open source and free. The value is the accumulated record of human-linked approvals, the audit trail, and the platform that makes those records useful at scale.
**Consequence:** Krutho's value is cumulative — it deepens over time as the chain of accountability grows. The identity should reflect that this is infrastructure that accrues meaning, not a tool that delivers a one-time result.
**Source:** Extraction Section 4 — "The moat isn't the code. The moat is the human trust chain."; Section 6 — D-68

---

## 1.3 — Tensions Identified

**Tension 1: Simplicity vs. cryptographic depth**
Krutho claims developer simplicity ("3 lines of code") while the underlying mechanism is genuinely complex — X.509v3, EC P-256, CBOR-encoded capabilities, biometric approval flow, multi-standard bridges.
Both are true simultaneously. The simplicity is real (developer surface). The depth is real (cryptographic mechanism).
Evidenced: developer simplicity [Section 4, Section 8]; technical depth [Section 2, Section 4]
Status: **Must remain open.** The identity cannot sacrifice either. Resolving this by hiding the depth would undermine technical credibility. Resolving it by foregrounding the depth would undermine developer adoption.

---

**Tension 2: Open standard vs. commercial product**
The format is deliberately free and open. The business model depends on format ubiquity — including on competitor infrastructure. But Krutho must also sell a paid platform on top of that free format.
The "Bluetooth" analogy from the repo provides a framing: give away the spec, build value in the ecosystem on top. But this tension cannot be fully resolved through analogy — the identity must navigate between not appearing as a locked-in vendor and not appearing as a not-for-profit.
Evidenced: open format [D-68, Section 4]; commercial platform [Section 6 — GTM phases, revenue model]
Status: **Partially resolvable.** The Bluetooth framing is available but must be handled carefully. Brief carries this forward.

---

**Tension 3: Developer-first voice vs. enterprise trust requirement**
The primary audience needs simplicity and no vendor lock-in. The revenue audience (platform teams, CISOs) needs accountability, governance, and compliance traceability. These registers are structurally different.
Evidenced: [Section 3 — audience tiers]; [Section 6 — revenue model]; [Section 8 — language samples]
Status: **Must remain open.** This is a positioning constraint, not a design problem. The brief carries it into hypotheses.

---

**Tension 4: Category leadership claimed from pre-seed**
Krutho claims to be creating a new category and to be the only product that does its three core things. It has no named customers, no published revenue, no confirmed deployments at time of extraction.
The claims are technically defensible. The credibility gap is real.
Evidenced: category claims [Section 4]; no named customers [Section 3]; pre-seed stage [Section 1]
Status: **Must remain open.** The identity cannot manufacture credibility that doesn't exist. Technical substance and intellectual honesty must carry the weight that customer evidence would normally provide.

---

## 1.4 — What the Extraction Cannot Answer

**Question 1:** What does Krutho look like in current use? The favicon.svg and custom.css exist but are not described. Are there visual decisions already in circulation?
**Brief assumes:** No prior visual identity to respect or build from. This is a new brand.
**Risk if assumption is wrong:** If visual decisions are already externally visible and associated with Krutho (GitHub, documentation site, npm), the brief may underestimate continuity constraints.
**Resolution:** Client should share the favicon and CSS for review before modules begin.

---

**Question 2:** Who is the primary decision-maker in the buying process — the developer, the platform team, or the CISO?
**Brief assumes:** Developer adopts first. Platform team governs. CISO approves. Developer is the primary identity audience.
**Risk if assumption is wrong:** If CISO is the actual primary buyer, the identity must speak enterprise trust first and developer simplicity second. This would substantially change the brief.
**Resolution:** Client, through sales or GTM validation.

---

**Question 3:** What is the intended relationship between Krutho and Vouch in public communications?
**Brief assumes:** Krutho operates independently as a brand. Vouch is parent, not co-brand. All expressions use Krutho only.
**Risk if assumption is wrong:** If Vouch branding is visible on developer tooling surfaces (GitHub owner is `anthonymaley`, npm package is `@krutho/core`), a mismatch between brand and infrastructure naming may create friction.
**Resolution:** Client has confirmed Krutho as the brand. Specific handling of Vouch parent visibility at developer touchpoints should be validated before modules.

---

**Question 4:** What is the target outcome — ecosystem standard or strategic acquisition?
**Brief assumes:** Krutho is building for ecosystem adoption. Identity reflects that posture.
**Risk if assumption is wrong:** If a specific strategic acquirer is in view, the identity may need to signal alignment with that acquirer's existing frameworks or systems.
**Resolution:** Client.

---

---

# Stage 2 — Foundational Brief

---

## 1. Strategic Summary

Krutho is a cryptographic identity primitive that binds AI agent actions to the specific human who authorized them — producing a portable, verifiable, offline-checkable credential that any system can trust without depending on Krutho's infrastructure. It is not a product in the conventional sense; it is a standard that other products and systems build on top of. The identity work must establish Krutho as that standard at the moment the category is forming — earning the trust of developers who adopt it first, while extending credibility to the platform teams and security leaders who govern deployment at scale.

*[Stage 1.1, 1.2 — Observations 1, 2, 3, 4]*

---

## 2. Structural Shift Required

**Current state (assumed — no deployment evidence in extraction):** AI agents authenticate using static API keys or OAuth tokens. Neither mechanism proves which human authorized the agent or what it is permitted to do. No standard exists for human-rooted agent identity. Krutho exists as an open-source SDK with no named customers and no established visual identity.

**Required state:** Krutho becomes the named primitive — the thing developers and platform teams reach for when they need to bind agent actions to human authorization. The format achieves sufficient ubiquity that verification without Krutho's infrastructure is a real-world behavior, not just a theoretical capability.

**What the shift depends on:** Developer adoption of the open-source SDK → format ubiquity → platform revenue. The identity work must reduce friction to adoption (credibility on first contact, simplicity of implementation signal) and raise the perceived legitimacy of the standard (intellectual authority, technical precision, institutional seriousness without enterprise-vendor appearance).

*[Stage 1.2 — Observations 3, 4; Stage 1.1]*

---

## 3. Active Tensions

**Tension 1: Simplicity vs. cryptographic depth**
The developer surface is genuinely simple. The cryptographic mechanism is genuinely complex. Both must be present.
*Why it exists:* Krutho is a cryptographic standard being sold to developers who want an HTTP-simple integration. [Extraction Sections 2, 4]
*What it means for design:* The identity cannot hide the depth (it is the source of technical authority) or foreground it (it would create friction for developer adoption). The surface must be clean; the depth must be legible for those who look.
*Should it be resolved before hypotheses or designed within?* Designed within. This is a permanent structural condition, not a problem to solve.

---

**Tension 2: Open standard vs. commercial product**
The format is deliberately free. The business depends on platform revenue on top of the free format.
*Why it exists:* The go-to-market strategy requires format ubiquity as a precondition for platform revenue. Making the format proprietary would undermine adoption. [D-68, Section 4, 6]
*What it means for design:* The identity must read as infrastructure-grade, not product-marketing. It must not signal lock-in. It must also signal that there is a company with a business model behind it — not a volunteer project.
*Should it be resolved before hypotheses or designed within?* Designed within. Each hypothesis will handle this differently.

---

**Tension 3: Developer-first voice vs. enterprise trust requirement**
Developer adoption and enterprise governance require different registers.
*Why it exists:* Developer adoption is the GTM precondition. Enterprise platform and CISO audiences are the revenue base. [Section 3, 6]
*What it means for design:* A single identity must be legible to both without being optimized for neither. This is a constraint on emotional register and language — not on visual form.
*Should it be resolved before hypotheses or designed within?* Designed within. Brief carries it.

---

**Tension 4: Credibility gap — category claims from pre-seed**
Krutho claims category leadership without customer evidence to support it.
*Why it exists:* The business is pre-revenue, category is pre-formed, window is 12–18 months. [Section 3, 5]
*What it means for design:* Technical substance must carry credibility. The identity must earn trust through precision, not claim it through assertion. Intellectual honesty is the available tool.
*Should it be resolved before hypotheses or designed within?* Designed within, and monitored — as Krutho moves from pre-seed to deployment, the identity should not need to change to accommodate real customer evidence. Brief that requires credibility gap to be resolved before it works is a brittle brief.

---

## 4. Central Position

**Category framing:** Krutho is not IAM, PAM, NHI management, or an auth protocol. Those categories answer: "Can this thing access this resource?" Krutho answers: "Who authorized this agent, what did they authorize it to do, and can I verify that without trusting anyone else?" The category is Human-Rooted Agent Identity.

**Axis of differentiation:** Human accountability is embedded in the credential itself — not managed in a policy engine, not delegated to a server, not assumed from a service account. Every agent action is traceable to a specific human's biometric act of consent, verifiable by any party, offline, with no dependency on Krutho's infrastructure.

**Central claim:** Krutho makes human accountability for AI agent actions cryptographic, portable, and verifiable by anyone — without requiring trust in Krutho.

**What it refuses to be:** A gatekeeper, a compliance dashboard, or a platform that must be present for agent identity to work. It issues credentials; it does not mediate them.

*[Stage 1.2 — Observations 1, 2, 3; Extraction Section 4]*

---

## 5. Audience

**Primary: Developers building agentic systems**
- Who: Engineers writing agent code who need identity to be as simple as an HTTP request — not a 6-month IAM integration project. [Section 3]
- Must believe: That Krutho is technically sound; that 3 lines of code is genuinely true; that they will not be locked into Krutho's infrastructure; that it will not become a dependency they cannot remove.
- Must feel: Confident they're using the right primitive. Not slowed down. Not marketed to.
- What breaks trust: Overclaiming. Vendor lock-in signals. Complexity hidden in implementation. Any appearance of security theater.

**Secondary: Platform teams deploying agents at scale**
- Who: Teams responsible for "what agents are running, who authorized them, what can they do?" [Section 3]
- Must believe: That Krutho gives them full accountability and instant revocation capability; that the audit trail is real and not dependent on Krutho's uptime.
- Must feel: That the system will hold up when something goes wrong; that they have actual control.
- What breaks trust: Ambiguity about what the audit trail covers; any implication that revocation is slow or limited.

**Tertiary: Compliance and security leaders (CISOs)**
- Who: Leaders who must answer "can we trace every agent action back to a human?" for SOC2, ISO 27001, NIST. [Section 3]
- Must believe: That Krutho's traceability is cryptographic and audit-ready; that adopting Krutho reduces exposure.
- Must feel: That the technical claims are backed by established standards, not invented.
- What breaks trust: Marketing claims without technical specificity; anything that resembles a compliance checkbox rather than a structural solution.

*[Extraction Section 3; Stage 1.2 — Observation 5]*

---

## 6. Authority

**Primary: Technical authority**
Krutho's claims are grounded in established cryptographic standards — X.509, ECDSA, WebAuthn, CBOR, RFC 8949. It explicitly states: "We didn't invent a new cryptographic primitive." Five standards bridges (OAuth, A2A, mTLS, SPIFFE, W3C VC/DID) demonstrate interoperability without novelty claims.
Evidence: [Section 2, Section 4, Section 8]
How it should feel: Precise and demonstrated, not asserted. Authority earned through specificity — naming the standard, not naming the claim.
What would undermine it: Vague security language; superlatives not backed by technical evidence; any appearance of the identity outrunning what the SDK can do.

**Secondary: Infrastructural authority**
Krutho is positioning as a primitive — a layer others build on. "The missing layer in the agentic AI stack." "The format is free." Infrastructure carries authority through adoption, not through marketing.
Evidence: [Section 4 — "identity primitive"; D-68; Section 8]
How it should feel: Foundational. Infrastructure doesn't promote itself — it demonstrates reliability over time.
What would undermine it: Anything that implies Krutho must be trusted, present, or consulted at verification time.

**Tertiary: Visionary authority**
NIST reference implementation, standards body participation, RFC for agent certificate profile. These are aspirations, not current status.
Evidence: [Section 5 — NIST AI Agent Standards Initiative; Section 6 — GTM Phase 3]
How it should feel: Stated as direction, not current position. Premature category-claiming without technical evidence undermines, not supports, credibility.
What would undermine it: Treating aspirations as current status; institutional claims without institutional participation.

*[Stage 1.2 — Observations 1, 2, 3, 6]*

---

## 7. Emotional Register

**Required register:** Precise. Direct. Assured without aggression. Technically grounded. Honest about limits.

**What must be avoided:**
- Startup urgency and hype — the 12–18 month window is a business condition, not an identity tone. If the identity reads as urgent, it will read as anxious, not confident.
- Enterprise-speak — compliance checklists, "enterprise-grade", "scalable solutions". This signals the category Krutho is explicitly not.
- AI company aesthetics and language — Krutho is an identity infrastructure company whose product operates in the AI context. It is not an AI company.
- Security theater — visual and verbal clichés of the security industry (fortress language, shield imagery, zero-trust buzzwords) signal the wrong category.

**Danger tone: Evangelical.** If the identity reads as trying to convert people to a belief system — about the future of AI, about the importance of trust, about Krutho's mission — it will alienate the technically skeptical developer audience who must verify claims, not accept them. Conviction without evidence is a liability at this stage.

*[Stage 1.2 — Observations 6, 7; Extraction Section 8 — tone descriptors]*

---

## 8. Constraints

**Hard constraints:**

Krutho is the brand name — not Vouch Krutho → All identity expressions use Krutho only. [Human decision; Extraction Section 7]

Identity must be technically legible to a developer on first contact → No abstraction that removes technical legibility. A developer who reads one paragraph should know what kind of thing this is. [Section 3; Stage 1.2 — Observation 5]

Must not signal vendor lock-in → Open standard positioning must be structurally present in the identity, not just stated in copy. [D-68; Section 4; Stage 1.2 — Observation 3]

No prior visual identity to build from → All visual work starts from scratch. No continuation brief. [Section 7; Stage 1.4 — Question 1]

**Soft constraints:**

Vouch is the parent — the identity should not obscure or deny this, but Vouch should not be foregrounded. [Extraction Section 7; human decision]

DevRel and community growth are a stated priority → Identity must carry enough warmth to support community adoption, not only enterprise authority. [Section 6]

The 12–18 month window is real → The identity must be fully deployable immediately. No identity that requires 12 months of brand-building before it works. [Section 5]

**Unknown constraints (must validate before modules begin):**

What visual decisions are already in use on the documentation site, GitHub, and npm? [Section 7]

How does Vouch's visual identity inform or constrain what Krutho can do visually? [Human decision; Extraction Section 7]

What does the developer tooling context require? (GitHub READMEs, npm package pages, CLI output — brand expression rules differ from marketing surfaces.) [Section 2]

---

## 9. Rejection Criteria

**Category mis-signals:**
- IAM or PAM vendor aesthetics — Okta, Auth0, CyberArk visual conventions → Krutho explicitly positions against these categories. [Section 4]
- Enterprise security vendor design language — blue palettes, shields, padlocks, fortress imagery → implies the wrong category and the wrong authority type.
- "AI company" aesthetics — gradient backgrounds, neural network imagery, glowing nodes, generative art → misidentifies what Krutho is. The AI is the context; identity is the product.
- NHI management dashboards → implies central control, which contradicts offline verification.

**Aesthetic tropes to reject:**
- Complexity as sophistication → The identity must not look like a 6-month integration project. Developer trust is built through apparent simplicity, not apparent depth.
- Biometric imagery as identity metaphor — fingerprints, face scans, iris recognition → too literal, too consumer, does not reflect the structural mechanism.
- Trust-as-warmth — soft colours, rounded forms, community-friendly aesthetic → signals the wrong authority type for a cryptographic standard.

**Behavioral anti-patterns:**
- Gated access to developer tooling → Everything about the GTM is open-source first. Identity must not imply friction where there is none.
- Sales-led surface → If the first impression requires a contact form, the identity contradicts the developer-first positioning.

**Narrative anti-patterns:**
- "The only platform that..." → Undermines intellectual honesty positioning. [Section 8]
- Compliance-first messaging → Signals enterprise-first, alienates developers.
- "Trust us" without demonstrable evidence → The developer audience does not grant trust; it verifies it.
- "AI is changing everything" framing → Category language, not Krutho's argument.

---

## 10. Identity Gate

### Gate Questions (Pass / Fail)

1. Does it read as infrastructure rather than a product? (Infrastructure enables; products deliver.)
2. Does it signal technical credibility to a developer on first contact — without requiring explanation?
3. Does it avoid implying that Krutho must be present at verification? (Offline verification is the structural differentiator — nothing in the identity should undermine it.)
4. Would a technically skeptical developer trust it — not prefer it, not like it, but trust it?
5. Could this be the identity of a cryptographic standard, not a startup?
6. Does it demonstrate intellectual honesty — does it show the reasoning or limits, rather than assert the conclusion?
7. Does it exclude the wrong categories clearly enough? (Krutho's position depends on clear exclusion: not IAM, not PAM, not NHI, not an AI company.)

### Required Invariants

These must hold across every expression — logo, type, colour, layout, imagery, language, UI behaviour:

1. The human-to-agent authorization chain is always the structural argument — not a feature, not a use case.
2. Technical precision governs expression — no vagueness in language, no ambiguity in form.
3. Open standard positioning must be present — nothing implies lock-in or ongoing Krutho dependency.
4. Krutho name only — no Vouch Krutho.
5. Developer-first in register — even when the audience is enterprise, the voice does not shift to enterprise-speak.

### Failure Modes

- Identity reads as a product, not infrastructure → structural misalignment with the open-standard business model and the offline verification differentiator.
- Identity resembles an IAM/PAM vendor → positions Krutho inside the category it explicitly rejects.
- Identity implies Krutho must be trusted or present → contradicts the mechanism.
- Identity reads as AI-first rather than identity-first → miscategorises what Krutho is.
- Identity requires customer evidence to be credible → brittle at the pre-seed stage; cannot hold.

---

## 11. Open Questions

**Q1: What is Vouch's visibility at developer touchpoints?**
The GitHub repository owner is `anthonymaley`. The npm namespace is `@krutho/core`. The brand decision is Krutho-only. How this maps to visible infrastructure (GitHub org, npm org, documentation domain) must be validated before modules begin.
Assumption: Krutho operates as an independent brand. Vouch is parent-company only.
Risk: Naming friction at developer-first touchpoints where Vouch infrastructure is visible.
Who can resolve: Client.

**Q2: Who is the primary decision-maker in the buying process?**
Brief assumes: Developer adopts → platform team governs → CISO approves. Developer is the primary identity audience.
Risk: If the CISO is actually the primary buyer, the identity brief needs to rebalance authority toward enterprise trust first. This would change the hypotheses substantially.
Who can resolve: Client, through sales or GTM experience to date.

**Q3: What visual decisions are already in use?**
Brief assumes: No prior identity constraints. New brand, full latitude.
Risk: If the documentation site or other surfaces are already externally visible and associated with Krutho, the brief may underestimate continuity obligations.
Who can resolve: Client — share `favicon.svg` and `custom.css` for review.

**Q4: What is the target outcome — ecosystem standard or strategic acquisition?**
Brief assumes: Krutho is building for ecosystem adoption. Identity reflects that posture.
Risk: If a specific strategic acquirer is in view, identity may need to signal compatibility with their existing framework.
Who can resolve: Client.

---

## Reviewer Handoff

This is the most significant review point. The questions to ask:

1. Does Stage 1 show its reasoning clearly, or does it jump to conclusions?
2. Do the Stage 2 brief sections follow logically from Stage 1?
3. Do the active tensions feel real — or has something been smoothed over?
4. Does the central position feel like it follows from the evidence, or does it feel invented?
5. Are the rejection criteria specific enough to use as real filters?
6. Are the identity gate questions genuine structural constraints or reworded preferences?
7. Does anything in the brief feel like it came from outside the extraction?

If the brief passes this review, hypotheses can be generated with confidence.
