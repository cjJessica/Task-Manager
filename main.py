from task_manager import TaskManager


manager = TaskManager()
instructions = """
Welcome to Task Manager!
    - If you want to add a task type 'add'
    - If you want to delete a task type 'delete'
    - If you want to check off a task type 'complete'
    - If you want to list all your tasks type 'list'
"""
menu_input = input(f"{instructions} \nType what you want to do: ")


while True:


    if menu_input.lower() == "add":
        priority_levels = ["high", "med", "low"]
        title_input = input("What is the name of the task? ")
        priority_input = input(f"What is the task's priority (high, med, low)? ")

        
        while priority_input.lower() not in priority_levels:
            priority_input = input(f"\nPlease type one of the following: \n{priority_levels} \n")

        manager.add_task(title_input, priority_input)


    elif menu_input.lower() == "list":
        print("\n" + " TASKS ".center(34, "="))
        manager.list_tasks()


    elif menu_input.lower() == "complete":
        id_input = int(input("What is the task's ID? "))
        if manager.complete_task(id_input):
            print("The task has been checked off!")
        
        while manager.complete_task(id_input) == False:
            id_input = input("Sorry, none of the tasks has that ID number.\n Please enter a correct ID number or type 'menu' to go back: ")
            if id_input.lower() == 'menu':
                break
            else:
                manager.complete_task(id_input)

    
    elif menu_input.lower() == "exit":
        break
    
    else:
        print("Sorry that wasn't one of the options")
        continue

    menu_input = input("\n\nType what you want to do: ")