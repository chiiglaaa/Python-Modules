import os

print("Lesson 2 of python os module.")
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
    print("\033[37m" + "[*]" + "\033[0m" + " open/read/close - whis will open a file, then read and automatically close it. (if you want this function just type open)")
    print("\033[37m" + "[*]" + "\033[0m" + " popen - this will execute shell command.")
    print("\033[37m" + "[*]" + "\033[0m" + " rename - this will rename a file.")
    print("\033[37m" + "[*]" + "\033[0m" + " path.exists - this will check if a file exists.")
    print("\033[37m" + "[*]" + "\033[0m" + " path.getsize - this will give us the size of the file in bytes.")
    print()
    print("    to quit use ctrl_c ")
    print()

ask()
user_input = input("What would you like to do?: ")

def main():
    if user_input == "open":
        try:
            path_input = input("Enter the path to the file: ")
            if not os.path.exists(path_input):
                print("Invalid Path. Try again.")
                main()
            os.chdir(f"{path_input}")
            filename_input = input("Enter the name of the file: ")
            full_path = os.path.join(path_input, filename_input)
            if not os.path.exists(full_path):
                print("File not found. Try again.")
                main()
            f = open(f"{full_path}", "r")
            text = f.read()
            print(text)
            f.close()
        except IOError:
            print("Unable to read file. try again.")
            exit()
    if user_input == "popen":
        try:
            print("This programm only supports: cat and ls commands.")
            command_input = input("Enter which command you want to execute: ")
            if command_input == "cat":
                file_input = input("Enter the name of the file: ")
                path_input = input("Enter the path to the file: ")
                if not os.path.exists(path_input):
                    print("Invalid Path. Try again.")
                    main()
                os.chdir(f"{path_input}")
                file = os.popen("cat " + file_input).read()
                print(file)
            if command_input == "ls":
                path_input = input("Enter the path to the directory: ")
                if not os.path.exists(path_input):
                    print("Invalid Path. Try again.")
                    main()
                os.chdir(f"{path_input}")
                file = os.popen("ls").read()
                print(file)
        except IOError:
            print("Error.")
            exit()
    if user_input == "rename":
        try:
            path_input = input("Enter the path to the file: ")
            if not os.path.exists(path_input):
                print("Invalid Path. Try again.")
                main()
            os.chdir(f"{path_input}")
            file_input = input("Enter the name of the file: ")
            newname_input = input("Enter the new name of the file: ")
            os.rename(file_input, f"{newname_input}")
            print("File renamed.")
        except IOError:
            print("Error.")
            exit()
    if user_input == "path.exists":
        try:
            path_input = input("Enter the path to the file: ")
            if not os.path.exists(path_input):
                print("Invalid Path. Try again.")
                main()
            os.chdir(f"{path_input}")
            file_input = input("Enter the name of the file: ")
            check = os.path.exists(file_input)
            if check == True:
                print("This file exists.")
            elif check == False:
                print("This file does not exist.")
            else:
                print("Error.")
        except IOError:
            print("Error.")
            exit()
    if user_input == "path.getsize":
        try:
            path_input = input("Enter the path to the file: ")
            if not os.path.exists(path_input):
                print("Invalid Path. Try again.")
                main()
            os.chdir(f"{path_input}")
            file_input = input("Enter the name of the file: ")
            size = os.path.getsize(file_input)
            print(size, "Bytes.")
        except IOError:
            print("Error.")
            exit()
main()