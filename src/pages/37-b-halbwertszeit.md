---
id: b-halbwertszeit
title: Pfad 2 · Station 2 – I-131: Zerfall und Halbwertszeit
nav: B2 · Station 2 · Zerfall und Halbwertszeit
group: Modul II
order: 38
badge: Modul II · Pfad 2 · Station 2
mod: 2
---

Eure Patientin überlegt, warum sie nach der Radioiodtherapie einige Tage im Krankenhaus bleiben muss. 

!!! info "Radionuklide in der Radioiodtherapie"
    Bei der Radioiodtherapie wird das radioaktive Nuklid **Iod-131** ($^{131}\mathrm{I}$) geschluckt. I-131 hat eine **Halbwertszeit** von nur etwa 8 Tagen.

Mit Würfeln könnt ihr zentrale Aspekte des radioaktiven Zerfalls simulieren: Wie nimmt die Menge des noch vorhandenen radioaktiven Materials ab – und warum gerade so?


# Würfelsimulation

**Material:** etwa 30 Würfel und ein Würfelbecher. Ohne Würfel: Online-Würfel, z. B. [wuerfel.virtuworld.net](https://wuerfel.virtuworld.net/?nr=30) (Anzahl einstellen).

!!! info "Die Analogien"
    - Die **Anzahl der Würfel** entspricht der Anzahl der zu Beginn vorhandenen radioaktiven Kerne.
    - Ein **Wurf** entspricht einem Zeitschritt $\Delta t$.
    - Die **verbleibenden Würfel** entsprechen den noch nicht zerfallenen Kernen.
    - Die nach einem Wurf **entfernten Würfel** entsprechen den zerfallenen Kernen.

## Durchführung 

1. Würfelt mit allen Würfeln. Nach jedem Wurf entfernt ihr alle Würfel mit der Augenzahl **6** und notiert die Anzahl der verbleibenden Würfel. Würfelt mit den verbliebenen Würfeln weiter, bis kein Würfel mehr übrig ist.

| Wurf Nr. | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Würfel vor dem Wurf | 30 | | | | | | | | | | | | | | |
| entfernte Würfel (Sechsen) | – | | | | | | | | | | | | | | |
| verbleibende Würfel | 30 | | | | | | | | | | | | | | |

## Auswertung

2. Erstellt ein $x$‑$y$‑Diagramm: Anzahl der Würfe auf der $x$‑Achse, verbleibende Würfel auf der $y$‑Achse. Beschreibt, wann besonders viele Würfel entfernt werden müssen (also viele Kerne zerfallen) und wann wenige. Erklärt, warum das so ist.
3. Lest den [Infotext Aktivität, Zählrate und Halbwertszeit](#info-halbwertszeit). Bestimmt aus eurem Diagramm die „Halbwertszeit“ eurer Würfelprobe in Würfen: Nach wie vielen Würfen ist nur noch die Hälfte übrig? Nach wie vielen weiteren Würfen nur noch ein Viertel?
4. Beschreibt, was man unter der Aktivität einer Probe versteht und in welcher Einheit sie angegeben wird. Was entspricht in der Würfelsimulation der Aktivität?


## Deutung im Kontext

5. Das folgende Diagramm zeigt die gemessene Zählrate einer Iod-Probe. Bestätigt, dass die Probe tatsächlich eine Halbwertszeit von etwa 8 Tagen hat. Prüft an zwei verschiedenen Startpunkten. 

![Diagramm: N(t) fällt von 48 bei t = 0 auf 24 bei t = 8 Tagen und auf 12 bei t = 16 Tagen](assets/i131_kurve.jpg "Abklingkurve einer Iod-131-Probe (t in Tagen, N in willkürlichen Einheiten)"){: width=520 }

6. Von der eingenommenen Menge Iod-131 wird nur etwa 20-40 % in der Schilddrüse aufgenommen, der Rest wird über Urin und Schweß innerhalb von 24-48 Stunden ausgeschieden. Eure Patientin darf nach einigen Tagen nach Hause – obwohl nichtmal die Hälfte des Iods zerfallen ist. Erklärt, warum die Entlassung trotzdem möglich ist.
7. Eure Patientin bekommt eine Kapsel mit einer Aktivität von 3 700 MBq. Berechne (ausgehend von den Angaben in Aufgabe 6), welche Aktivität nach 8, 16, 24, 32 und 64 Tagen näherungsweise noch vorhanden ist. 

!!! zusatz "Zum Weiterdenken: Warum ist es Zufall – und trotzdem vorhersagbar? (optional)"
    Ob ein einzelner Würfel eine Sechs zeigt, ist reiner Zufall. Bei 30 Würfeln kann man trotzdem gut vorhersagen, dass etwa 5 entfernt werden müssen ($30 \cdot \tfrac{1}{6}$). Bei radioaktiven Kernen ist es genauso: Für den einzelnen Kern ist der Zerfallszeitpunkt nicht vorhersagbar, für die Milliarden Kerne einer echten Probe gilt die Halbwertszeit sehr genau. Erklärt, warum die Menge an Iod-131 im Körper eurer Patientin mit der Halbwertszeit allein nur *näherungsweise* angegeben werden kann. 

!!! Zum Weiterdenken "Warum die Halbwertszeit für die Therapie passt (optional)"
    Ein Nuklid mit *sehr kurzer* Halbwertszeit (wie Tc-99m mit 6 h) wäre für die Therapie schon zerfallen, bevor die Schilddrüse das Iod vollständig aufgenommen hat. Ein Nuklid mit *sehr langer* Halbwertszeit würde über Monate im Körper strahlen und die Umgebung belasten. Acht Tage sind ein Kompromiss: lange genug, um die Krebszellen über einige Wochen zu bestrahlen, kurz genug, dass nach zwei Monaten fast nichts mehr übrig ist.


