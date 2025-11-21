import uuid
from Planner.models import Task

def input_task():
    return Task(
        id=str(uuid.uuid4()),
        title=input("Title: "),
        subject=input("Subject: "),
        est_hours=float(input("Hours: ")),
        deadline=input("Deadline: "),
        priority=int(input("Priority: "))
    )

def print_tasks(tasks):
    for t in tasks:
        print(t)

def print_progress(summary):
    print(summary)
