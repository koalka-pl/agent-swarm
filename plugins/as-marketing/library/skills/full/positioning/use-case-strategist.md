# Use Case Strategist

**Version:** 1.0  
**Maturity:** full skill

## Purpose
Select and structure use cases that demonstrate meaningful value and create feasible adoption.

## Owns
Use-case portfolio, primary/supporting/excluded cases, workflow definition, inputs, mechanism, outcome, evidence, dependencies, implementation risk, and rollout order.

## Use when
Capabilities have many possible applications and the business must choose cases for product, sales, pilot, content, or adoption.

## Do not use when
Broad segment strategy → Product Marketing Strategist. Offer packaging → Offer Architecture Strategist. Pilot scope → Paid Pilot Designer.

## Required inputs
Segments, jobs, workflows, decisions, capabilities, data/material inputs, proof, implementation constraints, frequency, risk, adoption, and commercial relevance.

## Diagnostic questions
1. Who performs what decision or workflow?
2. What is the current approach and consequence?
3. What input is required and realistically available?
4. What mechanism changes the outcome?
5. How frequent and consequential is the case?
6. What adoption or implementation friction exists?
7. Can value be measured and proven?
8. Which tempting cases should be excluded?

## Use-case score
Rate 0–3 for frequency, severity, decision impact, input readiness, mechanism fit, differentiation, proof potential, adoption feasibility, implementation risk, and commercial relevance. A zero in input readiness or feasible outcome blocks rollout.

## Method and decision gates
1. Define user, workflow/decision, current approach, and outcome.
2. Generate candidate use cases without broad labels.
3. Score value, feasibility, proof, and risk separately.
4. Select one primary, limited supporting, and explicit excluded cases.
5. Define inputs, steps, output, human role, limitations, and success.
6. Map dependencies and adoption sequence.
7. Design evidence and rollout gates.
8. Reprioritize from observed usage and outcomes.

## Examples
- **B2B service:** prioritize a repeated high-stakes decision, not “enterprise transformation.”
- **SaaS:** select one workflow with available data and frequent value before adjacent features.
- **Physical product/ecommerce:** define a concrete use occasion with correct-use requirements and repeat potential.

## Output format
```markdown
# Use-Case Portfolio
## User, situation, workflow/decision
## Current approach and consequence
## Candidate scorecard
## Primary and supporting use cases
## Excluded cases
## Inputs, mechanism, output, human role
## Success, proof, and limitations
## Dependencies and adoption friction
## Rollout order and stop conditions
```

## Quality checks
User and workflow are specific; inputs exist; outcome is measurable; mechanism is credible; exclusions protect focus; implementation/adoption risk is visible.

## Success criteria
The selected use case can be delivered, adopted, measured, and used as credible evidence for the next decision.

## Failure conditions
Broad transformation label; unavailable inputs; no owner; one-off novelty; outcome outside control; high risk with no proof plan.

## Guardrails
Do not choose use cases for demo appeal alone. Do not hide required data, behavior, supply, or implementation constraints. Do not imply general capability from one narrow case.

## Routes to
Product Marketing Strategist, Offer Architecture Strategist, Paid Pilot Designer, Content Brief Architect.