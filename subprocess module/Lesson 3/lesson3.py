import subprocess
import time

print("     Lesson 3 of python subprocess module.")


def welcome():
    print("-----------------------------")
    print()
    print("\033[37m" + "   [*]" + "\033[0m" + " subprocess.run - this will run a shell command.")
    print()
    print("\033[31m" + "Available arguments: " + "\033[0m")
    print()
    print("\033[1m" + "   " + "1)" + "\033[0m" + "\033[33m" + "input" + "\033[0m")
    print("\033[1m" + "   " + "2)" + "\033[0m" + "\033[33m" + "cwd" + "\033[0m")
    print("\033[1m" + "   " + "3)" + "\033[0m" + "\033[33m" + "timeout" + "\033[0m")
    print("\033[1m" + "   " + "4)" + "\033[0m" + "\033[33m" + "encoding" + "\033[0m")
    print("\033[1m" + "   " + "5)" + "\033[0m" + "\033[33m" + "errors" + "\033[0m")
    print("\033[1m" + "   " + "6)" + "\033[0m" + "\033[33m" + "universal_newline" + "\033[0m")
    print("    " + "\033[1m" + "Type argument to get info about it." + "\033[0m")
    print()
    print("    " + "\033[1m" + "\033[31m" + "to quit use ctrl+c or type 'q'." + "\033[0m")
    print()
    while True:
        welcome_input = input("Which argument would you like to use?: ")
        if welcome_input not in ['q', '1', '2', '3', '4', '5', '6', '7']:
            print("Invalid argument for this function. Please try again.")
        else:
            break
    return welcome_input


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
    elif choice == '1':
        print("----------------------------------")
        print()
        print("This argument is similar to 'input', but it is used")
        print("to provide input to the subprocess as a Unicode string.")
        print("Available commands: ")
        print("\033[33m" + "    grep" + "\033[0m")
        print()
        print("\033[1m" + "\033[31m" + "    to go back type 'back'" + "\033[0m")
        print()
        while True:
            un_input = input("What would you like to do?: ")
            if un_input not in ['back', 'grep']:
                print("Invalid input. Try again.")
            else:
                break
        if un_input == "back":
            choice = welcome()
            main(choice)
        elif un_input == 'grep':
            final_input = ''
            howmany = input("How many words you want to provide in list?: ")
            for i in range(int(howmany)):
                user_input = input("Enter text: ")
                final_input = final_input + '\n' + user_input
            grep_input = input("What would you like to grep from text?: ")
            result = subprocess.run(['grep', f'{grep_input}'], input=final_input, stdout=subprocess.PIPE, text=True)
            print(result.stdout)
            main(choice='1')
    elif choice == '2':
        print("----------------------------------")
        print()
        print("This argument sets the current working directory.")
        print("Available commands with this argument: ")
        print("\033[33m" + "    pwd, ls, mkdir, rmdir" + "\033[0m")
        print()
        print("\033[1m" + "\033[31m" + "    to go back type 'back'" + "\033[0m")
        print()
        while True:
            cwd_input = input("What would you like to do?: ")
            if cwd_input not in ['back', 'ls', 'pwd', 'mkdir', 'rmdir']:
                print("Invalid input. Try again.")
            else:
                break
        if cwd_input == "back":
            choice = welcome()
            main(choice)
        elif cwd_input == "ls":
            cwd_path = input("Where would you like to change the cwd?: ")
            ls_argument = input("Would you like to use 'ls' argument?(-l, -a, etc. if not type 'n'): ")
            if ls_argument == 'n' or ls_argument == '':
                result = subprocess.run(['ls'], cwd=f'{cwd_path}')
                print(result)
            else:
                result = subprocess.run(['ls', f'{ls_argument}'], cwd=f'{cwd_path}')
                print(result)
        elif cwd_input == 'pwd':
            cwd_path = input("Where would you like to change the cwd?: ")
            result = subprocess.run(['pwd'], cwd=cwd_path)
            print(result)
        elif cwd_input == 'mkdir':
            cwd_path = input("Where would you like to change the cwd?: ")
            dirname = input("Enter the new directory name: ")
            subprocess.run(['mkdir', dirname], cwd=cwd_path, text=True, capture_output=True)
            print("Directory created successfully.")
        elif cwd_input == 'rmdir':
            cwd_path = input("Where would you like to change the cwd?: ")
            dirname = input("Enter the directory name which you want to remove: ")
            subprocess.run(['rmdir', dirname], cwd=cwd_path)
            print("Directory removed successfully.")
        main(choice='2')
    elif choice == '3':
        print("----------------------------------")
        print()
        print("This argument sets the maximum amount of time")
        print("(in seconds) that the process is allowed to run.")
        print("Available commands with this argument: ")
        print("\033[33m" + "    ping" + "\033[0m")
        print()
        print("\033[1m" + "\033[31m" + "    to go back type 'back'" + "\033[0m")
        print()
        while True:
            timeout_input = input("What would you like to do?: ")
            if timeout_input not in ['back', 'ping']:
                print("Invalid input. Try again.")
            else:
                break
        if timeout_input == "back":
            choice = welcome()
            main(choice)
        elif timeout_input == "ping":
            while True:
                timeout_sec = input("How much time would you like to grant this process to run: ")
                if not timeout_sec.isdigit():
                    print("Invalid input. Must be an integer or positive integer. Try again.")
                else:
                    break
            if int(timeout_sec) > 10:
                timeout_sec = '10'
            host = input("Enter the host which you want to ping: ")
            try:
                result = subprocess.run(['ping', '-c', '1', host], timeout=int(timeout_sec), check=True,
                                        capture_output=True)
                print(result.stdout.decode())
            except subprocess.CalledProcessError:
                print("\033[31m" + "Server is down." + "\033[0m")
            except subprocess.TimeoutExpired:
                print("\033[31m" + f"Ping timed out after {timeout_sec} seconds." + "\033[0m")
            time.sleep(1.5)
            main(choice='3')
    elif choice == "4":
        print("----------------------------------")
        print()
        print("This argument sets the character encoding")
        print("used for the input/output/error pipes of the")
        print("child process.")
        print("Available encoding methods: ")
        print("\033[33m" + "\033[1m" + "  [*]" + "\033[0m" + "\033[31m" + "  utf-8" + "\033[0m")
        print("\033[33m" + "\033[1m" + "  [*]" + "\033[0m" + "\033[31m" + "  utf-16" + "\033[0m")
        print("\033[33m" + "\033[1m" + "  [*]" + "\033[0m" + "\033[31m" + "  ascii" + "\033[0m")
        print()
        print("Available commands: ")
        print("\033[33m" + "    echo" + "\033[0m")
        print()
        print("\033[1m" + "\033[31m" + "    to go back type 'back'" + "\033[0m")
        print()
        while True:
            encoding_input = input("What would you like to do?(choose encoding method): ")
            if encoding_input not in ['back', 'utf-8', 'utf-16', 'ascii']:
                print("Invalid input. Try again.")
            else:
                break
        if encoding_input == "back":
            choice = welcome()
            main(choice)
        elif encoding_input == 'utf-8':
            text_input = input("Enter the text: ")
            result = subprocess.run(['echo', '-n', text_input], stdout=subprocess.PIPE, encoding='utf-8')
            print('Result:', result.stdout)
        elif encoding_input == 'utf-16':
            text_input = input("Enter the text: ")
            result = subprocess.run(['echo', '-n', text_input], stdout=subprocess.PIPE, encoding='utf-16')
            print('Result:', result.stdout)
        elif encoding_input == 'ascii':
            text_input = input("Enter the text: ")
            result = subprocess.run(['echo', '-n', text_input], stdout=subprocess.PIPE, encoding='ascii')
            print('Result:', result.stdout)
        time.sleep(1.5)
        main(choice='4')
    elif choice == '5':
        print("----------------------------------")
        print()
        print("This argument is a parameter that can be passed")
        print("to specify how encoding errors should be handled")
        print("when decoding the output of a subprocess.")
        print("Available error methods: ")
        print("\033[33m" + "\033[1m" + "  1)" + "\033[0m" + "\033[31m" + "  strict" + "\033[0m")
        print("\033[33m" + "\033[1m" + "  2)" + "\033[0m" + "\033[31m" + "  ignore" + "\033[0m")
        print("\033[33m" + "\033[1m" + "  3)" + "\033[0m" + "\033[31m" + "  replace" + "\033[0m")
        print("\033[33m" + "\033[1m" + "  4)" + "\033[0m" + "\033[31m" + "  backslashreplace" + "\033[0m")
        print("\033[33m" + "\033[1m" + "  5)" + "\033[0m" + "\033[31m" + "  xmlcharrefreplace" + "\033[0m")
        print()
        print("Available commands: ")
        print("\033[33m" + "    echo" + "\033[0m")
        print()
        print("\033[1m" + "\033[31m" + "    to go back type 'back'" + "\033[0m")
        print()
        while True:
            errors_input = input("What would you like to do?(choose error method): ")
            if errors_input not in ['back', '1', '2', '3', '4', '5', 'strict', 'ignore', 'replace', 'backslashreplace',
                                    'xmlcharrefreplace']:
                print("Invalid input. Try again.")
            else:
                break
        if errors_input == "back":
            choice = welcome()
            main(choice)
        if errors_input == '1' or errors_input == 'strict':
            text_input = input("Enter the text: ")
            try:
                result = subprocess.run(['echo', text_input.encode('ascii', errors='strict')], capture_output=True)
                print(f"Result: {result.stdout}")
            except UnicodeError as e:
                print(f"Error: {e}")
        elif errors_input == '2' or errors_input == 'ignore':
            text_input = input("Enter the text: ")
            try:
                result = subprocess.run(['echo', text_input.encode('ascii', errors='ignore')], capture_output=True)
                print(f"Result: {result.stdout}")
            except UnicodeError as e:
                print(f"Error: {e}")
        elif errors_input == '3' or errors_input == 'replace':
            text_input = input("Enter the text: ")
            try:
                result = subprocess.run(['echo', text_input.encode('ascii', errors='replace')], capture_output=True)
                print(f"Result: {result.stdout}")
            except UnicodeError as e:
                print(f"Error: {e}")
        elif errors_input == '4' or errors_input == 'backslashreplace':
            text_input = input("Enter the text: ")
            try:
                result = subprocess.run(['echo', text_input.encode('ascii', errors='backslashreplace')], capture_output=True)
                print(f"Result: {result.stdout}")
            except UnicodeError as e:
                print(f"Error: {e}")
        elif errors_input == '5' or errors_input == 'xmlcharrefreplace':
            text_input = input("Enter the text: ")
            try:
                result = subprocess.run(['echo', text_input.encode('ascii', errors='xmlcharrefreplace')], capture_output=True)
                print(f"Result: {result.stdout}")
            except TypeError as e:
                print(f"Error: {e}")
            except UnicodeError as e:
                print(f"Error: {e}")
        time.sleep(1.5)
        main(choice='5')
    elif choice == '6':
        print("----------------------------------")
        print()
        print("This argument sets whether the input/output/error")
        print("pipes of the child process are opened in text mode")
        print("with universal newline support.")
        print("Available commands: ")
        print("\033[33m" + "    ls" + "\033[0m")
        print()
        print("\033[1m" + "\033[31m" + "    to go back type 'back'" + "\033[0m")
        print()
        while True:
            un_input = input("What would you like to do?: ")
            if un_input not in ['back', 'ls']:
                print("Invalid input. Try again.")
            else:
                break
        if un_input == "back":
            choice = welcome()
            main(choice)
        elif un_input == 'ls':
            un_path = input("Where would you like to change the working directory?: ")
            ls_argument = input("Would you like to use 'ls' argument?(-l, -a, etc. if not type 'n'): ")
            if ls_argument == 'n' or ls_argument == '':
                result = subprocess.run(['ls'], cwd=f'{un_path}', universal_newlines=True)
                print(result.stdout)
            else:
                result = subprocess.run(['ls', f'{ls_argument}'], cwd=f'{un_path}', universal_newlines=True)
                print(result.stdout)
        main(choice='6')

try:
    main(choice)
except FileNotFoundError as e:
    print(f'Error: {e}')
    time.sleep(1.5)
    main(choice)
except subprocess.CalledProcessError as e:
    print(f'Error: {e}')
    time.sleep(1.5)
    main(choice)
except TypeError as e:
    print(f'Error: {e}')
    time.sleep(1.5)
    main(choice)