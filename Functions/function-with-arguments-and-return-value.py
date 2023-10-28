'''
def get_add(p, q): # these are positional arguments #3(this function is called by main() and returns the value to the main())
    result = p + q
    return result # for the calling function i.e., main() we send the value of it, not the variable
def main():
    a = eval(input("enter the first number: ")) #1
    b = eval(input("enter the second number: ")) #2
    arbitary = get_add(a, b) #these are arguments #4, the value of result from get_add() is sent here
    print(f"the addition of {a} and {b} is {arbitary}")
    return None
main()
'''

def multiply(x):
    result = x * 10
    return result
def main():
    y = eval(input("enter a number: "))
    sudhamsh = multiply(y) # the value of result gets assigned here
    print(f"the result is: {sudhamsh}")
    return None
main()
