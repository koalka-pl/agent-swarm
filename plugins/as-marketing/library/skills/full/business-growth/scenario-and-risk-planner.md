# Scenario and Risk Planner

**Version:** 1.0  
**Maturity:** full skill

## Purpose
Prepare robust decisions and trigger-based responses under material uncertainty without presenting scenarios as forecasts.

## Owns
Decision uncertainty, coherent scenarios, exposure, no-regret actions, reversible bets, hedges, indicators, triggers, and contingency responses.

## Use when
- A decision depends on uncertain external or internal drivers.
- Downside exposure is material.
- Leadership needs pre-agreed responses rather than reactive replanning.
- Timing or staged commitment matters.

## Do not use when
- A quantitative forecast is the primary deliverable → Forecasting and Scenario Analyst.
- Strategy is known and only sequencing is needed → Strategic Planning Architect.
- The task is general risk compliance rather than a business decision.

## Required inputs
Decision, horizon, assumptions, critical drivers, dependencies, exposure, constraints, reversible actions, monitoring access, owners, and review cadence.

## Diagnostic questions
1. What decision must remain robust?
2. Which assumptions could invalidate it?
3. Which drivers are uncertain and materially consequential?
4. What exposure is financial, operational, reputational, regulatory, or strategic?
5. Which actions are reversible, irreversible, or time-sensitive?
6. What leading indicators are observable soon enough?
7. What threshold should trigger which response?
8. What no-regret actions help across scenarios?
9. What contingency lacks an owner or required resource?
10. What event would require abandoning the current strategy?

## Risk readiness rubric
Score 0–3 for driver clarity, scenario coherence, exposure visibility, indicator quality, trigger specificity, response feasibility, owner readiness, and reversibility.

0–7 narrative only; 8–14 incomplete controls; 15–19 decision-useful; 20–24 execution-ready. A zero in observable indicators or feasible response means the contingency is not operational.

## Method and decision gates
1. Define the decision, horizon, and current assumptions.
2. Identify a small set of independent high-impact drivers.
3. Build coherent downside, base, upside, and disruption scenarios.
4. Describe operational consequences, not only market narratives.
5. Identify no-regret actions, reversible bets, hedges, and options.
6. Define leading indicators, thresholds, owners, and response deadlines.
7. Test whether resources and permissions exist for each response.
8. Review on schedule and when triggers fire.

## Examples
- **B2B service:** prepare capacity, pipeline, and cash responses for delayed client decisions rather than predicting exact close dates.
- **SaaS:** connect retention, funding, infrastructure cost, and enterprise demand signals to hiring and product investment gates.
- **Physical product/ecommerce:** connect supplier delay, sell-through, returns, and cash thresholds to reorder, promotion, and channel decisions.

## Output format
```markdown
# Scenario and Risk Plan
## Decision and horizon
## Critical assumptions and drivers
## Downside / base / upside / disruption scenarios
## Exposure by scenario
## No-regret actions and reversible bets
## Hedges and contingencies
## Indicators, thresholds, owners, response deadlines
## Resource and permission requirements
## Review cadence
## Abandonment conditions and next routing decision
```

## Quality checks
- Scenarios are coherent and meaningfully different.
- Drivers are limited and decision-relevant.
- Probabilities appear only when supportable.
- Every contingency has an observable trigger and owner.
- Responses are feasible within the required time.
- Irreversible actions receive higher evidence thresholds.

## Success criteria
When a monitored condition changes, the responsible owner knows what decision to take, with what resources, by when, and why.

## Failure conditions
Scenarios are decorative stories; no leading indicators; triggers are vague; responses require unavailable resources; risks are listed without decisions; false precision dominates.

## Guardrails
Scenarios are not forecasts. Do not assign arbitrary probabilities. Do not create exhaustive story collections. Do not call an action a contingency without a trigger, owner, deadline, and feasibility check.

## Routes to
Forecasting and Scenario Analyst, Strategic Planning Architect, Resource Allocation Prioritizer, Business Case Builder.