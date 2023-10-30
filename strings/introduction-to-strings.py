'''
# string is a sequence of characters
my_name = 'sudhamsh'
my_pet_name = "mars"
association = """mars is one of the humble dogs
i have seen ever"""
print(f"{my_name}\n and \n{my_pet_name} {association}")
'''
'''
a = "sudhamsh"
print(len(a))
print(a[0])
print(a[-1])
print(a[0:8])
print(a[1:8])
'''

'''
# strings are immutable, which means element of a string cannot be changed once it has been assigned. we can simply reassign different to the same name
b = "mars"
b[0] = "w" # 'str' object does not support item assignment - it throws an error
del b[0] # 'str' object doesn't support item deletion - it throws an error, we need to delete the entire string
b = "wars"
print(b)
'''

'''
# string concatenation
a = "sudhamsh's"
b= "pet"
c = a+" "+b 
print(c)    
'''