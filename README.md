# Stromverbrauchsprognose mit Prophet

Dieses Projekt analysiert und prognostiziert den Stromverbrauch auf Basis historischer Verbrauchsdaten mithilfe des Facebook Prophet Modells. Es demonstriert den vollständigen Workflow eines Data-Engineering-Projekts mit strukturierter Codebasis, CI/CD und Visualisierung der Ergebnisse.

## Ausführung

### Lokal starten

1. **Abhängigkeiten installieren:**
   
   Stelle sicher, dass Python 3.x und pip auf deinem System installiert sind. Installiere dann alle benötigten Abhängigkeiten:

   `pip install -r requirements.txt`

2. **Hauptskript ausführen:**

   Nach der Installation kannst du das Hauptskript ausführen, um das Modell zu trainieren und die Vorhersage zu visualisieren:

   `python main.py`

   Der Plot wird automatisch in `outputs/forecast_plot.png` gespeichert.

## CI/CD Pipeline (GitHub Actions)

Dieses Projekt nutzt GitHub Actions für die Automatisierung von Tests, Build und Deployment. Bei jedem Push auf den `master`-Branch wird die Pipeline ausgelöst, die Folgendes durchführt:

- Das Projekt wird gebaut.
- Das Modell wird trainiert und evaluiert.
- Der Vorhersage-Plot wird erstellt und gespeichert.

Die Pipeline ist in der Datei `.github/workflows/ci.yml` definiert.

## Struktur

Das Projekt besteht aus mehreren Python-Skripten und verwendet eine saubere Ordnerstruktur. Die Hauptdateien sind:

- **main.py**: Der Einstiegspunkt des Projekts, der das Modell trainiert, evaluiert und visualisiert.
- **src/train.py**: Trainiert das Prophet-Modell mit den Trainingsdaten.
- **src/evaluate_model.py**: Bewertet das Modell anhand von Testdaten und berechnet Metriken wie MAE und RMSE.
- **src/plotting.py**: Visualisiert die Vorhersagen und speichert die Diagramme.
- **data/**: Enthält die Eingabedaten, die für das Training und die Tests verwendet werden.
- **outputs/**: Enthält die visualisierten Plots und andere Ausgabe-Dateien.

## Installation

1. Klone das Repository:

   `git clone https://github.com/Azneo/stromverbrauch.git`

2. Navigiere in das Projektverzeichnis:

   `cd stromverbrauch`

3. Installiere die benötigten Pakete:

   `pip install -r requirements.txt`

## Anforderungen

- Python 3.7 oder höher
- Die folgenden Python-Bibliotheken sind erforderlich:
  - pandas
  - matplotlib
  - fbprophet
  - scikit-learn

## Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert – siehe [LICENSE](LICENSE) für Details.

## Kontakt

Für Fragen oder Anmerkungen kannst du mich erreichen unter: aziz.ishankhodschaev@gmail.com
