import re
my_string = "python is easy and it is easy to master once focussed"
pattern = re.split('i[st]', my_string)
print(pattern)