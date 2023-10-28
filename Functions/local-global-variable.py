def sudhamsh():
    x = 2
    print(x)
    mars(x) # while passing it's argument
    return None

def mars(y): # while calling it's argument
    y = 3
    print(y)
    return None
def main():
    # global x
    x = 5
    sudhamsh()
    return None
main()
