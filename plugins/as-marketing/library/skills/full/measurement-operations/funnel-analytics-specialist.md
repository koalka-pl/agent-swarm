# Funnel Analytics Specialist

**Version:** 1.0  
**Maturity:** full skill

## Purpose
Identify meaningful conversion loss, delay, and segment differences across a precisely defined journey without mistaking missing data for abandonment or drop-off for cause.

## Owns
Funnel population, stages, sequence/window rules, identities, denominators, conversion and timing calculations, segment comparison, bottleneck prioritization, data-gap diagnosis, and hypotheses.

## Use when
A business needs to understand progression and time between defined stages in a marketing, sales, onboarding, purchase, or customer journey.

## Do not use when
Broad change analysis → Marketing Analytics Analyst. Stage/process design → Pipeline Process Designer. Page diagnosis → Marketing Page CRO Auditor. Tracking gaps → Tracking Plan Architect.

## Required inputs
Decision question, stage definitions, events or CRM states, identities, timestamps, denominator, entry rules, observation window, allowed order, repeat behavior, segments, value per outcome, and data-quality context.

## Diagnostic questions
Who enters the funnel? Are stages mandatory, ordered, or optional? What entity is followed? How long may progression take? Are stage populations compatible? What missing events exist? Which loss matters by absolute value and downstream quality? Could delay or capacity explain apparent drop-off?

## Funnel readiness score
Rate 1–5 for decision clarity, stage validity, identity continuity, timestamp quality, denominator consistency, observation-window sufficiency, event coverage, segment sample, downstream outcome linkage, and actionability. Label findings **observation**, **calculation**, **estimate**, **assumption**, or **hypothesis**.

## Method and decision gates
1. Define population, entry, stages, order, repeat rules, identity, window, conversion, and success outcome.
2. Validate compatible entities/populations, timestamps, duplicates, missingness, backfills, and state reversals.
3. Calculate counts, stage conversion, cumulative conversion, time-to-stage, time-in-stage, abandonment, and censoring.
4. Link stage outcomes to downstream quality/value where available.
5. Segment by source, audience, cohort, device, offer, geography, lifecycle, or owner only when it changes action.
6. Prioritize bottlenecks by absolute lost value, delay, quality, capacity, and fixability—not percentage alone.
7. Investigate instrumentation gaps, mix shifts, seasonality, eligibility, operational queues, and process constraints.
8. Form hypotheses, required evidence, and next owner; do not infer causality from drop-off.

## Examples
B2B service: inquiry → accepted lead → discovery → qualified opportunity → proposal → decision. SaaS: signup → activation → repeated use → paid conversion → retention. Ecommerce/physical product: product view → cart → checkout → order → fulfilled → retained/refund-adjusted value.

## Output format
```markdown
# Funnel Analysis
## Decision, population, identity, window
## Stage definitions and data checks
## Counts and denominators
## Stage/cumulative conversion
## Timing, delay, censoring
## Segment and downstream-quality differences
## Prioritized bottleneck
## Data gaps and alternative explanations
## Hypotheses, next actions, next routes
```

## Quality checks
Stages use compatible populations; denominators are explicit; late conversion is handled; missing tracking is not abandonment; absolute value and quality accompany rates; segments are decision-relevant.

## Success criteria
Decision owners can identify where meaningful progression is lost or delayed, how confident the evidence is, and what analysis, process, tracking, or experiment should follow.

## Failure conditions
Mixed denominators; optional stage treated as mandatory; short window; missing event called drop-off; largest percentage prioritized despite tiny volume; downstream harm ignored; correlation called cause.

## Guardrails
Do not invent events, identity continuity, or causality. Do not optimize a stage at the expense of qualification, margin, retention, or customer outcomes.

## Routes to
Marketing Analytics Analyst, Tracking Plan Architect, Marketing Page CRO Auditor, Pipeline Process Designer.