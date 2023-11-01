# Reading csv file
'''
import csv
req_path = "/Users/mars/Documents/git-projects/python-automation/CSV/info.csv"
fo  = open(req_path, 'r')
content = fo.readlines()
# print(list(content))
fo.close()
for each_row in content:
    print(each_row.strip("\n").split(","))
'''
'''
import csv
req_path = "/Users/mars/Documents/git-projects/python-automation/CSV/info.csv"
fo  = open(req_path, 'r')
csv_reader = csv.reader(fo, delimiter=',')
for each_row in csv_reader:
    print(each_row)
fo.close()
'''


import csv
req_path = "/Users/mars/Documents/git-projects/python-automation/CSV/sam.csv"
fo  = open(req_path, 'r')
csv_reader = csv.reader(fo, delimiter="|") # delimiter splits into actual columns
for each_row in csv_reader:
    print(each_row)
fo.close()


