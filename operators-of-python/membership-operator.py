a = [1,2,3,4,5,6]
b = [7,8,9,10,11]
c = a in b
print(c)

valid_java = [1.1, 2.1, 3.1, 4.1, 5.1]
host_java = [1.3]
if host_java in valid_java: # here in is the membership operator
    print("valid")
else:
    print("invalid")    

valid_java = [1.1, 2.1, 3.1, 4.1, 5.1]
host_java = [1.3]
if host_java not in valid_java: # here not in is the membership operator
    print("valid")
else:
    print("invalid")    