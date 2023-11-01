'''
import csv
req_path = "/Users/mars/Documents/git-projects/python-automation/CSV/sam.csv"
fo  = open(req_path, 'r')
csv_reader = csv.reader(fo, delimiter="|") # delimiter splits into actual columns
for each_row in csv_reader:
    print(each_row)
fo.close()
'''

import csv
req_path = "/Users/mars/Documents/git-projects/python-automation/CSV/sudhamsh.csv"
fo  = open(req_path, 'w', newline="")
csv_writer = csv.writer(fo, delimiter=",")
'''
csv_writer.writerow(["Name", "Age", "City"])
csv_writer.writerow(["Sudhamsh", "25", "Pune"])
csv_writer.writerow(["Mars", "25", "Pune"])
'''
my_data = [["Name", "Age", "City"], ["Sudhamsh", "25", "Pune"], ["Mars", "25", "Pune"], ["Ashridh", "22", "warangal"]]

csv_writer.writerows(my_data)
fo.close()

