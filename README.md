# Teilbarkeit – Arbeitsblatt für einen Lern-Agenten

Dieses Verzeichnis enthält ein deutsches Mathematik-Trainingsblatt für Klasse 5–6.

## Dateien

- [`Mathe-Trainingsblatt-Teilbarkeit.md`](Mathe-Trainingsblatt-Teilbarkeit.md): Aufgaben, Lösungsteil, Merkhilfe und kurzer Beweis zur Teilbarkeit durch 3.
- [`brainstorming.md`](brainstorming.md): Konzept für den ersten Detektivfall und seine Lernziele.
- [`story-1.md`](story-1.md): „Die drei ??? und das Geheimnis der letzten Kiste“ – abgeschlossene Geschichte mit allen für die Arbeitsblätter benötigten Regeln.
- [`Mathe-Arbeitsblatt-Teilbarkeit-2.md`](Mathe-Arbeitsblatt-Teilbarkeit-2.md): Neues Arbeitsblatt mit anderen Zahlen, ohne Lösungen, zum separaten Ausdrucken.
- [`Mathe-Loesungen-Teilbarkeit-2.md`](Mathe-Loesungen-Teilbarkeit-2.md): Separates Lösungsblatt zu Variante 2.

Die Geschichte und die Arbeitsblätter sind separate Dokumente. Nach der Geschichte kann eines der Arbeitsblätter bearbeitet werden. Die nächste Geschichte behandelt ein neues Mathethema.

## PDFs zum Ausdrucken erstellen

Voraussetzungen: Python, `uv`, Pandoc und XeLaTeX (zum Beispiel aus MacTeX).
Das Python-Paket in `requirement.txt` bindet das separat installierte Pandoc ein.

Einmalig im Projektverzeichnis einrichten:

```sh
uv venv .venv
uv pip install --python .venv/bin/python -r requirement.txt
```

Geschichte, Arbeitsblatt und Lösungen als drei getrennte PDFs erzeugen:

```sh
uv run --no-project --python .venv/bin/python scripts/markdown_to_pdf.py \
  story-1.md \
  Mathe-Arbeitsblatt-Teilbarkeit-2.md \
  Mathe-Loesungen-Teilbarkeit-2.md
```

Die A4-Dateien liegen anschließend in `pdf/`. Vorhandene PDFs mit demselben
Namen werden nach erfolgreicher Konvertierung ersetzt. Die Markdown-Dateien
bleiben unverändert. Es ist keine Aktivierung der virtuellen Umgebung nötig.

Einzelne Datei oder anderes Zielverzeichnis:

```sh
uv run --no-project --python .venv/bin/python scripts/markdown_to_pdf.py story-1.md --output-dir druck
```

## Verwendung im Agenten

Gib dem Agenten die README und das gewünschte Arbeitsblatt als Kontext oder lege sie in sein Projektverzeichnis. Bei Variante 2 kann das separate Lösungsblatt zur Kontrolle hinzukommen. Der Agent soll das Trainingsblatt als Aufgabenquelle nutzen, die Lösungen aber **nicht ungefragt verraten**.

### Beispiel-Prompt für den Agenten

```text
Du bist ein freundlicher Mathe-Lernbegleiter für Klasse 5–6.
Verwende Mathe-Trainingsblatt-Teilbarkeit.md als Aufgabenquelle.
Stelle immer nur eine Aufgabe oder Teilaufgabe auf einmal.
Warte auf meine Antwort und prüfe sie sorgfältig.
Wenn die Antwort falsch ist, gib zuerst einen kleinen Hinweis,
dann einen weiteren Hinweis und erst auf Wunsch die Lösung.
Erkläre Teilbarkeitsregeln mit einfachen Beispielen.
Bei Beweisen prüfe insbesondere, ob die Argumentation logisch ist
und ob sie nur eine oder beide Richtungen beweist.
Zeige den Lösungsteil des Blatts nicht ohne Aufforderung.
Erzeuge auf Wunsch neue, ähnlich schwierige Aufgaben mit
separaten, rechnerisch geprüften Lösungen.
Antworte auf Deutsch.
```

## Hinweise zum Bearbeiten

1. Für ein Arbeitsblatt **ohne Lösungen** den Abschnitt `# Lösungen (für Lehrkräfte / Selbstkontrolle)` und alles danach entfernen (oder die Merkhilfe separat übernehmen).
2. Für neue Varianten Zahlen und Ziffern austauschen, aber die Teilbarkeit jeder Zahl und die Beispielantworten vor Ausgabe prüfen.
3. Markdown lässt sich direkt in GitHub, Cursor, VS Code oder vielen Agent-Workspaces öffnen.
4. Die mathematische Kurzbegründung am Ende des Blatts zeigt **beide Richtungen** der Quersummenregel für dreistellige Zahlen.
