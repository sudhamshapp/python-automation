'''
import re
text = "There is a python installed on a machine, we can switch b/w python2 and Python3"
pattern = r"\bpython[23]?\b"
matches = re.findall(pattern, text, flags=re.IGNORECASE)
matches1 = re.search(pattern, text, flags=re.IGNORECASE)
matches2 = re.match(pattern, text, flags=re.IGNORECASE)
print(matches)
'''

import re
text = "There is a python installed on a machine, we can switch b/w python2 and Python3"
pattern = r"\bpython[23]?\b"
pattern_object = re.compile(pattern, flags=re.IGNORECASE)
print(pattern_object.findall(text))

