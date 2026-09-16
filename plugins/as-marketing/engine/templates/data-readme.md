<!-- agent-swarm:data-readme v1 -->
# AgentSwarm project data

This directory holds everything AgentSwarm plugins know and produce for this project. It is created by `/<plugin>:start` (e.g. `/as-marketing:start`) and shared by every AgentSwarm plugin installed here. The plugins themselves live elsewhere and are read-only; all project-specific data lives here.

The location of this directory is recorded in `.as.yaml` at the project root (`data_dir`).

## Layout

| Path | What it is | Who writes it | Edit by hand? |
|---|---|---|---|
| `project-context.md` | The single source of truth about the project: `## Shared` facts plus one section per plugin. Imported into every Claude Code session through `CLAUDE.md`. | `start`, then you | Yes. Keep facts confirmed, mark gaps as `unknown`, update "Last verified". |
| `access.yaml` | Your consent for the `source-reader` agent to read project files, and which directories. A hook enforces it. | `start`, then you | Yes. Set `granted: false` to revoke access. |
| `outputs/` | Finished work: strategies, audits, briefs, plans. One folder per project id. | `run` | Yes, it is your material. Keep file names so state and audit references stay valid. |
| `notes/` | Handoff notes: findings for another plugin or proposed changes to `## Shared`. `status: open` until resolved. | `run` | Yes. Close a note once its decision is applied to the context. |
| `state/projects/` | One YAML file per initiative: goal, selected routing, plan, open questions, pending approvals, next action. | `start`, `run` | Rarely. Files are validated against a schema; run the validator after changes. |
| `state/audit/` | One record per completed run: routing, tools used, claims review, approvals, validation. | `run` | No. It is the history of what was done and why. |
| `state/.as-trail.json` | What the current session actually loaded (routers, skills, sources). Used by `/<plugin>:trail`. | hook | No. Overwritten every session. |
| `private/` | Sensitive data (finances, contracts, personal data). Never imported into context and blocked for `source-reader`. | you | Yes. |

## Rules

- **One fact, one place.** Facts used by more than one plugin go under `## Shared`; plugin-specific facts under that plugin's section. A plugin edits only its own section and asks before changing `## Shared`.
- **Nothing is inferred silently.** Unconfirmed information is `unknown` or listed as an open question.
- **External actions need approval.** Sending, publishing, deleting or spending is prepared here and executed only after your explicit approval.

## Git

Commit: `project-context.md`, `access.yaml`, `outputs/`, `notes/`, `state/projects/`, `state/audit/`, this README.

Ignore: `private/` and `state/.as-trail.json` (`start` offers to add both to `.gitignore`).

If this directory is part of something that gets published (a docs site, a static build), exclude it or at least `private/` and `access.yaml` from publishing.

## Moving this directory

Move the whole directory, update `data_dir` in `.as.yaml`, update the `@…/project-context.md` line in `CLAUDE.md` and the paths in `.gitignore`. Paths stored in `state/` are relative to the project root, so update `company_context_path` in each project state file too.
