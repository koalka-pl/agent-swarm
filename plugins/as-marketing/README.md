# as-marketing

AgentSwarm Marketing: a routing system for marketing and business growth.

## Commands

- `/as-marketing:start [project-id]` — initialize in a project
- `/as-marketing:run <task>` — execute a task through routing
- `/as-marketing:trail` — routing diagnostics

## Structure

```
engine/      config, registry, policies, schemas, templates, validate.py
library/     routers, skills (core and full), workflows, business-model profiles
skills/      start, run, trail commands
agents/      source-reader
hooks/       as-trail.py (routing trail), source-guard.py (source consent), as_data.py (data directory)
tests/smoke/ reference routing scenario
```

`engine/registry.yaml` has two path bases: `package`, relative to the plugin directory, and `project`, relative to the data directory chosen in `/as-marketing:start` and recorded in `.as.yaml`.

## Scope

Nine domains: Business & Growth, Market & Customer Insight, Positioning & Product Marketing, Offer/Pricing/Monetization, Content/SEO/AEO, Acquisition & Distribution, Conversion & Experimentation, Sales & Revenue, Measurement & Marketing Operations.

Out of scope: paid media planning and execution, and website design and development.

## Requirements

Python 3 (standard library only) for hooks and validation.

## License

Proprietary commercial software. See [LICENSE](LICENSE).
