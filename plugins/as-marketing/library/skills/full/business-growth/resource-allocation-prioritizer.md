# Resource Allocation Prioritizer

**Version:** 1.0  
**Maturity:** full skill

## Purpose
Allocate limited money, people, time, inventory, production capacity, and attention across competing operations, bets, and experiments.

## Owns
Portfolio prioritization, protected operations, minimum viable funding, opportunity cost, capacity-aware allocations, stop/defer decisions, and review triggers.

## Use when
- Several initiatives compete for constrained resources.
- Existing commitments hide true available capacity.
- Teams spread resources thinly instead of making choices.
- A primary bet and bounded experiments must be selected.

## Do not use when
- The strategic outcomes are not defined → Strategic Planning Architect.
- The problem is specifically marketing-channel allocation → Channel Portfolio Prioritizer.
- Uncertainty requires trigger-based scenarios → Scenario and Risk Planner.

## Required inputs
Objective, initiatives, mandatory work, capacity, full costs, expected impact, evidence confidence, dependencies, reversibility, timing, risks, opportunity cost, owners, and review horizon.

## Diagnostic questions
1. What outcome is allocation meant to change?
2. What work is mandatory, contractual, safety-critical, or required to keep operations running?
3. What capacity remains after current commitments?
4. What is the minimum viable funding or staffing for each initiative?
5. Which dependencies create all-or-nothing thresholds?
6. Which assumptions support expected impact?
7. How quickly can each initiative produce decision-quality learning?
8. What founder, management, inventory, or context-switching cost is hidden?
9. What gets stopped or deferred if this is funded?
10. What evidence triggers continuation, reallocation, or termination?

## Allocation scorecard
Rate 0–3 for strategic fit, expected impact, evidence confidence, urgency, dependency readiness, time-to-learning, reversibility, capacity fit, and downside exposure. Record full cost separately; do not hide it inside a score.

Interpretation: use the score to structure debate, not automate the decision. Any initiative below minimum viable resourcing should be deferred rather than partially funded. Mandatory work is classified before scoring.

## Method and decision gates
1. Define one allocation outcome and time horizon.
2. Separate mandatory operations, commitments, strategic bets, and experiments.
3. Remove work with no outcome or obligation link.
4. Calculate true capacity and full cost, including attention and switching.
5. Map prerequisites and minimum viable resource levels.
6. Score comparable initiatives and document uncertainty.
7. Select protected operations, one primary bet, and bounded experiments.
8. Assign fund/do/defer/stop decisions, owners, thresholds, and review dates.

## Examples
- **B2B service:** protect client delivery, fund one productized offer test, and stop three low-signal content channels.
- **SaaS:** fund activation and retention work before increasing acquisition capacity; preserve reliability operations.
- **Physical product/ecommerce:** allocate cash to proven inventory and one controlled new-SKU test rather than underfunding several launches.

## Output format
```markdown
# Resource Allocation Decision
## Outcome and horizon
## Available capacity and mandatory work
## Initiative portfolio
## Full cost and opportunity cost
## Dependencies and minimum viable resources
## Scorecard and evidence confidence
## Fund / do / defer / stop decisions
## Allocation by money, people, time, inventory, and attention
## Owners, metrics, thresholds, and review dates
## Explicit exclusions and next routing decision
```

## Quality checks
- Mandatory work is separated from optional work.
- Capacity is net of real commitments.
- Initiatives below minimum viable funding are not diluted.
- Full and opportunity costs are visible.
- Dependencies are not averaged away by scoring.
- Every funded item has a stop or review trigger.

## Success criteria
Resources concentrate on a feasible portfolio that protects essential operations, advances the chosen outcome, and produces evidence before the next major commitment.

## Failure conditions
No objective; hidden commitments; political equal-splitting; partial funding below viability; ignored dependencies; no owner; no review/stop trigger.

## Guardrails
Do not use scoring as false objectivity. Do not spread resources for political balance. Do not ignore founder attention, inventory, maintenance, working capital, or context switching. Do not fund an initiative that cannot reach a meaningful learning or delivery threshold.

## Routes to
Strategic Planning Architect, Scenario and Risk Planner, Channel Portfolio Prioritizer, Growth Strategy Architect, Marketing ROI Analyst.