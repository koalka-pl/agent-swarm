# Attribution Strategist

**Version:** 1.0  
**Maturity:** full skill

## Purpose
Build a practical, explicitly limited view of how observable channels and interactions contribute to acquisition and revenue decisions.

## Owns
Attribution decision, journey/data coverage map, descriptive model set, precedence, windows, direct/unknown handling, source reconciliation, reporting interpretation, governance, and limitations.

## Use when
A team needs a consistent way to describe source and influence across a multi-touch, cross-system journey for planning and learning.

## Do not use when
Causal incrementality is claimed without experimental/quasi-experimental evidence. UTM taxonomy → UTM Governance Designer. ROI calculation → Marketing ROI Analyst. Paid-platform attribution and offline conversion loops are excluded.

## Required inputs
Customer journey, sales cycle, channels, campaign taxonomy, referral/partner data, direct/branded behavior, CRM, first/last touch, opportunity source, self-report, identity coverage, offline touchpoints, and decision needs.

## Diagnostic questions
Which decision must attribution inform? Which journey stages are observable? Where do identities break? What does direct mean operationally? Which touch owns acquisition, opportunity, or revenue state? How do self-report and behavioral records disagree? What remains unknowable?

## Attribution readiness score
Rate 1–5 for decision clarity, source capture, taxonomy quality, identity continuity, CRM linkage, offline coverage, self-report quality, revenue-state clarity, deduplication, and governance. Label outputs **observed source**, **assigned credit**, **self-reported influence**, **estimate**, or **unknown**. Never call assigned credit causal truth.

## Method and decision gates
1. Define decision, entity, outcome, time horizon, and acceptable uncertainty.
2. Map observable and unobservable journey stages, identities, handoffs, and source loss.
3. Audit source, campaign, referral, cross-domain/device, offline, CRM, and revenue coverage.
4. Define complementary descriptive views: first touch, last non-direct, lead/opportunity source, self-report, assisted interactions, partner/referral, and qualitative evidence.
5. Specify precedence, lookback, direct handling, unknown categories, overwrite rules, and revenue deduplication.
6. Reconcile disagreements; preserve each model’s question rather than forcing one universal number.
7. Define reporting for planning, source quality, journey learning, and ROI with limitations visible.
8. Validate classifications, drift, unknown share, and known journeys; govern changes prospectively.

## Examples
B2B service: combine first source, founder/outbound context, self-report, partner influence, and opportunity source. SaaS: report acquisition and assisted product/content touches without claiming full causality. Ecommerce/physical product: reconcile referral, email, organic, partner, direct, and repeat-customer journeys while separating orders from realized margin.

## Output format
```markdown
# Attribution Strategy
## Decision, entity, outcome, horizon
## Journey and observability map
## Identity and source coverage
## Descriptive attribution views
## Precedence, windows, direct/unknown rules
## Reconciliation and deduplication
## Reporting interpretations
## Limitations, validation, governance
## Implementation needs and next routes
```

## Quality checks
Models answer distinct questions; unknown remains visible; revenue is deduplicated; pipeline and realized revenue are separate; self-report is not forced to match click data; limitations accompany every view.

## Success criteria
Teams use consistent descriptive attribution to compare source quality and journey influence without mistaking model-assigned credit for complete causal truth.

## Failure conditions
One model declared truth; unknown erased; direct reassigned arbitrarily; pipeline mixed with revenue; touch counts double revenue; identity gaps hidden; paid-platform claims imported into starter.

## Guardrails
No attribution model reveals complete causality. Do not fabricate touchpoints, erase unknowns, double-count outcomes, or compare incompatible definitions.

## Routes to
UTM Governance Designer, Tracking Plan Architect, Marketing ROI Analyst, Marketing Analytics Analyst.