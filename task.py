class Task:
    def __init__(self, id, title, priority, completed=False):
        self.id = id
        self.title = title
        self.priority = priority
        self.completed = completed

    def mark_completed(self):
        self.completed = True
    
    def display(self):
        check = "[X]" if self.completed else "[ ]"
        return f"{check}  {self.id} | {self.title} | {self.priority}"
    
