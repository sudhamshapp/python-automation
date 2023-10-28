def display(x=1): #here x is the positional argument 
    print(x)
    return None
display(18)
display(10)
display()

def add_numbers(a=4, b=2):
    c=a+b
    print (c)
    return None
add_numbers(4,5)
add_numbers(10)
add_numbers()

def dummy(user="root"):
    print(f"working with the {user}")
    return None
dummy()
dummy("sudhamsh")