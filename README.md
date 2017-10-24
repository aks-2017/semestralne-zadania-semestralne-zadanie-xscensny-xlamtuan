# Latency Monitoring in Software - Defined Networks

Authors : Alaa M. Allakany, Koji Okamura

Latency in a network is an important parameter that can be utilized by a variety of applications which required QoS policies. Recently, methods for monitoring latency have been introduced. Most of these methods monitor end-to-end path delay (per path) by sending probes requests along the path. These methods led to redundant work and network overhead, which resulting from monitoring multiple paths between each pair of nodes. Moreover, end-to-end probes cannot monitor the delay on path segments (per link) between arbitrary network devices. However, measuring per link delay is challenging. In this paper, we propose a method to measure per link delay in real-time to efficiently apply QoS policies, our method does not require any complementary support from the switching hardware and can avoid redundant work and network overhead. We validate our method using the popular Mininet network emulation environment with Pox controller.

## URL: [Link to source][url]

## Opis článku
V članku sú porovnávané simulátori pre modelovanie SDN ako mininet a
ns-3. V článku sú popı́sané vlastnosti simulátorov a štandardy ktoré tieto
simulátori nasledujú ako aj opis tried v niektorých simulátorov.
Ďalej sú opı́sané topológie nad ktorými sa budú vykonávat’ merania. V
týchto topológiach je napı́saný bandwith a oneskorenia.
Na konci článku je spı́sané zariadenie na ktorom boly simulácie vykonané
a zhrnutie týchto výsledkov.

[url]: <https://dl.acm.org/citation.cfm?id=3095791>
