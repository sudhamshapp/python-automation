# raise Exception("This is a exception")
# raise NameError("variable isn't defined")
'''
age = 20
if age > 30:
    print("valid age")
else:
    # raise Exception("invalid age")
    # raise NameError("variable isn't defined")
    # raise TypeError("invalid age")
    raise ValueError("invalid age")
    # raise ZeroDivisionError("invalid age")
    # raise ArithmeticError("invalid age")
    # raise MemoryError("invalid age")
    # raise EOFError("invalid age")
    # raise ImportError("invalid age")
    # raise LookupError("invalid age")
    # raise RuntimeError("invalid age")
    # raise NotImplementedError("invalid age")
    # raise SystemError("invalid age")
    # raise TimeoutError("invalid age")
    # raise ReferenceError("invalid age")
    # raise SyntaxError("invalid age")
    # raise IndentationError("invalid age")
    # raise KeyError("invalid age")
    # raise AttributeError("invalid age")
    # raise NameError("invalid age")
    # raise TypeError("invalid age")
    # raise ValueError("invalid age")
    # raise ZeroDivisionError("invalid age")
    # raise ArithmeticError("invalid age")
    # raise MemoryError("invalid age")
    # raise EOFError("invalid age")
'''


# assert 4>3
# assert 4<3

age = 20
try:
    assert age > 30
    print("valid age")
except AssertionError as e:
    print(e)
except Exception as e:
    print(e)    