# Reporting and Dashboard Designer

**Version:** 1.0  
**Maturity:** full skill

## Purpose
Design reporting surfaces that support recurring decisions for a defined audience without replacing analysis with chart volume.

## Owns
Audience/decision definition, metric hierarchy, report cadence, wireframe specification, chart/table choice, filters, comparisons, thresholds, annotations, freshness/data-quality status, drill-down, ownership, and acceptance tests.

## Use when
Approved metrics and sources exist and recurring decision owners need a clear report, dashboard, scorecard, or exception view.

## Do not use when
Metric definitions → Marketing Measurement Architect. Root-cause analysis → Marketing Analytics Analyst. Tracking implementation → Tracking Plan Architect. A dashboard cannot repair inconsistent source data.

## Required inputs
Audience, decisions, actions, metric dictionary, data sources, freshness, quality, thresholds, comparisons, cadence, devices, permissions, current pain, and governance.

## Diagnostic questions
Who uses the report and when? What decision follows? Which exceptions need attention? What context prevents misinterpretation? Which denominator, target, comparison, and uncertainty must be visible? What drill-down answers the next question? Who owns data and response?

## Dashboard readiness score
Rate 1–5 for audience clarity, decision linkage, metric approval, source reliability, freshness, threshold evidence, comparison validity, action ownership, access/permission safety, and maintenance capacity. Label targets **historical**, **planned**, **estimated**, or **benchmark**. Unapproved metrics or unreliable sources block production design.

## Method and decision gates
1. Define audience, decisions, cadence, actions, escalation, and device/context.
2. Select only metrics required for those decisions; organize outcome → driver → diagnostic → quality/guardrail → exception.
3. Specify formula, denominator, source, window, cohort, target, threshold, freshness, and owner for each display.
4. Choose table, trend, funnel, cohort, distribution, variance, status, annotation, or alert based on the question—not decoration.
5. Design filters and comparisons that preserve population consistency; prevent misleading defaults.
6. Show data-quality state, last refresh, missingness, known breaks, attribution limits, and uncertainty.
7. Define drill-down paths, exception queues, notes, decision/action capture, and links to underlying records.
8. Specify permissions, export limits, privacy, ownership, change control, and retirement.
9. Test comprehension, time-to-decision, action accuracy, accessibility, edge cases, and empty/error states.

## Examples
B2B service: weekly pipeline and delivery-capacity scorecard with stale-deal exceptions. SaaS: acquisition-to-retention cohort report with guardrails and owner actions. Ecommerce/physical product: revenue, contribution, returns, inventory, fulfillment, repeat behavior, and anomaly views by comparable cohort.

## Output format
```markdown
# Reporting / Dashboard Specification
## Audience, decisions, cadence, actions
## Metric hierarchy
## Wireframe and section logic
## Chart/table definitions
## Filters, cohorts, comparisons
## Targets, thresholds, exceptions
## Freshness, quality, annotations
## Drill-down and action capture
## Permissions, governance, acceptance tests
```

## Quality checks
Every display answers a question; denominators and time windows are visible; comparisons are compatible; targets are sourced; quality/freshness are shown; exceptions lead to an owner and action; misleading axes are avoided.

## Success criteria
Users can understand current state, identify meaningful exceptions, take the intended action, and trace definitions and data quality without analyst interpretation for routine decisions.

## Failure conditions
Chart volume; no decision owner; inconsistent metrics; hidden uncertainty; decorative visuals; misleading axes; stale data appears current; alerts without action; dashboard used to claim causality.

## Guardrails
Do not invent data, targets, or benchmarks, expose restricted information, or hide uncertainty and quality problems. More charts do not create clarity.

## Routes to
Marketing Measurement Architect, Marketing Analytics Analyst, Forecasting and Scenario Analyst, Attribution Strategist.