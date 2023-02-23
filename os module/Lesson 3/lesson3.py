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
    print("\033[37m" + "[*]" + "\033[0m" + " basename - return the basename of the file from given path.")
    print("\033[37m" + "[*]" + "\033[0m" + " dirname - return the directory name of the given path.")
    print("\033[37m" + "[*]" + "\033[0m" + " isabs - check if the given path is absolute.")
    print("\033[37m" + "[*]" + "\033[0m" + " isdir - check if the given path is a directory.")
    print("\033[37m" + "[*]" + "\033[0m" + " isfile - check if the given path is a file.")
    print("\033[37m" + "[*]" + "\033[0m" + " normcase - return the normalized case of the given string.")
    print("\033[37m" + "[*]" + "\033[0m" + " normpath - return the normalized path of the given path.")
    print()
    print("    to quit use ctrl+c ")
    print()

ask()
user_input = input("What would you like to do?: ")

def main():
    if user_input == "basename":
        try:
            path_input = input("Enter the path: ")
            print(os.path.basename(path_input))
        except IOError:
            print("Error. try again.")
            exit()
    if user_input == "dirname":
        try:
            path_input = input("Enter the path: ")
            print(os.path.dirname(path_input))
        except IOError:
            print("Error. try again.")
            exit()
    if user_input == "isabs":
        try:
            path_input = input("Enter the path: ")
            print(os.path.isabs(path_input))
        except IOError:
            print("Error. try again.")
            exit()
    if user_input == "isdir":
        try:
            path_input = input("Enter the path: ")
            print(os.path.isdir(path_input))
        except IOError:
            print("Error. try again.")
            exit()
    if user_input == "isfile":
        try:
            path_input = input("Enter the path: ")
            print(os.path.isfile(path_input))
        except IOError:
            print("Error. try again.")
            exit()
    if user_input == "normcase":
        try:
            path_input = input("Enter the path: ")
            print(f"Original Path: {path_input}")
            print(f"Normalised Path: {os.path.normcase(path_input)}")
        except IOError:
            print("Error. try again.")
            exit()
    if user_input == "normpath":
        try:
            path_input = input("Enter the path: ")
            print(f"Original Path: {path_input}")
            print(f"Normalised Path: {os.path.normpath(path_input)}")
        except IOError:
            print("Error. try again.")
            exit()

main()