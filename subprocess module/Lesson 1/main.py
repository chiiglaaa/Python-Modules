import subprocess

print("Lesson 1 of python subprocess module.")


def welcome():
    print()
    print("Tools you can use:")
    print()
    print("\033[37m" + "   1)" + "\033[0m" + " subprocess.run - this will run a shell command.")
    print("\033[37m" + "   2)" + "\033[0m" + " subprocess.Popen - this will run a shell command.")
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
    if choice == "q":
        print("----------------------------------")
        r_u_sure = input("Do you really want to quit? (y/n): ")
        if r_u_sure.lower() == "y":
            exit()
        elif r_u_sure.lower() == "n":
            choice = welcome()
            main(choice)
    if choice == "1":
        print()
        print("----------------------------------")
        print()
        print("    " + "\033[1m" + "\033[31m" + "to quit type 'back'." + "\033[0m")
        print("\033[31m" + "Available commands: " + "\033[33m" + "ls, pwd, whoami, date, cat, echo" + "\033[0m")
        while True:
            cmd = input("Which command would you like to run?: ")
            if cmd not in ['ls', 'pwd', 'whoami', 'date', 'cat', 'echo', 'back']:
                print("Invalid input. Please try again.")
            else:
                break
        if cmd == "back":
            choice = welcome()
            main(choice)
        elif cmd == "ls":
            print("\033[31m" + "USE man ls COMMAND BEFORE USING ANY ARGUMENT." + "\033[0m")
            error_result = ["ls: cannot access", "ls: invalid line width", "ls: option requires an argument"]
            while True:
                specify_cmd = input("Do you want to use specific arguments? (y/n): ")
                if specify_cmd.lower() == 'n':
                    result = subprocess.run(['ls'], stdout=subprocess.PIPE)
                    output = result.stdout.decode('utf-8')
                    print("\033[34m" + output + "\033[0m")
                    break
                elif specify_cmd.lower() == 'y':
                    while True:
                        which_cmd = input("Which argument would you like to add?(To exit type) 'exit': ")
                        if which_cmd == 'exit':
                            break
                        else:
                            result = subprocess.run(['ls', f"-{which_cmd}"], stdout=subprocess.PIPE)
                            output = result.stdout.decode('utf-8')
                            print("\033[34m" + output + "\033[0m")
                            for e in error_result:
                                if e in str(result):
                                    print("[!] invalid argument. try again")
                                    break
                    break
                else:
                    result = subprocess.run(["ls"], stdout=subprocess.PIPE)
                    output = result.stdout.decode('utf-8')
                    print(output)
                break
            main(choice="1")
        elif cmd == "pwd":
            result = subprocess.run(['pwd'], stdout=subprocess.PIPE)
            output = result.stdout.decode('utf-8')
            print()
            print("\033[34m" + output + "\033[0m")
            main(choice="1")
        elif cmd == "whoami":
            result = subprocess.run(['whoami'], stdout=subprocess.PIPE)
            output = result.stdout.decode('utf-8')
            print()
            print("\033[34m" + output + "\033[0m")
            main(choice="1")
        elif cmd == 'date':
            result = subprocess.run(['date'], stdout=subprocess.PIPE)
            output = result.stdout.decode('utf-8')
            print()
            print("\033[34m" + output + "\033[0m")
            main(choice="1")
        elif cmd == "echo":
            text = input("What would you like to print?: ")
            result = subprocess.run(['echo', f"{text}"], stdout=subprocess.PIPE)
            output = result.stdout.decode('utf-8')
            print()
            print("\033[34m" + output + "\033[0m")
            main(choice='1')
        elif cmd == "cat":
            name_input = input("Enter file name: ")
            path_input = input("Enter path: ")
            if path_input[-1] != "/":
                path_input += "/"
            full_path = path_input + name_input
            result = subprocess.run(['cat', f"{full_path}"], stdout=subprocess.PIPE)
            output = result.stdout.decode('utf-8')
            print()
            print("\033[34m" + output + "\033[0m")
            main(choice='1')
    elif choice == "2":
        print()
        print("----------------------------------")
        print()
        print("    " + "\033[1m" + "\033[31m" + "to quit type 'back'." + "\033[0m")
        print("\033[31m" + "Available commands: " + "\033[33m" + "ls, ping" + "\033[0m")
        while True:
            cmd = input("Which command would you like to run?: ")
            if cmd not in ['ls', 'ping', 'back']:
                print("Invalid input. Please try again.")
            else:
                break
        if cmd == "back":
            choice = welcome()
            main(choice)
        elif cmd == "ls":
            while True:
                file_input = input("Wanna use file?(y/n): ")
                if file_input not in ['n', 'y']:
                    print("Invalid input.")
                elif file_input == 'n':
                    p = subprocess.Popen(['ls'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    output = p.communicate()[0].decode()
                    print("Output:", output)
                    break
                elif file_input == "y":
                    file_name = input("Whats the name of the file?: ")
                    p = subprocess.Popen(['ls', f'{file_name}'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    output, errors = p.communicate()
                    output = output.decode('utf-8')
                    errors = errors.decode('utf-8')
                    print("Output:", output)
                    print("Errors:", errors)
                    break
            main(choice="2")
        elif cmd == "ping":
            web_input = input("Which website would you like to ping?(example: google.com): ")
            p = subprocess.Popen(["ping", f"{web_input}"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            for line in iter(p.stdout.readline, 'b'):
                if "icmp_seq=16" in str(line):
                    break
                else:
                    print(line.decode('utf-8'), end='')

            p.stdout.close()
            p.wait()
            main(choice="2")


main(choice)
