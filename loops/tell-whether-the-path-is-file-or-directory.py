# find-files-in-a-directory-with-desired-extension
import os
req_path = input("enter your path: ")
if os.path.exists(req_path):
    print("The given path {req_path} exists")
    if os.path.isdir(req_path):
        print("The given path {req_path} is a file")
    else:
        print("The given path {req_path} is a directory")
else:
    print("The given path {req_path} does not exist")