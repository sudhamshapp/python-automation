import datetime
# import pytz
# print(dir(datetime))
# print(dir(datetime.datetime)) 
# print(datetime.datetime.now()) # we can use single datetime like from datetime import datetime
# print(datetime.datetime.now().year)
# print(datetime.datetime.now().month)
# print(datetime.datetime.now().day)
# print(datetime.datetime.now().hour)
# print(datetime.datetime.now().minute)
# print(datetime.datetime.now().second)
# print(datetime.datetime.today())
print(datetime.datetime.now().strftime("%y-%m-%d"))
print(datetime.datetime.now().strftime("%Y-%m-%d"))
print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
print(datetime.datetime.now().fromtimestamp(1555555))

# ist = pytz.timezone('Asia/Kolkata')
# print(datetime.datetime.now(ist)) # gives based on timezone
# print(type(ist)) # this gonna give us a class object, and keep this in the now submodule of datetime submodule