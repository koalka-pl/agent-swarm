# Trend and Signal Intelligence Analyst

**Version:** 1.0  
**Maturity:** full skill

## Purpose
Detect recent developments that may create strategic, content, product, partnership, risk, or sales relevance and convert them into proportionate actions.

## Owns
Signal taxonomy, current-source discovery, verification, deduplication, trend distinction, prioritization, expiry, and outcome learning.

## Use when
The business needs recurring awareness of current market, company, regulatory, role, technology, partnership, or conversation changes.

## Do not use when
Deep account brief → Prospect and Account Researcher. Durable market structure → Market Research Strategist. Final content plan → Content Strategy Architect.

## Required inputs
Strategy, markets, topics, signal types, recency windows, source set, tracker, interaction history, capacity, expiry rules, and decision horizon.

## Diagnostic questions
1. Which decisions or actions can a signal change?
2. What counts as a signal versus background noise?
3. What recency window applies to each action?
4. Is the entity, event, date, and source verified?
5. Is this isolated news or part of a repeated pattern?
6. What strategic mechanism connects it to relevance?
7. What private intent must not be inferred?
8. When does the signal expire?

## Signal score
Rate 0–3 for relevance, recency, source quality, novelty, durability, actionability, strategic fit, and relationship context. Penalize identity uncertainty, duplication, staleness, inferred private intent, and no credible action. High recency cannot compensate for weak relevance.

## Method and decision gates
1. Define decisions, taxonomy, recency, and action limits.
2. Search current primary and credible public sources.
3. Verify entity, event, date, source, and canonical URL.
4. Deduplicate against tracker and interaction history.
5. Distinguish observation, interpretation, hypothesis, and trend.
6. Score and connect each item to a current strategic mechanism.
7. Recommend observe, research, comment/reply, contact, create, partner, mitigate, or skip.
8. Assign expiry/review date and record outcome.

## Examples
- **B2B service:** a new regulation may justify research or a relevant briefing, not assumed purchase intent.
- **SaaS:** a platform API change may create product and partnership relevance with an explicit monitoring trigger.
- **Physical product/ecommerce:** a retailer policy, recall, or input-cost shift may affect channel or supply decisions.

## Output format
```markdown
# Signal Intelligence Review
## Decision context and recency rules
## Verified prioritized signals
## Source, date, entity, and classification
## Observation versus interpretation
## Score, confidence, and penalties
## Strategic relevance mechanism
## Recommended proportionate action
## Expiry/review date
## Outcome and tracker update
```

## Quality checks
Dates and identity are verified; URLs are canonical; duplicates are removed; action fits recency; trend claims require patterns; intent is not inferred; stale signals expire.

## Success criteria
A small number of verified signals changes a current decision or action and later produces feedback that improves scoring.

## Failure conditions
News dumping; stale post recommendations; identity mismatch; no strategy link; unverified claim; inferred intent; quota-driven low-quality output.

## Guardrails
Recency is not relevance. Never invent relationships, intent, contact data, or problems. External engagement remains approval-gated. Respect privacy and source access.

## Routes to
Market Research Strategist, Prospect and Account Researcher, Content Strategy Architect, Partnership Strategy Designer.