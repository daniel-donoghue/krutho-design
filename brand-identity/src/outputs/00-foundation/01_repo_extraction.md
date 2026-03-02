# Phase 1 — Repository Extraction

**Entity:** Krutho / Vouch Krutho
**Extraction date:** 2026-02-26
**Lens status:** Not active (extraction only)

---

## Section 1 — Entity Basics

| Field | Extracted Content | Source Citation |
|---|---|---|
| Entity name | **Krutho** (primary); also referred to as "Vouch Krutho" in technical documents | [README.md, title: "# Krutho"] [docs/technical/overview.md, title: "Vouch Krutho — Overview"] |
| Entity type | Product/SDK/Platform — described as "a certificate-based identity SDK for AI agents" | [docs/business/one-pager.md: "Krutho is a certificate-based identity SDK for AI agents."] |
| One-sentence functional description (their words) | "Certificate-based identity for AI agents, rooted in human biometric trust." | [README.md, subtitle immediately below title] |
| Year founded / operational since | Not explicitly stated. All plan documents are dated February 2026. | [docs/plans/ — all files dated 2026-02-20 through 2026-02-25] |
| Geography (HQ, markets served) | Not evidenced in repository. | — |
| Company stage | "Pre-Seed / Seed" | [docs/business/investor-pitch.md: "Vouch Security \| Pre-Seed / Seed"] |
| Headcount or size indicators | Three co-founders referenced (CEO, CTO, VP Engineering). Post-seed plan includes 2 engineering hires + 1 DevRel hire. GitHub repository owner: `anthonymaley`. | [docs/business/investor-pitch.md, Team section] [docs/business/one-pager.md, Team section] [README.md: "git clone git@github.com:anthonymaley/krutho.git"] |
| Ownership / funding status | Unfunded at time of documentation; raising seed round of $2–3M. Built on top of Vouch's existing biometric identity platform. | [docs/business/investor-pitch.md: "The Ask — Seed Round: $2-3M"] [docs/technical/overview.md: "Vouch Krutho gives AI agents short-lived X.509 certificates"] |

---

## Section 2 — What It Does

| Field | Extracted Content | Source Citation |
|---|---|---|
| Core function | Issues short-lived X.509 certificates to AI agents, cryptographically encoding which human authorized the agent, what it is permitted to do, and when that authorization expires. | [README.md: "Krutho gives AI agents short-lived X.509 certificates that cryptographically prove: 1. Which human authorized the agent to act, 2. What actions the agent is permitted to perform, 3. That authority is genuine — verifiable offline, peer-to-peer, no central server needed"] |
| How it works (mechanism) | (1) Agent generates EC P-256 key pair; (2) Human biometrically approves (Face ID / Touch ID / passkey) the agent's capability request; (3) Krutho CA issues a short-lived X.509 certificate with CBOR-encoded capabilities; (4) Agent presents the certificate to any verifier; (5) Verifier validates the chain offline using pure cryptography and the root CA public key — no network calls. | [README.md, "How It Works" section] [docs/technical/overview.md, "How It Works"] [docs/technical/whitepaper.md, Sections 5 and 6] |
| Key features or capabilities | • Human biometric root of trust (Face ID / Touch ID / passkey) for certificate issuance<br>• CBOR-encoded capabilities embedded in the X.509 certificate itself<br>• Offline peer-to-peer verification (pure cryptography, no network call)<br>• Short-lived TTLs: 1 hour default; 15 minutes financial; 5 minutes admin; 24 hours read-only<br>• CRL/OCSP revocation (emergency kill switch)<br>• Auto-renewal policy for long-running agents<br>• Role system: 5 built-in roles (`purchasing_agent`, `data_reader`, `research_assistant`, `customer_service`, `admin_agent`) + custom roles<br>• Challenge-response with nonce (replay prevention)<br>• Stake level recording in cert (`hi` / `lo`)<br>• 5 standards bridges: OAuth Token Exchange, Google A2A, mTLS, SPIFFE/SPIRE, W3C VC/DID<br>• Framework integrations: Claude Agent SDK, LangChain, CrewAI, AutoGen, MCP<br>• WebAuthn/Passkey browser-based approval (alternative to mobile push) | [README.md; docs/technical/overview.md; docs/technical/whitepaper.md; docs/business/open-source-vs-platform.md] |
| Technology or infrastructure | EC P-256 (secp256r1) key algorithm; SHA256withECDSA signature; X.509v3 certificate format; CBOR (RFC 8949) capability encoding; custom OID `1.3.6.1.4.1.99999.1.1` for capabilities extension; TypeScript monorepo (npm workspaces, 6 packages); Python SDK (PyPI); Clojure backend integration (vouch-master); FastAPI WebAuthn server; @peculiar/x509, @peculiar/webcrypto (TypeScript); pyca/cryptography (Python); cbor-x (TypeScript), cbor2 (Python) | [docs/technical/whitepaper.md, Section 12.1; ONBOARDING.md; docs/project/decisions.md D-01 through D-24] |
| Delivery model | Open-source SDK (Apache 2.0 license, npm/PyPI) for developers; paid "Vouch Platform" for human biometric approval, compliance audit trail, and extension modules. | [docs/business/open-source-vs-platform.md; docs/project/decisions.md D-57, D-68] |
| Integrations or dependencies | OAuth 2.0 Token Exchange (RFC 8693); Google A2A Agent Cards protocol; mTLS (TLS 1.3); SPIFFE/SPIRE; W3C Verifiable Credentials / DID; Claude Agent SDK; LangChain; CrewAI; AutoGen; MCP; Vouch biometric identity backend (production, Clojure) | [README.md, "Standards Bridges" section; docs/technical/overview.md, "How It Integrates"] |

---

## Section 3 — Who It Serves

| Field | Extracted Content | Source Citation |
|---|---|---|
| Primary audience (stated) | "Developers Building Agentic Systems — The person writing `agent.present(nonce)` in their code. They need identity to be as simple as making an HTTP request — not a 6-month IAM integration project." | [docs/business/positioning.md, "Who We're For"] |
| Secondary audiences (stated) | "Platform Teams Deploying Agents at Scale — The team responsible for 'what agents are running, who authorized them, and what can they do?' They need governance, audit trails, and the ability to revoke instantly." | [docs/business/positioning.md, "Who We're For"] |
| Tertiary audience (stated) | "Compliance & Security Teams — The CISO who needs to answer 'can we trace every agent action back to a human?' for SOC2, ISO 27001, or the emerging NIST agent identity standards." | [docs/business/positioning.md, "Who We're For"] |
| Who they are NOT for (stated) | Enterprise IAM teams wanting to manage agents through Okta/Azure AD dashboards; infrastructure teams who only need workload identity; organizations with no agents. | [docs/business/positioning.md, "Who We're NOT For (Yet)"] |
| Audience descriptors used | Developers; platform teams; CISOs; enterprises deploying AI agents; regulated industries (finance, healthcare, government); AI platform builders; service providers | [docs/technical/overview.md, "Why This Matters"; docs/business/positioning.md] |
| Stated customer pain points | • API keys are shared secrets with no human binding<br>• OAuth tokens require central server, weren't built for autonomous agents<br>• No cryptographic proof of who authorized an agent or what it's allowed to do<br>• 80% of organizations deploying autonomous AI cannot tell what those agents are doing in real time<br>• Only 28% can trace agent actions back to a human sponsor<br>• Only 21% maintain real-time inventory of active agents<br>• 44% still using static API keys for agent authentication | [docs/business/investor-pitch.md, "The Problem"; docs/business/competitive-landscape.md, "Market Context"; docs/business/one-pager.md] |
| Stated customer outcomes | • Cryptographic proof of human authorization for every agent action<br>• Offline verification without vendor dependency<br>• Full audit trail from biometric event to agent action<br>• Blast radius of compromised agent measured in minutes<br>• Scoped permissions travel with the credential — no separate policy engine | [README.md; docs/technical/overview.md; docs/business/positioning.md] |
| Any named customers or case studies | None evidenced in repository. | — |

---

## Section 4 — What It Claims

| Field | Extracted Content | Source Citation |
|---|---|---|
| Primary value proposition (their words) | "Krutho is the portable identity credential for AI agents — the only one that cryptographically proves which human authorized which agent to do what, verifiable by anyone, anywhere, offline." | [docs/business/positioning.md, "One-Line Positioning"] |
| Secondary value propositions | "The credential IS the proof. Any service can verify an Krutho certificate offline using just the CA public key. No network call. No vendor dependency. No policy engine lookup. Pure cryptography." | [docs/business/investor-pitch.md, "The Solution"] |
| Stated differentiators ("unlike X, we...") | Three things "only Krutho does":<br>1. **Human Biometric Root of Trust** — "every Krutho certificate traces back to a specific human's biometric approval (Face ID, Touch ID, passkey). Not a password. Not an OAuth consent screen... No one else does this."<br>2. **Capabilities In The Credential** — "encodes the agent's permissions directly in the X.509 certificate as CBOR-encoded extensions... No one else does this."<br>3. **Offline Peer-to-Peer Verification** — "certificates are standard X.509 — verifiable by anyone with the root CA public key. No server. No SDK dependency at verification time... Every competitor requires their infrastructure at verification time." | [docs/business/positioning.md, "The Three Things Only Krutho Does"] |
| Stated competitive positioning | vs. Keycard: "token-based — their dynamic tokens require Keycard infrastructure to validate. Krutho is certificate-based — any service can verify a credential with just our root CA public key."<br>vs. Okta/Auth0: "we bridge to OAuth — we don't replace it. We add what it can't: human accountability binding and offline verification."<br>vs. SPIFFE: "SPIFFE identifies workloads. We add the human authorization layer on top."<br>vs. CyberArk: "they answer 'can this agent access this server?' We answer 'which human authorized this agent to take this action?'" | [docs/business/positioning.md, "Competitive Positioning by Scenario"; docs/business/one-pager.md] |
| Claims about category or market leadership | "The category we're creating is Human-Rooted Agent Identity." "Krutho makes that answer cryptographic, portable, and instant." | [docs/business/positioning.md; docs/marketing/linkedin.md] |
| Any guarantees, SLAs, or performance claims | "Verification in microseconds vs. milliseconds-to-seconds for a token validation round-trip." "85%+ gross margin (SaaS, minimal COGS per approval)" (target, not guarantee) | [docs/business/positioning.md, "3. Offline Peer-to-Peer Verification"; docs/business/investor-pitch.md] |

---

## Section 5 — Market & Industry Context

| Field | Extracted Content | Source Citation |
|---|---|---|
| Industry or sector (stated) | AI agent identity / agentic AI security / non-human identity (NHI) management / identity and access management (IAM) | [docs/business/positioning.md; docs/business/investor-pitch.md; docs/business/competitive-landscape.md] |
| Market size or opportunity (if stated) | Agentic AI market: $7.55B (2025) → $199B (2034), 43.8% CAGR (Precedence Research); NHI management: $9.45B (2024); IAM market (total): $19.8B (2025); SAM estimate: $1.5–3B by 2028; bottom-up SAM: $684M | [docs/business/investor-pitch.md, "Market Opportunity"; docs/business/one-pager.md] |
| Named competitors (if stated) | Keycard ($38M, a16z); Okta/Auth0 (public, $12B); CyberArk (public, $12B); Teleport ($110M+ raised); SPIFFE (open standard); Aembit ($45M); ConductorOne ($79M, $350M val); Strata Identity; Alter; Defakto ($30.75M Series B); Visa + Akamai | [docs/business/investor-pitch.md, "Competitive Landscape"; docs/business/competitive-landscape.md] |
| Regulatory or compliance context (if stated) | NIST AI Agent Standards Initiative (launched February 2026 — explicitly named); NIST NCCoE lab demonstrations; EU AI Act referenced; SOC2 Type II; ISO 27001; NIST SP 800-229 | [docs/business/competitive-landscape.md: "NIST published a concept paper in Feb 2026"; docs/blog/launch.md; docs/business/compliance-whitepaper.md; docs/project/decisions.md D-69] |
| Market trends referenced | "76% of organizations will have AI agents in production within 3 years"; "44% still using static API keys"; "only 28% can trace agent actions back to a human sponsor"; "nearly 80% deploying autonomous AI cannot tell what those systems are doing in real time"; "Agent proliferation: every major tech company shipping agent capabilities in 2025-2026"; "MCP has no identity layer"; "The window is 12-18 months" | [docs/business/investor-pitch.md; docs/business/competitive-landscape.md] |
| Category language used to describe themselves | "Human-Rooted Agent Identity"; "portable identity credential for AI agents"; "certificate-based identity SDK"; "identity primitive"; "the missing layer in the agentic AI stack" | [docs/business/positioning.md; docs/marketing/linkedin.md; docs/business/one-pager.md] |

---

## Section 6 — Business Direction

| Field | Extracted Content | Source Citation |
|---|---|---|
| Stated mission | Not stated as a formal mission statement. Closest formulation: "Vouch Krutho is built by Vouch — eliminating passwords, starting with identity." | [docs/technical/whitepaper.md, closing line] |
| Stated vision | Not stated as a formal vision statement. Closest formulation from GTM Phase 3: "Become the default identity layer for agent ecosystems." | [docs/business/investor-pitch.md, "Go-To-Market — Phase 3"] |
| Stated values (list each) | Not explicitly listed as values. Principles expressed throughout: intellectual honesty ("Intellectual honesty builds trust. Things we do NOT claim..."); developer-first; security-first; standards-based ("We didn't invent a new cryptographic primitive"); openness ("We give away the format. The product is the human trust chain"). | [docs/business/positioning.md, "What We Don't Claim"; docs/blog/launch.md; docs/business/open-source-vs-platform.md] |
| Short-term goals (stated) | Phase 1 (0–6 months): 500+ GitHub stars; 100+ npm weekly downloads in first 30 days; developer community adoption | [docs/business/investor-pitch.md, "Go-To-Market — Phase 1"] |
| Long-term ambitions (stated) | Phase 3 (12–24 months): NIST reference implementation; A2A ecosystem integration; MCP identity layer standardization; RFC for agent certificate profile; standards body participation; become ecosystem default. At scale: $500K+ ARR → Series A at $35–50M pre-money; or strategic acquisition at $50–150M. | [docs/business/investor-pitch.md] |
| Growth or expansion plans (stated) | Phase 1: Open source SDK → npm/PyPI; Phase 2: Enterprise pipeline (10 pilots, 3 paying customers); Phase 3: Standards play. Seed round allocates 45% to engineering, 25% to DevRel, 15% to enterprise sales, 15% to operations. | [docs/business/investor-pitch.md, "Go-To-Market"] |
| Any stated pivots or changes in direction | Pricing model updated: D-67 supersedes D-58 — moved from per-certificate pricing to per-approval (human-linked approval event) as the billable unit. Revenue model: D-68 supersedes D-59 — "Make the cert format free and ubiquitous everywhere, including on competitor CAs." | [docs/project/decisions.md D-67, D-68] |

---

## Section 7 — Existing Brand & Visual Identity

| Field | Extracted Content | Source Citation |
|---|---|---|
| Current brand name(s) in use | "Krutho" (primary brand name); "Vouch Krutho" (used in technical documents and whitepaper); "Vouch" (parent company name). ONBOARDING.md header: "Vouch Krutho — Onboarding". README.md title: "# Krutho". | [README.md; docs/technical/overview.md; docs/technical/whitepaper.md; ONBOARDING.md] |
| Logo or mark (described or present) | A favicon.svg file exists at `docs-site/public/favicon.svg`. No description of logo form or mark provided in repository text files. | [docs-site/public/favicon.svg — file present, not described] |
| Colour palette (stated or present) | A custom CSS file exists at `docs-site/src/styles/custom.css`. No colour values described in text documents. | [docs-site/src/styles/custom.css — file present, not described] |
| Typography (stated or present) | Not evidenced in repository text files. | — |
| Existing brand guidelines or rules | Not evidenced in repository. | — |
| Brand history or previous identities | Not evidenced. Krutho appears to be a new product name. The npm package name is `@krutho/core`. Python package: `krutho`. | [README.md; package.json references] |
| Brand assets provided (list files) | `docs-site/public/favicon.svg`; `docs-site/src/styles/custom.css`; `docs-site/src/assets/houston.webp`; HTML presentation assets in `docs/assets/`: `demo.html`, `investor-deck.html`, `presentation.html`, `landing.html`, `business-portal.html`, `one-pager.html`, `roi-calculator.html`, `sdk-api-reference.html`, `mobile-screen-flows.html`, `mobile-screen-flows.pdf`; Screen flow images in `docs/images/` (18 PNG files showing mobile approval flow) | [docs-site/; docs/assets/; docs/images/] |
| Any stated brand problems or dissatisfactions | Not evidenced in repository. | — |

---

## Section 8 — Language & Communication

**Repeated phrases or slogans** (with citations):

| Phrase | Citation |
|---|---|
| "Your AI agents should carry ID. Real ID." | [docs/business/positioning.md, Messaging Hierarchy; docs/marketing/linkedin.md; docs/marketing/twitter-thread.md] |
| "Certificate-based identity for AI agents, rooted in human biometric trust." | [README.md, subtitle; docs/business/positioning.md, Sub-headline] |
| "The credential IS the proof." | [docs/business/investor-pitch.md; docs/business/positioning.md; docs/marketing/twitter-thread.md] |
| "Don't replace your stack. Extend it." | [docs/marketing/twitter-thread.md, Tweet 5] |
| "3 lines of code" | [docs/business/positioning.md; docs/business/investor-pitch.md; docs/marketing/linkedin.md] |
| "The moat isn't the code. The moat is the human trust chain." | [docs/business/open-source-vs-platform.md, closing line] |
| "Eliminating passwords, starting with identity." | [docs/technical/whitepaper.md, closing] |
| "The format is free. The human link is the product." | [docs/business/open-source-vs-platform.md, subtitle] |
| "Zero genesis password" | [README.md; docs/technical/whitepaper.md; docs/technical/overview.md] |
| "Blast radius" (used to describe exposure from compromised agent) | [README.md; docs/business/positioning.md; docs/business/investor-pitch.md; docs/marketing/linkedin.md] |

**Key terms or vocabulary unique to this entity** (with citations):

| Term | Citation |
|---|---|
| "Human-Rooted Agent Identity" (stated category name) | [docs/business/positioning.md; docs/business/competitive-landscape.md; docs/marketing/linkedin.md; docs/project/decisions.md D-62] |
| "biometric root of trust" | [README.md; docs/business/positioning.md; docs/technical/whitepaper.md] |
| "short-lived X.509 certificates" | [README.md; docs/technical/overview.md; docs/business/investor-pitch.md] |
| "CBOR-encoded capabilities" | [README.md; docs/technical/whitepaper.md; docs/business/positioning.md] |
| "offline peer-to-peer verification" | [docs/business/positioning.md; docs/blog/launch.md] |
| "capabilities in the credential" | [docs/business/positioning.md; docs/blog/launch.md] |
| "stake level" (hi/lo) | [docs/technical/whitepaper.md; docs/project/decisions.md D-34] |
| "trust chain" | [README.md; ONBOARDING.md; docs/technical/overview.md] |
| "human-linked approval" | [docs/business/open-source-vs-platform.md; docs/project/decisions.md D-67] |
| "krutho:agent:<id>" / "krutho:human:<id>" (URI scheme) | [README.md; docs/technical/whitepaper.md; docs/blog/launch.md] |

**Tone descriptors used in the repo** (how they describe their own voice):

| Descriptor | Citation |
|---|---|
| "Intellectual honesty builds trust" (stated principle) | [docs/business/positioning.md, "What We Don't Claim"] |
| "Developer-first" (used as a category differentiator from competitors) | [docs/business/positioning.md; docs/business/competitive-landscape.md; docs/project/decisions.md D-63] |
| "Three lines of code" (simplicity as a stated value) | [docs/business/positioning.md; docs/business/investor-pitch.md] |
| No explicit tone guide or voice descriptor document found | — |

**Sample language** — 7 representative passages:

| Passage | Source |
|---|---|
| "Your AI agents should carry ID. Real ID. There is a trust gap in enterprise AI that nobody is talking about enough." | [docs/marketing/linkedin.md] |
| "AI agents have an identity crisis. Every AI agent deployed today authenticates using one of two approaches: Static API keys — shared secrets that don't expire, can't be scoped, and don't prove who authorized the agent... OAuth tokens — better, but require a central server to validate, don't carry human accountability..." | [docs/business/investor-pitch.md, "The Problem"] |
| "Krutho isn't a walled garden. We built five bridges so it works with existing infrastructure from day one." | [docs/blog/launch.md] |
| "The key insight: The credential IS the proof. Any service can verify an Krutho certificate offline using just the CA public key. No network call. No vendor dependency. No policy engine lookup. Pure cryptography." | [docs/business/investor-pitch.md, "The Solution"] |
| "The category we're creating is Human-Rooted Agent Identity. This is not IAM. It's not PAM. It's not NHI management. It's not an auth protocol. Those categories answer: 'Can this thing access this resource?' We answer a different question: 'Who authorized this agent, what did they authorize it to do, and can I verify that without trusting anyone else?'" | [docs/business/positioning.md, "The Category We're Creating"] |
| "Think of it like Bluetooth: the spec is free, anyone can build devices, and the value is in what you build on top. We give away the format. The product is the human trust chain, the audit trail, and the extension modules that turn a crypto primitive into a platform." | [docs/business/open-source-vs-platform.md] |
| "Krutho is open source (Apache 2.0) and available today. 145 tests passing across TypeScript and Python. 14 demo scripts. Five standards bridges... Start issuing." | [docs/blog/launch.md, closing] |

**Inconsistencies in language:**

| Inconsistency observed | Source A | Source B |
|---|---|---|
| Entity name: "Krutho" vs "Vouch Krutho" — used interchangeably across files | [README.md: "# Krutho"] | [docs/technical/overview.md: "Vouch Krutho — Overview"; docs/technical/whitepaper.md: "Vouch Krutho"] |
| DID method name: "did:vouch" vs "did:krutho" | [docs/business/open-source-vs-platform.md: "W3C Verifiable Credentials / DID (`did:vouch`)"] | [docs/technical/overview.md: "`did:krutho` DID method"; docs/technical/whitepaper.md: "`did:krutho`"] |
| Pricing unit: "per-certificate" vs "per-approval" | [docs/project/decisions.md D-58: "Per certificate issued ($0.02 Team, $0.015 Enterprise)"] | [docs/project/decisions.md D-67: "Per human-linked approval event" — supersedes D-58; docs/business/open-source-vs-platform.md] |
| Investor pitch team section uses placeholder names "[Founder Name]", "[Co-founder Name]" | [docs/business/investor-pitch.md] | [docs/project/decisions.md D-69: "submitted by Anthony Maley / Vouch Identity"] |

---

## Section 9 — People & Culture

| Field | Extracted Content | Source Citation |
|---|---|---|
| Named founders or leadership | Anthony Maley — identified as submitter of NIST comment and GitHub repository owner (`anthonymaley`). Investor pitch lists three co-founders with placeholder names: [Founder Name] CEO/Co-founder; [Co-founder Name] CTO/Co-founder; [Co-founder Name] VP Engineering/Co-founder. | [docs/project/decisions.md D-69: "submitted by Anthony Maley / Vouch Identity"; README.md: "git clone git@github.com:anthonymaley/krutho.git"; docs/business/investor-pitch.md, Team section] |
| Founder background or credentials (stated) | "The founding team built Vouch's production biometric identity platform. 20M+ identities issued, Face ID/Touch ID enrollment, Datomic audit trail, production infrastructure." | [docs/business/investor-pitch.md, Team section] |
| Team size or composition (stated) | Three co-founders. Post-seed hiring plan: 2 senior engineering hires + 1 DevRel hire. | [docs/business/investor-pitch.md] |
| Culture descriptors (stated) | Not evidenced. TDD (test-driven development) is stated as a project methodology: "Write failing tests first, then implement." "Ensures every feature is testable by design. Prevents over-engineering." | [docs/project/decisions.md D-52] |
| Hiring or talent positioning | Plans for 2 senior engineers (core SDK + human trust platform) and 1 DevRel hire (open source community growth) post-seed. | [docs/business/investor-pitch.md, "The Ask"; docs/business/one-pager.md, "The Ask"] |

---

## Section 10 — Project-Specific Context

| Field | Extracted Content | Source Citation |
|---|---|---|
| Stated brief or design requirements | Not evidenced in repository. No design brief document found. | — |
| Stated deliverables expected | Not evidenced. | — |
| Stated timeline or constraints | Not evidenced. | — |
| Stated stakeholders or decision-makers | Not evidenced. | — |
| Previous agency or design work referenced | Not evidenced. | — |
| Any stated reasons for rebrand or new identity | Not evidenced. This is a new product, not a rebrand. | — |

---

## Coverage Assessment

**Sparse Repo Flag: 1–2 gaps — Proceed to Phase 2.**

| Section | Coverage Rating | Notes on Gaps |
|---|---|---|
| 1. Entity Basics | Partially Evidenced | Geography/HQ not stated. Exact founding date not stated. |
| 2. What It Does | Well Evidenced | Multiple sources, detailed and consistent. |
| 3. Who It Serves | Well Evidenced | Clear audience articulation across multiple documents. Named customers absent (expected at this stage). |
| 4. What It Claims | Well Evidenced | Extensive competitive positioning and value prop documentation. |
| 5. Market & Industry | Well Evidenced | Market sizing, competitor set, regulatory context, trends — all well documented. |
| 6. Business Direction | Partially Evidenced | No formal mission or vision statement. Values inferred from behaviour, not listed. Goals and GTM well documented. |
| 7. Brand & Visual Identity | Not Evidenced | Brand asset files exist (favicon, CSS, HTML decks) but are not described in text. No colour palette, typography, or guidelines documented. |
| 8. Language & Communication | Well Evidenced | Rich vocabulary, repeated phrases, representative passages. Minor inconsistencies noted. |
| 9. People & Culture | Partially Evidenced | One founder identified by name; others placeholder. No explicit culture documentation. |
| 10. Project-Specific Context | Not Evidenced | No design brief, deliverables, timeline, or stakeholders stated. This appears to be a new brand identity project for a new product. |

**Summary:**
- Well Evidenced: 4 sections (2, 3, 4, 5)
- Partially Evidenced: 3 sections (1, 6, 8, 9) — note Section 8 is Well Evidenced for language but Partially for tone descriptors specifically
- Not Evidenced: 2 sections (7, 10)

**Flag level: 2 gaps (Sections 7 and 10) — Proceed to Phase 2.** The brand/visual identity gap is expected for a new product with no prior identity. The project-specific context gap is expected if no formal design brief has been written. These will carry forward as explicit unknowns.

---

## What This Document Is Not

This document does not contain strategic recommendations, positioning statements, design directions, tensions or contradictions, inferences or implications, or lens-derived observations of any kind.
