'''
my_string = "sudhamsh is mastering devops"
# print("\n".join(my_string)) # it gonna give the same ouput
for each_char in my_string:
    print(each_char)
'''
'''
my_list = [1,2,3,4,5,6,7,8,9,10]
for each_num in my_list:
    print(each_num)    
'''
'''
my_list = [(1, 2), [3, 4], (5, 6)] # it gonna same for list and tuple
for f, s in my_list:
    print(f)
    print(s)
'''
'''
my_dict = {"name": "sudhamsh", "age": "25"}
for each_key in my_dict.keys():
    print(each_key)
my_dict = {"name": "sudhamsh", "age": "25"}
for each_key in my_dict.values():
    print(each_key)
my_dict = {"name": "sudhamsh", "age": "25"}
for each_key in my_dict.items(): # gonna give us a tuple
    print(each_key)
'''

my_dict = {"name": "sudhamsh", "age": "25"}
for key, value in my_dict.items(): # gonna give us a tuple
    print(key, value)


