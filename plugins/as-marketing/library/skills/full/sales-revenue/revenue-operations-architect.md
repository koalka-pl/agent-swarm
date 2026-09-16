# Revenue Operations Architect

**Version:** 1.0  
**Maturity:** full skill

## Purpose
Align marketing, sales, and customer success around shared lifecycle definitions, ownership, handoffs, data flow, automation requirements, and operating reviews.

## Owns
Cross-team lifecycle, shared definitions, handoff architecture, SLAs, recycle/rejection logic, system-of-record policy, data flow, automation decision requirements, governance, and revenue operating cadence.

## Use when
Growth is constrained by conflicting definitions, broken handoffs, fragmented systems, unowned work, or inconsistent customer/revenue state across teams.

## Do not use when
CRM data model → CRM Architecture Strategist. Opportunity stages → Pipeline Process Designer. Integration implementation → Integration Workflow Designer. Marketing-only operations → Marketing Operations owner. Define process before automation.

## Required inputs
GTM motion, customer lifecycle, pipeline, CRM and systems, team ownership, SLAs, scoring, routing, onboarding, expansion, reporting, current failures, permissions, and data-quality evidence.

## Diagnostic questions
Which customer/revenue state must teams share? Where does ownership change? What evidence triggers a handoff? What gets rejected or recycled? Which system is authoritative? What fails silently? Which decisions are stable enough to automate? Which review resolves cross-team conflict?

## RevOps readiness score
Rate 1–5 for lifecycle clarity, shared definitions, ownership, handoff observability, SLA feasibility, data quality, fallback safety, system-of-record integrity, permission clarity, and decision usefulness. Label inputs **fact**, **estimate**, **assumption**, or **inference**. Conflicting definitions block automation.

## Method and decision gates
1. Define customer and revenue outcomes plus one authoritative state system.
2. Map lifecycle stages with entry, evidence, owner, action, exit, and allowed transitions.
3. Map handoffs across acquisition, sales, delivery, success, renewal, and expansion; document failure modes.
4. Define SLAs, acceptance/rejection, recycle, duplicate, escalation, and feedback reasons.
5. Align lead score, routing, opportunity, onboarding, customer health, renewal, and expansion definitions.
6. Map sources, identities, integrations, permissions, latency, conflicts, and audit needs.
7. Automate only stable decisions; require fallback owner, visible failure, retry/escalation, and audit log.
8. Define operating reviews, decision rights, change control, data-quality checks, and metrics.
9. Sequence implementation by dependency and risk rather than tool convenience.

## Examples
B2B service: align inquiry, qualification, opportunity, delivery kickoff, value review, and renewal ownership. SaaS: connect marketing lifecycle, sales opportunity, subscription, onboarding, product adoption, health, and renewal. Ecommerce/physical product B2B: align lead, account, quote/order, fulfillment, support, retailer success, and reorder states.

## Output format
```markdown
# Revenue Operations Architecture
## Outcomes and system of record
## Lifecycle dictionary
## Cross-team handoff map
## SLAs, rejection, recycle, escalation
## Scoring/routing/pipeline/success alignment
## Data, identity, integration requirements
## Automation gates, fallback, audit
## Governance and operating reviews
## Implementation sequence, metrics, risks
```

## Quality checks
Definitions are shared; every transition has evidence and owner; failures are visible; automation has fallback; one source of truth governs state; metrics support decisions; governance can change the system safely.

## Success criteria
Teams use consistent customer and revenue state, handoffs happen predictably, failures surface quickly, and operating decisions rely on trustworthy shared evidence.

## Failure conditions
Automation over conflict; parallel truth; silent stage changes; unowned alerts; SLA without capacity; tool migration presented as operating design; fake forecast precision.

## Guardrails
Do not automate unstable or harmful decisions, expose unnecessary personal data, or infer intent from weak signals. Architecture does not grant system permissions or implement integrations.

## Routes to
CRM Architecture Strategist, Lead Scoring Designer, Lead Routing Designer, Pipeline Process Designer, Integration Workflow Designer.