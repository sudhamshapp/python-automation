'''
# the number columns in a mac terminal can be find using tput cols, for mac it's 137 columns
given_string = input("Enter the string: ")
print(given_string.center(137))
print(given_string.ljust(137)) # left just gonna adjust the desired string to the left side of terminal
print(given_string.rjust(137))
'''
'''
import os
print(os.get_terminal_size())
print(os.get_terminal_size().columns)
print(os.get_terminal_size().lines)
'''

# Now it's a platform independent script
import os
number_of_columns = os.get_terminal_size().columns
given_string = input("Enter the string: ")
print(given_string.center(number_of_columns).title())
print(given_string.ljust(number_of_columns).title())
print(given_string.rjust(number_of_columns).title())

