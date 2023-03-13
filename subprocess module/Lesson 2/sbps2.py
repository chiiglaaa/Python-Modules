import subprocess

print("Lesson 2 of python subprocess module.")

def welcome():
    print()
    print("Tools you can use:")
    print()
    print("\033[37m" + "   1)" + "\033[0m" + " subprocess.run - this will run a shell command.")
    print("\033[37m" + "   2)" + "\033[0m" + " subprocess.Popen - this will run a shell command.")
    print("\033[37m" + "             This will give you more control over the process." + "\033[0m")
    print()
    print("    " + "\033[1m" + "\033[31m" + "to quit use ctrl+c or type 'q'." + "\033[0m")
    print()
    while True:
        welcome_input = input("~$: ")
        if welcome_input not in ["1", "2", "q"]:
            print("Invalid input. Please try again.")
        else:
            break
    return welcome_input


print("-----------------------------")
choice = welcome()

def main(choice):
    if choice.lower() == "q":
        print("----------------------------------")
        r_u_sure = input("Do you really want to quit? (y/n): ")
        if r_u_sure.lower() == "y":
            exit()
        elif r_u_sure.lower() == "n":
            choice = welcome()
            main(choice)
    elif choice == "1":
        print()
        print("----------------------------------")
        print()
        print("    " + "\033[1m" + "\033[31m" + "to quit type 'back'." + "\033[0m")
        print("\033[31m" + "Available commands: " + "\033[33m" + "mkdir, grep, echo" + "\033[0m")
        while True:
            cmd = input("Which command would you like to run?: ")
            if cmd not in ['mkdir', 'grep', 'echo', 'back']:
                print("Invalid input. Please try again.")
            else:
                break
        if cmd.lower() == "back":
            choice = welcome()
            main(choice)
        elif cmd.lower() == "mkdir":
            print("If you want to make new directory, we need to use shell=True argument.")
            path_way = input("Specify the path: ")
            dir_name = input("Specify the name: ")
            if path_way[-1] != "/":
                path_way += "/"
            full_path = path_way + dir_name
            subprocess.run(f'mkdir {full_path}', shell=True)
            choice = welcome()
            main(choice)
        elif cmd.lower() == "grep":
            path_way = input("Specify the path: ")
            file_name = input("Specify the name of the file: ")
            grep_name = input("Specify what you are searching: ")
            if path_way[-1] != "/":
                path_way += "/"
            full_path = path_way + file_name
            try:
                print()
                subprocess.run(f'grep {grep_name} {full_path}', shell=True, check=True)
            except subprocess.CalledProcessError as err:
                print(f"ERROR: {err}")
            choice = welcome()
            main(choice)
        elif cmd.lower() == "echo":
            user_input = input("What would you like to print?: ")
            subprocess.run(f'echo {user_input}', shell=True)
            choice = welcome()
            main(choice)
    elif choice == "2":
        print()
        print("----------------------------------")
        print()
        print("    " + "\033[1m" + "\033[31m" + "to quit type 'back'." + "\033[0m")
        print("\033[31m" + "Available commands: " + "\033[33m" + "mkdir, grep, echo" + "\033[0m")
        while True:
            cmd = input("Which command would you like to run?: ")
            if cmd not in ['mkdir', 'grep', 'echo', 'back']:
                print("Invalid input. Please try again.")
            else:
                break
        if cmd.lower() == "back":
            choice = welcome()
            main(choice)
        elif cmd.lower() == "mkdir":
            path_way = input("Specify the path: ")
            dir_name = input("Specify the name: ")
            if path_way[-1] != "/":
                path_way += "/"
            full_path = path_way + dir_name
            command = f"mkdir {full_path}"
            p = subprocess.Popen(command, shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = p.communicate()
            print(stdout.decode())
            print("Directory created successfully")
            choice = welcome()
            main(choice)
        elif cmd.lower() == "grep":
            path_way = input("Specify the path: ")
            file_name = input("Specify the name of the file: ")
            grep_name = input("Specify what you are searching: ")
            if path_way[-1] != "/":
                path_way += "/"
            full_path = path_way + file_name
            command = f"grep {grep_name} {full_path}"
            p = subprocess.Popen(command, shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = p.communicate()
            print()
            print(stdout.decode())
            choice = welcome()
            main(choice)
        elif cmd.lower() == "echo":
            user_input = input("What would you like to print?: ")
            command = f"echo {user_input}"
            p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = p.communicate()
            print()
            print(stdout.decode())
            choice = welcome()
            main(choice)

main(choice)