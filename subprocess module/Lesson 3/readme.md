#        Lesson 3 of subprocess module in python

------------------------------------

Lets talk about arguments in 'subprocess.run' function.
'subprocess.run' function runs a command with arguments and waits for it to
complete. It returns a 'CompletedProcess' instance that represents the result
of running the command. This function is a high-level interface to 'Popen' and
is recommended for most use cases.

    cwd=None - Argument sets the current working directory
               of the child process.

               If set to 'None'(which is the default), the
               child process inherits the working directory
               of the parent process.

    timeout=None - Argument sets the maximum amount of time
               (in seconds) that the process is allowed to 
               run.

               If the process exceeds the timeout, a
               'TimeoutExpired' exception is raised.
                   
               If set to 'None'(which is default), the
               process is allowed to run indefinetely.

    encoding=None - Argument sets the character encoding 
               used for the input/output/error pipes of the 
               child process.

               If set to 'None'(which is default), the 
               character encoding is determined by the system.

    errors=None - Argument is a parameter that can be passed to
               specify how encoding errors should be handeled 
               when decoding the output of a subprocess.

               If the subprocess output contains characters that
               are not valid in the target encoding, a
               'UnicodeDecodeError' will be raised.

               "strict": ignore any invalid characters and 
               continue decoding.

               "ignore": ignore any invalid characters and continue 
               decoding.

               "replace": replace any invalid characters with the 
               Unicode replacement character ("\ufffd") and continue 
               decoding.

               "backslashreplace": replace any invalid characters 
               with backslash escape sequences ("\xhh") and continue 
               decoding.

               "xmlcharrefreplace": replace any invalid characters 
               with XML character references ("&xhh;") and continue 
               decoding.

    env=None - Argument sets the environment variabnles for 
               the child process. 

               If set to 'None'(which is default), the child 
               process inherits the environment variables of 
               the parent process.

    universal_newline=None - This argument sets whether the
               input/output/error pipes of the child process 
               are opened in text mode with universal newline 
               support. 

               If set to 'True', the pipes are opened in text
               mode with universal newline support.

               If set to 'False', the pipes are opened in 
               binary mode.

               If set to 'None'(which is default), the mode is
               determined by the 'text' argument.

    start_new_session=False - Argument sets whether the child 
               process runs in a new session.

               If set to 'True', the child process runs in a 
               new session.

               If set to 'False'(which is default), the child 
               process runs in the same session as the parent
               process.

    pass_fds() - Argument allows you to specify a set of file 
               descriptors to be passed to the child process.

               The file descriptors are specified as a sequence. 

------------------------------------

#  Examples:

------------------------------------

###Example of 'cwd' argument:

    import subprocess
    
    subprocess.run(['ls', '-l'], cwd='/home/user')

This Python code will run the 'ls -l' command in the directory '/home/user'

------------------------------------

###Example of 'timeout' argument:

    import subprocess
    
    try:
        subprocess.run(['sleep', '10'], timeout=5)
    except subprocess.TimeoutExpired:
        print("Process timed out!")

This code will run the 'sleep 10' command, which will sleep for 10 second.
However, since we set the timeout to 5 seconds, the 'TimeoutExpired' 
exception will be raised after 5 second.

------------------------------------

###Example of 'encoding' argument:

    import subprocess
    
    result = subprocess.ruin(['echo', 'hello'], capture_output=True, text=True)
    print(result.stdout)

This code will run the 'echo hello' command and capture its output.
The 'text=True' argument tells 'subprocess' to open the pipes in text mode
with the default encoding.

------------------------------------

###Example of 'env' argument:

    import subprocess
    
    subprocess.run(['printenv', 'PATH'], env={'PATH': 'my/custom/path'})

This code will run the 'printenv PATH' command with a custom 'PATH' 
environment variable.

------------------------------------

###Example of 'universal_newline' argument:

    import subprocess
    
    result = subprocess.run(['echo', 'hello\nworld'], capture_output=True, text=True)
    print(result.stdout)

This code will run the 'echo hello\nworld' command and capture its output.
The 'text=True' argument tells 'subprocess' to open the pipes in text mode
with the default encoding and universal newline support.

------------------------------------

###Example of 'start_new_session' argument:

    import subprocess
    
    subprocess.run(['nohup', 'mycommand'], start_new_session=True)

This code will run the 'nohup mycommand' command in a new session.

