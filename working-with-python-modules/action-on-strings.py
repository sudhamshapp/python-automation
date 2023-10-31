'''
# this script gonna need two inputs
user_string = input("enter the string: ")
user_action = input("enter your action on string (valid actions are: lower/upper/title: )")
if user_action == "lower":
    print(user_string.lower())
elif user_action == "upper":
    print(user_string.upper())
elif user_action == "title":
    print(user_string.title())
else:
    print("invalid action")            
'''
# python3 action-on-strings.py "python scripting" upper
import sys
if len(sys.argv) != 3:
    print("invalid arguments")
    sys.exit() # this will exit the program after printing the error message
user_string = sys.argv[1] # it gonna get input from command line as "python scripting"
user_action = sys.argv[2] # it gonna get input from command line as title
if user_action == "lower":
    print(user_string.lower())
elif user_action == "upper":
    print(user_string.upper())
elif user_action == "title":
    print(user_string.title())
else:
    print("invalid action")            
