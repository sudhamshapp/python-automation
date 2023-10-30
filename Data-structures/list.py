'''
# discloses the methods in the list, lists are mutable(can be changed)
print(dir(list))
my_list = []
print(type(my_list))
print(bool(my_list))
my_list_wit_proper_stuff = [1, 2, 3, "sudhamsh", 4.4, 3+4j]
print(bool(my_list_wit_proper_stuff))
print(my_list_wit_proper_stuff[0])
print(my_list_wit_proper_stuff[3][0]) #gives the first letter of the string from the third index
print(my_list_wit_proper_stuff[-1])
print(my_list_wit_proper_stuff[0:4]) # 0 includes the first index and 4 excludes the last index (4 - 0 = 4)
print(my_list_wit_proper_stuff[:]) # gives the entire list
print(my_list_wit_proper_stuff[0:]) # gives the entire list
my_list_wit_proper_stuff[0] = "ashridh"
print(my_list_wit_proper_stuff)
'''
'''
a = [1,2,3,4,5]
print(a.index(5)) # gives the index position of 5, if there are multiple values like 5, we can use the regex(regular expressions)
print(a.count(5)) # gives the count of the value 5
a.reverse() # reverses the list
print(a)
a.clear() # modification should be done like this, don't use print statement while modifying, it won't gonna work
print(a)
'''

'''
my_list = [1,2,3,4,5]
print(id(my_list)) # standard memory location
my_dummy_list = my_list # here we are copying the memory location of my_list to my_dummy_list
print(id(my_dummy_list))
my_new_list = my_list.copy() # after applying the copy method we gonna get the new memory location
print(my_new_list)
print(id(my_new_list))
'''
'''
my_list = [1,2,3,4,5]
my_list.append(18) # gonna add at the end of the list
print(my_list)
my_list.insert(2, "ashridh") # gonna add at the specified index
print(my_list)
'''
'''
my_list = [1,2,3,4,5]
my_new_list = [2,3,4]
my_list.append(my_new_list) # gonna add the list in the list
print(my_list)
'''
'''
my_list = [1,2,3,4,5]
my_new_list = [2,3,4]
my_list.extend(my_new_list) # extend gonna give us ordinary list
print(my_list)
'''
'''
my_list = [1,2,3,4,5]
my_list.pop() # gonna remove the last element
my_list.pop(0) # gonna remove the first element
print(my_list)
'''
'''
my_list = [1,2,3,4,5]
my_list.remove(4) # gonna remove the specified element
print(my_list)
'''


'''
my_list = [5,4,3,2,1]
my_list.sort() # sorts the list in ascending order
print(my_list)
my_list.reverse() # sorts the list in descending order
print(my_list)
'''