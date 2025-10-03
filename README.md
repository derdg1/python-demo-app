# Python Demo App

Eine einfache Demo-Anwendung mit FastAPI, die verschiedene grundlegende Web-API-Funktionen demonstriert.

## Funktionen

- ✅ REST API mit FastAPI
- ✅ Aufgaben-Management (CRUD-Operationen)
- ✅ Zufällige Zitate
- ✅ System Health Check
- ✅ Zeitabfragen
- ✅ Automatische API-Dokumentation

## Installation

1. Repository klonen:
```bash
git clone https://github.com/derdg1/python-demo-app.git
cd python-demo-app
```

2. Virtuelle Umgebung erstellen:
```bash
python -m venv venv
source venv/bin/activate  # Auf Windows: venv\\Scripts\\activate
```

3. Abhängigkeiten installieren:
```bash
pip install -r requirements.txt
```

## Ausführung

```bash
python app.py
```

Die Anwendung läuft dann auf `http://localhost:8000`

## API-Dokumentation

Nach dem Start der Anwendung können Sie die automatische API-Dokumentation unter folgenden URLs einsehen:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## API-Endpoints

### Grundlegende Endpoints
- `GET /` - Willkommensseite
- `GET /health` - System Status
- `GET /time` - Aktuelle Zeit
- `GET /quote` - Zufälliges Zitat

### Aufgaben-Management
- `GET /tasks` - Alle Aufgaben abrufen
- `POST /tasks` - Neue Aufgabe erstellen
- `GET /tasks/{task_id}` - Spezifische Aufgabe abrufen
- `PUT /tasks/{task_id}` - Aufgabe aktualisieren
- `DELETE /tasks/{task_id}` - Aufgabe löschen

## Beispiel-Nutzung

### Neue Aufgabe erstellen:
```bash
curl -X POST "http://localhost:8000/tasks" \\
     -H "Content-Type: application/json" \\
     -d '{
       "title": "Demo Aufgabe",
       "description": "Das ist eine Test-Aufgabe",
       "completed": false
     }'
```

### Alle Aufgaben abrufen:
```bash
curl "http://localhost:8000/tasks"
```

## Docker

Die App kann auch mit Docker ausgeführt werden:

```bash
docker build -t python-demo-app .
docker run -p 8000:8000 python-demo-app
```

## Technologie-Stack

- **Framework**: FastAPI
- **Server**: Uvicorn
- **Datenvalidierung**: Pydantic
- **Python**: 3.8+

## Entwicklung

Diese Demo-App zeigt grundlegende Konzepte für moderne Python-Web-APIs:

- RESTful API Design
- Automatische Dokumentation
- Datenvalidierung mit Pydantic
- Asynchrone Programmierung
- Error Handling
- In-Memory Datenspeicherung

## Lizenz

MIT License