# find-files-in-a-directory-with-desired-extension with .py, .sh, .txt, .log
import os
req_path = input("enter your directory path: ")
req_ext = input("enter your extension .py/.sh/.txt/.log: ")
if os.path.isfile(req_path):
    print("it is a file path, do enter the directory path")
else:
    desired_files = []
    for file in os.listdir(req_path):
        if file.endswith(req_ext):
            desired_files.append(file)
    print(f"these are desired list of files: {desired_files}")            
