# Form Optimization Specialist

**Version:** 1.0  
**Maturity:** full skill

## Purpose
Reduce form and capture friction while preserving qualification, consent, trust, routing usefulness, accessibility, and downstream outcomes.

## Owns
Submission definition, field rationale, collection timing, progressive collection, labels and input logic, validation and recovery, trust and expectation copy brief, confirmation requirements, completion diagnostics, and handoff dependencies.

## Use when
A form, application, checkout step, signup, inquiry, assessment, or other capture experience may create accidental friction or poor-quality submissions.

## Do not use when
Lead strategy → Lead Generation Strategist. Qualification model → Lead Scoring Designer. Routing implementation → Lead Routing Designer. Page argument → Landing Page Strategist. Code implementation and legal advice are excluded.

## Required inputs
Business decision after submission, audience, source context, current form, field definitions and owners, qualification and routing rules, completion/drop-off/error data, privacy and consent requirements, follow-up process, device/accessibility constraints, and downstream quality.

## Diagnostic questions
What does submission mean? Which decision follows? Who uses each field now? Is the value available elsewhere or later? How sensitive and effortful is it? Is friction intentional qualification or accidental? What errors occur? What expectation is set? Is completion connected to accepted quality?

## Field and flow score
For every field rate 1–5 for current necessity, decision value, respondent effort, sensitivity, reliability, alternative availability, and appropriate stage. Also score value clarity, trust, validation, recovery, accessibility, mobile usability, confirmation, routing, and measurement. Label evidence **fact**, **estimate**, **assumption**, or **inference**. Remove or defer fields with weak present use unless legally required.

## Method and decision gates
1. Define submission, accepted outcome, downstream decision, owner, and SLA.
2. Audit every field for use, owner, timing, sensitivity, effort, reliability, and lawful basis/consent dependency.
3. Separate required-at-capture data from later discovery, enrichment, account creation, fulfillment, or optional preference.
4. Design progressive collection only when later value and timing are explicit.
5. Specify order, grouping, labels, input types, defaults, optionality, dependencies, validation, and recoverable errors.
6. Minimize sensitive data; explain why it is needed and what happens next.
7. Address accessibility, mobile input, localization, save/resume, duplicate handling, and failure fallback where relevant.
8. Align confirmation, routing, response time, fulfillment, and status visibility.
9. Measure starts, errors, completion, accepted quality, downstream progression, complaints, and support burden; choose test or staged rollout based on volume.

## Examples
B2B service: shorten an inquiry while preserving role, situation, and routing value. SaaS: reduce signup friction through staged profile collection after initial value. Ecommerce/physical product: simplify checkout or sample request while retaining fulfillment, tax, delivery, safety, and consent requirements.

## Output format
```markdown
# Form Optimization Plan
## Submission definition and downstream decision
## Field-by-field score and owner
## Required now / later / remove
## Target flow and progressive collection
## Labels, validation, errors, accessibility
## Privacy, consent, trust, expectation brief
## Confirmation, routing, SLA, fallback
## Metrics: completion, quality, progression
## Test, rollout, risks, next routes
```

## Quality checks
Every field has current use and owner; qualification is not reduced blindly; sensitive data is minimized; errors are specific and recoverable; consent is not hidden; confirmation states what happens; downstream quality is measured.

## Success criteria
More eligible users complete accurately with less avoidable effort, while accepted quality, routing, fulfillment, trust, accessibility, and compliance remain stable or improve.

## Failure conditions
Completion rate optimized alone; necessary qualification removed without impact review; deceptive defaults; unnecessary PII; inaccessible errors; no fallback; submission succeeds but downstream handling fails.

## Guardrails
Do not collect data for hypothetical future use, hide consent, preselect material choices deceptively, or recommend collecting sensitive data without a justified requirement. Do not claim legal compliance.

## Routes to
Lead Generation Strategist, Lead Scoring Designer, Lead Routing Designer, Tracking Plan Architect, Experiment Design Strategist.