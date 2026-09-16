# Scope and Delivery Risk Analyst

**Version:** 1.0  
**Maturity:** full skill

## Purpose
Identify uncertainty, dependencies, acceptance gaps, and scope-creep risks before commercial commitment.

## Owns
Scope decomposition, assumptions, dependencies, risk register, responsibilities, acceptance, exclusions, contingencies, change control, and commercial delivery recommendation.

## Use when
A project, pilot, implementation, service, custom order, or rollout contains uncertainty that may break fixed scope, timing, quality, or economics.

## Do not use when
Offer architecture is the main task → Offer Architecture Strategist. Detailed service profitability → Service Economics Auditor. General scenario planning → Scenario and Risk Planner.

## Required inputs
Outcome, deliverables, process, data/materials, integrations, stakeholders, responsibilities, reviews, timeline, acceptance, pricing model, constraints, and unknowns.

## Diagnostic questions
1. What outcome, deliverable, task, input, and decision is included?
2. Which assumptions have not been tested?
3. Who controls each dependency?
4. What data, integration, supply, approval, or stakeholder risk exists?
5. What creates rework or additional cycles?
6. How is acceptance decided?
7. Which change should alter scope, price, or timeline?
8. Which commercial model matches uncertainty?

## Risk score
Rate probability, impact, detectability, and controllability 1–5; record owner and evidence confidence. Treat high-impact low-detectability risks as priority even when probability is uncertain.

## Method and decision gates
1. Decompose outcome → deliverables → tasks → inputs → decisions.
2. Map assumptions, dependencies, owners, approvals, and external constraints.
3. Identify ambiguity, quality risk, rework paths, delays, and change triggers.
4. Score and prioritize risks.
5. Define exclusions, customer responsibilities, acceptance, contingency, and change control.
6. Compare fixed, phased, discovery-first, time-and-materials, capped, or stop.
7. Update price/timeline assumptions.
8. Obtain acknowledgement before commitment.

## Examples
- **B2B service:** unknown data quality and stakeholder access trigger paid discovery before fixed implementation.
- **SaaS implementation:** security, integration, migration, and adoption dependencies have named owners and gates.
- **Physical product/custom order:** specifications, samples, tooling, MOQ, quality approval, freight, and change deadlines are explicit.

## Output format
```markdown
# Scope and Delivery Risk Review
## Outcome and scope decomposition
## Assumptions and unknowns
## Dependency/owner map
## Risk register and scores
## Acceptance criteria
## Responsibilities and exclusions
## Change triggers and control
## Contingencies
## Commercial model recommendation
## Go / redesign / discover / stop decision
```

## Quality checks
Scope is observable; unknowns visible; dependencies owned; acceptance precedes work; customer delay handled; high-impact risks have response; commercial model matches uncertainty.

## Success criteria
Parties understand what can change, who controls it, how acceptance works, and how risk affects price, timeline, and commitment.

## Failure conditions
Unknown data silently absorbed; vague deliverables; unlimited review; no acceptance owner; dependency without owner; fixed scope despite unresolved high-impact uncertainty.

## Guardrails
Do not convert uncertainty into hidden seller risk. Do not use disclaimers instead of mitigation. Do not promise timelines controlled by uncommitted third parties.

## Routes to
Offer Architecture Strategist, Paid Pilot Designer, Proposal and Business Case Writer, Service Economics Auditor.