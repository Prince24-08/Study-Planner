import json
from pathlib import Path
from .models import Task

FILE = Path("tasks.json")

def load_tasks():
    if not FILE.exists():
        return []
    return [Task.from_dict(d) for d in json.load(open(FILE))]

def save_tasks(tasks):
    json.dump([t.to_dict() for t in tasks], open(FILE,'w'), indent=2)
