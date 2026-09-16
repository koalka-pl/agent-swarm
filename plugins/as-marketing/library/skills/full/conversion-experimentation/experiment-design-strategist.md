# Experiment Design Strategist

**Version:** 1.0  
**Maturity:** full skill

## Purpose
Design a controlled experiment that can support a predefined business decision with acceptable statistical, operational, customer, and ethical risk.

## Owns
Decision statement, causal hypothesis, population, experimental unit, assignment, control and variants, primary metric, guardrails, minimum useful effect, sample and duration assumptions, QA, stopping rules, analysis plan, and fallback method.

## Use when
A meaningful decision depends on whether a specific change causes an outcome and sufficient stable exposure, instrumentation, and implementation control may exist.

## Do not use when
A completed test needs interpretation → A/B Test Analyst. The page problem is not diagnosed → Marketing Page CRO Auditor. Traffic cannot support useful inference → qualitative validation, staged rollout, or observational learning. Implementation and tracking setup belong elsewhere.

## Required inputs
Observed problem, evidence, proposed change, causal mechanism, business decision, baseline rate/distribution, eligible population, variance assumptions, business value, implementation method, instrumentation quality, risks, seasonality, and prior experiments.

## Diagnostic questions
What exact decision will the result change? Why might the variant cause the outcome? What is randomized? Can exposure remain stable? What effect is worth acting on? Which harm metrics matter? How much sample and time are available? What contamination or novelty risks exist? What happens if evidence remains inconclusive?

## Experiment readiness score
Rate 1–5 for decision importance, diagnosis quality, mechanism clarity, manipulability, sample feasibility, stable assignment, metric validity, instrumentation, guardrail coverage, implementation parity, and ethical acceptability. Label inputs **fact**, **estimate**, **assumption**, or **inference**. Any score below 3 for assignment, instrumentation, or customer safety blocks launch.

## Method and decision gates
1. State observation, uncertainty, business decision, and alternative actions.
2. Write hypothesis: because [evidence], changing [variable] for [population] should change [primary outcome] through [mechanism].
3. Define population, exclusions, experimental unit, assignment, persistence, and contamination risks.
4. Specify control and variants; isolate an interpretable change unless factorial/multivariate design is explicitly justified.
5. Choose one primary metric, precise denominator/window, diagnostics, and harm guardrails.
6. Define minimum useful effect before sizing; separate practical from statistical significance.
7. Estimate sample and duration using declared model, variance, allocation, traffic, seasonality, and attrition assumptions.
8. Freeze QA, exposure, monitoring, stopping, exclusion, segment, and analysis rules before launch.
9. Decide test feasibility; otherwise specify qualitative research, sequential rollout, interrupted time series, or observational learning with weaker causal claims.

## Examples
B2B service: test a high-volume qualification step only if enough comparable visitors exist; otherwise use interviews and staged rollout. SaaS: randomize onboarding guidance with activation and support guardrails. Ecommerce/physical product: test product-page explanation or checkout step with revenue, returns, margin, and error guardrails.

## Output format
```markdown
# Experiment Protocol
## Decision, observation, evidence
## Hypothesis and causal mechanism
## Population, unit, assignment, exclusions
## Control, variants, allocation
## Primary metric, diagnostics, guardrails
## Minimum useful effect
## Sample and duration assumptions
## Instrumentation and QA
## Stopping, segments, analysis policy
## Ethics, risks, fallback method
```

## Quality checks
Decision precedes metric; hypothesis is causal and testable; unit and denominator are explicit; practical effect is predefined; sample is feasible; guardrails cover harm; protocol is frozen; fallback preserves weaker inference language.

## Success criteria
The protocol can be executed consistently and its result can support the declared decision with known uncertainty and acceptable downside risk.

## Failure conditions
Testing an undetectably small change; vague decision; unstable exposure; metric gaming; insufficient sample; peeking-based stopping; variant changes mid-test; unplanned segmentation; harmful dark-pattern experiment.

## Guardrails
Do not claim power without assumptions, treat ICE as truth, cherry-pick outcomes, or run unethical manipulation. Underpowered tests must be rejected or explicitly reframed as exploratory.

## Routes to
Tracking Plan Architect, A/B Test Analyst, Marketing Page CRO Auditor, Funnel Analytics Specialist.