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

add_task("Arise Beru", 1)

add_task("Arise Beru", -2)

save_tasks([{"name": "Arise Beru", "priority": 1}])
