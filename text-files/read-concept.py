'''
fo = open("dummy.txt", "r")
content_in_file = fo.read()
fo.close()
print(content_in_file)
'''
'''
fo = open("dummy.txt", "r")
print(fo.readline()) # reads first line
print(fo.readline()) # reads second line
fo.close()
'''

fo = open("dummy.txt", "r")
data = fo.readlines()
fo.close()
for each_line in range(5):
    print(data[each_line])
# print(data)
