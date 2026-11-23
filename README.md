# Księga zleceń

Prosty program w Pythonie do zapisywania zleceń firmy i generowania raportu.

## Co robi
- `zapis.py` dopisuje zlecenia (usługa, cena, data) do pliku tekstowego
- `raport.py` wczytuje plik i liczy liczbę zleceń, sumę oraz najdroższe zlecenie
- obsługuje błędne dane (zła cena, brak pliku, uszkodzone linie)

## Jak uruchomić
1. Zainstaluj Pythona 3
2. `python zapis.py`, aby dodać zlecenia
3. `python raport.py`, aby zobaczyć raport

## Czego użyłem
Python, pliki, funkcje, `try / except`, moduł `datetime`, Git i GitHub.