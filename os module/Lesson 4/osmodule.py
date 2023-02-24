import os


def choose():
    print("This is my final project using os module.")
    print()
    print("Options you can choose:")
    print()
    print(" \033[1m" + "\033[33m" + "   1)" + "\033[32m" + "File Management")
    print(" \033[1m" + "\033[33m" + "   2)" + "\033[32m" + "System Information")
    print(" \033[1m" + "\033[33m" + "   3)" + "\033[32m" + "Process Management")
    print()
    print("\033[35m" + " To quit use CTRL+C or type 'q'." + "\033[0m")
    print()

    while True:
        ask_input = input("~$: ")
        if ask_input not in ["1", "2", "3", "q"]:
            print("Invalid input, please try again.")
        else:
            break
    return ask_input


print("----------------------------------")
chooser = choose()

def main(chooser):
    if chooser == "q":
        print("----------------------------------")
        r_u_sure = input("Do you really want to quit? (y/n): ")
        if r_u_sure.lower() == "y":
            exit()
        elif r_u_sure.lower() == "n":
            chooseer = choose()
            main(chooseer)
    elif chooser == "1":
        print("----------------------------------")
        print()
        print("With File Management tools you can:")
        print()
        print("\033[1m" + "\033[37m" + "    [*]" + "\033[36m" + "Create")
        print("\033[1m" + "\033[37m" + "    [*]" + "\033[35m" + "Delete")
        print("\033[1m" + "\033[37m" + "    [*]" + "\033[36m" + "Rename")
        print("\033[1m" + "\033[37m" + "    [*]" + "\033[36m" + "Move")
        print("\033[1m" + "\033[0m" + "    files and directories.")
        print()
        print("\033[1m" + "\033[36m" + " if you want to go back type 'back'." + "\033[0m")
        print()
        while True:
            user_input = input("What would you like to do?: ")
            if user_input not in ['create', 'rename', 'delete', 'move', 'back']:
                print("Invalid input, please try again.")
            else:
                break
        if user_input == "back":
            chooser = choose()
            main(chooser)
        if user_input == 'create':
            while True:
                ask = input("What would you like to create?(file | directory): ")
                if ask not in ['file', 'directory']:
                    print("Invalid input, please try again.")
                else:
                    break
            if ask == 'file':
                while True:
                    path_input = input("Where would you like to make the file?(specify the path): ")
                    if os.path.isdir(path_input):
                        break
                    else:
                        print("Invalid path, please try again.")
                while True:
                    name_input = input("What would you like to name the file?: ")
                    file_checker = os.path.join(path_input, name_input)
                    if os.path.isfile(file_checker):
                        print("That file already exists, please try again.")
                    else:
                        break
                full_path = os.path.join(path_input, name_input)
                with open(full_path, "w") as file:
                    write_input = input("What would you like to write in the file?: ")
                    file.write(write_input)
                print("File created successfully.")
                exit()
            elif ask == 'directory':
                while True:
                    path_input = input("Where would you like to make the file?(specify the path): ")
                    if os.path.isdir(path_input):
                        break
                    else:
                        print("Invalid path, please try again.")
                while True:
                    name_input = input("What would you like to name the directory?: ")
                    dir_checker = os.path.join(path_input, name_input)
                    if os.path.isdir(dir_checker):
                        print("That directory already exists, please try again.")
                    else:
                        break
                full_path = os.path.join(path_input, name_input)
                os.mkdir(full_path)
                print("Directory created successfully.")
                exit()
        elif user_input == 'delete':
            while True:
                ask = input("What would you like to create?(file | directory): ")
                if ask not in ['file', 'directory']:
                    print("Invalid input, please try again.")
                else:
                    break
            if ask == 'file':
                while True:
                    path_input = input("Where is the file located?(specify the path): ")
                    if os.path.isdir(path_input):
                        break
                    else:
                        print("Invalid path, please try again.")
                while True:
                    name_input = input("What is the name of the file?: ")
                    dir_checker = os.path.join(path_input, name_input)
                    if not os.path.isfile(dir_checker):
                        print("That file do not exists, please try again.")
                    else:
                        break
                full_path = os.path.join(path_input, name_input)
                os.remove(full_path)
                print("File deleted successfully.")
                exit()
            elif ask == 'directory':
                print("\033[35m" + "Note that this will only delete empty directories!!!" + "\033[0m]")
                while True:
                    path_input = input("Where is the file located?(specify the path): ")
                    if os.path.isdir(path_input):
                        break
                    else:
                        print("Invalid path, please try again.")
                while True:
                    name_input = input("What is the name of the directory?: ")
                    dir_checker = os.path.join(path_input, name_input)
                    if not os.path.isdir(dir_checker):
                        print("That directory do not exists, please try again.")
                    else:
                        break
                full_path = os.path.join(path_input, name_input)
                os.rmdir(full_path)
                print("Directory deleted successfully.")
                exit()
        elif user_input == 'rename':
            while True:
                ask = input("What would you like to rename?(file | directory): ")
                if ask not in ['file', 'directory']:
                    print("Invalid input, please try again.")
                else:
                    break
            if ask == 'file':
                while True:
                    path_input = input("Where is the file located?(specify the path): ")
                    if os.path.isdir(path_input):
                        break
                    else:
                        print("Invalid path, please try again.")
                while True:
                    name_input = input("What is the name of the file?: ")
                    dir_checker = os.path.join(path_input, name_input)
                    if not os.path.isfile(dir_checker):
                        print("That file do not exists, please try again.")
                    else:
                        break
                os.chdir(path_input)
                new_name = input("What is the new name of the file?: ")
                os.rename(name_input, new_name)
                print("File renamed successfully.")
                exit()
            if ask == 'directory':
                while True:
                    path_input = input("Where is the directory located?(specify the path): ")
                    if os.path.isdir(path_input):
                        break
                    else:
                        print("Invalid path, please try again.")
                while True:
                    name_input = input("What is the name of the directory?: ")
                    dir_checker = os.path.join(path_input, name_input)
                    if not os.path.isdir(dir_checker):
                        print("That directory do not exists, please try again.")
                    else:
                        break
                full_path = os.path.join(path_input, name_input)
                new_name = input("What is the new name of the directory?: ")
                new_full_path = os.path.join(path_input, new_name)
                os.rename(full_path, new_full_path)
                print("Directory renamed successfully.")
                exit()
        if user_input == 'move':
            while True:
                ask = input("What would you like to move?(file | directory): ")
                if ask not in ['file', 'directory']:
                    print("Invalid input, please try again.")
                else:
                    break
            if ask == 'file':
                while True:
                    path_input = input("Where is the file located?(specify the path): ")
                    if os.path.isdir(path_input):
                        break
                    else:
                        print("Invalid path, please try again.")
                while True:
                    name_input = input("What is the name of the file?: ")
                    full_path = os.path.join(path_input, name_input)
                    if not os.path.isfile(full_path):
                        print("That file do not exists in this directory, please try again.")
                    else:
                        break
                old_path = os.path.join(path_input, name_input)
                while True:
                    new_path = input("Where would you like to move the file?(specify the path): ")
                    if os.path.isdir(new_path):
                        break
                    else:
                        print("Invalid path, please try again.")
                os.rename(old_path, os.path.join(new_path, name_input))
                print("File moved successfully.")
                exit()
    elif chooser == "2":
        print("----------------------------------")
        print()
        print("Information about your system:")
        uname = os.uname()
        print()
        print(" \033[1m" + "\033[33m" + "   [*]" + "\033[32m" + "OS name:" + "\033[0m" + uname.sysname + " " + uname.machine + " " + os.name)
        print(" \033[1m" + "\033[33m" + "   [*]" + "\033[32m" + "OS version:" + "\033[0m" + uname.version)
        print(" \033[1m" + "\033[33m" + "   [*]" + "\033[32m" + "Kernel:" + "\033[0m" + uname.release)
        if uname.sysname == "Darwin":
            print(" \033[1m" + "\033[33m" + "   [*]" + "\033[32m" + "CPU:" + "\033[0m" + os.popen("sysctl -n machdep.cpu.brand_string").read().strip())
            print("\033[33m" + "      [*]" + "\033[32m" + "CPU cores: " + str(os.cpu_count()) + "\033[0m")
        elif uname.sysname == "Linux":
            print(" \033[1m" + "\033[33m" + "   [*]" + "\033[32m" + "CPU:" + "\033[0m" + os.popen("cat /proc/cpuinfo | grep 'model name' | uniq").readline().strip().split(": ")[1])
            print("\033[33m" + "      [*]" + "\033[32m" + "CPU cores: " + str(os.cpu_count()) + "\033[0m")
        print()
        print("\033[1m" + "\033[36m" + " if you want to go back type 'back'." + "\033[0m")
        print()
        user_input = input("~$: ")
        if user_input == "back":
            chooser = choose()
            main(chooser)
        elif chooser == "3":
        print("----------------------------------")
        print()
        print("Process Managament:")
        print()
        print(" \033[1m" + "\033[33m" + "   1)" + "\033[32m" + "Show running processes.")
        print(" \033[1m" + "\033[33m" + "   2)" + "\033[32m" + "Kill process.")
        print()
        print("\033[36m" + " if you want to go back type 'back'." + "\033[0m")
        print()
        while True:
            user_input = input("~$: ")
            if user_input not in ['1', '2', 'back']:
                print("Invalid input, please try again.")
            else:
                break
        if user_input == "back":
            chooser = choose()
            main(chooser)
        if user_input == "1":
            user_name = input("What is your user name?:")
            process_list = os.popen(f"ps -u {user_name} -o pid,cmd").read()
            print(process_list)
            print()
            exit()
        if user_input == "2":
            id_input = int(input("What is the process id you want to kill?: "))
            try:
                os.kill(id_input, 0)
                os.kill(id_input, 9)
                print(f"Process with PID {id_input} has been terminated.")
                exit()
            except OSError as e:
                print(f"Process with PID {id_input} does not exist or could not be terminated: {e}")
                exit()

main(chooser)
