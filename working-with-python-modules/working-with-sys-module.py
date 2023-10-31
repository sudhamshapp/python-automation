# sys module is used to run with python runtime environment, helps interact with interpreter, works completely regarding the python interpreter
import sys
# print(dir(sys))
# print(help(sys))
print(sys.platform) # if it's a variable no need of paranthesis, if it's a function then need paranthesis
print(sys.version)
# print(sys.modules)
print(sys.path) # its kinda echo $PATH on linux/mac, sys.path is a environmental variable for python

sys.exit() # stops the python runtime environment, abrupt the python script
print("hello") # it won't get executed because of sys.exit()