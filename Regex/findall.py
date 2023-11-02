'''
import re
text = "This is pyhton and it is to learn"
pattern = "is"
# pattern = "i[st]"
result = re.findall(pattern,text)
print(result)
'''

'''
import re
text = "This is pyhton and it is to learn"
pattern = "[abcd]" # can be written as [a-d]
# pattern = "i[st]"
result = re.findall(pattern,text)
print(result)
'''
'''
import re
text = "This is pyhton and it is to learn"
# pattern = "\w"
# pattern = "\w\w"
# pattern = "\w\w\w"
# pattern = "\w\w\w\w"
pattern = "\w\w\w\w\w"
result = re.findall(pattern,text)
print(result)
'''
'''
import re
text = "Sudh@ms$1756_happened-in-india."
pattern = "\W"
result = re.findall(pattern,text)
print(result)
'''

'''
import re
text = "we have the couple of versions, python2 and python3"
pattern = "python\d"
result = re.findall(pattern,text)
print(result)
'''
'''
import re
text = "1, 33, 22, 44, 56, 78, 43, 2, 18"
pattern = "\d\d"
result = re.findall(pattern,text)
print(result)
'''

'''
import re
text = "This is pyhton and it is to learn"
# pattern = "."
# pattern = "."
pattern = "..."
result = re.findall(pattern,text)
print(result)
'''
'''
import re
text = "This is pyhton and it is to learn."
pattern = "\."
result = re.findall(pattern,text)
print(result)
'''
'''
import re
text = "This is the ip of a my-dbserver: 255:333:444:111"
pattern = "\d\d\d.\d\d\d.\d\d\d.\d\d\d"
result = re.findall(pattern,text)
print(result)
'''

'''
import re
text = "This is the ip of a my-dbserver: 255:333:444:111 12345678908765432"
pattern = "\w\w\w.\w\w\w.\w\w\w.\w\w\w"
result = re.findall(pattern,text)
print(result)
'''


'''
import re
text = "This is the ip of a my-dbserver: 255.333.444.111 12345678908765432"
pattern = "\d\d\d\.\d\d\d\.\d\d\d\.\d\d\d"
result = re.findall(pattern,text)
print(result)
'''

'''
import re
# text = "it is the beginning of career"
text = "is the beginning of career"
pattern = "^i[ts]" # cap(^) gonna retrieve matching string in a given string
result = re.findall(pattern,text)
print(result)
'''
'''
import re
text = "it is the beginning of career, career"
pattern = "career$" # $ gonna retrieve matching string at the end of a given string
result = re.findall(pattern,text)
print(result)
'''

'''
import re
text = "it is the beginning of career, career"
# pattern = "\\bcareer" # searches a desired string spaces before it
# pattern = r"\bcareer" # r is a raw string which skips special characters
pattern = r"\bcareer\b"
result = re.findall(pattern,text)
print(result)
'''
'''
import re
text = "it is the beginning of iscareeris, career"
pattern = r"\Bcareer\B"
result = re.findall(pattern,text)
print(result)
'''

'''
import re
text = "This is a pythonnnnn and python"
pattern = r"python{4}"
result = re.findall(pattern,text)
print(result)
'''

'''
import re
text = "This is a pythonnnnn and python aaaa hakjcsadj xyzssssssss"
# pattern = r"xyzs{8}"
pattern = r"\bxyzs{8}\b"
result = re.findall(pattern,text)
print(result)
'''


import re
text = "xyz xyzsssssssssz xyzssssz xyzsssssz xyzs"
# pattern = r"\bxyzs{1,8}z\b"
# pattern = r"\bxyzs{2,}z\b"
# pattern = r"\bxyzs{1,}z\b"
# pattern = r"\bxyzs+z\b"
# pattern = r"\bxyzs*z\b"
pattern = r"\bxyzs?z\b"
result = re.findall(pattern,text)
print(result)



















