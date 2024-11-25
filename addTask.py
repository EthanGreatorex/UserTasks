
def add_task() -> list:
    # Get the name of the task
    while True:
        try:
            print("\n")
            name = input("Name of new task >> ")
        except Exception as e:
            print(f"Error occured getting name {e}")
        else:
            break

    # Get the description of the task
    while True:
        try:
            description = input("Description of new task >> ")
        except Exception as e:
            print(f"Error occured getting description {e}")
        else:
            break
    
    # Get the priority of the task
    while True:
        try:
            priority = int(input("Priority of new task\n1- High\n2- Medium\n3- Low\n>> "))
            # Make sure the input is a valid option
            if priority not in [1,2,3]:
                continue
            else:
                match priority:
                    case 1:
                        priority = "High"
                    case 2:
                        priority = "Medium"
                    case 3:
                        priority = "Low"
        except ValueError:
            print("Cannot understand your input :< Make sure it's a valid number!")
        except Exception as e:
            print(f"Error occured getting priority {e}")
        else:
            break
    return (name.title(), description.capitalize(), priority)