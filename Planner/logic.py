def suggest_schedule(tasks, days, hrs):
    return {t.id: t.est_hours for t in tasks if t.status != 'Completed'}

def compute_progress(tasks):
    total = len(tasks)
    completed = len([t for t in tasks if t.status == 'Completed'])
    pending = total - completed
    return {"total": total, "completed": completed, "pending": pending}
