# dictionary is a ordered collection
'''
my_dict = {}
print(bool(my_dict))
print(type(my_dict))
'''

'''
print(dir(dict))
my_dict = {'name':'sudhamsh', 'age':23}
print(my_dict['name'])
print(my_dict.get('age'))
my_dict.clear() # gives the empty dictionary
print(my_dict)
'''

'''
my_dict = {'name':'sudhamsh', 'age':23}
my_dict['weight'] = 60
print(my_dict)
'''
'''
my_dict = {'name':'sudhamsh', 'age':23}
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())
my_dict1 = my_dict.copy()
print(my_dict1)
'''
'''
my_dict1 = {'pet':'mars', 'age':10}
my_dict = {'name':'sudhamsh', 'age':23}
my_dict1.update(my_dict) # update helps appending two different dictionaries
print(my_dict1)
'''
'''
my_dict = {'name':'sudhamsh', 'age':23}
my_dict.pop('age')
print(my_dict)
my_dict.popitem()
print(my_dict)
'''

