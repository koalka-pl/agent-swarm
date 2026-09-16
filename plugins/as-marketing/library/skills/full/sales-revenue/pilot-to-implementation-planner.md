# Pilot-to-Implementation Planner

**Version:** 1.0  
**Maturity:** full skill

## Purpose
Convert pilot evidence into an informed go, change, extend, or stop decision and define what responsible production requires.

## Owns
Pilot criteria comparison, evidence classification, limitation register, production-readiness assessment, decision options, phased production scope, operating requirements, risk, stakeholder decision case, and proposal inputs.

## Use when
A pilot, proof of concept, trial implementation, or limited deployment has produced evidence that must inform a production decision.

## Do not use when
Pilot design before launch → Paid Pilot Designer. General scope risk → Scope and Delivery Risk Analyst. Proposal drafting → Proposal and Business Case Writer. A working demo alone is not production readiness.

## Required inputs
Original pilot scope, baseline, success and acceptance criteria, results, data quality, limitations, user feedback, technical architecture, security/compliance review, operating model, ownership, support, adoption, economics, and stakeholder process.

## Diagnostic questions
Which criteria were agreed before results? What was demonstrated, observed, estimated, or not tested? Were conditions representative? What failed? Which production gaps exist in data, integration, reliability, security, operations, support, adoption, governance, and economics? Who owns each gap? What decision is possible now?

## Production readiness score
Rate 1–5 for evidence quality, business value, technical feasibility, representative conditions, data/integration, security/compliance readiness, reliability/performance, operational ownership, support, adoption, economics, and stakeholder alignment. Label evidence **demonstrated fact**, **observation**, **estimate**, **assumption**, or **unknown**. Any critical production gap can block go regardless of average.

## Method and decision gates
1. Freeze and restate original scope, baseline, criteria, exclusions, and test conditions.
2. Compare each result with pre-agreed success and acceptance criteria; do not rewrite thresholds after seeing data.
3. Separate demonstrated outcomes, feasibility evidence, observations, estimates, failures, limitations, and unknowns.
4. Assess representativeness, sample, duration, edge cases, external support, and data quality.
5. Audit production gaps across data, integrations, performance, reliability, security, compliance, governance, UX, operations, support, adoption, ownership, and economics.
6. Define go, change, extend, pause, or stop options with risk, cost, evidence, and decision implications.
7. For viable paths, create phased production scope, dependencies, owners, acceptance, rollback, support, operating model, and commercial inputs.
8. Build a stakeholder decision case and prioritized next-step agenda, including evidence still required.

## Examples
B2B service: convert a limited diagnostic or implementation pilot into a phased program only after outcome and delivery evidence. SaaS: move a sandbox or departmental trial toward production after security, integration, reliability, adoption, and support gaps are closed. Physical product/ecommerce B2B: scale a retailer or market pilot after quality, fulfillment, returns, demand, margin, and operational evidence are representative.

## Output format
```markdown
# Pilot-to-Implementation Decision
## Original scope, baseline, criteria
## Results by criterion
## Demonstrated / observed / estimated / unknown
## Limitations, failures, representativeness
## Production-readiness score
## Critical gaps, owners, evidence needed
## Go / change / extend / pause / stop options
## Recommended phased production path
## Risks, acceptance, rollback, operating model
## Stakeholder decision and proposal inputs
```

## Quality checks
Original criteria remain fixed; negative evidence is visible; demo and production are distinct; critical gaps cannot average away; owners and dependencies are explicit; scale claims match test conditions.

## Success criteria
Stakeholders can make an evidence-based production decision and, if proceeding, understand the phased scope, risks, ownership, acceptance, support, and commercial requirements.

## Failure conditions
Criteria rewritten post hoc; demo treated as production; unrepresentative test generalized; failures suppressed; security/operations/support ignored; recommendation exceeds evidence; no stop option.

## Guardrails
Do not fabricate results, suppress negative evidence, imply scale from a narrow test, or promise compliance/readiness without review. External commitments require approval.

## Routes to
Customer Success Strategist, Scope and Delivery Risk Analyst, Proposal and Business Case Writer, Pricing and Packaging Strategist.