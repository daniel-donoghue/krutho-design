# Krutho Design Philosophy

Last edit 10th April 2026

---

## Grounding Statement

This document is the Krutho Design Philosophy. It defines the terms precision, correctness, verifiability, and truth, and establishes the chain that governs every document derived from it. All other Krutho design system documents operate under this one.

---

## Terms

Four terms govern this document. Each is defined once. Each is used throughout in its defined sense only. No term substitutes for another.

**Precision**
A property of construction. A thing is precise when it is defined without ambiguity: when its boundaries, behaviour, and meaning cannot be reasonably misread. Precision is a condition applied at the point of making. It is not a quality added afterward.

**Correctness**
A property of conformance. A thing is correct when its behaviour matches its specification. Correctness is relational: it requires something to be correct *against*. A thing cannot be correct in isolation. Correctness is determined by inspection, not by assertion.

**Verifiability**
A property of accessibility. A correct thing is verifiable when its correctness can be confirmed by an independent party through inspection, without requiring trust in the maker. Verifiability is the condition that makes correctness operationally useful. Correctness that cannot be verified is indistinguishable from incorrectness.

**Truth**
The output of verification. Truth is not a claim made about a thing. It is what remains after a correct thing has been verified. Truth cannot be asserted. It can only be demonstrated.

---

## The Chain

The four terms are not independent. They form a directed chain. Each term is a precondition for the next.

```
Precision → Correctness → Verifiability → Truth
```

**Precision enables correctness.**
Without precision, there is no specification to conform to. A thing cannot be determined correct or incorrect if its expected behaviour is ambiguous. Precision is the minimum condition for correctness to be assessable.

**Correctness enables verifiability.**
A thing that does not conform to its specification cannot be verified as correct: only as incorrect, or as unverifiable. Verifiability requires something correct to verify. A broken chain at this point produces a result that appears verifiable but is not.

**Verifiability enables truth.**
Correctness without verifiability cannot produce truth. It can produce an assertion of truth, which is a different thing. An assertion requires trust. Truth requires only inspection. The chain is broken if correctness exists but cannot be inspected independently.

**A break at any point in the chain produces failure.**
If precision fails, correctness cannot be established. If correctness fails, there is nothing to verify. If verifiability fails, truth cannot be demonstrated. The chain does not degrade gracefully. It either holds completely or it does not hold.

---

## Philosophy

**1. The domain this philosophy operates in requires correctness.**

Krutho issues short-lived cryptographic certificates that bind human authorization to AI agent actions. These certificates are inspectable by any party, without contacting Krutho. The verification is independent. The chain is not aspirational in this domain: precision in the certificate format, correctness in the signature, verifiability without trust, truth as the output of inspection. It is functional. A certificate that breaks the chain is not a degraded certificate. It is not a certificate.

The same chain governs how Krutho presents.

**2. Presentation is not separate from product.**

An organization that operates in a domain requiring correctness and presents with ambiguity has broken the chain at its boundary. The break is not contained. It propagates: into the reading of the product, into the trust placed in the documentation, into the confidence of the person deciding whether the system can be relied upon.

Presentation is not aesthetic decoration applied to a correct system. It is part of the system. It is subject to the same chain.

**3. Precision is not a property of appearance. It is a property of construction.**

A precise thing is not one that looks exact. It is one that is defined without ambiguity: where every decision traces to a reason, and that reason excludes the alternatives. A design decision that could have gone another way without consequence is not a precise decision. It is an arbitrary one.

Arbitrary decisions accumulate. They produce a system in which decisions cannot be traced, conformance cannot be assessed, and correctness cannot be determined. The system becomes unverifiable. Nothing that cannot be verified can produce truth.

**4. Correctness requires a specification. The specification is not negotiable mid-inspection.**

A thing is correct against its specification at the time of inspection. A specification that changes during inspection is not a specification. It is a moving target, which is a form of imprecision. Once a specification is established, the question of correctness is closed to interpretation. It is open only to inspection.

This applies to the design system. The specification must be complete enough that any output can be assessed for correctness against it. An output that cannot be assessed is a failure of specification, not of the output.

**5. Verifiability requires independence.**

If a thing can only be verified by its maker, it has not been verified: it has been asserted. Verification requires that an independent party can inspect the thing and reach the same conclusion. This requires that the chain is fully externalised: the specification is accessible, the correctness criteria are legible, and the inspection process requires no privileged knowledge.

Documentation that omits the reasoning behind a decision is not verifiable. It requires trust in the maker's judgment. Trust is not verification.

**6. Truth is demonstrated, not claimed.**

A system that performs trustworthiness is not trustworthy. A system that performs precision is not precise. A system that asserts correctness without making itself inspectable has claimed truth, which is the opposite of demonstrating it.

This philosophy does not claim that Krutho is precise. It establishes what precision means in this domain, and it governs what Krutho builds and how Krutho presents against that definition. The assessment of whether Krutho is precise is made by inspection, not by Krutho.

**7. Simplicity is a verifiability condition, not an aesthetic one.**

A thing that is more complex than its function requires is harder to inspect. Unnecessary complexity introduces ambiguity: not in intent, but in inspection. If an independent party cannot determine what a thing is doing, they cannot verify whether it is doing it correctly.

Simplicity in design, copy, and documentation is a structural requirement of the chain. A simpler thing is easier to inspect. An inspectable thing can be verified. A verified thing can produce truth. Simplicity is therefore not a stylistic preference. It is a functional one.

**8. Omission governs as much as inclusion.**

A specification defines what belongs. It also defines, by omission, what does not. A decision that has no basis in the specification does not exist in a neutral state. It exists as a violation of the specification. The boundary of the specification is not soft.

This applies in both directions. A thing that should be present and is absent is a failure of correctness. A thing that should be absent and is present is also a failure of correctness.

---

## Operational Conditions

The philosophy produces a set of conditions that apply to everything built, written, or published under it.

**Every decision must trace to a reason.**
Not a preference. Not a convention. A reason that excludes the alternatives. If a decision cannot be traced, it is arbitrary. Arbitrary decisions are imprecise. Imprecise decisions break the chain.

**Every specification must be complete enough to assess conformance.**
A specification that leaves decisions to interpretation is not a specification. It is a direction. Directions cannot produce correctness, because correctness requires a closed criterion.

**Every document must be self-contained.**
A document that requires external knowledge to interpret is not independently verifiable. Reasoning must be present in the document that contains the decision it governs.

**No term defined here is substituted for another.**
Synonymy in defined terms introduces ambiguity. Ambiguity breaks precision. The terms in this document are used in their defined senses throughout. A reader, human or machine, can depend on this.

**No claim is made that cannot be verified by inspection.**
If a property of Krutho is asserted and cannot be verified, the assertion is excluded. The demonstration is preferred in all cases where it is available.

---

## Design Criteria

The chain applies to the design system without modification. These criteria are derived from it. They govern admission and exclusion of every element in the system.

**An element is admitted only if it has a function traceable to the chain.**
An element that cannot be connected to precision, correctness, verifiability, or truth in this domain has no basis for inclusion. Aesthetic preference is not a basis. Convention is not a basis. An element without a traceable function is arbitrary, and arbitrary decisions are imprecise.

**Each element has one function.**
An element that serves multiple functions introduces ambiguity about which function governs its correct form. Ambiguity breaks precision. Where a single element appears to serve multiple functions, those functions must be separated or one must be identified as primary and the other excluded.

**Constraint is the method.**
The system is defined as much by what it excludes as by what it includes. An element not present in the specification does not exist in a neutral state. Its absence is a decision. Its unauthorised presence is a failure of correctness.

**Every element must be assessable for correctness.**
If an element cannot be inspected and determined correct or incorrect against the specification, the specification is incomplete. The failure belongs to the specification, not the element. An incomplete specification must be completed before the element is used.

**No element performs a property it does not have.**
An element that appears precise without being precisely defined is not precise. An element that appears simple without being reducible to a single function is not simple. The property must be present in the construction, not performed in the appearance.

---

## System Terms

The four terms defined above govern this philosophy. The documents derived from this philosophy use additional shared terms whose formal specification belongs to those documents. One such term is referenced widely enough that a provisional definition is recorded here so that any document operating under this philosophy can be read without external knowledge.

**Surface.**
A rendered output context to which the Krutho design system applies. A surface is the specific medium in which the foundations are realised: web, diagrams, decks, print, application UI, brand artifacts. The formal specification of surface classes, their characteristics, and the conditions for selecting between them is the subject of the Krutho Surface System, which is published separately. Until that document is published, the term is used provisionally. Foundation documents that depend on a surface declaration record this dependency explicitly.

---

## Summary

> **Not claimed. Proven.**
> 
> The brand doesn't claim. It demonstrates.
> It doesn't say it's precise, it is precise.
> It doesn't say it's trustworthy, it behaves in a way that is verifiable.
> 
> Every output is built to be inspected.
> Every statement traces to evidence.
> Every artifact can be verified.
> 
> Correctness is not aesthetic.
> It is operational truth.
> 
> Krutho operates in a domain where systems must be correct.
> So does the design.

This summary is a derived artifact. It is not the source of this philosophy. Every statement in it traces to the terms, chain, and philosophy statements above. It is included as evidence that the philosophy is articulable in natural language. That articulability is itself a verifiability condition.
