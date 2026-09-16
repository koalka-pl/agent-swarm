# Unit Economics Analyst

**Version:** 1.0  
**Maturity:** full skill

## Purpose
Evaluate whether acquisition, revenue, retention, fulfillment, and delivery produce economically sustainable growth.

## Owns
Unit/cohort definition, contribution model, CAC/payback, retention/expansion economics, sensitivity, dominant constraint, and data gaps.

## Use when
A business must understand whether a customer, order, subscription, location, product, channel, or cohort creates sustainable contribution.

## Do not use when
Detailed service delivery economics → Service Economics Auditor. Marketing campaign ROI only → Marketing ROI Analyst. Pricing architecture → Pricing and Packaging Strategist.

## Required inputs
Revenue, price, discounts, gross margin, variable costs, acquisition/sales cost, payback, retention/churn, expansion, support, fulfillment, refunds/returns, volume, and period.

## Diagnostic questions
1. What is the economic unit and cohort?
2. What period and decision are being evaluated?
3. Which costs vary with acquisition, order, use, delivery, or support?
4. What labor or founder work is unpaid/unallocated?
5. How do retention, repeat purchase, returns, and expansion behave?
6. What cash timing or working capital matters?
7. Which assumption dominates the result?
8. Which data is measured versus estimated?

## Data confidence rubric
Rate 0–3 for revenue quality, cost completeness, CAC allocation, cohort retention, support/fulfillment cost, refunds/returns, cash timing, and sample stability. Low confidence requires ranges and a data plan, not a precise ratio.

## Method and decision gates
1. Define unit, cohort, period, and decision.
2. Separate revenue, gross margin, contribution, cash flow, and profit.
3. Allocate acquisition, sales, fulfillment/delivery, support, infrastructure, commissions, refunds, and variable labor.
4. Calculate contribution, CAC, payback, retention/repeat/expansion, and relevant lifetime economics.
5. Model downside/base/upside and sensitivity.
6. Compare segments, products, channels, or cohorts only with compatible definitions.
7. Identify dominant constraint and data gaps.
8. Recommend pricing, scope, acquisition, retention, delivery, or stop action.

## Examples
- **B2B service:** include presales, delivery, rework, support, and founder oversight by project type.
- **SaaS:** use gross-margin contribution and cohort retention; do not treat booked ARR as realized lifetime value.
- **Ecommerce/physical product:** include landed COGS, fulfillment, payment fees, returns, discounts, support, and repeat purchase.

## Output format
```markdown
# Unit Economics Analysis
## Decision, unit, cohort, period
## Formula definitions
## Revenue and cost model
## Contribution and cash timing
## CAC and payback
## Retention/repeat/expansion
## Downside/base/upside scenarios
## Sensitivity and dominant assumptions
## Segment/product/channel comparison
## Constraint, recommendation, data plan
```

## Quality checks
Unit and denominator explicit; formulas shown; full variable costs included; cohorts comparable; cash differs from profit; uncertainty visible; recommendation follows dominant constraint.

## Success criteria
The model supports a specific operating decision and clearly shows which assumptions or behaviors determine sustainability.

## Failure conditions
Revenue confused with profit; blended incompatible cohorts; missing labor/returns/support; CAC excludes sales cost; unsupported LTV; precision exceeds data.

## Guardrails
Do not invent benchmarks or inputs. Include founder/unpaid labor where relevant. Label allocations and estimates. Do not use lifetime value beyond credible retention evidence.

## Routes to
Pricing and Packaging Strategist, Service Economics Auditor, Marketing ROI Analyst, Business Model Strategist.