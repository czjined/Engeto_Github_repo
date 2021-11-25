# Engeto_Scraper
Repository for Engeto final project - Election Scraper.


Popis projektu

Tento projekt slouží k extrahování výsledků z parlamentních voleb v roce 2017. Odkaz k nahlédnutí zde.
Instalace knihoven

Knihovny, které jsou použity v kódu jsou uvedené v souboru requirements.txt. Pro instalaci doporučuji použít nové virtuální prostředí a s nainstalovaným manažerem spustit následovně:
$ pip3 install -r requirements.txt

Spuštění projektu

Spuštění programu election_scraper.py v příkazovém řádku požaduje dva povinné argumenty – odkaz na stránku okresu, který chceme extrahovat a výstupní CSV soubor.

Př.: python election_scraper.py [odkaz územního celku] [výsledný soubor]
Źádané výsledky se stáhnou a uloží jako zadaný soubor s příponou CSV (s možností dalšího zpracováníé ve standardním tabulkovém editor, např. Excel).

Ukázka projektu

Výsledky hlasování pro okres Trutnov:
1.	Argument: https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=8&xnumnuts=5205
2.	Argument: hlasovani2017_trutnov.csv
Konkrétní spuštění program I jeho průběh je znázorněn na následujícím screen shotu:
 
Z obrázku je vidět, že běh programu má několik okomentovaných fází s dílčím uvedením finálního statusu jejich ukončení:
•	Kontrola správnosti zadání vstupních argumentů, konkrétně jejich počet a syntaxe.
•	Dotaz na zadanou webovou stránku za účelem kolekce všech příslušejících obcí, jejich čísel a odkazů.
•	Extrahování kompletní sady informací daného okresu a jejich utřídění do výsledné proměnné.
•	Vytvoření (pokud již v adresáři programu neexistuje) požadovaného výstupního CSV souboru s daty v daném formátu.
•	Ukončení programu s uvedením potřebné doby jeho zpracování.
Pokud dojde při běhu programu k chybě, je tato vypsána ve výstupní konzoli uživateli a program se ukončí bez jakýchkoliv dílčích výsledků, např. pro chybně zadanou adresu:
 
