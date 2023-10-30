# we can use any of the operations of python to create a condition for if and elif
import os
number_of_columns = os.get_terminal_size().columns
given_string = input("Enter the string: ")
print(given_string)
usr_conformation = input("Do you want to align the string? (Y/N): ")
if usr_conformation == 'yes':
    print(given_string.center(number_of_columns).title())
    print(given_string.ljust(number_of_columns).title())
    print(given_string.rjust(number_of_columns).title())
else:
    print("you can't able to assign the test")