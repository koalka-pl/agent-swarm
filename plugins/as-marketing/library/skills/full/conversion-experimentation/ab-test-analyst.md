# A/B Test Analyst

**Version:** 1.0  
**Maturity:** full skill

## Purpose
Analyze a completed controlled experiment, quantify uncertainty and practical effect, and recommend ship, reject, continue, iterate, or rerun.

## Owns
Protocol review, data-quality and exposure validation, primary analysis, uncertainty, guardrails, preregistered segments, practical and commercial interpretation, decision recommendation, and learning record.

## Use when
A controlled experiment has ended or reached a predefined analysis point and the protocol plus exposure and outcome data are available.

## Do not use when
The test has not been designed or launched → Experiment Design Strategist. Tracking repair → Tracking Plan Architect. Observational before/after comparison must not be presented as A/B causal evidence.

## Required inputs
Preregistered protocol, hypothesis, decision rule, control and variants, assignment and exposure logs, metric definitions, sample plan, dates, raw or aggregated outcomes, guardrails, exclusions, external events, implementation notes, and analysis method.

## Diagnostic questions
Was the protocol fixed before results? Was assignment valid? Did users receive persistent exposure? Is sample ratio plausible? Were metrics measured equally? Was planned sample/duration reached? Which deviations occurred? Does uncertainty include meaningful benefit and harm? Are segments planned or exploratory?

## Analysis integrity score
Rate 1–5 for protocol fidelity, assignment, exposure, sample-ratio balance, metric validity, missingness, contamination control, duration, guardrail quality, and analysis reproducibility. Label inputs and derived interpretations **fact**, **estimate**, **assumption**, or **inference**. Critical assignment, exposure, or measurement failure forces rerun/no causal conclusion.

## Method and decision gates
1. Confirm protocol, primary metric, minimum useful effect, stopping rule, and deviations before interpreting outcomes.
2. Validate assignment, sample-ratio mismatch, exposure persistence, event parity, missingness, bots/internal traffic, exclusions, and contamination.
3. Check planned sample and duration; report early stopping or underpower explicitly.
4. Estimate absolute and relative effects with confidence or credible intervals using the planned method and denominators.
5. Compare uncertainty with zero, minimum useful effect, downside tolerance, and business value—not significance alone.
6. Review guardrails and planned diagnostics; quantify operational and customer harm.
7. Analyze preregistered segments; label all other cuts exploratory and address multiplicity and low sample.
8. Assess novelty, seasonality, source mix, implementation incidents, and generalizability.
9. Recommend ship, reject, continue, iterate, rerun, or no-decision with conditions and reusable learning.

## Decision framework
- **Ship:** credible practically valuable effect; acceptable guardrails.
- **Reject:** credible harm or adequately powered absence of useful upside.
- **Continue:** protocol allows more data and uncertainty remains decision-relevant.
- **Iterate:** mechanism remains plausible but implementation/audience mismatch is evidenced.
- **Rerun:** protocol, assignment, exposure, or data quality prevents interpretation.
- **Inconclusive:** uncertainty still spans materially positive and negative outcomes.

## Examples
B2B service: low traffic usually yields inconclusive evidence and should not be called a win. SaaS: interpret activation lift alongside retention and support guardrails. Ecommerce/physical product: assess conversion with absolute revenue, margin, returns, cancellations, and customer-impact intervals.

## Output format
```markdown
# Experiment Analysis
## Protocol, decision rule, deviations
## Data-quality and exposure checks
## Sample, dates, denominators
## Primary absolute/relative effect and interval
## Minimum useful effect comparison
## Guardrails and diagnostics
## Planned vs exploratory segments
## Practical and commercial interpretation
## Decision and implementation conditions
## Limitations, generalizability, next hypothesis
```

## Quality checks
Primary metric remains primary; absolute effects and denominators are shown; statistical and practical importance remain separate; inconclusive is not neutral proof; segment claims reflect multiplicity; decision accounts for downside and implementation cost.

## Success criteria
The analysis provides a reproducible, uncertainty-aware decision consistent with the preregistered protocol and documents learning for future experiments.

## Failure conditions
P-value misinterpretation; early read called final; hidden deviations; cherry-picked metric or segment; relative lift without base rate; underpowered null called proof; generalization beyond tested population.

## Guardrails
Do not fabricate data, retroactively change the primary metric, hide harm, or claim causality from invalid assignment. State when no reliable decision is possible.

## Routes to
Experiment Design Strategist, Marketing Analytics Analyst, Tracking Plan Architect, Reporting and Dashboard Designer.