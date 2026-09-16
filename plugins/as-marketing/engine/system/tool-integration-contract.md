# Tool Integration Contract

## Required tool metadata
Name, description, actions, input/output schemas, read/write status, source of truth, cost, permissions, approval requirement, idempotency, retry policy, sensitive-data handling, and validation method.

## Selection rules
Prefer authoritative workspace and first-party sources. Use public research before paid contact data. Discover actions and schemas before execution. Prefer bounded reads and targeted writes. Check existing state before creating records.

## Write contract
Specify target, intended state, existing state when relevant, idempotency/deduplication, approval status, and validation query.

## Retry contract
Retry only idempotent actions or after checking current state. Never blindly retry sends, payments, publication, deletion, or non-idempotent batches.

## Result rules
Structured output is authoritative. Do not invent unsupported actions. Record errors and blockers. External, destructive, costly, and public writes follow the Approval Policy.