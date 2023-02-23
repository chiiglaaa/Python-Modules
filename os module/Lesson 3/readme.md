        Lesson 3
    we will talk about os.path in this lesson.
-----------------------------------
Topics in this lesson:
    os.path.basename - this function is used to return the basename of the file.
    os.path.dirname - this fucntion is used to return the directory name from the given path.
    os.path.isabs - this function is used to determine whether a given path is an absolute or relative.
    os.path.isdir - this function specifies whether given path is existing directory or not.
    os.path.isfile - this function specifies whether the path is existing file or not.
    os.path.normcase - this function normalizes the case of the pathname specifies.(this is useful on windows os because windows is a case-insensitive file system)
    os.path.normpath - this function normalizes the path names by collasing redundant separators and up-level references. on windows it converts forward slashes to backward slashes.
    
-----------------------------------

example of os.path.basename:

    print(os.path.basename("/home/user/Desktop/file_name"))

output will be: file_name

-----------------------------------

example of os.path.dirname:

    print(os.path.dirname("/home/user/Desktop/file_name"))

output will be: /home/user/Desktop/

-----------------------------------

example of os.path.isabs:

    print(os.path.isabs("/home/user/Desktop/file_name"))
output in this case will be: True

    print(os.path.isabs("Desktop/file_name"))
output in this case will be: False

-----------------------------------

example of os.path.isdir:

    print(os.path.isdir("/home/user/Desktop"))
output in this case will be: True

    print(os.path.isdir("/home/user/notDesktop"))    (note that this is just example and there might be someone who somehow named Desktop "notDesktop" ;D)
output in this case will be: False

-----------------------------------

example of os.path.isfile:

for example i have "file" on Desktop.

    print(os.path.isfile("/home/user/Desktop/file_name"))
output in this case will be: True

    print(os.path.isfile("/home/user/Desktop/not_existing_file_name"))
output in this case will be: False

-----------------------------------

example of os.path.normcase:


