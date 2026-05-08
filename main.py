from task_manager import TaskManager


manager = TaskManager()

while True:
    menu_input = input(f"Welcome to Task Manager! \nType what you want to do: ")

    if menu_input.lower() == "add":
        title_input = input("What is the name of the task? ")
        priority_input = input("What is the task's priority level (high, med, low)? ")

        manager.add_task(title_input, priority_input)

    elif menu_input.lower() == "list":
        manager.list_tasks()

    elif menu_input.lower() == "complete":
        id_input = int(input("What is the task's ID? "))
    
    elif menu_input.lower() == "exit":
        break