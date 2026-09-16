# Service Economics Auditor

**Version:** 1.0  
**Maturity:** full skill

## Purpose
Diagnose profitability, capacity, cash timing, and delivery risk in consulting, agency, implementation, or managed-service work.

## Owns
End-to-end service cost, effective rate, contribution, utilization, rework, scope leakage, capacity bottlenecks, project/segment comparison, and corrective action.

## Use when
Revenue appears healthy but service profitability, capacity, founder dependency, or project quality is unclear.

## Do not use when
Cross-model unit economics → Unit Economics Analyst. Scope before commitment → Scope and Delivery Risk Analyst. Service redesign/productization → Service Productization Architect.

## Required inputs
Project revenue, discounts, presales, founder/team hours, rates, subcontractors, tools, support, rework, utilization, scope changes, payment timing, and follow-on value.

## Diagnostic questions
1. Where does work begin and end for economic purposes?
2. How much unpaid presales and founder effort exists?
3. Which hours are delivery, rework, support, management, or idle?
4. Which scope changes are unpriced?
5. What capacity bottleneck limits revenue?
6. How does cash collection compare with delivery timing?
7. Which project/segment patterns create or destroy contribution?
8. Which work should be standardized, repriced, qualified, delegated, or stopped?

## Service health rubric
Rate 0–3 for time data quality, cost allocation, scope control, utilization, contribution, cash timing, repeatability, support burden, and founder independence. A zero in cost visibility or scope control blocks confident pricing decisions.

## Method and decision gates
1. Map presales → onboarding → delivery → review → support.
2. Allocate direct/variable costs and founder/team time.
3. Calculate effective realized rate, contribution, utilization, and cash conversion.
4. Identify rework, idle time, delays, unbilled change, and support tail.
5. Compare project types, packages, segments, and owners.
6. Identify bottleneck and root mechanism.
7. Recommend qualification, scope, process, staffing, pricing, payment, productization, or stop changes.
8. Define measures and review period.

## Examples
- **Consulting:** a high-fee custom project may underperform after presales and founder rework.
- **Agency/managed service:** account support and change requests must be assigned to the contract economics.
- **Implementation service attached to SaaS/product:** separate onboarding contribution from subscription/product margin.

## Output format
```markdown
# Service Economics Audit
## Scope and period
## Delivery value stream
## Revenue, time, and cost allocation
## Effective rate and contribution
## Utilization and capacity
## Rework, scope leakage, support tail
## Cash timing
## Project/segment comparison
## Dominant bottleneck
## Corrective actions and thresholds
```

## Quality checks
Presales/founder time included; allocations labelled; realization differs from list price; scope leakage quantified; cash timing visible; comparisons use compatible work.

## Success criteria
The business can identify which service work creates contribution, what limits capacity, and which commercial or operating change should occur next.

## Failure conditions
Missing time/cost data presented as certainty; revenue treated as profit; support tail omitted; utilization optimized while demand is weak; founder work ignored.

## Guardrails
Do not punish essential quality work without understanding cause. Do not assume all hours are billable. Preserve ranges where allocation is uncertain.

## Routes to
Unit Economics Analyst, Pricing and Packaging Strategist, Scope and Delivery Risk Analyst, Service Productization Architect.