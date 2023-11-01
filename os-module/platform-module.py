# write a single pyhton script to clear terminal of any os
# write a platform independant script to clear terminal of any os
import os
import platform
if platform.system() == "Darwin": # for macos
    os.system("clear")
elif platform.system() == "Linux":
    os.system("clear")
else:
    os.system("cls")    
