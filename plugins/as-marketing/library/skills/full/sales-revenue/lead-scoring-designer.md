# Lead Scoring Designer

**Version:** 1.0  
**Maturity:** full skill

## Purpose
Prioritize leads or accounts for a defined operational decision using evidence-backed fit, explicit intent, engagement, timing, and negative signals.

## Owns
Score decision, factor taxonomy, weights or model logic, thresholds, decay, caps, missing-data behavior, reason codes, validation, human review, drift monitoring, fairness checks, and recalibration.

## Use when
A team has more eligible records than it can treat equally and needs transparent prioritization linked to acceptance or progression outcomes.

## Do not use when
Routing ownership → Lead Routing Designer. ICP design → ICP and Segmentation Architect. General prediction without operational action is not a useful score. Fit alone is not active demand.

## Required inputs
Score purpose, ICP, lifecycle, historical outcomes, explicit and behavioral signals, source quality, CRM fields, capacity, routing, rejection reasons, sampling bias, permissions, and measurement windows.

## Diagnostic questions
Which decision will the score control? What outcome defines usefulness? Which signals are observed versus inferred? Are they reliable, fresh, available, and lawful? How does missing data behave? What capacity threshold exists? Could the score encode source, demographic, or access bias? How will users see reasons?

## Factor quality score
Rate each factor 1–5 for predictive evidence, reliability, freshness, coverage, actionability, fairness, manipulability, leakage risk, and maintenance cost. Label evidence **fact**, **estimate**, **assumption**, or **inference**. Weak engagement cannot be relabeled as intent.

## Method and decision gates
1. Define one operational decision, eligible population, action, owner, capacity, and outcome window.
2. Separate stable fit, explicit intent, observed engagement, recency/timing, relationship, and negative/disqualifying signals.
3. Select factors tied to historical outcomes or an explicit strategic hypothesis; document provenance and limitations.
4. Define weights/model, interactions, caps, thresholds, decay, missing values, duplicate behavior, and reason codes.
5. Back-test on accepted, rejected, progressed, won, lost, inactive, and relevant holdout/cohort records.
6. Evaluate precision, recall, lift, calibration, workload, source effects, bias, leakage, and gaming.
7. Launch in shadow or human-review mode; compare score to real decisions and record overrides.
8. Monitor drift, acceptance, progression, false positives/negatives, capacity impact, and fairness; recalibrate or retire.

## Examples
B2B service: prioritize inquiries using ICP fit, explicit project context, timing, and negative delivery constraints. SaaS: combine account fit, explicit evaluation actions, product-relevant behavior, and decay. Ecommerce/physical product B2B: score retailer/distributor inquiries by market fit, assortment need, commercial readiness, geography, and fulfillment feasibility.

## Output format
```markdown
# Lead Scoring Design
## Operational decision and population
## Outcome, capacity, action
## Factor dictionary and evidence
## Weights/model, caps, decay, missing data
## Thresholds and reason codes
## Back-test and bias/leakage review
## Shadow launch and human review
## Monitoring, drift, recalibration
## Risks and next routes
```

## Quality checks
Score controls a real decision; fit and intent remain separate; factors are observable and maintained; missingness is explicit; thresholds fit capacity; reasons are visible; overrides become learning.

## Success criteria
The score improves prioritization quality and workload allocation relative to the existing process while maintaining transparency, fairness, and recalibration discipline.

## Failure conditions
Score treated as truth; weak clicks as buying intent; weights invented with false precision; unavailable fields; historical leakage; biased source proxy; no action or owner; no drift review.

## Guardrails
Do not infer sensitive traits or private intent, use unlawful data, or automate irreversible exclusion without review and appeal. State predictive uncertainty.

## Routes to
ICP and Segmentation Architect, Revenue Operations Architect, Lead Routing Designer, Marketing Analytics Analyst.