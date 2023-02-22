        Lesson 1

import os  (VERY FIRST THING TO DO BEFORE USING OS MODULE IN PYTHON)

-----------------------------------

topics in this lesson:

    os.remove - remove files
    os.rmdir - remove empty dirs
    os.mkdir - makes dirs - same as linux mkdir command
    mode = 0o666 - give only root user rw permissions
    os.getcwd - same as pwd command in terminal which prints your current working dir
    os.chdir - same as cd command in terminal which changes your working dir
    os.listdir(path) - same as ls/l command in terminal which shows you files of your current working dir
    os.name - this function gives the name of the operating system dependent module imported. the following names have currently been registered: ‘posix’, ‘nt’, ‘os2’, ‘ce’, ‘java’ and ‘riscos’.
    

-----------------------------------

example of os.getcwd:

this function is similar as pwd command in Linux Terminal. it will print our working directory(current).

    simply just write --> print(os.getcwd())

or

    cwd = os.getcwd()

    print("Current working directory:", cwd)

-----------------------------------

example of os.chdir:

this function is similar as cd command in Linux Terminal. it will change our working directory(current).

for example if our path is "~/Desktop" and we want to change our directory and go to "/" root directory:

    os.chdir('/')

if we print our os.getcwd() we will find ourself in '/' root dir.

-----------------------------------

example of os.mkdir:

if we want to make directory for example on "~/Desktop"

    directory = "name of dir"
    location = "/home/user/Desktop/"
    path = os.path.join(location, directory)

    os.mkdir(path)
    print("Directory '% s' created" % directory)

if we want to give only root user permission to read and write in that directory we would add "mode = 0o666"
which look like this:

    directory = "name of dir"
    location = "/home/user/Desktop/"
    mode = 0o666
    path = os.path.join(location, directory)

    os.mkdir(path, mode)
    print("Directory '% s' created" % directory)

-----------------------------------

example of os.remove:

if we want to remove file from somewhere we will need to use os.remove function.

    file = 'filename.txt'
    location = "/home/user/Desktop/"
    path = os.path.join(location, file)

    os.remove(path)

-----------------------------------

example of os.rmdir:

if we want to remove an EMPTY directory from somewhere we will need to use os.rmdir function.
but remember if our written directory contains any kind of info we will get Error message.

    directory = "name_of_dir"
    location = "/home/user/Desktop/"
    path = os.path.join(location, directory)

    os.rmdir(path)

-----------------------------------

example of os.listdir:

this function is similar as ls/l function in Linux Terminal. it will show us all files in out written directory.

    path = "/"
    dir_list = os.listdir(path)

-----------------------------------

example of os.name:

    print(os.name)

    1)posix: This indicates a Unix or Linux-based operating system, such as macOS, Ubuntu, or Debian.
    2)nt: This indicates a Windows operating system, such as Windows 10 or Windows Server.
    3)os2: This indicates an IBM OS/2 operating system.
    4)ce: This indicates a Windows CE operating system, which is a stripped-down version of Windows designed for embedded systems and mobile devices.
    5)java: This indicates a Java-based operating system, such as JavaOS or JNode.
    6)riscos: This indicates a RISC OS operating system, which is designed for ARM-based computers.

-----------------------------------


