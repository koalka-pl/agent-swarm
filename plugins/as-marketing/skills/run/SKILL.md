---
name: run
description: Wykonuje zadanie marketingowe lub biznesowe przez AgentSwarm Marketing — wybiera jeden router, jednego właściciela i maksymalnie dwóch specjalistów, zapisuje wynik i audyt.
argument-hint: "<zadanie, np. zrób kampanię dla X>"
disable-model-invocation: true
---

Zadanie: $ARGUMENTS

Wykonaj je przez system **as-marketing**. Pliki pluginu (tylko do odczytu) leżą w `${CLAUDE_PLUGIN_ROOT}`; wszystkie ścieżki `engine/` i `library/` są względne wobec tego katalogu. Dane projektu leżą w `.as/` w katalogu projektu.

## Warunek wejścia

Jeśli nie istnieje `.as/project-context.md` albo brakuje w nim sekcji `## as-marketing`, zatrzymaj się i poproś o uruchomienie `/as-marketing:start`. Nie improwizuj kontekstu.

## Start (za każdym razem)

1. Przeczytaj `engine/config.yaml` i `engine/registry.yaml`.
2. Przeczytaj wszystkie pliki z `as.always_load`.
3. Przeczytaj `.as/project-context.md` (sekcje `## Shared` i `## as-marketing`). Pomiń, jeśli jest już w kontekście sesji przez import w `CLAUDE.md`.
4. Znajdź aktywny stan w `.as/state/projects/` (`plugin: as-marketing`, `status` inny niż `closed`/`completed`). Jeśli jest kilka i zadanie nie wskazuje jednego — zapytaj.
5. Wczytaj jedną sekcję profilu z `library/business-model-profiles.md`, zgodnie z `business_model_profile`.
6. Przejrzyj `.as/notes/` pod kątem otwartych notatek adresowanych do `as-marketing`.

## Routing

1. Sklasyfikuj zadanie do **dokładnie jednej** domeny z `routers` w registry.
2. Wczytaj **jeden** router. Wybierz właściciela z sekcji „Routing” i „Selection rules”.
3. Router podaje nazwę wyświetlaną skilla. Rozwiąż ją po nagłówku H1: `grep -rlx "# <Nazwa>" "${CLAUDE_PLUGIN_ROOT}/library/skills"`. Wynik musi być dokładnie jeden i musi figurować w `skills` w registry. Brak dopasowania lub więcej niż jedno = zatrzymanie (fail closed), nie zgadywanie.
4. Wczytaj **jeden** owner skill. Specjalistów (maks. 2) i workflow (maks. 1) wczytaj tylko wtedy, gdy owner skill ich wymaga w „Routes to” lub metodzie.
5. Nigdy nie wczytuj plików spoza registry i nigdy całej biblioteki.
6. Zadania z `as.excluded_domains` odrzuć jawnie.

## Wykonanie

- Stosuj „Execution Policy”, „Evidence and Claims Guard” i „Approval and Safety Policy”.
- Pytaj tylko wtedy, gdy brak informacji zmienia kierunek, ryzyko, koszt lub zakres.
- **Źródła projektu**: nie czytaj plików projektu spoza `.as/` samodzielnie. Jeśli zadanie tego wymaga, sprawdź `.as/access.yaml`. Przy `granted: true` deleguj odczyt agentowi `as-marketing:source-reader`, podając konkretne ścieżki i pytanie. Przy braku zgody poproś o nią i zatrzymaj tę część pracy.
- **Notatki**: jeśli ustalenie dotyczy innego pluginu albo wymaga zmiany sekcji `## Shared`, zapisz notatkę `.as/notes/<data>-<temat>.md` z polami: `from`, `to`, `status: open`, `decision`, `evidence`, `open_questions`. Zmiany w `## Shared` wprowadzaj wyłącznie po potwierdzeniu użytkownika.

## Zapis i walidacja

1. Wynik narracyjny zapisz w `.as/outputs/<project-id>/<data>-<slug>.md`.
2. Zaktualizuj stan projektu: `selected_router`, `selected_owner_skill`, `loaded_specialists`, `active_workflow` (pełne ścieżki z registry), `plan`, `artifacts`, `open_questions`, `assumptions`, `pending_approvals`, `next_action`, `updated_at`.
3. Utwórz rekord audytu `.as/state/audit/<data>-<project-id>-<slug>.yaml` z `plugin: as-marketing`.
4. Waliduj:
   `python3 "${CLAUDE_PLUGIN_ROOT}/engine/validate.py" project-state <plik stanu>`
   `python3 "${CLAUDE_PLUGIN_ROOT}/engine/validate.py" audit-record <plik audytu>`
   Popraw i powtarzaj do skutku.

## Odpowiedź

Podsumowanie: cel biznesowy; wybrana domena → router → owner → specjaliści → workflow; założenia; zapisane artefakty; status dowodów; wynik walidacji; oczekujące zgody; następny krok.

Nie oznaczaj pracy jako zakończonej, dopóki wynik nie istnieje na dysku, walidacja nie przejdzie, a stan i audyt nie są zaktualizowane.
