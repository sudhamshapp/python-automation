'''
import re
# print(dir(re))
text = "This for python and there are two major versions python2 and python3 and in future python4"
# pattern = r"\bpython\b"
# pattern = r"\bpython2\b"
# pattern = r"\bpython[23]\b"
pattern = r"\bpython[23]?\b"
pattern = r"\bpython\d?\b"
result = re.findall(pattern, text)
print(result)
'''

'''
# search operstion
import re
text = "This for python and there are two major versions python2 and python3 and in future python4"
pattern = r"\bpython[23]?\b"
match_object = re.search(pattern, text)
if match_object:
    print(match_object.group()) # gives matched string outta object
    print("starting index: ", match_object.start()) # gives starting index
    print("ended index: ", match_object.end()) # gives ending index
    print("Length: " , match_object.start() - match_object.end())
else:
    print("No match found")
'''

# match operation

import re
text = "python and there are two major versions python2 and python3 and in future python4"
pattern = r"\bpython[23]?\b"
match_object = re.match(pattern, text) # searches the desired stuff at index[0]
if match_object:
    print(match_object.group()) # gives matched string outta object
    print("starting index: ", match_object.start()) # gives starting index
    print("ended index: ", match_object.end()) # gives ending index
    print("Length: " , match_object.start() - match_object.end())
else:
    print("No match found")

