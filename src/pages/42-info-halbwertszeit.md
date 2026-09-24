---
id: info-halbwertszeit
title: Infotext - Aktivität, Zählrate und Halbwertszeit
nav: B · Infotext - Aktivität, Zählrate, Halbwertszeit
group: Modul II
order: 41
badge: Modul II · Infotext - beide Pfade
mod: 2
---

## Aktivität

In einer radioaktiven Probe zerfallen ständig einzelne instabile Atomkerne. Wie viele Kerne dabei pro Sekunde zerfallen, beschreibt die **Aktivität** $A$ der Probe. Sie ist definiert als Quotient aus der Anzahl der zerfallenen Kerne $\Delta N$ und der dafür benötigten Zeit $\Delta t$:

$$A = \frac{\Delta N}{\Delta t}$$

Die Einheit der Aktivität ist das **Becquerel (Bq)**, benannt nach Henri Becquerel, der 1896 die Radioaktivität entdeckte: $1\,\mathrm{Bq} = 1\ \frac{\text{Zerfall}}{\text{Sekunde}}$. In der Nuklearmedizin sind die Aktivitäten groß, deshalb rechnet man in Megabecquerel (1 MBq = 1 000 000 Bq) oder Gigabecquerel (1 GBq = 1 000 MBq). Zum Vergleich: Der menschliche Körper hat von Natur aus eine Aktivität von etwa 8 000 Bq (vor allem Kalium-40 und Kohlenstoff-14).

| Anwendung | typische Aktivität |
| --- | --- |
| Schilddrüsen-Szintigraphie mit Tc-99m | ≈ 50–80 MBq |
| Skelettszintigraphie mit Tc-99m | ≈ 400–800 MBq |
| Radioiodtherapie mit I-131 (Schilddrüsenkrebs) | ≈ 1 000–7 000 MBq (1–7 GBq) |

## Aktivität ist nicht Zählrate

Die Aktivität darf nicht mit der **Zählrate** $R$ verwechselt werden: Die Zählrate gibt an, wie viele Impulse ein *Messgerät* (Zählrohr, Gammakamera) pro Sekunde registriert. Weil die Strahlung in alle Richtungen ausgesandt wird, trifft nur ein Bruchteil das Messgerät, und nicht jedes Teilchen wird erkannt. Die Zählrate ist daher immer **kleiner** als die Aktivität, aber **proportional** dazu: Halbiert sich die Aktivität, halbiert sich auch die Zählrate. Deshalb kann man die Halbwertszeit aus einer Zählraten-Messung bestimmen.

Bei jeder Messung registriert das Gerät zusätzlich die natürliche Umgebungsstrahlung – den **Nulleffekt** (Nullrate $R_0$). Er muss von der gemessenen Zählrate abgezogen werden.

## Halbwertszeit

Radioaktiver Zerfall ist ein **Zufallsprozess**: Für einen einzelnen Atomkern lässt sich nicht vorhersagen, wann er zerfällt. Bei einer sehr großen Anzahl von Kernen lässt sich aber sehr genau vorhersagen, wie viele davon in einem bestimmten Zeitraum zerfallen (das habt ihr in der Würfelsimulation gesehen).

Die Zeitspanne, nach der die **Hälfte** der ursprünglich vorhandenen radioaktiven Kerne zerfallen ist, heißt **Halbwertszeit** $T_{1/2}$. Nach einer Halbwertszeit ist noch die Hälfte der Kerne vorhanden, nach zwei Halbwertszeiten ein Viertel, nach drei ein Achtel usw. Mit der Anzahl der Kerne nimmt auch die Aktivität ab – nach jeder Halbwertszeit halbiert sie sich.

Jedes Radionuklid besitzt eine charakteristische Halbwertszeit. Sie reicht von Sekundenbruchteilen bis zu Milliarden von Jahren:

| Nuklid | Halbwertszeit | Rolle in dieser Einheit |
| --- | --- | --- |
| Polonium-214 (Po-214) | 0,16 ms | Radon-Zerfallskette (Modul IV) |
| Technetium-99m (Tc-99m) | ≈ 6 Stunden | Szintigraphie (Pfad 1) |
| Iod-131 (I-131) | ≈ 8 Tage | Radioiodtherapie (Pfad 2) |
| Cäsium-137 (Cs-137) | ≈ 30 Jahre | Reaktorunfälle |
| Uran-238 (U-238) | ≈ 4,5 Milliarden Jahre | Ausgangsmaterial für Reaktoren und Kernwaffen |

!!! warnung "Halbwertszeit ist kein Gefahrenmaß"
    Die Halbwertszeit sagt **nichts** darüber aus, ob eine Strahlung gefährlich ist – sie sagt nur, wie schnell die Aktivität abnimmt. Bei gleicher Anzahl Kerne bedeutet eine *kurze* Halbwertszeit eine *hohe* Aktivität (viele Zerfälle pro Sekunde, aber kurz), eine *lange* Halbwertszeit eine *niedrige* Aktivität (wenige Zerfälle pro Sekunde, aber lange).


!!! zusatz "Zum Weiterdenken: Die Formel (optional)"
    Sind zu Beginn $N_0$ Kerne vorhanden, so gilt für die Anzahl der nach der Zeit $t$ noch nicht zerfallenen Kerne:

    $$N(t) = N_0 \cdot \left(\tfrac{1}{2}\right)^{t / T_{1/2}} \qquad\text{und ebenso}\qquad A(t) = A_0 \cdot \left(\tfrac{1}{2}\right)^{t / T_{1/2}}$$

    Beispiel: 3,7 GBq I-131 nach 64 Tagen: $3{,}7\ \mathrm{GBq} \cdot \left(\tfrac{1}{2}\right)^{8} \approx 14\ \mathrm{MBq}$ – ohne Ausscheidung.

!!! info "Weiterlesen"
    [LEIFIphysik – Halbwertszeit](https://www.leifiphysik.de/kern-teilchenphysik/radioaktivitaet-einfuehrung/grundwissen/halbwertszeit) · [LEIFIphysik – Aktivität](https://www.leifiphysik.de/kern-teilchenphysik/radioaktivitaet-einfuehrung/grundwissen/aktivitaet)

