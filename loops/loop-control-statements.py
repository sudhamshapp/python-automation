'''
# stops the iterations in a loop when condition is met
my_list = [1, 2, 3, 4, 5]
for each_item in my_list:
    break
    print(each_item)
print('after for loop')    
'''
'''
my_list = [1, 2, 3, 4, 5]
for each_item in my_list:
    print(each_item)
    if each_item == 3:
        break
        print(each_item)
print('after for loop')    
'''
'''
paths = ["/usr/bin", "/usr/bin/httpd", "/usr/bin/sudhamsh"]
for each_path in paths:
    print(each_path)
    if each_path.endswith('/httpd'):
        break
        print(each_path)
'''

'''
cnt = 0
while True:
    print(cnt)
    cnt += 1
    if cnt == 5:
        break
print(cnt)    
'''
'''
my_range = range(1, 11)
for each_value in my_range:
    print(each_value)
    if each_value != 8:
        # print("printing you number")
        continue # continue gonna skip the block of statements beneath it
        print("'it won't gonna execute because of continue")

'''

'''
if True:
    pass
'''


if True: # if there is nothing beneath the if block, it gonna throw us a error, that's why we should keep the pass keyword for time being
    