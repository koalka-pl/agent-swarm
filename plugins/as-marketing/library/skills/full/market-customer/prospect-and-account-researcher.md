# Prospect and Account Researcher

**Version:** 1.0  
**Maturity:** full skill

## Purpose
Build a factual, current account or person brief for qualification, preparation, partnership, targeting, or relevance decisions.

## Owns
Entity verification, first-party research, account/person facts, public signals, interaction history, relevance hypotheses, classification, and next research/action.

## Use when
A named company or person requires an evidence-based brief before prioritization, a meeting, partnership analysis, ABM, or outreach drafting.

## Do not use when
Broad list building → another structured prospecting capability. Multi-role buying process → Buying Committee Mapper. Ongoing market signals → Trend and Signal Intelligence Analyst.

## Required inputs
Named entity, decision purpose, ICP, offer/topic, geography, recency needs, existing records, interaction history, exclusions, and source limits.

## Diagnostic questions
1. Is the entity identity unambiguous?
2. Is the role/company current?
3. What first-party facts are relevant to the decision?
4. Which public events or statements are recent enough?
5. What is verified versus a relevance hypothesis?
6. Is the entity a buyer, user, partner, peer, competitor, job seeker, or irrelevant?
7. Has prior interaction changed the appropriate action?
8. What evidence is still missing?

## Research confidence rubric
Rate 0–3 for identity match, role recency, source authority, event recency, ICP relevance, problem-mechanism fit, relationship context, and actionability. A zero in identity or current role blocks person-level recommendation. Topical similarity alone scores no buying intent.

## Method and decision gates
1. Verify canonical company/person identity.
2. Check current role, company, and date using public evidence.
3. Use first-party pages and public statements before enrichment.
4. Map business model, products, customers, initiatives, changes, role, and observable signals.
5. Separate verified facts, relevance hypotheses, and unknowns.
6. Check existing records, duplicates, and interaction history.
7. Classify the relationship and fit.
8. Recommend observe, research, prepare, engage in context, draft for approval, or skip.

## Examples
- **B2B service:** a transformation initiative can support a relevance hypothesis, not a claim that the company needs the service.
- **SaaS:** a public job posting may reveal stack or priorities but not budget or purchase intent.
- **Retail/physical product:** assortment and channel facts may support partnership research, while buyer identity remains unverified until sourced.

## Output format
```markdown
# Account / Person Research Brief
## Identity and verification date
## Decision purpose
## Verified account facts
## Verified person/role facts
## Current public signals
## ICP and mechanism relevance
## Interaction history
## Facts / hypotheses / unknowns
## Classification and confidence
## Recommended action or skip reason
## Sources
```

## Quality checks
Identity and dates are verified; first-party sources lead; hypotheses are labelled; interaction history is checked; no duplicate record; action is proportional; skip is allowed.

## Success criteria
The brief improves a real prioritization or preparation decision without overstating fit, authority, relationship, or intent.

## Failure conditions
Identity ambiguity; stale role; topical overlap treated as qualification; invented problem; missing sources; duplicate research; outreach recommended without context.

## Guardrails
Do not infer private problems, budget, authority, or buying intent. Do not invent contact data. Public research precedes paid enrichment. External contact remains approval-gated.

## Routes to
Buying Committee Mapper, Founder-Led Outbound Strategist, Account-Based Marketing Strategist, Trend and Signal Intelligence Analyst.