# Campaign Message-Match Analyst

**Version:** 1.0  
**Maturity:** full skill

## Purpose
Determine whether a source message and destination continue the same audience, situation, promise, terminology, evidence, offer, and action coherently.

## Owns
Direct source-to-destination comparison, continuity diagnosis, mismatch severity, likely consequence, strategic correction side, and measurement requirements.

## Use when
Traffic arrives from an email, post, partner placement, search result, outreach message, event asset, referral, or campaign and destination performance may depend on expectation continuity.

## Do not use when
Destination-only CRO → Marketing Page CRO Auditor. New landing argument → Landing Page Strategist. Paid-campaign targeting, bidding, creative optimization, or media decisions are excluded.

## Required inputs
Exact captured source message or creative, destination content, target audience, campaign objective, offer, desired action, variants, source-specific performance, timing, device context, and tracking quality.

## Diagnostic questions
Who does the source appear to address? What situation, promise, proof, offer, and action does it imply? What does the destination show first? Which differences are useful elaboration versus broken expectation? Is the mismatch in source, destination, targeting, or offer? Are sources being wrongly aggregated?

## Message-match score
Rate 1–5 for audience, situation/intent, promise, terminology, specificity, offer identity, proof, risk/terms, CTA, visual/verbal cues, and next-step expectation. Label each comparison **observed fact**, **estimate**, **assumption**, or **inference**. Audience, promise, or offer below 3 is critical unless intentionally segmented.

## Method and decision gates
1. Inspect and preserve the exact source, variant, date, placement, and visible context.
2. Record source audience signal, trigger, awareness, promise, mechanism, terminology, proof, offer, and expected action.
3. Record destination first-screen signal and subsequent promise, mechanism, proof, terms, CTA, and next-step expectation.
4. Compare continuity dimension by dimension; distinguish mismatch from necessary elaboration.
5. Classify critical, material, minor, or intentional divergence and state confidence.
6. Identify whether source, destination, targeting/segmentation, or offer must change; do not default to destination edits.
7. Recommend exact strategic corrections while preserving product and offer truth.
8. Define source-specific outcomes, diagnostics, guardrails, and a feasible validation method.

## Examples
B2B service: compare a founder outreach promise with a consultation page. SaaS: align an integration email or organic post with a workflow landing page. Ecommerce/physical product: verify that an influencer, referral, email, or search snippet matches product, variant, availability, price/terms, and delivery expectations.

## Output format
```markdown
# Message-Match Analysis
## Source capture and context
## Destination capture and context
## Audience / promise / offer / action matrix
## Mismatches, severity, confidence
## Healthy elaboration vs broken expectation
## Source, destination, targeting, or offer correction
## Variant-specific notes
## Source-specific metrics and validation
## Risks and next routes
```

## Quality checks
The exact source is inspected; variants remain separate; mismatch is not confused with elaboration; terms and next-step expectations are included; recommended correction names which side changes; product truth is preserved.

## Success criteria
Visitors encounter a destination consistent with the expectation that brought them there, reducing avoidable confusion and enabling source-specific evaluation.

## Failure conditions
Channel name substituted for source evidence; variants averaged; destination changed without reading source; intentional segmentation called mismatch; paid-media optimization advice introduced; uplift promised without test.

## Guardrails
Do not infer campaign intent, audience, or promise from metadata alone. Do not fabricate performance or causality. Keep paid-campaign optimization outside this skill.

## Routes to
Landing Page Strategist, Marketing Page CRO Auditor, Messaging Architect, Objection and Proof Strategist, Funnel Analytics Specialist.