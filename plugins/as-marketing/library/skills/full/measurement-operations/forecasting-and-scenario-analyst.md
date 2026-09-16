# Forecasting and Scenario Analyst

**Version:** 1.0  
**Maturity:** full skill

## Purpose
Model future outcomes as conditional ranges under explicit assumptions and identify the drivers, constraints, and triggers that matter most.

## Owns
Decision horizon, driver model, baseline validation, scenario assumptions, sensitivity, constraints, leading indicators, trigger thresholds, back-testing, update cadence, and uncertainty communication.

## Use when
A decision requires understanding plausible future outcomes and which controllable or uncertain variables drive them.

## Do not use when
Historical explanation → Marketing Analytics Analyst. Program ROI → Marketing ROI Analyst. Strategic risk planning beyond quantitative model → Scenario and Risk Planner. Forecasts are not commitments.

## Required inputs
Decision and horizon, outcome definition, historical baseline, funnel/economic drivers, constraints, seasonality, planned changes, uncertainty ranges, structural breaks, capacity, and update cadence.

## Diagnostic questions
What decision will the forecast change? Which outcome and horizon matter? What driver chain produces it? Which data is stable? What structural break may invalidate history? What constraints cap upside? Which uncertainty dominates? What leading signal should trigger an update?

## Forecast readiness score
Rate 1–5 for decision clarity, baseline quality, driver completeness, parameter evidence, structural stability, seasonality handling, constraint visibility, scenario plausibility, back-test ability, and update ownership. Label every input **fact**, **estimate**, **assumption**, or **scenario choice**.

## Method and decision gates
1. Define decision, entity, outcome, horizon, granularity, and required confidence.
2. Build a transparent driver model from volumes, rates, timing, value, retention, capacity, and cost.
3. Validate baseline, definitions, missingness, cohort maturity, trend, seasonality, and structural breaks.
4. Assign evidence-based ranges or distributions to uncertain drivers.
5. Create downside, base, and upside scenarios with internally consistent assumptions—not arbitrary percentage shifts.
6. Run sensitivity and identify dominant drivers, bottlenecks, break-even values, and irreversible risks.
7. Add leading indicators, trigger thresholds, ownership, and response rules.
8. Back-test against prior periods or holdouts where possible; document error and bias.
9. Define update cadence, versioning, actual-vs-forecast review, and retirement conditions.

## Examples
B2B service: forecast qualified pipeline and delivery capacity from conversations, qualification, cycle, win rate, scope, and staffing. SaaS: model acquisition, activation, retention, expansion, price, and support capacity. Ecommerce/physical product: model demand, conversion, order value, margin, returns, inventory, lead time, repeat rate, and fulfillment constraints.

## Output format
```markdown
# Forecast and Scenario Model
## Decision, outcome, horizon
## Baseline and data quality
## Driver logic and formulas
## Assumption register and ranges
## Downside / base / upside scenarios
## Sensitivity and break-even points
## Constraints and structural risks
## Leading indicators and triggers
## Back-test, error, update process
```

## Quality checks
Model is transparent; ranges reflect evidence; scenarios are coherent; constraints cap unrealistic upside; sensitivity identifies real drivers; actuals update assumptions; point estimates do not hide uncertainty.

## Success criteria
Decision owners understand plausible ranges, dominant drivers, downside exposure, capacity limits, and conditions that should change the plan.

## Failure conditions
Single precise forecast; incompatible periods; historical break ignored; arbitrary scenarios; upside exceeds capacity; correlation embedded as causal driver; model never updated.

## Guardrails
Forecasts are conditional, not promises. Do not fabricate baselines, hide uncertainty, or present model output as guaranteed pipeline, revenue, or demand.

## Routes to
Marketing ROI Analyst, Marketing Analytics Analyst, Unit Economics Analyst, Reporting and Dashboard Designer.