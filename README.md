# AgentSwarm

A Claude Code plugin marketplace whose plugins share one project context. Each plugin is a separate domain (routers, skills, workflows) built on a common pattern: registry, fail-closed execution, evidence guard, approval gates, audit.

## Plugins

| Plugin | Domain | Version |
|---|---|---|
| `as-marketing` | marketing and business growth: 9 routers, 100 skills, 3 workflows | 0.3.1 |

## Installation

```
/plugin marketplace add koalka-pl/agent-swarm
/plugin install as-marketing@agent-swarm
```

Locally, without installing:

```
claude --plugin-dir ./plugins/as-marketing
```

## How it works in a project

1. `/as-marketing:start` creates or completes `.as/project-context.md`, asks for consents and creates the project state.
2. `/as-marketing:run <task>` selects one router, one owner and at most two specialists, saves the result to `.as/outputs/` and state and audit to `.as/state/`.
3. `/as-marketing:trail` shows the declared routing versus what was actually loaded.

Project data layout:

```
.as/
  project-context.md   shared context: Shared section + one section per plugin
  access.yaml          consent to read project sources and its scope
  private/             sensitive data, never imported into context
  notes/               handoff notes between plugins
  outputs/             work results
  state/               project state, audit, routing trail
```

Principles:

- **One context.** Every fact lives in one place. `## Shared` for common facts, `## <plugin>` for plugin-specific ones. A plugin edits only its own section; changes to `## Shared` require confirmation.
- **Plugin files are read-only.** Everything mutable lives in the project's `.as/`.
- **Project sources require consent.** Files outside `.as/` are read only by the `source-reader` agent, and the `source-guard.py` hook blocks it outside the scope in `.as/access.yaml`. The hook does not affect normal work in the repository.
- **Hooks stay silent elsewhere.** Nothing is written in repositories without a `.as/` directory.

## Development

```
python3 scripts/check-plugin.py plugins/as-marketing
claude plugin validate plugins/as-marketing
claude plugin validate .
```

`check-plugin.py` verifies that every registry path exists, every library file is registered, and every router route resolves to exactly one skill. Run it after any change to a router, skill, registry or policy.
