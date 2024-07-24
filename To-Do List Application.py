class TodoItem:
    def __init__(self, task, completed=False):
        self.task = task
        self.completed = completed

    def __str__(self):
        return f"{'✓' if self.completed else '◻'} {self.task}"

class TodoList:
    def __init__(self):
        self.items = []

    def add_item(self, task):
        self.items.append(TodoItem(task))

    def complete_item(self, index):
        self.items[index].completed = True

    def uncomplete_item(self, index):
        self.items[index].completed = False

    def remove_item(self, index):
        self.items.pop(index)

    def display(self):
        for i, item in enumerate(self.items):
            print(f"{i+1}. {item}")

def main():
    todo_list = TodoList()

    while True:
        print("\nTodo List:")
        todo_list.display()
        print("\nOptions:")
        print("1. Add task")
        print("2. Complete task")
        print("3. Uncomplete task")
        print("4. Remove task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            task = input("Enter new task: ")
            todo_list.add_item(task)
        elif choice == "2":
            index = int(input("Enter the task number to complete: "))
            todo_list.complete_item(index - 1)
        elif choice == "3":
            index = int(input("Enter the task number to uncomplete: "))
            todo_list.uncomplete_item(index - 1)
        elif choice == "4":
            index = int(input("Enter the task number to remove: "))
            todo_list.remove_item(index - 1)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()