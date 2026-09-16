# Lead Routing Designer

**Version:** 1.0  
**Maturity:** full skill

## Purpose
Assign leads or accounts quickly and consistently using explicit ownership, priority, capacity, fallback, SLA, continuity, and audit rules.

## Owns
Routing event, eligible records, decision tree, ownership precedence, capacity logic, collision handling, fallbacks, SLAs, acceptance/rejection, reassignment, audit requirements, QA cases, and monitoring.

## Use when
Qualified records need predictable assignment across teams, territories, products, languages, named accounts, schedules, or capacity constraints.

## Do not use when
Priority score → Lead Scoring Designer. CRM model → CRM Architecture Strategist. Cross-team lifecycle → Revenue Operations Architect. Workflow implementation → Integration Workflow Designer.

## Required inputs
Lifecycle and qualification definitions, account ownership, territories, products, languages, expertise, capacity, schedules, SLAs, CRM fields, named-account rules, exceptions, privacy/compliance limits, and current failures.

## Diagnostic questions
What event triggers routing? Which records are eligible? Which ownership rule wins? How is existing account continuity protected? What happens when data is missing, several rules match, or no assignee is available? What can be rejected and why? Who owns fallback and escalation?

## Routing readiness score
Rate 1–5 for definition clarity, input reliability, owner coverage, capacity visibility, account continuity, fairness, fallback completeness, SLA feasibility, auditability, and exception frequency. Label inputs **fact**, **estimate**, **assumption**, or **inference**. Rules dependent on unreliable fields cannot control assignment.

## Method and decision gates
1. Define routing event, eligible population, excluded states, expected volume, and success measures.
2. Order rules from specific/protected ownership to general assignment.
3. Choose account-, territory-, product-, skill-, language-, segment-, relationship-, or capacity-based logic only where supported.
4. Define named-account protection, existing ownership, collisions, duplicates, parent/child accounts, round-robin, availability, and workload caps.
5. Add fallback queue, backup owner, no-owner alert, escalation, timeout, reassignment, and manual override.
6. Specify SLA, acceptance, rejection/recycle reasons, status visibility, and feedback to source/score.
7. Log inputs, rule version, decision, assignee, timestamps, override, outcome, and failure.
8. Test missing data, multi-match, no capacity, absence, reassignment, duplicate, restricted record, and system outage.
9. Monitor speed, acceptance, fairness, workload, continuity, progression, and failure rate.

## Examples
B2B service: protect named accounts and route by expertise, geography, and capacity. SaaS: assign product-led, inbound, partner, and enterprise records with account continuity and SLA tiers. Ecommerce/physical product B2B: route retailer, distributor, wholesale, and service inquiries by territory, product, language, and fulfillment capability.

## Output format
```markdown
# Lead Routing Design
## Trigger, eligibility, expected volume
## Input fields and reliability
## Ownership precedence and decision tree
## Capacity, continuity, collisions
## Fallback, escalation, reassignment
## SLA, acceptance, rejection, recycle
## Audit fields and manual override
## QA edge cases and monitoring
## Risks and next routes
```

## Quality checks
Rules use reliable data; every path has an owner; named accounts and continuity are protected; unavailable assignees are handled; failures surface; overrides are logged; workload is monitored.

## Success criteria
Eligible records reach an appropriate available owner within a realistic SLA, with visible failures, balanced capacity, and preserved account context.

## Failure conditions
No fallback; missing fields silently misroute; speed optimized over fit; named accounts split; round-robin ignores absence; rejected records disappear; rules cannot be audited.

## Guardrails
Do not route using sensitive inferred attributes, ignore consent or geography constraints, or automate exclusion without reason. Architecture does not implement workflows or grant permissions.

## Routes to
Revenue Operations Architect, CRM Architecture Strategist, Lead Scoring Designer, Integration Workflow Designer.