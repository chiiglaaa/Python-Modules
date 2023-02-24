        Lesson 1 of subprocess module in Python

    DONT FORGET TO "import subprocess" FIRST!!!!
------------------------------------
used functions in this lesson:

    subprocess.run() - this function is used to run a command as a subprocess and capture its output, exit status, and any errors that occur during execution.
    
    stdout = subprocess.PIPE - stdout stands for "standart output". stdout is where a program or command sends its normal output when its run.when you run a program or command in a terminal or command prompt, the output that is printed to the screen is usually the output sent to stdout.this output can be redirected to a file, a pipe, or another program using various Unix commands or Python functions like subprocess.run()
    
    .PIPE, pipe - In Unix-like operating systems, a pipe is a mechanism for inter-process communication(IPC) that allows the output of one process to be directed as input to another process. A pipe is represented by the "|" symbol and can be used to chain together multiple commands or processes so that the output of one is passed as input to the next.(for example these two commands: "ps aux" and "grep user" would look like this: "ps aux | grep user")
    
    subprocess.Popen() - this function is used to launch a new process and execute a command in a similar way to subprocess.run(), but with more control over how the subprocess is launched and how its output is handeled. Unlike subprocess.run(), which waits for the command ro complete and returns a 'CompletedProcess' object, subprocess.Popen() returns a Popen object that represents the running subprocess and can be used to interact with it in various ways.
    
    stderr = subprocess.STDOUT - this is an argument that can be passed to the subprocess.Popen() function to redirect the standart error stream of a subprocess to the same pipe as the standart output stream.if any error messages or output that a subprocess generates will be redirected to the same place as its regular output, making it easier to capture and handle both types of output together.(for example if we run a command that generates both regular output and error messages, we might want to use stderr = subprocess.STDOUT to redirect eroor messages to the same place as the regular outputs so that you can capture and process them together. Thic can be useful for error logging or debuggind purposes, among other things.)

    p.stdout - is a file-like object that represents the standart output stream of a subprocess.

    iter() - is a built-in Python function that takes an iterator(in this case, the readline() method) and a sentinel value(in this case, the byte string 'b'''), and returns an iterator that generates the same values as the original iterator until the sentinel value is reached.
    
    
------------------------------------

example of subprocess.run():

lets see some of the examples of this function:

1)"pwd" command:

    result = subprocess.run(['pwd'], stdout = subprocess.PIPE)
    output = result.stdout.decode('utf-8')
    print(output)

Output will be:

    /home/chiiglaaa/PycharmProjects/abcd/venv


2)"whoami" command:

    result = subprocess.run(['whoami'], stdout=subprocess.PIPE)
    output = result.stdout.decode('utf-8')
    print(output)

Output will be your user name(in my case it is 'chiiglaaa'):

    chiiglaaa


3)"date" command:

    result = subprocess.run(['date'], stdout=subprocess.PIPE)
    output = result.stdout.decode('utf-8')
    print(output)

Output will be:

    Sat Feb 25 02:44:03 AM +04 2023    (that's the time when i execute this function, in your case it will be different)


4)"echo" command:

    result = subprocess.run(['echo', 'Hello, world!'], stdout=subprocess.PIPE)
    output = result.stdout.decode('utf-8')
    print(output)

Output will be:

    Hello, world!


5)"ls -l" command:

    result = subprocess.run(['ls', '-l', '/home/user/Desktop'], stdout=subprocess.PIPE)
    output = result.stdout.decode('utf-8')
    print(output)

Output will be:

    total 496
    -rw-rw-r-- 1 user user   1658 Dec 19 03:20 textfile0
    -rw-rw-r-- 1 user user    607 Feb  7 03:37 textfile1
    drwxrwxr-x 2 user user   4096 Jan 20 00:59 directory0
    -rwxrwxr-x 1 user user    927 Jan 15 02:03 pythonfile0
    -rw-rw-r-- 1 user user   1824 Dec 18 04:13 textfile2
    drwxrwxr-x 5 user user   4096 Feb 19 00:53 directory1
    -rw-rw-r-- 1 user user 408730 Feb 11 15:54 textfile3
    -rw-rw-r-- 1 user user     21 Feb 23 17:36 textfile4
    -rw-rw-r-- 1 user user    100 Feb 10 22:36 textfile5
    -rw-rw-r-- 1 user user   1705 Feb 23 01:43 textfile6
    -rw-rw-r-- 1 user user      0 Feb 25 02:40 textfile7
    -rw-rw-r-- 1 user user   2489 Feb 25 00:18 textfile8
    -rw-rw-r-- 1 user user    717 Feb 24 18:59 textfile9
    -rw-rw-r-- 1 user user  20295 Feb 20 23:26 textfile10
    drwxrwxr-x 4 user user   4096 Feb 19 00:52 dictionary2
    drwxr-xr-x 8 user user   4096 Feb 11 13:56 dictionary3
    drwxrwxr-x 3 user user   4096 Feb 21 17:34 dictionary4
    -rw-rw-r-- 1 user user    572 Feb 12 00:45 textfile11
    -rw-rw-r-- 1 user user   3074 Feb 25 02:30 textfile12
    -rw-rw-r-- 1 user user    127 Dec 23 02:59 pythonfile1
    -rw-rw-r-- 1 user user    202 Feb 25 00:50 pythonfile2
    -rw-rw-r-- 1 user user    597 Dec 30 03:51 pythonfile3

------------------------------------

example of subprocess.Popen():

1)"ls" command:

    p = subprocess.Popen(['ls'], stdout = subprocess.PIPE)
    output = p.communicate()[0].decode('utf-8')
    print(output)

Output will be:

    #This is how my PyCharm venv folder looks like :DDD your definetely looks different.
    abcd.py
    ANSI codes
    binary.py
    bubble_sorting.py
    caesar_bruteforce.py
    caesar_cypher.py
    cryptotest.py
    dictionary
    dict.py
    fibo_google_rec.py
    fibonacci_itterative.py
    fibonacci_recursive.py
    flappuchino
    insertion_sorting.py
    lib
    linear_searching.py
    local
    merge_sorting.py
    merge_sort.py
    os_module.py
    osmodule.py
    otp.py
    __pycache__
    pyvenv.cfg
    sentinel_linear_search.py
    ternery_searching.py
    ternerysearch.py
    test2.py
    test3.py
    test4.py
    test5.py
    test.py
    vigenere_cracking.py
    vigenere_cypher.py
    vigenereModule.py
    word_count.py


2)"ping" command:

    p = subprocess.Popen(['ping', 'google.com'], stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
    
    for line in iter(p.stdout.readline, 'b'):
        print(line.decode('utf-8'), end='')

    p.stdout.close()
    p.wait()

Output will be:

    PING google.com (142.251.141.46) 56(84) bytes of data.
    64 bytes from sof04s07-in-f14.1e100.net (142.251.141.46): icmp_seq=1 ttl=113 time=49.9 ms
    64 bytes from sof04s07-in-f14.1e100.net (142.251.141.46): icmp_seq=2 ttl=113 time=53.3 ms
    64 bytes from sof04s07-in-f14.1e100.net (142.251.141.46): icmp_seq=3 ttl=113 time=50.7 ms
    64 bytes from sof04s07-in-f14.1e100.net (142.251.141.46): icmp_seq=4 ttl=113 time=49.3 ms
    64 bytes from sof04s07-in-f14.1e100.net (142.251.141.46): icmp_seq=5 ttl=113 time=50.7 ms
    64 bytes from sof04s07-in-f14.1e100.net (142.251.141.46): icmp_seq=6 ttl=113 time=50.3 ms
    64 bytes from sof04s07-in-f14.1e100.net (142.251.141.46): icmp_seq=7 ttl=113 time=53.4 ms

------------------------------------
