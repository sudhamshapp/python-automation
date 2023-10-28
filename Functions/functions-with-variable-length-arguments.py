def dummy(*args): # it gonna give us a tuple data-type
    # print(args)
    for each in args:
        print(type(each))
    return None
dummy(55,6)
dummy(55,6,7,8)
dummy()