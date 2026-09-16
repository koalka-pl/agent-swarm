# as-marketing

AgentSwarm Marketing: system routingu dla marketingu i wzrostu biznesu.

## Komendy

- `/as-marketing:start [project-id]` — inicjalizacja w projekcie
- `/as-marketing:run <zadanie>` — wykonanie zadania przez routing
- `/as-marketing:trail` — diagnostyka routingu

## Struktura

```
engine/      config, registry, polityki, schematy, szablony, validate.py
library/     routery, skille (core i full), workflow, profile modeli biznesowych
skills/      komendy start, run, trail
agents/      source-reader
hooks/       as-trail.py (ślad routingu), source-guard.py (zgoda na źródła)
tests/smoke/ scenariusz referencyjny routingu
```

`engine/registry.yaml` ma dwie bazy ścieżek: `package` względem katalogu pluginu i `project` względem katalogu projektu.

## Zakres

Dziewięć domen: Business & Growth, Market & Customer Insight, Positioning & Product Marketing, Offer/Pricing/Monetization, Content/SEO/AEO, Acquisition & Distribution, Conversion & Experimentation, Sales & Revenue, Measurement & Marketing Operations.

Poza zakresem: planowanie i prowadzenie płatnych kampanii oraz projektowanie i budowa stron.

## Wymagania

Python 3 (tylko biblioteka standardowa) do hooków i walidacji.
