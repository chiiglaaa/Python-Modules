#        Lesson 3 of subprocess module in python

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
               specify how encoding errors should be handled 
               when decoding the output of a subprocess.

               If the subprocess output contains characters that
               are not valid in the target encoding, a
               'UnicodeDecodeError' will be raised.

               "strict": raise a 'UnicodeError' if an error occurs
               during encoding or decoding.

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

    env=None - Argument sets the environment variables for 
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

    input=None - This argument is used to provide input to the
               subprocess as a byte string.
    
    text=None - This argument is similar to 'input', but it is
               used to provide input to the subprocess as a 
               Unicode string.

------------------------------------

##  Examples:


### Example of 'cwd' argument:

    import subprocess
    
    subprocess.run(['ls', '-l'], cwd='/home/user')

This Python code will run the 'ls -l' command in the directory '/home/user'

------------------------------------

### Example of 'timeout' argument:

    import subprocess
    
    try:
        subprocess.run(['sleep', '10'], timeout=5)
    except subprocess.TimeoutExpired:
        print("Process timed out!")

This code will run the 'sleep 10' command, which will sleep for 10 second.
However, since we set the timeout to 5 seconds, the 'TimeoutExpired' 
exception will be raised after 5 second.

------------------------------------

### Example of 'encoding' argument:

    import subprocess
    
    result = subprocess.ruin(['ls'], stdout=subprocess.PIPE, encoding='utf-8')
    print(result.stdout)

In this example, the ls command is run and the output is captured using 
the subprocess.PIPE option. The encoding argument is set to 'utf-8' to 
decode the output as UTF-8 text. The output is then printed to the console 
using print().

------------------------------------

### Example of 'env' argument:

    import subprocess
    
    subprocess.run(['printenv', 'PATH'], env={'PATH': 'my/custom/path'})

This code will run the 'printenv PATH' command with a custom 'PATH' 
environment variable.

------------------------------------

### Example of 'universal_newline' argument:

    import subprocess
    
    result = subprocess.run(['echo', 'hello\nworld'], capture_output=True, text=True)
    print(result.stdout)

This code will run the 'echo hello\nworld' command and capture its output.
The 'text=True' argument tells 'subprocess' to open the pipes in text mode
with the default encoding and universal newline support.

------------------------------------

### Example of 'input' argument:

    import subprocess
    
    output = subprocess.run(['my_program'], input=b'Hello World', stdout=subprocess.PIPE)

This code will run the 'my_program' and pass the input data to it
standart input channel.

------------------------------------

### Example of 'text' argument:

    import subprocess

    output = subprocess.run(['my_program'], text='Hello World', stdout=subprocess.PIPE)

This code will run the 'my_program' and pass the input data to it
standart input channel.

------------------------------------

### Example of 'errors' argument:

Lets start with 'strict':

    import subprocess
    
    s = 'Hello, 世界!'
    
    try:
        subprocess.run(['echo', s.encode('ascii', errors='strict')])
    except subprocess.CalledProcessError as e:
        print(e)

Output:

    Traceback (most recent call last):
        File "<stdin>", line 3, in <module>
    UnicodeEncodeError: 'ascii' codec can't encode character '\u4e16' in position 7: ordinal not in range(128)

------------------------------------

'ignore':

    import subprocess
    
    s = 'Hello, 世界!'
    
    subprocess.run(['echo', s.encode('ascii', errors='ignore')])

Output:

    b'Hello, !\n'

Note that the non-ASCII character has been removed from the output.

------------------------------------

'replace':

    import subprocess
    
    s = 'Hello, 世界!'
    
    subprocess.run(['echo', s.encode('ascii', errors='replace')])

Output:

    b'Hello, ??!\n'

Note that the non-ASCII character has been replaced with '??'.

------------------------------------

'backslashreplace':

    import subprocess
    
    s = 'Hello, 世界!'
    
    subprocess.run(['echo', s.encode('ascii', errors='backslashreplace')])

Output:

    b'Hello, \\u4e16\\u754c!\n'

Note that the non-ASCII character has been replaced with its
Unicode escape sequence.

------------------------------------

'xmlcharrefreplace':

    import subprocess
    
    s = 'Hello, 世界!'
    
    subprocess.run(['echo', s.encode('ascii', errors='xmlcharrefreplace')])

Output:

    b'Hello, &#19990;&#30028;!\n'

Note that the non-ASCII character has been replaced with its
XML character reference.
