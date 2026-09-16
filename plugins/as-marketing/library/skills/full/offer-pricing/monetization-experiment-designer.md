# Monetization Experiment Designer

**Version:** 1.0  
**Maturity:** full skill

## Purpose
Test a revenue mechanism, price, package, term, or value metric with bounded commercial, customer, operational, and reputational risk.

## Owns
Commercial hypothesis, test design, audience/exposure, variants, economic metrics, guardrails, stopping rules, customer handling, and learning record.

## Use when
A monetization choice has meaningful uncertainty that can be reduced through a controlled offer or market test.

## Do not use when
General experiment methodology → Experiment Design Strategist. Pricing decision without a test → Pricing and Packaging Strategist. Offer is undefined → Offer Architecture Strategist.

## Required inputs
Decision, hypothesis, audience, offer, baseline, price/terms, channel, sample, economics, capacity, customer communication, fulfillment/refunds, permissions, and measurement.

## Diagnostic questions
1. What commercial decision follows the result?
2. Which single primary hypothesis is tested?
3. What behavior indicates value, not curiosity?
4. What economic and quality guardrails apply?
5. What concurrent changes could confound interpretation?
6. Can the offer be fulfilled for every exposed customer?
7. What fairness, legal, disclosure, or migration issue exists?
8. What stops the experiment early?

## Experiment readiness rubric
Rate 0–3 for decision clarity, hypothesis isolation, audience definition, baseline/comparison, exposure control, economic measurement, fulfillment readiness, customer fairness, sample adequacy, and stopping rule. Any zero in truthful offer, fulfillment, or customer safety blocks launch.

## Method and decision gates
1. Define one decision and primary hypothesis.
2. Select audience, exposure, variant, and comparison.
3. Define behavior, revenue/contribution metric, quality guardrails, duration, and stopping rule.
4. Control or document confounding.
5. Prepare fulfillment, terms, communication, refunds, migration, and approval.
6. Run without changing definitions mid-test.
7. Analyze behavior, quality, economics, uncertainty, and segment limits.
8. Decide adopt, iterate, reject, or research.

## Examples
- **B2B service:** test paid diagnostic versus free discovery with matched qualification and delivery capacity.
- **SaaS:** test packaging/value metric without simultaneously changing onboarding and audience.
- **Ecommerce/physical product:** test bundle or subscription economics including returns, fulfillment, churn/cancellation, and inventory.

## Output format
```markdown
# Monetization Experiment
## Decision and hypothesis
## Audience and eligibility
## Baseline, variants, exposure
## Primary behavior and economic metrics
## Guardrails and stopping rules
## Fulfillment, terms, fairness, approvals
## Confounds and limitations
## Analysis by segment
## Adopt / iterate / reject decision
## Learning record and next test
```

## Quality checks
One primary change; decision rule set before launch; contribution measured; fulfillment ready; customer treatment fair; uncertainty reported; early results not called.

## Success criteria
The experiment reduces a monetization uncertainty enough to make a defined decision without creating disproportionate customer or operating harm.

## Failure conditions
Multiple uncontrolled changes; no baseline; misleading pricing; unfulfillable demand; vanity metric; sample too small; post-hoc success definition.

## Guardrails
Do not fabricate willingness to pay, use deception, discriminate unlawfully, or expose customers to terms the business cannot honor. Approval may be required for live commercial changes.

## Routes to
Pricing and Packaging Strategist, Experiment Design Strategist, Unit Economics Analyst, Offer Architecture Strategist.