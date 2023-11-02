# print(a) - NameError
# print("sudhamsh" + 4) - TypeError
# open("dummy.txt", "r") - FileNotFoundError
# print(5/0) - ZeroDivisionError
# import fabric - ModuleNotFoundError

'''
# what else if I donno the exception,  we can proceed like this
try:
    print(a)
except Exception as e:
    print(e)
'''




# This is syntax if I Know the exception before hand
try:
    # print(a)
    # print("sudhamsh" + 4)
    # print(4/0)
    # open("dummy.txt", "r")
    import fabric
except NameError as e:
    print("Variable is not defined")  
except TypeError as e:
    print("string and integer can't be concatenated")
except FileNotFoundError as e:
    print("File not found")
except ZeroDivisionError as e:
    print("Can't divide by zero")
except ModuleNotFoundError as e:
    print("Module not found")    
except Exception as e:
    print(e)
finally:
    print("This gonna execute regardless of the try and except block")                  