from task_manager import TaskManager
import storage


manager = TaskManager()
instructions = """
Welcome to Task Manager!
    - If you want to add a task type 'add'
    - If you want to delete a task type 'delete'
    - If you want to check off a task type 'complete'
    - If you want to list all your tasks type 'list'
Or type 'exit' to exit the program
"""



while True:
    menu_input = input(f"{instructions} \nType what you want to do: ")


    if menu_input.lower() == "add":
        priority_levels = ["high", "med", "low"]
        title_input = input("What is the name of the task? ")

        while title_input == "":
            title_input = input("Please enter a valid task name: ")

        priority_input = input("What is the task's priority (high, med, low)? ")

        
        while priority_input.lower() not in priority_levels:
            priority_input = input(f"\nPlease type one of the following: \n{priority_levels} \n")

        manager.add_task(title_input, priority_input.lower())


    elif menu_input.lower() == "list":
        print("\n" + " TASKS ".center(34, "="))
        manager.list_tasks()


    elif menu_input.lower() == "complete":
        while True:

            id_input = input(
                "What is the task's ID? "
                "or enter 'menu' to go back: "
            )

            if id_input.lower() == "menu":
                break

            try:
                id_input = int(id_input)

                if manager.complete_task(id_input):
                    print("The task has been checked off!")
                    break

                print("Sorry none of the tasks have that ID number")

            except ValueError:
                print("Please enter a valid number")


    elif menu_input.lower() == "delete":
        while True:
            id_input = input(
                "What is the task's ID? "
                "or enter 'menu' to go back: "
            )

            if id_input.lower() == "menu":
                break

            try:
                id_input = int(id_input)
                
                deleted_taskname = manager.delete_task(id_input)
                
                if deleted_taskname is None:
                    print("Sorry none of the tasks have that ID number")

                else:
                    print(f"The '{deleted_taskname}' has been deleted")
                    break

            except ValueError:
                print("Please enter a valid number")


    elif menu_input.lower() == "exit":
        save_input = input("Do you want to save your current task list? y/n: ")
        while save_input.lower() != 'y' and save_input.lower() != 'n':
            save_input = input("Please enter 'y' or 'n'")

        if save_input.lower() == 'y':
            storage.save_data(manager)
            print("Your tasks are saved!")      
        else:
            print("All your tasks are deleted")

        break
    
    else:
        print("Sorry that wasn't one of the options")