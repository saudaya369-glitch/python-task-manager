def add_task(name: str,priority: int) -> None:
    if name == "":
        print("Task name cannot be empty.")
        return
    if priority < 0:
        print("Priority cannot be negative.")
        return 
    print(f"Task added: {name} with priority {priority}")












add_task("Buy groceries", 2)
add_task("", 2)
add_task("Buy groceries", -1)