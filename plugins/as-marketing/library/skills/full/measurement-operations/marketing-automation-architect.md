# Marketing Automation Architect

**Version:** 1.0  
**Maturity:** full skill

## Purpose
Design reliable recurring or trigger-based marketing workflows with explicit state, approvals, deduplication, retries, monitoring, and recovery.

## Owns
Automation eligibility, trigger and state model, decision branches, action specification, approval gates, idempotency, retries, limits, fallback ownership, audit, testing, monitoring, and runbook requirements.

## Use when
A stable, repeatable process should run on a schedule or business event and failures, permissions, and human review can be designed explicitly.

## Do not use when
The underlying process, lifecycle, ownership, or source of truth is unresolved. Data movement detail → Integration Workflow Designer. Lifecycle automation → Revenue Operations Architect. Tool-specific execution requires authorization.

## Required inputs
Business process, decision and outcome, trigger, source systems, records, states, actions, owners, permissions, schedule, approval policy, expected volume, service limits, legal/consent constraints, and failure risks.

## Diagnostic questions
Is the process stable enough? Which state is authoritative? Can the action be safely repeated? What requires human approval? What happens on duplicate, timeout, partial success, missing data, revoked access, or unavailable owner? How is failure seen and recovered?

## Automation readiness score
Rate 1–5 for process stability, decision clarity, source-of-truth integrity, input reliability, action reversibility, idempotency, permission safety, fallback ownership, observability, and expected value. Label inputs **fact**, **estimate**, **assumption**, or **inference**. Scores below 3 on process, permission, or fallback block activation.

## Method and decision gates
1. Confirm business decision, owner, expected outcome, manual baseline, and why automation is appropriate.
2. Define trigger/schedule, eligibility, source, record identity, state, exclusions, and termination.
3. Map decisions, branches, waits, actions, approvals, consent checks, and state transitions.
4. Specify idempotency key, deduplication, ordering, concurrency, retries, backoff, timeout, rate limit, and non-retryable errors.
5. Add fallback owner, dead-letter queue/process, alert, manual recovery, replay, and audit fields.
6. Apply least privilege, secret management requirements, data minimization, retention, and access revocation.
7. Test happy path, duplicate, missing data, stale state, partial failure, revoked permission, unavailable dependency, and recovery.
8. Monitor business outcome separately from workflow health; define review, change control, and shutdown.

## Examples
B2B service: route approved inquiries and send internal reminders while human review controls external messages. SaaS: lifecycle prompts based on stable state and consent with suppression and recovery. Ecommerce/physical product: stock, service, reorder, or partner workflows with inventory/state authority and duplicate protection.

## Output format
```markdown
# Marketing Automation Specification
## Decision, process, manual baseline
## Trigger, eligibility, state model
## Branches, actions, approvals
## Identity, idempotency, deduplication
## Retry, timeout, rate-limit rules
## Fallback, dead-letter, recovery
## Permissions, consent, data limits
## Test cases and monitoring
## Runbook, change, shutdown
```

## Quality checks
Process is stable; state is authoritative; external actions have required approval; writes are idempotent or protected; every failure path has owner; tests include adversarial cases; monitoring separates health from outcome.

## Success criteria
The workflow executes eligible cases reliably, avoids duplicate or unauthorized actions, exposes failures quickly, and can be recovered or stopped safely.

## Failure conditions
Automation hides undefined process; blind retries; silent partial failure; no fallback owner; excessive permissions; external communication without approval; health metrics replace business outcome.

## Guardrails
Do not automate unstable, deceptive, discriminatory, or unlawful processes. Never expose credentials, bypass consent, or retry non-idempotent writes blindly. Architecture does not grant permissions.

## Routes to
Integration Workflow Designer, Revenue Operations Architect, Reporting and Dashboard Designer, Tracking Plan Architect.