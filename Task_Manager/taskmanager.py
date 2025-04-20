#task manager

#task folder
tasks = ['eat', 'sleep', 'walk', 'bath']
#completed folder
complete = []


#add task func
def add_task():
    new_task = input("Add new task: ")
    if new_task not in tasks:
        tasks.append(new_task)
        print(f"{new_task} added to tasks. your current tasks are: {tasks}")
    elif new_task in tasks:
        print(f"{new_task} already exists, bitch!")

#delete task func
def del_task():
    deleted = input("Enter task to delete: ")
    if deleted in tasks:
        tasks.remove(deleted)
        print(f"{deleted} has been deleted from tasks. your tasks are now: {tasks}")
    elif deleted not in tasks:
            print('Invalid task name')

#mark as complete
def mark_comp():
    mark = input("Enter task to mark as complete: ")
    tasks.remove(mark)
    complete.append(mark)
    print(f"{mark} has been marked as complete. your current tasks are: {tasks},\nCompleted tasks are: {complete}")


#view tasks
def view_tasks():
    pass

#menu fuction
while True:
        print("Welcome to task Manager pro max\n1. Add task\n2. Delete task\n3. Mark task as complete\n4. View all tasks\n5. Exit")
        opt = input("Enter option: ")
        if opt == '1':
            add_task() #add task
        elif opt == '2':
            del_task() #delete task
        elif opt == '3':
            mark_comp() #mark task as complete
        elif opt == '4':
            print(f"your current tasks are: {tasks}, completed tasks are: {complete}") #view tasks
        elif opt == '5':
            print('Goodbye') #exit
            break
        else:
            print("Invalid entry. Enter a valid option")