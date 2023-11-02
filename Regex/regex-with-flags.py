'''
import re
text = "this is a string, ThIs is a new string THIS"
pattern = r"this"
# result = re.findall(pattern, text, re.IGNORECASE)
result = re.findall(pattern, text)
print(result)   
'''

import re
text = """this is a string end 
ThIs is a new End
string THIS"""
# pattern = r"^this"
pattern = r'end$'
result = re.findall(pattern, text, re.MULTILINE|re.IGNORECASE)
print(result)   