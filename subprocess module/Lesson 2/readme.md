        Lesson 2 of subprocess module in Python

------------------------------------
Used functions in this lesson:

    shell=True - tells the system to execute a command as if it were typed
                into the command-line interface. This means that the command 
                can use shell features, but may also introduce security risks
                if the command includes untrusted input.

    check=True - tells the system to raise an error if the command being
                executed returns a non-zero exit code. This means that if the
                command fails to run or encounters an error, the 
                'subprocess.run()' function will raise a 'CalledProcessError'
                exception with details about the error. Using 'check=True' is
                a convenient way to ensure that your Python code halts when
                the command it runs fails to execute successfully

    subprocess.CalledProcessError - returns a non-zero exit status. It 
                provides information about the command that failed, the exit
                code and any output or errors generataed by the command.

                non-zero exit status - in simple terms, means that a command
                 executed by the computer has encountered an error or some
                 unexcepted behaviour. When a program or command runs 
                 successfully, it generally returns a zero exit status.

    subprocess.DEVNULL - is a way to tell Python to throw away any output or
                errors generated by a command that is executed using subprocess.

                in other words, when you use 'subprocess.DEVNULL', any output
                or error messages that would normally be sent to the console or
                a file are instead discarded and not visible to the user.

    .communicate() - function allows you to send data to a process and read its
                output generated by the process. This is useful when you need to
                capture the output of a command that is run using 'subprocess'. 
        
    .returncode - attribute is used to determine the exit status of a child 
                process launched using run() or Popen() functions.

                it allows you to check the exit code of a subprocess after it has
                completed running. If the subprocess completed successfully, the
                value will be zero. If an error occurred duting execution, the
                value will be non-zero, indicating that there was a problem.

                its a simple way to check if a subprocess completed succssfully
                or encountered an error.

------------------------------------

Example of shell and .returncode:

    completed = subprocess.run('echo $HOME', shell=True)
    print('returncode:', completed.returncode)

Output:

    /Users/name
    returncode: 0

------------------------------------

Example of check and subprocess.CalledProcessError:

    try:
        subprocess.run(['false'], check=True)
    except subprocess.CalledProcessError as err:
        print('ERROR:', err)

Output:

    ERROR: Command '['false']' returned non-zero exit status 1

------------------------------------

Example of subprocess.DEVNULL:
example 1:

    subprocess.run(['echo', 'hello'], stdout=subprocess.DEVNULL)

Output:

    CompletedProcess(args=['echo', 'hello'], returncode=0)

-------------------------------------

Example of .communicate():

    output = subprocess.Popen(["echo", "hello"], stdout=subprocess.PIPE)
    stdout, stderr = output.communicate()

    print(stdout.decode())

Output:

    hello
