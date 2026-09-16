# Pipeline Process Designer

**Version:** 1.0  
**Maturity:** full skill

## Purpose
Define opportunity stages, buyer-progress evidence, ownership, next actions, inactivity rules, review discipline, and forecasting hygiene.

## Owns
Opportunity lifecycle, stage definitions, entry/exit evidence, ownership, required next action, stage regression, closed/nurture/disqualified logic, stale-deal rules, review cadence, and pipeline metrics.

## Use when
A business needs a shared, observable process for managing qualified opportunities and distinguishing buyer progress from seller activity.

## Do not use when
CRM object/field design → CRM Architecture Strategist. Cross-team lifecycle → Revenue Operations Architect. Discovery criteria → Discovery and Qualification Architect. Forecast modeling → Forecasting and Scenario Analyst.

## Required inputs
Actual buying journey, sales process, opportunity data, cycle length, stakeholders, CRM constraints, ownership, review cadence, loss/no-decision reasons, forecasting needs, and historical records.

## Diagnostic questions
What buyer decision occurs at each stage? Which evidence proves it? What seller activity is currently mistaken for progress? Who owns the next action? How long can a deal remain inactive? When does it regress, nurture, close, or disqualify? Which fields support decisions rather than reporting burden?

## Stage quality score
Rate 1–5 for buyer observability, mutual commitment, evidence clarity, distinctness, actionability, forecast usefulness, historical validity, ownership, and data burden. Label stage assumptions **fact**, **estimate**, **assumption**, or **inference**. “Proposal sent” and “follow-up attempted” cannot alone define buyer progress.

## Method and decision gates
1. Map the customer decision process and real variations using historical evidence.
2. Create the fewest useful stages; separate qualification, evaluation, commercial decision, and implementation commitment where relevant.
3. Define for each stage: purpose, entry evidence, required evidence, owner, buyer commitment, next action, exit, maximum inactivity, and regression.
4. Add closed-won, closed-lost, no-decision, nurture, disqualified, duplicate, and abandoned logic with reason codes.
5. Define close-date governance, amount confidence, stage changes, exceptions, and required fields.
6. Establish review cadence, stale-deal actions, escalation, and data-quality checks.
7. Measure stage conversion, time, velocity, slippage, losses, no-decision, forecast error, and cohort/source differences.
8. Validate against historical opportunities; revise definitions that fail to distinguish outcomes.

## Examples
B2B service: stages based on confirmed problem, mutual scoping, decision case, and approved start. SaaS: qualification, technical/security evaluation, commercial approval, procurement, and launch commitment. Ecommerce/physical product B2B: buyer interest, assortment review, commercial terms, sample/quality approval, purchase order, and fulfillment readiness.

## Output format
```markdown
# Pipeline Process
## Buying journey and opportunity definition
## Stage dictionary
## Entry, evidence, exit, owner, inactivity
## Regression, nurture, loss, no-decision rules
## Required fields and reason codes
## Review cadence and stale-deal actions
## Metrics and forecast hygiene
## Historical validation and governance
## Risks and next routes
```

## Quality checks
Stages represent buyer progress; evidence is observable; owners and next actions are explicit; stale deals cannot hide; closed and nurture states are distinct; required data is minimal and decision-useful.

## Success criteria
Teams manage opportunities consistently, identify real progress and risk, reduce stale pipeline, and produce more trustworthy operational and forecast inputs.

## Failure conditions
Seller activities as stages; too many stages; no exit evidence; close dates roll silently; lost/no-decision reasons absent; forecast certainty exceeds evidence; CRM burden prevents adoption.

## Guardrails
Do not force false certainty, inflate pipeline, or change stages silently. Stage probability is not a substitute for deal-specific evidence.

## Routes to
CRM Architecture Strategist, Discovery and Qualification Architect, Revenue Operations Architect, Forecasting and Scenario Analyst.