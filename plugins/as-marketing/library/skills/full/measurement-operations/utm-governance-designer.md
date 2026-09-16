# UTM Governance Designer

**Version:** 1.0  
**Maturity:** full skill

## Purpose
Create a consistent campaign-link taxonomy, controlled vocabulary, generator specification, validation process, ownership model, and historical mapping.

## Owns
UTM semantics, naming standard, controlled values, hierarchy, versioning, generator inputs, validation, exceptions, legacy mapping, QA, ownership, and change governance.

## Use when
Multiple people, systems, partners, or channels create campaign links and inconsistent parameters reduce reporting reliability.

## Do not use when
Broader attribution model → Attribution Strategist. Event tracking → Tracking Plan Architect. Paid campaign naming or platform optimization is excluded. UTMs do not prove causality.

## Required inputs
Reporting decisions, channels, campaign/program structure, current UTMs, analytics/CRM ingestion, naming conventions, teams/partners, link tools, redirects, privacy constraints, and legacy values.

## Diagnostic questions
Which reporting dimensions are actually needed? What does source versus medium mean? Which hierarchy identifies initiative, audience, asset, variant, region, or language? Who creates and approves links? How are values validated? What happens to old links and unknown values?

## Governance readiness score
Rate 1–5 for decision relevance, semantic clarity, controlled coverage, usability, system compatibility, ownership, validation, legacy mapping, privacy safety, and monitoring. Label mappings **canonical**, **legacy alias**, **exception**, **unknown**, or **invalid**. Do not change semantics without preserving comparability.

## Method and decision gates
1. Define reporting questions and minimum dimensions; remove fields with no use.
2. Specify semantics for source, medium, campaign, content, and term plus when each is blank.
3. Create lowercase controlled vocabularies, delimiter, character, length, reserved-value, and normalization rules.
4. Define hierarchy, stable campaign identifier, audience/asset/variant handling, regional/language versions, and partner conventions.
5. Specify generator inputs, validation rules, examples, error messages, and approval flow.
6. Map legacy and misspelled values to canonical terms without rewriting raw history silently.
7. Define redirect, short-link, CRM capture, cross-domain, and destination-query behavior.
8. Assign creation, approval, QA, documentation, change control, and retirement owners.
9. Monitor unknown, malformed, duplicate, conflicting, PII-bearing, and deprecated values.

## Examples
B2B service: distinguish newsletter, partner, event, founder social, referral, and outreach assets consistently. SaaS: preserve campaign, audience, lifecycle, and variant context across signup. Ecommerce/physical product: govern email, creator, partner, QR, retail, organic social, and catalog links without embedding customer data.

## Output format
```markdown
# UTM Governance Standard
## Reporting decisions and dimensions
## Parameter semantics
## Controlled vocabulary
## Naming and hierarchy rules
## Generator and validation specification
## Examples and exceptions
## Legacy-to-canonical map
## Ownership and change control
## QA monitoring and risks
```

## Quality checks
Each field has one meaning; vocabulary is usable; values survive downstream systems; raw history remains traceable; unknowns are visible; owners and validation exist; URLs contain no PII.

## Success criteria
Campaign links are created consistently, reporting values remain comparable over time, and malformed or risky parameters are detected before widespread use.

## Failure conditions
Fields overloaded; free-form names; taxonomy too complex to use; legacy history rewritten; partner exceptions ungoverned; customer/confidential data placed in URLs; taxonomy mistaken for attribution truth.

## Guardrails
Do not encode PII, secrets, customer names, confidential deal data, or sensitive targeting in URLs. Preserve historical traceability and document every semantic change.

## Routes to
Attribution Strategist, Tracking Plan Architect, Integration Workflow Designer, Reporting and Dashboard Designer.