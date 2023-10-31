# Read a directory path and identify all files and directories
import os
import sys
path = input("Enter the path: ")
if os.path.exists(path):
    files_and_dirs = os.listdir(path)
else:
    print("Path does not exist")
    sys.exit()
list_of_dir_files = os.listdir(path)
print("it list all the files and directories: ", list_of_dir_files)
for each_file_or_dir in list_of_dir_files:
    file_or_dir_path = os.path.join(path, each_file_or_dir)
    if os.path.isdir(file_or_dir_path): # we're checking if, else for each item in the for loop, that which iterates list
        print(f"it's a directory: {each_file_or_dir}")
    else:
        print(f"it's a file: {each_file_or_dir}")
