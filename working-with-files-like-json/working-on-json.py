'''
# Read content from json
import json
req_file = "arbitary.json" # we took this json data from chatgpt
fo = open(req_file, "r")
print(json.load(fo)) # this gonna give us a dictionary
# print(type(fo.read())) # this gonna give us a string, this for reference, we should use json load to perform some activity
fo.close()
'''
# write content to json
import json
my_dict = {"name": "John", "age": 30, "city": "New York"}
req_file = "arbitary1.json"

fo = open(req_file, "w")
json.dump(my_dict, fo, indent=4)
fo.close()
