# os.system() - gonna execute os commands
# os.system gonna give us the return code 0 if it's a success
import os
import time
print(os.system("pwd"))
print(os.system("ls -ltra"))
time.sleep(5)
print(os.system("clear"))