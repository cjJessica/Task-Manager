from task import Task

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self, title, priority):
        new_task = Task(self.next_id, title, priority)

        self.tasks.append(new_task)

        self.next_id += 1

    def list_tasks(self):
        for x in self.tasks:
            print(f"{x.display()}")

    def complete_task(self, task_id):
        for task in self.tasks:
            if task == task_id:
                task.mark_completed()
                return "The task is marked as complete"
        return "No task had that id number"
