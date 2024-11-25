
def delete_tasks():
    try:
        with open('tasks.txt','r') as f:
            lines = f.read()
            task_list = lines.split('*')
            for i in range(len(task_list)):
                task_list[i] += '*'
    except FileNotFoundError:
        print("Error when opening the file. Maybe you haven't created a task yet? :<")

    while True:
        try:
            task_number = int(input("What number task would you like to delete? >> "))
        except ValueError:
            print("You must enter a number :<")
            continue
        except Exception as e:
            print(f"Error in taking task number :< {e}")
            continue
        else:
            break
    try:
        task_list.pop(task_number-1)
        task_list.pop(-1)
    except Exception as e:
        print("Couldn't seem to find that task :<")
    else:
        with open('tasks.txt','w') as f:
            f.write("")
        with open('tasks.txt','a') as f:
            for task in task_list:
                f.write(task)