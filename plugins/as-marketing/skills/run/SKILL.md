---
name: run
description: Executes a marketing or business task through AgentSwarm Marketing — selects one router, one owner and at most two specialists, saves the result and an audit record.
argument-hint: "<task, e.g. build a campaign for X>"
disable-model-invocation: true
---

Task: $ARGUMENTS

Execute it through the **as-marketing** system. Plugin files (read-only) live in `${CLAUDE_PLUGIN_ROOT}`; all `engine/` and `library/` paths are relative to that directory. Project data lives in the project's data directory, written below as `<data>/`.

## Entry condition

Resolve `<data>`: the `data_dir` value from `.as.yaml` at the project root; if that file does not exist but `<data>/` does, use `.as`. If neither exists, or `<data>/project-context.md` does not exist or has no `## as-marketing` section, stop and ask the user to run `/as-marketing:start`. Do not improvise context or create the data directory yourself.

## Startup (every time)

1. Read `engine/config.yaml` and `engine/registry.yaml`.
2. Read every file in `as.always_load`.
3. Read `<data>/project-context.md` (the `## Shared` and `## as-marketing` sections). Skip if it is already in the session context through the `CLAUDE.md` import.
4. Find the active state in `<data>/state/projects/` (`plugin: as-marketing`, `status` other than `closed`/`completed`). If there are several and the task does not point to one — ask.
5. Load one profile section from `library/business-model-profiles.md`, matching `business_model_profile`.
6. Check `<data>/notes/` for open notes addressed to `as-marketing`.

## Routing

1. Classify the task into **exactly one** domain from `routers` in the registry.
2. Load **one** router. Select the owner from its "Routing" and "Selection rules" sections.
3. The router gives the skill's display name. Resolve it by H1 heading: `grep -rlx "# <Name>" "${CLAUDE_PLUGIN_ROOT}/library/skills"`. There must be exactly one result and it must be listed under `skills` in the registry. No match or more than one = stop (fail closed), do not guess.
4. Load **one** owner skill. Load specialists (max 2) and a workflow (max 1) only when the owner skill calls for them in "Routes to" or its method.
5. Never load files outside the registry and never the whole library.
6. Explicitly reject tasks from `as.excluded_domains`.

## Execution

- Apply the "Execution Policy", "Evidence and Claims Guard" and "Approval and Safety Policy".
- Ask only when missing information changes direction, risk, cost or scope.
- **Project sources**: do not read project files outside `<data>/` yourself. If the task needs them, check `<data>/access.yaml`. With `granted: true`, delegate the reading to the `as-marketing:source-reader` agent, giving concrete paths and a question. Without consent, ask for it and pause that part of the work.
- **Notes**: if a finding concerns another plugin or requires a change to `## Shared`, write a note `<data>/notes/<date>-<topic>.md` with fields: `from`, `to`, `status: open`, `decision`, `evidence`, `open_questions`. Change `## Shared` only after the user confirms.

## Save and validate

1. Save narrative output to `<data>/outputs/<project-id>/<date>-<slug>.md`.
2. Update the project state: `selected_router`, `selected_owner_skill`, `loaded_specialists`, `active_workflow` (full registry paths), `plan`, `artifacts`, `open_questions`, `assumptions`, `pending_approvals`, `next_action`, `updated_at`.
3. Create an audit record `<data>/state/audit/<date>-<project-id>-<slug>.yaml` with `plugin: as-marketing`.
4. Validate:
   `python3 "${CLAUDE_PLUGIN_ROOT}/engine/validate.py" project-state <state file>`
   `python3 "${CLAUDE_PLUGIN_ROOT}/engine/validate.py" audit-record <audit file>`
   Fix and repeat until both pass.

## Reply

Summary: business outcome; selected domain → router → owner → specialists → workflow; assumptions; saved artifacts; evidence status; validation result; pending approvals; next step.

Do not mark the work complete until the output exists on disk, validation passes, and state and audit are updated.
