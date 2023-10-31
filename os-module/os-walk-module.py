# os.walk() - used to generate directory and files names in a directory tree by walking
# find / -name <filename>
import os
path = "/Users/mars/Documents/git-projects/python-automation/os-module"
# print(list(os.walk(path))) # first gonna give us a object then gonna generate a list after appending the list operation
for r, d, f in os.walk(path): # r - root directory/relative-path, directory - directory, f - file
    if len(f) != 0:
        # print(r)
        for each_file in f:
            print(os.path.join(r, each_file))
        print('path of file in directroy ends here')    