# Marketing Measurement Architect

**Version:** 1.0  
**Maturity:** full skill

## Purpose
Define a compact, business-linked metric system with stable definitions, owners, thresholds, review cadence, and action rules.

## Owns
Decision map, metric hierarchy, definitions, formulas, denominators, scope, windows, source/owner map, data-quality requirements, thresholds, review routine, and metric retirement.

## Use when
A business needs to decide what to measure across marketing, customer, and revenue activity before creating tracking plans, analyses, or dashboards.

## Do not use when
Event/property specification → Tracking Plan Architect. Existing-data analysis → Marketing Analytics Analyst. Dashboard specification → Reporting and Dashboard Designer. Paid-platform measurement belongs to the paid-advertising owner.

## Required inputs
Business goals, model, strategy, customer journey, funnel/lifecycle, recurring decisions, current metrics, systems, data quality, owners, review cadence, and constraints.

## Diagnostic questions
Which recurring decisions need evidence? Who owns them? What outcome matters? Which leading or diagnostic measures explain it? What is the denominator and time window? Which source is authoritative? What threshold changes action? Which metrics have no decision use?

## Metric quality score
Rate each metric 1–5 for decision relevance, definition clarity, controllability, reliability, timeliness, comparability, actionability, gaming risk, and collection burden. Label targets and thresholds **fact**, **historical baseline**, **estimate**, **assumption**, or **external benchmark**. Metrics below 3 on relevance or reliability should not become KPIs.

## Method and decision gates
1. List recurring decisions, owners, cadence, alternatives, and consequences.
2. Map the customer and revenue system from attention through value realization.
3. Choose a primary outcome or north-star only if it reflects durable customer and business value.
4. Define outcome, leading, diagnostic, quality, efficiency, and guardrail metrics.
5. Specify formula, numerator, denominator, entity, scope, time/event window, cohort, exclusions, source, owner, freshness, and revision policy.
6. Establish targets or thresholds from strategy and evidence; expose assumptions and confidence.
7. Design review cadence, comparison logic, action rules, and escalation.
8. Identify instrumentation, identity, privacy, and integration gaps.
9. Remove vanity, duplicate, gameable, or ownerless metrics.

## Examples
B2B service: qualified opportunities, cycle, win/loss, delivery capacity, realized value, and contribution. SaaS: acquisition, activation, retention, expansion, support, and unit economics by cohort. Ecommerce/physical product: qualified traffic, conversion, margin, returns, repeat purchase, inventory/fulfillment, and customer quality.

## Output format
```markdown
# Marketing Measurement Framework
## Business decisions and owners
## Customer/revenue system map
## Metric hierarchy
## Metric dictionary and formulas
## Sources, freshness, quality, ownership
## Targets, thresholds, assumptions
## Review cadence and action rules
## Tracking/reporting dependencies
## Metrics to remove and next routes
```

## Quality checks
Every metric supports a decision; denominators and windows are explicit; one source is authoritative; quality and guardrails balance volume; targets are sourced; review creates action; unused metrics retire.

## Success criteria
Teams use a small shared metric system to make recurring decisions consistently and can explain definition, source, limitation, owner, and action for every KPI.

## Failure conditions
Dashboard-first design; vanity metrics; shifting definitions; incompatible populations; ownerless KPIs; target without evidence; north-star ignores customer value or harms quality.

## Guardrails
Do not invent baselines, benchmarks, attribution, or precision. Do not collect metrics without decision use or expose unnecessary personal data.

## Routes to
Tracking Plan Architect, Funnel Analytics Specialist, Reporting and Dashboard Designer, Marketing Analytics Analyst.