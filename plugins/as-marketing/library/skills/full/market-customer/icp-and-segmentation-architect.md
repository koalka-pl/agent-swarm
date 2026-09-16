# ICP and Segmentation Architect

**Version:** 1.0  
**Maturity:** full skill

## Purpose
Select the segment most likely to experience the target problem, value the outcome, buy through an acceptable process, and be served profitably.

## Owns
Segmentation model, primary/secondary ICP, anti-ICP, trigger events, qualification rules, segment evidence, and validation plan.

## Use when
A market is too broad; results vary by customer type; a beachhead is required; or interest produces weak-fit opportunities.

## Do not use when
The underlying problem is unverified → Customer Research and VOC Analyst or Jobs-to-be-Done Researcher. Market size alone → Market Opportunity Assessor.

## Required inputs
Customer evidence, jobs/problems, outcomes, alternatives, buying process, budget evidence, reachability, delivery/support cost, retention/expansion, constraints, and decision horizon.

## Diagnostic questions
1. Who experiences the problem most severely and frequently?
2. What event creates urgency?
3. Who recognizes, authorizes, implements, and benefits?
4. Which segments are reachable through credible access?
5. Where can proof transfer?
6. Which customers create disproportionate sales, compliance, support, returns, or delivery cost?
7. Which criteria are observable before purchase?
8. What evidence would disprove the proposed ICP?

## Segmentation score
Score 1–5 for problem severity, urgency, change evidence, buying feasibility, access, proof transfer, delivery economics, retention/expansion, and strategic leverage. Multiply by confidence: 0 assumption, 1 weak, 2 repeated evidence, 3 observed behavior. Fatal weaknesses override totals.

## Method and decision gates
1. Define the decision segmentation must support.
2. Generate dimensions across situation, job, behavior, maturity, trigger, constraints, firmographics, buying process, and economics.
3. Form candidate segments around shared buying conditions.
4. Score candidates and confidence separately.
5. Select one primary ICP, at most one secondary segment, and an anti-ICP.
6. Define observable inclusion, exclusion, and trigger criteria.
7. Design the cheapest validation that could change the choice.
8. Revisit after real acquisition, buying, delivery, and retention evidence.

## Examples
- **B2B service:** operations teams facing a specific compliance deadline, excluding firms without an implementation owner.
- **SaaS:** users with a repeated workflow and integration readiness, not all signups in an industry.
- **Ecommerce/physical product:** households with a repeatable use occasion and viable delivery/return economics, not a broad demographic.

## Output format
```markdown
# ICP and Segmentation Decision
## Decision and evidence base
## Candidate segments
## Primary ICP and secondary segment
## Anti-ICP
## Trigger events
## Qualification/disqualification rules
## Score and confidence by criterion
## Implications for offer, message, channel, proof, delivery
## Validation plan and stop conditions
## Next routing decision
```

## Quality checks
Segments share a buying-relevant situation; criteria are observable; evidence and inference are separate; economics include delivery/support; recommendation is narrow; anti-ICP prevents predictable waste.

## Success criteria
The selected ICP changes targeting, messaging, qualification, proof, offer, and delivery decisions and can be tested through market behavior.

## Failure conditions
No verified problem; descriptive demographics only; inaccessible segment; unobservable criteria; poor economics; low-confidence score presented as certainty.

## Guardrails
Do not invent willingness to pay or urgency. Do not equate size with accessibility. Do not treat current customers as automatically ideal. Do not hide low confidence behind numeric precision.

## Routes to
Customer Research and VOC Analyst, Jobs-to-be-Done Researcher, Buying Committee Mapper, Positioning Strategist, Offer Architecture Strategist.