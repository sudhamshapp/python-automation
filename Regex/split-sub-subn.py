'''
# using split
import re
# print(help(re.split))
text = "This is python tutorial, there are couple of versions of python2 and Python3"
pattern = r"python[23]?"
# flags=re.I gonna pick the case-sensitive as well like capital P and maxsplit gonna split at desired number from left to right
result = re.split(pattern, text, maxsplit=0, flags=re.I) 
print(result)
'''

'''
# using sub
import re
# print(help(re.sub))
text = "This is python tutorial, there are couple of versions of python2 and Python3"
pattern = r"python[23]?"
result = re.sub(pattern, "java", text, count=0, flags=re.I) 
print(result)
'''

# using subn
import re
# print(help(re.sub))
text = "This is python tutorial, there are couple of versions of python2 and Python3"
pattern = r"python[23]?"
result = re.subn(pattern, "java", text, count=0, flags=re.I) #subn gonna give us how many times a matched pattern is replaced in  a given string
print(result)

