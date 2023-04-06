#       Lesson 4 of subprocess module in python

------------------------------------

Used functions and arguments in this lesson.

    .check_call() - this function is same as .run()
                 function with check=True argument.

                 it runs a command and waits for it
                 to complete. If the command returns 
                 a non-zero exit code, it will raise 
                 a 'CalledProcessError'.

    .check_output() - this function is same as using
                 check=True and stdout=subprocess.PIPE
                 arguments in .run or .Popen functions.

                 it runs a command and captures its 
                 output. If the command returns a 
                 non-zero exit code, it will raise a 
                 'CalledProcessError'.
    
    .call() - this function is used to execute a 
                 command as a subprocess and wait for it
                 to complete. It return the return code
                 of the subprocess.

                 it runs a command and waits for it to
                 complete. If returns the exit code of
                 the command.

### subprocess.Popen() arguments:

    close_fds - argument is used to specify whether or not
                to close all file descriptors (e.g., open files, pipes)
                before starting the new process. If set to 
                True, all file descriptors except 0, 1 and 2
                (stdin, stdout and stderr) will be closed.
                
                This is useful for preventing the child process
                from inheriting unnecessary file descriptors
                from the parent process, which could cause
                problems.

    pass_fds - argument is used to specify a list of file
                descriptors that should be passed to the 
                child process.

                This can be useful for passing open file
                descriptors(e.g., for communication between
                the parent and child process.)

    group - argument is used to specify the process group ID
                to which the new process will belong.

                This can be useful for sending signals 
                to a group of processes.

    extra_groups - argument is used to specify a list of 
                supplementary group IDs for the new process.

                This can be useful for granting the process
                additional permissions.

    user - argument is used to specify the user ID or username
                under which to run the new process.

                This can be useful for running the process
                with different permissions or privileges.

    umask - argument is used to specify the file creation mask
                for the new process.

                This can be useful for setting the default
                permissions for new files created by the process.

    pipesize - argument is used to specify the buffer size for
                pipes used for interprocess communication.

                This can be useful for controlling the amount
                of data that can be buffered in the pipe.

    process_group - argument is used to specify whether the new
                process should be part of its own process group.

                This can be useful for sending signals to the
                process or its children.

    startupinfo - argument is used to specify additional startup
                information for the new process.

                This can include the working directory, environment
                variables, and other settings.

    preexec_fn - argument is vallable object that gets called just
                before the new process is spawned.

                It can br used to set up signal handlers, change the
                current working directory, or perform any other
                neccesary setup before the new process is created.

    creationflags - argument is a set of flags that control how the
                new process is created. On Windows, this argument
                can be used to set various process creation flags
                such as 'CREATE_NEW_CONSOLE' or 'DETACHED_PROCESS'.
                On Unix-based systems, this argument is ignored.

    restore_signals - argument controls whether the new process should
                restore the signal handlers to their default values.
                
                If set to 'True', the new process will restore the
                signal handlers. If set to 'False', the new process
                will inherit the signal handlers from the parent process.

                On Unix-based systems, this argument is ignored.

    bufsize - argument controls the size of the I/O buffer used by
                the new process for stdout and stderr.

                By default, the buffer size is set to '-1', which
                means that the buffer size is determined by the
                underlying operating system.

                If you set 'bufsize' to '0', the I/O streams will be
                unbuffered.

                If you set 'bufsize' to a positive integer, the I/O
                streams will use a buffer of that size.
    
------------------------------------

## Examples:

### Example of .check_call() function:

    import subprocess
    
    subprocess.check_call(['ls', '-l'])

Output:

    total 96
    -rw-rw-r--  1 user user  294 Feb 27 16:07  filename
    -rw-rw-r--  1 user user 2247 Feb  3 05:57  filename
    -rw-rw-r--  1 user user 1161 Feb  3 05:58  filename
    -rw-rw-r--  1 user user 1103 Feb 24 15:16  filename
    -rw-rw-r--  1 user user 2726 Feb 11 00:31  filename
    drwxr-xr-x 10 user user 4096 Mar 30 17:40  Desktop
    drwxrwxr-x  3 user user 4096 Dec 18 00:16  Dev
    drwxr-xr-x  2 user user 4096 Feb 12 00:13  Documents
    drwxr-xr-x  2 user user 4096 Mar 30 23:13  Downloads
    drwxrwxr-x  4 user user 4096 Feb  2 04:16  FolderName
    drwxrwxr-x  5 user user 4096 Feb 21 17:20  FolderName
    -rw-rw-r--  1 user user 1297 Feb 11 02:29  FolderName
    drwxr-xr-x  2 user user 4096 Nov 23 19:34  Music
    drwxrwxr-x  2 user user 4096 Feb 24 00:46  filename
    drwxr-xr-x  2 user user 4096 Nov 23 19:34  Pictures
    drwxrwxr-x  3 user user 4096 Feb 12 00:24  FolderName
    drwxr-xr-x  2 user user 4096 Nov 23 19:34  Public
    drwxrwxr-x  5 user user 4096 Feb  2 04:15  FolderName
    drwx------  4 user user 4096 Feb 12 00:18  filename
    drwxr-xr-x  2 user user 4096 Nov 23 19:34  Templates
    drwxr-xr-x  2 user user 4096 Nov 23 19:34  Videos
    drwxrwxr-x  2 user user 4096 Feb  7 03:35  FolderName
    drwxrwxr-x  3 user user 4096 Mar 15 22:12  FolderName
    drwxrwxr-x  2 user user 4096 Jan 28 17:50  FolderName
    0

------------------------------------

### Example of .check_output() function:

    import subprocess
    
    output = subprocess.check_output(['ls', '-l'])
    print(output)

Output:

    b'total 96\n-rw-rw-r--  1 user user  294 Feb 27 16:07 asdasdasdasd\n-rw-rw-r--  1 user user 2247 Feb  3 05:57 asdf\n-rw-rw-r--  1 user user 1161 Feb  3 05:58 asdfa\n-rw-rw-r--  1 user user 1103 Feb 24 15:16 asdfg\n-rw-rw-r--  1 user user 2726 Feb 11 00:31 beyond basic stuff in python\ndrwxr-xr-x 10 user user 4096 Mar 30 17:40 Desktop\ndrwxrwxr-x  3 user user 4096 Dec 18 00:16 Dev\ndrwxr-xr-x  2 user user 4096 Feb 12 00:13 Documents\ndrwxr-xr-x  2 user user 4096 Mar 30 23:13 Downloads\ndrwxrwxr-x  4 user user 4096 Feb  2 04:16 Flask\ndrwxrwxr-x  5 user user 4096 Feb 21 17:20 gnome-terminal\n-rw-rw-r--  1 user user 1297 Feb 11 02:29 modules\ndrwxr-xr-x  2 user user 4096 Nov 23 19:34 Music\ndrwxrwxr-x  2 user user 4096 Feb 24 00:46 onlytest\ndrwxr-xr-x  2 user user 4096 Nov 23 19:34 Pictures\ndrwxrwxr-x  3 user user 4096 Feb 12 00:24 Postman\ndrwxr-xr-x  2 user user 4096 Nov 23 19:34 Public\ndrwxrwxr-x  5 user user 4096 Feb  2 04:15 PycharmProjects\ndrwx------  4 user user 4096 Feb 12 00:18 snap\ndrwxr-xr-x  2 user user 4096 Nov 23 19:34 Templates\ndrwxr-xr-x  2 user user 4096 Nov 23 19:34 Videos\ndrwxrwxr-x  2 user user 4096 Feb  7 03:35 VSC\ndrwxrwxr-x  3 user user 4096 Mar 15 22:12 VSCode\ndrwxrwxr-x  2 user user 4096 Jan 28 17:50 Warpinator\n'

------------------------------------

### Example of .call() function:

    import subprocess
    
    retcode = subprocess.call(['ls', '-l'])
    print(retcode)

Output:

    0

------------------------------------

## examples of subprocess.Popen arguments

### close_fds

    import subprocess
    
    # Close all file descriptors except stdin, stdout, and stderr
    subprocess.Popen(command, close_fds=True)

------------------------------------

### pass_fds

    import subprocess
    import os
    
    # Create a pipe and pass the write end to the child process
    read_fd, write_fd = os.pipe()
    p = subprocess.Popen(command, pass_fds=[writre_fd])

------------------------------------

### group

    import subprocess
    
    # Create a process group
    pgid = os.getpid()
    os.setpgid(pgid, pgid)
    
    # Start a new process in the same group
    subprocess.Popen(command, group=pgid)

------------------------------------

### extra_groups

    import subprocess
    import os
    
    # Get the current list of group IDs for the process
    groups = os.getgroups()

    # Add a new group ID to the list
    groups.append(1000)
    
    # Start a new process with the updatged group list
    subprocess.Popen(command, extra_groups=groups)

------------------------------------

### user

    import subprocess
    
    # Start a new process as the user "www-data"
    subprocess.Popen(command, user="www-data")

------------------------------------

### umask

    import subprocess
    
    # Start a new process with a umask of 0o22 (i.e., 755)
    subprocess.Popen(command, umask=0o22)

------------------------------------

### pipesize

    import subprocess
    
    # Start a new process with a pipe buffer size of 1 MB
    subprocess.Popen(command, pipesize=1024*1024)

------------------------------------

### process_group

    import subprocess
    
    # Start a new process in its own process group
    subprocess.Popen(command, process_group=True)

------------------------------------

### startupinfo

    import subprocess
    
    # Define the startupinfo object
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.cwd = 'home/my_folder' # set the working directory to /home/my_folder
    startupinfo.env = {'VAR_NAME': 'VAR_VALUE'} # set the environment variable VAR_NAME to VAR_VALUE
    
    # Start a new process with the specified startupinfo
    subprocess.Popen(['python', 'my_script.py'], startupinfo=startupinfo)

------------------------------------

### preexec_fn

    import os
    import subprocess
    
    def preexec_func():
        # Ignore the SIGINT signal (Ctrl-C) in the child process
        os.setpgrp()
        signal.signal(signal.SIGINT, signal.SIG_IGN)
    
    subprocess.Popen(['my_command'], preexec_fn=preexec_func)

------------------------------------

### creationflags

    import subprocess
    
    # Start a new process with a new console window on Windows
    subprocess.Popen(['my_command'], creationflags=subprocess.CREATE_NEW_CONSOLE)

------------------------------------

### restore_signals

    import subprocess
    
    # Start a new process and inherit the signal handlers from the parent process
    subprocess.Popen(['my_command'], restore_signals=False)

------------------------------------

### bufsize

    import subprocess
    
    # Start a new process with a stdout buffer size of 1024 bytes
    subprocess.Popen(['my_commmand'], bufsize=1024)
