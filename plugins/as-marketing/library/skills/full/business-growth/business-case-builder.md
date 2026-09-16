# Business Case Builder

**Version:** 1.0  
**Maturity:** full skill

## Purpose
Build an evidence-based justification for an investment, project, pilot, operating change, or explicit decision not to invest.

## Owns
Decision framing, baseline, value levers, scenario economics, assumptions, stakeholder evidence needs, and proceed/test/defer/stop recommendations.

## Use when
- An investment requires executive, customer, partner, or internal approval.
- Benefits, costs, risks, and uncertainty must be compared.
- A pilot or project needs a decision agenda rather than promotional ROI.

## Do not use when
- A sales proposal is the primary deliverable → Proposal and Business Case Writer.
- A pilot must be designed → Paid Pilot Designer.
- The task is only a financial forecast → Forecasting and Scenario Analyst.

## Required inputs
Decision, baseline process, no-change option, alternatives, costs, value levers, stakeholders, implementation requirements, dependencies, risks, evidence, uncertainty, and horizon.

## Diagnostic questions
1. What exact decision and decision date must this case support?
2. What happens under no change?
3. Which costs are cash, time, capacity, risk, or opportunity cost?
4. Which value levers are measured, estimated, inferred, or unknown?
5. Who receives value and who bears cost or risk?
6. What implementation dependencies delay realization?
7. Which assumptions dominate the result?
8. What evidence would materially change the decision?
9. Is a staged test more rational than full commitment?
10. What downside is acceptable and reversible?

## Evidence and confidence rubric
Score 0–3 for baseline quality, cost completeness, value evidence, implementation realism, stakeholder alignment, sensitivity coverage, reversibility, and measurement feasibility.

0–7: insufficient case; 8–14: discovery/research; 15–19: bounded test case; 20–24: decision-ready. Never use the total to override an unsupported dominant value assumption.

## Method and decision gates
1. Define decision, owner, date, alternatives, and no-change baseline.
2. Quantify current costs and consequences without forcing false precision.
3. Map financial, operational, risk, learning, and strategic value levers.
4. Classify each input by source and confidence.
5. Model downside, base, upside, timing, and sensitivity.
6. Include implementation cost, adoption, delay, opportunity cost, and residual risk.
7. Map stakeholder objections and evidence requirements.
8. Recommend proceed, test, defer, or stop; specify next-decision evidence.

## Examples
- **B2B service:** compare a paid diagnostic and pilot with continued manual process; value includes cycle-time and risk reduction, not invented revenue.
- **SaaS:** model adoption and retained usage before claiming license ROI; show sensitivity to implementation delay.
- **Physical product:** include tooling, MOQ, inventory, returns, channel margin, and cash conversion—not only gross demand.

## Output format
```markdown
# Business Case
## Decision, owner, and date
## Baseline and no-change consequences
## Alternatives
## Cost model
## Value levers and evidence classes
## Downside / base / upside scenarios
## Sensitivity and dominant assumptions
## Implementation plan and time to value
## Stakeholder concerns
## Risks and residual uncertainty
## Proceed / test / defer / stop recommendation
## Next-decision agenda
```

## Quality checks
- No-change is explicit.
- All values show source, unit, period, and confidence.
- Cash, time, capacity, and opportunity costs are included.
- Timing and adoption affect realized value.
- Sensitivity identifies decision-dominant assumptions.
- Recommendation remains valid under a stated range.

## Success criteria
A decision maker can see what is known, what drives value, what can go wrong, and what evidence is required before additional commitment.

## Failure conditions
Undefined decision; missing baseline; benefits without owners; costs exclude implementation; ROI rests on one unsupported assumption; scenarios use arbitrary probabilities; no validation plan.

## Guardrails
Never fabricate ROI, savings, revenue, probabilities, benchmarks, or customer evidence. Do not hide opportunity cost, adoption effort, or downside. Use ranges where precision is unsupported.

## Routes to
Forecasting and Scenario Analyst, Scenario and Risk Planner, Paid Pilot Designer, Proposal and Business Case Writer, Marketing Measurement Architect.