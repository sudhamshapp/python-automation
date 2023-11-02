'''
print("welcome to exception concept")
try:
    print(10/0)
except:
    print("exception occured")    
'''
'''
def file():
    try:
        fo = open("dummy.txt","r")
        print(fo.read())
        fo.close()
    except Exception as e:
        print(e)
file()    
'''
'''
try:
    fo = open("dummy.txt","r")
    print(fo.read())
    fo.close()
except Exception as e:
    print(e)
'''


try:
    my_list = [1,2,3,4,5]
    print(my_list[8])
except Exception as e:
    print(e)
print("This code also gonna execute")    