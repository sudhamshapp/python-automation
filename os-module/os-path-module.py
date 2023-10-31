# os.path is a sub module of os
# os.path module is used to work with file/directory paths
import os
print(dir(os.path))
print(os.path.sep)
path = "/Users/mars/Documents/git-projects/python-automation/os-module"
print(os.path.basename(path))
print(os.path.dirname(path))
print(os.path.split(path)) # split the path into a tuple of (dirname, basename)
# path1 = "ec2"
# path2 = "s3"
# print(os.path.join(path1, path2)) # gonna combine a path based on the os
print(os.path.exists(path)) # check if the path exists, if exists gonna give a boolean
print(os.path.isdir(path)) # check if the path is a directory
print(os.path.isfile(path)) # check if the path is a file
print(os.path.getsize(path)) # get the size of the file
