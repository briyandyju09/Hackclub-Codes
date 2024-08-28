import json
import os

class TaskManager:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        if not os.path.exists(self.filename):
            with open(self.filename, "w") as f:
                json.dump([], f)
        self.load()

    def load(self):
        with open(self.filename, "r") as f:
            self.tasks = json.load(f)

    def save(self):
        with open(self.filename, "w") as f:
            json.dump(self.tasks, f, indent=4)

    def add_task(self, task_name):
        task = {"name": task_name, "completed": False}
        self.tasks.append(task)
        self.save()
        print(f"Task '{task_name}' added.")

    def mark_completed(self, task_name):
        for task in self.tasks:
            if task["name"] == task_name:
                task["completed"] = True
                self.save()
                print(f"Task '{task_name}' marked as completed.")
                return
        print(f"Task '{task_name}' not found.")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        for task in self.tasks:
            status = "Completed" if task["completed"] else "Not Completed"
            print(f"Task: {task['name']}, Status: {status}")

def main():
    task_manager = TaskManager()
    
    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. Mark Task as Completed")
        print("3. List Tasks")
        print("4. Exit")
        
        choice = input("Choose an option: ")

        if choice == "1":
            task_name = input("Enter task name: ")
            task_manager.add_task(task_name)

        elif choice == "2":
            task_name = input("Enter task name to mark as completed: ")
            task_manager.mark_completed(task_name)

        elif choice == "3":
            task_manager.list_tasks()

        elif choice == "4":
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
