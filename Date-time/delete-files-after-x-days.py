import os
import sys
import datetime
req_path = input("Enter the path: ")
age = 3
if not os.path.exists(req_path):
    print("Path exists")
    sys.exit(1)
if os.path.isfile(req_path):
    print("Do provide a directory path")
    sys.exit(2)
today = datetime.datetime.now()
for each_file in os.listdir(req_path):
    each_file_path = os.path.join(req_path,each_file)
    if os.path.isfile(each_file_path): # gonna give us a file path
        file_creation_date = datetime.datetime.fromtimestamp(os.path.getctime(each_file_path))
        # print(each_file_path, datetime.datetime.fromtimestamp(os.path.getctime(each_file_path)))
        # print(dir((today - file_creation_date))) - whatever the operation are there in each object, it gonna find for us
        difference_in_days = (today - file_creation_date).days
        if difference_in_days > age: # it gonna give us the files which are older than 3 days
            os.remove(each_file_path)
            print("Deleted file: ", each_file_path)
            print(each_file_path, difference_in_days)