from addTask import add_task
from storeTask import store_task
from viewTasks import view_tasks
from deleteTasks import delete_tasks

def get_run_choice() -> int:
    while True:
        try:
            print("\n")
            run_choice = int(input("What would you like to perform?\n1- Add Task\n2- View Tasks\n3- Delete Tasks\n4- Exit\n>> "))
        except ValueError:
            print(f"You must enter a valid number :<")
            continue
        if run_choice not in [1,2,3,4]:
            print("You did not enter a valid choice :< ")
            continue
        else:
            return run_choice

def execute_choice(run_choice):
    if run_choice == 1:  
        try:
            # Get the details of the new task from the user
            name, description, priority = add_task()
            print("Successfully added new task :)")
        except Exception as e:
            print(f"An error occurred when processing task information :< {e}")
            print("Performing self destruct...")
            exit()

        try:
            print("Saving new task...")
            successfully_stored = store_task(name, description, priority)
            if successfully_stored == True:
                print("Saved new task :)")
            else:
                print("Couldn't save new task :<")
        except Exception as e:
            print(f"Error occrued when trying to call file writing function :< {e}")
            print("Performing self destruct...")
            exit()
        execute_choice(get_run_choice())

    elif run_choice == 2:
        try:
            view_tasks()
        except Exception as e:
            print(f"Error occured when viewing tasks :< {e}")
        execute_choice(get_run_choice())
        
    elif run_choice == 3:
        try:
            delete_tasks()
        except Exception as e:
            print(f"Error occured when trying to run delete task function :< {e}")
        execute_choice(get_run_choice())

    elif run_choice == 4:
        exit()

# Only start the main program is the file is being directly run
if __name__ == "__main__":
    execute_choice(get_run_choice())