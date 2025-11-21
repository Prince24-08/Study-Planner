from Planner.storage import load_tasks, save_tasks
from Planner import logic, ui

MENU = """
=== Smart Study Planner ===
1) Add Task
2) View Tasks
3) Suggest Study Plan
4) Show Progress & Analytics
5) Mark Task Completed
6) Exit
Choose: """

def main():
    while True:
        choice = input(MENU)
        tasks = load_tasks()

        if choice == '1':
            task = ui.input_task()
            tasks.append(task)
            save_tasks(tasks)
            print("Task added.")

        elif choice == '2':
            ui.print_tasks(tasks)

        elif choice == '3':
            plan = logic.suggest_schedule(tasks, 7, 3)
            print(plan)

        elif choice == '4':
            summary = logic.compute_progress(tasks)
            ui.print_progress(summary)

        elif choice == '5':
            tid = input("Enter task id: ")
            for t in tasks:
                if t.id == tid:
                    t.status = "Completed"
            save_tasks(tasks)
            print("Task marked completed.")

        elif choice == '6':
            break

if __name__ == "__main__":
    main()
