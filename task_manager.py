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

    def find_id(self, task_id):
        for task in self.tasks:
            if task_id == task.id:
                return task
    
        return None
        
            

    def complete_task(self, task_id):
        task = self.find_id(task_id)
        
        if task is None:
            return False
        
        task.mark_completed()
        return True


    def delete_task(self, task_id):
        task = self.find_id(task_id)

        if task is None:
            return None

        self.tasks.remove(task)
        return task.title