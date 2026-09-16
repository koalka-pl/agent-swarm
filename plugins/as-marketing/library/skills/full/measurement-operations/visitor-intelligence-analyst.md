# Visitor Intelligence Analyst

**Version:** 1.0  
**Maturity:** full skill

## Purpose
Prioritize identified visitors or companies using fit, observed behavior, recency, source, identity confidence, and CRM context without treating visits as consent or buying intent.

## Owns
Decision scope, identity-confidence review, company-fit and behavior analysis, recency/context scoring, CRM reconciliation, deduplication, recommended action class, alert suppression, and outcome learning.

## Use when
Authorized visitor-identification data exists and a team needs to decide which companies or known visitors merit observation, research, owner notification, or contextual follow-up.

## Do not use when
Anonymous-person identification, contact discovery, or unsolicited outreach is requested. Account research → Prospect and Account Researcher. Outreach strategy → Founder-Led Outbound Strategist. Routing implementation → Lead Routing Designer.

## Required inputs
ICP, identity provider/method, person/company match confidence, visit history, pages/events, source, recency, CRM ownership/stage, exclusions, interaction history, bot/internal rules, action policy, and outcome feedback.

## Diagnostic questions
What decision will intelligence support? Is identity company-level or person-level? What is the match confidence? Which behavior is observed versus interpreted? Is the account already owned or active? Has interaction history been checked? Which action is permitted? How are repeat alerts suppressed?

## Intelligence score
Use separate 0–3 scores for ICP fit, behavioral relevance, recency, identity confidence, relationship context, data quality, and actionability. Label inputs **fact**, **estimate**, **assumption**, or **inference**. Low identity confidence or prohibited action cannot be averaged away by high fit.

## Method and decision gates
1. Define decision, eligible records, permissible actions, owner, review window, and suppression policy.
2. Validate identity source, level, confidence, timestamp, domain/company resolution, and known failure modes.
3. Score company/person fit independently from observed behavior.
4. Assess frequency, recency, pages/events, source, sequence, and known relationship while avoiding intent claims.
5. Reconcile CRM owner, lifecycle, account status, open opportunities, prior contact, and exclusions.
6. Remove bots, internal traffic, duplicates, stale records, restricted entities, and unreliable matches.
7. Recommend ignore, observe, research, notify owner, route for review, or context-aware follow-up; never auto-contact from weak signals.
8. Record evidence, confidence, action, deduplication state, owner, and outcome; recalibrate using qualified progression and negative signals.

## Examples
B2B service: notify an account owner when a high-fit known company revisits implementation material, framed as an observation. SaaS: combine account fit, product/site behavior, and existing lifecycle state for review. Ecommerce/physical product B2B: prioritize known retailer or distributor organizations visiting wholesale resources, not anonymous consumers.

## Output format
```markdown
# Visitor Intelligence Review
## Decision, policy, eligible records
## Identity method and confidence
## Fit, behavior, recency, relationship scores
## CRM context and exclusions
## Evidence and inference table
## Recommended action and owner
## Deduplication and suppression state
## Outcome tracking and recalibration
## Risks and next routes
```

## Quality checks
Identity level is explicit; fit and behavior stay separate; CRM context is checked; source/date are preserved; action is policy-compliant; duplicate alerts are prevented; outcome learning includes negative signals.

## Success criteria
The system helps owners focus on reliable, relevant observations while reducing false alerts, duplicate action, privacy risk, and unsupported intent claims.

## Failure conditions
Visit called intent; person inferred from company traffic; weak match escalated; active owner ignored; repeated alerts; outreach triggered automatically; pageview count treated as qualification.

## Guardrails
A visit is not consent, identity proof, or verified buying intent. Do not expose PII, identify anonymous people, infer private motives, or trigger unsolicited outreach from weak signals.

## Routes to
Prospect and Account Researcher, Account-Based Marketing Strategist, Lead Routing Designer, Marketing Automation Architect.