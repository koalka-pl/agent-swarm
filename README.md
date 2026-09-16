# AgentSwarm

Marketplace pluginów Claude Code, które dzielą jeden kontekst projektu. Każdy plugin to osobna domena (routery, skille, workflow) na wspólnym wzorcu: registry, fail-closed, evidence guard, bramki akceptacji, audyt.

## Pluginy

| Plugin | Domena | Status |
|---|---|---|
| `as-marketing` | marketing i wzrost biznesu: 9 routerów, 100 skilli, 3 workflow | 0.3.0 |

## Instalacja

```
/plugin marketplace add koalka-pl/agent-swarm
/plugin install as-marketing@agent-swarm
```

Lokalnie, bez instalacji:

```
claude --plugin-dir ./plugins/as-marketing
```

## Jak to działa w projekcie

1. `/as-marketing:start` tworzy lub uzupełnia `.as/project-context.md`, pyta o zgody i zakłada stan projektu.
2. `/as-marketing:run <zadanie>` wybiera jeden router, jednego właściciela i maksymalnie dwóch specjalistów, zapisuje wynik w `.as/outputs/` oraz stan i audyt w `.as/state/`.
3. `/as-marketing:trail` pokazuje zadeklarowany routing kontra to, co faktycznie wczytano.

Układ danych w projekcie:

```
.as/
  project-context.md   wspólny kontekst: sekcja Shared + sekcje pluginów
  access.yaml          zgoda na odczyt źródeł projektu i jej zakres
  private/             dane wrażliwe, nieimportowane do kontekstu
  notes/               notatki przekazania między pluginami
  outputs/             wyniki pracy
  state/               stan projektów, audyt, ślad routingu
```

Zasady:

- **Jeden kontekst.** Każdy fakt żyje w jednym miejscu. `## Shared` dla faktów wspólnych, `## <plugin>` dla specyficznych. Plugin edytuje tylko swoją sekcję; zmiany w `## Shared` wymagają potwierdzenia.
- **Pliki pluginu są tylko do odczytu.** Wszystko, co mutowalne, leży w `.as/` projektu.
- **Źródła projektu za zgodą.** Pliki spoza `.as/` czyta wyłącznie agent `source-reader`, a hook `source-guard.py` blokuje go poza zakresem z `.as/access.yaml`. Hook nie wpływa na zwykłą pracę w repozytorium.
- **Hooki milczą w obcych repozytoriach.** Bez katalogu `.as/` nic nie jest zapisywane.

## Rozwój

```
python3 scripts/check-plugin.py plugins/as-marketing
claude plugin validate plugins/as-marketing
claude plugin validate .
```

`check-plugin.py` sprawdza, że każda ścieżka z registry istnieje, każdy plik biblioteki jest zarejestrowany, a każda trasa routera wskazuje dokładnie jeden skill. Uruchom go po każdej zmianie routera, skilla, registry lub polityki.
