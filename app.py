from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
import uvicorn
import random
import json

app = FastAPI(
    title="Python Demo App",
    description="Eine einfache Demo-Anwendung mit FastAPI",
    version="1.0.0"
)

# Pydantic Modelle
class Task(BaseModel):
    id: int = None
    title: str
    description: str = ""
    completed: bool = False
    created_at: datetime = None

class Quote(BaseModel):
    text: str
    author: str

# In-Memory Datenbank
tasks = []
task_counter = 0

quotes = [
    Quote(text="Das Leben ist wie Programmieren - manchmal funktioniert es, manchmal nicht.", author="Anonymous Developer"),
    Quote(text="Code ist Poesie in Bewegung.", author="Tech Philosoph"),
    Quote(text="Debugging ist wie ein Detektivspiel, bei dem Sie sowohl der Detektiv als auch der Mörder sind.", author="Coding Wisdom")
]

@app.get("/")
async def root():
    """Willkommensseite der Demo-App"""
    return {
        "message": "Willkommen zur Python Demo App!",
        "endpoints": {
            "/docs": "API Dokumentation",
            "/tasks": "Aufgaben verwalten",
            "/quote": "Zufällige Zitate",
            "/time": "Aktuelle Zeit",
            "/health": "System Status"
        }
    }

@app.get("/health")
async def health_check():
    """System Health Check"""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "version": "1.0.0"
    }

@app.get("/time")
async def get_current_time():
    """Aktuelle Zeit abrufen"""
    return {
        "current_time": datetime.now().isoformat(),
        "timezone": "UTC"
    }

@app.get("/quote")
async def get_random_quote():
    """Zufälliges Zitat abrufen"""
    quote = random.choice(quotes)
    return quote

@app.get("/tasks")
async def get_tasks():
    """Alle Aufgaben abrufen"""
    return {"tasks": tasks, "count": len(tasks)}

@app.post("/tasks")
async def create_task(task: Task):
    """Neue Aufgabe erstellen"""
    global task_counter
    task_counter += 1
    task.id = task_counter
    task.created_at = datetime.now()
    tasks.append(task)
    return {"message": "Aufgabe erstellt", "task": task}

@app.get("/tasks/{task_id}")
async def get_task(task_id: int):
    """Spezifische Aufgabe abrufen"""
    task = next((t for t in tasks if t.id == task_id), None)
    if not task:
        raise HTTPException(status_code=404, detail="Aufgabe nicht gefunden")
    return task

@app.put("/tasks/{task_id}")
async def update_task(task_id: int, updated_task: Task):
    """Aufgabe aktualisieren"""
    task = next((t for t in tasks if t.id == task_id), None)
    if not task:
        raise HTTPException(status_code=404, detail="Aufgabe nicht gefunden")
    
    task.title = updated_task.title
    task.description = updated_task.description
    task.completed = updated_task.completed
    return {"message": "Aufgabe aktualisiert", "task": task}

@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    """Aufgabe löschen"""
    global tasks
    task = next((t for t in tasks if t.id == task_id), None)
    if not task:
        raise HTTPException(status_code=404, detail="Aufgabe nicht gefunden")
    
    tasks = [t for t in tasks if t.id != task_id]
    return {"message": "Aufgabe gelöscht"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)