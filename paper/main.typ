#set page(
  paper: "a4",
  margin: (x: 1.8cm, y: 2cm),
)

#set text(
  font: "New Computer Modern",
  size: 11pt
)
#set par(
  justify: true,
  leading: 0.52em,
)

#set heading(numbering: "1.")

#show heading.where(level: 1): set block(above: 1.75em, below: 1.5em)

#include "titlepage.typ"

#counter(page).update(1)
#set page(numbering: "1")

= Problemstellung

Es soll ein Text mithilfe von Hashing verarbeitet werden. Dabei werden die einzelnen Worte des Textes in einer Liste der länge $m$ abgebildet.
Der Algorithmus zur Erstellung einer Hashtabelle durchläuft dabei PLATZHALTER Schritte.\
Zunächst muss der gegebene Text in eine Liste der Wörter umgewandelt werden. Dazu werden in Vorbereitung alle Sonderzeichen aus dem Text entfernt. 
An dieser Stelle kann es sich außerdem anbieten, Groß- in Kleinbuchstaben umzuwandel. So wird an späterer Stelle, je nach Umwandlungsverfahren, nicht zwischen einem Wort am Satzanfang oder im Satz unterschieden.
Danach können die Wörter mithilfe der Leerzeichen zwischen ihnen von einander getrennt werden.

```python
text = 'Es war einmal mitten im Winter, und die Schneeflocken.'
```

wird zu:

```python
words = ['es', 'war', 'einmal', 'mitten', 'im', 'winter', 'und', 'die', 'schneeflocken']
```

Im nächsten Schritt kann dann mit der entstandenen Wortliste weitergearbeitet werden. Aus ihr soll eine Hashtabelle erzeugt werden. Dazu wird eine leere Liste der Länge $m$ angelegt. In diese wird dann Schritt für Schritt jedes Wort an die, dem generierten Hashwert entsprechende, Stelle gelegt. Hierbei kann allerdings das Problem auftreten, dass Wörter den gleichen Hashwert haben und somit an die gleiche Stelle in der Liste gehören müssten. Dieses Problem nennt man Adresskolission und tritt bei einer Anzahl von $sqrt((pi m )/ 2)$ Schlüsseln auf einer Hashliste der Größe $m$ zu einer Wahrscheinlichkeit von mehr als 50% auf.
Für den Umgang mit diesem Problem gibt es drei mögliche Lösungsansätze.

Der erste ist das geschlossene Hashing, bei dem mit Sondierungsverfahren nach nächstmöglichen freien Adressen gesucht wird. Allerdings ist dieses Verfahren gänzlich ungeeignet bei mehr Datensätzen als Schlüsseln, da hier keine Hashtabelle entsteht. Die nächsten beiden Verfahren gehören zum offenen Hashing, bei der jeder Hashadresse beliebig viele Schlüssel zugeordnet werden können. Diese Verfahren sind listenbasiert 

Bei der direkten Verkettung enthält jeder Eintrag (oder auch Behälter) der Hashtabelle einen Listenkopf, der auf eine Liste mit Datensätzen gleicher Adresse zeigt.

Die separate Verkettung wiederum enthält pro Behälter maximal einen Datensatz und bei möglichen Überläufen einen Listenkopf der auf die Liste der Überläufer zeigt. 

= Hauptteil
