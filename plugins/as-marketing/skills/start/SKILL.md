---
name: start
description: Inicjalizuje AgentSwarm Marketing w bieżącym projekcie — tworzy lub uzupełnia .as/project-context.md, zbiera zgody i zakłada stan projektu.
argument-hint: "[project-id]"
disable-model-invocation: true
---

Zainicjalizuj plugin **as-marketing** w bieżącym projekcie.

Sugerowany `project-id` (jeśli podany): $ARGUMENTS

Pliki pluginu (tylko do odczytu) leżą w `${CLAUDE_PLUGIN_ROOT}`. Dane projektu leżą w katalogu `.as/` w katalogu głównym projektu. Nigdy nie zapisuj niczego w `${CLAUDE_PLUGIN_ROOT}`.

## Procedura

1. Przeczytaj `${CLAUDE_PLUGIN_ROOT}/engine/config.yaml` i `${CLAUDE_PLUGIN_ROOT}/engine/registry.yaml`.
2. Załaduj wszystkie pliki z `as.always_load` (ścieżki względem `${CLAUDE_PLUGIN_ROOT}`).
3. Sprawdź stan projektu i ustal tryb:
   - **Nowy** — nie istnieje `.as/project-context.md`. Utworzysz go z `${CLAUDE_PLUGIN_ROOT}/engine/templates/project-context.md`.
   - **Dołączenie** — plik istnieje (np. utworzył go inny plugin AgentSwarm), ale nie ma sekcji `## as-marketing`. Nie ruszasz sekcji `## Shared` poza lukami; dopisujesz sekcję `## as-marketing` z szablonu.
   - **Uzupełnienie** — plik i sekcja istnieją. Dopytujesz tylko o pola nadal oznaczone `[required]` lub `unknown`, które blokują pracę.
   Jeśli `Schema version` w istniejącym pliku różni się od wersji w szablonie, zatrzymaj się i opisz różnicę zamiast nadpisywać.
4. Zadaj **jedną rundę pytań** (maks. 5–7, zgrupowanych), wyłącznie o brakujące pola `[required]`. Pola `[optional]` i `[known/unknown]` zostaw na później.
5. Wybierz dokładnie jeden profil z `${CLAUDE_PLUGIN_ROOT}/library/business-model-profiles.md`, respektując „Selection guardrails”. Uzasadnij jednym zdaniem i poproś o potwierdzenie.
6. W tej samej rundzie poproś o trzy zgody, każdą osobno:
   a. **Import kontekstu** — dopisanie linii `@.as/project-context.md` do `CLAUDE.md` projektu (utwórz plik, jeśli nie istnieje). Dzięki temu kontekst trafia do każdej sesji i każdego subagenta. Jeśli linia już jest, nie dopisuj jej drugi raz.
   b. **Dostęp do źródeł projektu** — czy agent `source-reader` może czytać pliki projektu, i jeśli tak, to które katalogi. Domyślnie brak dostępu.
   c. **.gitignore** — dopisanie `.as/private/` i `.as/state/.as-trail.json`.
7. Zapisz pliki (patrz „Wymagany rezultat”).
8. Na końcu pokaż podsumowanie.

## Zasady wykonania

- Nie zaczynaj od pisania plików. Najpierw pytania i zgody.
- Każde niepotwierdzone pole zapisz jako `unknown` i dopisz do `open_questions` w stanie projektu. Zero zgadywania: żadnych domyślnych cen, metryk, segmentów, narzędzi ani wyników.
- Jeśli w repozytorium są materiały opisujące firmę, możesz je przeczytać tylko po udzieleniu zgody 6b i tylko przez agenta `source-reader`. Fakty z nich oznacz źródłem i nadal poproś o potwierdzenie.
- `project-id`: użyj argumentu, jeśli podano; w przeciwnym razie zaproponuj stabilny kebab-case i poproś o potwierdzenie. Jeśli `.as/state/projects/<project-id>.yaml` istnieje — zatrzymaj się i zapytaj.
- Router i owner skill wybierz zgodnie z `as.loading_limits`. Na etapie startu wystarczy rekomendacja routera i owner skilla; specjaliści i workflow zostają puste.
- Nie proponuj zakresów z `as.excluded_domains`.
- Brak odpowiedzi na prośbę o zgodę oznacza brak zgody.

## Wymagany rezultat

1. `.as/project-context.md` — potwierdzone fakty, jawne `unknown`, uzupełnione oba „Last verified”.
2. `.as/access.yaml` — z `${CLAUDE_PLUGIN_ROOT}/engine/templates/access.yaml`. Przy zgodzie: `granted: true`, `granted_by`, `granted_at` (UTC ISO-8601 `Z`) i `read_paths` jako lista katalogów względnych wobec projektu, zakończonych `/`. Bez zgody zostaw `granted: false`.
3. `.as/state/projects/<project-id>.yaml` z `${CLAUDE_PLUGIN_ROOT}/engine/templates/project-state.yaml`, z ustawionymi: `plugin: as-marketing`, `project_id`, `workspace_id`, `title`, `user_goal`, `status: active`, `company_context_path`, `business_model_profile`, `selected_router`, `selected_owner_skill`, `open_questions`, `assumptions`, `next_action`, `updated_at`.
4. Istniejące katalogi `.as/state/audit/`, `.as/notes/`, `.as/outputs/`, `.as/private/`.
5. Zmiany z pkt 6a i 6c, tylko jeśli udzielono zgody.
6. Walidacja: `python3 "${CLAUDE_PLUGIN_ROOT}/engine/validate.py" project-state .as/state/projects/<project-id>.yaml`. Jeśli nie przechodzi, popraw plik i powtórz. Zaraportuj wynik.
7. Podsumowanie w odpowiedzi: (a) kontekst w 5–8 punktach, (b) otwarte pytania i `unknown`, (c) udzielone i nieudzielone zgody, (d) rekomendowany pierwszy obszar pracy z konkretnym następnym krokiem w postaci `/as-marketing:run <zadanie>`.

Nie oznaczaj pracy jako zakończonej, dopóki pliki nie istnieją na dysku, a walidacja nie przejdzie.
