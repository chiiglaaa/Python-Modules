import os

print("Lesson 1 of python os module.")
def ask():
    print()
    print("""\
                                     8       8          w                       w   8                 
    .d8b. d88b    8d8b.d8b. .d8b. .d88 8   8 8 .d88b    w 8d8b.    88b. Yb  dP w8ww 8d8b. .d8b. 8d8b. 
    8' .8 `Yb.    8P Y8P Y8 8' .8 8  8 8b d8 8 8.dP'    8 8P Y8    8  8  YbdP   8   8P Y8 8' .8 8P Y8 
    `Y8P' Y88P    8   8   8 `Y8P' `Y88 `Y8P8 8 `Y88P    8 8   8    88P'   dP    Y8P 8   8 `Y8P' 8   8 
                                                                   8     dP                                                                         
                                               """)
    print("Tools you can use:")
    print("\033[37m" + "[*]" + "\033[0m" + " remove (which removes files)")
    print("\033[37m" + "[*]" + "\033[0m" + " rmdir (which removes empty directories)")
    print("\033[37m" + "[*]" + "\033[0m" + " mkdir (which makes directories)")
    print("\033[37m" + "[*]" + "\033[0m" + " cwd (which will tell you your current working directory")
    print("\033[37m" + "[*]" + "\033[0m" + " cd (which will change your current working directory)")
    print("\033[37m" + "[*]" + "\033[0m" + " ls/l (which will list all files and directories in the current directory)")
    print("\033[37m" + "[*]" + "\033[0m" + " osname (which will tell you your operating system name)")
    print()
    print("     to quit use ctrl+c ")
    print()

ask()
user_input = input("What would you like to do?: ")

def main():
    if user_input == "remove":
        path_input = input("From where would you like to remove a file?: ")
        filename_input = input("What file would you like to remove?: ")
        path = os.path.join(path_input, filename_input)

        try:
            os.remove(path)
            print(f"File {filename_input} has been removed")
        except FileNotFoundError:
            print("File not found. try again.")
            main()
    elif user_input == "rmdir":
        path_input = input("From where would you like to remove an empty directory?: ")
        dirname_input = input("What directory would you like to remove?: ")
        path = os.path.join(path_input, dirname_input)

        try:
            os.rmdir(path)
            print(f"Directory {dirname_input} has been removed")
        except FileNotFoundError:
            print("File not found. try again.")
            main()
    elif user_input == "mkdir":
        path_input = input("Where would you like to make a directory?: ")
        dirname_input = input("What would you like to name a directory?: ")
        path = os.path.join(path_input, dirname_input)

        try:
            os.mkdir(path)
            print(f"Directory {dirname_input} has been created")
        except FileExistsError:
            print("Directory already exists. try again.")
            main()
        except PermissionError:
            print("Permission denied. try again.")
            main()
        except FileNotFoundError:
            print("The path does not exist. try again.")
            main()
    elif user_input == "cwd":
        print(os.getcwd())
    elif user_input == "cd":
        path_input = input("Where would you like to change your working directory?: ")

        try:
            os.chdir(path_input)
            print("your working directory has changed to", os.getcwd())
        except FileNotFoundError:
            print("The path does not exist. try again.")
            main()
    elif user_input == "ls" or user_input == "l":
        path_input = input("From where would you like to list files?: ")
        print("Files and directories in '", path_input ,"' :")

        try:
            print(os.listdir(path_input))
        except FileNotFoundError:
            print("The path does not exist. try again.")
            main()
    elif user_input == "osname":
        print(os.name)
        if os.name == "posix":
            print("This indicates a Unix or Linux-based operating system, such as macOS, Ubuntu, Debian etc.")
        elif os.name == "nt":
            print("This indicates a Windows operating system, such as Windows 10 or Windows Server.")
        elif os.name == "os2":
            print("This indicates an IBM OS/2 operating system.")
        elif os.name == "ce":
            print("This indicates a Windows CE operating system, which is a stripped-down version of Windows designed for embedded systems and mobile devices.")
        elif os.name == "java":
            print("This indicates a Java-based operating system, such as JavaOS or JNode.")
        elif os.name == "riscos":
            print("This idicates a RISC OS operating system, which is designed for ARM-based computers.")

main()
