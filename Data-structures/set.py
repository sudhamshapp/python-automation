# it gonna give us the data from ascending to descending order, sets are unordered collection of data, it gonna remove the duplicates as well
my_random_set = {6,7,8,9,3,4,5,0,2,1,1,2,7}
print(my_random_set)
print(type(my_random_set))
my_set = set({}) # empty set
print(type(my_set))
print(bool(my_set))
print(bool(my_random_set))

my_list = [1,2,3,4,5,6,7,8,9,0]
converssion_from_list_to_set = set(my_list)
print(converssion_from_list_to_set)
print(type(converssion_from_list_to_set))


# discloses the methods that are present in set 
print(dir(set))

a = {1,2,3,4,5}
b = {4,5,6,7,8}
print(a.union(b))
print(a.intersection(b))