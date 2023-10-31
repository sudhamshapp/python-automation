'''
# loops iterate over a block of code
my_list = [1,2,3,4]
for each_item in my_list: # here the 1 is assigned to each_item and gets printed, for loop gonna continue till the list is ended
    print("------------------")
    print(each_item)
    print("This is a Iteration")
    print("__________________")
'''





'''
my_list = [1,2,3,4,5,6]
for each_item in my_list:
    if each_item == 4:
        break
    print(each_item)
# print(each_item)    
'''
'''
for each_char in "Hello":
    print("=================", each_char)
'''

'''
for each_char in "Hello":
    print("=================", each_char)
print("This line is gonna print, after the iteration of for loop, cheers'") # because, it's not the part of for loop, it's outside of for_loop 
'''

my_list = [1,2,3,4,5,6,7,8,9,10]
for each_item in my_list:
    if each_item % 2 == 0: # % denotes the remainder
        print(f"{each_item} is even")
    else:
        print(f"{each_item} is odd")    