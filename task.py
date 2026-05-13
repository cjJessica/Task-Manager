from colorama import Fore, Style, init

init(autoreset=True)

class Task:
    def __init__(self, id, title, priority, completed=False):
        self.id = id
        self.title = title
        self.priority = priority
        self.completed = completed

    def mark_completed(self):
        self.completed = True
    
    def display(self):
        #Check mark styling
        check = (Fore.GREEN + Style.BRIGHT + "[X]" + Style.RESET_ALL) if self.completed else "[ ]"

        #Priority styling
        if self.priority == "high":
            color = Fore.RED
        elif self.priority == "med":
            color = Fore.YELLOW
        elif self.priority == "low":
            color = Fore.CYAN
        else:
            color = Fore.WHITE

        #task title styling
        title_spacing = self.title[:9] + "..." if len(self.title) > 12 else self.title

            
        return f"\n{check}    {self.id:<3} |  {title_spacing:<12} |  {color}{self.priority.upper():<5}"
    
