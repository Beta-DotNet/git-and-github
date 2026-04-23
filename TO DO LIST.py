print("To Do List")

print("Select 1  To Add a task, Selct 2 to View TasK, Select 3 to delete task, Select 4 to mark task as completed, Select 5 load tasks from a file when program sarts")

task = ""

choice = int(input("Enter your choice: "))
if choice == 1:
    task = input("Enter Task: ")
elif choice == 2:
    print("You have "+ task + " on your to do list")
elif choice == 3:
    task = ""
    print("Task deleted succesfully")
elif choice == 4:
    print(task, "completed")
elif choice == 5:
    with open("task.txt", "w") as file:
        file.write(task)
elif choice == 6:
    with open("task.txt", "r") as file:
        tasks = file.read()
        print(tasks)
else:
    print("INVALID OPTION")





