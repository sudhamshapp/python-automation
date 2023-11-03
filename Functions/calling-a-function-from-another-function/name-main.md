# my_module.py
def my_function():
    # Some useful function

if __name__ == "__main__":
    # This code will not be executed when imported

# another_script.py
import my_module

my_module.my_function()  # This will execute the function, but not the main code
