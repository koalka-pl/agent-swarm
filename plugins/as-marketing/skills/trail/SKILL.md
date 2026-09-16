---
name: trail
description: Shows the AgentSwarm Marketing routing trail — the declared chain versus what was actually loaded in this session.
disable-model-invocation: true
---

Show the full **as-marketing** routing trail for the current session.

1. Read `.as/state/.as-trail.json` (the observed trail, written by a hook). Use only entries with `plugin: as-marketing`. If the file does not exist, say plainly that no router or skill has been loaded in this session yet.
2. Read the most recent `.as/state/projects/*.yaml` with `plugin: as-marketing` (the declared trail): `project_id`, `selected_router`, `selected_owner_skill`, `loaded_specialists`, `active_workflow`.
3. Read `loading_limits` from `${CLAUDE_PLUGIN_ROOT}/engine/config.yaml`.

Present the result as:

**Declared chain** — `<project-id> > <router> > <owner skill> > <specialists> > <workflow>`. Mark empty fields as `—`.

**Observed chain** — trail entries in load order, grouped by `kind` (router / skill / workflow / profile / context / source), with timestamps.

**Divergences** — each one separately:
- a router was loaded but differs from `selected_router`
- more than one router loaded in the session
- a skill was loaded but is neither `selected_owner_skill` nor in `loaded_specialists`
- more specialists than `loading_limits.specialists`
- `selected_owner_skill` declared but never loaded
- project sources read (`kind: source`) outside the `source-reader` agent

If there are no divergences, say in one sentence that the chain is consistent.

Do not fix anything and do not modify state. This is a diagnostic command: its output is a report and, when there are divergences, a recommended fix for approval.
