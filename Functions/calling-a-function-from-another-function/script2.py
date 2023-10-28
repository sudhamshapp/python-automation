'''
import script1
# print(dir(script1)) - helps us know what are the functions that are residing in the script1
def multiplication(e, f):
    print(f"the multiplication of {e} and {f} is {e * f}")
    return None
def main():
    x = 20
    y = 30
    script1.addition(x, y)
    script1.subtraction(x, y)
    multiplication(x, y)
    return None
if __name__ == "__main__":
    main() # it avoids execution of main block while it's invoked from another file
'''
import script1 # it won't gonna invoke the main() function in script1.py because of if __script1__!=__main__where it won't gonna call the main(), just try print(__name__) in a empty file, it gives us __main__
print("this is from script2:", __name__) # whenever if we run the script directly __name__ variable is __main__