'''
import re
text = "There is a python installed on a machine, we can switch b/w python2 and python3"
pattern = r"\bpython[23]?\b"
matches = re.findall(pattern, text)
print(matches)
'''


import re
text = "There is a python installed on a machine, we can switch b/w python2 and python3"
pattern = r"\bpython[23]?\b"
matches = re.finditer(pattern, text)
# print(matches) # finditer gonna give us a object
for match_obj in matches:
    print(match_obj.group(), match_obj.start(), match_obj.end()-1)

