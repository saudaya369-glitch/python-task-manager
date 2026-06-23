import json
def add_task(name: str,priority: int) -> dict:
    if name.strip() == "":
        print("Task name cannot be empty.")
        return {}
    if priority > 7:
        print("Priority cannot be greater or equal to 7.")
        return {}
    if priority < 0:
        print("Priority cannot be negative.")
        return {}
    return {"name": name,"priority": priority}
def save_tasks(tasks: list) -> None:
    with open("tasks.json", "w") as f:
        f.write(json.dumps(tasks))


def load_tasks():
    try:
        with open("tasks.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []
print(load_tasks())

while True:
    print("1. Add task")
    print("2. View tasks")
    print("3. Quit")
    choice = input("Choose: ")
    if choice == "1":
        name = input("Task name: ")
        priority = int(input("Priority: "))
        tasks = load_tasks()
        new_task = add_task(name, priority)
        if new_task:
            tasks.append(new_task)
            save_tasks(tasks)
    elif choice == "2":
        print(load_tasks())
    elif choice == "3":
        break
