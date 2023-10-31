'''
# range(start, stop, step)
print(range(8)) # gonna give us a tuple
print(list(range(8))) # gonna give us a list
print(list(range(0, 5, 1))) # gonna give the default output
print(list(range(0, 20, 1))) # gonna give the default output
print(list(range(0, 20, 2))) # gonna give the different output with difference of 2 
'''

my_list = [1, 2, 3, 4, 5]
for each_item in range(len(my_list)):
    print(f"index--->{each_item}: value-->{my_list[each_item]}")