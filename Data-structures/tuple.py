# tuple object doesn't support item assignment, we can modify the entire string, but we can't modify part of the string, tuple is immutable
'''
print(dir(tuple)) # discloses the objects and methods in tuple
my_tuple = (1,2,3) # non-empty tuple
print(type(my_tuple))
print(bool(my_tuple))
'''

'''
my_tuple = (1,2,3, [4,5,6,7,8],8)
print(my_tuple[3][0])
'''
my_tuple = (1,1,2,3,4,5,6)
print(my_tuple.count(1)) # tells the occurence of 1 in the tuple
print(my_tuple.index(4)) # tells the index of 4 in the tuple

x = 5, # it gonna be a tuple data structure
print(x, type(x))