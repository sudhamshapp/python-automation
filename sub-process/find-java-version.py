import subprocess
# print(dir(subprocess.Popen))
cmd  = "java -version"
sp = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE, universal_newlines= True)
rc = sp.wait()
o, e = sp.communicate()
if rc == 0:
    if bool(o) == True: # I think this block isn't necessary  
        print(o)
    '''
    if bool(o) == False and bool(e) == True:
        print(e.splitlines()[0].split()[2].strip("\""))    
    '''
    if bool(o) == False: # instead of these lines we can use and operator as above
        if bool(e) == True:
            print(e.splitlines()[0].split()[2].strip("\""))
else:
    print("java is not installed")
    print(e)    