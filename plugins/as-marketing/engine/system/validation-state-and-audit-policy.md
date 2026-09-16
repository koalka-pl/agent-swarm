# Validation, State, and Audit Policy

## State layers
- Project context: durable company/product facts and approved decisions.
- Project state: goal, plan, completed work, assumptions, blockers, approvals, and next action.
- Operational records: contacts, accounts, content, opportunities, experiments, metrics, and runs.
- Source documents: research, strategies, briefs, and reports.

## Validation
Documents require their stated sections, evidence, labeled assumptions, and decision logic. Structured records require schema, counts, valid statuses/dates, and duplicate checks. External drafts require correct context and review status. Host-system implementation requires focused functional validation.

## Completion check
Confirm requested output exists, is durable, includes required evidence, respects approvals, changes no unrelated scope, and records unresolved risks.

## Audit
Validate run records against `engine/schemas/audit-record.schema.json`, project state against `engine/schemas/project-state.schema.json`, and approvals against `engine/schemas/approval.schema.json`.

## Guardrails
Do not store credentials, secrets, sensitive personal data without need, or private chain-of-thought. Record decisions, evidence, actions, and reasons—not hidden reasoning.