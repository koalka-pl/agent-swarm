# Skill Contract and Registry Schema

## Required skill interface
Each skill should define: name, version, description/purpose, owns, use when, do not use when, required inputs/context, tools, diagnostic questions, method, scoring/readiness criteria, output schema, examples, quality checks, success criteria, failure conditions, guardrails, and routes to.

Existing concise specialist contracts may omit some maturity fields temporarily, but registry presence does not imply full-quality certification.

## Ownership
Every substantial task has one owner. Specialists support but do not redefine the goal. `do not use when` should name the nearest alternative.

## Registry entry
Every registered item requires a stable ID and an exact path relative to its declared base: package paths resolve from the plugin root, project paths from the project root. Paths must resolve to one file. Removed, renamed, or split files require a registry update.

## Loading policy
Load system core, project context, one profile, one router, one owner, at most two specialists, current state, and at most one workflow. Never preload the entire library.

## Output contract
Decision; evidence; assumptions; required actions; success metric; failure threshold; saved output location when applicable; next routing decision.

## Versioning
Record material changes to methods, inputs, outputs, or guardrails and test modified routing against a previous use case.