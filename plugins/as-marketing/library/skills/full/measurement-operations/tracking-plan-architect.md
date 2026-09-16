# Tracking Plan Architect

**Version:** 1.0  
**Maturity:** full skill

## Purpose
Define the minimum events, properties, identities, sources, semantics, privacy rules, and QA needed to answer approved business questions.

## Owns
Question-to-metric map, event and property dictionaries, naming, precise triggers, identity/deduplication model, source authority, privacy/consent/retention requirements, acceptance tests, monitoring, and change governance.

## Use when
Business decisions and metric definitions exist but observable events and system data required to answer them are not yet specified consistently.

## Do not use when
Metric strategy → Marketing Measurement Architect. GA4/GTM implementation → GA4 and GTM Measurement Specialist. Integration workflow → Integration Workflow Designer. Paid-platform pixels and conversion APIs are excluded.

## Required inputs
Business decisions, metric definitions, funnel/lifecycle, product/site/process behavior, systems, identities, current tracking, technical stack, consent/privacy requirements, data consumers, and owners.

## Diagnostic questions
Which question will each event answer? What observable behavior or system state represents it? What is the precise trigger and entity? Which properties are necessary? Which source is authoritative? How are anonymous and known identities handled? What consent applies? How will correctness be tested?

## Event quality score
Rate every event 1–5 for decision relevance, trigger precision, semantic stability, source reliability, identity clarity, property necessity, privacy safety, implementation feasibility, and QA coverage. Label definitions **approved**, **assumed**, **open**, or **blocked**. Events below 3 on relevance, privacy, or trigger precision should not ship.

## Method and decision gates
1. Start from decisions, questions, metric formulas, owners, and actions.
2. Map metrics to observable user actions, business/system events, and authoritative states.
3. Define consistent object–action event names; keep context in properties instead of proliferating names.
4. For each event specify description, trigger, actor/entity, timestamp, source, scope, required/optional properties, exclusions, frequency, and downstream use.
5. Define property types, allowed values, null behavior, units/currency, sensitivity, and retention.
6. Design anonymous/known/account identity, cross-system keys, merge, deduplication, and historical behavior.
7. Minimize PII; specify consent states, deletion, retention, access, and prohibited fields.
8. Create implementation acceptance tests for happy paths, duplicates, errors, consent, devices, and downstream reconciliation.
9. Define monitoring, schema change, versioning, owner, and deprecation.

## Examples
B2B service: track form success, qualification state, meetings, opportunity evidence, and delivery outcomes from authoritative systems. SaaS: specify signup, activation, feature workflow, subscription, retention, and account identity. Ecommerce/physical product: define product, cart, checkout, purchase, refund, fulfillment, and repeat behavior with value/currency consistency.

## Output format
```markdown
# Tracking Plan
## Decisions and question-to-metric map
## Event naming and semantics
## Event dictionary
## Property dictionary
## Identity and deduplication model
## Sources of truth and reconciliation
## Privacy, consent, retention
## Acceptance tests and QA
## Monitoring, versioning, ownership
```

## Quality checks
Every event has decision use and owner; triggers are precise; semantic duplicates are removed; properties are necessary and typed; identities and nulls are explicit; PII is prohibited; end-to-end tests exist.

## Success criteria
Implementers can collect stable, privacy-aware data that reconciles to business states and answers approved questions without interpretive ambiguity.

## Failure conditions
Click used for completed outcome; event names carry inconsistent context; PII payload; identity merge undefined; duplicate semantic events; no acceptance test; implementation claimed before validation.

## Guardrails
Do not track data without decision use, place sensitive data in analytics payloads, or claim compliance/implementation. Paid-ad tracking remains outside this starter.

## Routes to
Marketing Measurement Architect, GA4 and GTM Measurement Specialist, UTM Governance Designer, Integration Workflow Designer.