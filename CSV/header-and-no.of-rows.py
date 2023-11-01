import csv
req_path = "/Users/mars/Documents/git-projects/python-automation/CSV/info.csv"
fo  = open(req_path, 'r')
content = csv.reader(fo, delimiter = ",")
# print(f"The header is:\n {list(content)[0]}")
header = next(content)
# print(len(list(content)))
print(f"The header is:\n {header}")
'''
for each_row in content:
    print(each_row)
'''
fo.close()
