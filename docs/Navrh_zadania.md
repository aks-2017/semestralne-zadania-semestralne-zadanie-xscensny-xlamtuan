# Navrh

Planujeme postupovať rovnakou metodológiou ako autori článku, ale v našom riešení chceme upraviť niektoré vlastnosti a funkcionalitu. Potom by sme radi porovnali a overili výsledky ich práce.
 1. Inštalácia prostredia v ktorom sa bude overovanie odohrávať: mininet ktorý bude priamo nainštalovaný na Ubuntu distribúcií Linuxu
 2. Vytvorenie rovnakej architektúry aká je navrhnutá autormi článku
 ![archi]()
 2. Použitie LLDP protokolu na zistenie topológie vygenerovanej siete
 3. Tree construction module - chceme zmeniť Djikstrov algoritmus ktorý bol použitý, za iný vhodný algoritmus napr.: Bellman-Ford alebo A*. Budeme ale porovnávať rozdiel medzi týmito algorimami.
 4. Posielanie packetu zo začiatku na koniec siete
 5. Zmena a porovnanie spôsobu výpočtu oneskorenia v spojeniach
 6. Generovanie topológií pomocou Brite nástroja
 7. Testovanie a následne porovnanie zvolených metód
 
# Použité nástroje
 1. Mininet
 2. POX kontrolér
 3. Brite
