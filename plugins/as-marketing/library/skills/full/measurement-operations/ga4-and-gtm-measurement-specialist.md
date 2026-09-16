# GA4 and GTM Measurement Specialist

**Version:** 1.0  
**Maturity:** full skill

## Purpose
Translate an approved tracking plan into authorized GA4/GTM configuration and verify that collected data is accurate, consent-aware, and usable.

## Owns
Existing implementation audit, plan-to-GA4/GTM mapping, data-layer requirements, tag/trigger/variable configuration specification or authorized execution, consent behavior, QA, defect documentation, monitoring, and maintenance handoff.

## Use when
An approved tracking plan exists and GA4/GTM must be configured or validated with authorized access.

## Do not use when
Business metrics or event semantics are unresolved → Marketing Measurement Architect / Tracking Plan Architect. Paid-platform pixels, conversion APIs, offline conversion loops, and ad attribution are excluded. Do not claim implementation without access and end-to-end evidence.

## Required inputs
Approved tracking plan, site/app architecture, environments, GA4 property/streams, GTM containers, data layer, consent platform, domain setup, conversion definitions, access, privacy requirements, release process, and QA cases.

## Diagnostic questions
Is the tracking plan approved? Which containers and streams are authoritative? What already fires? How does consent change collection? Which identities and properties are allowed? What cross-domain/referral behavior exists? Who can publish? How will processed reports be verified after debug testing?

## Implementation readiness score
Rate 1–5 for plan completeness, access, environment clarity, data-layer stability, consent configuration, identity/privacy safety, release controls, QA coverage, ownership, and monitoring. Label state **verified**, **observed**, **assumed**, **blocked**, or **not applicable**. Missing authorization or consent clarity blocks publishing.

## Method and decision gates
1. Review approved plan and reject attempts to redefine business metrics during implementation.
2. Audit containers, tags, triggers, variables, streams, duplicate libraries, environments, and consent behavior.
3. Map events/properties to data-layer values, triggers, tags, custom definitions, key events, scope, and exclusions.
4. Specify or implement consistently through authorized release controls; preserve version and rollback.
5. Test each trigger and payload across consent states, browsers, devices, routes, identities, errors, duplicates, and edge paths.
6. Check unwanted PII, internal/bot traffic strategy, referrals, cross-domain behavior, session attribution settings, and data retention.
7. Validate in debug/preview and again in collected reports after processing delay using acceptance cases.
8. Document configuration, evidence, defects, fixes, limitations, owners, monitoring, and change process.

## Examples
B2B service: validate form success and qualified-action events without sending form content as analytics properties. SaaS: map signup/activation events with account-safe identifiers and consent. Ecommerce/physical product: verify product, cart, checkout, purchase, refund, and fulfillment-relevant events with consistent value/currency and no personal data.

## Output format
```markdown
# GA4/GTM Measurement Implementation
## Approved plan and access status
## Existing-state audit
## Data-layer and configuration map
## Consent and privacy behavior
## Environment/version/release plan
## QA cases and evidence
## Defects, fixes, rollback
## Processed-report validation
## Ownership, monitoring, limitations
```

## Quality checks
Plan remains authoritative; containers are not duplicated; triggers are exact; consent states are tested; no PII leaks; conversions/key events use approved definitions; debug and processed data both validate; rollback exists.

## Success criteria
Approved events and properties are collected once, with correct values and consent behavior, and remain traceable through configuration, QA evidence, and monitoring.

## Failure conditions
Untested publish; duplicate tags; click proxy substituted for success; PII in payload; consent bypass; environment confusion; debug-only validation; business definition changed silently.

## Guardrails
Requires authorized access. Do not bypass consent, expose credentials, collect PII, publish untested changes, or implement paid-ad tracking in this starter.

## Routes to
Tracking Plan Architect, Attribution Strategist, UTM Governance Designer, Marketing Analytics Analyst.