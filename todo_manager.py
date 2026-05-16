
BLUE = "\033[34m"
RESET = "\033[0m"
print(f""" \n{'':=^60}\n
{'':20} My To-Do List \n
{'':=^60}\n

1. Buy groceries
2. finish homework
3. Call the dentist \n

What would you like to {BLUE}do{RESET}?
1. Add a task
2. Remove a task 
""")

tasks = ["Buy groceries", "finish homework", "call the dentist"]


while True:
    try:
        choice = (input("Choice: ")).strip()
        if len(choice.split()) != 1:
            raise ValueError("Enter too many item.")
        choice = int(choice)
        if choice >2 or choice <= 0:
            raise ValueError("You only have 2 choices")
        if choice == 1:
            try:
                task = input("Enter new task: ") 
                tasks.append(task);
            except ValueError:
                print("Please enter strings")
        if choice == 2:
            try:
                task = input("Enter Task To Remove: ")
                print("\n")
                tasks.pop(int(task) - 1)
            except ValueError:
                print("Please Enter a Number")
        break
        
    except ValueError:
        print("Please Try Again")
print("\n")
print("Updated list:")
for i, t in enumerate(tasks):
    print(f"""{i + 1}. {t} """)

print(f"""\nTotal tasks: {len(tasks)}\n""")