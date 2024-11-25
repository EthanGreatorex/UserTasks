
def store_task(name, description, priority) -> bool:
    try:
        # 'a' opener will create the file if needed
        with open("tasks.txt","a") as f:
            try:
                f.write("\n")
                f.write(f"+{'_'*60}+\n")
                f.write(f"|{'[Task -- ' + name + ']':^60}|\n")
                f.write(f"|{'_'*60}|\n") 
                f.write(f"|{' ':^60}|\n") 
                f.write(f"|{description:^60}|\n")
                f.write(f"|{' ':^60}|\n")
                f.write(f"|{'Priority -- ' + priority:^60}|\n")
                f.write(f"+{'_'*60}+\n")
                f.write("*")
                f.write("\n")
            except Exception as e:
                print(f"Error occrued whilst trying to write to file :< {e}")
                return False
    except:
        print(f"Error occrued whilst trying to open the file :< {e}")  
        return False
    else:
        return True
