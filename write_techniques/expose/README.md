# Expose


[Expose form 1](https://www.bachelorprint.de/expose-beispiel/)

Einführung

Das Ziel jedes Unternehmens ist es Aufgaben zu zentralisieren, um schneller zu gewünschten Ergebnissen zu kommen. Dabei ist oft die technische Kommunikation zwischen einzelnen Abteilungen ein großes Hindernis. Verschiedene Schnittstellen erschweren das Arbeitsleben. Eine der größten Fehlerquellen im Arbeitsalltag sind jedoch sich immer wiederholende Arbeitsprozesse. Die Schwierigkeit besteht darin, menschliche Fehler zu minimieren. Man bräuchte voll autonome Computersysteme, die den Mitarbeiter entlasten, und verschiedene Arbeitsprozesse alleine bewältigen.

Problem

Bei der Bestellung von Einzelteilen für alle möglichen Varianten von Bussen ist der Aufwand sehr hoch gewesen. Bis vor ein paar Monaten wurde ein Auftrag noch in diesen Arbeitsschritten bewältigt: Zuerst wurde der Bestand geprüft, falls man nicht fündig wurde, hat man danach den Auftrag an die Lieferanten weitergeleitet. Dabei sind lange Wartezeiten entstanden, da für die jeweiligen Lieferanten der Auftrag keine hohe Priorität hatte. Deshalb hat das Unternehmen sich entschieden mit neuesten 3D Druckern, das Problem an einem zentralen Ort zu bewältigen.

Wie so oft sind neue Probleme aufgetreten. Die Kommunikation mit Vertrieb und Betrieb ist sehr problematisch. Die gespeicherten Daten sind redundant und inkonsistent. Für die Bewältigung braucht ein Ingenieur mehrere Stunden. Die Arbeit birgt ein hohes Risiko für Flüchtigkeitsfehler. Die Komplexität ist nicht hoch, aber man braucht eine hohe Konzentration und muss mehrere Daten abgleichen. Momentan sind es über 350.000 Teile und es kommen ca. 10 Teile pro Tag hinzu. Die Arbeit ist sehr verhasst und in mehreren Gesprächen mit den zuständigen Personen war der Wunsch hoch, einen Sammelpunkt für die Ersatzteile zu haben.

Ich habe einen Prototyp entwickelt, der die Machbarkeit der verschiedenen Use Cases zeigen sollte. Dabei war es durch die verschiedene Sicherheitsprotokolle in den ersten Wochen sehr schwer Zugänge zu allen Applikationen zu bekommen. Die betriebsinterne VM war auch kein Garant dafür Tag und Nacht fehlerfrei zu laufen.

Zu Beginn des Projektes war ich auch gewillt ein RPA Tool zu verwenden, wie z.B. Workfusion, Ranorex und UIPath. Nach einer Woche mit den verschiedenen Tools war die Bedienung aufwendiger als gedacht. Nach Besprechung mit meinem Chef wurde beschlossen das RPA Tool vorzuschieben. Ursprünglich war es geplant, die Realisierung erst in 2 bis 3 Monaten zu starten

Lösung

Zu Beginn liegt der Schwerpunkt darin, die Arbeitsschritte mit Hilfe eines Programmes zu wiederholen und dies auf Video festzuhalten. Dabei sollen auch verschiedene Problematiken dokumentiert werden, um den Ablauf des Prozesses zu vertiefen. Die Kommunikation mit den Kunden hat die höchste Priorität, damit am Schluss auch der Kunde mit dem Endprodukt zufrieden ist.
Die Umsetzung auf technischer Ebene wird mit Python realisiert. Um Problematiken in den verschiedenen Use Cases vom Kunden abzuarbeiten werden Hilfs-Bibliotheken benutzt, wie zum Beispiel Keras (Maschinelles Lernen) oder Tesseract (OCR um aus technischen Zeichnungen Daten herauszulesen). Für die Steuerung der Bedienelemente im Programm habe ich das Modul PyAutoGui gewählt.
Die Infrastruktur, wie Kommunikation, Git, Pipeline, Coding Standards, usw., wurde von Anfang an von mir festgelegt, um das erlernte Wissen von LSD (Large scale development) und AGI (Agile Prozesse) im letzten Semester anzuwenden.
Das Ziel ist es ein Programm zu entwickeln (RPA), das selbständig auch dazu lernt und anhand von Informationen aus der Bildverarbeitung nächste Schritte ausführt.




Module entwickelt
OOP
coding standards
generators
comphrensive list
numpy

Schnittstellen mit Indien
Dockerisierung
-> REDIS
Pipeline
Struktur
XP Techniken
-> PAIR programming
-> TDD
Agile Verfahren
-> Scrum Techniken
Kanban BOARD

libaries
Optical Character Recognition (OCR).
tesseract
pyautogui

PLUS DOCUMENTATION
Toolbox