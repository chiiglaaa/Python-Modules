        Lesson 2

DONT FORGET TO IMPORT OS!!!

------------------------------

    .open - this will open out file but we need to specify the path.
    .read - this will read out file.
    os.popen - with this function we can execute shell command and obtain output as a file-like object.
    os.close - this is necessary function when we are opening a file. if file is opened with open() and we try to close it with os.close() python would throw TypeError.
    os.rename - with this function we can rename a file. file name would change only if the file exists and the user have permission to change the file.
    os.path.exists - this will check whether a file exists or not by passing the name of the file as a parameter, but it will only work if we are in the same directory where the file is.
    os.path.getsize - this will give us the size of the file in bytes.
    
     
------------------------------

example of how to open, read and close file:

for example if i want to open file from my Desktop we need to change our working dir to Desktop.
which we already know how to do:   

    os.chdir("PATH")
    #after that we need to specify the file name.

    file_name = 'name'
    #now lets open file
    
    f = open(file_name, 'r')  # its now necessary to call f to open file its just for example. 'r' stand for read. 'w' stand for write.
    text = f.read()
    print(text)
    
    #FINALLY DONT FORGET TO CLOSE OPENED FILE.
    f.close()

------------------------------

example of os.popen:

as we know popen allows us to execute shell commands like: ls, cd, cat etc.

cat example:

    filename = 'name'
    file = os.popen("cat " + filename).read()
    print(file)

ls example:
    
    #lets change our working dir.
    os.chdir("path")
    file = os.popen("ls").read()
    print(file)

------------------------------

example of os.rename:

    filename = 'old_name'
    os.rename(filename, "new_name")

------------------------------

example of os.path.exists:

lets say im searching 2 files. 1 file is in our working dir and other is not.

    file1 = 'thisoneexists'
    file2 = 'thisdoesnot'
    print(os.path.exists(file1))
    print(os.path.exists(file2))

Output:   on file1 we will get: True
          on file2 we will get: False

------------------------------

example of os.path.getsize:

    file_name = 'name'
    print(os.path.getsize(file_name))

------------------------------
