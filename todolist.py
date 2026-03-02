class Task:
    def __init__(self, description, completed=False):
        self.description = description
        self.completed = completed
class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def display_tasks(self):
        for index, task in enumerate(self.tasks, start=1):
            status = "Done" if task.completed else "Not Done"
            print(f"{index}. {task.description} - {status}")

    def mark_task_completed(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index - 1].completed = True
            print("Task marked as completed.")
        else:
            print("Invalid task index.")
def main():
    todo_list = ToDoList()

    while True:
        print("\n=== To-Do List ===")
        print("1. Add Task")
        print("2. Display Tasks")
        print("3. Mark Task as Completed")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            task_description = input("Enter task description: ")
            new_task = Task(description=task_description)
            todo_list.add_task(new_task)
            print("Task added successfully.")

        elif choice == '2':
            todo_list.display_tasks()

        elif choice == '3':
            task_index = int(input("Enter the task number to mark as completed: "))
            todo_list.mark_task_completed(task_index)

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()

