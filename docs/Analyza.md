# Latency Monitoring in Software-Defined Networks

##### Patrik Sčensný, Lam Tuan Anh              
##### Cvičiaci: Tomáš Boros, Utorok 16:00

# Úvod
V článku autori navrhujú novú metódu na zistenie topológie siete, minimálnu kostru siete a monitorovanie latencie v siete. 
Autori prezentujú svoju metódu založenú na OpenFlow s POX kontrolérom. Nimi navrhnutá architektúra a funkcionalita jednotlivých modulov je nasledovná: modul ktorý zisťuje topológiu pomocou Link Layer Discovery Protocol (LLDP), vytvorenie minimálnej kostry topológie, monitorovanie latencie medci jednotlivými úrovniami siete a výpočet oneskorenia medzi jednotlivými uzlami. Výsledky zistení porovnávajú s už existujúcim nástrojom OPENNETMON. Topológia použitá na testovanie bola generovaná v BRITE.


# Analýza

## Software defined network (SDN)
je metóda používania otvorených protokolov ako napr.: OpenFlow, na prístup k smerovačom a prepínačom ktoré by normálne používaly uzavretý a vlastný firmvér. Softvérové definované siete ponúkajú množstvo výhod, medzi ktoré patrí poskytovanie služieb na požiadanie, automatické vyvažovanie záťaže, zjednodušená fyzická infraštruktúra a schopnosť škálovať sieťové zdroje v zámke s potrebami aplikácií a dát. V spojení s prebiehajúcou virtualizáciou serverov a úložných priestorov, SDN uvádza najmenej úplne virtualizované dátové centrum, kde sa budú rozmiestňovať koncové počítačové prostredia a vyradiť ich z prevádzky.[^1]
 ![trad-SDN](https://image.slidesharecdn.com/ryu-sdn-framework-upload-130914010856-phpapp01/95/ryu-sdn-framework-7-638.jpg?cb=1379121452)

## OpenFLow
Jedna z najstarších noriem definovaných SDN. Definoval komunikačný protokol v SDN prostredí, umožnuje kontrolóru priamo komunikovať s vrstvou preposielacích zariadení ako prepínače a smerovače, aby sa mohli lepšie prispôsobiť meniacim sa obchodným požiadavkám. [^2]

## Mininet
Mininet je virtuálne prostredie pre prepínače, prepojenia a kontroléry ktoré sú vytvorené pomocou softvéru než hardvéru a ich správanie je podobné ich reálnym reprezentáciam. Pomocou Mininet prostredia je možné simulovať sieť ktorá sa podobá alebo je totožná ako reálna sieť. Vďaka jeho otvorenosti je možné nasimulovať iba softvérovo navrhnutú diskrétnu harvérový prvok.[^3]

## Pox controller
POX je sieťová softvérová platforma napísaná v jazyku Python POX začal fungovať ako kontrolér OpenFlow, ale teraz môže fungovať aj ako prepínač OpenFlow a môže byť užitočný pri písaní sieťového softvéru všeobecne.[^4]

## QoS
Siete musia poskytovať zabezpečené, predvídateľné, merateľné a niekedy zaručené služby. Dosiahnutie požadovanej kvality služby (QoS) riadením oneskorenia, odchýlky oneskorenia (jitter), šírky pásma a parametrov straty paketov v sieti sa stáva tajomstvom úspešného podnikového riešenia od konca. Takže QoS je súbor techník na správu sieťových zdrojov.[^5]

[^1]: https://www.webopedia.com/TERM/S/software_defined_networking.html
[^2]: https://www.sdxcentral.com/sdn/definitions/what-is-openflow/
[^3]: https://github.com/mininet/mininet/wiki/Introduction-to-Mininet#what
[^4]: https://github.com/noxrepo/pox
[^5]: https://www.cisco.com/c/en/us/products/ios-nx-os-software/quality-of-service-qos/index.html








