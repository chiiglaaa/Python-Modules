            Lesson 4
    Im making my final project in this lesson.
    i want to make programm which can help you in file management(in a basic way)
    to give you some information about your system.
    and to help manage the basic process.
----------------------------------------------------------------------
New commands used in this project:

    os.uname - returns a tuple containing several system-related details such as operating system, hostname, and kernel version.
    os.cpucount - returns the number of CPUs in the system.
    os.path.join - joins one or more path components (strings) into a single path.
    os.kill - sends a signal to a process with a specified process ID (PID).
    OSError - an error raised when a system function fails, such as file access errors.
    IOError - an error raised when an input/output operation fails, such as when a file cannot be opened or read.

-----------------------------------

example of os.uname:

    uname = os.uname()
    print(uname.sysname, uname.machine, os.name)

Output will be:

    Linux x86_64 posix

    [*] uname.sysname - returns the name of the operating system kernel.  Output is: "Linux"
    [*] uname.machine - returns the machine type or hardware architecture.  Output is:"x86_64"
    [*] os.name - returns the name of the operating system dependent module imported.   Output is:"posix"

-----------------------------------

example of os.cpucount:

    print(f"CPU cores: " + str(os.cpu_count()))

Output will be:

    CPU cores: 8        (in my case it is 8)

-----------------------------------

example of os.path.join:

so if i have some file on Desktop and i have 2 inputs for example.
one is asking the path and other is asking name.

    name = input("What is the name of the file?: ")  #Lets say we wrote "testfile.txt"
    path = input("Where is the file located?: ")  # /home/user/Desktop
    full_path = os.path.join(path, name)  #This will be: /home/user/Desktop/testfile.txt
    
    print(full_path)

Output will be:

    /home/user/Desktop/testfile.txt

-----------------------------------

example of os.kill:

lets say i want to kill some specific process which is running in my computer.
i will get the id of the process with "ps aux | grep {user_name}" command.

    os.kill(id_of_process, 0)  #this will check if give PID exists or not.
    os.kill(id_of_process, 9)  #this will send a 'SIGKILL' signal. in other words this will kill process.

-----------------------------------
    
