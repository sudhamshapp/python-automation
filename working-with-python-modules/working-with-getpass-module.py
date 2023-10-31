# getpass() and getpassuser()
# getpass is like input keyword, where input echos, but getpass won't
import getpass
print(dir(getpass))
db_password = getpass.getpass()
# db_password = getpass.getpass(prompt="enter your db-password")
print(db_password)
# print(getpass.getuser())


# env | grep mars - in mac/linux we gonna search like this, using the python we search using the following statements
system_user = getpass.getuser()
print(f"it gonna print the system's user - {system_user}")