---
name: trail
description: Pokazuje ślad routingu AgentSwarm Marketing — zadeklarowany łańcuch kontra to, co faktycznie zostało wczytane w tej sesji.
disable-model-invocation: true
---

Pokaż pełny ślad routingu **as-marketing** dla bieżącej sesji.

1. Odczytaj `.as/state/.as-trail.json` (ślad obserwowany, zapisywany przez hook). Uwzględnij tylko wpisy z `plugin: as-marketing`. Jeśli plik nie istnieje, powiedz wprost, że w tej sesji nie wczytano jeszcze żadnego routera ani skilla.
2. Odczytaj najnowszy plik `.as/state/projects/*.yaml` z `plugin: as-marketing` (ślad zadeklarowany): `project_id`, `selected_router`, `selected_owner_skill`, `loaded_specialists`, `active_workflow`.
3. Odczytaj `loading_limits` z `${CLAUDE_PLUGIN_ROOT}/engine/config.yaml`.

Przedstaw wynik jako:

**Zadeklarowany łańcuch** — `<project-id> > <router> > <owner skill> > <specjaliści> > <workflow>`. Pola puste oznacz jako `—`.

**Obserwowany łańcuch** — wpisy ze śladu w kolejności wczytania, pogrupowane po `kind` (router / skill / workflow / profile / context / source), ze znacznikami czasu.

**Rozbieżności** — każda osobno:
- router wczytany, ale inny niż `selected_router`
- więcej niż jeden router wczytany w sesji
- skill wczytany, ale nieobecny w `selected_owner_skill` ani `loaded_specialists`
- liczba specjalistów ponad `loading_limits.specialists`
- `selected_owner_skill` zadeklarowany, ale nigdy nie wczytany
- odczyt źródeł projektu (`kind: source`) poza agentem `source-reader`

Jeśli rozbieżności nie ma, napisz jedno zdanie, że łańcuch jest spójny.

Nie naprawiaj niczego i nie modyfikuj stanu. To komenda diagnostyczna: wyjściem jest raport i, przy rozbieżnościach, rekomendacja poprawki do zatwierdzenia.
