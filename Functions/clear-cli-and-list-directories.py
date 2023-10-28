# it's platform independant script gonna execute on windows as well as linux kinda systems
import os
# print(dir(os)) - gives us the methods
import time
import platform
def mycode(cmd1, cmd2):
    print("please wait, cleanig the cli")
    time.sleep(2)
    os.system(cmd1)
    print("finding the list of directories and files")
    time.sleep(2)
    os.system(cmd2)
    return None
if platform.system() == "Windows":
    mycode("cls", "dir")
else:
    mycode("clear", "ls -ltra")

# platform_name = platform.system() - here platform is the module and system is the method, method can be null() as well as accepts the arguments(a, b)
# print(platform_name)    
