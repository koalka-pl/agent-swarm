# Outbound Sequence Designer

**Version:** 1.0  
**Maturity:** full skill

## Purpose
Design a contextual, respectful follow-up sequence that progresses from verified relevance toward conversation with explicit branching, approval, and stop rules.

## Owns
Sequence objective, touch logic, message briefs, new-value requirement, timing, channel sequence, personalization fields, branches, approvals, opt-out, CRM updates, and quality metrics.

## Use when
Approved targeting and research already establish a credible reason to contact a person or account and the next need is a bounded interaction sequence.

## Do not use when
Targeting, research, or relevance thesis → Founder-Led Outbound Strategist. High-volume automation, contact-data discovery, and unapproved sending are excluded. Discovery after reply → Discovery and Qualification Architect.

## Required inputs
Targeting rules, verified person/account research, dated trigger, relevance thesis, offer, credibility assets, prior interactions, approved channels, legal/norm constraints, approval policy, CRM, and capacity.

## Diagnostic questions
Why this person and now? Which facts are sourced? What useful contribution can each touch add? What is the smallest desired response? Which channel is contextually appropriate? Has interaction history been checked? What branches follow reply, referral, not-now, or opt-out? When does contact stop?

## Sequence quality score
Rate 0–3 for fit, trigger, role relevance, evidence, specificity, recipient value, proof, timing, channel fit, consent context, and reputation risk. Label each input **fact**, **estimate**, **assumption**, or **inference**. No sequence when identity, relevance, or source quality fails threshold.

## Method and decision gates
1. Define target, verified trigger, relevance, desired first response, maximum attempts, and stop horizon.
2. Select a useful insight, asset, question, introduction, clarification, or offer.
3. Design each touch to add genuinely new value: first contact → value follow-up → clarification → optional commercial transition → close-the-loop.
4. Match channel and timing to public context, relationship history, norms, and recipient preference.
5. Define required personalization fields, source/date, prohibited inference, and human review.
6. Add branches for positive reply, question, referral, objection, not now, wrong person, no reply, and opt-out.
7. Specify approvals, CRM status, evidence retention, next action, suppression, and duplicate handling.
8. Measure reply quality, qualified conversations, negative signals, complaints, opt-outs, progression, and learning—not reply rate alone.

## Examples
B2B expert: a short sourced message followed by one useful framework and a close-the-loop. SaaS: role-specific workflow relevance with a product resource, not repeated meeting asks. Ecommerce/physical product B2B: retailer or partner sequence using verified assortment, audience, or distribution context rather than consumer-level private inference.

## Output format
```markdown
# Outbound Sequence
## Objective, target, evidence, threshold
## Relevance thesis and recipient value
## Touch-by-touch message briefs
## Timing and channel logic
## Personalization fields and prohibited inference
## Reply / referral / not-now / opt-out branches
## Approval, suppression, CRM rules
## Metrics, negative signals, review
## Risks and next routes
```

## Quality checks
Every touch adds new value; context has source/date; history is checked; language is low-pressure; branches are explicit; follow-up is bounded; negative outcomes affect decisions.

## Success criteria
The sequence creates a manageable number of relevant, consent-respecting conversations or clear disqualifications without reputational harm or excessive manual burden.

## Failure conditions
Generic volume automation; invented familiarity or need; stale evidence; repeated identical asks; hidden opt-out; no suppression; reply rate treated as qualification; sending without approval.

## Guardrails
Do not scrape or infer private contact data, fabricate context, manipulate persistence, or bypass channel rules. Every external send remains approval-gated.

## Routes to
Founder-Led Outbound Strategist, Prospect and Account Researcher, CRM Architecture Strategist, Discovery and Qualification Architect.