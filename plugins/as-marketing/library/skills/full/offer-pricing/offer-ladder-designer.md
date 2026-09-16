# Offer Ladder Designer

**Version:** 1.0  
**Maturity:** full skill

## Purpose
Create a sequence of offers matching increasing trust, commitment, customer value, evidence, and delivery depth.

## Owns
Entry offer, expansion sequence, level value, qualification, transitions, proof flow, price logic, capacity/economics, alternatives, and stop rules.

## Use when
Customers need different commitment levels or a natural path exists from initial value to deeper outcomes, repeat purchase, implementation, or expansion.

## Do not use when
Only one offer needs design → Offer Architecture Strategist. General retention/expansion process → Expansion and Renewal Planner. Business-model evolution → Offer Evolution Planner.

## Required inputs
ICP, jobs/triggers, current offers, buying risk, journey, proof, pricing, delivery capacity, expansion evidence, retention/repeat behavior, and economics.

## Diagnostic questions
1. What is the smallest standalone valuable outcome?
2. What customer decision follows each outcome?
3. What new need, evidence, usage, maturity, or scale triggers progression?
4. Can customers enter at the appropriate level?
5. Does each level create value independently?
6. What proof does each level produce?
7. Can operations support conversion between levels?
8. Which step is artificial or serves only the seller?

## Ladder viability rubric
Rate 0–3 for standalone value, trigger clarity, natural progression, qualification, proof creation, commercial logic, delivery capacity, economics, customer choice, and measurement. Any zero in standalone value means remove the step.

## Method and decision gates
1. Define entry problem and smallest valuable outcome.
2. Map subsequent jobs, decisions, and expansion triggers.
3. For each level define audience, outcome, mechanism, scope, proof, price logic, qualification, and handoff.
4. Test standalone value and customer freedom.
5. Remove artificial gates, dead ends, and duplicated offers.
6. Model conversion, contribution, capacity, retention, and learning.
7. Define transition, skip, downgrade, stop, and alternative paths.
8. Measure value progression rather than upsell pressure.

## Examples
- **B2B service:** paid diagnostic → bounded pilot → implementation → managed support, each solving a distinct decision/job.
- **SaaS:** self-serve/use-case package → team plan → enterprise governance based on actual usage and complexity.
- **Physical product/ecommerce:** trial size → core product → replenishment/bundle, without forcing a subscription before repeat value.

## Output format
```markdown
# Offer Ladder
## Customer journey and trigger map
## Entry offer
## Level-by-level briefs
## Standalone value and proof produced
## Qualification and disqualification
## Transition, skip, downgrade, stop paths
## Pricing logic and economics
## Delivery capacity and handoffs
## Metrics and validation
## Removed artificial steps
```

## Quality checks
Every step creates value; transitions follow customer progress; qualification is explicit; customers are not trapped; proof flows forward; economics/capacity support progression.

## Success criteria
The ladder reduces buying risk while allowing customers to reach the right value level through natural evidence-based transitions.

## Failure conditions
Lead magnet without value; forced stages; redundant packages; progression based only on seller revenue; no trigger; operational handoff breaks; subscription before recurring value.

## Guardrails
Do not force unnecessary steps, hide the most suitable offer, or design manipulative lock-in. Expansion must follow customer value and consent.

## Routes to
Offer Architecture Strategist, Paid Pilot Designer, Pricing and Packaging Strategist, Expansion and Renewal Planner.