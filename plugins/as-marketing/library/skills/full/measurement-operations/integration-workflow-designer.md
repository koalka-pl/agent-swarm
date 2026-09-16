# Integration Workflow Designer

**Version:** 1.0  
**Maturity:** full skill

## Purpose
Design safe, observable data movement between marketing, sales, analytics, customer, and communication systems while preserving identity, ownership, and source-of-truth integrity.

## Owns
Business event, source/destination authority, schema mapping, identity matching, transformations, sync direction, conflict policy, permissions, idempotency, retries, reconciliation, monitoring, replay, and runbook.

## Use when
Approved processes require records or state to move between systems and technical failure, duplication, ordering, and ownership must be designed before implementation.

## Do not use when
Business process automation → Marketing Automation Architect. CRM schema → CRM Architecture Strategist. Event semantics → Tracking Plan Architect. Vendor-specific implementation requires authorized access and discovered capabilities.

## Required inputs
Source/destination systems, authoritative source by field/state, schemas, identities, permissions, trigger/schedule, expected volume, latency, transformations, filters, conflict policy, limits, retention, and failure requirements.

## Diagnostic questions
What business event causes movement? Which system owns each field? How are records matched? What happens on duplicate, out-of-order, partial, late, deleted, or conflicting data? Can writes be repeated safely? Which permissions are essential? Who detects and repairs failure?

## Integration readiness score
Rate 1–5 for process clarity, source authority, schema stability, identity reliability, transformation determinism, permission safety, idempotency, failure recovery, observability, and owner readiness. Label mappings **authoritative**, **derived**, **estimated**, **optional**, or **prohibited**. Unresolved source authority blocks activation.

## Method and decision gates
1. Define business event, decision, source, destination, entity, volume, latency, and service expectation.
2. Create source-of-truth map for each object, field, status, deletion, and timestamp.
3. Map names, types, required/optional values, enums, relationships, nulls, units, timezone, and transformations.
4. Define identity matching, deduplication, merge/survivorship, conflict resolution, and unmatched handling.
5. Specify trigger/schedule, direction, filtering, ordering, batching, and backfill.
6. Apply least privilege, secret-management requirements, data minimization, retention, and environment separation.
7. Design idempotency, retries/backoff, timeout, rate limits, partial failure, dead-letter handling, reconciliation, and replay.
8. Add logs, metrics, alerts, owner, runbook, audit, versioning, and shutdown.
9. Test representative, duplicate, malformed, out-of-order, missing, conflicting, revoked-access, limit, outage, and recovery cases before activation.

## Examples
B2B service: synchronize qualified inquiries and opportunity state without overwriting CRM ownership. SaaS: connect product/account/subscription events to CRM and lifecycle systems using stable IDs. Ecommerce/physical product: move order, refund, fulfillment, consent, and customer state while keeping commerce system authoritative.

## Output format
```markdown
# Integration Workflow Design
## Business event and service expectation
## Source-of-truth map
## Object and field mapping
## Identity, deduplication, conflict rules
## Trigger, direction, filter, transformation
## Permissions, secrets, data minimization
## Retry, ordering, partial failure, replay
## Reconciliation, monitoring, ownership
## Test suite, runbook, shutdown
```

## Quality checks
Authority is explicit; transformations are deterministic; identities handle unmatched cases; writes are idempotent/protected; conflicts never overwrite silently; permissions are minimal; failures can be detected and replayed.

## Success criteria
Data moves accurately and traceably within expected latency, preserves authoritative state, and can recover from duplicates, partial failures, outages, and schema change.

## Failure conditions
Multiple uncontrolled truths; credentials exposed; silent overwrite; blind retry; no reconciliation; deletion ignored; production activated without adversarial tests; implementation claimed without validation.

## Guardrails
Never expose credentials, bypass permissions, move unnecessary personal data, or silently resolve conflicts. Architecture does not grant access or execute unapproved writes.

## Routes to
Marketing Automation Architect, CRM Architecture Strategist, Tracking Plan Architect, Revenue Operations Architect.