---
name: start
description: Initializes AgentSwarm Marketing in the current project — creates or completes .as/project-context.md, collects consents and creates the project state.
argument-hint: "[project-id]"
disable-model-invocation: true
---

Initialize the **as-marketing** plugin in the current project.

Suggested `project-id` (if provided): $ARGUMENTS

Plugin files (read-only) live in `${CLAUDE_PLUGIN_ROOT}`. Project data lives in the `.as/` directory at the project root. Never write anything to `${CLAUDE_PLUGIN_ROOT}`.

## Procedure

1. Read `${CLAUDE_PLUGIN_ROOT}/engine/config.yaml` and `${CLAUDE_PLUGIN_ROOT}/engine/registry.yaml`.
2. Load every file listed in `as.always_load` (paths relative to `${CLAUDE_PLUGIN_ROOT}`).
3. Inspect the project and pick a mode:
   - **New** — `.as/project-context.md` does not exist. Create it from `${CLAUDE_PLUGIN_ROOT}/engine/templates/project-context.md`.
   - **Join** — the file exists (e.g. created by another AgentSwarm plugin) but has no `## as-marketing` section. Do not touch `## Shared` beyond filling gaps; append the `## as-marketing` section from the template.
   - **Complete** — the file and the section exist. Ask only about fields still marked `[required]` or `unknown` that block work.
   If `Schema version` in the existing file differs from the template, stop and describe the difference instead of overwriting.
4. Ask **one round of questions** (max 5–7, grouped), only about missing `[required]` fields. Leave `[optional]` and `[known/unknown]` fields for later.
5. Select exactly one profile from `${CLAUDE_PLUGIN_ROOT}/library/business-model-profiles.md`, respecting its "Selection guardrails". Justify it in one sentence and ask for confirmation.
6. In the same round, ask for three consents, each separately:
   a. **Context import** — append the line `@.as/project-context.md` to the project's `CLAUDE.md` (create the file if missing). This puts the context into every session and every subagent. If the line is already there, do not add it again.
   b. **Project source access** — whether the `source-reader` agent may read project files, and if so, which directories. Default: no access.
   c. **.gitignore** — add `.as/private/` and `.as/state/.as-trail.json`.
7. Write the files (see "Required result").
8. Finish with a summary.

## Execution rules

- Do not start by writing files. Questions and consents come first.
- Record every unconfirmed field as `unknown` and add it to `open_questions` in the project state. No guessing: no default prices, metrics, segments, tools or results.
- If the repository contains material describing the company, you may read it only after consent 6b and only through the `source-reader` agent. Mark facts from it with their source and still ask for confirmation.
- `project-id`: use the argument if given; otherwise propose a stable kebab-case id and ask for confirmation. If `.as/state/projects/<project-id>.yaml` already exists — stop and ask.
- Choose the router and owner skill according to `as.loading_limits`. At start, a recommended router and owner skill is enough; specialists and workflow stay empty.
- Do not propose anything from `as.excluded_domains`.
- No answer to a consent request means no consent.

## Required result

1. `.as/project-context.md` — confirmed facts, explicit `unknown`, both "Last verified" blocks filled in.
2. `.as/access.yaml` — from `${CLAUDE_PLUGIN_ROOT}/engine/templates/access.yaml`. With consent: `granted: true`, `granted_by`, `granted_at` (UTC ISO-8601 with `Z`) and `read_paths` as a list of project-relative directories ending with `/`. Without consent keep `granted: false`.
3. `.as/state/projects/<project-id>.yaml` from `${CLAUDE_PLUGIN_ROOT}/engine/templates/project-state.yaml`, with: `plugin: as-marketing`, `project_id`, `title`, `user_goal`, `status: active`, `company_context_path`, `business_model_profile`, `selected_router`, `selected_owner_skill`, `open_questions`, `assumptions`, `next_action`, `updated_at`.
4. Existing directories `.as/state/audit/`, `.as/notes/`, `.as/outputs/`, `.as/private/`.
5. Changes from 6a and 6c, only if consent was given.
6. Validation: `python3 "${CLAUDE_PLUGIN_ROOT}/engine/validate.py" project-state .as/state/projects/<project-id>.yaml`. If it fails, fix the file and repeat. Report the result.
7. Summary in the reply: (a) context in 5–8 bullets, (b) open questions and `unknown` fields, (c) consents granted and not granted, (d) recommended first area of work with a concrete next step in the form `/as-marketing:run <task>`.

Do not mark the work complete until the files exist on disk and validation passes.
