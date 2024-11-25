
def view_tasks():
    try:
        with open('tasks.txt','r') as f:
            lines = f.read()
            print(lines)
    except FileNotFoundError:
        print("Error when opening the file. Maybe you haven't created a task yet? :<")