---
name: start
description: Initializes AgentSwarm Marketing in the current project — lets the user choose the data directory, creates or completes project-context.md, collects consents and creates the project state.
argument-hint: "[project-id]"
disable-model-invocation: true
---

Initialize the **as-marketing** plugin in the current project.

Suggested `project-id` (if provided): $ARGUMENTS

Plugin files (read-only) live in `${CLAUDE_PLUGIN_ROOT}`. Never write anything there. Project data lives in the project's **data directory**, written below as `<data>/`.

## Data directory

Resolve it before anything else:

1. If `.as.yaml` exists at the project root, `<data>` is its `data_dir` value. Do not ask again. If the value is invalid (absolute, outside the project, `.` or empty), stop and report it.
2. Otherwise, if `.as/` exists at the project root, `<data>` is `.as` (earlier installation). Do not ask again; you will write `.as.yaml` with `data_dir: .as`.
3. Otherwise ask the user where AgentSwarm should keep project data. Default: `.as`. Rules for the answer:
   - a relative path inside the project, without `..`, not the project root itself; strip a leading `/` or `./` (`/docs` means `docs`);
   - if the directory exists and already contains unrelated files, propose a subfolder instead (e.g. `docs/as`) and let the user decide;
   - warn that the directory will contain `private/` and `access.yaml`; if it is published (a docs site, a static build input, a public folder), recommend a different location or at least excluding `private/` from publishing.

The data directory is shared by every AgentSwarm plugin in this project. Changing it later means moving the files and updating `.as.yaml`; do not do that as part of start.

## Procedure

1. Read `${CLAUDE_PLUGIN_ROOT}/engine/config.yaml` and `${CLAUDE_PLUGIN_ROOT}/engine/registry.yaml`.
2. Load every file listed in `as.always_load` (paths relative to `${CLAUDE_PLUGIN_ROOT}`).
3. Resolve `<data>` (see above).
4. Inspect the project and pick a mode:
   - **New** — `<data>/project-context.md` does not exist. Create it from `${CLAUDE_PLUGIN_ROOT}/engine/templates/project-context.md`.
   - **Join** — the file exists (e.g. created by another AgentSwarm plugin) but has no `## as-marketing` section. Do not touch `## Shared` beyond filling gaps; append the `## as-marketing` section from the template.
   - **Complete** — the file and the section exist. Ask only about fields still marked `[required]` or `unknown` that block work.
   If `Schema version` in the existing file differs from the template, stop and describe the difference instead of overwriting.
5. Ask **one round of questions** (max 5–7, grouped): the data directory if it is not resolved yet, the website URL (or that there is none), then only missing `[required]` fields. Leave `[optional]` and `[known/unknown]` fields for later. Do not read the website at this stage; answers come from the user, so they are not anchored by what the site currently says.
6. Select exactly one profile from `${CLAUDE_PLUGIN_ROOT}/library/business-model-profiles.md`, respecting its "Selection guardrails". Justify it in one sentence and ask for confirmation.
7. In the same round, ask for three consents, each separately:
   a. **Context import** — append the line `@<data>/project-context.md` to the project's `CLAUDE.md` (create the file if missing). This puts the context into every session and every subagent. If the line is already there, do not add it again.
   b. **Project source access** — whether the `source-reader` agent may read project files, and if so, which directories. Default: no access.
   c. **.gitignore** — add `<data>/private/` and `<data>/state/.as-trail.json`.
8. Write the files (see "Required result").
9. Finish with a summary.
10. **Follow-up: website audit.** Only if the context has a website URL, end the reply with one question: whether to audit the website content against the confirmed context now (contradictions, gaps, unsupported claims, current state of content). No answer or "no" means no audit.
    If the user agrees, run it through the `run` procedure: read `${CLAUDE_PLUGIN_ROOT}/skills/run/SKILL.md` and execute it for the task "website context audit", using the registered workflow `library/workflows/website-context-audit.md` and its fixed routing.

## Execution rules

- Do not start by writing files. Questions and consents come first.
- Record every unconfirmed field as `unknown` and add it to `open_questions` in the project state. No guessing: no default prices, metrics, segments, tools or results.
- If the repository contains material describing the company, you may read it only after consent 7b and only through the `source-reader` agent. Mark facts from it with their source and still ask for confirmation.
- `project-id`: use the argument if given; otherwise propose a stable kebab-case id and ask for confirmation. If `<data>/state/projects/<project-id>.yaml` already exists — stop and ask.
- Choose the router and owner skill according to `as.loading_limits`. At start, a recommended router and owner skill is enough; specialists and workflow stay empty.
- Do not propose anything from `as.excluded_domains`.
- No answer to a consent request means no consent.

## Required result

1. `.as.yaml` at the project root containing exactly `data_dir: <data>` (create or keep; never point it somewhere else than the resolved directory).
2. `<data>/project-context.md` — confirmed facts, explicit `unknown`, both "Last verified" blocks filled in.
3. `<data>/access.yaml` — from `${CLAUDE_PLUGIN_ROOT}/engine/templates/access.yaml`. With consent: `granted: true`, `granted_by`, `granted_at` (UTC ISO-8601 with `Z`) and `read_paths` as a list of project-relative directories ending with `/`. Without consent keep `granted: false`.
4. `<data>/state/projects/<project-id>.yaml` from `${CLAUDE_PLUGIN_ROOT}/engine/templates/project-state.yaml`, with: `plugin: as-marketing`, `project_id`, `title`, `user_goal`, `status: active`, `company_context_path: <data>/project-context.md`, `business_model_profile`, `selected_router`, `selected_owner_skill`, `open_questions`, `assumptions`, `next_action`, `updated_at`.
5. Existing directories `<data>/state/audit/`, `<data>/notes/`, `<data>/outputs/`, `<data>/private/`.
6. `<data>/README.md` from `${CLAUDE_PLUGIN_ROOT}/engine/templates/data-readme.md`, explaining the directory to people who open it. Write it if it does not exist. If it exists and its first line is `<!-- agent-swarm:data-readme v…` with an older version, replace it. If it exists without that marker, it is the user's own file: do not overwrite it, ask whether to write the AgentSwarm README as `<data>/AGENTSWARM.md` instead.
7. Changes from 7a and 7c, only if consent was given.
8. Validation: `python3 "${CLAUDE_PLUGIN_ROOT}/engine/validate.py" project-state <data>/state/projects/<project-id>.yaml`. If it fails, fix the file and repeat. Report the result.
9. Summary in the reply: (a) data directory, (b) context in 5–8 bullets, (c) open questions and `unknown` fields, (d) consents granted and not granted, (e) recommended first area of work with a concrete next step in the form `/as-marketing:run <task>`, (f) the website audit question from step 10, if applicable.

Do not mark the work complete until the files exist on disk and validation passes.
