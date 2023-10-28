'''
# Read a number and increment it by 10
def get_result(arbitary):
    result = arbitary + 10
    print(f"your result is: {result}")
    return None
def main():
    # global num
    num = eval(input("Enter a number: "))
    get_result(num) # from here we're passing the value of num to the function, but not the variable
    return None
main()
'''

def get_add(p, q):
    aresult = p + q
    print(f"your result is: {aresult}")
    return None
def get_sub(m, n):
    sresult = m - n
    print(f"your result is: {sresult}")
    return None

def main():
    a = eval(input("Enter a number: "))
    b = eval(input("Enter a number: "))
    get_add(a, b) # here we're passing the value of a and b to the function, not the a and b
    get_sub(a, b)
    return None
main()